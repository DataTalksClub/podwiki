#!/usr/bin/env python3
"""Check source-derived registry files against the DataTalks.Club source repo."""

from __future__ import annotations

import argparse
import re
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
CANONICAL_ENTITY_URL_RE = re.compile(
    r"https://datatalks\.club/(?:people|books|podcast)/[^\s\)\"'<]*[ \t][^\n\)\"'<]*?\.html"
)


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


def report_records(label: str, expected: set[str], actual: set[str]) -> list[str]:
    missing = sorted(expected - actual)
    stale = sorted(actual - expected)
    print(f"{label}: {len(actual)} records, {len(missing)} missing, {len(stale)} stale")
    problems: list[str] = []
    for slug in missing:
        print(f"  missing - {slug}.md")
        problems.append(f"{label}/{slug}.md")
    for slug in stale:
        print(f"  stale - {slug}.md")
        problems.append(f"{label}/{slug}.md")
    return problems


def report_malformed_canonical_urls(paths: list[Path]) -> list[str]:
    problems: list[str] = []
    for directory in paths:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            for match in CANONICAL_ENTITY_URL_RE.finditer(text):
                rel = path.relative_to(ROOT)
                print(f"malformed canonical URL - {rel}: {match.group(0)}")
                problems.append(f"{rel}: {match.group(0)}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--podcast-source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--book-source", type=Path, default=DEFAULT_BOOK_SOURCE)
    parser.add_argument("--podcast-target", type=Path, default=DEFAULT_PODCAST_TARGET)
    parser.add_argument("--people-target", type=Path, default=DEFAULT_PEOPLE_TARGET)
    parser.add_argument("--book-target", type=Path, default=DEFAULT_BOOK_TARGET)
    args = parser.parse_args()

    problems: list[str] = []
    problems.extend(
        report_records(
            "_podcast_summaries",
            podcast_source_stems(args.podcast_source),
            markdown_stems(args.podcast_target),
        )
    )
    problems.extend(
        report_records(
            "_people",
            people_source_stems(args.people_source, args.podcast_source),
            markdown_stems(args.people_target),
        )
    )
    problems.extend(
        report_records(
            "_books",
            book_source_stems(args.book_source),
            markdown_stems(args.book_target),
        )
    )
    problems.extend(
        report_malformed_canonical_urls(
            [args.podcast_target, args.people_target, args.book_target]
        )
    )

    if problems:
        print("")
        print("Run source sync or remove stale source-derived records before building graph/search.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
