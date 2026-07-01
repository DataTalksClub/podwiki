#!/usr/bin/env python3
"""Build the packed Zerosearch artifact used by the exploration search Lambda."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SIBLING_ZEROSEARCH = ROOT.parent / "zerosearch"
if SIBLING_ZEROSEARCH.exists():
    sys.path.insert(0, str(SIBLING_ZEROSEARCH))

from zerosearch import Index  # noqa: E402


DEFAULT_CORPUS = ROOT / "artifacts" / "search" / "search-corpus.json"
DEFAULT_BROWSER_CORPUS = ROOT / "search" / "search-corpus.json"
DEFAULT_INDEX = ROOT / "artifacts" / "search" / "search-index.zsx"
COLLECTIONS = {
    "_wiki": ("wiki", "/wiki/"),
    "_guides": ("guide", "/guides/"),
    "_comparisons": ("comparison", "/comparisons/"),
    "_roadmaps": ("roadmap", "/roadmaps/"),
    "_how_tos": ("how_to", "/how-tos/"),
    "_podcast_summaries": ("podcast_summary", "/podcasts/"),
    "_people": ("person", "/people/"),
}


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("/", "")
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


def plain_text(markdown: str) -> str:
    markdown = re.sub(r"```.*?```", " ", markdown, flags=re.S)
    markdown = re.sub(r"`([^`]*)`", r"\1", markdown)
    markdown = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", markdown)
    markdown = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", markdown)
    markdown = re.sub(r"<[^>]+>", " ", markdown)
    markdown = re.sub(r"^#+\s*", "", markdown, flags=re.M)
    markdown = re.sub(r"[*_>#|~-]", " ", markdown)
    return re.sub(r"\s+", " ", markdown).strip()


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def metadata_text(meta: dict[str, object], level: str) -> str:
    fields = ["keyword", "collection", "source_episode"]
    list_fields = [
        "secondary_keywords",
        "topics",
        "guests",
        "related",
        "related_wiki",
        "expertise",
        "podcast_episodes",
    ]
    parts = [level]
    for field in fields:
        value = meta.get(field)
        if isinstance(value, str) and value.strip():
            parts.append(value)
    for field in list_fields:
        parts.extend(as_list(meta.get(field)))
    return " ".join(parts)


def section_docs(body: str, base: dict, url: str) -> list[dict]:
    docs = []
    matches = list(re.finditer(r"^(#{2,3})\s+(.+?)\s*$", body, flags=re.M))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        heading = plain_text(match.group(2))
        text = plain_text(body[start:end])
        if not heading or len(text) < 80:
            continue
        anchor = slugify(heading)
        docs.append(
            {
                **base,
                "id": f"{base['id']}#{anchor}",
                "document_type": "section",
                "page_title": base["title"],
                "title": f"{heading} - {base['title']}",
                "segment_title": heading,
                "url": f"{url}#{anchor}",
                "text": text,
            }
        )
    return docs


def build_docs() -> list[dict]:
    docs: list[dict] = []
    for directory, (level, prefix) in COLLECTIONS.items():
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
            url = f"{prefix}{slug}/"
            related_terms = metadata_text(meta, level)
            base = {
                "id": f"{level}:{slug}",
                "level": level,
                "document_type": "page",
                "page_title": title,
                "episode_slug": slug if level == "podcast_summary" else "",
                "title": title,
                "segment_title": "",
                "url": url,
                "related_terms": related_terms,
            }
            docs.append(
                {
                    **base,
                    "text": plain_text(" ".join([title, summary, related_terms, body])),
                }
            )
            docs.extend(section_docs(body, base, url))
    return docs


def load_docs(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        return payload["docs"]
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--browser-corpus", type=Path, default=DEFAULT_BROWSER_CORPUS)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args()

    docs = build_docs()
    args.corpus.parent.mkdir(parents=True, exist_ok=True)
    args.corpus.write_text(json.dumps({"docs": docs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.browser_corpus.parent.mkdir(parents=True, exist_ok=True)
    args.browser_corpus.write_text(json.dumps({"docs": docs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    index = Index(
        text_fields=["title", "segment_title", "text", "related_terms"],
        keyword_fields=["id", "level", "document_type", "episode_slug", "related_terms"],
    )
    index.fit(docs)
    args.index.parent.mkdir(parents=True, exist_ok=True)
    index.save(args.index)
    print(f"indexed {len(docs)} docs -> {args.index}")
    print(f"wrote corpus -> {args.corpus}")
    print(f"wrote browser corpus -> {args.browser_corpus}")


if __name__ == "__main__":
    main()
