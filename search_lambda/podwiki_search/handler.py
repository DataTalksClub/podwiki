from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import parse_qs

ROOT = Path(__file__).resolve().parents[2]
SIBLING_ZEROSEARCH = ROOT.parent / "zerosearch"
if SIBLING_ZEROSEARCH.exists():
    sys.path.insert(0, str(SIBLING_ZEROSEARCH))

from zerosearch import Index


INDEX_PATH = Path(os.environ.get("SEARCH_INDEX_PATH", "artifacts/search/search-index.zsx"))
_INDEX: Index | None = None


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
    allowed_levels = {"wiki", "article", "podcast_summary", "person", "section"}
    filters = {"level": level} if level in allowed_levels else {}
    results = index().search(
        query,
        filter_dict=filters,
        boost_dict={"title": 4.0, "segment_title": 3.0, "text": 1.0},
        num_results=20,
    )
    return response(200, {"query": query, "results": results})
