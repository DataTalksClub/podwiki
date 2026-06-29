---
layout: wiki
title: "Search"
summary: "How the podcast archive frames search as retrieval, ranking, evaluation, semantic matching, and product relevance."
related:
  - Search, RAG, and Knowledge Systems
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - NLP
---

## Definition and Scope

Search helps people or systems find relevant information. In the archive, search
includes classical information retrieval, candidate generation, ranking,
semantic retrieval, vector search, hybrid retrieval, personalization, and RAG.

Use [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
as the larger hub. This bridge keeps the narrower search vocabulary available
for people pages, episode topics, and cross-links.

## Contents

Use these links to jump between the main search sections.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

Search is a relevance system, not only a database query. Daniel Svonava's
production-search episode starts from information retrieval as a decision
problem. A production search system usually separates candidate generation from
ranking. Teams then tune relevance, freshness, latency, filters, and business
constraints.

Classical search still matters in the LLM era. Atita Arora's search episode
roots modern systems in Solr, Lucene, OpenNLP, and query-content matching. Vector
search and RAG add new retrieval modes, but they don't remove keyword search,
filtering, evaluation, or user-centered relevance metrics.

Hybrid retrieval is the practical center. The archive rarely treats keyword
search and vector search as mutually exclusive. Keyword search handles exact
terms, constraints, and explainability. Vector search handles semantic
similarity, synonyms, language variation, and multimodal matching. Production
systems combine signals, then measure what changes for users and the business.

Search quality and RAG quality are related but separate. A RAG system can
fail because the retriever finds the wrong chunk. It can also fail because the
prompt loses the citation, the model hallucinates, or the answer doesn't solve
the product need. The archive's search episodes keep retrieval evaluation
separate from final answer evaluation.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Modern Search Systems](https://datatalks.club/podcast.html): The 4:42 and
  9:18 clips connect Solr, Lucene, and NLP-based query matching. The 20:27 clip
  compares vectors in existing search stacks with standalone vector databases.
  The 23:00 clip links personalization, learning to rank, and LLM-era search.
- [Production ML Search](https://datatalks.club/podcast.html): The 8:00 and
  12:45 clips define search as an information-retrieval decision problem and
  separate retrieval from ranking. The 17:40 and 20:02 clips recommend practical
  indexes over hand-rolled keyword rules. The 34:00 clip covers hybrid search
  with filters and recency.
- [Modern Search Systems](https://datatalks.club/podcast.html): At 52:07,
  extends vector databases beyond RAG into ML use cases such as session-based
  recommendations and re-ranking. At 54:54, compares personalization
  approaches.
- [Production ML Search](https://datatalks.club/podcast.html): At 61:25, ties
  search metrics to business KPIs and A/B tests.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})

## Maintenance Notes

Future updates should label each search example by the layer it supports.

- Add a compact podcast summary for `production-ml-search-vector-search-embeddings-hybrid-search.md`.
- Keep search architecture guidance in the larger hub unless a future episode
  gives enough material for a dedicated production search checklist.
- When adding examples, label whether they concern candidate retrieval, ranking,
  evaluation, personalization, or RAG answer generation.
