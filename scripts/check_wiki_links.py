#!/usr/bin/env python3
"""Fast source-level link checker for the tagged wiki (no build required).

Validates, straight from the Markdown sources, that internal wiki references
resolve to a real page:

- body links of the form ``/wiki/<slug>/`` (also inside ``{{ '...' | relative_url }}``)
- ``related`` / ``related_wiki`` frontmatter titles, which the article layout
  renders as ``/wiki/<title | slugify>/``

Because the site is now tags-only with no redirects, any reference to a missing
or removed slug is a dead link. Exits non-zero and lists every dead reference.

For full rendered-HTML coverage (anchors, nav, generated pages) run
``make links`` (build + scripts/check_links.py). This script is the quick
pre-build gate.

Usage:
    python scripts/check_wiki_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "_wiki"

WIKI_URL_RE = re.compile(r"/wiki/([a-z0-9][a-z0-9-]*)/")
LIST_KEY_RE = re.compile(r"^(related|related_wiki)\s*:\s*$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.*?)\s*$")


def slugify(value: str) -> str:
    """Match Jekyll's default slugify used by the article layout."""
    value = value.strip().strip('"').strip("'").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def split_frontmatter(raw: str) -> tuple[list[str], str]:
    if not raw.startswith("---\n"):
        return [], raw
    end = raw.find("\n---", 4)
    if end == -1:
        return [], raw
    return raw[4:end].splitlines(), raw[end + 4:]


def main() -> int:
    pages = [p for p in sorted(WIKI.glob("*.md")) if p.name != "README.md"]
    valid_slugs = {p.stem for p in pages}

    failures: list[str] = []
    checked = 0

    for path in pages:
        raw = path.read_text(encoding="utf-8")
        fm_lines, body = split_frontmatter(raw)

        # body /wiki/<slug>/ links
        for slug in WIKI_URL_RE.findall(body):
            checked += 1
            if slug not in valid_slugs:
                failures.append(f"{path.name}: body link /wiki/{slug}/ -> missing page")

        # related / related_wiki frontmatter titles
        in_list = False
        for line in fm_lines:
            if LIST_KEY_RE.match(line):
                in_list = True
                continue
            item = LIST_ITEM_RE.match(line)
            if in_list and item:
                title = item.group(1)
                if not title:
                    continue
                slug = slugify(title)
                checked += 1
                if slug not in valid_slugs:
                    failures.append(
                        f"{path.name}: related '{title}' -> /wiki/{slug}/ missing page"
                    )
                continue
            if line.strip() and not line.startswith((" ", "\t")):
                in_list = False

    if failures:
        print(f"wiki link check FAILED: {len(failures)} dead references")
        for f in failures:
            print(f"- {f}")
        return 1
    print(f"wiki link check passed: {checked} internal references, {len(pages)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
