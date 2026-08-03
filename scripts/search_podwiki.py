#!/usr/bin/env python3
"""Query the same packed Zerosearch index used by the Podwiki Lambda."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from search_lambda.podwiki_search import handler as search_handler  # noqa: E402


DEFAULT_INDEX = ROOT / "artifacts" / "search" / "search-index.zsx"
LEVELS = {
    "wiki",
    "guide",
    "comparison",
    "roadmap",
    "transition",
    "how_to",
    "podcast_summary",
    "person",
    "book",
}


def search(
    query: str,
    *,
    index_path: Path = DEFAULT_INDEX,
    level: str | None = None,
    document_type: str | None = None,
    limit: int = 10,
) -> list[dict]:
    """Return locally reranked results using the production search behavior."""
    if not index_path.exists():
        raise FileNotFoundError(f"search index not found: {index_path}; run `make index`")

    resolved_index = index_path.resolve()
    loaded_index = Path(search_handler.INDEX_PATH).resolve()
    if search_handler._INDEX is None or loaded_index != resolved_index:
        search_handler.INDEX_PATH = resolved_index
        search_handler._INDEX = None
        search_handler._STEM = None

    filters: dict[str, str] = {}
    if level:
        filters["level"] = level
    if document_type:
        filters["document_type"] = document_type

    results = search_handler.index().search(
        query,
        filter_dict=filters,
        boost_dict={"title": 4.0, "segment_title": 3.0, "text": 1.0},
        num_results=limit,
    )
    return search_handler.rerank_results(query, results)[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="search terms")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--level", choices=sorted(LEVELS))
    parser.add_argument("--document-type", choices=["page", "section"])
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    results = search(
        query,
        index_path=args.index,
        level=args.level,
        document_type=args.document_type,
        limit=max(1, args.limit),
    )

    if args.json:
        print(json.dumps({"query": query, "results": results}, indent=2, ensure_ascii=False))
        return

    for result in results:
        score = float(result.get("score", 0.0))
        level = str(result.get("level", ""))
        kind = str(result.get("document_type", ""))
        title = str(result.get("title", ""))
        url = str(result.get("url", ""))
        print(f"{score:8.2f}  {level:16} {kind:7}  {title}")
        print(f"          {url}")


if __name__ == "__main__":
    main()
