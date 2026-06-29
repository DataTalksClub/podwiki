#!/usr/bin/env python3
"""Create local people pages from DataTalks.Club people and podcast sources."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

from podcast_source_data import (
    DEFAULT_PEOPLE_SOURCE,
    DEFAULT_PODCAST_SOURCE,
    ROOT,
    split_frontmatter,
    read_people,
    read_podcasts,
    yaml_list,
    yaml_string,
)


DEFAULT_TARGET = ROOT / "_people"


def merge_existing_page(target: Path, rendered: str) -> str:
    if not target.exists():
        return rendered

    raw = target.read_text(encoding="utf-8")
    meta, body, _ = split_frontmatter(raw)
    if not body.strip():
        return rendered
    if not meta.get("source_person") and "## Podcast Discussions" in body:
        return rendered

    generated_meta, _, _ = split_frontmatter(rendered)
    for key, value in generated_meta.items():
        if key in {"source_url", "podcast_episodes"}:
            meta[key] = value
        elif key in {"layout", "title", "summary"} and not meta.get(key):
            meta[key] = value

    frontmatter = ["---"]
    for key, value in meta.items():
        if isinstance(value, list):
            frontmatter.append(f"{key}: {yaml_list(value)}")
        else:
            frontmatter.append(f"{key}: {yaml_string(value)}")
    frontmatter.extend(["---", ""])
    return "\n".join(frontmatter) + body


def topic_links(topics: object) -> list[str]:
    if not isinstance(topics, list):
        return []
    links = []
    wiki_dir = ROOT / "_wiki"
    for topic in topics[:8]:
        label = str(topic).strip()
        if not label:
            continue
        slug = label.lower().replace(" ", "-")
        if (wiki_dir / f"{slug}.md").exists():
            links.append(f"[{label}]({{{{ '/wiki/{slug}/' | relative_url }}}})")
        else:
            links.append(label)
    return links


def render_person(slug: str, person: dict[str, object], episodes: list[dict[str, object]]) -> str:
    title = str(person.get("title") or slug)
    bio = str(person.get("bio") or "").strip()
    summary = (
        f"{title}'s DataTalks.Club podcast discussions, organized for topic exploration."
        if episodes
        else f"{title}'s DataTalks.Club profile."
    )

    frontmatter = [
        "---",
        "layout: person",
        f"title: {yaml_string(title)}",
        f"summary: {yaml_string(summary)}",
        f"source_url: {yaml_string(f'https://datatalks.club/people/{slug}.html')}",
        f"podcast_episodes: {yaml_list([str(item['slug']) for item in episodes])}",
    ]
    for key in ("github", "twitter", "linkedin", "web"):
        value = str(person.get(key) or "").strip()
        if value:
            frontmatter.append(f"{key}: {yaml_string(value)}")
    frontmatter.extend(["---", ""])

    lines = [f"# {title}", ""]
    if bio:
        lines.extend(["## Background", "", bio, ""])

    if episodes:
        lines.extend(["## Podcast Discussions", ""])
        for episode in episodes:
            episode_title = str(episode["title"])
            episode_slug = str(episode["slug"])
            topics = topic_links(episode.get("topics"))
            topic_text = f" Related topics: {', '.join(topics)}." if topics else ""
            lines.append(
                f"- [{episode_title}]({{{{ '/podcasts/{episode_slug}/' | relative_url }}}}).{topic_text}"
            )

    return "\n".join(frontmatter + lines).rstrip() + "\n"


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
        person = people.get(slug, {"title": slug, "bio": ""})
        target = args.target / f"{slug}.md"
        rendered = merge_existing_page(target, render_person(slug, person, appearances.get(slug, [])))
        total += 1
        if target.exists() and target.read_text(encoding="utf-8") == rendered:
            continue
        target.write_text(rendered, encoding="utf-8")
        changed += 1

    print(f"synced {total} people pages, changed {changed}")


if __name__ == "__main__":
    main()
