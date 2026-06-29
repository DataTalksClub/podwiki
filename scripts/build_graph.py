#!/usr/bin/env python3
"""Build the static exploration graph from Podwiki collections."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "graph" / "graph.json"

COLLECTIONS = {
    "_wiki": ("wiki", "/wiki/"),
    "_articles": ("article", "/articles/"),
    "_podcast_summaries": ("podcast", "/podcasts/"),
    "_people": ("person", "/people/"),
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def clean_value(value: str) -> str:
    return value.strip().strip('"').strip("'")


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return [clean_value(value)] if value else []
    raw_items = re.findall(r'"([^"]+)"|\'([^\']+)\'|([^,\[\]]+)', value)
    items = []
    for quoted, single_quoted, bare in raw_items:
        item = clean_value(quoted or single_quoted or bare)
        if item:
            items.append(item)
    return items


def split_frontmatter(raw: str) -> tuple[dict[str, object], str]:
    if not raw.startswith("---\n"):
        return {}, raw
    end = raw.find("\n---", 4)
    if end == -1:
        return {}, raw
    frontmatter = raw[4:end].strip().splitlines()
    body = raw[end + 4 :].lstrip()
    meta: dict[str, object] = {}
    current_key: str | None = None

    for line in frontmatter:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(clean_value(stripped[2:]))
            continue
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        if not value:
            meta[current_key] = []
        elif value.startswith("[") and value.endswith("]"):
            meta[current_key] = parse_inline_list(value)
        else:
            meta[current_key] = clean_value(value)
    return meta, body


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)] if str(value).strip() else []


def plain_text(markdown: str) -> str:
    markdown = re.sub(r"```.*?```", " ", markdown, flags=re.S)
    markdown = re.sub(r"`([^`]*)`", r"\1", markdown)
    markdown = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", markdown)
    markdown = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", markdown)
    markdown = re.sub(r"\{\{.*?\}\}", " ", markdown)
    markdown = re.sub(r"<[^>]+>", " ", markdown)
    markdown = re.sub(r"^#+\s*", "", markdown, flags=re.M)
    markdown = re.sub(r"[*_>#|~-]", " ", markdown)
    return re.sub(r"\s+", " ", markdown).strip()


def read_pages() -> list[dict[str, object]]:
    pages = []
    for directory, (node_type, prefix) in COLLECTIONS.items():
        collection_dir = ROOT / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            title = str(meta.get("title") or path.stem.replace("-", " ").title())
            summary = str(meta.get("summary") or "")
            pages.append(
                {
                    "id": f"{node_type}:{path.stem}",
                    "type": node_type,
                    "slug": path.stem,
                    "title": title,
                    "label": title,
                    "url": f"{prefix}{path.stem}/",
                    "meta": meta,
                    "body": body,
                    "search": plain_text(" ".join([title, summary])),
                }
            )
    return pages


def collection_target(path: str) -> str | None:
    path = path.strip()
    liquid_match = re.search(r"'(/(?:wiki|articles|podcasts|people)/[^']+)'", path)
    if liquid_match:
        path = liquid_match.group(1)
    path = path.split("#", 1)[0]
    match = re.match(r"/(wiki|articles|podcasts|people)/([^/]+)/?", path)
    if not match:
        return None
    type_by_path = {
        "wiki": "wiki",
        "articles": "article",
        "podcasts": "podcast",
        "people": "person",
    }
    return f"{type_by_path[match.group(1)]}:{match.group(2)}"


def markdown_targets(body: str) -> list[str]:
    targets = []
    for href in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = collection_target(href)
        if target:
            targets.append(target)
    for href in re.findall(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", body):
        target = collection_target(href)
        if target:
            targets.append(target)
    return targets


def build_graph() -> dict[str, object]:
    pages = read_pages()
    nodes = []
    node_ids = set()
    title_to_id = {str(page["title"]).lower(): str(page["id"]) for page in pages}
    topic_labels: dict[str, str] = {}
    topic_counts: Counter[str] = Counter()
    link_weights: Counter[tuple[str, str, str]] = Counter()

    def add_link(source: str, target: str, kind: str, weight: int = 1) -> None:
        if source == target:
            return
        link_weights[(source, target, kind)] += weight

    def topic_id(label: str) -> str:
        normalized = re.sub(r"\s+", " ", label).strip()
        slug = slugify(normalized)
        topic_labels.setdefault(slug, normalized)
        topic_counts[slug] += 1
        return f"topic:{slug}"

    def target_for_label(label: str) -> str:
        return title_to_id.get(label.lower()) or topic_id(label)

    for page in pages:
        node = {
            "id": page["id"],
            "type": page["type"],
            "label": page["label"],
            "title": page["title"],
            "url": page["url"],
            "count": 1,
            "search": page["search"],
        }
        keyword = page["meta"].get("keyword") if isinstance(page["meta"], dict) else None
        if keyword:
            node["keyword"] = keyword
        nodes.append(node)
        node_ids.add(str(page["id"]))

    for page in pages:
        source = str(page["id"])
        meta = page["meta"]
        page_type = str(page["type"])
        if not isinstance(meta, dict):
            continue

        for label in as_list(meta.get("related")):
            add_link(source, target_for_label(label), f"{page_type}-related", 3)
        for label in as_list(meta.get("related_wiki")):
            add_link(source, target_for_label(label), f"{page_type}-wiki", 5)
        for label in as_list(meta.get("topics")):
            add_link(source, topic_id(label), f"{page_type}-topic", 2)
        for label in as_list(meta.get("expertise")):
            add_link(source, topic_id(label), f"{page_type}-expertise", 2)
        for guest in as_list(meta.get("guests")):
            add_link(source, f"person:{guest}", "podcast-person", 4)
        for episode in as_list(meta.get("podcast_episodes")):
            add_link(source, f"podcast:{episode}", "person-podcast", 4)
        for target in markdown_targets(str(page["body"])):
            add_link(source, target, f"{page_type}-link", 1)

    for slug, label in sorted(topic_labels.items()):
        nodes.append(
            {
                "id": f"topic:{slug}",
                "type": "topic",
                "label": label,
                "title": label,
                "url": "/wiki/",
                "count": topic_counts[slug],
                "search": label,
            }
        )
        node_ids.add(f"topic:{slug}")

    links = [
        {"source": source, "target": target, "kind": kind, "weight": weight}
        for (source, target, kind), weight in sorted(link_weights.items())
        if source in node_ids and target in node_ids
    ]

    counts = Counter(str(node["type"]) for node in nodes)
    return {
        "generated_at": "generated-by-scripts/build_graph.py",
        "counts": {
            "wikis": counts["wiki"],
            "articles": counts["article"],
            "podcasts": counts["podcast"],
            "persons": counts["person"],
            "topics": counts["topic"],
            "nodes": len(nodes),
            "links": len(links),
        },
        "nodes": sorted(nodes, key=lambda item: (str(item["type"]), str(item["label"]).lower())),
        "links": links,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    graph = build_graph()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "graph "
        f"{graph['counts']['nodes']} nodes, "
        f"{graph['counts']['links']} links -> {args.output}"
    )


if __name__ == "__main__":
    main()
