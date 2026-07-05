#!/usr/bin/env python3
"""Audit generated graph connectivity for weakly linked public wiki nodes."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPH = ROOT / "graph" / "graph.json"


def load_graph(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def wiki_nodes(graph: dict[str, object]) -> list[dict[str, object]]:
    nodes = graph.get("nodes", [])
    if not isinstance(nodes, list):
        raise SystemExit("graph nodes must be a list")
    return [node for node in nodes if isinstance(node, dict) and str(node.get("id", "")).startswith("wiki:")]


def inbound_counts(graph: dict[str, object]) -> Counter[str]:
    links = graph.get("links", [])
    if not isinstance(links, list):
        raise SystemExit("graph links must be a list")
    counts: Counter[str] = Counter()
    for link in links:
        if not isinstance(link, dict):
            continue
        target = link.get("target")
        if isinstance(target, str):
            counts[target] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH, help="Path to graph JSON")
    parser.add_argument(
        "--min-inbound",
        type=int,
        default=6,
        help="Report wiki nodes with fewer than this many inbound links",
    )
    parser.add_argument("--limit", type=int, default=30, help="Maximum rows to print")
    parser.add_argument(
        "--fail",
        action="store_true",
        help="Exit non-zero when weak wiki nodes are found",
    )
    args = parser.parse_args()

    graph = load_graph(args.graph)
    inbound = inbound_counts(graph)
    weak = sorted(
        (
            inbound[node_id],
            node_id,
            str(node.get("title", "")),
            str(node.get("type", "")),
        )
        for node in wiki_nodes(graph)
        for node_id in [str(node.get("id", ""))]
        if inbound[node_id] < args.min_inbound
    )

    print(f"graph: {args.graph}")
    counts = graph.get("counts")
    if isinstance(counts, dict):
        print(
            "counts: "
            + ", ".join(f"{key}={value}" for key, value in counts.items() if key in {"nodes", "links", "wikis", "articles"})
        )
    print(f"weak wiki nodes: {len(weak)} below {args.min_inbound} inbound links")

    for count, node_id, title, node_type in weak[: args.limit]:
        print(f"{count}\t{node_id}\t{title}\t{node_type}")

    if len(weak) > args.limit:
        print(f"... {len(weak) - args.limit} more")

    return 1 if args.fail and weak else 0


if __name__ == "__main__":
    raise SystemExit(main())
