#!/usr/bin/env python3
"""Rewrite old split-collection URLs to /wiki/ for migrated content.

This is a cleanup helper only. The site no longer keeps redirect stubs or
public split-collection pages.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ["_wiki", "_podcast_summaries", "_people", "_books"]

MAPPING = {
    "/guides/": "/wiki/",
    "/comparisons/": "/wiki/",
    "/roadmaps/": "/wiki/",
    "/how-tos/": "/wiki/",
}

# Don't rewrite these collection index pages
INDEX_PAGES = {"/guides/", "/comparisons/", "/roadmaps/", "/how-tos/"}


def rewrite_links(text: str) -> tuple[str, int]:
    count = 0

    def replace(m: re.Match) -> str:
        nonlocal count
        full = m.group(0)
        prefix = m.group(1)  # /guides/ etc
        slug = m.group(2)    # the slug
        trailing = m.group(3)  # / or nothing

        if f"{prefix}{slug}{trailing}" in INDEX_PAGES and slug == "":
            return full

        new_prefix = MAPPING.get(prefix, prefix)
        count += 1
        return f"{new_prefix}{slug}{trailing}"

    # Match patterns like /guides/slug/ or /guides/slug
    pattern = r'(/(?:guides|comparisons|roadmaps|how-tos)/)([a-z0-9-]+)(/?)'
    text = re.sub(pattern, replace, text)
    return text, count


def main():
    total_changes = 0
    files_changed = 0

    for d in CONTENT_DIRS:
        dir_path = ROOT / d
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            if f.name == "README.md":
                continue
            raw = f.read_text(encoding="utf-8")
            new_text, count = rewrite_links(raw)
            if count > 0:
                f.write_text(new_text, encoding="utf-8")
                total_changes += count
                files_changed += 1
                print(f"  {d}/{f.name}: {count} links")

    print(f"\nDone: {total_changes} links rewritten in {files_changed} files")


if __name__ == "__main__":
    main()
