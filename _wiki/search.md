---
layout: wiki
title: "Search"
summary: "Search as the product system that turns retrieval, ranking, answers, recommendations, constraints, and evaluation into a useful surface."
related:
  - Information Retrieval
  - Search Relevance
  - Production Search Evaluation
  - Retrieval-Augmented Generation
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Graph RAG vs Vector RAG
  - Knowledge Graph vs Vector Search
  - Vector Databases
  - Embeddings
  - Recommendation Systems
  - A/B Testing
---

Search turns queries, prompts, and intent signals into useful product surfaces.
Those surfaces may be ranked results, generated answers, or recommendations. It
sits above
[[information-retrieval=>Information Retrieval]], [[search-relevance=>Search
Relevance]], and [[production-search-evaluation=>Production Search Evaluation]].

Retrieval finds candidates, and relevance orders and filters them for the
product task. Evaluation checks whether the surface helped people do their work.

That boundary matters because a search product isn't only a retriever. Product
search, semantic document search, recommendations, and RAG answer surfaces
depend on retrieval. They also depend on ranking behavior and latency. Product
constraints add freshness, filters, and
[[machine-learning-personalization=>machine learning personalization]].
Business rules, citations, and feedback signals also influence the product.
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Product Surface

Search owns the surface where people judge usefulness, and a classic search page
shows ranked results. E-commerce search may show products, filters, and facets.
It may also show recommendations and personalized ordering. RAG search may show
a generated answer plus cited passages. Multimodal search may return images for
text queries or similar items for an uploaded image.
[[cite:building-production-search-systems@21:55=>Building Search Systems]]
[[cite:building-production-search-systems@58:17=>Building Search Systems]]

The same retrieval stack can support different surfaces, but each surface
changes what the product has to show. A results page needs inspectable result
snippets and a good order. A recommendation surface needs useful alternatives
even when the query is implicit. An answer surface needs enough context for the
model to answer and enough evidence for the reader to trust it.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Modern Search Systems]]
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@40:46=>Deploying LLMs in Production]]

## Product Constraints

Search systems have to satisfy product constraints after retrieval finds
candidates. Latency can change conversion and user trust. A product search team
therefore treats response time as part of relevance, not only an infrastructure
metric.[[cite:building-production-search-systems@10:45=>Building Search Systems]]

Filters, freshness, permissions, and business rules also live at the search
product boundary. Some constraints narrow the candidate set before ranking.
Others become ranking features or post-ranking rules. [[Information Retrieval]]
owns the retrieval-unit, index, candidate-generation, and prefilter decisions.
[[Search Relevance]] owns the ordering and product-fit tradeoffs after those
candidates exist.

Hybrid systems make the boundary visible. A team may use semantic retrieval to
find similar items. It may then combine recency, filters, popularity, and
product weights before displaying results.
[[cite:building-production-search-systems@34:00=>Building Search Systems]]
[[cite:building-production-search-systems@45:11=>Building Search Systems]]
The product question isn't whether lexical search, vector search, or graph
search is fashionable. The question is which mix produces useful results under
the constraints the team can operate.

## Matching Links, Not Matching Mechanics

Search links the matching choices together at a high level. Lexical search is
useful for exact terms, structured filters, and predictable behavior. Vector
search helps when queries and results use different words or modalities but
still mean similar things.[[cite:building-production-search-systems@20:02=>Building Search Systems]]
[[cite:building-production-search-systems@21:55=>Building Search Systems]]

The mechanics belong on narrower pages. [[Information Retrieval]] covers
retrieval units, indexes, candidate generation, and prefilters. It also covers
the handoff to ranking or generation. [[Vector Search vs Keyword Search]]
compares matching methods. [[Vector Database vs Search Engine]] covers the
serving boundary for nearest-neighbor search, filters, and mature search-engine
features.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Modern Search Systems]]
[[cite:building-production-search-systems@52:35=>Building Search Systems]]

Custom embeddings and custom rankers turn search into a production ML system.
Teams then own training data, rollout, evaluation, and rollback. They also own
model versioning and index refreshes.
[[cite:building-production-search-systems@36:21=>Building Search Systems]]
[[cite:building-production-search-systems@30:22=>Building Search Systems]]
That operating work connects search to [[MLOps]] and [[Data Quality and
Observability]].

## Answers and Relationship Search

RAG uses search as the product path to an answer. Retrieval brings context into
the prompt, but the search product still has to decide what the answer surface
shows. It may show citations and passages. It may also show traces, refusal
behavior, and follow-up actions.

[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] owns the full
RAG flow, while the [[llm-rag-production-roadmap=>LLM and RAG production
roadmap]] connects retrieval decisions to citation behavior, feedback loops,
and operations. [[RAG Evaluation Workflow]] and [[LLM Evaluation Workflows]]
cover answer checks after retrieval.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag@44:26=>Practical LLM Engineering and RAG]]

Relationship-heavy search changes the surface again. Automotive R&D search can
combine reports, parts, simulations, and load paths. Materials and references
can enter the same graph. The useful result may be a graph neighborhood or path
rather than a single text chunk.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@15:58=>Knowledge Graphs and LLMs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@38:10=>Knowledge Graphs and LLMs]]
[[Graph RAG vs Vector RAG]] and [[Knowledge Graph vs Vector Search]] cover that
architecture boundary.

Entity search has the same product structure in operational data. Identity
resolution and fraud investigation need candidate retrieval. Supplier matching
and account matching need it too. People then review matches, networks, and
evidence on the decision surface.
[[cite:building-open-source-data-product-for-identity-resolution@07:14=>Identity Resolution]]
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@29:15=>Fraud Detection Data Engineering]]

## Evaluation and Operations

Search quality spans retrieval quality, ranking quality, product impact, and
system health. Offline tests can reveal candidate or ranking failures before a
launch. Online experiments and business metrics show whether the shipped
surface helps people complete the task.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]]
[[cite:building-production-search-systems@61:25=>Building Search Systems]]
[[cite:building-production-search-systems@63:50=>Building Search Systems]]

Failure analysis should follow the layer that failed. Missing candidates move
the investigation to ingestion, chunking, and indexing. Filters and retrieval
settings belong in the same check.

Bad ordering indicates ranking and relevance problems. Unhelpful generated
answers move the investigation to context selection, prompt packaging, answer
checks, or review.
[[cite:practical-llm-engineering-and-rag@23:00=>Practical LLM Engineering and RAG]]
[[cite:practical-llm-engineering-and-rag@27:20=>Practical LLM Engineering and RAG]]

Production search also needs operational ownership, and each architecture has
different chores. Lexical systems need schema, synonym, and ranking-rule
maintenance. Vector systems need embedding pipelines, index refreshes, and
model-version handling. RAG systems need retrieval tests, answer checks, traces,
and human review. Knowledge-graph systems need reliable entities and edges
because extracted facts can be wrong.
[[cite:building-production-search-systems@30:22=>Building Search Systems]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@42:42=>Knowledge Graphs and LLMs]]
