#!/usr/bin/env python3
"""Create source-derived podcast records from the DataTalks.Club podcast source."""

from __future__ import annotations

import argparse
from pathlib import Path

from extract_podcast_sources import KNOWN_ARCHIVE_TOPICS, candidate_topics, slugify
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


def clean_text(value: object) -> str:
    text = " ".join(str(value or "").split())
    return (
        text.replace("—", "-")
        .replace("–", "-")
        .replace("’", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace(" very ", " ")
        .replace(" Very ", " ")
        .replace("you are", "you're")
        .replace("You are", "You're")
        .replace(" shape ", " influence ")
        .replace(" Shape ", " Influence ")
    )


def sentence(value: object, max_chars: int = 360) -> str:
    text = clean_text(value)
    if "?" in text:
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0].rstrip(".") + "."


def concept_labels(podcast: dict[str, object]) -> list[str]:
    source_topics = podcast.get("topics")
    labels = [str(topic).strip() for topic in source_topics if str(topic).strip()] if isinstance(source_topics, list) else []
    if not labels:
        known = {topic.lower() for topic in KNOWN_ARCHIVE_TOPICS}
        wiki_dir = ROOT / "_wiki"
        labels = [
            topic
            for topic in candidate_topics(podcast)
            if topic.lower() in known or (wiki_dir / f"{slugify(topic)}.md").exists()
        ][:8]
    seen = set()
    concepts = []
    for label in labels:
        key = label.lower()
        if key in seen:
            continue
        seen.add(key)
        concepts.append(label)
    return concepts[:8]


def chapter_labels(podcast: dict[str, object], limit: int = 5) -> list[str]:
    chapters = podcast.get("chapters")
    if not isinstance(chapters, list):
        return []
    labels = []
    for chapter in chapters:
        if not isinstance(chapter, dict):
            continue
        label = clean_text(chapter.get("title"))
        if not label:
            continue
        if label.lower().startswith(("podcast introduction", "introduction", "closing", "wrap")):
            continue
        if label.lower().startswith("transcript checkpoint"):
            label = label.split(":", 1)[-1].strip()
        labels.append(label)
        if len(labels) >= limit:
            break
    return labels


def page_body(podcast: dict[str, object], people: dict[str, dict[str, object]]) -> str:
    slug = str(podcast["slug"])
    title = clean_text(podcast.get("title") or slug.replace("-", " ").title())
    concepts = concept_labels(podcast)
    lines = [
        f"# Episode: {title}",
        "",
        "## Source",
        "",
        f"- [DataTalks.Club episode]({podcast['source_url']})",
    ]

    links = podcast.get("links")
    if isinstance(links, dict):
        if links.get("youtube") and links["youtube"] != "TODO":
            lines.append(f"- [Watch on YouTube]({links['youtube']})")
        if links.get("spotify") and links["spotify"] != "TODO":
            lines.append(f"- [Listen on Spotify]({links['spotify']})")
        if links.get("apple") and links["apple"] != "TODO":
            lines.append(f"- [Listen on Apple Podcasts]({links['apple']})")

    guests = podcast.get("guests")
    if isinstance(guests, list) and guests:
        lines.extend(["", "## People", ""])
        lines.append("")
        for guest in guests:
            slug = str(guest or "").strip()
            if slug:
                lines.append(
                    f"- [{person_label(slug, people)}](https://datatalks.club/people/{slug}.html)"
                )

    lines.extend(["", "## Key Concepts", ""])
    if concepts:
        for concept in concepts:
            lines.append(f"- {concept}")
    else:
        lines.append("- No explicit topic metadata is available; use the chapter summary before relying on this episode.")

    chapters = podcast.get("chapters")
    lines.extend(["", "## Chapter Headers", ""])
    if isinstance(chapters, list) and chapters:
        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            label = clean_text(chapter.get("title"))
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

    lines.extend(["", "## Source File", "", f"- `{podcast.get('source_episode')}`"])

    return "\n".join(lines) + "\n"


def render_page(source: Path, target: Path, people: dict[str, dict[str, object]]) -> bool:
    podcast = read_podcast(source)
    links = podcast.get("links") if isinstance(podcast.get("links"), dict) else {}
    topics = podcast.get("topics")
    if not isinstance(topics, list) or not topics:
        topics = concept_labels(podcast)

    frontmatter = [
        "---",
        "layout: podcast_summary",
        f"title: {yaml_string(podcast['title'])}",
        f"source_episode: {yaml_string(podcast['source_episode'])}",
        f"source_url: {yaml_string(podcast['source_url'])}",
        f"season: {podcast.get('season', '')}",
        f"episode: {podcast.get('episode', '')}",
        f"guests: {yaml_list(podcast.get('guests'))}",
        f"topics: {yaml_list(topics)}",
        "summary_status: source-index",
    ]
    if isinstance(links, dict):
        for key in ("youtube", "spotify", "apple"):
            if links.get(key) and links[key] != "TODO":
                frontmatter.append(f"{key}_url: {yaml_string(links[key])}")
    frontmatter.extend(["---", "", ""])

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

    print(f"synced {total} podcast records, changed {changed}")


if __name__ == "__main__":
    main()
