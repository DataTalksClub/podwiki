---
layout: wiki
title: "Production Search Evaluation"
summary: "Production search evaluation with relevance checks, RAG quality, business metrics, A/B tests, and monitoring."
related:
  - Search
  - Search Relevance
  - Retrieval-Augmented Generation
  - Information Retrieval
  - Vector Databases
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Evaluation
  - A/B Testing
---

Teams evaluate production search to prove that a search or retrieval system
returns useful results under product constraints. The workflow covers offline
tests and online experiments. It also covers monitoring, failure diagnosis, and
production metrics. [[Search]] and [[Information Retrieval]] define the system being
measured.

The system has to retrieve relevant candidates and rank them well. It also has
to meet latency, freshness, permission, and business constraints.
[[search-relevance=>search relevance]] defines ranking quality and product fit,
[[Vector Search vs Keyword Search]] compares matching-method tradeoffs, and
[[Vector Database vs Search Engine]] covers infrastructure placement.

Teams use the same evaluation discipline for [[vector databases]],
[[embeddings]], and [[retrieval-augmented-generation=>retrieval-augmented
generation]]. The broader architecture map belongs in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

## Measurement Scope

Production search evaluation isn't one relevance number. Teams need separate
checks for candidate retrieval, ranking order, generated answers, and product
impact. Search systems separate candidate generation from ranking. Evaluation
has to show whether the right items were retrieved before it asks whether they
were ordered correctly
[[cite:building-production-search-systems=>Building Search Systems]].

RAG systems add answer-level checks to that retrieval base. Chunking, embedding
choice, retrieval count, and prompt context are separate failure points.
Citations, generated answers, offline tests, and human review need separate
checks too. Evaluation must show both that the right evidence was retrieved and
that the generated response used it correctly.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Production search evaluation sits between [[Evaluation]], [[LLM Evaluation
Workflows]], [[a-b-testing=>A/B Testing]], and [[Model Monitoring]]. Offline
relevance checks diagnose the system quickly. Online experiments and monitoring
show whether changes hold up with real users, traffic, and business goals.

## Failure Boundaries

Search evaluation starts with relevance and ranking. It becomes more useful when
teams connect search metrics to product outcomes such as clicks, contacts,
orders, and revenue. Offline tests, A/B tests, and engineer-facing metrics give
teams a faster way to compare changes before and after launch.
[[cite:building-production-search-systems=>Building Search Systems]]

Modern search and RAG evaluation start from architecture. Vector databases and
existing search systems can each be the source of poor answers. Chunking,
embedding choice, and retrieval can fail separately. Prompt construction,
citations, and generation need their own checks too. Evaluation has to locate
the layer that failed instead of treating the answer as one undifferentiated
model output.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Production ML search adds constraints that semantic similarity alone misses.
Recency, popularity, and metadata can change the result set. Filters, feature
fusion, and query-time weights can do the same. The best result can depend on
freshness, constraints,
[[machine-learning-personalization=>machine learning personalization]], and the
current task.
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

## Retrieval Before Ranking

Evaluate retrieval before ranking because retrieval evaluation asks whether the
candidate set contains the right records. Those records may include documents
and products. They may also include chunks, images, or entities. Ranking
evaluation asks whether the best candidates appear near the top after scoring,
reranking, filtering, or personalization.

The candidate-generation and ranking split gives a practical debugging rule. If
relevant items are absent from the candidate set, work on indexing and query
understanding. Embeddings or metadata may need changes too.
[[cite:building-production-search-systems=>Building Search Systems]]

If the items are present but buried, work on ranking features and weights.
Reranking or business rules may need changes. A single dashboard metric can
hide the fix when retrieval and ranking failures are mixed together.

A RAG chatbot may answer badly for the same layered reasons. The retriever may
find the wrong chunks, the prompt may use them poorly, or the model may invent
unsupported text. Offline tests and human review keep those checks separate.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Segment and Hybrid Checks

Hybrid search turns evaluation into a segment problem. Vector similarity has to
work with product signals such as filters, recency, and popularity. Metadata
and query-time weights belong in the same design, so nearest-neighbor quality
alone isn't enough
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

Segment-level checks matter more than aggregate metrics alone. Teams should
evaluate exact-match and semantic queries separately, and they should separate
long-tail queries from new and stale content.

Content behind permission filters and high-value business segments need their
own checks. A freshness boost can help newsy queries and hurt evergreen results.
A strict filter can enforce a product rule but remove a useful near match.

## RAG Answer Quality

RAG evaluation adds answer-level checks on top of retrieval checks. A transcript
chatbot pipeline starts with ingestion, chunking, overlap, and embedding models.
Vectorization belongs in the same setup. The pipeline then retrieves context,
builds a prompt, returns citations, and uses multi-level metrics. Offline tests
and human review complete the evaluation.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

The same evaluation boundary appears in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] and [[LLM
Evaluation Workflows]].
The retrieval layer should be judged on evidence coverage and citation
usefulness. The answer layer should be judged on correctness, support from the
retrieved context, and refusal behavior. Formatting and user feedback belong in
the same review.

The comparison in [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] is also an
evaluation question. If the failure is missing or stale knowledge, retrieval and
source preparation are likely the right levers. If the failure is behavior or
style, the fix may belong in prompting or fine-tuning. Formatting and task
execution may show that the issue belongs in application logic.

## Offline Tests and Online Experiments

Offline tests are the fast diagnostic pass. They let engineers compare
retrievers, rankers, chunking strategies, and embedding models against a stable
set of representative cases. Prompts and rerankers belong in the comparison too.
Search teams use offline evaluation for faster iteration, while RAG evaluation
pairs offline tests with human review.
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Online experiments check whether the change improved user behavior under live
product conditions. Business metrics tie search changes to
[[a-b-testing=>A/B Testing]] and production rollouts. A/B tests are useful when
traffic, assignment, exposure logging, and metric definitions are strong enough
to support the decision.[[cite:building-production-search-systems=>Building Search Systems]]

Teams need both kinds of evidence because offline tests catch obvious
regressions and explain failure modes. Online experiments measure whether new
retrieval or ranking behavior improves the product outcome the team cares about.

## Monitoring After Launch

Search evaluation doesn't end at launch. Indexes change, content freshness
changes, user behavior changes, and business rules can shift. Vector compute and
ingestion create operational risk. Embedding pipelines add another risk because
recomputing embeddings or swapping models can change retrieval behavior even
when the UI stays the same.[[cite:building-production-search-systems=>Building Search Systems]]

Monitoring should include service health, latency, and index freshness, plus
empty and low-confidence results. Click behavior, conversion behavior, and user
feedback matter too.

Drift checks should cover queries, documents, metadata, and ranking signals.
Production search shares this monitoring surface with [[Model Monitoring]] and
[[MLOps]]. The search-specific concern is relevance over time, especially
whether results still help with current user queries.

RAG systems need additional feedback loops. They should log retrieved chunks,
citations, prompts, and generated answers where privacy and product constraints
allow. User feedback and review labels belong in the logs too.

Those logs help teams locate failures because the issue may belong in
ingestion, chunking, or retrieval. It may also belong in prompt assembly, model
choice, or answer policy.

## Product Metrics and Trust

Production search evaluation is ultimately a product-fit question. A
marketplace or ecommerce site may need different success metrics from a support
system, internal knowledge base, or RAG assistant. Useful metrics include
contact rate, order rate, resolved tickets, and time saved. Answer acceptance,
user trust, and revenue may matter too.[[cite:building-production-search-systems=>Building Search Systems]]

Product fit can conflict with raw similarity. Freshness, filters, metadata, and
popularity can improve one workflow while hurting another. Business rules can do
the same. Evaluation names the user segment and decision the system serves
before optimizing the metric.[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

For RAG, product fit includes trust. Citation and human-review checks turn answer
quality into a user-facing issue. A fluent answer that hides weak retrieval is
worse than a cautious answer with clear sources when the product depends on
evidence.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Related Topics

[[Search]] and [[Information Retrieval]] define the retrieval foundations.
[[search-relevance=>search relevance]] covers relevance objectives and ranking
quality, while
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
places search evaluation inside the wider knowledge-system map.

Generated-answer systems connect this page to
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
[[LLM Evaluation Workflows]],
and [[Search and RAG Project Checklist]].
For infrastructure choices, compare
[[Vector Database vs Search Engine]]
with
[[Knowledge Graph vs Vector Search]].

The same measurement boundaries apply across candidate generation, ranking,
answer grounding, and product constraints.
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]
