---
layout: wiki
title: "RAG Portfolio Projects"
summary: "Archive-backed guidance for choosing RAG portfolio projects that prove retrieval quality, chunking, grounding, citations, evaluation, failure analysis, and production-minded LLM engineering."
related:
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - LLM Production Patterns
  - Embeddings
  - Vector Databases
---

## Definition and Scope

A RAG portfolio project should prove that the learner can build and evaluate a
retrieval-backed LLM system, not only call a chat API with a vector database.
The archive treats RAG as search plus generation: documents need preparation,
chunks need metadata, retrieval needs measurement, prompts need grounding, and
answers need citations or evidence that a human can inspect.

Use this page for AI engineering, LLM application, search, and knowledge-system
portfolios. For the archive's conceptual RAG synthesis, use
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).

## Contents

- [Project Criteria](#project-criteria)
- [Project Shapes](#project-shapes)
- [What the Project Should Demonstrate](#what-the-project-should-demonstrate)
- [Episode Evidence](#episode-evidence)
- [Anti-Patterns](#anti-patterns)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Project Criteria

Good RAG portfolio projects meet these criteria:

- **Useful corpus**: Choose documents where retrieval is necessary: changing
  knowledge, long documents, policies, tickets, transcripts, support docs,
  technical docs, research notes, or private organizational context.
- **Document preparation**: Parse, clean, chunk, deduplicate, attach metadata,
  and preserve source provenance.
- **Retrieval baseline**: Compare keyword, vector, and hybrid retrieval where
  practical. Do not assume embeddings solve the search problem by themselves.
- **Grounded generation**: Require answers to cite retrieved evidence, say when
  evidence is missing, and avoid unsupported claims.
- **Evaluation set**: Build a small gold set of questions, expected evidence,
  acceptable answers, and failure categories.
- **Observability**: Log queries, retrieved chunks, prompts, model outputs,
  latency, cost, and user feedback.
- **Iteration story**: Show how failure analysis changes chunking, metadata,
  retrieval, prompting, reranking, or scope.

## Project Shapes

### Source-Cited Knowledge Assistant

Build an assistant over a corpus such as podcast transcripts, docs, handbooks,
GitHub issues, legal policies, or research notes. The answer should include
citations or source links and expose retrieved chunks for inspection.

This is the strongest general RAG portfolio shape because it forces the learner
to handle provenance, chunking, and answer support.

### Search-First RAG Project

Start with a search UI, evaluate retrieval quality, then add generation. Include
keyword search, vector search, filters, metadata, reranking, and a comparison of
retrieval failures before and after changes.

This project aligns with the archive's warning that RAG is not a replacement
for information retrieval.

### Document Workflow Assistant

Build an assistant that summarizes, extracts fields, classifies documents, or
answers questions across emails, invoices, policies, tickets, or meeting notes.
Keep the first version narrow. Add tools or agentic behavior only when the
workflow requires action beyond retrieval and response.

### Evaluation and Monitoring Project

Take an existing RAG demo and make it measurable. Add a gold set, regression
tests, human review labels, answer-grounding checks, retrieval metrics, traces,
and a failure-analysis dashboard. A simple UI is enough if the evaluation
surface is strong.

## What the Project Should Demonstrate

Use this checklist as the project review standard:

1. **Question scope**: Which questions should the system answer, refuse, or route
   elsewhere?
2. **Chunking and metadata**: What is the chunk unit, overlap, wrapper, title,
   source, timestamp, author, or section metadata?
3. **Retrieval design**: Which retrieval signals are used, and how are filters,
   recency, exact terms, semantic similarity, and reranking balanced?
4. **Prompt contract**: How does the prompt instruct the model to use evidence,
   cite sources, handle missing context, and format answers?
5. **Evaluation**: Which questions are in the gold set, what counts as correct,
   and how are retrieval failure and generation failure separated?
6. **Debuggability**: Can another person see the query, retrieved chunks, prompt,
   model, answer, latency, cost, and feedback?
7. **Production caveats**: What are the privacy, rate-limit, model-drift,
   reindexing, hallucination, and maintenance risks?

## Episode Evidence

| Episode | Portfolio Evidence |
| --- | --- |
| [Modern Search Systems](https://datatalks.club/podcast.html) | At 30:38, RAG is framed as retrieval plus generation to reduce hallucinations. At 35:49, podcast transcript search becomes a concrete chatbot example. At 38:24, the episode covers chunking, overlap, embeddings, and vectorization. At 48:09, it introduces multi-level RAG evaluation and human review. |
| [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html) | At 13:56, Hugo Bowne-Anderson discusses generator-evaluator quality control. At 23:00, he covers gold tests and representative evaluation sets. At 26:43, failure analysis categorizes errors and retrieval fixes. At 44:26, RAG is positioned as a quick business win when chunking and embeddings fit the task. |
| [Deploying LLMs in Production](https://datatalks.club/podcast.html) | Supports retrieval for changing knowledge, API versus open-source model tradeoffs, model drift risk, fine-tuning boundaries, and production deployment concerns. |
| [Building Agentic AI Systems](https://datatalks.club/podcast.html) | Keeps the boundary between RAG and agents: retrieval may be enough for knowledge lookup, while tools and agents add latency, cost, context noise, and evaluation complexity. |
| [Production ML Search, Vector Search, Embeddings, Hybrid Search](https://datatalks.club/podcast.html) | Supports separating vector compute from vector storage and treating vector databases as one retrieval component, not the whole product. |

## Anti-Patterns

- "Chat with PDF" with no retrieval evaluation, citations, or visible source
  chunks.
- Embedding every document into a vector database without cleaning, metadata,
  deduplication, or chunking rationale.
- Only evaluating whether the final answer sounds plausible.
- Hiding prompts, retrieved context, model version, and retrieval scores from
  the README.
- Treating long context or agents as a reason to skip retrieval design.
- Claiming production readiness without cost, latency, privacy, model drift, or
  reindexing notes.

## Related Pages

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/modern-search-systems-vector-databases-llms-semantic-retrieval.md`,
  `../datatalksclub.github.io/_podcast/practical-llm-engineering-and-rag.md`,
  `../datatalksclub.github.io/_podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.md`,
  `../datatalksclub.github.io/_podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.md`,
  and `../datatalksclub.github.io/_podcast/production-ml-search-vector-search-embeddings-hybrid-search.md`.
- Future expansion should add a compact RAG project rubric with beginner,
  interview-ready, and production-like levels.
- Keep this page project-focused. Detailed conceptual synthesis belongs in the
  RAG and search wiki pages.
