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
        if label.lower().startswith("transcript excerpt"):
            label = label.split(":", 1)[-1].strip()
        labels.append(label)
        if len(labels) >= limit:
            break
    return labels


def agent_summary_section(podcast: dict[str, object], people: dict[str, dict[str, object]]) -> str:
    title = clean_text(podcast.get("title") or podcast.get("slug") or "this episode")
    source_summary = sentence(
        podcast.get("short") or podcast.get("intro") or podcast.get("description"),
        max_chars=340,
    )
    concepts = concept_labels(podcast)
    chapters = chapter_labels(podcast, limit=4)
    guest_slugs = podcast.get("guests")
    guest_names = []
    if isinstance(guest_slugs, list):
        guest_names = [person_label(str(slug), people) for slug in guest_slugs if str(slug).strip()]

    if source_summary:
        why = source_summary
    elif concepts:
        why = f"Connects {', '.join(concepts[:3])} to a DataTalks.Club podcast discussion."
    else:
        why = f"Source-derived record for {title}."

    useful_bits = []
    if concepts:
        useful_bits.append(", ".join(concepts[:4]))
    if chapters:
        useful_bits.append("; ".join(chapters[:3]))
    useful_for = "Future agents triaging " + " and ".join(useful_bits) + "."
    if not useful_bits:
        useful_for = "Future agents deciding whether to open the source episode for transcript-level evidence."

    skip_bits = []
    if guest_names:
        skip_bits.append(f"you do not need material from {', '.join(guest_names[:2])}")
    if concepts:
        skip_bits.append(f"you are not working on {', '.join(concepts[:3])}")
    if skip_bits:
        probably_skip = "Probably skip if: " + " or ".join(skip_bits) + "."
    else:
        probably_skip = (
            "Probably skip if: you need a different domain or a transcript-verified quote "
            "rather than source-index triage."
        )

    return "\n".join(
        [
            "## Agent Summary",
            "",
            f"- Why it matters: {why}",
            f"- Useful for: {useful_for}",
            f"- {probably_skip}",
        ]
    )


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
        lines.append("- No explicit topic metadata is available. Use the chapter summary before relying on this episode.")

    lines.extend(["", agent_summary_section(podcast, people)])

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


def markdown_section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:].strip()
    return text[start:next_start].strip()


def insert_before_heading(text: str, heading: str, section: str) -> str:
    marker = f"\n## {heading}\n"
    index = text.find(marker)
    if index == -1:
        return text.rstrip() + "\n\n" + section.strip() + "\n"
    return text[: index + 1] + section.strip() + "\n\n" + text[index + 1 :]


def replace_section(text: str, heading: str, section: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return text
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[:start] + section.strip() + "\n"
    return text[:start] + section.strip() + "\n" + text[next_start:]


def preserve_curated_sections(rendered: str, existing: str, generated_has_fallback: bool = False) -> str:
    agent_summary = markdown_section(existing, "Agent Summary")
    if agent_summary:
        rendered = replace_section(rendered, "Agent Summary", agent_summary)

    existing_chapters = markdown_section(existing, "Chapter Headers")
    generated_chapters = markdown_section(rendered, "Chapter Headers")
    generated_is_fallback = (
        generated_has_fallback
        or "Transcript checkpoint" in generated_chapters
        or "Transcript excerpt" in generated_chapters
    )
    if existing_chapters and "Transcript checkpoint" not in existing_chapters and generated_is_fallback:
        rendered = replace_section(rendered, "Chapter Headers", existing_chapters)

    return rendered


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
    if target.exists():
        chapters = podcast.get("chapters")
        generated_has_fallback = any(
            isinstance(chapter, dict) and bool(chapter.get("fallback"))
            for chapter in chapters
        ) if isinstance(chapters, list) else False
        rendered = preserve_curated_sections(
            rendered,
            target.read_text(encoding="utf-8"),
            generated_has_fallback=generated_has_fallback,
        )
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
