#!/usr/bin/env python3
"""Check source-derived registry files against the DataTalks.Club source repo."""

from __future__ import annotations

import argparse
from pathlib import Path

from podcast_source_data import (
    DEFAULT_PEOPLE_SOURCE,
    DEFAULT_PODCAST_SOURCE,
    ROOT,
    read_people,
    read_podcasts,
    should_skip_podcast,
    split_frontmatter,
)

DEFAULT_BOOK_SOURCE = ROOT.parent / "datatalksclub.github.io" / "_books"
DEFAULT_PODCAST_TARGET = ROOT / "_podcast_summaries"
DEFAULT_PEOPLE_TARGET = ROOT / "_people"
DEFAULT_BOOK_TARGET = ROOT / "_books"


def markdown_stems(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {item.stem for item in path.glob("*.md") if item.name != "README.md"}


def podcast_source_stems(source: Path) -> set[str]:
    return {str(podcast["slug"]) for podcast in read_podcasts(source)}


def people_source_stems(people_source: Path, podcast_source: Path) -> set[str]:
    expected = set(read_people(people_source))
    for episode in read_podcasts(podcast_source):
        for guest in episode.get("guests", []):
            if isinstance(guest, str) and guest.strip():
                expected.add(guest.strip())
    return expected


def book_source_stems(source: Path) -> set[str]:
    expected: set[str] = set()
    for path in source.glob("*.md"):
        if path.stem == "_template":
            continue
        raw = path.read_text(encoding="utf-8")
        meta, _body, _frontmatter = split_frontmatter(raw)
        if meta.get("draft"):
            continue
        expected.add(path.stem)
    return expected


def report_stale(label: str, expected: set[str], actual: set[str]) -> list[str]:
    stale = sorted(actual - expected)
    if not stale:
        print(f"{label}: {len(actual)} records, 0 stale")
        return []
    print(f"{label}: {len(actual)} records, {len(stale)} stale")
    for slug in stale:
        print(f"  - {slug}.md")
    return [f"{label}/{slug}.md" for slug in stale]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--podcast-source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--book-source", type=Path, default=DEFAULT_BOOK_SOURCE)
    parser.add_argument("--podcast-target", type=Path, default=DEFAULT_PODCAST_TARGET)
    parser.add_argument("--people-target", type=Path, default=DEFAULT_PEOPLE_TARGET)
    parser.add_argument("--book-target", type=Path, default=DEFAULT_BOOK_TARGET)
    args = parser.parse_args()

    stale: list[str] = []
    stale.extend(
        report_stale(
            "_podcast_summaries",
            podcast_source_stems(args.podcast_source),
            markdown_stems(args.podcast_target),
        )
    )
    stale.extend(
        report_stale(
            "_people",
            people_source_stems(args.people_source, args.podcast_source),
            markdown_stems(args.people_target),
        )
    )
    stale.extend(
        report_stale(
            "_books",
            book_source_stems(args.book_source),
            markdown_stems(args.book_target),
        )
    )

    if stale:
        print("")
        print("Remove or migrate stale source-derived records before building graph/search.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
