#!/usr/bin/env python3
"""Create source-derived event records from the DataTalks.Club events data.

The source of truth is ``../datatalksclub.github.io/_data/events.yaml``. Only
webinar, workshop, and conference rows become event records: podcast-type rows
are already covered by the podcast archive registry. Each record filename is
``<date>-<title-slug>.md``; the graph node slug matches the filename, and the
YouTube video id (when the recording exists) is stored as ``video_id`` so
chips and body links can resolve back to the event node.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

import yaml

from podcast_source_data import (
    DEFAULT_PEOPLE_SOURCE,
    ROOT,
    read_people,
    yaml_string,
)

DEFAULT_EVENT_SOURCE = ROOT.parent / "datatalksclub.github.io" / "_data" / "events.yaml"
DEFAULT_TARGET = ROOT / "_events"
EVENT_TYPES = {"webinar", "workshop", "conference"}
VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|embed/|shorts/)([A-Za-z0-9_-]{11})")
FALLBACK_SOURCE_URL = "https://datatalks.club/events.html"

# Fields a later agent/human may curate; sync preserves them so concept
# extraction work is not clobbered by a re-run.
CURATED_FIELDS = ("topics", "summary")


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def video_id(url: object) -> str | None:
    if not url:
        return None
    match = VIDEO_ID_RE.search(str(url))
    return match.group(1) if match else None


def person_label(slug: str, people: dict[str, dict[str, object]]) -> str:
    person = people.get(slug, {})
    title = str(person.get("title") or "").strip()
    if title:
        return title
    return slug.replace("-", " ").replace("_", " ").title()


def event_time(value: object) -> datetime | None:
    if isinstance(value, datetime):
        return value
    if value:
        try:
            return datetime.fromisoformat(str(value))
        except ValueError:
            return None
    return None


def event_slug(event: dict[str, object], taken: set[str]) -> str | None:
    moment = event_time(event.get("time"))
    title = str(event.get("title") or "").strip()
    if not moment or not title:
        return None
    base = f"{moment:%Y-%m-%d}-{slugify(title)}".strip("-")
    slug = base
    counter = 2
    while slug in taken:
        slug = f"{base}-{counter}"
        counter += 1
    taken.add(slug)
    return slug


def summary_line(event: dict[str, object], people: dict[str, dict[str, object]]) -> str:
    etype = str(event.get("type") or "event").strip().lower()
    moment = event_time(event.get("time"))
    speakers = [
        person_label(str(s).strip(), people)
        for s in (event.get("speakers") or [])
        if str(s).strip()
    ]
    parts = [etype.capitalize()]
    if moment:
        parts.append(f"on {moment:%Y-%m-%d}")
    if speakers:
        parts.append("with " + ", ".join(speakers))
    sentence = ", ".join(parts)
    return f"{sentence}."


def render_event(event: dict[str, object], slug: str, people: dict[str, dict[str, object]]) -> str:
    etype = str(event.get("type") or "event").strip().lower()
    moment = event_time(event.get("time"))
    youtube = str(event.get("youtube") or "").strip() or None
    registration = str(event.get("link") or "").strip() or None
    source_url = youtube or registration or FALLBACK_SOURCE_URL
    speakers = [str(s).strip() for s in (event.get("speakers") or []) if str(s).strip()]
    summary = summary_line(event, people)

    lines = [
        "---",
        "layout: event",
        f"title: {yaml_string(str(event.get('title') or slug))}",
        f"event_type: {etype}",
    ]
    if moment:
        lines.append(f"date: {moment:%Y-%m-%d %H:%M:%S}")
    if speakers:
        lines.append("speakers: [" + ", ".join(yaml_string(s) for s in speakers) + "]")
    lines.append(f"summary: {yaml_string(summary)}")
    lines.append(f'source_url: "{source_url}"')
    vid = video_id(youtube)
    if vid:
        lines.append(f'video_id: "{vid}"')
    if registration:
        lines.append(f'registration_url: "{registration}"')
    lines.append(f"recording_status: {'recorded' if youtube else 'upcoming'}")
    lines.append("topics: []")
    lines.append("summary_status: pending")
    lines.append("---")
    lines.append("")
    title = str(event.get("title") or slug)
    lines.append(f"# {title}")
    lines.append("")
    body = [summary]
    links = []
    if youtube:
        links.append(f"[Watch the recording]({youtube})")
    if registration:
        links.append(f"[Event page]({registration})")
    for speaker in speakers:
        links.append(
            f"[{person_label(speaker, people)}](https://datatalks.club/people/{speaker}.html)"
        )
    if links:
        body.append("- " + "\n- ".join(links))
    lines.extend(body)
    lines.append("")
    return "\n".join(lines)


def read_curated(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    if not match:
        return {}
    frontmatter = match.group(1)
    status = re.search(r"^summary_status:\s*(\S+)", frontmatter, re.M)
    if not status or status.group(1).strip() == "pending":
        return {}
    curated: dict[str, object] = {}
    for line in frontmatter.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in CURATED_FIELDS and value and value not in ("[]", '""'):
            curated[key] = value
    return curated


def expected_slugs(source: Path) -> set[str]:
    events = yaml.safe_load(source.read_text(encoding="utf-8")) or []
    taken: set[str] = set()
    slugs = set()
    for event in events:
        if str(event.get("type") or "").strip().lower() not in EVENT_TYPES:
            continue
        slug = event_slug(event, taken)
        if slug:
            slugs.add(slug)
    return slugs


def event_speakers(source: Path) -> set[str]:
    """All speaker slugs across every event row, including podcast-type rows."""
    events = yaml.safe_load(source.read_text(encoding="utf-8")) or []
    speakers: set[str] = set()
    for event in events:
        for speaker in event.get("speakers") or []:
            if isinstance(speaker, str) and speaker.strip():
                speakers.add(speaker.strip())
    return speakers


def sync(source: Path, target: Path, people_source: Path) -> int:
    events = yaml.safe_load(source.read_text(encoding="utf-8")) or []
    people = read_people(people_source)
    target.mkdir(parents=True, exist_ok=True)

    taken: set[str] = set()
    written = 0
    for event in events:
        etype = str(event.get("type") or "").strip().lower()
        if etype not in EVENT_TYPES:
            continue
        slug = event_slug(event, taken)
        if not slug:
            print(f"skip (no date/title): {event.get('title')!r}")
            continue
        curated = read_curated(target / f"{slug}.md")
        text = render_event(event, slug, people)
        if curated:
            text = text.replace("summary_status: pending", "summary_status: done")
            for key, value in curated.items():
                text = re.sub(rf"^{key}: .*$", f"{key}: {value}", text, count=1, flags=re.M)
        (target / f"{slug}.md").write_text(text, encoding="utf-8")
        written += 1

    expected = expected_slugs(source)
    stale = sorted(p.stem for p in target.glob("*.md") if p.stem != "README" and p.stem not in expected)
    print(f"events: wrote {written} records to {target}")
    for slug in stale:
        print(f"stale (not in source, remove manually) - {slug}.md")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event-source", type=Path, default=DEFAULT_EVENT_SOURCE)
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    args = parser.parse_args()
    return sync(args.event_source, args.target, args.people_source)


if __name__ == "__main__":
    raise SystemExit(main())
