#!/usr/bin/env python3
"""Convert wiki `related:` / `related_wiki:` front matter from titles to slugs.

Slugs are stable across title renames and let the build verify a referenced
page actually exists. This rewrites each list entry to the target page's slug
and reports any entry that resolves to no `_wiki/<slug>.md` (a dangling ref),
which is the build-time existence check.

Deterministic and idempotent: an entry that is already a valid slug is left as
is. Run after content edits; a good home is `make sources`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "_wiki"
KEYS = ("related", "related_wiki")


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def page_title(path: Path) -> str | None:
    head = path.read_text(encoding="utf-8")[:2000]
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', head, re.M)
    return m.group(1).strip() if m else None


def build_maps() -> tuple[set[str], dict[str, str]]:
    slugs: set[str] = set()
    title_to_slug: dict[str, str] = {}
    for path in sorted(WIKI.glob("*.md")):
        if path.name == "README.md":
            continue
        slugs.add(path.stem)
        title = page_title(path)
        if title:
            title_to_slug[title.lower()] = path.stem
    return slugs, title_to_slug


def resolve(entry: str, slugs: set[str], title_to_slug: dict[str, str]) -> tuple[str, bool]:
    """Return (slug, exists). exists=False means it maps to no wiki page."""
    e = entry.strip().strip('"').strip("'")
    if e in slugs:
        return e, True
    mapped = title_to_slug.get(e.lower())
    if mapped:
        return mapped, True
    s = slugify(e)
    if s in slugs:
        return s, True
    return s, False  # best-effort slug, but flagged as dangling


def convert(path: Path, slugs: set[str], title_to_slug: dict[str, str]) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    # operate only within the front matter block
    if not text.startswith("---\n"):
        return 0, []
    end = text.find("\n---", 4)
    if end == -1:
        return 0, []
    fm, body = text[: end + 1], text[end + 1 :]

    lines = fm.splitlines()
    out: list[str] = []
    dangling: list[str] = []
    changed = 0
    in_block = False

    for line in lines:
        key_inline = re.match(r'^(related|related_wiki):\s*\[(.*)\]\s*$', line)
        if key_inline:
            key, inner = key_inline.group(1), key_inline.group(2)
            items = [i.strip().strip('"').strip("'") for i in inner.split(",") if i.strip()]
            new_items = []
            for it in items:
                slug, ok = resolve(it, slugs, title_to_slug)
                if not ok:
                    dangling.append(it)
                if slug != it:
                    changed += 1
                new_items.append(slug)
            out.append(f"{key}: [{', '.join(new_items)}]")
            in_block = False
            continue
        if re.match(r'^(related|related_wiki):\s*$', line):
            in_block = True
            out.append(line)
            continue
        if in_block:
            item = re.match(r'^(\s+-\s+)(.*)$', line)
            if item:
                prefix, val = item.group(1), item.group(2)
                slug, ok = resolve(val, slugs, title_to_slug)
                if not ok:
                    dangling.append(val.strip())
                if slug != val.strip().strip('"').strip("'"):
                    changed += 1
                out.append(f"{prefix}{slug}")
                continue
            in_block = False
        out.append(line)

    if changed:
        path.write_text("\n".join(out) + body, encoding="utf-8")
    return changed, dangling


def main() -> None:
    slugs, title_to_slug = build_maps()
    total_changed = 0
    files_changed = 0
    all_dangling: dict[str, list[str]] = {}
    for path in sorted(WIKI.glob("*.md")):
        if path.name == "README.md":
            continue
        changed, dangling = convert(path, slugs, title_to_slug)
        if changed:
            files_changed += 1
            total_changed += changed
        if dangling:
            all_dangling[path.name] = dangling

    print(f"related->slugs: rewrote {total_changed} entries in {files_changed} files")
    if all_dangling:
        print(f"\nDANGLING related refs (no matching _wiki page) in {len(all_dangling)} files:")
        for name, refs in sorted(all_dangling.items()):
            print(f"  {name}: {', '.join(refs)}")
    else:
        print("no dangling refs")


if __name__ == "__main__":
    main()
