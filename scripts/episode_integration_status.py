#!/usr/bin/env python3
"""Report which source episodes still need Podwiki review or source sync."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from podcast_source_data import DEFAULT_PODCAST_SOURCE, read_podcasts


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_DIR = ROOT / "_podcast_summaries"
WIKI_DIR = ROOT / "_wiki"
DECISIONS_PATH = ROOT / "sources" / "episode-integration-decisions.json"
ACTION_STATUSES = {"needs_sync", "needs_review"}
CHIP_REF_RE = re.compile(r"\[\[(?:cite|podcast):([^@\]|=]+)")
CANONICAL_REF_RE = re.compile(r"https://datatalks\.club/podcast/([^/)]+)\.html")


def load_decisions(path: Path = DECISIONS_PATH) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    episodes = payload.get("episodes", {})
    if not isinstance(episodes, dict):
        raise ValueError(f"invalid episodes object in {path}")
    return {
        str(slug): value
        for slug, value in episodes.items()
        if isinstance(value, dict)
    }


def all_wiki_references() -> dict[str, list[str]]:
    references: dict[str, list[str]] = {}
    for path in sorted(WIKI_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        slugs = set(CHIP_REF_RE.findall(raw)) | set(CANONICAL_REF_RE.findall(raw))
        relative = str(path.relative_to(ROOT))
        for slug in slugs:
            references.setdefault(slug, []).append(relative)
    return references


def numeric(value: object) -> int:
    try:
        return int(str(value))
    except ValueError:
        return -1


def build_report(source: Path = DEFAULT_PODCAST_SOURCE) -> dict[str, object]:
    decisions = load_decisions()
    references_by_slug = all_wiki_references()
    episodes = []
    source_slugs = set()

    for podcast in read_podcasts(source):
        slug = str(podcast["slug"])
        source_slugs.add(slug)
        summary_exists = (SUMMARY_DIR / f"{slug}.md").exists()
        references = references_by_slug.get(slug, [])
        decision = decisions.get(slug, {})

        if not summary_exists:
            status = "needs_sync"
        elif references:
            status = "integrated"
        elif decision.get("status") == "reviewed_no_change":
            status = "reviewed_no_change"
        else:
            status = "needs_review"

        episodes.append(
            {
                "slug": slug,
                "title": podcast["title"],
                "season": numeric(podcast.get("season")),
                "episode": numeric(podcast.get("episode")),
                "status": status,
                "wiki_pages": references,
                "decision": decision,
            }
        )

    episodes.sort(
        key=lambda item: (item["season"], item["episode"], item["slug"]),
        reverse=True,
    )
    local_slugs = {
        path.stem.removesuffix(".md")
        for path in SUMMARY_DIR.glob("*.md")
        if path.name != "README.md"
    }
    return {
        "episodes": episodes,
        "stale_summaries": sorted(local_slugs - source_slugs),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--season", type=int)
    parser.add_argument(
        "--status",
        choices=["action", "all", "needs_sync", "needs_review", "integrated", "reviewed_no_change"],
        default="action",
    )
    parser.add_argument("--limit", type=int, default=0, help="maximum rows; zero means unlimited")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = build_report(args.source)
    episodes = list(report["episodes"])
    if args.season is not None:
        episodes = [item for item in episodes if item["season"] == args.season]
    if args.status == "action":
        episodes = [item for item in episodes if item["status"] in ACTION_STATUSES]
    elif args.status != "all":
        episodes = [item for item in episodes if item["status"] == args.status]
    if args.limit > 0:
        episodes = episodes[: args.limit]

    if args.json:
        print(json.dumps({**report, "episodes": episodes}, indent=2, ensure_ascii=False))
        return

    for item in episodes:
        identifier = f"s{item['season']:02d}e{item['episode']:02d}"
        print(f"{item['status']:18} {identifier}  {item['slug']}")
    stale = report["stale_summaries"]
    if stale:
        print("\nstale local summaries:")
        for slug in stale:
            print(f"  {slug}")
    print(f"\n{len(episodes)} episode(s) shown")


if __name__ == "__main__":
    main()
