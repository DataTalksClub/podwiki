---
layout: wiki
title: "Vector Databases"
summary: "How the podcast archive discusses vector databases as retrieval infrastructure for semantic search, RAG, recommendations, and multimodal matching."
related:
  - Search, RAG, and Knowledge Systems
  - Embeddings
  - Search
  - Retrieval-Augmented Generation
  - LLMs
---

## Definition and Scope

Vector databases store and search embeddings with nearest-neighbor methods. In
the archive, they appear in semantic search, RAG, recommendations, multimodal
retrieval, and personalization. Guests treat vector databases as one layer in a
retrieval system, not as the whole search product.

For the broader architecture, use
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).


## Recurring Archive Themes

Existing search stack or dedicated vector database is a real tradeoff. Atita
Arora's search episode compares vector support in an existing stack with a
standalone vector database. Existing systems can reduce operational sprawl when
they already serve production search. A dedicated vector database can reduce
migration risk or support vector experimentation.

Vector storage is different from vector compute. Daniel Svonava separates
vector compute from vector storage. The model or pipeline creates embeddings
during ingestion and at query time. The vector database stores and retrieves
them. This split affects reindexing, model versioning, latency, and consistency
between document vectors and query vectors.

Vector databases need ranking and business context. Nearest-neighbor search
doesn't solve every relevance problem. Production search still needs filters,
recency, popularity, personalization, metadata, and business constraints. The
archive warns against treating vector similarity as the final product metric.

Vector databases support more than chatbots. RAG is the most visible use
case, but the archive also covers session-based recommendations, e-commerce
personalization, re-ranking, multimodal image-text retrieval, and feature
fusion. Vector databases are retrieval infrastructure for many ML systems.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Modern Search Systems](https://datatalks.club/podcast.html): The 17:01 and
  20:27 clips introduce Qdrant and compare existing search stacks with
  standalone vector databases. The 38:24 clip uses vectorization inside a
  transcript RAG pipeline. The 52:07 clip discusses vector databases for ML use
  cases beyond RAG.
- [Production ML Search](https://datatalks.club/podcast.html): At 21:55,
  explains vector search through shared embedding representations. At 29:00,
  separates vector compute from storage. At 52:35, covers vector database
  selection and vendor tradeoffs. At 55:53, compares monolithic search systems
  with specialized vector databases.
- [Deploying LLMs in Production](https://datatalks.club/podcast.html): At 48:01,
  explains vector databases through embeddings, indexing, and semantic search in
  retrieval-augmented systems.
- [Production ML Search](https://datatalks.club/podcast.html): At 58:17, uses
  e-commerce personalization, embeddings, and CLIP as a concrete vector-search
  application.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
