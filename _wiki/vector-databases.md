---
layout: wiki
title: "Vector Databases"
summary: "Vector databases as retrieval infrastructure for semantic search, RAG, recommendations, and multimodal matching."
related:
  - Embeddings
  - Search
  - Retrieval-Augmented Generation
  - Vector Database vs Search Engine
  - Vector Search vs Keyword Search
  - Knowledge Graph vs Vector Search
  - Graph RAG vs Vector RAG
  - Production Search Evaluation
  - LLMs
---

Vector databases store and index [[embeddings]] so systems can retrieve nearby
items with nearest-neighbor search. Guests use them as the storage and indexing
layer behind semantic [[search]], recommendations, multimodal lookup, and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
[[llms=>LLM]] applications that need outside knowledge use the same storage
layer [[cite:building-production-search-systems=>Building Search Systems]].

Vector database work centers on storage, indexing, embedding lifecycle, and
vector retrieval operations. Matching methods belong with [[Vector Search vs
Keyword Search]]. Service boundaries belong with [[Vector Database vs Search
Engine]]. [[Knowledge Graph vs Vector Search]] covers structured relationship
retrieval.

A vector database can retrieve candidates, but the surrounding product handles
chunking and filters. The product also handles reranking, source constraints,
citations, and evaluation.

[[person:atitaarora=>Atita Arora]] gives the clearest
entry point: she introduces Qdrant and vector databases as plug-and-play vector
search infrastructure. She then compares adding vectors to an existing search
stack with adopting a standalone vector database [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

## Storage, Embeddings, and Search

A vector database stores model-produced vectors and indexes them for
nearest-neighbor lookup. It returns items close to a query vector. The query
vector may represent text, an image, a user session, or a product. It may also
represent another signal from a machine learning model.

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

## Placement in the Stack

Teams usually add a vector database to an existing retrieval stack rather than
replace every search component with one service. The storage layer belongs in
the stack, while [[Vector Database vs Search Engine]] covers the service-boundary
decision.

Atita starts from existing search systems. She compares adding vector support to
a current search engine with running a standalone vector database. She also
covers combining both
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
That puts vector databases beside Lucene, Elasticsearch, and Solr. OpenSearch
and Postgres can be part of the same placement choice.

Qdrant appears as the focused standalone option in that comparison. It can sit
beside the existing text-search stack and receive vector data from the same
ingestion path. Solr, Elasticsearch, OpenSearch, and Postgres also support
vectors
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Vectors in Existing Search]].

Daniel starts from representation learning and [[production search evaluation]].
He puts vectors next to filters, recency, and business constraints, then
compares Lucene and Elasticsearch with specialized vector databases
[[cite:building-production-search-systems=>Building Search Systems]]. That
framing treats the vector database as the similarity index inside a larger
ranking system.

Vector databases own the vector index. When teams need to decide whether
vectors should live inside the search engine or in a separate service, use
[[Vector Database vs Search Engine]].

## RAG Storage Role

[[retrieval-augmented-generation=>RAG]] is the most visible vector-database use
case in these episodes, but the guests don't reduce RAG to vector storage.
Atita's podcast-transcript example puts the vector database after chunking,
overlap, embedding models, and vectorization
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript RAG Chunking]].
She also covers prompt design, citations, and RAG evaluation
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>RAG Evaluation]].

Meryem gives the production LLM reason for retrieval. She argues that retrieval
often handles changing knowledge better than repeated fine-tuning. She then
connects that choice to indexing documents and grounding answers.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

A vector database stores and retrieves the embedded candidates, but the
application still chooses sources and applies metadata filters. It also reranks
results, writes citations, and evaluates the answer with
[[LLM evaluation workflows]].

In [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]],
retrieval fits changing facts and source-backed answers while fine-tuning fits
behavior, style, or task adaptation. Vector databases help with the retrieval
side of that decision. [[Graph RAG vs Vector RAG]] covers the later question of
which retrieved units enter the LLM prompt.

## Candidate Retrieval for Products and Recommendations

Production systems use vector databases as candidate generators, not as the
whole relevance stack. Daniel combines vector similarity with filters and
recency. He then discusses why constraints and business rules don't fit well
when teams try to express everything as one vector query
[[cite:building-production-search-systems=>Building Search Systems]].

Vector databases also support retrieval beyond document chunks. Daniel uses
CLIP for text-to-image retrieval, title and content embeddings, image and
behavioral embeddings, and recency or time bias in vector space [[cite:building-production-search-systems=>Building Search Systems]].

Those examples connect vector databases to
[[machine learning]] products
that retrieve products, images, sessions, or recommendation candidates. They
also connect vector infrastructure to
[[machine-learning-personalization=>machine learning personalization]], where
retrieval is only the candidate step before ranking and product constraints.

Atita reaches a similar conclusion from search practice. Her session-based
recommendation example includes reranking and a comparison with collaborative
filtering
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
That makes the vector database a candidate generator or similarity layer. The
product still needs a ranking rule that decides what to show in the current
session.

Session vectors can capture what the person is doing now, while collaborative
filtering depends more on accumulated user-item history. Reranking then decides
which of the retrieved items should actually surface in the product
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@54:54=>Session Recommendations]].

Those examples place vector databases beside [[recommendation systems]],
ranking, and search, not above them. Follow the vector store through candidate
retrieval here. [[search-relevance=>Search Relevance]] covers ranking
objectives.

## Relationship Retrieval Boundary

[[person:anahitapakiman=>Anahita Pakiman]] adds a structured-knowledge
contrast by comparing text chunking, embeddings, and vector databases with
knowledge graph semantics [[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]].
Nearest-neighbor retrieval finds similar chunks, while a graph can preserve
explicit relationships and typed paths.

Her episode shows a different retrieval substrate. Knowledge graphs and
Cypher-driven retrieval can return structured relationships instead of only
nearby vectors.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]].
[[Knowledge Graph vs Vector Search]] covers that representation and query
comparison. Vector database work stays focused on storage, indexing, and
nearest-neighbor retrieval.

For the underlying graph database technology, Dave Bechberger and Josh
Perryman's [[book:20210614-graph-databases-in-action=>graph database book]]
covers property graph models and query patterns. It also covers when graph
storage fits a domain better than relational or vector stores.
That graph-storage question belongs with [[Knowledge Graph vs Vector Search]]
and [[Graph Data Science]], not with vector database operations.

## Operations

A vector database can return nearest neighbors quickly and still fail the user
task. The embedding model can miss intent, the index can become stale, filters
can remove useful candidates, and reranking can bury relevant items.
[[production-search-evaluation=>Production Search Evaluation]] covers those
retrieval, ranking, and product-outcome checks
[[cite:building-production-search-systems=>Building Search Systems]].

Storage and compute also change at different speeds. Daniel separates
ingestion-time encoding from query-time encoding and covers recomputing
embeddings and model versioning
[[cite:building-production-search-systems=>Building Search Systems]].
Teams may need to rebuild indexes during model swaps, chunking changes, new
modalities, or metadata changes. During those migrations, old and new vectors
need compatible retrieval behavior.
