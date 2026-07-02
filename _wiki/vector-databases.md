---
layout: wiki
title: "Vector Databases"
summary: "How DataTalks.Club podcast guests discuss vector databases as retrieval infrastructure for semantic search, RAG, recommendations, and multimodal matching."
related:
  - Search, RAG, and Knowledge Systems
  - Embeddings
  - Search
  - Retrieval-Augmented Generation
  - LLMs
---

Vector databases store
[[embeddings]] and retrieve nearby
items with nearest-neighbor search. In DataTalks.Club podcast discussions, they
appear in semantic [[search]] and
[[retrieval-augmented-generation|retrieval-augmented generation]].
They also support recommendations, multimodal retrieval, and
[[llms|LLM]] applications that need outside
knowledge.

A vector database isn't the full search product because it only stores vectors,
indexes them, and returns candidate items. The surrounding system still handles
ingestion, chunking, metadata filters, and reranking. It also handles
citations, permissions, and evaluation. That boundary appears throughout
[[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]]
and matters for
[[Vector Database vs Search Engine]].

[[person:atitaarora|Atita Arora]] gives the clearest
entry point in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 17:01, she introduces Qdrant and vector databases as plug-and-play vector
search infrastructure. At 20:27, she compares adding vectors to an existing
search stack with adopting a standalone vector database.

## Storage, Embeddings, and Search

The shared definition across the podcast discussions is practical. A vector
database stores model-produced vectors and indexes them for nearest-neighbor
lookup. It returns items close to a query vector. The query vector may represent
text, an image, a user session, or a product. It may also represent another
signal from a machine learning model.

[[person:meryemarik|Meryem Arik]] gives the LLM version
in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 48:01, she connects vector databases to embeddings, indexing, and semantic
search in retrieval-augmented systems. Her framing places the database between
document preparation and answer generation. It stores representations, while
the application chooses what to retrieve, how to package context, and how to
judge the final answer.

[[person:danielsvonava|Daniel Svonava]] gives the
search-engineering version in
[[podcast:building-production-search-systems|Building Search Systems]].
At 27:21, he frames vector databases as stores for embeddings plus
nearest-neighbor search. At 29:00, he separates vector compute from vector
storage. The model or ingestion pipeline creates embeddings during indexing and
at query time. The database stores those vectors and retrieves candidates.

Vector search depends on representation quality. If the embedding model does
not encode the distinction a product needs, the vector database can't repair
the retrieval result. Daniel's 21:55 discussion in
[[podcast:building-production-search-systems|Building Search Systems]]
explains vector search through shared embedding representations. The same
episode extends that idea to multimodal retrieval and personalization, where
different signals have to live in a comparable vector space.

## Adoption Boundaries

Teams differ most on where a vector database belongs in the stack. Atita starts
from existing search systems. Her 20:27 discussion in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]
asks whether teams should add vector support to a current search engine. They
could also run a standalone vector database or combine both. That makes
adoption a migration
and operations decision rather than a blanket replacement for Lucene,
Elasticsearch, or Solr.

Daniel starts from representation learning and
[[production search evaluation]].
In
[[podcast:building-production-search-systems|Building Search Systems]],
his 34:00 discussion puts vectors next to filters, recency, and business
constraints. His 52:35 discussion covers vendor selection. At 54:56, he
compares Lucene and Elasticsearch with specialized vector databases. This view
treats vector databases as one component in a ranking system, not as the
ranking system.

The useful architecture question is which part of the retrieval system needs a
specialized vector index. Existing search engines can reduce operational sprawl
when they already serve production traffic. A dedicated vector database can
make vector search easier to prototype, scale, or isolate from a legacy search
stack. That tradeoff belongs with
[[Vector Database vs Search Engine]]
and [[Information Retrieval]].

## RAG and Context Retrieval

[[retrieval-augmented-generation|RAG]] is the most visible vector-database use
case in these episodes, but the guests don't reduce RAG to vector storage.
Atita's podcast-transcript example in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]
starts with chunking, overlap, embedding models, and vectorization at 38:24. At
42:49, she connects retrieval and augmentation to generation. She also covers
prompt design and citations.

Meryem gives the production LLM reason for retrieval. Her
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
discussion argues at 40:46 that changing knowledge is often better handled with
retrieval than with repeated fine-tuning. At 42:02, she connects that choice to
indexing documents and grounding answers. A vector database can retrieve
context, but the application still needs source selection and permissions. It
also needs citations and
[[LLM evaluation workflows]].

In [[rag-vs-fine-tuning|RAG vs Fine-Tuning]],
retrieval fits changing facts and source-backed answers while fine-tuning fits
behavior, style, or task adaptation. Vector databases help with the retrieval
side of that decision, but they don't choose the model behavior.

## Hybrid Search and Recommendations

Production search still needs ranking, filtering, metadata, and business
constraints. Vector similarity produces candidate matches. Product search,
support search, and recommendation systems often need hybrid retrieval.
Daniel's 34:00 discussion in
[[podcast:building-production-search-systems|Building Search Systems]]
combines vector similarity with filters and recency. At 39:53, he discusses how
constraints and business rules fit poorly if teams try to express everything as
one vector query.

Vector databases also support retrieval beyond document chunks. At 32:43 in
[[podcast:building-production-search-systems|Building Search Systems]],
Daniel uses CLIP for text-to-image retrieval. At 38:11, he discusses title and
content embeddings. He also discusses image and behavioral embeddings. At
40:48, he discusses recency and time bias in vector space.

Those examples connect vector databases to
[[machine learning]] products
that retrieve products, images, sessions, or recommendation candidates.

Atita reaches a similar conclusion from search practice. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
her 52:07 discussion covers session-based recommendations and reranking. At
54:54, she compares session-based personalization with collaborative filtering.
Those examples place vector databases beside
[[recommendation systems]],
ranking, and search, not above them.

## Graph and Structured Retrieval

[[person:anahitapakiman|Anahita Pakiman]] adds a
structured-knowledge contrast in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]].
At 38:10, she contrasts text chunking, embeddings, and vector databases with
knowledge graph semantics. Nearest-neighbor retrieval finds similar chunks,
while a graph can preserve explicit relationships and typed paths.

Her 33:43 and 39:56 discussions in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]
show a different retrieval design. She combines LLM grounding with knowledge
graphs and Cypher-driven retrieval. That makes
[[Graph RAG vs Vector RAG]]
and
[[Knowledge Graph vs Vector Search]]
architecture choices about evidence structure. Some systems need similar text or
images. Others need entities, paths, report structure, or domain relationships.

For the underlying graph database technology, [[book:20210614-graph-databases-in-action|Graph Databases in Action]] by Dave Bechberger and Josh Perryman covers property graph models, query patterns, and when graph storage fits a domain better than relational or vector stores.

## Evaluation and Operations

Teams need to evaluate the retrieval result and the product outcome separately.
A vector database can return nearest neighbors quickly and still fail the user
task. The embedding model can miss intent, or the index can become stale.
Filters can remove useful candidates. Reranking can bury relevant items, and
the final LLM answer can cite the wrong chunk.

Atita discusses multi-level RAG evaluation and human-in-the-loop review at
48:09 in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Daniel takes the search-metrics route in
[[podcast:building-production-search-systems|Building Search Systems]]:
at 1:01:25, he connects search quality to business metrics, A/B tests, and
revenue attribution. At 1:03:50, he discusses offline evaluation and
operational metrics. Those discussions make vector database evaluation part of
[[production search evaluation]],
not a standalone benchmark.

Storage and compute also change at different speeds. In
[[podcast:building-production-search-systems|Building Search Systems]],
Daniel separates ingestion-time encoding from query-time encoding at 29:00. At
30:22, he covers recomputing embeddings and model versioning. Teams may need to
rebuild indexes during model swaps, chunking changes, new modalities, or
metadata changes. They also need to keep old and new vectors consistent during
the migration.
