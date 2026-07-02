#!/usr/bin/env python3
"""Check generated HTML for chips trapped in accidental Markdown tables."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CHIP_TABLE_RE = re.compile(r"<table\b[^>]*>.*?class=\"chip\b.*?</table>", re.DOTALL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    args = parser.parse_args()

    site = args.site.resolve()
    if not site.exists():
        print(f"site directory does not exist: {site}", file=sys.stderr)
        return 1

    failures: list[str] = []
    for path in sorted(site.rglob("*.html")):
        html = path.read_text(encoding="utf-8")
        if CHIP_TABLE_RE.search(html):
            failures.append(str(path.relative_to(site)))

    if failures:
        print(f"chip HTML check failed: {len(failures)} pages contain chips inside tables")
        for failure in failures[:200]:
            print(f"- {failure}")
        if len(failures) > 200:
            print(f"... and {len(failures) - 200} more")
        return 1

    print("chip HTML check passed: no chips inside generated tables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
