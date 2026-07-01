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
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) and retrieve nearby
items with nearest-neighbor search. In DataTalks.Club podcast discussions, they
appear in semantic [search]({{ '/wiki/search/' | relative_url }}) and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).
They also support recommendations, multimodal retrieval, and
[LLM]({{ '/wiki/llms/' | relative_url }}) applications that need outside
knowledge.

A vector database isn't the full search product because it only stores vectors,
indexes them, and returns candidate items. The surrounding system still handles
ingestion, chunking, metadata filters, and reranking. It also handles
citations, permissions, and evaluation. That boundary appears throughout
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and matters for
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }}).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the clearest
entry point in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 17:01, she introduces Qdrant and vector databases as plug-and-play vector
search infrastructure. At 20:27, she compares adding vectors to an existing
search stack with adopting a standalone vector database.

## Storage, Embeddings, and Search

The shared definition across the podcast discussions is practical. A vector
database stores model-produced vectors and indexes them for nearest-neighbor
lookup. It returns items close to a query vector. The query vector may represent
text, an image, a user session, or a product. It may also represent another
signal from a machine learning model.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the LLM version
in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 48:01, she connects vector databases to embeddings, indexing, and semantic
search in retrieval-augmented systems. Her framing places the database between
document preparation and answer generation. It stores representations, while
the application chooses what to retrieve, how to package context, and how to
judge the final answer.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
search-engineering version in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
At 27:21, he frames vector databases as stores for embeddings plus
nearest-neighbor search. At 29:00, he separates vector compute from vector
storage. The model or ingestion pipeline creates embeddings during indexing and
at query time. The database stores those vectors and retrieves candidates.

Vector search depends on representation quality. If the embedding model does
not encode the distinction a product needs, the vector database can't repair
the retrieval result. Daniel's 21:55 discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
explains vector search through shared embedding representations. The same
episode extends that idea to multimodal retrieval and personalization, where
different signals have to live in a comparable vector space.

## Adoption Boundaries

Teams differ most on where a vector database belongs in the stack. Atita starts
from existing search systems. Her 20:27 discussion in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
asks whether teams should add vector support to a current search engine. They
could also run a standalone vector database or combine both. That makes
adoption a migration
and operations decision rather than a blanket replacement for Lucene,
Elasticsearch, or Solr.

Daniel starts from representation learning and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
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
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
and [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).

## RAG and Context Retrieval

[RAG]({{ '/wiki/rag/' | relative_url }}) is the most visible vector-database use
case in these episodes, but the guests don't reduce RAG to vector storage.
Atita's podcast-transcript example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
starts with chunking, overlap, embedding models, and vectorization at 38:24. At
42:49, she connects retrieval and augmentation to generation. She also covers
prompt design and citations.

Meryem gives the production LLM reason for retrieval. Her
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
discussion argues at 40:46 that changing knowledge is often better handled with
retrieval than with repeated fine-tuning. At 42:02, she connects that choice to
indexing documents and grounding answers. A vector database can retrieve
context, but the application still needs source selection and permissions. It
also needs citations and
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

In [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}),
retrieval fits changing facts and source-backed answers while fine-tuning fits
behavior, style, or task adaptation. Vector databases help with the retrieval
side of that decision, but they don't choose the model behavior.

## Hybrid Search and Recommendations

Production search still needs ranking, filtering, metadata, and business
constraints. Vector similarity produces candidate matches. Product search,
support search, and recommendation systems often need hybrid retrieval.
Daniel's 34:00 discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
combines vector similarity with filters and recency. At 39:53, he discusses how
constraints and business rules fit poorly if teams try to express everything as
one vector query.

Vector databases also support retrieval beyond document chunks. At 32:43 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel uses CLIP for text-to-image retrieval. At 38:11, he discusses title and
content embeddings. He also discusses image and behavioral embeddings. At
40:48, he discusses recency and time bias in vector space.

Those examples connect vector databases to
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) products
that retrieve products, images, sessions, or recommendation candidates.

Atita reaches a similar conclusion from search practice. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
her 52:07 discussion covers session-based recommendations and reranking. At
54:54, she compares session-based personalization with collaborative filtering.
Those examples place vector databases beside
[recommendation systems]({{ '/wiki/recommendation-systems/' | relative_url }}),
ranking, and search, not above them.

## Graph and Structured Retrieval

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) adds a
structured-knowledge contrast in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
At 38:10, she contrasts text chunking, embeddings, and vector databases with
knowledge graph semantics. Nearest-neighbor retrieval finds similar chunks,
while a graph can preserve explicit relationships and typed paths.

Her 33:43 and 39:56 discussions in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
show a different retrieval design. She combines LLM grounding with knowledge
graphs and Cypher-driven retrieval. That makes
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
and
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
architecture choices about evidence structure. Some systems need similar text or
images. Others need entities, paths, report structure, or domain relationships.

For the underlying graph database technology, [Graph Databases in Action]({{ '/books/20210614-graph-databases-in-action/' | relative_url }}) by Dave Bechberger and Josh Perryman covers property graph models, query patterns, and when graph storage fits a domain better than relational or vector stores.

## Evaluation and Operations

Teams need to evaluate the retrieval result and the product outcome separately.
A vector database can return nearest neighbors quickly and still fail the user
task. The embedding model can miss intent, or the index can become stale.
Filters can remove useful candidates. Reranking can bury relevant items, and
the final LLM answer can cite the wrong chunk.

Atita discusses multi-level RAG evaluation and human-in-the-loop review at
48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Daniel takes the search-metrics route in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
at 1:01:25, he connects search quality to business metrics, A/B tests, and
revenue attribution. At 1:03:50, he discusses offline evaluation and
operational metrics. Those discussions make vector database evaluation part of
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
not a standalone benchmark.

Storage and compute also change at different speeds. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel separates ingestion-time encoding from query-time encoding at 29:00. At
30:22, he covers recomputing embeddings and model versioning. Teams may need to
rebuild indexes during model swaps, chunking changes, new modalities, or
metadata changes. They also need to keep old and new vectors consistent during
the migration.
