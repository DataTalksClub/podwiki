---
layout: article
title: "Knowledge Graph vs Vector Search"
keyword: "knowledge graph vs vector search"
secondary_keywords:
  - knowledge graph versus vector search
  - vector search vs knowledge graph
  - knowledge graph vs vector database
summary: "How DataTalks.Club podcast guests compare explicit graph relationships with embedding-based retrieval for search, RAG, and domain knowledge systems."
related_wiki:
  - Search, RAG, and Knowledge Systems
  - Vector Databases
  - Embeddings
  - Search
  - Retrieval-Augmented Generation
---

Knowledge graphs and vector search preserve different signals for retrieval.
Knowledge graphs store explicit entities and relation types. They also store
properties, paths, and neighborhoods. Vector search stores
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) and retrieves nearby
items by similarity.

Three DataTalks.Club episodes anchor the comparison:

- [Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) gives the
  graph-side example in
  [Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
  Automotive R&D teams use Neo4j for semantic reporting and simulation
  comparison. They also use it for clustering, load-path detection, and
  Cypher-driven retrieval.
- [Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the
  vector-side RAG example in
  [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
  Podcast transcripts are chunked, embedded, retrieved, and passed to an LLM
  with citations.
- [Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) anchors the
  production vector-search side in
  [Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
  Vector similarity becomes one signal inside candidate generation and ranking.
  Filters, recency, and business evaluation still matter.

This comparison is about the retrieval substrate: explicit relationships versus
embedding similarity.
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
covers the next layer, where the question is what context to give an LLM.
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
covers whether vector retrieval belongs in a dedicated vector store or an
existing [search]({{ '/wiki/search/' | relative_url }}) stack.

## Common Definition

DataTalks.Club guests usually define the split by representation. Vector search
turns a query and candidate items into vectors, then retrieves nearby vectors.
Daniel explains this as shared representation space at 21:55 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
the embedding model has to encode the properties the product cares about. Only
then can the retrieval system match query vectors against item vectors.

Atita shows the RAG version at 38:24-42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}):
teams chunk transcripts and embed the chunks. They retrieve the chunks for a
question and send them to the LLM with prompt instructions and citations.

A knowledge graph makes relationships explicit before retrieval. Anahita's
automotive R&D discussion uses graph structure for semantic reporting and
simulation comparison. It also uses graphs for clustering and load-path
detection
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
15:58-20:32). Later in the same episode, she contrasts chunks in a vector
database with knowledge graph semantics and relations, then shows
Cypher-driven prompt templates at 38:10-39:56.

Start by asking what the system must retrieve. Use vector search when the
failure is missing semantically related passages or products. It can also cover
users and media. Use a knowledge graph when the answer depends on relations and
paths. It can also depend on hierarchy, constraints, or lineage.

Daniel supports the vector side in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
at 12:45 and 34:00. Anahita supports the graph side in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
at 38:10. See also
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).

## Guest Differences

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) starts from classical
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
Her vector-search discussion asks whether teams should use a standalone vector
database or add vectors to an existing search stack. At 17:01 and 20:27 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she frames Qdrant and vector databases as useful when the use case needs
vectors. She still keeps Solr, Lucene, Elasticsearch, and OpenSearch in the
architecture conversation.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) starts from
production search as candidate generation plus ranking. His 29:00-30:22
discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
separates vector compute from vector storage. A vector database doesn't remove
ingestion work. Teams still need embedding-model consistency, reindexing, and
query-time encoding.

His 34:00-45:11 discussion adds filters and recency while also covering
metadata, behavior, popularity, and query-time weights. Those production
choices tie vector search to
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) starts from
domain semantics. In
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
her comparison isn't only about retrieval relevance. She asks whether the
system preserves relationships across simulations and reports. It also has to
preserve relationships across sections, entities, and engineering concepts.
Around 42:42, she warns that LLM-extracted graph
content needs verification, so graphs move trust work into modeling and
validation rather than eliminating it.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) adds the
agent boundary. At 29:30-37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she treats RAG and search as tools with latency and cost constraints. Metadata
and garbage-in-garbage-out constraints matter too.

Retrieval is enough when it reduces a large search space to useful context.
Agents enter when the product needs planning, multiple tools, or dynamic state.
That places vector search and graph lookup inside a wider
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}) design.

## Retrieval Units

Vector search retrieves nearby embeddings. In Daniel's production-search example,
the vector can represent products or users. It can also represent images,
sessions, or text. The embedding model has to place useful matches near each
other
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
21:55 and 33:13).

In Atita's transcript RAG example, the retrieval unit is a chunked passage. The
team controls chunk size, overlap, and the embedding model. It also controls
retrieval count, prompt instructions, and citations
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-42:49). See
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).

Knowledge graphs retrieve entities and relationships through paths and
neighborhoods. Anahita's automotive example depends on vehicle structures and
simulation relationships. It also depends on common parts, clustering, and load
paths
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
15:58-20:32).

When she moves into LLM retrieval, chapters and sections become retrieval
inputs. Semantic relations and Cypher queries become retrieval inputs too. They
aren't only metadata around a chunk
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
38:10-39:56). See
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}).

## Question Types

Vector search fits questions where the user doesn't know the exact words in
the source. Daniel frames embeddings as a way to retrieve candidates by shared
representation rather than brittle keyword rules
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
20:02-21:55). Atita's podcast-transcript system uses the same idea. It embeds
the question, retrieves relevant transcript chunks, and asks the LLM to answer
from those chunks with references
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-42:49). See [Embeddings]({{ '/wiki/embeddings/' | relative_url }}).

Knowledge graphs fit questions where the connection is the answer. Anahita's
graph examples answer questions about how parts and simulations relate to each
other. They also cover chapter structure, section structure, and domain
concepts.

Those questions need order and containment. They also need paths and typed
relations, not only semantically similar text
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
20:32 and 38:10). See
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}).

## Production Work

Vector search creates pipeline work. Daniel separates embedding generation from
vector storage at 29:00-30:22 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Teams compute embeddings during ingestion and again at query time. They also
keep model versions consistent and plan reindexing. They choose between Lucene,
Elasticsearch, Postgres, and specialized vector stores.

Atita adds RAG-specific work around chunking and retrieval strategy. Prompt
design, citations, and human review belong in the same decision
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-48:09). See
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}).

Knowledge graphs create modeling work, so teams need entity definitions and
relation types. They also need graph ingestion, query patterns, provenance, and
verification.

At 39:56, Anahita shows graph queries feeding prompts. At 42:42, she warns
that graph retrieval context needs validation. Teams need to check
LLM-extracted nodes and relations before trusting it
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
39:56-42:42). See
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

## Hybrid Retrieval

Production systems often combine the two ideas. Vector search can retrieve
candidate passages or entities, while a graph supplies neighborhoods and paths.
It can also supply constraints, provenance, or section hierarchy before the
final answer.

Anahita
describes that combined direction at 33:43-39:56 in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
Knowledge graphs and LLMs ground answers together. Graph semantics compensate
for relations that chunk-only retrieval can miss.

Daniel's production-search episode makes the same point from the ranking side.
At 34:00-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
vector similarity is combined with filters and recency. Behavior, popularity,
metadata, and query-time weights influence the result too.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
frames retrieval as the better fit for changing knowledge in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
40:46-48:01. [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
treats chunking and RAG as useful only when the retrieved context can support
the answer in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
44:26-53:34.

## Failure Modes

Vector systems can return similar but wrong neighbors. They can also fail
because embeddings are stale or chunks are poorly sized. Missing metadata can
break filtering and citations. Ranking can also miss the product goal.

Atita's RAG discussion ties those risks to chunking, overlap, and retrieval count.
Prompt design, citations, and human review matter too
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-48:09).

Daniel adds business KPIs, A/B tests, offline tests, and revenue attribution at
1:01:25-1:03:50 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).

Graph systems fail when they encode wrong relations. They also fail when they
miss important relations or become stale as the domain changes. Brittle schemas
and unverified LLM extraction create graph failures too.

Anahita's 42:42 warning in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
matters because a graph can make provenance and relation type visible. It can
also expose paths. Incorrect nodes or edges still corrupt downstream RAG and
analysis.

For vector search, check retrieval, ranking, and citations before answer
quality. For a graph, check entity extraction, relation correctness, and
traversal behavior before answer quality and provenance.

[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
covers retrieval and ranking checks.
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
covers systems where retrieved context feeds an LLM.

## Related Pages

The comparison connects to these search, RAG, and evaluation topics:

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
