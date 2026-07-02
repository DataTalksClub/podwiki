---
layout: article
tags: ["comparison"]
title: "Knowledge Graph vs Vector Search"
keyword: "knowledge graph vs vector search"
secondary_keywords:
  - knowledge graph versus vector search
  - vector search vs knowledge graph
  - knowledge graph vs vector database
summary: "How DataTalks.Club podcast guests compare explicit graph relationships with embedding-based retrieval for search, RAG, and domain knowledge systems."
related_wiki:
  - Search
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
[[embeddings]] and retrieves nearby
items by similarity.

[[person:anahitapakiman|Anahita Pakiman]] gives the
graph-side example in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]].
Automotive R&D teams use Neo4j for semantic reporting and simulation
comparison. They also use it for clustering, load-path detection, and
Cypher-driven retrieval.

[[person:atitaarora|Atita Arora]] gives the vector-side RAG example in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Teams chunk podcast transcripts and embed them. Then they retrieve matching
chunks and pass them to an LLM with citations. [[person:danielsvonava|Daniel Svonava]]
anchors the production vector-search side in
[[podcast:building-production-search-systems|Building Search Systems]],
where vector similarity becomes one signal inside candidate generation and
ranking. Filters, recency, and business evaluation matter too.

[[book:20210405-the-practitioners-guide-to-graph-data|The Practitioner's Guide to Graph Data]]
by Denise Gosnell gives the graph-data engineering side of this comparison,
from graph database modeling to query-driven retrieval.

Use vector search when the system must find semantically related passages or
products. It also fits images, users, or sessions. Use a knowledge graph when
the answer depends on relationships and paths. It also fits hierarchy,
constraints, provenance, or lineage.
Use hybrid retrieval when semantic recall finds candidates and graph structure
adds the relationships or constraints that make the answer trustworthy.

Start here when choosing the retrieval substrate.
[[Graph RAG vs Vector RAG]] covers how those
retrieval choices package context for an LLM. [Vector Database vs Search
Engine]({{ '/wiki/vector-database-vs-search-engine/' | relative_url }})
covers whether vector retrieval belongs in a dedicated vector store or an
existing [[search]] stack.
[[retrieval-augmented-generation|RAG]] and
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
cover the broader answer-generation design.

## Representation and Retrieval Unit

Vector search first turns a query and candidate items into vectors. It then
retrieves nearby vectors. Daniel explains this as a shared representation space
at 21:55 in
[[podcast:building-production-search-systems|Building Search Systems]].
The embedding model has to encode the properties the product cares about before
nearest-neighbor retrieval can work.

Atita shows the RAG version at 38:24-42:49 in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Teams chunk transcripts and choose overlap. They embed the chunks, retrieve
relevant pieces for a question, and ask the LLM to answer with prompt
instructions and citations. Because the system retrieves chunks, chunk size and
metadata matter. Retrieval count and citation quality determine the result too.

A knowledge graph makes relationships explicit before retrieval. In Anahita's
automotive R&D discussion, graph structure supports semantic reporting and
simulation comparison. It also supports clustering and load-path detection
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
15:58-20:32). When she moves into LLM retrieval, chapters and sections become
retrieval inputs. Semantic relations and Cypher queries do too, rather than
serving as metadata around a text chunk
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
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
([[podcast:building-production-search-systems|Building Search Systems]],
20:02-21:55). Atita's podcast-transcript system uses the same idea. The system
embeds the question, retrieves relevant transcript chunks, and asks the LLM to
answer from those chunks with references
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
38:24-42:49).

Knowledge graphs fit questions where the connection is part of the answer.
Anahita's graph examples answer questions about how parts, simulations, and
reports relate to each other. They also cover chapters, sections, and
engineering concepts. Those questions need order and containment. They also
need paths and typed relations, not only semantically similar text
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
20:32 and 38:10).

The practical split is failure-driven. Choose vector search when the system
misses semantically related material. Choose a knowledge graph when the system
loses relationship structure, hierarchy, constraints, or provenance. Choose
both when the product first needs candidate recall and then needs structured
context. [[Graph RAG vs Vector RAG]]
uses the same split for LLM context packaging.

## Search Stack Boundaries

Atita starts from classical
[[information retrieval]].
In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
she discusses Qdrant and vector databases at 17:01 when the use case needs
vectors. Around 20:27, she still keeps Solr and Lucene in the architecture
conversation. Elasticsearch and OpenSearch stay in scope too. Vector search can
live in a standalone vector database or inside an existing search stack.

Daniel starts from production search as candidate generation plus ranking. His
29:00-30:22 discussion in
[[podcast:building-production-search-systems|Building Search Systems]]
separates vector compute from vector storage. A vector database doesn't remove
ingestion work. Teams still need embedding-model consistency, reindexing, and
query-time encoding.

At 34:00-45:11, he combines vector similarity with filters
and recency. Metadata, behavior, popularity, and query-time weights also influence
the result.

That production view connects vector search to
[[Vector Database vs Search Engine]]
and [[Production Search Evaluation]].
The retrieval stack should serve relevance, latency, ranking quality, and
business outcomes. It shouldn't stop at nearest-neighbor lookup.

Anahita starts from domain semantics, so her comparison isn't only about
relevance. The system has to preserve relationships across simulations and
reports. It also has to preserve relationships across sections, entities, and
engineering concepts. At 42:42 in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
she warns that LLM-extracted graph content needs verification. Graph systems
move trust work into modeling and validation rather than eliminating it.

## Production Work

Vector search creates pipeline work. Teams compute embeddings during ingestion
and again at query time. They keep model versions consistent, plan reindexing,
and decide which component should own retrieval. Daniel's options include
Lucene and Elasticsearch. They also include Postgres and specialized vector stores
([[podcast:building-production-search-systems|Building Search Systems]],
29:00-33:13).

Atita adds RAG-specific work around chunking, overlap, and retrieval count.
Prompt design, citations, and human review matter too
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
38:24-48:09). Those choices tie vector retrieval to
[[LLM Evaluation Workflows]]
because the team has to evaluate retrieved context, citation quality, and final
answers.

Knowledge graphs create modeling work. Teams define entities and relation
types, ingest graph data, and design graph queries. They also keep provenance
and validate the graph. At 39:56, Anahita shows graph queries feeding prompts.
At 42:42, she
warns that teams need to check LLM-extracted nodes and relations before trusting
them
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
39:56-42:42).

[[person:ranjithakulkarni|Ranjitha Kulkarni]] adds the
agent boundary. At 29:30-37:39 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]],
she treats RAG and search as tools with latency and cost constraints. Metadata
and garbage-in-garbage-out constraints matter too. Retrieval is enough when it
reduces a large search space to useful context.
[[Agent Engineering]]
enters when the product also needs planning, multiple tools, dynamic state, or
actions beyond retrieval.

## Hybrid Retrieval Patterns

Production systems often combine vector search and lexical search with metadata
and structured context. Vector search can retrieve candidate passages or
entities, while a graph can add neighborhoods and paths. It can also add
constraints, provenance, or section hierarchy before the final answer.

Anahita describes that combined direction at 33:43-39:56 in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]].
Knowledge graphs and LLMs ground answers together. Graph semantics compensate
for relations that chunk-only retrieval can miss.

Daniel makes the same point from the ranking side. At 34:00-45:11 in
[[podcast:building-production-search-systems|Building Search Systems]],
vector similarity works with filters and recency. Behavior, popularity,
metadata, and query-time weights influence the served result.

[[person:meryemarik|Meryem Arik]] frames retrieval as
the better fit for changing knowledge in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
40:46-48:01. [[person:hugobowneanderson|Hugo Bowne-Anderson]]
treats chunking and RAG as useful only when the retrieved context can support
the answer in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
44:26-53:34. Together, those episodes put vector search and graph lookup inside
the same retrieval design space rather than competing slogans.

## Evaluation and Failure Modes

Vector systems can return similar but wrong neighbors. They can also fail
because embeddings are stale, chunks are poorly sized, metadata is missing, or
ranking ignores the product goal. Atita ties those risks to chunking, overlap,
and retrieval count. Prompt design, citations, and human review matter too
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
38:24-48:09).

Daniel adds business KPIs and A/B tests. He also covers offline tests and
revenue attribution at
1:01:25-1:03:50 in
[[podcast:building-production-search-systems|Building Search Systems]].
For vector search, check retrieval, ranking, and filters. Check citations and
business outcomes before judging the generated answer.

Graph systems fail when they encode wrong relations, miss important relations,
or become stale as the domain changes. Brittle schemas and unverified LLM
extraction create graph failures too. Anahita's 42:42 warning in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]
matters because a graph can expose provenance, relation types, and paths.
Incorrect nodes or edges still corrupt downstream RAG and analysis.

For a graph, check entity extraction, relation correctness, and traversal
behavior. Check provenance and validation before answer quality. For vector
search, check candidate quality and embedding freshness. Then check chunk
boundaries, filters, and ranking.

[[Production Search Evaluation]]
covers retrieval and ranking checks.
[[LLM Evaluation Workflows]] covers systems where
retrieved context feeds an LLM.

## Related Topics

Use these pages for the surrounding retrieval, search, and LLM-system decisions:

- [[Graph RAG vs Vector RAG]] for LLM context packaging.
- [[Vector Database vs Search Engine]] for retrieval-stack ownership.
- [[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]], [[Search]], [[retrieval-augmented-generation|RAG]], and [[retrieval-augmented-generation|Retrieval-Augmented Generation]] for the broader architecture.
- [[Vector Databases]] and [[Embeddings]] for the vector side.
- [[Production Search Evaluation]] and [[LLM Evaluation Workflows]] for evaluation.
- [[Agent Engineering]] for systems where retrieval becomes one tool inside a multi-step agent.

