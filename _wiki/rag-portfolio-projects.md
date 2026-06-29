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
The archive treats RAG as search plus generation. Teams prepare documents,
attach chunk metadata, measure retrieval, ground prompts, and provide citations
or evidence that a human can look at.

Learners can use this page for AI engineering, LLM application, search, and
knowledge-system portfolios. For the archive's conceptual RAG synthesis, use
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).


## Project Criteria

Good RAG portfolio projects meet these criteria.

- Useful corpus: choose documents where retrieval is necessary. Good examples
  include changing knowledge, long documents, policies, tickets, transcripts,
  support docs, technical docs, research notes, and private organizational
  context.
- Document preparation: parse, clean, chunk, deduplicate, attach metadata, and
  preserve source provenance.
- Retrieval baseline: compare keyword, vector, and hybrid retrieval where
  practical. Don't assume embeddings solve the search problem by themselves.
- Grounded generation: require answers to cite retrieved evidence, say when
  evidence is missing, and avoid unsupported claims.
- Evaluation set: build a small gold set of questions, expected evidence,
  acceptable answers, and failure categories.
- Observability: log queries, retrieved chunks, prompts, model outputs, latency,
  cost, and user feedback.
- Iteration story: show how failure analysis changes chunking, metadata,
  retrieval, prompting, reranking, or scope.

## Project Types

Choose a project type that forces retrieval decisions into the open.

- Source-cited knowledge assistant: build an assistant over podcast transcripts,
  docs, handbooks, GitHub issues, legal policies, or research notes. Answers
  should include citations or source links and expose retrieved chunks for
  review.
- Search-first RAG project: start with a search UI, evaluate retrieval quality,
  then add generation. Include keyword search, vector search, filters, metadata,
  reranking, and a comparison of retrieval failures before and after changes.
- Document assistant: build an assistant that summarizes, extracts fields,
  classifies documents, or answers questions across emails, invoices, policies,
  tickets, or meeting notes. Keep the first version narrow.
- Evaluation and monitoring project: take an existing RAG demo and make it
  measurable. Add a gold set, regression tests, human review labels,
  answer-grounding checks, retrieval metrics, traces, and a failure-analysis
  dashboard.

## Project Proof

Use this checklist as the project review standard.

1. Question scope: name questions the system should answer, refuse, or route
   elsewhere.
2. Chunking and metadata: define the chunk unit, overlap, wrapper, title, source,
   timestamp, author, or section metadata.
3. Retrieval design: explain retrieval signals and balance filters, recency,
   exact terms, semantic similarity, and reranking.
4. Prompt rules: instruct the model to use evidence, cite sources, handle missing
   context, and format answers.
5. Evaluation: list gold-set questions, correctness criteria, and the split
   between retrieval failure and generation failure.
6. Debuggability: log the query, retrieved chunks, prompt, model, answer,
   latency, cost, and feedback.
7. Production caveats: document privacy, rate-limit, model-drift, reindexing,
   hallucination, and maintenance risks.

## Episode Evidence

These episodes anchor the project criteria.

- [Modern Search Systems](https://datatalks.club/podcast.html):
  at 30:38, RAG is framed as retrieval plus generation to reduce hallucinations.
  At 35:49, podcast transcript search becomes a concrete chatbot example.
  At 38:24, the episode covers chunking, overlap, embeddings, and vectorization.
  At 48:09, it introduces multi-level RAG evaluation and human review.
- [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html):
  at 13:56, Hugo Bowne-Anderson discusses generator-evaluator quality control.
  At 23:00, he covers gold tests and representative evaluation sets. At 26:43,
  failure analysis categorizes errors and retrieval fixes. At 44:26, RAG is a
  quick business win when chunking and embeddings fit the task.
- [Deploying LLMs in Production](https://datatalks.club/podcast.html):
  supports retrieval for changing knowledge, API versus open-source model
  tradeoffs, model drift risk, fine-tuning boundaries, and production deployment
  concerns.
- [Building Agentic AI Systems](https://datatalks.club/podcast.html):
  keeps the boundary between RAG and agents. Retrieval may be enough for
  knowledge lookup, while tools and agents add latency, cost, context noise, and
  evaluation complexity.
- [Production ML Search, Vector Search, Embeddings, Hybrid Search](https://datatalks.club/podcast.html):
  supports separating vector compute from vector storage and treating vector
  databases as one retrieval component, not the whole product.

## Anti-Patterns

Avoid these weak portfolio signals.

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

Use these pages for adjacent project and role context.

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
