#!/usr/bin/env python3
"""Find near-duplicate content for SEO focus, using the local Zerosearch index.

Two jobs:

1. Internal wiki dedup: near-duplicate pages *within* podwiki collections
   (`_wiki`, `_guides`, `_comparisons`, `_roadmaps`, `_how_tos`). These compete
   with each other for the same query (keyword cannibalization) and should be
   merged into one focused page.

2. Cross-site cannibalization: podwiki pages that overlap main-site articles in
   `../datatalksclub.github.io/_posts` (and `_tools`). The main site should own
   its branded/article terms; podwiki should trim overlap and link out.

No network, no Lambda: builds a Zerosearch index locally and reads the same
collections `build_search_index.py` indexes.

Usage:
    python scripts/find_duplicates.py                 # both reports, to stdout
    python scripts/find_duplicates.py --internal      # only internal wiki dedup
    python scripts/find_duplicates.py --cross-site    # only cross-site overlap
    python scripts/find_duplicates.py --threshold 8   # min score to report
    python scripts/find_duplicates.py --json out.json # machine-readable dump
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ZEROSEARCH = ROOT.parent / "zerosearch"
if SIBLING_ZEROSEARCH.exists():
    sys.path.insert(0, str(SIBLING_ZEROSEARCH))

from zerosearch import Index  # noqa: E402

# Reuse the exact frontmatter/plaintext parsing the real index uses.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_search_index import plain_text, split_frontmatter  # noqa: E402

MAIN_SITE = ROOT.parent / "datatalksclub.github.io"

# Collections whose pages compete with each other in podwiki.
PODWIKI_COLLECTIONS = {
    "_wiki": ("wiki", "/wiki/"),
    "_guides": ("guide", "/guides/"),
    "_comparisons": ("comparison", "/comparisons/"),
    "_roadmaps": ("roadmap", "/roadmaps/"),
    "_how_tos": ("how_to", "/how-tos/"),
}


@dataclass
class Page:
    id: str
    collection: str
    slug: str
    title: str
    summary: str
    body: str
    path: Path
    url: str = ""
    text: str = field(default="")

    def query_text(self) -> str:
        # Title + summary + first slice of body: enough signal, bounded length.
        return plain_text(" ".join([self.title, self.summary, self.body[:1200]]))


def load_pages(base: Path, collections: dict[str, tuple[str, str]]) -> list[Page]:
    pages: list[Page] = []
    for directory, (level, prefix) in collections.items():
        collection_dir = base / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            if meta.get("redirect_to") or str(meta.get("published", "")).lower() == "false":
                continue
            slug = path.stem
            title = str(meta.get("title") or meta.get("h1") or slug.replace("-", " ").title())
            summary = str(meta.get("summary") or meta.get("description") or "")
            pages.append(
                Page(
                    id=f"{level}:{slug}",
                    collection=level,
                    slug=slug,
                    title=title,
                    summary=summary,
                    body=body,
                    path=path,
                    url=f"{prefix}{slug}/",
                    text=plain_text(" ".join([title, summary, body])),
                )
            )
    return pages


def load_main_posts(base: Path) -> list[Page]:
    pages: list[Page] = []
    posts_dir = base / "_posts"
    tools_dir = base / "_tools"
    for directory, level in ((posts_dir, "article"), (tools_dir, "tool")):
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            slug = path.stem
            title = str(meta.get("h1") or meta.get("title") or slug)
            summary = str(meta.get("description") or "")
            pages.append(
                Page(
                    id=f"{level}:{slug}",
                    collection=level,
                    slug=slug,
                    title=title,
                    summary=summary,
                    body=body,
                    path=path,
                    text=plain_text(" ".join([title, summary, body])),
                )
            )
    return pages


def build_index(pages: list[Page]) -> Index:
    docs = [
        {"id": p.id, "title": p.title, "summary": p.summary, "text": p.text}
        for p in pages
    ]
    index = Index(
        text_fields=["title", "summary", "text"],
        keyword_fields=["id"],
    )
    index.fit(docs)
    return index


def internal_report(pages: list[Page], threshold: float, top_k: int) -> list[dict]:
    index = build_index(pages)
    by_id = {p.id: p for p in pages}
    seen_pairs: set[tuple[str, str]] = set()
    findings: list[dict] = []
    for page in pages:
        results = index.search(
            page.query_text(),
            boost_dict={"title": 3.0, "summary": 2.0, "text": 1.0},
            num_results=top_k + 1,
        )
        for res in results:
            other_id = res["id"]
            if other_id == page.id:
                continue
            pair = tuple(sorted((page.id, other_id)))
            if pair in seen_pairs:
                continue
            score = res["score"]
            if score < threshold:
                continue
            seen_pairs.add(pair)
            other = by_id[other_id]
            findings.append(
                {
                    "score": round(score, 2),
                    "a": {"id": page.id, "title": page.title, "url": page.url,
                          "path": str(page.path.relative_to(ROOT))},
                    "b": {"id": other.id, "title": other.title, "url": other.url,
                          "path": str(other.path.relative_to(ROOT))},
                }
            )
    findings.sort(key=lambda f: f["score"], reverse=True)
    return findings


def cross_site_report(pages: list[Page], posts: list[Page], threshold: float,
                      top_k: int) -> list[dict]:
    index = build_index(posts)
    by_id = {p.id: p for p in posts}
    findings: list[dict] = []
    for page in pages:
        results = index.search(
            page.query_text(),
            boost_dict={"title": 3.0, "summary": 2.0, "text": 1.0},
            num_results=top_k,
        )
        matches = []
        for res in results:
            if res["score"] < threshold:
                continue
            post = by_id[res["id"]]
            matches.append(
                {"score": round(res["score"], 2), "id": post.id,
                 "title": post.title, "path": str(post.path)}
            )
        if matches:
            findings.append(
                {
                    "wiki": {"id": page.id, "title": page.title, "url": page.url,
                             "path": str(page.path.relative_to(ROOT))},
                    "main_matches": matches,
                    "top_score": matches[0]["score"],
                }
            )
    findings.sort(key=lambda f: f["top_score"], reverse=True)
    return findings


def print_internal(findings: list[dict]) -> None:
    print(f"\n=== INTERNAL near-duplicate pairs ({len(findings)}) ===")
    for f in findings:
        print(f"\n[{f['score']}]")
        print(f"  A  {f['a']['path']}  ({f['a']['title']})")
        print(f"  B  {f['b']['path']}  ({f['b']['title']})")


def print_cross(findings: list[dict]) -> None:
    print(f"\n=== CROSS-SITE overlap: podwiki page -> main-site article ({len(findings)}) ===")
    for f in findings:
        print(f"\n{f['wiki']['path']}  ({f['wiki']['title']})  top={f['top_score']}")
        for m in f["main_matches"]:
            print(f"    [{m['score']}] {m['title']}  <- {m['path']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--internal", action="store_true", help="only internal wiki dedup")
    parser.add_argument("--cross-site", action="store_true", help="only cross-site overlap")
    parser.add_argument("--threshold", type=float, default=6.0)
    parser.add_argument("--cross-threshold", type=float, default=5.0)
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    run_internal = args.internal or not args.cross_site
    run_cross = args.cross_site or not args.internal

    pages = load_pages(ROOT, PODWIKI_COLLECTIONS)
    payload: dict[str, object] = {}

    if run_internal:
        internal = internal_report(pages, args.threshold, args.top_k)
        payload["internal"] = internal
        print_internal(internal)

    if run_cross:
        posts = load_main_posts(MAIN_SITE)
        cross = cross_site_report(pages, posts, args.cross_threshold, args.top_k)
        payload["cross_site"] = cross
        print_cross(cross)

    if args.json:
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
