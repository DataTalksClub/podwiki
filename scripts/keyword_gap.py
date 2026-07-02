#!/usr/bin/env python3
"""Cluster an Ubersuggest keyword export and find content gaps to create.

For each keyword it decides, using the local Zerosearch index (no network):

- MAIN     — the main DataTalks.Club site (../datatalksclub.github.io) already
             owns this query (article, course, book, tool, person, or podcast).
             Do NOT create a competing podwiki page (cannibalization).
- COVERED  — an existing podwiki `_wiki/` page already targets it.
- BRAND    — branded/navigational term (zoomcamp, datatalks, slack, course
             signup, "free ... course"). The main site owns these.
- NOISE    — book piracy / download intent (pdf, download, epub, "handbook"
             free copies) — not wiki content.
- GAP      — none of the above: a concept/how-to/role query with search volume
             that podwiki could own without overlapping the main site.

GAP keywords are clustered by shared head tokens and written to a report.

Usage:
    python scripts/keyword_gap.py .tmp/ubersuggest_Current_Queries.csv
    python scripts/keyword_gap.py <csv> --min-volume 30 --out docs/keyword-gaps.md
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ZEROSEARCH = ROOT.parent / "zerosearch"
if SIBLING_ZEROSEARCH.exists():
    sys.path.insert(0, str(SIBLING_ZEROSEARCH))
from zerosearch import Index  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_search_index import plain_text, split_frontmatter  # noqa: E402

MAIN_SITE = ROOT.parent / "datatalksclub.github.io"

BRAND_RE = re.compile(
    r"\b(zoomcamp|datatalks|data talks|dtc|slack community|free .*course|"
    r"free .*courses|sign ?up|discord|meetup)\b"
)
NOISE_RE = re.compile(r"\b(pdf|epub|download|free download|torrent|mobi|drive)\b")
STOP = set(
    "the a an to of and or in for with vs is are how what your you this that "
    "on at by from into can do does using use it its as be best top".split()
)


def toks(s: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if len(t) > 2 and t not in STOP]


def load_collection(base: Path, dirs: list[str], text_from_body=True) -> list[dict]:
    docs = []
    for d in dirs:
        cd = base / d
        if not cd.exists():
            continue
        for p in sorted(cd.glob("*.md")):
            if p.name == "README.md":
                continue
            raw = p.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            if meta.get("redirect_to"):
                continue
            title = str(meta.get("title") or meta.get("h1") or p.stem.replace("-", " "))
            kw = " ".join(
                [str(meta.get("keyword") or "")]
                + (meta.get("secondary_keywords") if isinstance(meta.get("secondary_keywords"), list) else [])
            )
            summary = str(meta.get("summary") or meta.get("description") or "")
            text = plain_text(" ".join([title, kw, summary, body if text_from_body else ""]))
            docs.append({"id": f"{d}:{p.stem}", "title": title, "kw": kw,
                         "summary": summary, "text": text})
    return docs


def build(docs: list[dict]) -> Index:
    idx = Index(text_fields=["title", "kw", "summary", "text"], keyword_fields=["id"])
    idx.fit(docs)
    return idx


def top_score(idx: Index, query: str) -> tuple[float, str]:
    res = idx.search(query, boost_dict={"title": 3.0, "kw": 3.0, "summary": 1.5, "text": 1.0},
                     num_results=1)
    if not res:
        return 0.0, ""
    return res[0]["score"], res[0]["id"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--min-volume", type=int, default=20)
    ap.add_argument("--covered", type=float, default=12.0,
                    help="min podwiki/main top score to count as owned/covered")
    ap.add_argument("--ground", type=float, default=10.0,
                    help="min podcast/book score for a gap to be groundable")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "keyword-gaps.md")
    args = ap.parse_args()

    rows = list(csv.DictReader(args.csv.open(encoding="utf-8-sig")))

    wiki_idx = build(load_collection(ROOT, ["_wiki"]))
    main_idx = build(load_collection(
        MAIN_SITE, ["_posts", "_courses", "_books", "_tools", "_people", "_podcast"]))
    # Grounding sources: what we can actually extract content from — the podcast
    # archive and the book summaries. A gap is only worth creating if grounding
    # exists here.
    book_docs = load_collection(ROOT, ["_books"])
    books_idx = build(book_docs)
    ground_docs = book_docs + load_collection(ROOT, ["_podcast_summaries"])
    ground_docs += load_collection(MAIN_SITE, ["_podcast"])
    ground_idx = build(ground_docs)

    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        kw = r["Keyword"].strip()
        vol = int(r.get("Search Volume") or 0)
        diff = r.get("SEO Difficulty") or ""
        rec = {"kw": kw, "vol": vol, "diff": diff}
        if NOISE_RE.search(kw):
            # download/pdf intent: we never share files, but if the title maps to
            # a book we summarize, a legit "key ideas + author episodes" page can
            # capture that intent. Otherwise it is genuine noise.
            b_score, b_id = top_score(books_idx, kw)
            if b_score >= args.covered:
                rec.update(b=round(b_score, 1), b_id=b_id)
                buckets["BOOK_INTENT"].append(rec)
            else:
                buckets["NOISE"].append(rec)
            continue
        if BRAND_RE.search(kw):
            buckets["BRAND"].append(rec); continue
        w_score, w_id = top_score(wiki_idx, kw)
        m_score, m_id = top_score(main_idx, kw)
        g_score, g_id = top_score(ground_idx, kw)
        rec.update(w=round(w_score, 1), w_id=w_id, m=round(m_score, 1), m_id=m_id,
                   g=round(g_score, 1), g_id=g_id)
        if m_score >= args.covered and m_score >= w_score:
            buckets["MAIN"].append(rec)
        elif w_score >= args.covered:
            buckets["COVERED"].append(rec)
        else:
            buckets["GAP"].append(rec)

    # a gap is only actionable if podcasts/books can ground it
    grounded, ungrounded = [], []
    for g in buckets["GAP"]:
        (grounded if g.get("g", 0) >= args.ground else ungrounded).append(g)
    buckets["GAP_GROUNDED"] = grounded
    buckets["GAP_UNGROUNDED"] = ungrounded

    # cluster grounded GAP keywords (min volume) by dominant token
    gaps = [g for g in grounded if g["vol"] >= args.min_volume]
    clusters: dict[str, list[dict]] = defaultdict(list)
    # priority head tokens to name clusters
    for g in gaps:
        t = toks(g["kw"])
        key = None
        for anchor in ("mlops", "llm", "rag", "agent", "airflow", "kafka", "spark",
                       "dbt", "docker", "kubernetes", "sql", "python", "pandas",
                       "interview", "roadmap", "portfolio", "salary", "resume",
                       "certification", "bootcamp", "embedding", "vector",
                       "fine", "prompt", "transformer", "deployment", "monitoring",
                       "feature", "pipeline", "warehouse", "lakehouse", "streaming"):
            if anchor in " ".join(t):
                key = anchor; break
        if key is None:
            key = t[0] if t else "misc"
        clusters[key].append(g)

    def fmt(recs):
        return "\n".join(
            f"  - {x['kw']}  (vol {x['vol']}, SEO diff {x['diff']}"
            + (f", ground: {x.get('g_id','')}~{x.get('g','')}" if x.get('g') else "") + ")"
            for x in sorted(recs, key=lambda z: -z['vol'])
        )

    def fmt_book(recs):
        return "\n".join(
            f"  - {x['kw']}  (vol {x['vol']}) -> {x.get('b_id','')}"
            for x in sorted(recs, key=lambda z: -z['vol'])
        )

    lines = ["# Keyword Gap Analysis", "",
             f"Source: `{args.csv}` ({len(rows)} keywords). "
             f"Coverage checked with the local Zerosearch index against podwiki "
             f"`_wiki/` and the main site (articles, courses, books, tools, people, "
             f"podcast). GAP = not covered by podwiki AND not owned by the main site.",
             "",
             "How to act on this (see CONTENT_GUIDE.md):",
             "- Only create a page if it is groundable in our podcast/book content "
             "(GAP_GROUNDED). We repurpose what guests and book authors said; we do "
             "not invent.",
             "- Never duplicate a main-site article, course, or book landing page "
             "(MAIN/BRAND/BOOK_INTENT route to the main site).",
             "- BOOK_INTENT (pdf/download) queries: link the intent to the main "
             "site's book page. On the wiki, fold a book author's podcast points "
             "into the relevant TOPIC hub instead of making a competing book page.",
             "- BM25 has no stemming, so singular/plural variants cluster "
             "separately; prefer merging doorway pages over creating new ones.",
             ""]
    for name, desc in [
        ("GAP_GROUNDED", "Gaps to create: podcast/book-groundable, not main-owned"),
        ("GAP_UNGROUNDED", "Gaps with no podcast/book grounding — cannot create here"),
        ("COVERED", "Already covered by a podwiki wiki page"),
        ("MAIN", "Owned by the main website — do NOT duplicate here"),
        ("BRAND", "Branded/navigational — main site owns"),
        ("BOOK_INTENT", "Book download intent that maps to a book we summarize"),
        ("NOISE", "Download intent with no matching book — not wiki content"),
    ]:
        lines.append(f"## {name} — {desc}: {len(buckets[name])}")
        lines.append("")
    if buckets["BOOK_INTENT"]:
        lines.append("### Book-intent opportunities (key-ideas pages, never PDFs)")
        lines.append(fmt_book(buckets["BOOK_INTENT"]))
        lines.append("")
    lines.append("## GAP clusters (min volume "
                 f"{args.min_volume}) — {sum(len(v) for v in clusters.values())} keywords")
    lines.append("")
    for key in sorted(clusters, key=lambda k: -sum(x['vol'] for x in clusters[k])):
        recs = clusters[key]
        vol = sum(x['vol'] for x in recs)
        lines.append(f"### {key}  ({len(recs)} keywords, total vol {vol})")
        lines.append(fmt(recs))
        lines.append("")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("bucket counts:", {k: len(v) for k, v in buckets.items()})
    print(f"gap clusters: {len(clusters)}; wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
