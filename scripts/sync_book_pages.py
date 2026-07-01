#!/usr/bin/env python3
"""Create local book reference pages from the DataTalks.Club Book of the Week source.

These pages are the internal citation targets for wiki and editorial pages,
following the same pattern as podcast summary pages.
"""

from __future__ import annotations

from pathlib import Path

from podcast_source_data import read_people, split_frontmatter

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK_SOURCE = ROOT.parent / "datatalksclub.github.io" / "_books"
DEFAULT_TARGET = ROOT / "_books"
DEFAULT_PEOPLE_DIR = ROOT / "_people"


def read_book(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    meta, _body, _ = split_frontmatter(raw)
    return meta


def load_people_titles(people_dir: Path) -> dict[str, str]:
    titles: dict[str, str] = {}
    for path in people_dir.glob("*.md"):
        if path.name == "README.md":
            continue
        raw = path.read_text(encoding="utf-8")
        meta, _body, _ = split_frontmatter(raw)
        title = str(meta.get("title") or "").strip()
        if title:
            titles[path.stem] = title
    return titles


def slug_from_filename(path: Path) -> str:
    return path.stem


def book_url(slug: str) -> str:
    return f"https://datatalks.club/books/{slug}.html"


def person_label(slug: str, people: dict[str, str]) -> str:
    slug = slug.strip()
    if slug in people:
        return people[slug]
    return slug.replace("-", " ").replace("_", " ").title()


def link_items(meta: dict[str, object]) -> list[dict[str, str]]:
    raw_links = meta.get("links")
    items: list[dict[str, str]] = []
    if isinstance(raw_links, dict):
        text = str(raw_links.get("text", "")).strip()
        link = str(raw_links.get("link", "")).strip()
        if text and link:
            items.append({"text": text, "url": link})
    elif isinstance(raw_links, list):
        for entry in raw_links:
            if isinstance(entry, dict):
                text = str(entry.get("text", "")).strip()
                link = str(entry.get("link", "")).strip()
                if text and link:
                    items.append({"text": text, "url": link})
    return items


def archive_qa_count(meta: dict[str, object]) -> int:
    archive = meta.get("archive")
    if isinstance(archive, list):
        return len(archive)
    return 0


def infer_topics(title: str, description: str) -> list[str]:
    text = f"{title} {description}".lower()
    keywords = [
        "machine learning", "data engineering", "mlops", "python", "sql",
        "deep learning", "nlp", "llm", "ai", "data science", "statistics",
        "data visualization", "streaming", "kafka", "spark", "analytics",
        "software engineering", "cloud", "aws", "gcp", "azure",
        "feature engineering", "data quality", "data governance",
        "reinforcement learning", "computer vision", "time series",
        "graph databases", "search", "rag", "agents", "devops",
        "data pipelines", "orchestration", "airflow", "dbt",
        "experimentation", "a/b testing", "causal inference",
        "privacy", "ethics", "responsible ai",
    ]
    found = []
    for kw in keywords:
        if kw in text and kw not in found:
            found.append(kw)
    return found[:8]


def render_page(
    meta: dict[str, object],
    slug: str,
    source_path: Path,
    people: dict[str, str],
) -> str:
    title = str(meta.get("title") or slug.replace("-", " ").title())
    description = str(meta.get("description") or "")
    authors = meta.get("authors")
    author_slugs: list[str] = []
    if isinstance(authors, list):
        author_slugs = [str(a).strip() for a in authors if str(a).strip()]
    elif isinstance(authors, str):
        author_slugs = [authors.strip()]
    author_names = [person_label(a, people) for a in author_slugs]

    source_url = book_url(slug)
    book_links = link_items(meta)
    qa_count = archive_qa_count(meta)
    topics = infer_topics(title, description)

    lines: list[str] = []
    lines.append("---")
    lines.append('layout: "book_summary"')
    lines.append(f'title: "{title}"')
    lines.append(f'source_book: "../datatalksclub.github.io/_books/{source_path.name}"')
    lines.append(f'source_url: "{source_url}"')
    if author_slugs:
        lines.append(f"authors: {author_slugs}")
        lines.append(f"author_names: {author_names}")
    if book_links:
        lines.append("book_links:")
        for bl in book_links:
            escaped_text = bl["text"].replace('"', "'")
            lines.append(f'  - text: "{escaped_text}"')
            lines.append(f'    url: "{bl["url"]}"')
    if qa_count:
        lines.append(f"qa_count: {qa_count}")
    if topics:
        lines.append(f"topics: {topics}")
    if description:
        escaped = description.replace('"', "'")
        lines.append(f'description: "{escaped}"')
    lines.append("---")
    lines.append("")

    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Original Book of the Week")
    lines.append("")
    lines.append("Use this link for the canonical book page and author Q&A.")
    lines.append("")
    lines.append(f"- [Open the original DataTalks.Club book page]({source_url})")
    if book_links:
        for bl in book_links:
            lines.append(f"- [{bl['text']}]({bl['url']})")
    lines.append("")

    if author_names:
        lines.append("## Author")
        lines.append("")
        author_links = []
        for aslug in author_slugs:
            label = person_label(aslug, people)
            author_links.append(
                f"[{label}]({{ '/people/{aslug}/' | relative_url }})"
            )
        lines.append(", ".join(author_links) + ".")
        lines.append("")

    if qa_count:
        lines.append("## Discussion Archive")
        lines.append("")
        lines.append(
            f"The Book of the Week Q&A has {qa_count} top-level questions with "
            f"author replies. Open the original page to read the full discussion."
        )
        lines.append("")

    return "\n".join(lines) + "\n"


def should_skip(meta: dict[str, object]) -> bool:
    return bool(meta.get("draft"))


def main() -> None:
    import argparse
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_BOOK_SOURCE)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--people-dir", type=Path, default=DEFAULT_PEOPLE_DIR)
    args = parser.parse_args()

    source: Path = args.source
    target: Path = args.target
    people = load_people_titles(args.people_dir)
    target.mkdir(parents=True, exist_ok=True)

    book_files = sorted(source.glob("*.md"))
    created = 0
    updated = 0
    skipped = 0
    unchanged = 0

    for path in book_files:
        meta = read_book(path)
        if should_skip(meta):
            skipped += 1
            continue

        slug = slug_from_filename(path)
        out_path = target / f"{slug}.md"
        content = render_page(meta, slug, path, people)

        if out_path.exists():
            existing = out_path.read_text(encoding="utf-8")
            if "curated: true" in existing:
                skipped += 1
                continue
            if existing == content:
                unchanged += 1
                continue
            updated += 1
        else:
            created += 1

        out_path.write_text(content, encoding="utf-8")

    total = len(list(target.glob("*.md")))
    print(
        f"books: {created} created, {updated} updated, {unchanged} unchanged, "
        f"{skipped} skipped -> {total} pages in {target}"
    )


if __name__ == "__main__":
    main()
