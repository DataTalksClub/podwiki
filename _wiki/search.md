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

Search retrieves and ranks information for a query or generated answer. It sits
above [[information retrieval]] and ranking. Filters, evaluation, and serving
belong in the same product layer.
Classical search systems use lexical indexes such as Solr and Lucene. Newer
systems add [[embeddings]], [[vector databases]], hybrid retrieval, and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

This is the routing hub for the search cluster. [[Information Retrieval]] owns
retrieval mechanics, indexes, chunking, and candidate generation. [[Search
Relevance]] owns ranking quality, filters, product fit, and metric choices.

[[Vector Search vs Keyword Search]] compares lexical, vector, and hybrid
matching. [[Vector Database vs Search Engine]] covers where vector retrieval
should live in the infrastructure. [[Production Search Evaluation]] covers
offline tests, online experiments, monitoring, and business metrics.

## Retrieval and Ranking

Search systems retrieve candidates, rank them, then check whether the results
helped the product or downstream system. [[book:20210712-relevant-search=>Relevant
Search]] covers scoring, ranking, and tuning in Solr and Elasticsearch-era
systems. [[book:20211101-ai-powered-search=>AI-Powered Search]] extends that
discipline into learning-to-rank, vector retrieval, and LLM-era retrieval.

Candidate generation and ranking fail separately. A retriever can miss the
right result, and a ranker can bury a good result. [[Information Retrieval]]
covers retrieval units and index design. [[Search Relevance]] covers ranking
signals, filters, freshness, and product objectives. [[Production Search
Evaluation]] covers how teams measure both stages [[cite:building-production-search-systems=>Building Search Systems]].

## Lexical, Vector, and Hybrid Search

Lexical search matches query terms against indexed text, while vector search
matches learned representations. Hybrid search combines those candidates with
filters, freshness, metadata, and query-time weights [[cite:building-production-search-systems=>Building Search Systems]].

The main comparison lives in [[Vector Search vs Keyword Search]]. Use
[[Vector Database vs Search Engine]] when the question is whether vectors
belong in an existing search stack or a standalone vector database. Use
[[Knowledge Graph vs Vector Search]] when retrieval depends on explicit
relationships, paths, or provenance rather than only text and embedding
distance.

## RAG

RAG uses search to retrieve context before an LLM generates an answer. It adds
prompt packaging and answer checks after retrieval. It doesn't replace
retrieval design. In the transcript-chatbot example, teams still choose chunk
size and overlap. They also choose embeddings, retrieval count, prompt design,
and citation handling
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]].

Use [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the
full RAG workflow. Use [[Search and RAG Project Checklist]] for a practical
build path, and use [[LLM Evaluation Workflows]] when generated answers need
their own tests. RAG evaluation should keep retrieved passages separate from
generated answers [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>RAG Evaluation]].

## Vector Databases

Vector databases store embeddings and support nearest-neighbor retrieval, but
they're one component in a larger search system.

Adding vectors to an existing search stack differs from introducing a standalone
vector database
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Vectors in Existing Search]]).

[[Vector Databases]] covers
storage and nearest-neighbor retrieval. [[Vector Database vs Search Engine]]
covers placement and ownership decisions. Search teams still have to choose
filters, ranking signals, evaluation metrics, and reindexing jobs.

When retrieval feeds an LLM,
[[Graph RAG vs Vector RAG]]
marks another boundary. Dense chunks help semantic similarity, while graph
retrieval helps when relationships define the answer.

## Evaluation

Search evaluation checks retrieval quality, ranking quality, latency, and
product impact. Production systems connect those checks to business KPIs,
offline tests, [[a-b-testing=>A/B testing]], and operational metrics
([[cite:building-production-search-systems=>Building Search Systems]]).

Use [[Search Relevance]] for ranking and product-fit quality. Use
[[Production Search Evaluation]] for relevance labels, offline tests, and
online experiments. It also covers monitoring and result analysis. Use
[[Metrics]] when the team needs to decide which product decision a number
should change.

## Production Tradeoffs

Production search work starts after a prototype retrieves a few plausible
results. Teams have to keep indexes fresh and manage embedding model versions.
They also have to handle latency, support filters, monitor relevance drift, and
decide when to re-rank.

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

Search therefore sits across
[[Machine Learning System Design]],
[[llm-production-patterns=>LLM production work]],
and [[MLOps]]. The core question isn't
which retrieval technology is newest. The question is which search design gives
the product relevant, explainable, and measurable results.
