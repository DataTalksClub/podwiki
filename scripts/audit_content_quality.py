#!/usr/bin/env python3
"""Report public content pages that still need citation/link cleanup."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FOLDERS = ("_wiki", "_articles")
GENERIC_PODCAST_URL = "https://datatalks.club/podcast.html"
FORBIDDEN_HEADING_RE = re.compile(
    r"^## (Contents|Search Intent|Archive Evidence|Episode Evidence|Guest Descriptions|"
    r"Recurring Archive Themes|Maintenance Notes|Agent Maintenance Notes|Guest Experts|Bottom Line)\b",
    re.MULTILINE,
)
LOCAL_LINK_RE = re.compile(r"'/([^']+)/' \| relative_url")


def page_paths(folders: list[str]) -> list[Path]:
    paths: list[Path] = []
    for folder in folders:
        paths.extend(path for path in (ROOT / folder).glob("*.md") if path.name != "README.md")
    return sorted(paths)


def link_counts(text: str) -> dict[str, int]:
    counts = {"podcasts": 0, "wiki": 0, "people": 0, "articles": 0}
    for match in LOCAL_LINK_RE.finditer(text):
        target = match.group(1)
        for collection in counts:
            if target.startswith(f"{collection}/"):
                counts[collection] += 1
    return counts


def audit_file(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    links = link_counts(text)
    forbidden = FORBIDDEN_HEADING_RE.findall(text)
    generic = text.count(GENERIC_PODCAST_URL)
    score = generic * 3 + len(forbidden) * 10
    if path.parts[-2] in {"_wiki", "_articles"} and links["podcasts"] == 0:
        score += 5
    return {
        "path": path.relative_to(ROOT),
        "generic_podcast_links": generic,
        "forbidden_headings": len(forbidden),
        "local_podcast_links": links["podcasts"],
        "wiki_links": links["wiki"],
        "people_links": links["people"],
        "article_links": links["articles"],
        "score": score,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="*", default=list(DEFAULT_FOLDERS))
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()

    rows = [audit_file(path) for path in page_paths(args.folders)]
    problem_rows = [
        row
        for row in rows
        if row["generic_podcast_links"] or row["forbidden_headings"] or row["local_podcast_links"] == 0
    ]

    print(f"pages: {len(rows)}")
    print(f"problem_pages: {len(problem_rows)}")
    print(f"generic_podcast_links: {sum(int(row['generic_podcast_links']) for row in rows)}")
    print(f"forbidden_headings: {sum(int(row['forbidden_headings']) for row in rows)}")
    print("")

    for row in sorted(problem_rows, key=lambda item: (-int(item["score"]), str(item["path"])))[: args.limit]:
        print(
            f"{row['path']}: score={row['score']} "
            f"generic={row['generic_podcast_links']} bad_headings={row['forbidden_headings']} "
            f"podcast_links={row['local_podcast_links']} wiki_links={row['wiki_links']} "
            f"people_links={row['people_links']}"
        )


if __name__ == "__main__":
    main()
