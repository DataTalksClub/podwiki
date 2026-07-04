---
layout: wiki
title: "Vector Databases"
summary: "How DataTalks.Club podcast guests discuss vector databases as retrieval infrastructure for semantic search, RAG, recommendations, and multimodal matching."
related:
  - Embeddings
  - Search
  - Retrieval-Augmented Generation
  - LLMs
---

Vector databases store
[[embeddings]] and retrieve nearby
items with nearest-neighbor search. In DataTalks.Club podcast discussions, they
appear in semantic [[search]] and
[[retrieval-augmented-generation=>retrieval-augmented generation]].
They also support recommendations, multimodal retrieval, and
[[llms=>LLM]] applications that need outside
knowledge.

A vector database is storage and nearest-neighbor retrieval infrastructure, not
the full search product. It stores vectors, indexes them, and returns candidate
items. The surrounding system still handles ingestion, chunking, metadata
filters, and reranking. It also handles citations, permissions, and evaluation.

For lexical-versus-semantic retrieval methods, use
[[Vector Search vs Keyword Search]]
and for infrastructure ownership use
[[Vector Database vs Search Engine]]
instead. That boundary appears throughout
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
and [[Production Search Evaluation]].

[[person:atitaarora=>Atita Arora]] gives the clearest
entry point: she introduces Qdrant and vector databases as plug-and-play vector
search infrastructure. She then compares adding vectors to an existing search
stack with adopting a standalone vector database [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

## Storage, Embeddings, and Search

The shared definition across the podcast discussions is practical. A vector
database stores model-produced vectors and indexes them for nearest-neighbor
lookup. It returns items close to a query vector. The query vector may represent
text, an image, a user session, or a product. It may also represent another
signal from a machine learning model.

[[person:meryemarik=>Meryem Arik]] gives the LLM version by connecting vector
databases to embeddings and indexing. She also ties them to semantic search in
retrieval-augmented systems [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Her framing places the database between document preparation and answer
generation. It stores representations, while the application chooses what to
retrieve, how to package context, and how to judge the final answer.

[[person:danielsvonava=>Daniel Svonava]] gives the search-engineering version:
vector databases store embeddings and provide nearest-neighbor search. The
model or ingestion pipeline creates embeddings during indexing and at query time [[cite:building-production-search-systems=>Building Search Systems]].
The database stores those vectors and retrieves candidates.

Vector search depends on representation quality. If the embedding model does
not encode the distinction a product needs, the vector database can't repair
the retrieval result. Daniel explains vector search through shared embedding
representations. He then extends that idea to multimodal retrieval and
personalization, where different signals have to live in a comparable vector space [[cite:building-production-search-systems=>Building Search Systems]].

## Approximate Nearest-Neighbor Indexes

Vector databases need specialized indexes because exact nearest-neighbor search
becomes expensive. Each query would compare one vector with many
high-dimensional items. Classic tree structures don't remove that problem
automatically.

Binary search trees fit one-dimensional ordering. KD-trees work only up to a
certain dimensionality and handle dynamic sets poorly
[[cite:algorithms-data-structures-for-engineers@39:10=>Nearest-Neighbor Data Structures]].

Approximate nearest-neighbor search accepts a close result when the product can
tolerate it. Examples include choosing between two warehouses with nearly the
same distance. They also include recommending items that are close enough to a
user vector
[[cite:algorithms-data-structures-for-engineers@42:44=>Approximate Nearest Neighbor]].

R-trees and SS-trees extend the search-tree idea to spatial and similarity
search. The index narrows the candidate set before distance comparisons finish
the retrieval. That's the data-structure reason vector databases are more than
simple vector storage. They combine [[embeddings]], distance metrics, and
approximate indexing. That combination lets [[Information Retrieval]] systems
search millions of items without brute-force scans on every request
[[cite:algorithms-data-structures-for-engineers@42:44=>Approximate Nearest Neighbor]].

## Adoption Boundaries

Teams differ most on where a vector database belongs in the stack. Atita starts
from existing search systems. She asks whether teams should add vector support
to a current search engine, run a standalone vector database, or combine both [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
That makes adoption a migration and operations decision rather than a blanket
replacement for Lucene, Elasticsearch, or Solr.

Daniel starts from representation learning and
[[production search evaluation]].
He puts vectors next to filters, recency, and business constraints, then
compares Lucene and Elasticsearch with specialized vector databases. That
comparison belongs to vendor selection [[cite:building-production-search-systems=>Building Search Systems]].
This view treats vector databases as one component in a ranking system, not as
the ranking system.

The useful architecture question is which part of the retrieval system needs a
specialized vector index. Existing search engines can reduce operational sprawl
when they already serve production traffic. A dedicated vector database can
make vector search easier to prototype, scale, or isolate from a legacy search
stack. That tradeoff belongs with
[[Vector Database vs Search Engine]]
and [[Information Retrieval]].

## RAG and Context Retrieval

[[retrieval-augmented-generation=>RAG]] is the most visible vector-database use
case in these episodes, but the guests don't reduce RAG to vector storage.
Atita's podcast-transcript example starts with chunking, overlap, embedding
models, and vectorization before connecting retrieval and augmentation to
generation. She also covers prompt design and citations [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Meryem gives the production LLM reason for retrieval. She argues that changing
knowledge is often better handled with retrieval than with repeated
fine-tuning. She then connects that choice to indexing documents and grounding
answers [[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
A vector database can retrieve context, but the application still needs source
selection and permissions. It also needs citations and
[[LLM evaluation workflows]].

In [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]],
retrieval fits changing facts and source-backed answers while fine-tuning fits
behavior, style, or task adaptation. Vector databases help with the retrieval
side of that decision, but they don't choose the model behavior.

## Hybrid Search and Recommendations

Production search still needs ranking, filtering, metadata, and business
constraints. Vector similarity produces candidate matches. Product search,
support search, and recommendation systems often need hybrid retrieval.
Daniel combines vector similarity with filters and recency. He then discusses
how constraints and business rules fit poorly if teams try to express
everything as one vector query [[cite:building-production-search-systems=>Building Search Systems]].

Vector databases also support retrieval beyond document chunks. Daniel uses
CLIP for text-to-image retrieval, title and content embeddings, image and
behavioral embeddings, and recency or time bias in vector space [[cite:building-production-search-systems=>Building Search Systems]].

Those examples connect vector databases to
[[machine learning]] products
that retrieve products, images, sessions, or recommendation candidates.

Atita reaches a similar conclusion from search practice. Her session-based
recommendation example includes reranking and a comparison with collaborative
filtering
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
That makes the vector database a candidate generator or similarity layer. The
product still needs a ranking rule that decides what to show in the current
session.
Those examples place vector databases beside
[[recommendation systems]],
ranking, and search, not above them.

## Graph and Structured Retrieval

[[person:anahitapakiman=>Anahita Pakiman]] adds a structured-knowledge
contrast by comparing text chunking, embeddings, and vector databases with
knowledge graph semantics [[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]].
Nearest-neighbor retrieval finds similar chunks, while a graph can preserve
explicit relationships and typed paths.

Her episode shows a different retrieval design: she combines LLM grounding with
knowledge graphs and Cypher-driven retrieval [[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]].
That makes
[[Graph RAG vs Vector RAG]]
and
[[Knowledge Graph vs Vector Search]]
architecture choices about evidence structure. Some systems need similar text or
images. Others need entities, paths, report structure, or domain relationships.

For the underlying graph database technology, Dave Bechberger and Josh
Perryman's [[book:20210614-graph-databases-in-action=>graph database book]]
covers property graph models and query patterns. It also covers when graph
storage fits a domain better than relational or vector stores.

## Evaluation and Operations

Teams need to evaluate the retrieval result and the product outcome separately.
A vector database can return nearest neighbors quickly and still fail the user
task. The embedding model can miss intent, or the index can become stale.
Filters can remove useful candidates. Reranking can bury relevant items, and
the final LLM answer can cite the wrong chunk.

Atita discusses multi-level RAG evaluation and human-in-the-loop review [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
Daniel takes the search-metrics route. He connects search quality to business
metrics, A/B tests, and revenue attribution. He also discusses offline
evaluation and operational metrics [[cite:building-production-search-systems=>Building Search Systems]].
Those discussions make vector database evaluation part of
[[production search evaluation]],
not a standalone benchmark.

Storage and compute also change at different speeds. Daniel separates
ingestion-time encoding from query-time encoding and covers recomputing
embeddings and model versioning [[cite:building-production-search-systems=>Building Search Systems]].
Teams may need to rebuild indexes during model swaps, chunking changes, new
modalities, or metadata changes. They also need to keep old and new vectors
consistent during the migration.
