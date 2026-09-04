---
title: "Data Ingestion — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=e0owGI2JV-s&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' code: - label: 'persistent_rag_ingest.ipynb' path: 'code/persistent_rag_ingest.ipynb' - label: 'persinsent_rag.ipynb' path..."
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Data Ingestion

## Notes

---
video_url: "https://www.youtube.com/watch?v=e0owGI2JV-s&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
code:
  - label: "persistent_rag_ingest.ipynb"
    path: "code/persistent_rag_ingest.ipynb"
  - label: "persinsent_rag.ipynb"
    path: "code/persinsent_rag.ipynb"
---
# Data Ingestion

So far, our RAG pipeline loads data and builds the search index at
startup. With minsearch, this is fine - our FAQ dataset is small, so
indexing takes less than a second. The entire pipeline runs in one
process.

This breaks down as the dataset grows. Fetching data takes time -
calling APIs, parsing files, cleaning text. With millions of
documents, the startup becomes slow. You don't want to wait minutes
every time your service restarts.

Minsearch is in-memory. It's a bunch of Python dictionaries bound to
the process where it's running. When you stop the process, the data
disappears, so you re-index every time you restart. That's wasteful if
indexing is slow or the data takes time to prepare.

So we separate ingestion from querying. One process writes the data to
a persistent search index. Another process reads from it. The two run
independently and only share the index between them.

The index survives restarts, so we ingest once and query as often as
we like. This is the ingestion step from data engineering. We move data
from its source into a target system the application can use.

You can use any persistent search backend for this, such as
Elasticsearch, OpenSearch, or Qdrant. In this module, we use
[sqlitesearch](https://github.com/alexeygrigorev/sqlitesearch), a
lightweight search library backed by SQLite FTS5. It has the same API
as minsearch, so it's a drop-in replacement that happens to be
persistent.

I picked SQLite because it asks nothing of you. It ships with Python,
so you don't add any dependency, and it has FTS5 (full text search)
built in. If you have Python, you already have a full text search
engine. Using FTS5 directly is a bit awkward, so I wrote sqlitesearch
as a convenient wrapper around it.

You can read more about the history of this library [here](https://aishippingblog.com/p/how-i-built-sqlitesearch-a-lightweight).

Install it:

```bash
uv add sqlitesearch
```

## Ingestion notebook

Create a new notebook called `sqlite-ingest.ipynb` (see persistent_rag_ingest.ipynb for reference). This is the
ingestion process - it fetches data and writes it to a persistent
index.

First, load the data using the function from `ingest.py`:

```python
from ingest import load_faq_data

documents = load_faq_data()
print(f"Loaded {len(documents)} documents")
```

Filter to just the LLM Zoomcamp documents:

```python
docs_llm = [doc for doc in documents if doc["course"] == "llm-zoomcamp"]
print(f"LLM Zoomcamp: {len(docs_llm)} documents")
```

Now create a sqlitesearch index and add documents one by one with a
small delay (to simulate slow ingestion):

```python
import time
from sqlitesearch import TextSearchIndex

index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)

for doc in docs_llm:
    index.add(doc)
    print(f"""Added: {doc["question"][:60]}...""")
    time.sleep(0.5)

index.close()
print("Done. Index saved to faq.db")
```

Run this notebook. You'll see each document being added one by one.
When it's done, there's a `faq.db` file on disk with the entire index.
This file persists across restarts.

## Querying notebook

While the ingestion is running (or after it finishes), create another
notebook (see persinsent_rag.ipynb for reference).

Connect to the same database:

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)
```

Check how many documents are in the index:

```python
sqlite_index.count()
```

Run this cell a few times while the other notebook is still ingesting.
You'll see the number growing as ingestion progres

## Key concepts

- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=e0owGI2JV-s&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/09-data-ingestion.md)
