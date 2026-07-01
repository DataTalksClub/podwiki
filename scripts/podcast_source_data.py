#!/usr/bin/env python3
"""Helpers for reading DataTalks.Club podcast source files."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PODCAST_SOURCE = ROOT.parent / "datatalksclub.github.io" / "_podcast"
DEFAULT_PEOPLE_SOURCE = ROOT.parent / "datatalksclub.github.io" / "_people"


def clean_value(value: object) -> str:
    text = str(value or "").strip().strip('"').strip("'")
    return text.replace('\\"', '"').replace("\\'", "'")


def yaml_string(value: object) -> str:
    text = str(value or "").replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def yaml_list(values: object) -> str:
    if not isinstance(values, list) or not values:
        return "[]"
    return "[" + ", ".join(yaml_string(value) for value in values) + "]"


def split_frontmatter(raw: str) -> tuple[dict[str, object], str, str]:
    if raw.startswith("_\n---\n"):
        raw = raw[2:]
    if not raw.startswith("---\n"):
        return {}, raw, ""
    end = raw.find("\n---", 4)
    if end == -1:
        return {}, raw, ""

    frontmatter_text = raw[4:end].strip()
    lines = frontmatter_text.splitlines()
    body = raw[end + 4 :].lstrip()
    meta: dict[str, object] = {}
    current_key: str | None = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            if not isinstance(meta.get(current_key), list):
                meta[current_key] = []
            meta[current_key].append(clean_value(stripped[2:]))
            continue
        if line.startswith(" ") and current_key:
            if isinstance(meta.get(current_key), dict):
                if ":" in stripped:
                    key, value = stripped.split(":", 1)
                    meta[current_key][key.strip()] = clean_value(value)
                continue
            if isinstance(meta.get(current_key), str):
                meta[current_key] = f"{meta[current_key]} {clean_value(stripped)}".strip()
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if not value:
            meta[key] = {}
        elif value.startswith("[") and value.endswith("]"):
            meta[key] = [clean_value(item) for item in value[1:-1].split(",") if clean_value(item)]
        else:
            meta[key] = clean_value(value)

    return meta, body, frontmatter_text


def parse_list_of_dicts(frontmatter: str, key: str) -> list[dict[str, str]]:
    lines = frontmatter.splitlines()
    in_block = False
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line in lines:
        if line.startswith(f"{key}:"):
            in_block = True
            continue
        if not in_block:
            continue
        if line and not line.startswith((" ", "-")):
            break
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            if current:
                items.append(current)
            current = {}
            stripped = stripped[2:].strip()
        if current is None or ":" not in stripped:
            continue
        item_key, value = stripped.split(":", 1)
        current[item_key.strip()] = clean_value(value)

    if current:
        items.append(current)
    return items


def first_paragraph(text: object, max_chars: int = 520) -> str:
    if not isinstance(text, str):
        return ""
    text = re.sub(r"<br\s*/?>", "\n\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    paragraphs = [re.sub(r"\s+", " ", part).strip() for part in re.split(r"\n\s*\n", text)]
    paragraph = next((part for part in paragraphs if part), "")
    if len(paragraph) <= max_chars:
        return paragraph
    return paragraph[:max_chars].rsplit(" ", 1)[0] + "."


def seconds_to_stamp(value: object) -> str:
    try:
        seconds = int(str(value))
    except ValueError:
        return ""
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{sec:02d}"
    return f"{minutes}:{sec:02d}"


def timestamp_url(base_url: object, seconds: object) -> str:
    url = clean_value(base_url)
    if not url:
        return ""
    try:
        sec = int(str(seconds))
    except ValueError:
        return url
    if "youtube.com/watch" in url:
        separator = "&" if "?" in url else "?"
        return f"{url}{separator}t={sec}"
    return url


def transcript_chapters(items: list[dict[str, str]], youtube_url: object) -> list[dict[str, str]]:
    chapters: list[dict[str, str]] = []
    pending: dict[str, str] | None = None

    for item in items:
        header = clean_value(item.get("header"))
        if header:
            if pending:
                pending["url"] = timestamp_url(youtube_url, pending.get("start", ""))
                chapters.append(pending)
            pending = {
                "title": header,
                "start": clean_value(item.get("sec")),
                "end": "",
                "time": clean_value(item.get("time")) or seconds_to_stamp(item.get("sec", "")),
                "url": "",
            }
            continue

        if pending and not pending["start"] and item.get("sec"):
            pending["start"] = clean_value(item.get("sec"))
            pending["time"] = clean_value(item.get("time")) or seconds_to_stamp(item.get("sec", ""))

    if pending:
        pending["url"] = timestamp_url(youtube_url, pending.get("start", ""))
        chapters.append(pending)

    return chapters


def transcript_fallback_chapters(
    items: list[dict[str, str]], youtube_url: object, limit: int = 12
) -> list[dict[str, str]]:
    """Create sparse navigational summaries when transcripts have no headers."""
    candidates = [
        item
        for item in items
        if clean_value(item.get("line")) and clean_value(item.get("sec"))
    ]
    if not candidates:
        return []

    if len(candidates) <= limit:
        selected = candidates
    else:
        step = (len(candidates) - 1) / (limit - 1)
        selected = [candidates[round(index * step)] for index in range(limit)]

    chapters = []
    for index, item in enumerate(selected, start=1):
        line = clean_value(item.get("line")).rstrip("\\").strip()
        excerpt = first_paragraph(line, max_chars=90)
        if not excerpt:
            continue
        start = clean_value(item.get("sec"))
        title = f"Transcript checkpoint {index}: {excerpt}"
        chapters.append(
            {
                "title": title,
                "start": start,
                "end": "",
                "time": clean_value(item.get("time")) or seconds_to_stamp(start),
                "url": timestamp_url(youtube_url, start),
            }
        )
    return chapters


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [clean_value(item) for item in value if clean_value(item)]
    if isinstance(value, str) and value.strip():
        return [clean_value(value)]
    return []


def should_skip_podcast(path: Path) -> bool:
    return path.name in {"README.md", "_template.md"}


def source_slug(path: Path) -> str:
    slug = path.stem.lstrip("_")
    if slug.endswith(".md"):
        slug = slug[:-3]
    return slug


def source_relative_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT.parent))
    except ValueError:
        return str(path)


def read_podcast(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    meta, body, frontmatter = split_frontmatter(raw)
    clips = parse_list_of_dicts(frontmatter, "quotableClips")
    transcript_items = parse_list_of_dicts(frontmatter, "transcript")
    links = meta.get("links") if isinstance(meta.get("links"), dict) else {}
    slug = source_slug(path)
    title = str(meta.get("title") or slug.replace("-", " ").title())
    intro = first_paragraph(meta.get("intro") or meta.get("description"))
    chapters = [
        {
            "title": clip.get("name", ""),
            "start": clip.get("startOffset", ""),
            "end": clip.get("endOffset", ""),
            "time": seconds_to_stamp(clip.get("startOffset", "")),
            "url": clip.get("url", ""),
        }
        for clip in clips
        if clip.get("name")
    ]
    if not chapters:
        chapters = transcript_chapters(transcript_items, links.get("youtube", ""))
    if not chapters:
        chapters = transcript_fallback_chapters(transcript_items, links.get("youtube", ""))

    return {
        "slug": slug,
        "title": title,
        "short": str(meta.get("short") or ""),
        "source_episode": source_relative_path(path),
        "source_url": f"https://datatalks.club/podcast/{slug}.html",
        "local_url": f"/podcasts/{slug}/",
        "season": str(meta.get("season") or ""),
        "episode": str(meta.get("episode") or ""),
        "guests": as_list(meta.get("guests")),
        "topics": as_list(meta.get("topics")),
        "description": first_paragraph(meta.get("description")),
        "intro": intro,
        "links": links,
        "chapters": chapters,
        "body": body,
    }


def read_people(source: Path = DEFAULT_PEOPLE_SOURCE) -> dict[str, dict[str, object]]:
    people: dict[str, dict[str, object]] = {}
    if not source.exists():
        return people

    for path in sorted(source.glob("*.md")):
        if path.name == "README.md" or path.name.startswith("_"):
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body, _ = split_frontmatter(raw)
        slug = path.stem
        people[slug] = {
            "slug": slug,
            "title": str(meta.get("title") or slug),
            "short": str(meta.get("short") or slug),
            "picture": str(meta.get("picture") or ""),
            "github": str(meta.get("github") or ""),
            "twitter": str(meta.get("twitter") or ""),
            "linkedin": str(meta.get("linkedin") or ""),
            "web": str(meta.get("web") or ""),
            "bio": first_paragraph(body, max_chars=700),
        }
    return people


def read_podcasts(source: Path = DEFAULT_PODCAST_SOURCE) -> list[dict[str, object]]:
    podcasts = []
    for path in sorted(source.glob("*.md")):
        if should_skip_podcast(path):
            continue
        podcasts.append(read_podcast(path))

    def sort_key(podcast: dict[str, object]) -> tuple[int, int, str]:
        def numeric(value: object) -> int:
            try:
                return int(str(value or "999"))
            except ValueError:
                return 999

        return (
            numeric(podcast.get("season")),
            numeric(podcast.get("episode")),
            str(podcast.get("slug") or ""),
        )

    return sorted(
        podcasts,
        key=sort_key,
    )
