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
    "a",
    "about",
    "and",
    "are",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "s",
    "the",
    "to",
    "vs",
    "versus",
    "with",
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
FILLER_TOPIC_WORDS = {
    "background",
    "brought",
    "closing",
    "checkpoint",
    "event",
    "everyone",
    "guest",
    "intro",
    "introduction",
    "transcript",
    "podcast",
    "q&a",
    "questions",
    "resources",
    "welcome",
}
KNOWN_ARCHIVE_TOPICS = [
    "a/b testing",
    "academic research",
    "ai engineering",
    "ai engineer",
    "ai infrastructure",
    "analytics engineering",
    "career break",
    "career growth",
    "career transition",
    "causal inference",
    "cloud governance",
    "community building",
    "computer vision",
    "data engineering",
    "data governance",
    "data mesh",
    "data observability",
    "data product",
    "data quality",
    "data science",
    "data strategy",
    "data teams",
    "dataops",
    "developer relations",
    "embeddings",
    "experimentation",
    "feature store",
    "freelance",
    "generative ai",
    "hiring",
    "job search",
    "knowledge graphs",
    "leadership",
    "llm evaluation",
    "llmops",
    "llms",
    "machine learning",
    "ml engineering",
    "ml platform",
    "mlops",
    "model monitoring",
    "open source",
    "orchestration",
    "portfolio",
    "privacy",
    "product analytics",
    "product management",
    "rag",
    "reproducibility",
    "retrieval",
    "search",
    "software engineering",
    "team building",
    "technical writing",
    "vector databases",
]
TOPIC_ALIASES = {
    "open-source": "open source",
    "retrieval augmented generation": "retrieval-augmented generation",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def normalize_topic(value: str) -> str:
    topic = re.sub(r"\s+", " ", value.strip().lower())
    topic = topic.replace(" & ", " and ")
    return TOPIC_ALIASES.get(topic, topic)


def valid_topic_phrase(phrase: str) -> bool:
    tokens = phrase.split()
    if not tokens:
        return False
    if tokens[0] in STOPWORDS or tokens[-1] in STOPWORDS:
        return False
    if any(token in FILLER_TOPIC_WORDS for token in tokens):
        return False
    if sum(1 for token in tokens if len(token) <= 2 and token not in {"ai", "ml"}) > 0:
        return False
    return len(phrase) >= 8


def searchable_episode_text(episode: dict[str, object]) -> str:
    parts = [
        str(episode.get("title") or ""),
        str(episode.get("short") or ""),
        str(episode.get("intro") or ""),
        str(episode.get("description") or ""),
    ]
    chapters = episode.get("chapters")
    if isinstance(chapters, list):
        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            title = str(chapter.get("title") or "")
            if title.lower().startswith("transcript checkpoint"):
                title = title.split(":", 1)[-1]
            parts.append(title)
    return normalize_topic(" ".join(parts))


def candidate_topics(episode: dict[str, object]) -> list[str]:
    topics: Counter[str] = Counter()
    for topic in episode.get("topics", []):
        if isinstance(topic, str) and topic.strip():
            topics[normalize_topic(topic)] += 12

    episode_text = searchable_episode_text(episode)
    for topic in KNOWN_ARCHIVE_TOPICS:
        if normalize_topic(topic) in episode_text:
            topics[normalize_topic(topic)] += 6

    for chapter in episode.get("chapters", []):
        if not isinstance(chapter, dict):
            continue
        title = str(chapter.get("title") or "").lower()
        if title.startswith("transcript checkpoint"):
            continue
        title = re.sub(r"[^a-z0-9+.#/ -]+", " ", title)
        tokens = [token for token in re.split(r"\s+", title) if token and token not in STOPWORDS]
        for size in (3, 2):
            for index in range(0, max(0, len(tokens) - size + 1)):
                phrase = normalize_topic(" ".join(tokens[index : index + size]))
                if valid_topic_phrase(phrase):
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
