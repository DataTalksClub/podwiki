#!/usr/bin/env python3
"""Rewrite generated URLs for a GitHub Pages project base path.

Covers two cases:

- sitemap/feed absolute URLs (``https://datatalks.club/...``) gain the baseurl.
- HTML ``href``/``src`` root-relative URLs (``/...``) gain the baseurl, so plain
  Markdown links in ``_course_wiki/`` (which intentionally use ``/course-wiki/``
  absolute paths that graph/search tooling parses) resolve under the project
  subpath instead of 404ing in production.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def normalize_baseurl(value: str) -> str:
    value = value.strip()
    if not value or value == "/":
        return ""
    if not value.startswith("/"):
        value = f"/{value}"
    return value.rstrip("/")


def rewrite_url(value: str, site_url: str, baseurl: str) -> str:
    if not baseurl:
        return value
    site_url = site_url.rstrip("/")
    wanted = f"{site_url}{baseurl}"
    if value == site_url:
        return wanted
    if value == f"{site_url}/":
        return f"{wanted}/"
    if value.startswith(f"{wanted}/") or value == wanted:
        return value
    if value.startswith(f"{site_url}/"):
        return f"{wanted}{value[len(site_url):]}"
    return value


def rewrite_xml(path: Path, site_url: str, baseurl: str) -> int:
    if not path.exists():
        return 0
    tree = ET.parse(path)
    root = tree.getroot()
    if root.tag.startswith("{"):
        namespace = root.tag.split("}", 1)[0].lstrip("{")
        ET.register_namespace("", namespace)
    changed = 0
    for element in root.iter():
        if element.text:
            rewritten = rewrite_url(element.text, site_url, baseurl)
            if rewritten != element.text:
                element.text = rewritten
                changed += 1
        for attr, value in list(element.attrib.items()):
            rewritten = rewrite_url(value, site_url, baseurl)
            if rewritten != value:
                element.set(attr, rewritten)
                changed += 1
    if changed:
        tree.write(path, encoding="utf-8", xml_declaration=True)
    return changed


def assert_no_missing_baseurl(path: Path, site_url: str, baseurl: str) -> list[str]:
    if not path.exists() or not baseurl:
        return []
    text = path.read_text(encoding="utf-8")
    site_url = site_url.rstrip("/")
    wanted = f"{site_url}{baseurl}"
    failures: list[str] = []
    marker = f"{site_url}/"
    start = 0
    while True:
        index = text.find(marker, start)
        if index == -1:
            break
        if not text.startswith(f"{wanted}/", index):
            end = text.find("<", index)
            failures.append(text[index : end if end != -1 else index + 160])
        start = index + len(marker)
    return failures


HTML_LINK_RE = re.compile(r"""(?P<attr>(?:href|src)\s*=\s*)(?P<quote>["'])(?P<url>/[^"']*)(?P=quote)""")


def rewrite_html_file(path: Path, baseurl: str) -> int:
    """Prefix root-relative href/src URLs with baseurl. Returns change count."""
    text = path.read_text(encoding="utf-8")
    changed = 0

    def replace(match: re.Match) -> str:
        nonlocal changed
        url = match.group("url")
        if url.startswith("//"):
            return match.group(0)
        if url == baseurl or url.startswith(f"{baseurl}/"):
            return match.group(0)
        changed += 1
        return f"{match.group('attr')}{match.group('quote')}{baseurl}{url}{match.group('quote')}"

    rewritten = HTML_LINK_RE.sub(replace, text)
    if changed:
        path.write_text(rewritten, encoding="utf-8")
    return changed


def rewrite_html_site(site: Path, baseurl: str) -> tuple[int, int]:
    """Rewrite all HTML files under site. Returns (files_changed, urls_changed)."""
    if not baseurl:
        return 0, 0
    files_changed = 0
    urls_changed = 0
    for path in sorted(site.rglob("*.html")):
        changed = rewrite_html_file(path, baseurl)
        if changed:
            files_changed += 1
            urls_changed += changed
    return files_changed, urls_changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--site-url", default="https://datatalks.club")
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()

    baseurl = normalize_baseurl(args.baseurl)
    changed = 0
    for filename in ("sitemap.xml", "feed.xml"):
        changed += rewrite_xml(args.site / filename, args.site_url, baseurl)

    failures: list[str] = []
    for filename in ("sitemap.xml", "feed.xml"):
        failures.extend(assert_no_missing_baseurl(args.site / filename, args.site_url, baseurl))
    if failures:
        print("absolute URL baseurl check failed", file=sys.stderr)
        for failure in failures[:20]:
            print(f"- {failure}", file=sys.stderr)
        return 1

    html_files, html_urls = rewrite_html_site(args.site, baseurl)

    print(f"rewrote {changed} absolute URLs for baseurl {baseurl or '/'}")
    if baseurl:
        print(f"rewrote {html_urls} root-relative HTML links in {html_files} files for baseurl {baseurl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
