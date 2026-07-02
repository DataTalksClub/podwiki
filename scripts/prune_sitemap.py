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

from stamp_wiki_dates import wiki_dates_map

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE = ROOT / "_site"
DEFAULT_SITEMAP = DEFAULT_SITE / "sitemap.xml"

URL_BLOCK_RE = re.compile(r"<url>.*?</url>", re.S)
LOC_RE = re.compile(r"<loc>([^<]+)</loc>")
WIKI_PATH_RE = re.compile(r"/wiki/([^/]+)/?$")


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


def prune(sitemap: Path, site: Path, baseurl: str) -> tuple[int, int, int]:
    text = sitemap.read_text(encoding="utf-8")
    wiki_dates = wiki_dates_map()
    kept = 0
    dropped = 0
    stamped = 0

    def replace(match: re.Match) -> str:
        nonlocal kept, dropped, stamped
        block = match.group(0)
        loc = LOC_RE.search(block)
        if loc and not loc_exists(loc.group(1), site, baseurl):
            dropped += 1
            return ""
        kept += 1
        # Add <lastmod> for wiki pages from git history, if not already present.
        if loc and "<lastmod>" not in block:
            wiki = WIKI_PATH_RE.search(urlsplit(loc.group(1)).path)
            if wiki:
                dates = wiki_dates.get(wiki.group(1))
                if dates:
                    stamped += 1
                    return block.replace(
                        loc.group(0),
                        f"{loc.group(0)}<lastmod>{dates['last_modified_at']}</lastmod>",
                    )
        return block

    pruned = URL_BLOCK_RE.sub(replace, text)
    # collapse blank lines left by removed <url> blocks
    pruned = re.sub(r"\n\s*\n+", "\n", pruned)
    sitemap.write_text(pruned, encoding="utf-8")
    return kept, dropped, stamped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sitemap", type=Path, default=DEFAULT_SITEMAP)
    parser.add_argument("--site", type=Path, default=DEFAULT_SITE)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()

    if not args.sitemap.exists():
        print(f"no sitemap at {args.sitemap}; skipping")
        return
    kept, dropped, stamped = prune(args.sitemap, args.site, args.baseurl)
    print(
        f"sitemap pruned: kept {kept}, dropped {dropped} missing entries, "
        f"stamped {stamped} wiki lastmod"
    )


if __name__ == "__main__":
    main()
