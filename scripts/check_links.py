#!/usr/bin/env python3
"""Check generated static-site links for missing local targets."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKIP_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str, str]] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value for key, value in attrs}
        if "id" in attr_map and attr_map["id"]:
            self.anchors.add(str(attr_map["id"]))
        if "name" in attr_map and attr_map["name"]:
            self.anchors.add(str(attr_map["name"]))
        for attr in ("href", "src"):
            value = attr_map.get(attr)
            if value:
                self.links.append((tag, attr, value))


def parse_html(path: Path) -> LinkParser:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def target_for_url(site: Path, current: Path, url: str, baseurl: str) -> tuple[Path | None, str]:
    parsed = urlsplit(url)
    if parsed.scheme in SKIP_SCHEMES or parsed.netloc:
        return None, ""
    if not parsed.path and parsed.fragment:
        return current, parsed.fragment
    if not parsed.path:
        return None, ""

    raw_path = unquote(parsed.path)
    if raw_path.startswith("//"):
        return None, ""
    if raw_path.startswith("/"):
        if baseurl:
            if raw_path == baseurl:
                raw_path = "/"
            elif raw_path.startswith(f"{baseurl}/"):
                raw_path = raw_path[len(baseurl) :]
            else:
                raise ValueError(f"root-relative URL is outside baseurl {baseurl!r}: {url}")
        relative = raw_path.lstrip("/")
        target = site / relative
    else:
        target = current.parent / raw_path

    if target.is_dir() or raw_path.endswith("/"):
        target = target / "index.html"
    elif not target.suffix:
        target = target / "index.html"
    return target.resolve(), parsed.fragment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()

    site = args.site.resolve()
    baseurl = args.baseurl.rstrip("/")
    if not site.exists():
        print(f"site directory does not exist: {site}", file=sys.stderr)
        return 1

    html_pages = sorted(site.rglob("*.html"))
    anchors_by_page = {path.resolve(): parse_html(path) for path in html_pages}
    failures: list[str] = []
    checked = 0

    for page, parsed_page in anchors_by_page.items():
        for tag, attr, url in parsed_page.links:
            try:
                target, fragment = target_for_url(site, page, url, baseurl)
            except ValueError as exc:
                failures.append(f"{page.relative_to(site)}: {tag}[{attr}] {exc}")
                continue
            if target is None:
                continue
            checked += 1
            if not target.exists():
                failures.append(
                    f"{page.relative_to(site)}: {tag}[{attr}] points to missing {url!r}"
                )
                continue
            if fragment and target.suffix == ".html":
                target_parser = anchors_by_page.get(target)
                if target_parser and fragment not in target_parser.anchors:
                    failures.append(
                        f"{page.relative_to(site)}: {tag}[{attr}] points to missing anchor {url!r}"
                    )

    if failures:
        print(f"link check failed: {len(failures)} failures")
        for failure in failures[:200]:
            print(f"- {failure}")
        if len(failures) > 200:
            print(f"... and {len(failures) - 200} more")
        return 1
    print(f"link check passed: {checked} internal links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
