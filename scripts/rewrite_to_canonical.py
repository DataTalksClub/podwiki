#!/usr/bin/env python3
"""Rewrite internal podcast/person/book cross-links to canonical main-site URLs.

podcast/person/book pages are node registries, not published pages (see
`_config.yml` output: false). Wiki and editorial bodies must therefore link
straight to the canonical DataTalks.Club URL instead of the local
`/podcasts/<slug>/`, `/people/<slug>/`, or `/books/<slug>/` path.

This migration is idempotent: canonical URLs no longer match the local path
patterns, so re-running it is a no-op. It runs as part of `make sources` as a
safety net after the sync scripts (which already emit canonical links).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# content collections whose bodies may reference podcast/person/book pages
CONTENT_DIRS = ["_wiki", "_podcast_summaries", "_people", "_books"]

# local link prefix -> (registry dir, main-site path segment)
# Note the main site uses the singular `/podcast/` path for episodes.
REGISTRY = {
    "podcasts": ("_podcast_summaries", "podcast"),
    "people": ("_people", "people"),
    "books": ("_books", "books"),
}

SOURCE_URL_RE = re.compile(r'^source_url:\s*["\']?([^"\'\n]+)["\']?\s*$', re.M)


def build_maps() -> dict[str, dict[str, str]]:
    """slug -> canonical source_url, per local prefix, from registry front matter."""
    maps: dict[str, dict[str, str]] = {prefix: {} for prefix in REGISTRY}
    for prefix, (directory, _segment) in REGISTRY.items():
        collection_dir = ROOT / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            head = path.read_text(encoding="utf-8")[:2000]
            match = SOURCE_URL_RE.search(head)
            if match:
                maps[prefix][path.stem] = match.group(1).strip()
    return maps


def canonical_url(prefix: str, slug: str, maps: dict[str, dict[str, str]]) -> str:
    mapped = maps.get(prefix, {}).get(slug)
    if mapped:
        return mapped
    segment = REGISTRY[prefix][1]
    return f"https://datatalks.club/{segment}/{slug}.html"


def rewrite_text(text: str, maps: dict[str, dict[str, str]]) -> tuple[str, int]:
    count = 0
    prefixes = "|".join(REGISTRY)
    # A local reference is a prefix + a slug segment; the bare `/podcasts/`
    # listing (no slug) must not match, so require at least one slug char.
    slug = r"([a-z0-9][a-z0-9-]*)"

    def resolve(prefix: str, slug_value: str) -> str:
        nonlocal count
        count += 1
        return canonical_url(prefix, slug_value, maps)

    # Liquid form: {{ '/podcasts/<slug>/' | relative_url }} (optional #fragment).
    # Braces are optional-doubled to also catch the malformed single-brace
    # `{ '/people/<slug>/' | relative_url }` emitted by older book pages.
    liquid = re.compile(
        r"\{\{?\s*['\"]/(?P<prefix>" + prefixes + r")/" + slug
        + r"/?(?:#[^'\"]*)?['\"]\s*\|\s*relative_url\s*\}\}?"
    )
    text = liquid.sub(lambda m: resolve(m.group("prefix"), m.group(2)), text)

    # Plain markdown href form: ](/podcasts/<slug>/) (optional #fragment)
    plain = re.compile(
        r"\]\(/(?P<prefix>" + prefixes + r")/" + slug + r"/?(?:#[^)]*)?\)"
    )
    text = plain.sub(lambda m: "](" + resolve(m.group("prefix"), m.group(2)) + ")", text)

    return text, count


def main() -> None:
    maps = build_maps()
    total_changes = 0
    files_changed = 0
    for directory in CONTENT_DIRS:
        collection_dir = ROOT / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            raw = path.read_text(encoding="utf-8")
            new_text, count = rewrite_text(raw, maps)
            if count and new_text != raw:
                path.write_text(new_text, encoding="utf-8")
                total_changes += count
                files_changed += 1
                print(f"  {directory}/{path.name}: {count} links")
    print(f"canonical rewrite: {total_changes} links in {files_changed} files")


if __name__ == "__main__":
    main()
