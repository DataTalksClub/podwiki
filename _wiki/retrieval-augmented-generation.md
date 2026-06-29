---
layout: wiki
title: "Retrieval-Augmented Generation"
summary: "How the podcast archive explains RAG as retrieval, context design, generation, citation, and evaluation."
related:
  - Search, RAG, and Knowledge Systems
  - LLM Production Patterns
  - Search
  - Vector Databases
  - Embeddings
---

## Definition and Scope

RAG combines a retrieval system with a generative model. The system searches
external documents and passes selected context to an LLM. The model then answers
with that evidence. In the archive, RAG depends on search quality, chunking,
metadata, prompt design, citations, evaluation, latency, and cost.

Use [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
for the larger hub. Use [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for the broader production context.

## Contents

Use these links to jump between the main RAG sections.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

RAG starts with retrieval quality. Atita Arora's search episode treats RAG as
search plus generation. A useful RAG system still needs candidate generation,
ranking, metadata, and relevance evaluation. Daniel Svonava's production-search
episode adds the same point from search infrastructure. Embeddings and vector
indexes help, but production systems still need filters, recency, ranking, and
business signals.

Chunking is a design decision. The archive doesn't treat chunking as a
token-limit hack. Chunk size, overlap, metadata, and wrappers determine the
evidence the model receives. Podcast transcript search is a recurring example
because it needs episode title, guest, timestamp, and nearby context.

Long context doesn't remove retrieval. Long-context models make some
large-document tasks easier, but guests keep retrieval in the design. Lavanya
Gupta's long-context work shows failures in specialized domains around large
context windows. Ranjitha Kulkarni rejects the idea that RAG is dead because
latency, cost, noisy context, and garbage-in garbage-out still matter.

RAG isn't always an agent. RAG is usually enough when the system answers
from a knowledge base. Agents become useful when the system must plan, call
tools, look at state, or act on the result. The archive's practical advice is to
start with the smallest reliable system, then add tools or agentic behavior when
the workflow needs them.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Modern Search Systems](https://datatalks.club/podcast.html): The 30:38 and
  35:49 clips define RAG and use podcast transcripts as a chatbot example. The
  38:24 clip covers chunking, overlap, embedding models, and vectorization. The
  42:49 and 48:09 clips discuss citations, prompt design, human review, and
  multi-level evaluation.
- [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html): At
  44:26, presents RAG as a quick business win when chunking and embeddings fit
  the problem. At 48:20, compares fixed length, sliding windows, and context
  rotation. At 50:19, discusses when to move from RAG to tools and agents.
- [Deploying LLMs in Production](https://datatalks.club/podcast.html): At 40:46,
  uses retrieval for changing knowledge. At 42:02, explains indexing documents
  and retrieval-augmented responses. At 46:42, covers injected passages,
  summarizers, and grounding layers.
- [Building Agentic AI Systems](https://datatalks.club/podcast.html): The 29:30
  clip pushes back on "RAG is dead". The 32:48 and 36:11 clips stress chunk
  metadata, wrappers, and retrieval as an agent tool. The 37:39 clip separates
  RAG-enough use cases from agent use cases.
- [Applied LLM Research](https://datatalks.club/podcast.html): At 14:54, returns
  to chunking, retrieval, and summarization for large documents after discussing
  long-context limits.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})

## Maintenance Notes

Future updates should preserve the boundary between retrieval, generation, and
agent workflows.

- Keep detailed architecture checklists in
  [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
- Add a podcast summary for `practical-llm-engineering-and-rag.md`. It's the
  main source for chunking, generator-evaluator work, and RAG-to-agent
  boundaries.
- When expanding this page, preserve the distinction between retrieval quality,
  answer quality, and product outcome.
