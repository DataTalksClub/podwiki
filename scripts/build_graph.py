#!/usr/bin/env python3
"""Build the static exploration graph from Podwiki collections."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "graph" / "graph.json"

COLLECTIONS = {
    "_wiki": ("wiki", "/wiki/", "wiki"),
    "_guides": ("article", "/guides/", "guide"),
    "_comparisons": ("article", "/comparisons/", "comparison"),
    "_roadmaps": ("article", "/roadmaps/", "roadmap"),
    "_how_tos": ("article", "/how-tos/", "how_to"),
    "_podcast_summaries": ("podcast", "/podcasts/", "podcast"),
    "_books": ("book", "/books/", "book"),
    "_people": ("person", "/people/", "person"),
}

TARGET_TYPES = {
    "wiki": ("wiki", "wiki"),
    "guides": ("article", "guide"),
    "comparisons": ("article", "comparison"),
    "roadmaps": ("article", "roadmap"),
    "how-tos": ("article", "how_to"),
    "podcasts": ("podcast", "podcast"),
    "books": ("book", "book"),
    "people": ("person", "person"),
}

# podcast/person/book pages are not published locally; wiki bodies link straight
# to the canonical main-site URL. Map those canonical URLs back to node ids so
# the graph edges survive. Note the singular `/podcast/` path on the main site.
CANONICAL_URL_RE = re.compile(
    r"https?://(?:www\.)?datatalks\.club/(podcast|people|books)/([^/#?\"'\s]+?)\.html",
    re.IGNORECASE,
)
CANONICAL_TYPES = {
    "podcast": ("podcast", "podcast"),
    "people": ("person", "person"),
    "books": ("book", "book"),
}

# Collections that resolve to the canonical main-site URL instead of a local page.
CANONICAL_NODE_TYPES = {"podcast", "person", "book"}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def source_slug(path: Path) -> str:
    slug = path.stem
    if slug.endswith(".md"):
        slug = slug[:-3]
    return slug


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


def node_id(node_type: str, id_scope: str, slug: str) -> str:
    if node_type == "article":
        return f"{node_type}:{id_scope}:{slug}"
    return f"{node_type}:{slug}"


def read_pages() -> list[dict[str, object]]:
    pages = []
    for directory, (node_type, prefix, id_scope) in COLLECTIONS.items():
        collection_dir = ROOT / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            if meta.get("redirect_to") or str(meta.get("published", "")).lower() == "false":
                continue
            slug = source_slug(path)
            title = str(meta.get("title") or slug.replace("-", " ").title())
            summary = str(meta.get("summary") or "")
            canonical = str(meta.get("source_url") or "").strip()
            if node_type in CANONICAL_NODE_TYPES and canonical:
                url = canonical
            else:
                url = f"{prefix}{slug}/"
            pages.append(
                {
                    "id": node_id(node_type, id_scope, slug),
                    "type": node_type,
                    "collection": id_scope,
                    "slug": slug,
                    "title": title,
                    "label": title,
                    "url": url,
                    "meta": meta,
                    "body": body,
                    "search": plain_text(" ".join([title, summary])),
                }
            )
    return pages


def collection_target(path: str) -> str | None:
    path = path.strip()
    canonical = CANONICAL_URL_RE.search(path)
    if canonical:
        node_type, id_scope = CANONICAL_TYPES[canonical.group(1).lower()]
        return node_id(node_type, id_scope, canonical.group(2))
    public_paths = "|".join(re.escape(name) for name in TARGET_TYPES)
    liquid_match = re.search(rf"'(/(?:{public_paths})/[^']+)'", path)
    if liquid_match:
        path = liquid_match.group(1)
    path = path.split("#", 1)[0]
    match = re.match(rf"/({public_paths})/([^/]+)/?", path)
    if not match:
        return None
    target_type, id_scope = TARGET_TYPES[match.group(1)]
    return node_id(target_type, id_scope, match.group(2))


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
    title_to_pages: dict[str, list[dict[str, object]]] = {}
    slug_to_pages: dict[str, list[dict[str, object]]] = {}
    for page in pages:
        title_to_pages.setdefault(str(page["title"]).lower(), []).append(page)
        slug_to_pages.setdefault(str(page["slug"]).lower(), []).append(page)
    wiki_title_to_page = {
        str(page["title"]).lower(): page for page in pages if str(page["collection"]) == "wiki"
    }
    wiki_slug_to_page = {
        str(page["slug"]).lower(): page for page in pages if str(page["collection"]) == "wiki"
    }
    topic_labels: dict[str, str] = {}
    topic_counts: Counter[str] = Counter()
    link_weights: Counter[tuple[str, str, str]] = Counter()

    def add_link(source: str, target: str, kind: str, weight: int = 1) -> None:
        if source == target:
            return
        link_weights[(source, target, kind)] += weight

    def wiki_page_for_label(label: str) -> dict[str, object] | None:
        normalized = re.sub(r"\s+", " ", label).strip()
        return wiki_title_to_page.get(normalized.lower()) or wiki_slug_to_page.get(slugify(normalized))

    def topic_id(label: str) -> str:
        normalized = re.sub(r"\s+", " ", label).strip()
        wiki_page = wiki_page_for_label(normalized)
        if wiki_page:
            return str(wiki_page["id"])
        slug = slugify(normalized)
        topic_labels.setdefault(slug, normalized)
        topic_counts[slug] += 1
        return f"topic:{slug}"

    def target_for_label(
        label: str,
        source_collection: str | None = None,
        prefer_wiki: bool = False,
    ) -> str:
        normalized = re.sub(r"\s+", " ", label).strip()
        candidates = title_to_pages.get(normalized.lower()) or slug_to_pages.get(slugify(normalized))
        if not candidates:
            return topic_id(normalized)

        if prefer_wiki:
            collection_order = ["wiki", source_collection]
        else:
            collection_order = [source_collection, "wiki"]
        collection_order.extend(["guide", "comparison", "roadmap", "how_to", "podcast", "person"])
        for collection in [item for item in collection_order if item]:
            for candidate in candidates:
                if str(candidate["collection"]) == collection:
                    return str(candidate["id"])
        return str(candidates[0]["id"])

    for page in pages:
        node = {
            "id": page["id"],
            "type": page["type"],
            "collection": page["collection"],
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

        collection = str(page["collection"])
        for label in as_list(meta.get("related")):
            add_link(source, target_for_label(label, collection), f"{page_type}-related", 3)
        for label in as_list(meta.get("related_wiki")):
            add_link(source, target_for_label(label, collection, prefer_wiki=True), f"{page_type}-wiki", 5)
        for label in as_list(meta.get("topics")):
            add_link(source, topic_id(label), f"{page_type}-topic", 2)
        for label in as_list(meta.get("expertise")):
            add_link(source, topic_id(label), f"{page_type}-expertise", 2)
        for guest in as_list(meta.get("guests")):
            add_link(source, f"person:{guest}", "podcast-person", 4)
        for episode in as_list(meta.get("podcast_episodes")):
            add_link(source, f"podcast:{episode}", "person-podcast", 4)
        for target in sorted(set(markdown_targets(str(page["body"])))):
            add_link(source, target, f"{page_type}-link", 1)

    for slug, label in sorted(topic_labels.items()):
        nodes.append(
            {
                "id": f"topic:{slug}",
                "type": "topic",
                "label": label,
                "title": label,
                "url": f"/search.html?q={quote(label)}",
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
    article_counts = Counter(str(node["collection"]) for node in nodes if node["type"] == "article")
    return {
        "generated_at": "generated-by-scripts/build_graph.py",
        "counts": {
            "wikis": counts["wiki"],
            "articles": counts["article"],
            "guides": article_counts["guide"],
            "comparisons": article_counts["comparison"],
            "roadmaps": article_counts["roadmap"],
            "how_tos": article_counts["how_to"],
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
