#!/usr/bin/env python3
"""Merge concept-extraction batch outputs into _events records.

Reads .tmp/events/concepts/batch-*.json (video_id -> topics/summary), validates
topic slugs against _wiki inventory (or an allowlist of deliberate new topic
labels), and writes them into the matching _events record frontmatter with
`summary_status: done`. Sync preserves these fields afterwards.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS_DIR = ROOT / ".tmp/events/concepts"
EVENTS_DIR = ROOT / "_events"

# Deliberate new topic labels accepted from the 2026-09 concept pass; see
# docs/taxonomy-log.md. They become `topic:<slug>` graph nodes until a wiki
# hub exists.
ALLOWED_NEW_TOPICS = {
    "bayesian-inference",
    "data-storytelling",
    "feature-selection",
    "geospatial-data",
    "knowledge-graphs",
    "llm-fine-tuning",
    "neuroscience-data-science",
    "prometheus",
    "terraform",
    "time-series-forecasting",
}


def wiki_slugs() -> set[str]:
    return {p.stem for p in (ROOT / "_wiki").glob("*.md") if p.stem != "README"}


def video_to_record() -> dict[str, Path]:
    """Map YouTube video ids to `_events` record paths via frontmatter."""
    by_video: dict[str, list[Path]] = {}
    for path in EVENTS_DIR.glob("*.md"):
        if path.stem == "README":
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^video_id:\s*"?([A-Za-z0-9_-]{11})"?', text, re.M)
        if match:
            by_video.setdefault(match.group(1), []).append(path)
    # Some videos map to two rows (a webinar plus the conference day that
    # included it). Prefer the pending record so curated ones keep their own
    # entry; a fully done pair simply keeps its first record.
    mapping: dict[str, Path] = {}
    for vid, paths in by_video.items():
        pending = [p for p in paths if "summary_status: done" not in p.read_text(encoding="utf-8")]
        mapping[vid] = (pending or paths)[0]
    return mapping


def merge() -> int:
    known = wiki_slugs() | ALLOWED_NEW_TOPICS
    mapping = video_to_record()
    problems: list[str] = []
    merged = 0
    for path in sorted(CONCEPTS_DIR.glob("batch-*.json")):
        if path.name.endswith(".requests.json"):
            continue
        entries = json.loads(path.read_text())
        for entry in entries:
            vid = entry.get("video_id")
            record = mapping.get(vid)
            if record is None:
                problems.append(f"{path.name}: no _events record for video {vid}")
                continue
            if "summary_status: done" in record.read_text(encoding="utf-8"):
                # Already curated (possibly by a concurrent pass); never clobber.
                continue
            topics = [str(t).strip() for t in entry.get("topics", []) if str(t).strip()]
            unknown = [t for t in topics if t not in known]
            if unknown:
                problems.append(f"{record.name}: unknown topic slugs {unknown}")
                continue
            if not topics:
                problems.append(f"{record.name}: no topics; left pending")
                continue
            summary = " ".join(str(entry.get("summary", "")).split())
            if not summary:
                problems.append(f"{record.name}: empty summary; left pending")
                continue
            text = record.read_text(encoding="utf-8")
            text = re.sub(
                r"^summary: .*$", f"summary: {json.dumps(summary)}", text, count=1, flags=re.M
            )
            text = re.sub(
                r"^topics: \[\]$",
                "topics: [" + ", ".join(json.dumps(t) for t in topics) + "]",
                text,
                count=1,
                flags=re.M,
            )
            text = text.replace("summary_status: pending", "summary_status: done")
            record.write_text(text, encoding="utf-8")
            merged += 1
    print(f"merged {merged} event records from {CONCEPTS_DIR}")
    for problem in problems:
        print(f"PROBLEM: {problem}", file=sys.stderr)
    return 1 if problems and merged == 0 else 0


if __name__ == "__main__":
    raise SystemExit(merge())
