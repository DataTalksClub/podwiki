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
SIBLING_STEMLITE = ROOT.parent / "stemlite"
if SIBLING_STEMLITE.exists():
    sys.path.insert(0, str(SIBLING_STEMLITE))

from zerosearch import Index  # noqa: E402


DEFAULT_CORPUS = ROOT / "artifacts" / "search" / "search-corpus.json"
DEFAULT_BROWSER_CORPUS = ROOT / "search" / "search-corpus.json"
DEFAULT_INDEX = ROOT / "artifacts" / "search" / "search-index.zsx"
TAGGED_WIKI_LEVELS = {
    "comparison": "comparison",
    "guide": "guide",
    "roadmap": "roadmap",
    "transition": "transition",
    "how-to": "how_to",
    "how_to": "how_to",
}
COLLECTIONS = {
    "_wiki": ("wiki", "/wiki/"),
    "_guides": ("guide", "/guides/"),
    "_comparisons": ("comparison", "/comparisons/"),
    "_roadmaps": ("roadmap", "/roadmaps/"),
    "_how_tos": ("how_to", "/how-tos/"),
    "_podcast_summaries": ("podcast_summary", "/podcasts/"),
    "_books": ("book", "/books/"),
    "_people": ("person", "/people/"),
}

BOILERPLATE_SECTION_HEADINGS = {
    "related pages",
    "related topics",
    "related pages and next steps",
    "chapter headers",
    "source",
    "source file",
    "source files",
    "source pointers",
    "key concepts",
    "useful for",
    "probably skip if",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("/", "")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def humanize_chip_target(value: str) -> str:
    value = value.split(":", 1)[-1]
    value = value.rsplit("@", 1)[0]
    return re.sub(r"[-_]+", " ", value).strip()


def chip_label(inner: str) -> str:
    inner = inner.replace("=&gt;", "=>")
    if "=>" in inner and "|" not in inner:
        return inner.split("=>", 1)[1].strip()
    parts = [part.strip() for part in inner.split("|") if part.strip()]
    if len(parts) > 1:
        non_time = [part for part in parts[1:] if not re.fullmatch(r"\d{1,2}:\d{2}(?::\d{2})?", part)]
        if non_time:
            return non_time[-1]
    return humanize_chip_target(parts[0] if parts else inner)


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
    markdown = re.sub(r"\[\[([^\]]+)\]\]", lambda m: chip_label(m.group(1)), markdown)
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


def tagged_wiki_level(meta: dict[str, object]) -> str | None:
    for tag in as_list(meta.get("tags")):
        normalized = tag.strip().lower()
        if normalized in TAGGED_WIKI_LEVELS:
            return TAGGED_WIKI_LEVELS[normalized]
    return None


def canonical_url(level: str, slug: str, source_url: str = "") -> str:
    source_url = source_url.strip()
    if source_url:
        return source_url
    if level == "podcast_summary":
        return f"https://datatalks.club/podcast/{slug}.html"
    if level == "person":
        return f"https://datatalks.club/people/{slug}.html"
    if level == "book":
        return f"https://datatalks.club/books/{slug}.html"
    return ""


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


def section_docs(body: str, base: dict, url: str, external: bool = False) -> list[dict]:
    docs = []
    matches = list(re.finditer(r"^(#{2,3})\s+(.+?)\s*$", body, flags=re.M))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        heading = plain_text(match.group(2))
        if heading.strip().lower() in BOILERPLATE_SECTION_HEADINGS:
            continue
        text = plain_text(body[start:end])
        if not heading or len(text) < 80:
            continue
        anchor = slugify(heading)
        # External (main-site) pages do not share our local heading anchors, so
        # link the section back to the canonical page without a fragment.
        section_url = url if external else f"{url}#{anchor}"
        docs.append(
            {
                **base,
                "id": f"{base['id']}#{anchor}",
                "document_type": "section",
                "page_title": base["title"],
                "title": f"{heading} - {base['title']}",
                "segment_title": heading,
                "url": section_url,
                "text": text,
            }
        )
    return docs


def build_docs() -> list[dict]:
    docs: list[dict] = []
    for directory, (base_level, prefix) in COLLECTIONS.items():
        collection_dir = ROOT / directory
        if not collection_dir.exists():
            continue
        for path in sorted(collection_dir.glob("*.md")):
            if path.name == "README.md" or path.stem == "_template":
                continue
            raw = path.read_text(encoding="utf-8")
            meta, body = split_frontmatter(raw)
            if meta.get("redirect_to") or str(meta.get("published", "")).lower() == "false":
                continue
            slug = source_slug(path)
            level = tagged_wiki_level(meta) if directory == "_wiki" else None
            if not level:
                level = base_level
            title = str(meta.get("title") or slug.replace("-", " ").title())
            summary = str(meta.get("summary") or "")
            # podcast/book/person pages are not published locally; point search
            # results at the canonical main-site URL from front matter.
            canonical = str(meta.get("source_url") or "").strip()
            external = level in {"podcast_summary", "book", "person"}
            url = canonical_url(level, slug, canonical) if external else f"{prefix}{slug}/"
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
            docs.extend(section_docs(body, base, url, external=external))
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
    parser.add_argument(
        "--stemmer", default=None,
        help="stemmer name (porter/snowball/lancaster) via the stemlite library. "
             "OFF by default: only enable once stemlite and the stemming-enabled "
             "zerosearch are available to the Lambda (see docs/search-stemming.md).",
    )
    args = parser.parse_args()

    docs = build_docs()
    args.corpus.parent.mkdir(parents=True, exist_ok=True)
    args.corpus.write_text(json.dumps({"docs": docs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.browser_corpus.parent.mkdir(parents=True, exist_ok=True)
    args.browser_corpus.write_text(json.dumps({"docs": docs}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    index = Index(
        text_fields=["title", "segment_title", "text", "related_terms"],
        keyword_fields=["id", "level", "document_type", "episode_slug", "related_terms"],
        stemmer=args.stemmer,
    )
    index.fit(docs)
    args.index.parent.mkdir(parents=True, exist_ok=True)
    index.save(args.index)
    print(f"indexed {len(docs)} docs -> {args.index}")
    print(f"wrote corpus -> {args.corpus}")
    print(f"wrote browser corpus -> {args.browser_corpus}")


if __name__ == "__main__":
    main()
