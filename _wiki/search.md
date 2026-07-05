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
  - Production Search Evaluation
  - Vector Databases
  - Embeddings
  - NLP
  - A/B Testing
---

Search retrieves, ranks, and serves information for a query or generated
answer. It's the broad product and system layer above [[information
retrieval]], [[search-relevance=>search relevance]], and [[production search
evaluation]]. Classical search systems use lexical indexes such as Solr and
Lucene. Newer systems add [[embeddings]], [[vector databases]], hybrid
retrieval, and [[retrieval-augmented-generation=>retrieval-augmented
generation]] [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Use this hub to move through the search cluster. [[Information Retrieval]]
covers retrieval mechanics, indexes, chunking, and candidate generation.
[[Search Relevance]] covers ranking quality, filters, and product fit.
[[Production Search Evaluation]] covers offline tests, online experiments,
monitoring, and business metrics.

[[Vector Search vs Keyword Search]] compares lexical, vector, and hybrid
matching methods. [[Vector Database vs Search Engine]] covers where vector
retrieval should live in the infrastructure. [[Knowledge Graph vs Vector
Search]] covers retrieval that depends on typed relationships, paths, or
provenance.

## Search System Layers

Search systems retrieve candidates, rank them, then check whether the results
helped the product or downstream system. [[book:20210712-relevant-search=>Relevant
Search]] covers scoring, ranking, and tuning in Solr and Elasticsearch-era
systems. [[book:20211101-ai-powered-search=>AI-Powered Search]] extends that
discipline into learning-to-rank, vector retrieval, and LLM-era retrieval.

Candidate generation and ranking fail separately. A retriever can miss the
right result, and a ranker can bury a good result. This hub keeps those layers
together because teams still have to serve one result page or one context set
to the product [[cite:building-production-search-systems=>Building Search Systems]].

## Retrieval Methods

Lexical search matches query terms against indexed text, while vector search
matches learned representations. Hybrid search combines those candidates with
filters, freshness, metadata, and query-time weights [[cite:building-production-search-systems=>Building Search Systems]].

Use [[Vector Search vs Keyword Search]] when the decision is lexical matching,
semantic matching, or hybrid retrieval. Use [[Vector Database vs Search Engine]]
when the decision is whether vectors belong in an existing search stack or a
standalone vector database. Use [[Knowledge Graph vs Vector Search]] when the
retrieval question depends on explicit relationships rather than only text and
embedding distance.

## RAG and Vector Infrastructure

RAG uses search to retrieve context before an LLM generates an answer. It adds
prompt packaging and answer checks after retrieval. It doesn't replace
retrieval design. In the transcript-chatbot example, teams still choose chunk
size and overlap. They also choose embeddings, retrieval count, prompt design,
and citation handling
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]].

Use [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the
full RAG workflow and [[LLM Evaluation Workflows]] when generated answers need
their own tests. Use [[Vector Databases]] for storage and nearest-neighbor
indexing. Use [[Vector Database vs Search Engine]] for placement and ownership
decisions [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Vectors in Existing Search]].

When retrieval feeds an LLM,
[[Graph RAG vs Vector RAG]]
marks another boundary. Dense chunks help semantic similarity, while graph
retrieval helps when relationships define the answer.

## Measurement and Operations

Search evaluation checks retrieval quality, ranking quality, latency, and
product impact. Production systems connect those checks to business KPIs,
offline tests, [[a-b-testing=>A/B testing]], and operational metrics
([[cite:building-production-search-systems=>Building Search Systems]]).

Use [[Search Relevance]] for ranking and product-fit quality. Use [[Production
Search Evaluation]] for relevance labels, offline tests, online experiments,
and monitoring. Use [[Metrics]] when the team needs to decide which product
decision a number should change.

These tradeoffs appear in everyday search systems. Keyword-search brittleness,
synonyms, and configuration debt show up on the lexical side. Recomputing
embeddings and keeping pipelines flexible matter when models change.
E-commerce [[machine-learning-personalization=>personalization]] with CLIP-style
embeddings is one example of moving from prototype to production
([[cite:building-production-search-systems=>Building Search Systems]]).

On the migration side, standalone vector storage isn't always the right move.
Existing search systems may already handle lexical relevance, filters, and
operational needs. That includes Solr, Lucene, or Elasticsearch systems. A new
vector component helps only if it improves the actual retrieval and ranking problem
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

Search therefore sits across [[Machine Learning System Design]],
[[llm-production-patterns=>LLM production work]], and [[MLOps]]. The core
question is which search design gives the product relevant, explainable, and
measurable results.
