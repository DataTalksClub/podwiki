---
layout: article
title: "Vector Search vs Keyword Search"
keyword: "vector search vs keyword search"
summary: "A comparison of keyword search, vector search, and hybrid retrieval for production search, RAG, ranking, filters, and evaluation."
related_wiki:
  - Search
  - Vector Databases
  - Embeddings
  - Information Retrieval
  - Production Search Evaluation
---

[Keyword search]({{ '/wiki/search/' | relative_url }}) retrieves documents by
matching query terms against indexed text. [Vector search]({{ '/wiki/vector-databases/' | relative_url }})
retrieves nearby [embeddings]({{ '/wiki/embeddings/' | relative_url }}) in a
learned representation space. Daniel Svonava, Atita Arora, and Reem Mahmoud
don't treat one as a universal replacement for the other. They treat both as
candidate retrieval tools inside a larger
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
system. That system still needs ranking, filters, latency work, and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
clearest production anatomy in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
at 12:45 he separates candidate generation from ranking. At 11:29-21:55 he
moves from bag-of-words retrieval and inverted indexes to dense vector
representations. [Atita Arora]({{ '/people/atitaarora/' | relative_url }})
frames the migration path in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
starting with Solr and Lucene at 4:42. She moves to vector databases at 17:01
and vectors inside existing search systems at 20:27.

[Reem Mahmoud]({{ '/people/reemmahmoud/' | relative_url }}) gives a parallel
production view in
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
with inverted indexes, embeddings, hybrid search, and
filters. It also covers query-time weights, vector database selection, and
search metrics.

## Core Difference

Keyword search starts with tokens. A Lucene-style inverted index maps words or
normalized terms to the documents or positions where they appear. Daniel
explains that structure at 12:45-20:02 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
then recommends using existing engines such as Lucene instead of hand-rolling a
reverse keyword lookup.

The same classical search lineage appears in Atita's
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
discussion at 4:42-20:27. She covers Solr, Lucene, Elasticsearch, and
OpenSearch. She also covers full-text search and query-content matching.

Vector search starts with representations. An embedding model can turn
documents, queries, products, and images into vectors. It can also represent
users or sessions. The retrieval step then searches for nearby vectors.

Daniel describes that shift at 21:55-33:13
in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
where vector databases store embeddings and run nearest-neighbor search. The
embedding pipeline creates vectors at ingestion and query time. Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
page covers the same production split around 21:55 and 29:00. Vector search is
a retrieval method rather than the whole search product.

In practice, the two methods fail differently. Keyword search can miss relevant
items when the user's wording differs from the indexed wording. Vector search
can retrieve plausible semantic neighbors. It may still ignore exact terms,
permissions, freshness, or product constraints. That's why the comparison
belongs beside
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }}).

Use this page for the matching method. Use the infrastructure comparison for
the system that owns storage, indexing, filtering, and ranking.

## Keyword Strengths

Keyword search is strong when exact language matters. Product SKUs and legal
terms often need predictable matching, and so do error codes or names. Domain
vocabulary and compliance filters need the same predictability. Daniel's
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
walkthrough at 12:45-17:40 shows why an inverted index is still a practical
candidate-generation tool. It narrows a large corpus quickly before ranking
decides what the user should see.

Lucene and Elasticsearch-style systems also make filters and query constraints
first-class. In the 39:53 section of
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel contrasts Lucene-style `must` and `should` clauses with vector-query
approaches. A strict keyword or metadata filter can enforce a business rule,
while a soft clause can keep a highly relevant older result in play. Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion covers the same constraint problem around 39:53, including filters,
recency, and business rules.

Keyword systems require ongoing maintenance. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel describes brittleness from synonyms, query rewrites, and dictionaries
around 20:02. He also ties that brittleness to configuration debt.
Atita's 9:18 section in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
adds the search-quality view. Teams still need user-centric metrics and
relevance work after search matches the right content to the right query.

## Vector Strengths

Vector search is strongest when users describe intent differently from the
stored text. Daniel describes embeddings as shared representations around
21:55 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Queries and candidate items can land near each other even when the exact words
differ. That makes vector search useful for semantic retrieval and
cross-language queries. It also helps with synonym-heavy queries, multimodal
retrieval, and personalization.

Atita gives the RAG version in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Her transcript chatbot example at 35:49-42:49 chunks podcast transcripts and
creates embeddings. It stores vectors, retrieves relevant chunks, and passes
them into a generated answer with citations. In that workflow, vector search helps
because the question may not share exact words with the passage that contains
the answer. The surrounding
[Search]({{ '/wiki/search/' | relative_url }}) and
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}) pages treat this as
retrieval before generation, not as a replacement for evaluation or grounding.

Vector search also extends beyond text. Daniel discusses CLIP-style
text-to-image retrieval and multiple embeddings for titles, content, images,
and behavior at 32:43-38:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
episode covers multimodal embeddings, feature fusion, and ecommerce
personalization around 33:13-38:50 and 58:17. Atita adds session-based
recommendations and reranking around 52:07 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).

## Hybrid Retrieval

Hybrid retrieval is the recurring production answer. Daniel introduces it
around 34:00 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
a news search result may need semantic relevance and freshness at the same
time. A hard one-month filter can remove a relevant article, while pure
vector similarity can ignore recency. The search system has to decide which
signals are mandatory, which signals are soft, and which weights should be
chosen at query time.

Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion covers the same hybrid production surface at 34:00-45:11. The
signals include vector similarity, filters, recency, and metadata. They also
include behavior, popularity, and time encoding. Normalization and query-time
weighting belong there too. That makes hybrid search a
ranking and operations problem, not just an index choice.

Atita's migration discussion at 20:27 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
keeps the architecture flexible. Teams can put vectors inside an existing Solr,
Lucene, Elasticsearch, or OpenSearch stack. They can also run a standalone
vector database such as Qdrant beside the existing text search stack. The right
hybrid design depends on the current system. It may already own reliable
filters, lexical relevance, production traffic, and operational tooling.

## Ranking and Filters

Both methods only produce candidates, and ranking decides which candidates
deserve the top positions. Daniel makes that split explicit at 12:45 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Daniel says retrieval narrows the search space. Ranking then estimates
relevance, click probability, purchase probability, or another product
objective. A vector
nearest-neighbor result can still rank poorly if it ignores freshness,
inventory, permissions, or business priorities.

Filters are easier to reason about in mature keyword search systems, but they
still create tradeoffs. Daniel's Lucene `must` and `should` examples at
39:53-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
show that a product rule can be strict or weighted. Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion adds vector-side approaches. Teams can encode recency, behavior,
metadata, or popularity into vector features. They can also normalize
components and choose weights at query time.

Those choices leave the matching method as part of
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
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

In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel separates those concerns at 27:21-33:13. Vector storage and vector
compute are separate. Model changes can force recomputing embeddings or
rebuilding indexes.

Atita describes the same system boundary from the search migration side in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 17:01 she introduces Qdrant-style vector search. At 20:27 she compares a
standalone vector database with vector support inside Solr, Elasticsearch,
OpenSearch, or other Lucene-based systems. Her point is practical: teams should
investigate whether vectors fit the use case before changing the existing
search stack.

For infrastructure decisions, use
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
with this page. Use this comparison to choose between lexical, semantic, and
hybrid matching. Use the infrastructure comparison to decide where vectors
should live and how they'll be indexed. The same infrastructure choice covers
filter placement, ranking ownership, and production reliability.

## Evaluation Tradeoffs

Use exact-match coverage and synonym behavior to evaluate keyword search. Add
field weighting, filters, latency, and ranking quality.
Daniel's 20:02 keyword-brittleness discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
warns against judging lexical search only by obvious-term lookup. Query
rewrites and synonym rules can help, but
they can also create configuration debt and unexpected matches.

Evaluate vector search by checking whether nearest neighbors contain the
evidence, products, images, or chunks the task needs. Atita's RAG evaluation
section at 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
separates embedding choice, chunking strategy, and retrieval count. She also
separates generated answer quality, citations, offline tests, and human review.
A vector database
can return similar chunks while the answer remains unsupported or incomplete.

Evaluate hybrid search through both offline relevance tests and product
metrics. Daniel's business-metric discussion at 1:01:25-1:03:50 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
ties search changes to A/B tests, business KPIs, offline evaluation, and
engineer-facing operational metrics. Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
episode covers the same production lens around 1:01:25-1:03:50. The question
isn't whether vector search or keyword search is newer. Teams need to ask which
retrieval and ranking design produces relevant, explainable, measurable results
for the product.

## Choosing Retrieval

Choose keyword search when exact terms and filters dominate the task. Metadata
fields, auditability, and predictable behavior support the same choice.
Together, those needs fit Atita's Lucene and Solr discussion at 4:42-9:18 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
They also fit Daniel's inverted-index candidate generation at 12:45-17:40 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).

Choose vector search when semantic recall or paraphrases are the main problem.
Multimodal matching and session similarity support the same choice. RAG context
retrieval does too.

Daniel's 21:55-33:13 vector-search sections in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
support that choice. So does Atita's 35:49-48:09 transcript-chatbot pipeline in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Reem's
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion of embeddings and multimodal retrieval also supports that choice.

Choose hybrid retrieval when the product needs both. Daniel's freshness example
at 34:00 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
and Reem's 34:00-45:11
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion both put semantic similarity beside lexical matching. They also keep
metadata filters and recency in the same decision. Permissions, popularity,
ranking, and business metrics stay there too.

For a broader retrieval map, continue with
[Search]({{ '/wiki/search/' | relative_url }}) and
[Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
For representation and storage, use
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) and
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}). For measurement, use
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
