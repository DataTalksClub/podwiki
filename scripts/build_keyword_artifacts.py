#!/usr/bin/env python3
"""Build machine-readable keyword coverage artifacts from current wiki pages."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import keyword_gap  # noqa: E402
from build_search_index import as_list, split_frontmatter  # noqa: E402


DEFAULT_CSV = ROOT / ".tmp" / "ubersuggest_Current_Queries.csv"
DEFAULT_XLSX = ROOT / ".tmp" / "next-actions-done-datatalks.club.xlsx"
DEFAULT_OUT = ROOT / "artifacts" / "keywords"


HEAD_TOKENS = [
    "data engineering",
    "data engineer",
    "machine learning",
    "data science",
    "data scientist",
    "software engineering",
    "software engineer",
    "analytics engineering",
    "business intelligence",
    "product manager",
    "product owner",
    "apache airflow",
    "airflow",
    "mlops",
    "dataops",
    "llm",
    "rag",
    "open source",
    "portfolio",
    "interview",
    "roadmap",
    "startup",
    "freelance",
]


def int_value(value: object) -> int:
    try:
        return int(str(value or "0").strip())
    except ValueError:
        return 0


def keyword_slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def file_from_doc_id(doc_id: str) -> str:
    if ":" not in doc_id:
        return ""
    folder, slug = doc_id.split(":", 1)
    return f"{folder}/{slug}.md"


def load_wiki_meta() -> dict[str, dict[str, object]]:
    pages: dict[str, dict[str, object]] = {}
    for path in sorted((ROOT / "_wiki").glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, _ = split_frontmatter(raw)
        tag = ""
        for value in as_list(meta.get("tags")):
            normalized = value.strip().lower()
            if normalized in {"guide", "comparison", "roadmap", "transition", "how-to"}:
                tag = normalized
                break
        pages[f"_wiki:{path.stem}"] = {
            "file": f"_wiki/{path.name}",
            "title": str(meta.get("title") or path.stem.replace("-", " ")),
            "tag": tag,
        }
    return pages


def classify_rows(csv_path: Path, covered: float, ground: float) -> list[dict[str, object]]:
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig")))
    wiki_docs = keyword_gap.load_collection(ROOT, ["_wiki"])
    wiki_idx = keyword_gap.build(wiki_docs)
    main_docs = keyword_gap.load_collection(
        keyword_gap.MAIN_SITE,
        ["_posts", "_courses", "_books", "_tools", "_people", "_podcast"],
    )
    main_idx = keyword_gap.build(main_docs)
    book_docs = keyword_gap.load_collection(ROOT, ["_books"])
    books_idx = keyword_gap.build(book_docs)
    ground_docs = book_docs + keyword_gap.load_collection(ROOT, ["_podcast_summaries"])
    ground_docs += keyword_gap.load_collection(keyword_gap.MAIN_SITE, ["_podcast"])
    ground_idx = keyword_gap.build(ground_docs)
    wiki_meta = load_wiki_meta()

    records: list[dict[str, object]] = []
    for row in rows:
        kw = str(row.get("Keyword") or "").strip()
        if not kw:
            continue
        no = int_value(row.get("No"))
        rec: dict[str, object] = {
            "no": no,
            "keyword": kw,
            "keyword_slug": keyword_slug(kw),
            "search_volume": int_value(row.get("Search Volume")),
            "cpc": str(row.get("CPC") or "").strip(),
            "paid_difficulty": int_value(row.get("Paid Difficulty")),
            "seo_difficulty": int_value(row.get("SEO Difficulty")),
        }

        if keyword_gap.NOISE_RE.search(kw):
            b_score, b_id = keyword_gap.top_score(books_idx, kw)
            if b_score >= covered:
                status = "BOOK_INTENT"
                rec.update(book_score=round(b_score, 1), book_file=file_from_doc_id(b_id))
            else:
                status = "NOISE"
            rec["status"] = status
            records.append(rec)
            continue

        if keyword_gap.BRAND_RE.search(kw):
            rec["status"] = "BRAND"
            records.append(rec)
            continue

        alias_status, alias_id = keyword_gap.alias_route(kw)
        if alias_status:
            rec["status"] = alias_status
            rec.update(
                wiki_score=0.0,
                main_score=0.0,
                ground_score=0.0,
                ground_file="",
            )
            if alias_status == "COVERED":
                page = wiki_meta.get(alias_id, {})
                rec.update(
                    covered_by_wiki=True,
                    wiki_file=page.get("file") or file_from_doc_id(alias_id),
                    wiki_title=page.get("title") or "",
                    wiki_tag=page.get("tag") or "",
                    covered_by_editorial=bool(page.get("tag")),
                    editorial_file=page.get("file") if page.get("tag") else "",
                )
            elif alias_status == "MAIN":
                rec.update(
                    covered_by_wiki=False,
                    wiki_file="",
                    wiki_title="",
                    wiki_tag="",
                    covered_by_editorial=False,
                    editorial_file="",
                    main_file=file_from_doc_id(alias_id),
                )
            records.append(rec)
            continue

        w_score, w_id = keyword_gap.top_score(wiki_idx, kw)
        m_score, m_id = keyword_gap.top_score(main_idx, kw)
        g_score, g_id = keyword_gap.top_score(ground_idx, kw)
        w_owned = keyword_gap.owned_by_phrase(
            wiki_docs, kw, ["title_terms", "keyword_terms"], allow_phrase=False
        )
        m_owned = keyword_gap.owned_by_phrase(
            main_docs,
            kw,
            ["title_terms", "keyword_terms", "summary_terms"],
            allow_phrase=True,
        )

        rec.update(
            wiki_score=round(w_score, 1),
            main_score=round(m_score, 1),
            ground_score=round(g_score, 1),
            ground_file=file_from_doc_id(g_id),
        )
        if w_owned:
            w_id = w_owned
            status = "COVERED"
        elif m_owned:
            m_id = m_owned
            status = "MAIN"
        elif m_score >= covered and m_score >= w_score:
            status = "MAIN"
        elif w_score >= covered:
            status = "COVERED"
        elif g_score >= ground:
            status = "GAP_GROUNDED"
        else:
            status = "GAP_UNGROUNDED"

        rec["status"] = status
        if status == "COVERED":
            page = wiki_meta.get(w_id, {})
            rec.update(
                covered_by_wiki=True,
                wiki_file=page.get("file") or file_from_doc_id(w_id),
                wiki_title=page.get("title") or "",
                wiki_tag=page.get("tag") or "",
                covered_by_editorial=bool(page.get("tag")),
                editorial_file=page.get("file") if page.get("tag") else "",
            )
        else:
            rec.update(
                covered_by_wiki=False,
                wiki_file="",
                wiki_title="",
                wiki_tag="",
                covered_by_editorial=False,
                editorial_file="",
            )
        if status == "MAIN":
            rec["main_file"] = file_from_doc_id(m_id)
        records.append(rec)
    return records


def family_name(keyword: str, record: dict[str, object]) -> str:
    if record.get("wiki_title"):
        return str(record["wiki_title"]).lower()
    if record.get("status") == "MAIN" and record.get("main_file"):
        return str(record["main_file"]).rsplit("/", 1)[-1].removesuffix(".md").replace("-", " ")
    normalized = " ".join(re.findall(r"[a-z0-9]+", keyword.lower()))
    for token in HEAD_TOKENS:
        if token in normalized:
            return token
    terms = [t for t in keyword_gap.toks(keyword) if t not in {"club", "free", "course"}]
    return " ".join(terms[:3]) or normalized


def build_families(records: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for rec in records:
        groups[family_name(str(rec["keyword"]), rec)].append(rec)
    families = []
    for name, items in groups.items():
        statuses = {str(item.get("status")) for item in items}
        families.append(
            {
                "family": name,
                "total_volume": sum(int(item.get("search_volume") or 0) for item in items),
                "min_seo_difficulty": min(int(item.get("seo_difficulty") or 0) for item in items),
                "statuses": sorted(statuses),
                "covered_by_wiki": any(bool(item.get("covered_by_wiki")) for item in items),
                "covered_by_editorial": any(
                    bool(item.get("covered_by_editorial")) for item in items
                ),
                "keywords": sorted(
                    items,
                    key=lambda item: (
                        -int(item.get("search_volume") or 0),
                        int(item.get("seo_difficulty") or 0),
                        str(item.get("keyword")),
                    ),
                ),
            }
        )
    return sorted(families, key=lambda item: (-int(item["total_volume"]), item["family"]))


def shared_strings(zip_file: zipfile.ZipFile) -> list[str]:
    path = "xl/sharedStrings.xml"
    if path not in zip_file.namelist():
        return []
    root = ET.fromstring(zip_file.read(path))
    ns = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    values = []
    for item in root.findall("x:si", ns):
        parts = [node.text or "" for node in item.findall(".//x:t", ns)]
        values.append("".join(parts))
    return values


def workbook_sheets(zip_file: zipfile.ZipFile) -> list[tuple[str, str]]:
    ns = {
        "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }
    workbook = ET.fromstring(zip_file.read("xl/workbook.xml"))
    rels = ET.fromstring(zip_file.read("xl/_rels/workbook.xml.rels"))
    rel_map = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels
        if rel.attrib.get("Id") and rel.attrib.get("Target")
    }
    sheets = []
    for sheet in workbook.findall("x:sheets/x:sheet", ns):
        name = sheet.attrib["name"]
        rel_id = sheet.attrib[f"{{{ns['r']}}}id"]
        target = rel_map[rel_id]
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        sheets.append((name, target))
    return sheets


def column_index(cell_ref: str) -> int:
    letters = re.match(r"[A-Z]+", cell_ref)
    if not letters:
        return 0
    idx = 0
    for char in letters.group(0):
        idx = idx * 26 + (ord(char) - ord("A") + 1)
    return idx - 1


def cell_value(cell: ET.Element, strings: list[str], ns: dict[str, str]) -> str:
    value = cell.find("x:v", ns)
    if value is None or value.text is None:
        inline = cell.find(".//x:t", ns)
        return inline.text if inline is not None and inline.text else ""
    if cell.attrib.get("t") == "s":
        idx = int_value(value.text)
        return strings[idx] if 0 <= idx < len(strings) else ""
    return value.text


def read_xlsx(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    ns = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    result = []
    with zipfile.ZipFile(path) as zf:
        strings = shared_strings(zf)
        for sheet_name, sheet_path in workbook_sheets(zf):
            root = ET.fromstring(zf.read(sheet_path))
            rows = []
            for row in root.findall(".//x:sheetData/x:row", ns):
                values: list[str] = []
                for cell in row.findall("x:c", ns):
                    idx = column_index(cell.attrib.get("r", "A1"))
                    while len(values) <= idx:
                        values.append("")
                    values[idx] = cell_value(cell, strings, ns)
                rows.append(values)
            headers = [value.strip() for value in rows[0]] if rows else []
            data_rows = []
            for values in rows[1:]:
                record = {
                    headers[i]: values[i].strip()
                    for i in range(min(len(headers), len(values)))
                    if headers[i] and values[i].strip()
                }
                if record:
                    data_rows.append(record)
            result.append({"sheet": sheet_name, "headers": headers, "rows": data_rows})
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--xlsx", type=Path, default=DEFAULT_XLSX)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--covered", type=float, default=12.0)
    parser.add_argument("--ground", type=float, default=10.0)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    keyword_records = classify_rows(args.csv, args.covered, args.ground)
    families = build_families(keyword_records)
    suggestions = read_xlsx(args.xlsx)

    (args.out_dir / "ubersuggest-keywords.json").write_text(
        json.dumps(keyword_records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "ubersuggest-families.json").write_text(
        json.dumps(families, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "content-suggestions.json").write_text(
        json.dumps(suggestions, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    counts = defaultdict(int)
    for record in keyword_records:
        counts[str(record.get("status"))] += 1
    print(f"keywords: {len(keyword_records)}")
    for key in sorted(counts):
        print(f"{key}: {counts[key]}")
    print(f"families: {len(families)}")
    print(f"suggestion sheets: {len(suggestions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
