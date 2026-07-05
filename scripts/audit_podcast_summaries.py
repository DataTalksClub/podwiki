#!/usr/bin/env python3
"""Audit source-derived podcast summaries for agent usability."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_INDEX = ROOT / "artifacts/podcast/source-index.json"
SUMMARY_DIR = ROOT / "_podcast_summaries"

REQUIRED_AGENT_BULLETS = (
    "- Why it matters:",
    "- Useful for:",
    "- Probably skip if:",
)


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:].strip()
    return text[start:next_start].strip()


def empty_source_summary_slugs() -> list[str]:
    data = json.loads(SOURCE_INDEX.read_text(encoding="utf-8"))
    episodes = data.get("episodes", [])
    slugs: list[str] = []
    for episode in episodes:
        if not isinstance(episode, dict):
            continue
        if not str(episode.get("summary") or "").strip():
            slugs.append(str(episode.get("slug") or "").strip())
    return sorted(slug for slug in slugs if slug)


def audit() -> list[str]:
    failures: list[str] = []

    for path in sorted(SUMMARY_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "Transcript checkpoint" in text:
            failures.append(f"{path.relative_to(ROOT)}: contains Transcript checkpoint label")

    for slug in empty_source_summary_slugs():
        path = SUMMARY_DIR / f"{slug}.md"
        if not path.exists():
            failures.append(f"{path.relative_to(ROOT)}: missing summary record")
            continue
        text = path.read_text(encoding="utf-8")
        agent_summary = section(text, "Agent Summary")
        if not agent_summary:
            failures.append(f"{path.relative_to(ROOT)}: missing Agent Summary for empty source summary")
            continue
        if not (
            text.find("## Key Concepts") < text.find("## Agent Summary") < text.find("## Chapter Headers")
        ):
            failures.append(f"{path.relative_to(ROOT)}: Agent Summary must sit between concepts and chapters")
        bullets = [line for line in agent_summary.splitlines() if line.startswith("- ")]
        if len(bullets) != 3:
            failures.append(f"{path.relative_to(ROOT)}: expected 3 Agent Summary bullets, got {len(bullets)}")
            continue
        for required in REQUIRED_AGENT_BULLETS:
            if not any(line.startswith(required) for line in bullets):
                failures.append(f"{path.relative_to(ROOT)}: missing Agent Summary bullet {required}")

    return failures


def main() -> None:
    failures = audit()
    if failures:
        print("podcast summary audit failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("podcast summary audit passed")


if __name__ == "__main__":
    main()
