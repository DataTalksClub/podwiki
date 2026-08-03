#!/usr/bin/env python3
"""Prepare a reviewable source-and-search worksheet for one podcast episode."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

from podcast_source_data import DEFAULT_PODCAST_SOURCE, read_podcast
from search_podwiki import DEFAULT_INDEX, search


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / ".tmp" / "episode-integration"
PUBLIC_LEVELS = {"wiki", "guide", "comparison", "roadmap", "transition", "how_to"}


def resolve_episode(slug: str, source_dir: Path) -> Path:
    exact = source_dir / f"{slug}.md"
    if exact.exists():
        return exact
    matches = sorted(source_dir.glob(f"*{slug}*.md"))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise FileNotFoundError(f"episode source not found for {slug!r} in {source_dir}")
    choices = ", ".join(path.stem for path in matches)
    raise ValueError(f"episode selector {slug!r} is ambiguous: {choices}")


def query_candidates(podcast: dict[str, object], limit: int) -> list[str]:
    raw = [*podcast.get("topics", []), *(chapter["title"] for chapter in podcast.get("chapters", []))]
    queries = []
    seen = set()
    for value in raw:
        query = re.sub(r"\s+", " ", str(value)).strip()
        normalized = query.casefold()
        if len(query) < 3 or normalized in seen:
            continue
        seen.add(normalized)
        queries.append(query)
        if len(queries) >= limit:
            break
    return queries


def result_path(result: dict) -> str:
    graph_id = str(result.get("graph_id", ""))
    if graph_id.startswith("wiki:"):
        return f"_wiki/{graph_id.split(':', 1)[1]}.md"
    if graph_id.startswith("podcast:"):
        return f"_podcast_summaries/{graph_id.split(':', 1)[1]}.md"
    return str(result.get("url", ""))


def public_results(query: str, index_path: Path, kind: str, limit: int) -> list[dict]:
    candidates = search(
        query,
        index_path=index_path,
        document_type=kind,
        limit=max(25, limit * 5),
    )
    filtered = [result for result in candidates if result.get("level") in PUBLIC_LEVELS]
    return filtered[:limit]


def related_episode_results(
    query: str, index_path: Path, exclude_slug: str, limit: int
) -> list[dict]:
    candidates = search(
        query,
        index_path=index_path,
        level="podcast_summary",
        document_type="page",
        limit=max(15, limit * 4),
    )
    return [result for result in candidates if result.get("episode_slug") != exclude_slug][:limit]


def render_results(results: list[dict]) -> list[str]:
    if not results:
        return ["- No strong existing match found."]
    lines = []
    for result in results:
        score = float(result.get("score", 0.0))
        title = str(result.get("title", ""))
        lines.append(f"- `{result_path(result)}` — {title} (search score {score:.2f})")
    return lines


def render_worksheet(
    podcast: dict[str, object],
    source_path: Path,
    index_path: Path,
    max_queries: int,
    results_per_query: int,
) -> str:
    slug = str(podcast["slug"])
    lines = [
        f"# Episode integration: {podcast['title']}",
        "",
        f"- Episode: `{slug}`",
        f"- Canonical URL: {podcast['source_url']}",
        f"- Source file: `{source_path}`",
        f"- Prepared: {date.today().isoformat()}",
        f"- Topics from source: {', '.join(podcast.get('topics', [])) or 'none'}",
        "",
        "This worksheet is a temporary review aid. The durable result belongs in synthesized "
        "`_wiki/` prose, or in `sources/episode-integration-decisions.json` when review finds "
        "nothing worth integrating.",
        "",
        "## Review rules",
        "",
        "- Treat a guest's factual statement as a claim until the transcript or another source supports it.",
        "- Keep facts, definitions, opinions, recommendations, experiences, predictions, and agent inferences distinct.",
        "- Preserve the speaker and timestamp for every atomic item.",
        "- Search before creating a page; prefer extending a focused existing page.",
        "- Integrate ideas as readable synthesis with sentence-final citation links, not as a transcript dump.",
        "",
        "## Transcript navigation",
        "",
    ]
    for chapter in podcast.get("chapters", []):
        stamp = chapter.get("time") or "unknown"
        lines.append(f"- {stamp} — {chapter.get('title', '')}")

    lines.extend(["", "## Existing Podwiki matches", ""])
    for query in query_candidates(podcast, max_queries):
        lines.extend([f"### Search: {query}", "", "Pages:"])
        lines.extend(render_results(public_results(query, index_path, "page", results_per_query)))
        lines.extend(["", "Sections:"])
        lines.extend(render_results(public_results(query, index_path, "section", results_per_query)))
        lines.extend(["", "Related episode summaries:"])
        lines.extend(
            render_results(
                related_episode_results(query, index_path, slug, min(2, results_per_query))
            )
        )
        lines.append("")

    lines.extend(
        [
            "## Atomic evidence",
            "",
            "Create one block per useful statement or concept. IDs should be stable within this worksheet "
            "(`E01`, `E02`, and so on).",
            "",
            "### E01",
            "",
            "- Kind: `fact_claim | definition | opinion | recommendation | experience | tradeoff | prediction | open_question`",
            "- Speaker:",
            "- Timestamp:",
            "- Atomic statement:",
            "- Transcript support:",
            "- Evidence form: `paraphrase | short_quote | agent_inference`",
            "- Confidence or uncertainty:",
            "- Concepts and entities:",
            "- Candidate target:",
            "- Proposed action: `support_existing | extend_existing | revise_conflict | create_page | cross_link | no_change`",
            "",
            "## Integration plan",
            "",
            "For each retained evidence ID, record the target page and section, the prose change, and why "
            "the evidence adds something that is not already present.",
            "",
            "## New-page gate",
            "",
            "Create a page only when the concept is not a near-duplicate, is important beyond this episode, "
            "can support at least three subtopics, and has enough podcast evidence to ground a focused page. "
            "Otherwise extend an existing page or record `reviewed_no_change`.",
            "",
            "## Completion checklist",
            "",
            "- [ ] Every retained claim has a speaker and timestamp.",
            "- [ ] Existing pages and sections were searched before proposing a new page.",
            "- [ ] Wiki prose synthesizes evidence and uses canonical citation chips.",
            "- [ ] Related wiki pages are cross-linked where useful.",
            "- [ ] A no-change review is recorded in the decisions file with a reason.",
            "- [ ] `make wiki-links` and `make check` pass.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episode", help="canonical episode slug or a unique substring")
    parser.add_argument("--source", type=Path, default=DEFAULT_PODCAST_SOURCE)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-queries", type=int, default=12)
    parser.add_argument("--results-per-query", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source_path = resolve_episode(args.episode, args.source)
    podcast = read_podcast(source_path)
    output = args.output or DEFAULT_OUTPUT_DIR / f"{podcast['slug']}.md"
    if output.exists() and not args.force:
        raise FileExistsError(f"worksheet already exists: {output}; pass --force to replace it")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_worksheet(
            podcast,
            source_path,
            args.index,
            max(1, args.max_queries),
            max(1, args.results_per_query),
        ),
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
