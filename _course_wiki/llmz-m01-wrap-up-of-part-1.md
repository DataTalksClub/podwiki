---
title: "Wrap-up of Part 1 — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=RPXMz5p5fb8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Wrap-up of Part 1"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Wrap-up of Part 1

## Notes

---
video_url: "https://www.youtube.com/watch?v=RPXMz5p5fb8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Wrap-up of Part 1

In Part 1 of this module, we:

- Learned what RAG is and why it matters: retrieve documents, build a
  prompt, let the LLM generate a grounded answer
- Built a search engine over a real FAQ dataset using minsearch
- Created a prompt template that combines the user's question with
  search results
- Wired search + prompt + LLM into a working RAG pipeline
- Split ingestion and query into separate processes with sqlitesearch

You now have a working RAG system and a clear mental model for how each
piece fits together. From here, the work is making each piece better.

## Two directions forward

Part 2 of this module: Agents. Our pipeline runs
search once with the exact user query, unchanged. If that search
returns garbage, the LLM has no way to recover. An agent puts the LLM
in charge instead. It decides what to search for, how many searches to
run, and when to stop.

An agent also handles questions in another language. It translates the
query before searching, then translates the answer back afterward.

Module 2: Vector Search. Keyword matches
are exact. Vector search matches by semantic meaning instead, which
helps when the user phrases things differently from the FAQ.

## Elasticsearch

Elasticsearch is the industry standard for text search.

It supports:

- Full-text search with BM25
- Filtering, aggregations, and faceting
- Vector search (dense and sparse)
- Distributed scaling
- Real-time indexing

It's heavier than sqlitesearch but handles production workloads at
scale. If you're building a real RAG system, Elasticsearch (or
OpenSearch) is a common choice for the search backend.

For an Elasticsearch tutorial, see the
[supplementary materials for Module 1](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2025/01-intro/elastic-search.md).

## Fine-tuning vs RAG

Instead of retrieving documents at query time, you could fine-tune
the LLM on your data.

Fine-tuning means taking a model's weights and adjusting them for
your specific use case.

This works, but it has downsides:

- It requires special hardware (GPUs) and tools we don't cover in
  this course
- It's difficult to update when new data arrives - you don't want to
  retrain the model every time a new FAQ entry is added
- The LLM already has internal knowledge, but RAG gives it access to
  information it wasn't trained on

RAG is more flexible, cheaper, and works with any LLM. In practice,
fine-tuning is rarely needed. I've never personally hit a case that
required it. When I analyzed around 2,500 job descriptions for my AI
engineering field guide, few asked for it. So focus on RAG first, and
reach for fine-tuning only when you genuinely need it.

## Moving forward

Try these next steps:

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Try Elasticsearch as a search backend

## Key concepts

- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
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
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
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

- [Video](https://www.youtube.com/watch?v=RPXMz5p5fb8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/10-rag-next-steps.md)
