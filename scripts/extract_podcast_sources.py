#!/usr/bin/env python3
"""Extract podcast episodes, people, chapters, and topic candidates for agents."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from podcast_source_data import DEFAULT_PODCAST_SOURCE, DEFAULT_PEOPLE_SOURCE, ROOT, read_people, read_podcasts


DEFAULT_OUTPUT = ROOT / "artifacts" / "podcast" / "source-index.json"
DEFAULT_AGENT_OUTPUT = ROOT / ".tmp" / "podcast-source-index.json"
STOPWORDS = {
    "and",
    "for",
    "from",
    "into",
    "with",
    "the",
    "how",
    "what",
    "why",
    "when",
    "where",
    "guest",
    "episode",
    "introduction",
    "overview",
    "closing",
    "resources",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def candidate_topics(episode: dict[str, object]) -> list[str]:
    topics: Counter[str] = Counter()
    for topic in episode.get("topics", []):
        if isinstance(topic, str) and topic.strip():
            topics[topic.strip().lower()] += 8

    for chapter in episode.get("chapters", []):
        if not isinstance(chapter, dict):
            continue
        title = str(chapter.get("title") or "").lower()
        title = re.sub(r"[^a-z0-9+.#/ -]+", " ", title)
        tokens = [token for token in re.split(r"\s+", title) if token and token not in STOPWORDS]
        for size in (3, 2):
            for index in range(0, max(0, len(tokens) - size + 1)):
                phrase = " ".join(tokens[index : index + size]).strip()
                if len(phrase) >= 8:
                    topics[phrase] += size
    return [topic for topic, _ in topics.most_common(12)]


def build_index(podcast_source: Path, people_source: Path) -> dict[str, object]:
    episodes = read_podcasts(podcast_source)
    people = read_people(people_source)
    appearances: dict[str, list[dict[str, str]]] = defaultdict(list)
    topic_to_episodes: dict[str, list[dict[str, str]]] = defaultdict(list)

    episode_docs = []
    for episode in episodes:
        candidates = candidate_topics(episode)
        for guest in episode.get("guests", []):
            if not isinstance(guest, str):
                continue
            appearances[guest].append(
                {
                    "episode": str(episode["slug"]),
                    "title": str(episode["title"]),
                    "local_url": str(episode["local_url"]),
                }
            )
        for topic in candidates:
            topic_to_episodes[topic].append(
                {
                    "episode": str(episode["slug"]),
                    "title": str(episode["title"]),
                    "local_url": str(episode["local_url"]),
                }
            )
        episode_docs.append(
            {
                "slug": episode["slug"],
                "title": episode["title"],
                "local_url": episode["local_url"],
                "source_url": episode["source_url"],
                "season": episode["season"],
                "episode": episode["episode"],
                "guests": episode["guests"],
                "topics": episode["topics"],
                "topic_candidates": candidates,
                "chapter_summary": episode["chapters"],
                "summary": episode.get("intro") or episode.get("description") or "",
            }
        )

    people_docs = []
    for slug in sorted(set(people) | set(appearances)):
        person = people.get(slug, {"slug": slug, "title": slug, "bio": ""})
        people_docs.append(
            {
                "slug": slug,
                "title": person.get("title") or slug,
                "local_url": f"/people/{slug}/",
                "source_url": f"https://datatalks.club/people/{slug}.html",
                "bio": person.get("bio") or "",
                "podcast_episodes": appearances.get(slug, []),
            }
        )

    topic_docs = [
        {
            "slug": slugify(topic),
            "topic": topic,
            "episodes": items[:12],
            "count": len(items),
        }
        for topic, items in sorted(topic_to_episodes.items(), key=lambda item: (-len(item[1]), item[0]))
    ]

    return {
        "source": str(podcast_source),
        "counts": {
            "episodes": len(episode_docs),
            "people": len(people_docs),
            "topics": len(topic_docs),
        },
        "episodes": episode_docs,
        "people": people_docs,
        "topics": topic_docs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--podcast-source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--people-source", type=Path, default=DEFAULT_PEOPLE_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--agent-output", type=Path, default=DEFAULT_AGENT_OUTPUT)
    args = parser.parse_args()

    index = build_index(args.podcast_source, args.people_source)
    for output in (args.output, args.agent_output):
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        "extracted "
        f"{index['counts']['episodes']} episodes, "
        f"{index['counts']['people']} people, "
        f"{index['counts']['topics']} topic candidates"
    )
    print(f"wrote {args.output}")
    print(f"wrote {args.agent_output}")


if __name__ == "__main__":
    main()
