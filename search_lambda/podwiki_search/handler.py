from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[2]
SIBLING_ZEROSEARCH = ROOT.parent / "zerosearch"
if SIBLING_ZEROSEARCH.exists():
    sys.path.insert(0, str(SIBLING_ZEROSEARCH))
# stemlite is optional: only needed when the index was built with a named
# stemmer. For local dev, find it beside the repo; when deployed it is vendored
# at the package root (already on the Lambda path) by prepare_lambda_package.py.
SIBLING_STEMLITE = ROOT.parent / "stemlite"
if SIBLING_STEMLITE.exists():
    sys.path.insert(0, str(SIBLING_STEMLITE))

from zerosearch import Index


INDEX_PATH = Path(os.environ.get("SEARCH_INDEX_PATH", "artifacts/search/search-index.zsx"))
_INDEX: Index | None = None
_STEM = None


def stemmer():
    """Word stemmer matching the loaded index (no-op if the index is unstemmed).

    Reranking compares the query against fields with substring/token matching, so
    it must stem the same way the index tokenized, or a query like ``startups``
    would rerank differently from its retrieval-equivalent ``startup``.
    """
    global _STEM
    if _STEM is None:
        name = getattr(index(), "_stemmer_name", None)
        try:
            from stemlite import get_stemmer
            _STEM = get_stemmer(name)
        except Exception:
            _STEM = lambda word: word
    return _STEM


def stem_text(value: object) -> str:
    stem = stemmer()
    return " ".join(stem(token) for token in normalize(value).split())


def index() -> Index:
    global _INDEX
    if _INDEX is None:
        _INDEX = Index.load(INDEX_PATH)
    return _INDEX


def response(status: int, body: dict, headers: dict[str, str] | None = None) -> dict:
    merged_headers = {
        "content-type": "application/json",
        "access-control-allow-origin": os.environ.get("CORS_ORIGIN", "*"),
    }
    if headers:
        merged_headers.update(headers)
    return {
        "statusCode": status,
        "headers": merged_headers,
        "body": json.dumps(body, ensure_ascii=False),
    }


def query_from_event(event: dict) -> str:
    params = event.get("queryStringParameters") or {}
    if params.get("q"):
        return params["q"]
    body = event.get("body")
    if body:
        try:
            payload = json.loads(body)
            return str(payload.get("q") or payload.get("query") or "")
        except json.JSONDecodeError:
            parsed = parse_qs(body)
            return parsed.get("q", [""])[0]
    return ""


def normalize(value: object) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", str(value).lower())
    return re.sub(r"\s+", " ", text).strip()


def all_tokens_match(tokens: list[str], value: str) -> bool:
    return bool(tokens) and all(token in value for token in tokens)


def rerank_results(query: str, results: list[dict]) -> list[dict]:
    phrase = stem_text(query)
    tokens = [token for token in phrase.split() if len(token) > 1]

    def bonus(result: dict) -> float:
        title = stem_text(result.get("title", ""))
        segment_title = stem_text(result.get("segment_title", ""))
        related_terms = stem_text(result.get("related_terms", ""))
        document_type = str(result.get("document_type", ""))

        value = 0.0
        if phrase and phrase in title:
            value += 200.0
        if phrase and phrase in segment_title:
            value += 120.0
        if phrase and phrase in related_terms:
            value += 80.0
        if all_tokens_match(tokens, title):
            value += 70.0
        if all_tokens_match(tokens, related_terms):
            value += 35.0
        if document_type == "page" and all_tokens_match(tokens, f"{title} {related_terms}"):
            value += 20.0
        return value

    return sorted(results, key=lambda item: (bonus(item), float(item.get("score", 0.0))), reverse=True)


def lambda_handler(event: dict, context: object) -> dict:
    path = (event.get("rawPath") or event.get("path") or "/").rstrip("/")
    method = (
        (event.get("requestContext") or {}).get("http") or {}
    ).get("method") or event.get("httpMethod") or "GET"

    if method == "OPTIONS":
        return response(204, {}, {"access-control-allow-methods": "GET,POST,OPTIONS"})
    if path == "/health":
        return response(200, {"ok": True, "app": "podwiki-search"})

    query = query_from_event(event).strip()
    if not query:
        return response(400, {"error": "missing query parameter q"})

    level = (event.get("queryStringParameters") or {}).get("level")
    allowed_levels = {
        "wiki",
        "guide",
        "comparison",
        "roadmap",
        "how_to",
        "podcast_summary",
        "person",
        "section",
    }
    filters = {"level": level} if level in allowed_levels else {}
    results = index().search(
        query,
        filter_dict=filters,
        boost_dict={"title": 4.0, "segment_title": 3.0, "text": 1.0},
        num_results=20,
    )
    results = rerank_results(query, results)
    return response(200, {"query": query, "results": results})
