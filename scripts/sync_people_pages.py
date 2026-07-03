#!/usr/bin/env python3
"""Create source-derived people index records from DataTalks.Club sources."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

from podcast_source_data import (
    DEFAULT_PEOPLE_SOURCE,
    DEFAULT_PODCAST_SOURCE,
    ROOT,
    read_people,
    read_podcasts,
    yaml_list,
    yaml_string,
)


DEFAULT_TARGET = ROOT / "_people"
def render_person(slug: str, person: dict[str, object], episodes: list[dict[str, object]]) -> str:
    title = str(person.get("title") or slug)
    summary = (
        f"{title}'s DataTalks.Club person index record."
        if episodes
        else f"{title}'s DataTalks.Club profile."
    )

    frontmatter = [
        "---",
        "layout: person",
        f"title: {yaml_string(title)}",
        f"summary: {yaml_string(summary)}",
    ]
    source_url = str(person.get("source_url") or "").strip()
    if source_url:
        frontmatter.append(f"source_url: {yaml_string(source_url)}")
    frontmatter.append(f"podcast_episodes: {yaml_list([str(item['slug']) for item in episodes])}")
    for key in ("github", "twitter", "linkedin", "web"):
        value = str(person.get(key) or "").strip()
        if value:
            frontmatter.append(f"{key}: {yaml_string(value)}")
    frontmatter.extend(["---", ""])
    return "\n".join(frontmatter).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--podcast-source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    args = parser.parse_args()

    people = read_people(args.people_source)
    appearances: dict[str, list[dict[str, object]]] = defaultdict(list)
    for episode in read_podcasts(args.podcast_source):
        for guest in episode.get("guests", []):
            if isinstance(guest, str) and guest.strip():
                appearances[guest].append(episode)

    args.target.mkdir(parents=True, exist_ok=True)
    changed = 0
    total = 0
    for slug in sorted(set(people) | set(appearances)):
        if slug in people:
            person = {**people[slug], "source_url": f"https://datatalks.club/people/{slug}.html"}
        else:
            person = {"title": slug, "bio": ""}
        target = args.target / f"{slug}.md"
        rendered = render_person(slug, person, appearances.get(slug, []))
        total += 1
        if target.exists() and target.read_text(encoding="utf-8") == rendered:
            continue
        target.write_text(rendered, encoding="utf-8")
        changed += 1

    print(f"synced {total} people records, changed {changed}")


if __name__ == "__main__":
    main()
