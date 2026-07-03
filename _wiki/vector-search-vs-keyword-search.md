---
layout: article
tags: ["comparison"]
title: "Vector vs Keyword Search"
keyword: "vector search vs keyword search"
summary: "A comparison of keyword search, vector search, and hybrid retrieval for production search, RAG, ranking, filters, and evaluation."
related_wiki:
  - Search
  - Vector Databases
  - Embeddings
  - Information Retrieval
  - Production Search Evaluation
---

[[search=>Keyword search]] retrieves documents by
matching query terms against indexed text. [[vector-databases|Vector search]]
retrieves nearby [[embeddings]] in a
learned representation space. Daniel Svonava, Atita Arora, and Reem Mahmoud
don't treat one as a universal replacement for the other. They treat both as
candidate retrieval tools inside a larger
[[information retrieval]]
system. That system still needs ranking, filters, latency work, and
[[production search evaluation]].

[[person:danielsvonava=>Daniel Svonava]] gives the
clearest production anatomy. He separates candidate generation from ranking,
then moves from bag-of-words retrieval and inverted indexes to dense vector
representations [[cite:building-production-search-systems|Building Search Systems]].
The migration path from Solr and Lucene to vector databases inside existing
search systems comes from [[person:atitaarora|Atita Arora]] in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].

[[person:reemmahmoud=>Reem Mahmoud]] gives a parallel production view with
inverted indexes, embeddings, hybrid search, and filters in [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
It also covers query-time weights, vector database selection, and search
metrics.

## Core Difference

Keyword search starts with tokens. A Lucene-style inverted index maps words or
normalized terms to the documents or positions where they appear. Daniel
explains that structure, then recommends using existing engines such as Lucene
instead of hand-rolling a reverse keyword lookup [[cite:building-production-search-systems|Building Search Systems]].

Atita traces the same classical search lineage. She covers Solr, Lucene,
Elasticsearch, and OpenSearch in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
She also covers full-text search and query-content matching.

Vector search starts with representations. An embedding model can turn
documents, queries, products, and images into vectors. It can also represent
users or sessions. The retrieval step then searches for nearby vectors.

Daniel describes that shift through vector databases that store embeddings and
run nearest-neighbor search [[cite:building-production-search-systems|Building Search Systems]].
The embedding pipeline creates vectors at ingestion and query time. Reem covers
the same production split [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
Vector search is a retrieval method rather than the whole search product.

In practice, the two methods fail differently. Keyword search can miss relevant
items when the user's wording differs from the indexed wording. Vector search
can retrieve plausible semantic neighbors. It may still ignore exact terms,
permissions, freshness, or product constraints. That's why the comparison
belongs beside
[[Vector Database vs Search Engine]].

Use this page for the matching method. Use the infrastructure comparison for
the system that owns storage, indexing, filtering, and ranking.

## Keyword Strengths

Keyword search is strong when exact language matters. Product SKUs and legal
terms often need predictable matching, and so do error codes or names. Domain
vocabulary and compliance filters need the same predictability. Daniel's search
systems walkthrough shows why an inverted index is still a practical
candidate-generation tool [[cite:building-production-search-systems|Building Search Systems]].
It narrows a large corpus quickly before ranking decides what the user should
see.

Lucene and Elasticsearch-style systems also make filters and query constraints
first-class. Daniel contrasts Lucene-style `must` and `should` clauses with
vector-query approaches [[cite:building-production-search-systems|Building Search Systems]].
A strict keyword or metadata filter can enforce a business rule, while a soft
clause can keep a highly relevant older result in play. Reem covers the same
constraint problem for filters, recency, and business rules
in [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].

Keyword systems require ongoing maintenance. Daniel describes brittleness from
synonyms and query rewrites [[cite:building-production-search-systems|Building Search Systems]].
He also covers dictionaries and ties that brittleness to configuration debt.
Atita adds the search-quality view in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Teams still need user-centric metrics and relevance work after search matches
the right content to the right query.

## Vector Strengths

Vector search is strongest when users describe intent differently from the
stored text. Daniel describes embeddings as shared representations
in [[cite:building-production-search-systems|Building Search Systems]].
Queries and candidate items can land near each other even when the exact words
differ. That makes vector search useful for semantic retrieval and
cross-language queries. It also helps with synonym-heavy queries, multimodal
retrieval, and personalization.

Atita gives the RAG version through a transcript-chatbot example in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
The chatbot chunks podcast transcripts and creates embeddings. It stores
vectors, retrieves relevant chunks, and passes them into a generated answer
with citations.
In that workflow, vector search helps because the question may not share exact
words with the passage that contains the answer. The surrounding
[[Search]] and
[[Embeddings]] pages treat this as
retrieval before generation, not as a replacement for evaluation or grounding.

Vector search also extends beyond text. Daniel discusses CLIP-style
text-to-image retrieval and multiple embeddings for titles, content, images,
and behavior [[cite:building-production-search-systems|Building Search Systems]].
Reem covers multimodal embeddings, feature fusion, and ecommerce
personalization [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
Atita adds session-based recommendations and reranking
in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].

## Hybrid Retrieval

Hybrid retrieval is the recurring production answer. Daniel introduces it with
a news search result that may need semantic relevance and freshness at the same
time [[cite:building-production-search-systems|Building Search Systems]].
A hard one-month filter can remove a relevant article, while pure vector
similarity can ignore recency. The search system has to decide which signals are
mandatory, which signals are soft, and which weights should be chosen at query
time.

Reem covers the same hybrid production surface [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
The signals include vector similarity, filters, recency, and metadata. They
also include behavior, popularity, and time encoding. Normalization and
query-time weighting belong there too. That makes hybrid search a ranking and
operations problem, not just an index choice.

Atita's migration discussion keeps the architecture flexible
in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Teams can put vectors inside an existing Solr, Lucene, Elasticsearch, or
OpenSearch stack. They can also run a standalone vector database such as Qdrant
beside the existing text search stack. The right hybrid design depends on the
current system. It may already own reliable filters, lexical relevance,
production traffic, and operational tooling.

## Ranking and Filters

Both methods only produce candidates, so ranking decides which candidates
deserve the top positions. Daniel says retrieval narrows the search space.
Ranking estimates relevance and product objectives such as click or purchase
probability [[cite:building-production-search-systems|Building Search Systems]].
A vector
nearest-neighbor result can still rank poorly if it ignores freshness,
inventory, permissions, or business priorities.

Filters are easier to reason about in mature keyword search systems, but they
still create tradeoffs. Daniel's Lucene `must` and `should` examples show that
a product rule can be strict or weighted [[cite:building-production-search-systems|Building Search Systems]].

Reem adds vector-side approaches, including recency and behavior encoded into
vector features [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
They can also encode metadata or popularity.
They can also normalize components and choose weights at query time.

Those choices leave the matching method as part of
[[production search evaluation]].
Evaluate exact-match queries separately from semantic queries. Evaluate
permissioned content, stale content, long-tail queries, and high-value product
segments separately too. A single aggregate relevance metric can hide whether
keyword retrieval, vector retrieval, filtering, or reranking caused the
failure.

## Vector Databases and Search Engines

A vector database stores embeddings and retrieves neighbors. A search engine
usually owns more of the retrieval product. It handles text analysis, inverted
indexes, fields, and filters. It also handles ranking features, query logic,
and serving behavior.

Daniel separates those concerns: vector storage and vector compute are
separate, and model changes can force recomputing embeddings or rebuilding
indexes [[cite:building-production-search-systems|Building Search Systems]].

Atita describes the same system boundary from the search migration side in
the Modern Search Systems episode [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
She introduces Qdrant-style vector search. Then she compares a standalone
vector database with vector support inside Solr, Elasticsearch, OpenSearch, or
other Lucene-based systems. Her point is practical: teams should investigate whether
vectors fit the use case before changing the existing search stack.

For infrastructure decisions, use
[[Vector Database vs Search Engine]]
with this page. Use this comparison to choose between lexical, semantic, and
hybrid matching. Use the infrastructure comparison to decide where vectors
should live and how they'll be indexed. The same infrastructure choice covers
filter placement, ranking ownership, and production reliability.

## Evaluation Tradeoffs

Use exact-match coverage and synonym behavior to evaluate keyword search. Add
field weighting, filters, latency, and ranking quality.
Daniel's keyword-brittleness discussion warns against judging lexical search
only by obvious-term lookup [[cite:building-production-search-systems|Building Search Systems]].
Query rewrites and synonym rules can help, but they can also create
configuration debt and unexpected matches.

Evaluate vector search by checking whether nearest neighbors contain the
evidence, products, images, or chunks the task needs. Atita's RAG evaluation
section separates embedding choice, chunking strategy, and retrieval count in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
She also separates generated answer quality, citations, offline tests, and
human review.
A vector database can return similar chunks while the answer remains unsupported
or incomplete.

Evaluate hybrid search through both offline relevance tests and product
metrics. Daniel ties search changes to A/B tests, business KPIs, offline
evaluation, and engineer-facing operational metrics
in [[cite:building-production-search-systems|Building Search Systems]].
Reem covers the same production lens [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
The question isn't whether vector search or keyword search is newer. Teams need
to ask which retrieval and ranking design produces relevant, explainable,
measurable results for the product.

## Choosing Retrieval

Choose keyword search when exact terms and filters dominate the task. Metadata
fields, auditability, and predictable behavior support the same choice.
Together, those needs fit Atita's Lucene and Solr discussion
in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
They also fit Daniel's inverted-index candidate generation
in [[cite:building-production-search-systems|Building Search Systems]].

Choose vector search when semantic recall or paraphrases are the main problem.
Multimodal matching and session similarity support the same choice. RAG context
retrieval does too.

Daniel's vector-search sections support that choice
in [[cite:building-production-search-systems|Building Search Systems]].
So does Atita's transcript-chatbot pipeline
in [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Reem's discussion of embeddings and multimodal retrieval also supports that
choice [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].

Choose hybrid retrieval when the product needs both. Daniel's freshness example
and Reem's hybrid-search discussion both put semantic similarity beside lexical
matching [[cite:building-production-search-systems|Building Search Systems]], [[cite:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
They also keep metadata filters and recency in the same decision. Permissions,
popularity, ranking, and business metrics stay there too.

For a broader retrieval map, continue with
[[Search]] and
[[Information Retrieval]].
For representation and storage, use
[[Vector Databases]] and
[[Embeddings]]. For measurement, use
[[Production Search Evaluation]].
