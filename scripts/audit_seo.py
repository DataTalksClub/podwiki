#!/usr/bin/env python3
"""Report on-page SEO issues in wiki front matter.

Flags the things that quietly hurt SERP presentation:
- <title> that will truncate (title + " | <site.title>" beyond ~60 chars)
- meta descriptions (summary) that truncate (>160) or are too thin (<70)
- missing summaries
- body-level H1 that duplicates the layout's <h1> (two H1s on the page)

Read-only. Exit code 1 if anything is flagged, so it can gate CI if wanted.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "_wiki"

TITLE_SUFFIX = " | DataTalks.Club Podcast Wiki"
TITLE_MAX = 60
DESC_MAX = 160
DESC_MIN = 70


def frontmatter(raw: str) -> dict[str, str]:
    if not raw.startswith("---\n"):
        return {}
    end = raw.find("\n---", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in raw[4:end].splitlines():
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return meta


def body_of(raw: str) -> str:
    if not raw.startswith("---\n"):
        return raw
    end = raw.find("\n---", 4)
    return raw[end + 4:] if end != -1 else raw


def main() -> None:
    long_titles: list[tuple[str, int]] = []
    long_desc: list[tuple[str, int]] = []
    short_desc: list[tuple[str, int]] = []
    missing_desc: list[str] = []
    dup_h1: list[str] = []

    for path in sorted(WIKI_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        raw = path.read_text(encoding="utf-8")
        meta = frontmatter(raw)
        name = path.name
        title = meta.get("title", "")
        full_title_len = len(title) + len(TITLE_SUFFIX)
        if full_title_len > TITLE_MAX:
            long_titles.append((name, full_title_len))

        summary = meta.get("summary", "")
        if not summary:
            missing_desc.append(name)
        elif len(summary) > DESC_MAX:
            long_desc.append((name, len(summary)))
        elif len(summary) < DESC_MIN:
            short_desc.append((name, len(summary)))

        if re.search(r"^# ", body_of(raw), flags=re.M):
            dup_h1.append(name)

    def report(label: str, items: list) -> None:
        print(f"\n{label}: {len(items)}")
        for item in items[:40]:
            if isinstance(item, tuple):
                print(f"  {item[0]}  ({item[1]})")
            else:
                print(f"  {item}")
        if len(items) > 40:
            print(f"  ... and {len(items) - 40} more")

    report(f"Titles over {TITLE_MAX} chars (with site suffix)", long_titles)
    report(f"Descriptions over {DESC_MAX} chars (SERP truncation)", long_desc)
    report(f"Descriptions under {DESC_MIN} chars (too thin)", short_desc)
    report("Missing descriptions", missing_desc)
    report("Body-level H1 duplicating the page title", dup_h1)

    total = len(long_titles) + len(long_desc) + len(short_desc) + len(missing_desc) + len(dup_h1)
    print(f"\nTotal flagged: {total}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
