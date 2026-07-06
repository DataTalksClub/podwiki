---
layout: wiki
title: "Information Retrieval"
summary: "Information retrieval as the design of retrieval units, indexes, candidate generation, prefilters, and the handoff to ranking or generation."
related:
  - Search
  - Search Relevance
  - Retrieval-Augmented Generation
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Vector Databases
  - Embeddings
  - Production Search Evaluation
---

Information retrieval finds candidate information from a larger collection. It
defines the retrieval unit, index, query representation, and
candidate-generation method. It also defines prefilters and the handoff to a
ranker or generator. [[Search]] owns the product system and visible surface.
Information retrieval owns what enters the candidate set before the product can
rank, answer, or recommend.

The same retrieval boundary appears in product search, semantic search, and
recommendations. RAG and agent tools use it too. Product search may retrieve
products. Semantic search may retrieve documents, passages, or images.

RAG may retrieve transcript chunks, source records, or graph neighborhoods.
Agent tools may retrieve database rows, log lines, or API results.
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Retrieval Units and Indexes

Retrieval starts by choosing the unit that can satisfy the downstream task. A
product-search system may retrieve product records. A document-search system may
retrieve documents or passages. A transcript RAG system may retrieve questions,
answers, speaker turns, or longer sections. Long context windows don't remove
the choice because irrelevant context can still weaken the answer.
[[cite:practical-llm-engineering-and-rag@44:26=>Practical LLM Engineering and RAG]]
[[cite:practical-llm-engineering-and-rag@46:39=>Practical LLM Engineering and RAG]]

Indexes make those units searchable without scanning the whole collection. An
inverted index supports term lookup for lexical search. Vector indexes support
nearest-neighbor lookup over embeddings. Graph indexes and graph databases make
entity and relationship lookup practical when the answer depends on paths,
edges, provenance, or domain constraints.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@04:42=>Modern Search Systems]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@28:00=>Knowledge Graphs and LLMs]]

The index isn't the product, but it gives the product a candidate set. [[Vector
Databases]] covers vector storage and nearest-neighbor serving. [[Vector
Database vs Search Engine]] covers when those capabilities belong inside a
search engine. It also covers when a dedicated vector database becomes the
center of the workload.

## Candidate Generation

Candidate generation narrows a collection to plausible results before ranking.
This split is central to production search: retrieval produces a smaller set,
then ranking estimates which query-result pairs fit the task.
[[cite:building-production-search-systems@06:20=>Building Search Systems]]
[[cite:building-production-search-systems@12:45=>Building Search Systems]]

Candidate recall sets the upper bound for the rest of the system. If the
retriever never returns the relevant product or passage, the ranker can't
rescue it. The same applies to records and graph paths. RAG has the same
failure mode: the model can only answer from the context the retriever places in
the prompt.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Modern Search Systems]]

Lexical candidate generation matches query terms against indexed text. It
supports exact words, domain terms, structured filters, and predictable
debugging behavior. Semantic candidate generation compares learned
representations, so it can connect different words, modalities, or behavior
signals that refer to similar intent.
[[cite:building-production-search-systems@20:02=>Building Search Systems]]
[[cite:building-production-search-systems@21:55=>Building Search Systems]]

[[Vector Search vs Keyword Search]] owns the method comparison, while
information retrieval owns the narrower design decision. The
candidate-generation method has to return the right units soon enough for the
ranker, generator, or tool call that follows.

## Prefilters, Blocking, and Mandatory Constraints

Prefilters reduce the search space before ranking or generation. Metadata
filters, permission checks, and date windows can prevent expensive or irrelevant
comparisons. Language filters, source filters, and identity-blocking keys can do
the same. They can also exclude the needed result, so they belong in retrieval
tests.

Bloom filters show the prefilter boundary in a compact form. They can answer
absence or possible presence, with false positives as part of the design. That
makes them useful for memory-saving containment checks, crawler URL
deduplication, routing-table checks, and adtech screening before a later system
makes a final decision.
[[cite:algorithms-data-structures-for-engineers@30:09=>Algorithms and Data Structures]]
[[cite:algorithms-data-structures-for-engineers@34:43=>Bloom Filter Applications]]
[[cite:algorithms-data-structures-for-engineers@35:59=>Adtech Bloom Filter Example]]

Entity resolution uses the same retrieval idea. Blocking and indexing keep the
system from comparing every record pair. Later scoring decides whether
customer, supplier, or product records refer to the same real-world entity. The
same scoring approach can apply to account and location records.
[[cite:building-open-source-data-product-for-identity-resolution@07:14=>Identity Resolution]]
[[cite:building-open-source-data-product-for-identity-resolution@14:02=>Identity Resolution]]

Fraud systems add graph and document retrieval around people, transactions,
products, and investigations. Document indexes, graph databases, and SPARQL help
teams retrieve connected entities before network features or investigators
evaluate the case.
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@21:30=>Fraud Detection Data Engineering]]
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@29:15=>Fraud Detection Data Engineering]]

## RAG Retrieval Units

RAG retrieval usually works over chunks, passages, source records, or graph
neighborhoods. Chunk size, overlap, and embedding model affect what the LLM can
see. Retrieval count and source metadata matter too.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Modern Search Systems]]

Retrieval also handles changing facts better than repeated fine-tuning when the
source of truth lives in documentation, wikis, or internal systems. The
retriever can index current sources and pass relevant passages into the answer,
while fine-tuning is better suited to style or behavior changes.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@40:46=>Deploying LLMs in Production]]
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]

Once retrieved material becomes model input, [[context-engineering=>Context
Engineering]] owns how that material is wrapped for the model.
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] owns the
broader answer flow. That flow includes prompting, citations, and synthesis. It
also includes refusal behavior and answer evaluation.

## Handoff to Ranking or Generation

Information retrieval ends at the handoff boundary. In search, the retriever
passes candidate documents or products to ranking. It may also pass chunks or
graph paths. In RAG, it passes context to prompt packaging and generation.

In agent systems, the retriever may pass logs and metrics to a planner. It may
also pass rows or API responses to a tool-calling step.
[[cite:building-production-search-systems@12:45=>Building Search Systems]]
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Evaluate that handoff by asking whether the right unit reached the next stage.
Candidate recall, filter behavior, and permission filtering are retrieval
checks. So are index freshness, deduplication, and top-k settings. Ordering,
merchandising, and personalization belong in [[search-relevance=>Search
Relevance]]. Product fit belongs there too.

Offline tests, online experiments, monitoring, and business metrics belong in
[[production-search-evaluation=>Production Search Evaluation]].
[[cite:building-production-search-systems@61:25=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]]

To preserve the boundary, failure analysis maps missing candidates to ingestion,
chunking, and indexing. It also checks filters and embeddings as well as graph
extraction and retrieval count. Bad ordering indicates ranking problems.

Bad answers after good retrieval indicate context-packaging, prompting, or
generation problems. They can also indicate answer-check problems.
[[cite:practical-llm-engineering-and-rag@23:00=>Practical LLM Engineering and RAG]]
[[cite:practical-llm-engineering-and-rag@27:20=>Practical LLM Engineering and RAG]]
