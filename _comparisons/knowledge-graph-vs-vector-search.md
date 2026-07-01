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
  - Search
  - RAG
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - Graph RAG vs Vector RAG
  - Vector Database vs Search Engine
  - Agent Engineering
  - Production Search Evaluation
  - LLM Evaluation Workflows
---

Knowledge graphs preserve entities and relationship types with their paths,
properties, and neighborhoods. Vector search stores
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) and retrieves nearby
items by similarity.

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) gives the
graph-side example in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
Automotive R&D teams use Neo4j for semantic reporting and simulation
comparison. They also use it for clustering, load-path detection, and
Cypher-driven retrieval.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the vector-side RAG example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Teams chunk podcast transcripts and embed them. Then they retrieve matching
chunks and pass them to an LLM with citations. [Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }})
anchors the production vector-search side in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
where vector similarity becomes one signal inside candidate generation and
ranking. Filters, recency, and business evaluation matter too.

[The Practitioner's Guide to Graph Data]({{ '/books/20210405-the-practitioners-guide-to-graph-data/' | relative_url }})
by Denise Gosnell gives the graph-data engineering side of this comparison,
from graph database modeling to query-driven retrieval.

Use vector search when the system must find semantically related passages or
products. It also fits images, users, or sessions. Use a knowledge graph when
the answer depends on relationships and paths. It also fits hierarchy,
constraints, provenance, or lineage.
Use hybrid retrieval when semantic recall finds candidates and graph structure
adds the relationships or constraints that make the answer trustworthy.

Start here when choosing the retrieval substrate.
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}) covers how those
retrieval choices package context for an LLM. [Vector Database vs Search
Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
covers whether vector retrieval belongs in a dedicated vector store or an
existing [search]({{ '/wiki/search/' | relative_url }}) stack.
[RAG]({{ '/wiki/rag/' | relative_url }}) and
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
cover the broader answer-generation design.

## Representation and Retrieval Unit

Vector search first turns a query and candidate items into vectors. It then
retrieves nearby vectors. Daniel explains this as a shared representation space
at 21:55 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
The embedding model has to encode the properties the product cares about before
nearest-neighbor retrieval can work.

Atita shows the RAG version at 38:24-42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Teams chunk transcripts and choose overlap. They embed the chunks, retrieve
relevant pieces for a question, and ask the LLM to answer with prompt
instructions and citations. Because the system retrieves chunks, chunk size and
metadata matter. Retrieval count and citation quality determine the result too.

A knowledge graph makes relationships explicit before retrieval. In Anahita's
automotive R&D discussion, graph structure supports semantic reporting and
simulation comparison. It also supports clustering and load-path detection
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
15:58-20:32). When she moves into LLM retrieval, chapters and sections become
retrieval inputs. Semantic relations and Cypher queries do too, rather than
serving as metadata around a text chunk
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
38:10-39:56).

Teams choose architecture around the unit they retrieve, because vector search
retrieves nearby chunks and records. Those records can represent products,
images, users, or sessions. A graph retrieves nodes and edges, then returns
neighborhoods, paths, or query results. [Search, RAG, and Knowledge
Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) puts
both choices inside the broader search and knowledge-system stack.

## Question Fit

Vector search fits questions where users don't know the source wording. Daniel
frames embeddings as a way to retrieve candidates through shared representation
instead of brittle keyword rules
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
20:02-21:55). Atita's podcast-transcript system uses the same idea. The system
embeds the question, retrieves relevant transcript chunks, and asks the LLM to
answer from those chunks with references
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-42:49).

Knowledge graphs fit questions where the connection is part of the answer.
Anahita's graph examples answer questions about how parts, simulations, and
reports relate to each other. They also cover chapters, sections, and
engineering concepts. Those questions need order and containment. They also
need paths and typed relations, not only semantically similar text
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
20:32 and 38:10).

The practical split is failure-driven. Choose vector search when the system
misses semantically related material. Choose a knowledge graph when the system
loses relationship structure, hierarchy, constraints, or provenance. Choose
both when the product first needs candidate recall and then needs structured
context. [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
uses the same split for LLM context packaging.

## Search Stack Boundaries

Atita starts from classical
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she discusses Qdrant and vector databases at 17:01 when the use case needs
vectors. Around 20:27, she still keeps Solr and Lucene in the architecture
conversation. Elasticsearch and OpenSearch stay in scope too. Vector search can
live in a standalone vector database or inside an existing search stack.

Daniel starts from production search as candidate generation plus ranking. His
29:00-30:22 discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
separates vector compute from vector storage. A vector database doesn't remove
ingestion work. Teams still need embedding-model consistency, reindexing, and
query-time encoding.

At 34:00-45:11, he combines vector similarity with filters
and recency. Metadata, behavior, popularity, and query-time weights also influence
the result.

That production view connects vector search to
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
and [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
The retrieval stack should serve relevance, latency, ranking quality, and
business outcomes. It shouldn't stop at nearest-neighbor lookup.

Anahita starts from domain semantics, so her comparison isn't only about
relevance. The system has to preserve relationships across simulations and
reports. It also has to preserve relationships across sections, entities, and
engineering concepts. At 42:42 in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
she warns that LLM-extracted graph content needs verification. Graph systems
move trust work into modeling and validation rather than eliminating it.

## Production Work

Vector search creates pipeline work. Teams compute embeddings during ingestion
and again at query time. They keep model versions consistent, plan reindexing,
and decide which component should own retrieval. Daniel's options include
Lucene and Elasticsearch. They also include Postgres and specialized vector stores
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
29:00-33:13).

Atita adds RAG-specific work around chunking, overlap, and retrieval count.
Prompt design, citations, and human review matter too
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-48:09). Those choices tie vector retrieval to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
because the team has to evaluate retrieved context, citation quality, and final
answers.

Knowledge graphs create modeling work. Teams define entities and relation
types, ingest graph data, and design graph queries. They also keep provenance
and validate the graph. At 39:56, Anahita shows graph queries feeding prompts.
At 42:42, she
warns that teams need to check LLM-extracted nodes and relations before trusting
them
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
39:56-42:42).

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) adds the
agent boundary. At 29:30-37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she treats RAG and search as tools with latency and cost constraints. Metadata
and garbage-in-garbage-out constraints matter too. Retrieval is enough when it
reduces a large search space to useful context.
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
enters when the product also needs planning, multiple tools, dynamic state, or
actions beyond retrieval.

## Hybrid Retrieval Patterns

Production systems often combine vector search and lexical search with metadata
and structured context. Vector search can retrieve candidate passages or
entities, while a graph can add neighborhoods and paths. It can also add
constraints, provenance, or section hierarchy before the final answer.

Anahita describes that combined direction at 33:43-39:56 in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
Knowledge graphs and LLMs ground answers together. Graph semantics compensate
for relations that chunk-only retrieval can miss.

Daniel makes the same point from the ranking side. At 34:00-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
vector similarity works with filters and recency. Behavior, popularity,
metadata, and query-time weights influence the served result.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) frames retrieval as
the better fit for changing knowledge in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
40:46-48:01. [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
treats chunking and RAG as useful only when the retrieved context can support
the answer in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
44:26-53:34. Together, those episodes put vector search and graph lookup inside
the same retrieval design space rather than competing slogans.

## Evaluation and Failure Modes

Vector systems can return similar but wrong neighbors. They can also fail
because embeddings are stale, chunks are poorly sized, metadata is missing, or
ranking ignores the product goal. Atita ties those risks to chunking, overlap,
and retrieval count. Prompt design, citations, and human review matter too
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-48:09).

Daniel adds business KPIs and A/B tests. He also covers offline tests and
revenue attribution at
1:01:25-1:03:50 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
For vector search, check retrieval, ranking, and filters. Check citations and
business outcomes before judging the generated answer.

Graph systems fail when they encode wrong relations, miss important relations,
or become stale as the domain changes. Brittle schemas and unverified LLM
extraction create graph failures too. Anahita's 42:42 warning in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
matters because a graph can expose provenance, relation types, and paths.
Incorrect nodes or edges still corrupt downstream RAG and analysis.

For a graph, check entity extraction, relation correctness, and traversal
behavior. Check provenance and validation before answer quality. For vector
search, check candidate quality and embedding freshness. Then check chunk
boundaries, filters, and ranking.

[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
covers retrieval and ranking checks.
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) covers systems where
retrieved context feeds an LLM.

## Related Topics

Use these pages for the surrounding retrieval, search, and LLM-system decisions:

- [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}) for LLM context packaging.
- [Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }}) for retrieval-stack ownership.
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}), [Search]({{ '/wiki/search/' | relative_url }}), [RAG]({{ '/wiki/rag/' | relative_url }}), and [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) for the broader architecture.
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) and [Embeddings]({{ '/wiki/embeddings/' | relative_url }}) for the vector side.
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}) and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for evaluation.
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) for systems where retrieval becomes one tool inside a multi-step agent.
