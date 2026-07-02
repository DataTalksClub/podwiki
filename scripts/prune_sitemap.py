#!/usr/bin/env python3
"""Drop sitemap entries whose page was not actually emitted.

The podcast/person/book collections are node registries with `output: false`
(they duplicate the main datatalks.club site), so no HTML is written for them.
rustkyll's sitemap generator still lists every collection document, which would
advertise hundreds of URLs that 404. This post-build pass keeps only `<loc>`
entries that map to a real file under `_site/`.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE = ROOT / "_site"
DEFAULT_SITEMAP = DEFAULT_SITE / "sitemap.xml"

URL_BLOCK_RE = re.compile(r"<url>.*?</url>", re.S)
LOC_RE = re.compile(r"<loc>([^<]+)</loc>")


def loc_exists(loc: str, site: Path, baseurl: str) -> bool:
    path = urlsplit(loc).path
    if baseurl and path.startswith(baseurl):
        path = path[len(baseurl):]
    path = path.lstrip("/")
    if path == "" or path.endswith("/"):
        target = site / path / "index.html"
    elif path.endswith((".html", ".xml", ".json", ".txt")):
        target = site / path
    else:
        # pretty permalink without trailing slash
        target = site / path / "index.html"
    return target.exists()


def prune(sitemap: Path, site: Path, baseurl: str) -> tuple[int, int]:
    text = sitemap.read_text(encoding="utf-8")
    kept = 0
    dropped = 0

    def replace(match: re.Match) -> str:
        nonlocal kept, dropped
        block = match.group(0)
        loc = LOC_RE.search(block)
        if loc and not loc_exists(loc.group(1), site, baseurl):
            dropped += 1
            return ""
        kept += 1
        return block

    pruned = URL_BLOCK_RE.sub(replace, text)
    # collapse blank lines left by removed <url> blocks
    pruned = re.sub(r"\n\s*\n+", "\n", pruned)
    sitemap.write_text(pruned, encoding="utf-8")
    return kept, dropped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sitemap", type=Path, default=DEFAULT_SITEMAP)
    parser.add_argument("--site", type=Path, default=DEFAULT_SITE)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()

    if not args.sitemap.exists():
        print(f"no sitemap at {args.sitemap}; skipping")
        return
    kept, dropped = prune(args.sitemap, args.site, args.baseurl)
    print(f"sitemap pruned: kept {kept}, dropped {dropped} missing entries")


if __name__ == "__main__":
    main()
