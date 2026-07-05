---
layout: article
tags: ["comparison"]
title: "Vector/Keyword Search"
keyword: "vector search vs keyword search"
summary: "A comparison of keyword search, vector search, and hybrid retrieval methods for exact terms, semantic neighbors, and filters."
related_wiki:
  - Search
  - Vector Databases
  - Embeddings
  - Information Retrieval
  - Production Search Evaluation
  - Search Relevance
  - Vector Database vs Search Engine
---

Keyword search matches query terms against indexed text. Vector search matches
a query embedding against nearby item embeddings in a learned representation
space. The matching-method boundary is exact terms, semantic neighbors, and
hybrid retrieval. Neither method replaces the rest of
[[information retrieval]]. Search systems still need ranking, filters, latency
work, and [[production search evaluation]].

The retrieval-method comparison asks how lexical matching, semantic matching,
and hybrid matching produce candidates. [[Search]] covers the product layer,
[[Embeddings]] covers learned representations, and [[Vector Databases]] covers
storage and indexing infrastructure
[[cite:building-production-search-systems=>Building Search Systems]][[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].
The standalone-vector-database choice belongs with [[Vector Database vs Search
Engine]], where vectors, filters, and serving become infrastructure ownership
questions.

Production search systems often separate candidate generation from ranking.
Teams then measure hybrid search and query-time weights in the same relevance
system
[[cite:building-production-search-systems=>Building Search Systems]][[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].

## Core Difference

Keyword search starts with tokens. A Lucene-style inverted index maps words or
normalized terms to the documents or positions where they appear. Existing
engines such as Lucene usually make more sense than a hand-rolled reverse
keyword lookup. [[cite:building-production-search-systems=>Building Search Systems]]

Solr, Lucene, Elasticsearch, and OpenSearch show the classical search lineage
behind full-text query-content matching
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Vector search starts with representations: the system embeds records and
queries, then searches for nearby vectors
[[cite:building-production-search-systems=>Building Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].
[[Embeddings]] covers model choice, representation drift, multimodal vectors,
and non-search uses. At the matching layer, semantic similarity changes which
candidates enter retrieval.

In practice, the two methods fail differently. Keyword search can miss relevant
items when query wording differs from indexed wording. Vector search can
retrieve plausible semantic neighbors that ignore exact terms, source
constraints, freshness, or metadata filters. Hybrid retrieval exists because
teams often need both matching behaviors before ranking applies product
objectives.

## Keyword Strengths

Keyword search is strong when exact language matters. Exact terms, domain
vocabulary, and metadata filters need predictable matching. An inverted index
is still a practical candidate-generation tool. [[cite:building-production-search-systems=>Building Search Systems]]
It narrows a large corpus quickly before ranking decides what the user should
see.

Lucene-style `must` and `should` clauses give teams explicit control over
strict and weighted constraints. [[cite:building-production-search-systems=>Building Search Systems]]
A strict keyword or metadata filter can enforce a business rule. A soft clause
can keep a highly relevant older result in play. Vector systems face similar
constraints around filters, recency, and business rules. [[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

Keyword systems require ongoing maintenance
[[cite:building-production-search-systems=>Building Search Systems]].
Synonyms, query rewrites, and dictionaries can reduce brittleness, but they
also create configuration debt
[[cite:building-production-search-systems=>Building Search Systems]].
Search quality still needs user-centric metrics and relevance work after the
system matches content to the query. [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Vector Strengths

Vector search is strongest when people describe intent differently from the
stored text [[cite:building-production-search-systems=>Building Search Systems]].
Embeddings map queries and candidate items into shared representations
[[cite:building-production-search-systems=>Building Search Systems]].

Queries and candidate items can land near each other even when the exact words
differ. That makes vector search useful for semantic retrieval and
cross-language queries. The same matching behavior helps synonym-heavy queries,
multimodal retrieval, and personalization.

RAG systems use vector search when the question may not share exact words with
the passage that contains the answer. Atita's transcript-chatbot example chunks
podcast transcripts, embeds the chunks, and retrieves relevant passages before
answer generation and citations
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers the
generation and citation workflow.

Vector search also extends beyond text through CLIP-style text-to-image
retrieval, ecommerce personalization, session-based recommendations, and
reranking
[[cite:building-production-search-systems=>Building Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]][[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
Those examples depend on embeddings. At the matching layer, semantic candidates
still pass through ranking, filters, and product constraints.

## Hybrid Matching

Hybrid retrieval is the recurring production answer. A news search result may
need semantic relevance and freshness at the same time
[[cite:building-production-search-systems=>Building Search Systems]].

A hard one-month filter can remove a relevant article, while pure vector
similarity can ignore recency. The search system has to decide which signals
are mandatory. It also has to decide which signals are soft. Query-time weights
make that decision operational.

Hybrid systems combine vector similarity with filters, recency, and metadata.
They can also use behavior, popularity, and time encoding. Normalization and
query-time weighting belong in the same matching layer. [[Search Relevance]]
covers how the final order serves product objectives
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].

Teams can migrate search incrementally and tune hybrid matching before settling
the system boundary [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
That ownership choice belongs in [[Vector Database vs Search Engine]].

## Ranking Handoff

Both methods only produce candidates, and ranking decides which candidates
deserve the top positions
[[cite:building-production-search-systems=>Building Search Systems]].
After retrieval narrows the search space, ranking estimates relevance and
product objectives such as click or purchase
probability [[cite:building-production-search-systems=>Building Search Systems]].
A vector nearest-neighbor result can still rank poorly if it ignores freshness,
source constraints, business rules, or product priorities.

Vector-side approaches can encode recency, behavior, metadata, or popularity
into vector features. They can also normalize components and choose weights at
query time
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].
[[Embeddings]] covers the representation risk behind those features. This
comparison keeps the focus on how the search system combines them with lexical
matches.

Exact-match queries and semantic queries can fail for different reasons.
[[search-relevance=>Search relevance]] covers ranking quality, and
[[production-search-evaluation=>production search evaluation]] covers the
measurement workflow.

## Method Checks

Keyword search needs checks for exact-match coverage, synonym behavior, field
weighting, and filters. Query rewrites and synonym rules can help, but they can
also create configuration debt and unexpected matches
[[cite:building-production-search-systems=>Building Search Systems]].

Vector search needs checks for nearest-neighbor quality against the task. The
neighbors should contain the needed evidence, products, images, or chunks. A
RAG answer can still fail when the vector store returns similar chunks. Those
chunks may be incomplete, poorly bounded, or weakly cited
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Hybrid search needs checks for how lexical matches and vector similarity
interact with filters. Freshness and query-time weights belong in the same
check
[[cite:building-production-search-systems=>Building Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].
[[Search Relevance]] covers ranking objectives. [[Production Search
Evaluation]] covers offline tests, A/B tests, monitoring, and business metrics.

## Choosing Retrieval

Choose keyword search when exact terms and filters dominate the task. Metadata
fields, auditability, and predictable behavior support the same choice.
Those needs fit inverted-index candidate generation
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]][[cite:building-production-search-systems=>Building Search Systems]].

Choose vector search when semantic recall or paraphrases are the main problem.
Multimodal matching and session similarity support the same choice. RAG context
retrieval does too.

Transcript-chatbot retrieval, embeddings, and multimodal retrieval support that
choice [[cite:building-production-search-systems=>Building Search Systems]][[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].

Choose hybrid retrieval when the product needs lexical matching and
freshness-sensitive semantic search. [[cite:building-production-search-systems=>Building Search Systems]][[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]
Hybrid approaches also keep metadata filters, recency, and permissions in the
same decision. Popularity, ranking, and business metrics stay there too.

For the broader retrieval map, use [[Search]] and [[Information Retrieval]].
For representation and storage, use [[Vector Databases]] and [[Embeddings]].
For ranking quality, use [[Search Relevance]]. For measurement, use
[[Production Search Evaluation]].
