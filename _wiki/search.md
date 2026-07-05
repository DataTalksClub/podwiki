---
layout: wiki
title: "Search"
summary: "Search as retrieval, ranking, evaluation, semantic matching, and product relevance."
related:
  - Information Retrieval
  - Search Relevance
  - Retrieval-Augmented Generation
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Knowledge Graph vs Vector Search
  - Production Search Evaluation
  - Vector Databases
  - Embeddings
  - NLP
  - A/B Testing
---

Search retrieves, ranks, and serves information for queries and generated
answers. It can also serve recommendation use cases. It's the product and system layer above [[information
retrieval]], [[search-relevance=>search relevance]], and [[production search
evaluation]]. Classical systems use lexical indexes such as Solr and Lucene.
Newer systems add [[embeddings]], [[vector databases]], hybrid retrieval, and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

At the search layer, teams connect retrieval mechanics and ranking quality.
They also connect evaluation and infrastructure choice. [[Information
Retrieval]] covers retrieval units, indexes, and prefilters. It also covers
chunking and candidate generation.

[[Search Relevance]] covers result order, filters, freshness, and product fit.
[[Production Search Evaluation]] covers offline tests, online experiments,
monitoring, and business metrics. [[Vector Search vs Keyword Search]] compares
matching methods, while [[Vector Database vs Search Engine]] compares service
ownership.

## Search System Layers

Search systems retrieve candidates and rank them. They then serve a result page,
recommendation set, or context set. [[book:20210712-relevant-search=>Relevant
Search]] covers scoring, ranking, and tuning in Solr and Elasticsearch-era
systems. [[book:20211101-ai-powered-search=>AI-Powered Search]] extends that
discipline into learning-to-rank, vector retrieval, and LLM-era retrieval.

Candidate generation and ranking fail separately. A retriever can miss the
right result, and a ranker can bury a good result. Search teams still have to
serve one result page or one context set to the product
[[cite:building-production-search-systems=>Building Search Systems]].

## Matching Methods

Lexical search matches query terms against indexed text, while vector search
matches learned representations. Hybrid search combines those candidates with
filters, freshness, metadata, and query-time weights [[cite:building-production-search-systems=>Building Search Systems]].

[[Vector Search vs Keyword Search]] compares matching methods, and [[Vector
Database vs Search Engine]] compares serving boundaries. [[Knowledge Graph vs
Vector Search]] applies when retrieval depends on explicit relationships
rather than only text and embedding distance.

## RAG and Vector Infrastructure

RAG uses search to retrieve context before an LLM generates an answer. It adds
prompt packaging and answer checks after retrieval. It doesn't replace
retrieval design. In the transcript-chatbot example, teams still choose chunk
size, overlap, and embeddings. They also choose retrieval count, prompt design,
and citation handling
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]].

[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers the
full RAG workflow, and [[LLM Evaluation Workflows]] covers generated-answer
tests. [[Vector Databases]] covers storage and nearest-neighbor indexing.
[[Vector Database vs Search Engine]] covers placement and service-boundary
decisions [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Vectors in Existing Search]].

When retrieval feeds an LLM, [[Graph RAG vs Vector RAG]] marks another
boundary. Dense chunks help semantic similarity, while graph retrieval helps
when relationships define the answer.

## Measurement and Operations

Search evaluation checks retrieval quality, ranking quality, latency, and
product impact. Production systems connect those checks to business KPIs,
offline tests, [[a-b-testing=>A/B testing]], and operational metrics
([[cite:building-production-search-systems=>Building Search Systems]]).

[[Search Relevance]] covers ranking and product-fit quality. [[Production
Search Evaluation]] covers relevance labels, offline tests, online
experiments, and monitoring. [[Metrics]] covers the product decision a number
should change.

Those operating concerns show up differently across the cluster.
Keyword-search brittleness, synonyms, and configuration debt belong with
[[Vector Search vs Keyword Search]]. Recomputing embeddings and keeping vector
pipelines flexible belong with [[Vector Databases]]. Whether Solr, Lucene,
Elasticsearch, or a standalone vector database should own retrieval belongs
with [[Vector Database vs Search Engine]]
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

Search therefore sits across [[Machine Learning System Design]],
[[llm-production-patterns=>LLM production work]], and [[MLOps]]. The core
question is which search design gives the product relevant, explainable, and
measurable results.
