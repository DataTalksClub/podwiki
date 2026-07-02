#!/usr/bin/env python3
"""Merge one wiki page into another with no redirect left behind.

Implements the No-Redirects merge procedure from CONTENT_GUIDE.md: after you have
moved the unique content from the source page into the target page by hand, run
this to rewrite every incoming link and delete the source page.

It rewrites, across all source collections (_wiki, _people, _podcast_summaries,
_books):
  - body links `/wiki/<source-slug>/` -> `/wiki/<target-slug>/`
  - `related` / `related_wiki` frontmatter items whose title slugifies to the
    source slug -> the target's title (de-duplicated within each list)
then deletes `_wiki/<source-slug>.md`.

It refuses to run if the target title does not slugify to the target slug (that
would create a dead `related` link), and it does NOT move body content — do that
first. Run `python scripts/check_wiki_links.py` afterwards.

Usage:
    python scripts/merge_wiki_page.py <source-slug> <target-slug>
    python scripts/merge_wiki_page.py rag retrieval-augmented-generation
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "_wiki"
LINK_SOURCE_DIRS = ["_wiki", "_people", "_podcast_summaries", "_books"]

LIST_KEY_RE = re.compile(r"^(related|related_wiki)\s*:\s*$")
LIST_ITEM_RE = re.compile(r"^(\s+-\s+)(.*?)\s*$")


def slugify(value: str) -> str:
    value = value.strip().strip('"').strip("'").lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def get_title(path: Path) -> str:
    m = re.search(r'^title:\s*"?([^"\n]+?)"?\s*$', path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else path.stem


def split_frontmatter(raw: str) -> tuple[str | None, str]:
    if not raw.startswith("---\n"):
        return None, raw
    end = raw.find("\n---", 4)
    if end == -1:
        return None, raw
    return raw[: end + 1], raw[end + 1:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_slug")
    ap.add_argument("target_slug")
    args = ap.parse_args()

    src = WIKI / f"{args.source_slug}.md"
    tgt = WIKI / f"{args.target_slug}.md"
    if not src.exists():
        print(f"source page not found: {src}", file=sys.stderr)
        return 1
    if not tgt.exists():
        print(f"target page not found: {tgt}", file=sys.stderr)
        return 1

    src_title = get_title(src)
    tgt_title = get_title(tgt)
    if slugify(tgt_title) != args.target_slug:
        print(
            f"refusing: target title {tgt_title!r} slugifies to "
            f"{slugify(tgt_title)!r}, not {args.target_slug!r} — a related link "
            f"to it would be dead. Fix the target title first.",
            file=sys.stderr,
        )
        return 1

    src_norm = args.source_slug
    body_changes = fm_changes = files_touched = 0

    for directory in LINK_SOURCE_DIRS:
        d = ROOT / directory
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            if p == src:
                continue
            raw = p.read_text(encoding="utf-8")
            fm, body = split_frontmatter(raw)
            orig = raw

            # body links
            def repl(m: re.Match) -> str:
                nonlocal body_changes
                if m.group(1) == src_norm:
                    body_changes += 1
                    return f"/wiki/{args.target_slug}/"
                return m.group(0)

            target_body = body if fm is not None else raw
            target_body = re.sub(r"/wiki/([a-z0-9-]+)/", repl, target_body)

            # frontmatter related items
            if fm is not None:
                out, seen, in_list = [], set(), False
                for line in fm.split("\n"):
                    if LIST_KEY_RE.match(line):
                        in_list, seen = True, set()
                        out.append(line)
                        continue
                    item = LIST_ITEM_RE.match(line)
                    if in_list and item:
                        title = item.group(2).strip().strip('"').strip("'")
                        mapped = tgt_title if slugify(title) == src_norm else title
                        key = slugify(mapped)
                        if key in seen:
                            fm_changes += 1
                            continue
                        seen.add(key)
                        if mapped != title:
                            fm_changes += 1
                            out.append(f"{item.group(1)}{mapped}")
                        else:
                            out.append(line)
                        continue
                    if line.strip() and not line.startswith((" ", "\t")):
                        in_list = False
                    out.append(line)
                fm = "\n".join(out)
                raw = fm + target_body
            else:
                raw = target_body

            if raw != orig:
                p.write_text(raw, encoding="utf-8")
                files_touched += 1

    src.unlink()
    print(
        f"merged {args.source_slug} -> {args.target_slug}: "
        f"{body_changes} body links, {fm_changes} related items, "
        f"{files_touched} files touched; deleted {src.relative_to(ROOT)}"
    )
    print("now run: python scripts/check_wiki_links.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
