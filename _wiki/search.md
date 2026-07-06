---
layout: wiki
title: "Search"
summary: "Search as retrieval, ranking, evaluation, semantic matching, and product relevance."
related:
  - Information Retrieval
  - Search Relevance
  - Retrieval-Augmented Generation
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Graph RAG vs Vector RAG
  - Knowledge Graph vs Vector Search
  - Production Search Evaluation
  - Vector Databases
  - Embeddings
  - NLP
  - A/B Testing
---

Search is the product layer that turns a query into a useful result, answer, or
recommendation. It sits above [[information retrieval]], [[search relevance]],
and [[production search evaluation]]. A search system has to retrieve
candidates and rank them. It also has to apply product constraints, serve the
result quickly, and measure whether people found what they needed.

Search is a practical engineering problem rather than a technology choice.
Classical systems use lexical indexes such as Lucene, Solr, and Elasticsearch.
Newer systems add [[embeddings]], [[vector databases]], hybrid retrieval, and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:building-production-search-systems=>Building Search Systems]].

Search work repeatedly crosses matching, ranking, and product judgment.
[[Information Retrieval]] covers retrieval units and indexes, plus candidate
generation, chunking, and prefilters. [[Search Relevance]] covers result order,
product fit, filters, and freshness. [[Production Search Evaluation]] covers
offline tests, online experiments, monitoring, and business metrics.

## Search System Layers

Search systems usually split into retrieval and ranking. Retrieval produces a
candidate set, and ranking orders those candidates for the product surface.
Daniel Svonava frames search as a decision problem about relevance, then separates
candidate generation from ranking and later measurement
[[cite:building-production-search-systems@06:20=>Building Search Systems]]
[[cite:building-production-search-systems@12:45=>Building Search Systems]].

That split matters because the failure modes differ. A retriever can miss the
right document, item, or chunk. A ranker can find a good candidate but bury it
below weaker results. A product can retrieve and rank correctly but still fail
because filters, freshness, latency, or business rules don't match the user
task. In shopping search, Daniel Svonava treats latency as a product constraint
because delays change the customer experience and business outcome
[[cite:building-production-search-systems@10:45=>Building Search Systems]].

Search also serves more than result pages. The same mechanics can serve product
recommendations and multimodal lookup. They can also serve document discovery
and context retrieval for an LLM. Daniel Svonava connects search to
recommendation systems, personalization, image-text retrieval, and e-commerce
prototypes
[[cite:building-production-search-systems@21:55=>Building Search Systems]]
[[cite:building-production-search-systems@58:17=>Building Search Systems]].

[[book:20210712-relevant-search=>Relevant Search]] covers scoring and ranking
in Solr and Elasticsearch-era systems. [[book:20211101-ai-powered-search=>AI-Powered Search]]
extends that discipline into learning-to-rank, vector retrieval, and LLM-era
retrieval.

## Matching Methods and Constraints

Lexical search matches query terms against indexed text. It fits exact terms
and structured filters, but it also brings the maintenance cost of synonyms,
configuration, and brittle query rules
[[cite:building-production-search-systems@20:02=>Building Search Systems]].

Vector search matches learned representations. It helps when the query and
result use different words, modalities, or behaviors but still mean similar
things. Daniel Svonava describes embeddings as shared representations for text
and images. He also connects them to metadata, behavior, and popularity signals
[[cite:building-production-search-systems@21:55=>Building Search Systems]]
[[cite:building-production-search-systems@38:11=>Building Search Systems]].

Hybrid search combines both approaches. A team may retrieve semantically
similar items, then apply filters and recency. It may also apply popularity or
product rules. Daniel
Svonava gives this as a practical design: combine vector similarity with
filters and recency. Then tune weights at query time when the product context
changes
[[cite:building-production-search-systems@34:00=>Building Search Systems]]
[[cite:building-production-search-systems@45:11=>Building Search Systems]].

Custom embeddings and custom rankers move search toward [[MLOps]]. Once a team
trains task-specific encoders or ranking models, it also owns data collection.
It also owns rollout, evaluation, and rollback
[[cite:building-production-search-systems@36:21=>Building Search Systems]].

That's why [[Vector Search vs Keyword Search]] isn't only a model comparison.
It's a constraint comparison. [[Vector Database vs Search Engine]] covers the
serving boundary. Keep vector retrieval inside an existing search engine when
the product still depends on mature filtering and ranking. Use a dedicated
vector database when nearest-neighbor search and embedding operations sit at the
center of the workload
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Modern Search Systems]]
[[cite:building-production-search-systems@52:35=>Building Search Systems]].

## Retrieval for RAG

RAG uses search to retrieve context before an LLM generates an answer. It adds
prompt packaging, answer synthesis, and answer checks after retrieval. It
doesn't remove retrieval design.

Atita Arora's transcript-chatbot discussion keeps the search choices visible.
Teams still choose chunk size, overlap, embedding models, and vectorization.
They also choose retrieval count, prompt structure, and citations
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Modern Search Systems]].

The production choice is whether the LLM should receive the right context.
Daniel Svonava argues that prompted timestamps and LLM-only retrieval have
limits. He also argues that specialized encoders can serve retrieval more
efficiently when the product needs stable relevance and latency
[[cite:building-production-search-systems@46:18=>Building Search Systems]]
[[cite:building-production-search-systems@47:37=>Building Search Systems]].

Retrieval also handles changing facts better than repeated fine-tuning. Meryem
Arik describes the common documentation case, where teams embed and index
sources such as Confluence or Notion. They retrieve the relevant passages and
ground the generated answer in current material. Fine-tuning is a better fit for
style or tone than for keeping factual knowledge fresh
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@40:46=>Deploying LLMs in Production]]
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

Hugo Bowne-Anderson gives the operating version of the same point. Start with a
simple RAG system that solves a real support or search need before escalating to
agents. Chunking depends on the data, so transcript search may use questions and
answers. It may also use speaker turns or larger sections. Long context can
reduce precision if it gives the model too much irrelevant text
[[cite:practical-llm-engineering-and-rag@44:26=>Practical LLM Engineering and RAG]]
[[cite:practical-llm-engineering-and-rag@46:39=>Practical LLM Engineering and RAG]].

[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers the
full RAG workflow, and [[LLM Evaluation Workflows]] covers generated-answer
tests. [[Vector Databases]] covers storage and nearest-neighbor indexing.
[[RAG Evaluation Workflow]] covers the evaluation set and failure analysis that
sit after retrieval.

## Relationship Search and Knowledge Graphs

Dense retrieval is strongest when similarity is enough. Relationship retrieval
is stronger when the answer depends on explicit structure. Anahita Pakiman's
automotive R&D episode uses knowledge graphs for crash simulation reports,
parts, and load paths. It also covers semantic reporting, graph analytics, and
graph ML
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@15:58=>Knowledge Graphs and LLMs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@28:00=>Knowledge Graphs and LLMs]].

In automotive search a text chunk describes a component, but a graph adds
simulation and material context around it. The graph can also include
load-path context and report-section context. Papers and references fit there
too.
Relationship questions need entity-and-edge retrieval, not only nearest text
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@38:10=>Knowledge Graphs and LLMs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@39:56=>Knowledge Graphs and LLMs]].

[[Graph RAG vs Vector RAG]] and [[Knowledge Graph vs Vector Search]] describe
that boundary. Vector retrieval is still useful for semantic matching and
candidate generation. Graph retrieval becomes useful when the product needs
verifiable relationships, paths, provenance, or domain constraints.

Entity resolution shows the same search boundary in tabular and warehouse
data. Sonal Goyal describes identity resolution as deciding whether customer
records refer to the same real-world entity. The same idea applies to supplier,
product, account, and location records. The retrieval layer uses blocking and
indexing so the system compares plausible candidate records instead of every
possible pair
[[cite:building-open-source-data-product-for-identity-resolution@07:14=>Identity Resolution]]
[[cite:building-open-source-data-product-for-identity-resolution@14:02=>Identity Resolution]].

Angela Ramirez gives the fraud-detection version. Document indexes, graph
databases, and SPARQL help teams search across entities. Network features then
connect members, transactions, products, and investigations
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@21:30=>Fraud Detection Data Engineering]]
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@29:15=>Fraud Detection Data Engineering]].

## Measurement and Operations

Search quality isn't one metric. Teams evaluate retrieval quality and ranking
quality, then track latency and product impact. They also track operating
health. Atita Arora describes multi-level RAG evaluation, offline tests, and
human-in-the-loop review.

Daniel Svonava connects search impact to business metrics and
[[a-b-testing=>A/B testing]]. He also connects it to operational metrics such as
fast iteration and offline evaluation
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]]
[[cite:building-production-search-systems@61:25=>Building Search Systems]]
[[cite:building-production-search-systems@63:50=>Building Search Systems]].

Failure analysis should decide the next change. If retrieval caused the error,
fix ingestion and chunking before tuning the generation prompt. Embedding
choice and filters belong in the same check, and so does top-k selection. That
keeps search/RAG work close to the part of the system that actually failed
[[cite:practical-llm-engineering-and-rag@23:00=>Practical LLM Engineering and RAG]]
[[cite:practical-llm-engineering-and-rag@27:20=>Practical LLM Engineering and RAG]].

The operating work also differs by architecture. Lexical systems need synonym
and schema maintenance plus ranking rules. Vector systems need embedding
pipelines, model versioning, recomputation, and index refreshes
[[cite:building-production-search-systems@30:22=>Building Search Systems]].

RAG systems need retrieval tests, answer checks, traces, and human review.
Knowledge-graph systems need entity quality, edge quality, and verification
because LLM-extracted knowledge can still be wrong
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@42:42=>Knowledge Graphs and LLMs]].

That puts search across [[Machine Learning System Design]],
[[llm-production-patterns=>LLM production patterns]], [[MLOps]], and
[[Data Quality and Observability]]. The durable question isn't which search
tool is newest. It's which design gives the product relevant, explainable, and
measurable results under the constraints the team can operate.

## Related Pages

The adjacent decisions split by search layer.

- [[Information Retrieval]]
- [[Search Relevance]]
- [[Production Search Evaluation]]
- [[Vector Search vs Keyword Search]]
- [[Vector Database vs Search Engine]]
- [[Graph RAG vs Vector RAG]]
- [[Knowledge Graph vs Vector Search]]
- [[Retrieval-Augmented Generation]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[search-and-rag-project-checklist=>Search/RAG Project Checklist]]
- [[Entity Resolution]]
