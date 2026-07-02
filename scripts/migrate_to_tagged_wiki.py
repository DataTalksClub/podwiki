#!/usr/bin/env python3
"""Migrate editorial collections into _wiki/ with tags.

For each page in _guides, _comparisons, _roadmaps, _how_tos:
1. Move content to _wiki/<slug>.md with appropriate tag
2. Leave a redirect stub in the original collection so old URLs resolve
3. Handle slug collisions (redirect stubs get replaced, real wiki pages kept)

After migration, run scripts/update_collection_links.py to rewrite internal
links from /guides/<slug>/ etc. to /wiki/<slug>/.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    "_guides": "guide",
    "_comparisons": "comparison",
    "_roadmaps": "roadmap",
    "_how_tos": "how-to",
}
WIKI = ROOT / "_wiki"

RENAME = {
    "notebook-to-production-ai-systems": "notebook-to-production-workflow",
}

REDIRECT_TMPL = """---
layout: redirect
title: "{title}"
redirect_to: /wiki/{dest_slug}/
sitemap: false
---
"""


def add_tag(fm_text: str, tag: str) -> str:
    if re.search(r"^tags?:", fm_text, re.MULTILINE):
        return fm_text
    lines = fm_text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("layout:"):
            lines.insert(i + 1, f'tags: ["{tag}"]')
            break
    return "\n".join(lines)


def get_title(fm_text: str) -> str:
    m = re.search(r'^title:\s*"?([^"\n]+)"?', fm_text, re.MULTILINE)
    return m.group(1) if m else ""


def migrate():
    moved = 0
    replaced_redirect = 0
    renamed = 0
    skipped = 0

    for collection_dir, tag in COLLECTIONS.items():
        col_path = ROOT / collection_dir
        if not col_path.exists():
            continue

        for src in sorted(col_path.glob("*.md")):
            if src.name == "README.md":
                continue

            raw = src.read_text(encoding="utf-8")
            if not raw.startswith("---\n"):
                print(f"SKIP (no frontmatter): {src.name}")
                skipped += 1
                continue
            fm_end = raw.find("\n---", 4)
            if fm_end == -1:
                print(f"SKIP (no fm end): {src.name}")
                skipped += 1
                continue

            fm_text = raw[4:fm_end]
            body = raw[fm_end + 4 :].lstrip()
            slug = src.stem
            title = get_title(fm_text)
            dest_slug = slug

            # Handle rename for real-content collisions
            if slug in RENAME:
                dest_slug = RENAME[slug]

            dest = WIKI / f"{dest_slug}.md"
            need_redirect = True

            if slug != dest_slug:
                # Renamed: move to new slug, redirect old slug
                new_fm = add_tag(fm_text, tag)
                dest.write_text(f"---\n{new_fm}\n---\n\n{body}\n", encoding="utf-8")
                print(f"RENAME: {collection_dir}/{slug} -> _wiki/{dest_slug} [{tag}]")
                renamed += 1
            elif dest.exists():
                existing = dest.read_text(encoding="utf-8")
                if "layout: redirect" in existing or "redirect_to:" in existing:
                    new_fm = add_tag(fm_text, tag)
                    dest.write_text(f"---\n{new_fm}\n---\n\n{body}\n", encoding="utf-8")
                    print(f"REPLACE_REDIRECT: {collection_dir}/{slug} -> _wiki/{slug} [{tag}]")
                    replaced_redirect += 1
                else:
                    # Real content collision, keep wiki version
                    # Still leave redirect from collection URL to wiki
                    print(f"KEEP_WIKI: {collection_dir}/{slug} -> _wiki/{slug} (existing)")
                    skipped += 1
            else:
                new_fm = add_tag(fm_text, tag)
                dest.write_text(f"---\n{new_fm}\n---\n\n{body}\n", encoding="utf-8")
                print(f"MOVE: {collection_dir}/{slug} -> _wiki/{dest_slug} [{tag}]")
                moved += 1

            # Write redirect stub back to the collection dir
            redirect = REDIRECT_TMPL.format(title=title, dest_slug=dest_slug)
            src.write_text(redirect, encoding="utf-8")

    print(f"\nDone: {moved} moved, {replaced_redirect} replaced redirects, "
          f"{renamed} renamed, {skipped} skipped")


if __name__ == "__main__":
    migrate()
