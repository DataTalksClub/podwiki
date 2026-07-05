#!/usr/bin/env python3
"""Report public content pages that still need citation/link cleanup."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FOLDERS = ("_wiki",)
GENERIC_PODCAST_URL = "https://datatalks.club/podcast.html"
PUBLIC_COLLECTIONS = ("podcasts", "wiki", "people", "books")
PUBLIC_CONTENT_FOLDERS = {"_wiki"}
CANONICAL_PODCAST_RE = re.compile(r"https://datatalks\.club/podcast/[^)\s\"']+\.html")
CANONICAL_PEOPLE_RE = re.compile(r"https://datatalks\.club/people/[^)\s\"']+\.html")
PODCAST_CHIP_RE = re.compile(r"\[\[(?:podcast|cite):", re.IGNORECASE)
PODCAST_MARKER_RE = re.compile(r"\[\[podcast:[^\]]+\]\]", re.IGNORECASE)
OLD_TIMESTAMPED_PODCAST_RE = re.compile(r"\[\[podcast:[^\]]*@[0-9]", re.IGNORECASE)
VISIBLE_TIMESTAMP_PROSE_RE = re.compile(
    r"\b(?:At|Around|at|around|~)\s*\d{1,2}:\d{2}\b|\(\d{1,2}:\d{2}\)"
)
PODCAST_LABEL_TIMESTAMP_RE = re.compile(
    r"(?:\||=>)[^\]]*(?:\b(?:at|around)\s+\d{1,2}:\d{2}\b|\b\d{1,2}:\d{2}\b)",
    re.IGNORECASE,
)
HOUR_FORMAT_CITATION_RE = re.compile(
    r"\[\[(?:cite|podcast):[^\]\n]*@\d{1,2}:\d{2}:\d{2}(?=\s*=>)",
    re.IGNORECASE,
)
SHORT_MINUTE_CITATION_RE = re.compile(
    r"\[\[(?:cite|podcast):[^\]\n]*@[0-9]:[0-9]{2}(?=\s*=>)",
    re.IGNORECASE,
)
RELATED_BOILERPLATE_RE = re.compile(
    r"(?im)^\s*(?:"
    r"For related (?:background|mechanics|production work|transition context),\s*(?:see|use)|"
    r"Continue through these pages(?: for narrower [^.]+)?|"
    r"Continue with (?:adjacent|these|surrounding)|"
    r"Use these pages|"
    r"These pages cover|"
    r"Related pages include|"
    r"See also:|"
    r"See also\b"
    r")"
)
LOCAL_ENTITY_PATH_RE = re.compile(
    r"\]\(/(?:podcasts|people|books)/[a-z0-9][a-z0-9-]*/?(?:#[^)]*)?\)"
    r"|href=[\"']/(?:podcasts|people|books)/[a-z0-9][a-z0-9-]*/?(?:#[^\"']*)?[\"']"
    r"|\{\{?\s*[\"']/(?:podcasts|people|books)/[a-z0-9][a-z0-9-]*/?(?:#[^\"']*)?[\"']\s*\|\s*relative_url\s*\}\}?",
    re.IGNORECASE,
)
WIKI_CHIP_RE = re.compile(r"\[\[([^\]]+)\]\]")
FORBIDDEN_HEADING_RE = re.compile(
    r"^## (Contents|Link Map|Search Intent|Archive Evidence|Episode Evidence|Guest Descriptions|"
    r"Recurring Archive Themes|Maintenance Notes|Agent Maintenance Notes|Guest Experts|Bottom Line)\b",
    re.MULTILINE,
)
SCAFFOLD_HEADING_RE = re.compile(
    r"^## (Common Definition|Guest Tradeoffs|Guest Differences|Guest Disagreements|Guest Emphasis)\b",
    re.MULTILINE,
)
ARCHIVE_HEADING_RE = re.compile(r"^## .*?\bArchive\b.*$", re.MULTILINE)
ARCHIVE_SCAFFOLDING_RE = re.compile(
    r"\b(?:the archive|The archive|DataTalks\.Club archive|archive-backed|archive's|archive’s)\b"
)
SOURCE_SCAFFOLDING_RE = re.compile(
    r"\b(?:DataTalks\.Club (?:podcast guests|guests|discussions)|"
    r"podcast guests|Podcast guests|guests treat|Guests treat|episodes show|"
    r"discussions converge)\b"
)
INDIRECT_ATTRIBUTION_RE = re.compile(
    r"\b(?:she says|he says|she explains|he explains|guest argues|guest explains|"
    r"in her episode|in his episode|podcast guests|guests treat)\b",
    re.IGNORECASE,
)
STRICT_SOURCE_SCAFFOLDING_RE = re.compile(
    r"\b(?:DataTalks\.Club episodes|DataTalks\.Club podcast discussions|"
    r"Podcast discussions|podcast discussions|episodes cover|Episodes cover|"
    r"The episodes treat|episodes treat|episodes frame|Episodes frame|"
    r"shared definition across the podcast discussions|the relevant podcast discussions)\b"
)
STRICT_ARCHIVE_SCAFFOLDING_RE = re.compile(
    r"\b(?:podcast archive|podcast-backed|podcast-grounded|"
    r"archive-grounded|archive-derived)\b",
    re.IGNORECASE,
)
STRICT_TOPIC_HEADING_RE = re.compile(
    r"^## (Workflow Definition|Tradeoffs in the Episodes|Operating Tradeoffs|"
    r"Agent Ops Versus LLMOps|Project Signals|Review Checklist|Ready to Review|"
    r"Interview Readiness|Learning Paths and Next Steps)\b",
    re.MULTILINE,
)
STRICT_PAGE_META_RE = re.compile(
    r"(?m)^\s*(?:Use this (?:page|checklist|guide)|"
    r"Use these pages|"
    r"For [^.\n]{1,100}, use this page|"
    r"Continue through these pages)",
    re.IGNORECASE,
)
GENERIC_CITATION_LABEL_RE = re.compile(
    r"\[\[cite:[^\]]*=>"
    r"(?:role episode|foundations episode|marketing transition episode|modern stack episode|"
    r"episode|podcast episode|interview|conversation|[^]]+\s+episode)\]\]",
    re.IGNORECASE,
)
MISSING_CITATION_LABEL_RE = re.compile(r"\[\[cite:[^\]=>]+\]\]", re.IGNORECASE)
SECTION_HEADING_RE = re.compile(r"^## .+$", re.MULTILINE)
SECTION_CITATION_RE = re.compile(r"\[\[cite:|https://datatalks\.club/podcast/", re.IGNORECASE)
SECTION_CITATION_EXEMPT_HEADINGS = {"## Related Pages", "## Related Topics"}
LOCAL_LINK_RE = re.compile(r"'/([^']+)/' \| relative_url")
RAW_RELATIVE_URL_RE = re.compile(r"relative_url")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((/[^)#?]+)")


def visible_body(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    _, separator, body = text.partition("\n---\n")
    if not separator:
        return text
    return body


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    raw, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        return {}
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def page_paths(folders: list[str]) -> list[Path]:
    paths: list[Path] = []
    for folder in folders:
        for path in (ROOT / folder).glob("*.md"):
            if path.name == "README.md":
                continue
            meta = frontmatter(path.read_text(encoding="utf-8"))
            if meta.get("redirect_to") or meta.get("published", "").lower() == "false":
                continue
            paths.append(path)
    return sorted(paths)


def selected_page_paths(paths: list[str]) -> list[Path]:
    selected: list[Path] = []
    for value in paths:
        path = (ROOT / value).resolve()
        if not path.is_file():
            continue
        if path.suffix != ".md" or path.name == "README.md":
            continue
        if path.parent.name not in PUBLIC_CONTENT_FOLDERS:
            continue
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("redirect_to") or meta.get("published", "").lower() == "false":
            continue
        selected.append(path)
    return sorted(set(selected))


def link_counts(text: str) -> dict[str, int]:
    counts = {collection: 0 for collection in PUBLIC_COLLECTIONS}
    targets = [match.group(1) for match in LOCAL_LINK_RE.finditer(text)]
    targets.extend(match.group(1).lstrip("/") for match in MARKDOWN_LINK_RE.finditer(text))
    for target in targets:
        for collection in counts:
            if target.startswith(f"{collection}/"):
                counts[collection] += 1
    counts["podcasts"] += len(CANONICAL_PODCAST_RE.findall(text))
    counts["podcasts"] += len(PODCAST_CHIP_RE.findall(text))
    counts["people"] += len(CANONICAL_PEOPLE_RE.findall(text))
    for inner in WIKI_CHIP_RE.findall(text):
        if ":" in inner:
            prefix = inner.split(":", 1)[0].strip().lower()
            if prefix not in {"wiki", "topic"}:
                continue
        counts["wiki"] += 1
    return counts


def uncited_substantive_sections(body: str) -> int:
    lines = body.splitlines()
    headings = [
        (index, line.strip())
        for index, line in enumerate(lines)
        if line.startswith("## ")
    ]
    total = 0
    for pos, (start, heading) in enumerate(headings):
        if heading in SECTION_CITATION_EXEMPT_HEADINGS:
            continue
        end = headings[pos + 1][0] if pos + 1 < len(headings) else len(lines)
        section = lines[start + 1 : end]
        substantive = sum(
            1
            for line in section
            if line.strip()
            and not line.strip().startswith(("-", "*"))
            and not line.strip().startswith("[[cite:")
        )
        if substantive >= 3 and not SECTION_CITATION_RE.search("\n".join(section)):
            total += 1
    return total


def audit_file(
    path: Path,
    strict_scaffold_headings: bool = False,
    strict_source_scaffolding: bool = False,
) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    body = visible_body(text)
    links = link_counts(text)
    is_public_content = path.parent.name in PUBLIC_CONTENT_FOLDERS
    forbidden = FORBIDDEN_HEADING_RE.findall(text)
    if strict_scaffold_headings:
        forbidden.extend(SCAFFOLD_HEADING_RE.findall(text))
        forbidden.extend(STRICT_TOPIC_HEADING_RE.findall(text))
    archive_headings = ARCHIVE_HEADING_RE.findall(text)
    source_text = body
    if strict_source_scaffolding:
        source_text = f"{body}\n{meta.get('summary', '')}"
    archive_scaffolding = ARCHIVE_SCAFFOLDING_RE.findall(source_text)
    source_scaffolding = SOURCE_SCAFFOLDING_RE.findall(source_text)
    indirect_attribution = INDIRECT_ATTRIBUTION_RE.findall(source_text)
    if strict_source_scaffolding:
        archive_scaffolding.extend(STRICT_ARCHIVE_SCAFFOLDING_RE.findall(source_text))
        source_scaffolding.extend(STRICT_SOURCE_SCAFFOLDING_RE.findall(source_text))
        source_scaffolding.extend(STRICT_PAGE_META_RE.findall(source_text))
    generic_citation_labels = GENERIC_CITATION_LABEL_RE.findall(body)
    missing_citation_labels = MISSING_CITATION_LABEL_RE.findall(body)
    uncited_sections = uncited_substantive_sections(body)
    generic = body.count(GENERIC_PODCAST_URL)
    old_timestamped_podcast = len(OLD_TIMESTAMPED_PODCAST_RE.findall(body))
    visible_timestamp_prose = len(VISIBLE_TIMESTAMP_PROSE_RE.findall(body))
    hour_format_citations = len(HOUR_FORMAT_CITATION_RE.findall(body))
    short_minute_citations = len(SHORT_MINUTE_CITATION_RE.findall(body))
    related_boilerplate = len(RELATED_BOILERPLATE_RE.findall(body))
    local_entity_paths = len(LOCAL_ENTITY_PATH_RE.findall(body))
    podcast_label_timestamps = sum(
        1 for marker in PODCAST_MARKER_RE.findall(body) if PODCAST_LABEL_TIMESTAMP_RE.search(marker)
    )
    raw_relative_url = len(RAW_RELATIVE_URL_RE.findall(body))
    tagged_shape_errors = 0
    tagged_keyword_errors = 0
    if is_public_content and meta.get("tags"):
        if meta.get("layout") != "article":
            tagged_shape_errors += 1
        if "related_wiki" not in meta:
            tagged_shape_errors += 1
        if "related" in meta:
            tagged_shape_errors += 1
        if not meta.get("keyword"):
            tagged_keyword_errors += 1
    score = (
        generic * 3
        + (len(forbidden) + len(archive_headings)) * 10
        + len(archive_scaffolding)
        + old_timestamped_podcast * 8
        + hour_format_citations * 4
        + short_minute_citations * 4
        + related_boilerplate * 2
        + local_entity_paths * 6
        + visible_timestamp_prose * 5
        + podcast_label_timestamps * 3
        + raw_relative_url * 4
        + tagged_shape_errors * 8
        + tagged_keyword_errors * 8
    )
    score += len(source_scaffolding) * 2
    score += len(indirect_attribution) * 2
    score += len(generic_citation_labels) * 3
    score += len(missing_citation_labels) * 3
    score += uncited_sections * 4
    if is_public_content and links["podcasts"] == 0:
        score += 5
    return {
        "path": path.relative_to(ROOT),
        "generic_podcast_links": generic,
        "forbidden_headings": len(forbidden) + len(archive_headings),
        "archive_scaffolding": len(archive_scaffolding),
        "source_scaffolding": len(source_scaffolding),
        "indirect_attribution": len(indirect_attribution),
        "generic_citation_labels": len(generic_citation_labels),
        "missing_citation_labels": len(missing_citation_labels),
        "uncited_sections": uncited_sections,
        "old_timestamped_podcast": old_timestamped_podcast,
        "hour_format_citations": hour_format_citations,
        "short_minute_citations": short_minute_citations,
        "related_boilerplate": related_boilerplate,
        "local_entity_paths": local_entity_paths,
        "visible_timestamp_prose": visible_timestamp_prose,
        "podcast_label_timestamps": podcast_label_timestamps,
        "raw_relative_url": raw_relative_url,
        "tagged_shape_errors": tagged_shape_errors,
        "tagged_keyword_errors": tagged_keyword_errors,
        "podcast_links": links["podcasts"],
        "wiki_links": links["wiki"],
        "people_links": links["people"],
        "book_links": links["books"],
        "score": score,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="*", default=list(DEFAULT_FOLDERS))
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--paths", nargs="*", help="Audit these specific public Markdown files instead of folders.")
    parser.add_argument(
        "--strict-scaffold-headings",
        action="store_true",
        help="Also flag older scaffold headings such as Common Definition and Guest Differences.",
    )
    parser.add_argument(
        "--strict-source-scaffolding",
        action="store_true",
        help="Also flag broad source-intro phrases such as podcast discussions and DataTalks.Club episodes.",
    )
    args = parser.parse_args()

    paths = selected_page_paths(args.paths) if args.paths else page_paths(args.folders)
    rows = [
        audit_file(path, args.strict_scaffold_headings, args.strict_source_scaffolding)
        for path in paths
    ]
    problem_rows = [
        row
        for row in rows
        if (
            row["generic_podcast_links"]
            or row["forbidden_headings"]
            or row["archive_scaffolding"]
            or row["source_scaffolding"]
            or row["indirect_attribution"]
            or row["generic_citation_labels"]
            or row["missing_citation_labels"]
            or row["uncited_sections"]
            or row["old_timestamped_podcast"]
            or row["hour_format_citations"]
            or row["short_minute_citations"]
            or row["related_boilerplate"]
            or row["local_entity_paths"]
            or row["visible_timestamp_prose"]
            or row["podcast_label_timestamps"]
            or row["raw_relative_url"]
            or row["tagged_shape_errors"]
            or row["tagged_keyword_errors"]
            or row["podcast_links"] == 0
        )
    ]

    print(f"pages: {len(rows)}")
    print(f"problem_pages: {len(problem_rows)}")
    print(f"generic_podcast_links: {sum(int(row['generic_podcast_links']) for row in rows)}")
    print(f"forbidden_headings: {sum(int(row['forbidden_headings']) for row in rows)}")
    print(f"archive_scaffolding: {sum(int(row['archive_scaffolding']) for row in rows)}")
    print(f"source_scaffolding: {sum(int(row['source_scaffolding']) for row in rows)}")
    print(f"indirect_attribution: {sum(int(row['indirect_attribution']) for row in rows)}")
    print(f"generic_citation_labels: {sum(int(row['generic_citation_labels']) for row in rows)}")
    print(f"missing_citation_labels: {sum(int(row['missing_citation_labels']) for row in rows)}")
    print(f"uncited_sections: {sum(int(row['uncited_sections']) for row in rows)}")
    print(f"old_timestamped_podcast: {sum(int(row['old_timestamped_podcast']) for row in rows)}")
    print(f"hour_format_citations: {sum(int(row['hour_format_citations']) for row in rows)}")
    print(f"short_minute_citations: {sum(int(row['short_minute_citations']) for row in rows)}")
    print(f"related_boilerplate: {sum(int(row['related_boilerplate']) for row in rows)}")
    print(f"local_entity_paths: {sum(int(row['local_entity_paths']) for row in rows)}")
    print(f"visible_timestamp_prose: {sum(int(row['visible_timestamp_prose']) for row in rows)}")
    print(f"podcast_label_timestamps: {sum(int(row['podcast_label_timestamps']) for row in rows)}")
    print(f"raw_relative_url: {sum(int(row['raw_relative_url']) for row in rows)}")
    print(f"tagged_shape_errors: {sum(int(row['tagged_shape_errors']) for row in rows)}")
    print(f"tagged_keyword_errors: {sum(int(row['tagged_keyword_errors']) for row in rows)}")
    print(f"pages_without_podcast_links: {sum(1 for row in rows if int(row['podcast_links']) == 0)}")
    print("")

    for row in sorted(problem_rows, key=lambda item: (-int(item["score"]), str(item["path"])))[: args.limit]:
        print(
            f"{row['path']}: score={row['score']} "
            f"generic={row['generic_podcast_links']} bad_headings={row['forbidden_headings']} "
            f"archive_scaffolding={row['archive_scaffolding']} "
            f"source_scaffolding={row['source_scaffolding']} "
            f"indirect_attribution={row['indirect_attribution']} "
            f"generic_citation_labels={row['generic_citation_labels']} "
            f"missing_citation_labels={row['missing_citation_labels']} "
            f"uncited_sections={row['uncited_sections']} "
            f"old_podcast_ts={row['old_timestamped_podcast']} "
            f"hour_format_citations={row['hour_format_citations']} "
            f"short_minute_citations={row['short_minute_citations']} "
            f"related_boilerplate={row['related_boilerplate']} "
            f"local_entity_paths={row['local_entity_paths']} "
            f"visible_ts={row['visible_timestamp_prose']} "
            f"podcast_label_ts={row['podcast_label_timestamps']} "
            f"raw_relative_url={row['raw_relative_url']} "
            f"tagged_shape={row['tagged_shape_errors']} "
            f"tagged_keyword={row['tagged_keyword_errors']} "
            f"podcast_links={row['podcast_links']} wiki_links={row['wiki_links']} "
            f"people_links={row['people_links']} book_links={row['book_links']}"
        )
    return 1 if problem_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
