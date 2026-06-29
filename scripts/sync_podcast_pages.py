#!/usr/bin/env python3
"""Create local podcast reference pages from the DataTalks.Club podcast source."""

from __future__ import annotations

import argparse
from pathlib import Path

from podcast_source_data import (
    DEFAULT_PEOPLE_SOURCE,
    DEFAULT_PODCAST_SOURCE,
    ROOT,
    read_people,
    read_podcast,
    should_skip_podcast,
    yaml_list,
    yaml_string,
)

DEFAULT_TARGET = ROOT / "_podcast_summaries"


def person_label(slug: str, people: dict[str, dict[str, object]]) -> str:
    person = people.get(slug, {})
    title = str(person.get("title") or "").strip()
    if title:
        return title
    return slug.replace("-", " ").replace("_", " ").title()


def page_body(podcast: dict[str, object], people: dict[str, dict[str, object]]) -> str:
    slug = str(podcast["slug"])
    intro = str(podcast.get("intro") or podcast.get("description") or "")
    lines = [
        f"# {podcast.get('title') or slug.replace('-', ' ').title()}",
        "",
        "## Original Episode",
        "",
        "Use these links for the canonical episode and media sources.",
        "",
        f"- [Open the original DataTalks.Club podcast page]({podcast['source_url']})",
    ]

    links = podcast.get("links")
    if isinstance(links, dict):
        if links.get("youtube") and links["youtube"] != "TODO":
            lines.append(f"- [Watch on YouTube]({links['youtube']})")
        if links.get("spotify") and links["spotify"] != "TODO":
            lines.append(f"- [Listen on Spotify]({links['spotify']})")
        if links.get("apple") and links["apple"] != "TODO":
            lines.append(f"- [Listen on Apple Podcasts]({links['apple']})")

    if intro:
        lines.extend(["", "## Episode Overview", "", intro])

    guests = podcast.get("guests")
    if isinstance(guests, list) and guests:
        lines.extend(["", "## People", "", "Use these links to connect the episode to guest notes."])
        lines.append("")
        for guest in guests:
            slug = str(guest or "").strip()
            if slug:
                lines.append(
                    f"- [{person_label(slug, people)}]({{{{ '/people/{slug}/' | relative_url }}}})"
                )

    chapters = podcast.get("chapters")
    lines.extend(["", "## Chapter Summary", ""])
    if isinstance(chapters, list) and chapters:
        lines.append("Use these checkpoints to decide whether to open the source transcript.")
        lines.append("")
        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            label = str(chapter.get("title") or "").strip()
            if not label:
                continue
            time = str(chapter.get("time") or "").strip()
            url = str(chapter.get("url") or "").strip()
            prefix = f"{time} - " if time else ""
            if url:
                lines.append(f"- {prefix}[{label}]({url})")
            else:
                lines.append(f"- {prefix}{label}")
    else:
        lines.append(
            "- No chapter clips or transcript section headers are available in the source file; "
            "open the original episode transcript before making fine-grained claims."
        )

    return "\n".join(lines) + "\n"


def render_page(source: Path, target: Path, people: dict[str, dict[str, object]]) -> bool:
    podcast = read_podcast(source)
    links = podcast.get("links") if isinstance(podcast.get("links"), dict) else {}

    frontmatter = [
        "---",
        "layout: podcast_summary",
        f"title: {yaml_string(podcast['title'])}",
        f"source_episode: {yaml_string(podcast['source_episode'])}",
        f"source_url: {yaml_string(podcast['source_url'])}",
        f"season: {podcast.get('season', '')}",
        f"episode: {podcast.get('episode', '')}",
        f"guests: {yaml_list(podcast.get('guests'))}",
        f"topics: {yaml_list(podcast.get('topics'))}",
        "summary_status: source-index",
    ]
    if isinstance(links, dict):
        for key in ("youtube", "spotify", "apple"):
            if links.get(key) and links[key] != "TODO":
                frontmatter.append(f"{key}_url: {yaml_string(links[key])}")
    frontmatter.extend(["---", ""])

    rendered = "\n".join(frontmatter) + page_body(podcast, people)
    if target.exists() and target.read_text(encoding="utf-8") == rendered:
        return False
    target.write_text(rendered, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    args = parser.parse_args()

    args.target.mkdir(parents=True, exist_ok=True)
    people = read_people(args.people_source)
    changed = 0
    total = 0
    for source in sorted(args.source.glob("*.md")):
        if should_skip_podcast(source):
            continue
        total += 1
        podcast = read_podcast(source)
        target = args.target / f"{podcast['slug']}.md"
        if render_page(source, target, people):
            changed += 1

    print(f"synced {total} podcast pages, changed {changed}")


if __name__ == "__main__":
    main()
