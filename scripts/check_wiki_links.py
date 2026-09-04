#!/usr/bin/env python3
"""Fast source-level link checker for the wiki and course wiki (no build).

Validates, straight from the Markdown sources, that internal wiki and
course-wiki references resolve to a real page:

- body links of the form ``/wiki/<slug>/`` and ``/course-wiki/<slug>/``
  (also inside ``{{ '...' | relative_url }}``)
- ``related`` / ``related_wiki`` frontmatter titles, which the article layout
  renders as ``/<collection>/<title | slugify>/``

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
COURSE_WIKI = ROOT / "_course_wiki"
# Collections/pages whose bodies may link to /wiki/ or /course-wiki/ pages
# and must not go dead.
LINK_SOURCE_DIRS = ["_wiki", "_course_wiki", "_people", "_podcast_summaries", "_books"]

WIKI_URL_RE = re.compile(r"/wiki/([a-z0-9][a-z0-9-]*)/")
COURSE_WIKI_URL_RE = re.compile(r"/course-wiki/([a-z0-9][a-z0-9-]*)/")
LIST_KEY_RE = re.compile(r"^(related|related_wiki|related_course)\s*:\s*$")
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
    wiki_pages = [p for p in sorted(WIKI.glob("*.md")) if p.name != "README.md"]
    course_pages = [p for p in sorted(COURSE_WIKI.glob("*.md")) if p.name != "README.md"]
    wiki_slugs = {p.stem for p in wiki_pages}
    course_slugs = {p.stem for p in course_pages}
    valid_slugs = wiki_slugs | course_slugs

    # Every page (across collections) whose internal links must resolve.
    link_pages: list[Path] = []
    for directory in LINK_SOURCE_DIRS:
        d = ROOT / directory
        if d.exists():
            link_pages += [p for p in sorted(d.glob("*.md")) if p.name != "README.md"]

    failures: list[str] = []
    checked = 0

    for path in link_pages:
        raw = path.read_text(encoding="utf-8")
        fm_lines, body = split_frontmatter(raw)
        rel = path.relative_to(ROOT)

        # body /wiki/<slug>/ and /course-wiki/<slug>/ links (any collection)
        for slug in WIKI_URL_RE.findall(body):
            checked += 1
            if slug not in wiki_slugs:
                failures.append(f"{rel}: body link /wiki/{slug}/ -> missing page")

        for slug in COURSE_WIKI_URL_RE.findall(body):
            checked += 1
            if slug not in course_slugs:
                failures.append(f"{rel}: body link /course-wiki/{slug}/ -> missing page")

        # related / related_wiki frontmatter titles
        in_list = False
        current_key = ""
        for line in fm_lines:
            key_match = LIST_KEY_RE.match(line)
            if key_match:
                in_list = True
                current_key = key_match.group(1)
                continue
            item = LIST_ITEM_RE.match(line)
            if in_list and item:
                title = item.group(1)
                if not title:
                    continue
                slug = slugify(title)
                checked += 1
                if current_key == "related_course":
                    if slug not in course_slugs:
                        failures.append(
                            f"{rel}: related_course '{title}' -> missing course-wiki page"
                        )
                elif slug not in valid_slugs:
                    failures.append(
                        f"{rel}: related '{title}' -> missing wiki or course-wiki page"
                    )
                continue
            if line.strip() and not line.startswith((" ", "\t")):
                in_list = False
                current_key = ""

    if failures:
        print(f"wiki link check FAILED: {len(failures)} dead references")
        for f in failures:
            print(f"- {f}")
        return 1
    print(f"wiki link check passed: {checked} internal references, "
          f"{len(link_pages)} pages across {len(LINK_SOURCE_DIRS)} collections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
