#!/usr/bin/env python3
"""Audit source-derived podcast summaries for agent usability."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


def audit() -> list[str]:
    failures: list[str] = []

    for path in sorted(SUMMARY_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "Transcript checkpoint" in text:
            failures.append(f"{path.relative_to(ROOT)}: contains Transcript checkpoint label")

    for path in sorted(SUMMARY_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        agent_summary = section(text, "Agent Summary")
        if not agent_summary:
            failures.append(f"{path.relative_to(ROOT)}: missing Agent Summary")
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
