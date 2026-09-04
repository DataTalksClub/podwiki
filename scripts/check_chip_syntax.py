#!/usr/bin/env python3
"""Check Markdown sources for legacy pipe-based chip aliases.

Pipe aliases such as ``[[cite:slug|Label]]`` can be interpreted by Markdown as
table syntax when adjacent chips appear on separate lines. New and edited
content should use ``=>`` aliases instead, for example
``[[cite:slug=>Label]]`` and ``[[cite:slug@12:34=>Label]]``.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHIP_PIPE_RE = re.compile(r"\[\[[^\]]*\|")


def iter_default_paths() -> list[Path]:
    paths: list[Path] = []
    for dirname in ["_wiki", "_people", "_podcast_summaries", "_books", "_events"]:
        directory = ROOT / dirname
        if directory.exists():
            paths.extend(sorted(directory.glob("*.md")))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files to check. If omitted, checks wiki/entity collections.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print findings but exit 0. Useful while legacy pages are being cleaned.",
    )
    args = parser.parse_args()

    paths = args.paths or iter_default_paths()
    failures: list[str] = []
    checked = 0

    for path in paths:
        full_path = path if path.is_absolute() else ROOT / path
        if not full_path.exists():
            failures.append(f"{path}: file does not exist")
            continue
        if full_path.suffix != ".md":
            continue
        checked += 1
        rel = full_path.relative_to(ROOT)
        for lineno, line in enumerate(full_path.read_text(encoding="utf-8").splitlines(), 1):
            if CHIP_PIPE_RE.search(line):
                failures.append(f"{rel}:{lineno}: use => aliases inside chips")

    if failures:
        print(f"chip syntax check found {len(failures)} legacy pipe aliases")
        for failure in failures[:200]:
            print(f"- {failure}")
        if len(failures) > 200:
            print(f"... and {len(failures) - 200} more")
        return 0 if args.report else 1

    print(f"chip syntax check passed: {checked} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
