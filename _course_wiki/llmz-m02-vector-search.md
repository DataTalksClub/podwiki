---
title: "Vector Search — LLM Zoomcamp Module 2"
summary: "--- video_url: 'https://www.youtube.com/watch?v=qyZgxTmC2cY&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Vector Search"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Vector Search

## Notes

---
video_url: "https://www.youtube.com/watch?v=qyZgxTmC2cY&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Vector Search

In module 1 we used keyword search with minsearch and sqlitesearch.
It matches exact words. If you search for "Docker", the document has
to contain "Docker" to come back.

But look at these two questions:

- "Can I still join the course after the start date?"
- "Is it possible to enroll late?"

They mean the same thing, yet they share almost no words. A keyword
engine struggles to match them. We need something that works on
meaning, not on the exact words.

That something is vector search. Instead of matching words, it matches
ideas.

## The vector search process

We run vector search in two stages.

1. Offline (indexing): we convert all documents into vectors (arrays
   of numbers) and store them in an index.
2. Online (querying): we convert the user's query into a vector with
   the same model, then find the closest document vectors by similarity.

An embedding model produces these vectors. It's a neural network
trained to capture meaning, so texts that mean similar things land on
similar vectors. We measure how close two vectors are with a distance
metric. The most common one is cosine similarity.

Cosine similarity measures the angle between two vectors:

- Vectors pointing in the same direction: similarity close to 1
  (similar)
- Vectors at right angles: similarity close to 0 (unrelated)
- Vectors pointing in opposite directions: similarity close to -1
  (opposite meaning)

The larger the cosine similarity, the more similar the two texts are
in meaning.

## Keyword search vs vector search

Here's how the two approaches differ:

- Keyword search matches exact words. Vector search matches meaning.
- Keyword search suits specific terms, IDs, and names. Vector search
  suits paraphrased questions and natural language.
- Keyword search example: "pandas dataframe". Vector search example:
  "How do I work with tabular data?"
- Keyword search uses an inverted index (BM25, TF-IDF). Vector search
  uses a vector index based on cosine similarity.
- Keyword search misses synonyms and paraphrases. Vector search misses
  exact term matches.

Vector search is usually better, but it adds a lot of operational
complexity, and you'll feel that throughout this module. So my advice
is to never start with vector search. Start with text search, and reach
for vectors once you can show they're worth the extra cost.

In practice the two work best together. Hybrid search combines them,
and we cover it in the
Best Practices module.

## Building vector search

We'll take the same FAQ dataset from module 1 and build vector search
with three tools:

1. minsearch - in-memory vector search (simplest, good for
   experiments)
2. sqlitesearch - persistent vector search backed by SQLite
   (production-friendly, same API as minsearch)
3. PGVector - vector search in PostgreSQL (scalable, runs in
   Docker)

Then we'll plug vector search into our RAG pipeline.

The code from this module is available in the
code directory.

## Prerequisites

In module 1 we set up a project with several libraries. Here we also
install sentence-transformers. It pulls in PyTorch and is heavy, so I
recommend a fresh project (a separate Codespace) for this module alone.

If you're starting from scratch, create a new project and install the
module 1 libraries:

```bash
mkdir llm-zoomcamp-code
cd llm-zoomcamp-code
uv init
uv add requests minsearch openai jupyter python-dotenv
```

You also need a `.env` file with your API key. See the
module 1 environment setup
for details.

## Key concepts

- [Hybrid Search](/course-wiki/hybrid-search/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)
- [Neural Networks](/course-wiki/neural-networks/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=qyZgxTmC2cY&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/01-intro.md)
