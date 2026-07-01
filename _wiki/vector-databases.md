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

Vector databases store and search embeddings with nearest-neighbor methods.
DataTalks.Club guests use them for semantic search,
[RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
recommendations, and multimodal retrieval.

A vector database isn't the full search product. It's the storage and retrieval
layer that returns candidates for the rest of the system to filter, rerank,
cite, and evaluate.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the clearest
entry point in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 17:01 she introduces Qdrant and vector databases as plug-and-play vector
search infrastructure. At 20:27 she compares adding vectors to an existing
search stack with adopting a standalone vector database.

## Common Definition

DataTalks.Club guests define vector databases practically. A vector database stores
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), indexes them for
nearest-neighbor lookup, and returns items whose vectors are close to the query
vector. The query vector may represent text, an image, a user session, or some
other model-produced signal.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) explains the LLM
version in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 48:01 she connects vector databases to embeddings, indexing, and semantic
search in retrieval-augmented systems. That definition places the database
between document preparation and answer generation. It stores representations,
but the application still decides what to retrieve, how to package context, and
how to judge the final answer.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
search-engineering version in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
At 27:21 he frames vector databases as stores for embeddings plus
nearest-neighbor search. At 29:00 he separates vector compute from vector
storage. The model or pipeline creates embeddings during ingestion and at query
time. The database stores those vectors and retrieves candidates.

## Guest Differences

Guests mostly differ on where a vector database belongs in the stack. Atita
starts from existing
[search]({{ '/wiki/search/' | relative_url }}) systems. Her 20:27 discussion in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
asks whether teams should add vector support to a current search engine. Teams
can also run a standalone vector database or combine both.

That view treats adoption as a migration and operations question.

Daniel starts from representation learning and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
his 34:00 discussion puts vectors next to filters, recency, and business
constraints. His 52:35 discussion covers vendor selection. His 54:56 discussion
compares Lucene and Elasticsearch with specialized vector databases. This view
treats vector databases as one component in a ranking system, not as the ranking
system.

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) adds a
structured-knowledge contrast in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
At 38:10 she contrasts text chunking, embeddings, vector databases, and
knowledge graph semantics. Her point matters for
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }}):
nearest-neighbor retrieval finds similar chunks, while a graph can preserve
explicit relationships and typed paths.

## Embeddings and Vector Search

Vector search depends on representation quality. If the embedding model does
not encode the distinction the product needs, the vector database can't fix the
retrieval result. Daniel's 21:55 chapter in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
explains vector search through shared embedding representations. The same
episode covers multimodal retrieval and personalization, where different kinds
of signals must live in a comparable vector space.

Daniel also shows why vector databases aren't only document stores. At 32:43
he uses CLIP for text-to-image retrieval. At 38:11 he discusses title, content,
image, and behavioral embeddings. At 40:48 he discusses recency and time bias
in vector space. Those examples connect vector databases to
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) products
that retrieve products, images, sessions, or recommendations.

## RAG

RAG is the most visible vector-database use case in these episodes, but the guests
don't reduce RAG to vector storage. Atita's podcast-transcript example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
uses chunking, overlap, embedding models, and vectorization at 38:24. At 42:49
she connects retrieval, augmentation, generation, and citation design.

Meryem gives the production LLM reason for retrieval. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she argues at 40:46 that changing knowledge is often better handled with
retrieval than with repeated fine-tuning. At 42:02 she connects that choice to
indexing documents and grounding answers. The vector database helps retrieve
context, but the application still needs source selection and permissions. It
also needs citations and
[LLM evaluation]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

Anahita's 33:43 and 39:56 chapters in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
show a different RAG design. She combines LLM grounding with knowledge graphs
and Cypher-driven retrieval. This makes
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
a separate design choice, not just a tooling preference.

## Production Search

Production search still needs ranking, filtering, metadata, and business
constraints. Vector similarity produces candidate matches, but product search,
support search, and recommender systems often need hybrid retrieval. Daniel's
34:00 chapter in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
combines vector similarity with filters and recency. At 39:53 he discusses how
constraints and business rules fit poorly if teams try to express everything as
one vector query.

Atita reaches a similar conclusion from search practice. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
her 52:07 chapter discusses session-based recommendations and re-ranking. At
54:54 she compares session-based personalization with collaborative filtering.
Those examples put vector databases next to
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}),
recommendation, and ranking, not above them.

## Evaluation

Teams should evaluate the retrieval result and the product outcome separately.
A vector database can return nearest neighbors quickly and still fail the user
task.

The wrong embedding model can miss intent, and the index can be stale. Filters
can remove useful candidates, and reranking can bury relevant items. The final
LLM answer can still cite the wrong chunk.

Atita discusses multi-level RAG evaluation and human-in-the-loop review at 48:09
in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Daniel takes the search-metrics route in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
at 1:01:25 he connects search quality to business metrics, A/B tests, and
revenue attribution. At 1:03:50 he discusses offline evaluation and operational
metrics. Those discussions make vector database evaluation part of
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}),
not a standalone benchmark.

## Storage and Indexing Tradeoffs

Vector storage and vector compute change at different speeds. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
Daniel separates ingestion-time encoding from query-time encoding at 29:00. At
30:22 he covers recomputing embeddings and model versioning. Teams may need to
rebuild indexes during model swaps, chunking changes, new modalities, or
metadata changes. They also need to keep old and new vectors consistent during
the migration.

Atita's 17:01 and 20:27 chapters in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
frame the storage decision as an architecture tradeoff. Existing search engines
can reduce operational sprawl when they already serve production traffic. A
dedicated vector database can make vector search easier to prototype, scale, or
separate from a legacy search stack.

The useful question isn't whether vector databases are better than search
engines. The useful question is which part of the retrieval system needs a
specialized vector index. That comparison belongs with
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }}).

## Related Pages

Use these pages for the adjacent retrieval, search, and LLM topics.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
- [Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
