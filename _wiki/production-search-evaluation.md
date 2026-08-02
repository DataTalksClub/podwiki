---
layout: wiki
title: "Production Search Evaluation"
summary: "How teams test, segment, monitor, and diagnose production search and RAG retrieval quality."
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
and online tests. It also covers segment checks, monitoring, and failure diagnosis.
[[Search]] and [[Information Retrieval]] define the system being measured.

The system has to retrieve relevant candidates and rank them well. It also has
to meet latency, freshness, permission, and business constraints.

[[search-relevance=>search relevance]] defines ranking judgment and product fit.
It also defines how filters, freshness, and business objectives affect ranking.
[[Vector Search vs Keyword Search]] compares matching-method tradeoffs.
[[Vector Database vs Search Engine]] covers infrastructure placement.

Teams use the same evaluation discipline for [[vector databases]],
[[embeddings]], and [[retrieval-augmented-generation=>retrieval-augmented
generation]]. The broader architecture map belongs in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

## Measurement Scope

Production search evaluation isn't one relevance number. Teams need separate
checks for candidate retrieval, ranking order, and generated answers. They also
need checks for product segments and production behavior. Search systems
separate candidate generation from ranking. Evaluation has to show whether the
right items were retrieved before it asks whether they were ordered correctly.
[[cite:building-production-search-systems=>Building Search Systems]]

RAG systems add answer-level checks to that retrieval base. Chunking, embedding
choice, retrieval count, and prompt context are separate failure points.
Citations, generated answers, offline tests, and human review need separate
checks too. Evaluation must show both that the right evidence was retrieved and
that the generated response used it correctly.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Production search evaluation sits between [[Evaluation]], [[LLM Evaluation
Workflows]], [[a-b-testing=>A/B Testing]], and [[Model Monitoring]]. Offline
checks diagnose the system quickly. Online experiments show whether changes
hold up with real users and traffic. Monitoring shows whether the same behavior
continues after launch.

## Failure Boundaries

Search evaluation starts with the relevance objective from [[search-relevance=>search relevance]]
and turns it into checks that engineers can run before and after launch. Those
checks can include relevance labels, click behavior, contact rate, and order
rate. They can also include revenue, solved tickets, latency, and empty-result
rate.
[[cite:building-production-search-systems=>Building Search Systems]]

Modern search and RAG evaluation start from architecture. Vector databases and
existing search systems can each be the source of poor answers. Chunking,
embedding choice, and retrieval can fail separately. Prompt construction,
citations, and generation need their own checks too. Evaluation has to locate
the layer that failed instead of treating the answer as one undifferentiated
model output.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Production ML search adds constraints that semantic similarity alone misses.
Evaluation has to preserve those constraints in test cases and segment reports.
Recency, popularity, and metadata can each change the result set. Filters,
feature fusion, and query-time weights can do the same. Freshness-sensitive,
[[machine-learning-personalization=>personalized]], and permissioned searches
need their own checks because aggregate scores can hide their failures.
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
The [[rag-evaluation-workflow=>RAG evaluation workflow]] turns that split into a
repeatable review path for retrieval, prompt context, citations, and answers.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

## Segment and Hybrid Checks

Hybrid search turns evaluation into a segment problem. Teams use
[[search-relevance=>search relevance]] to decide how vector similarity trades
off against filters, recency, and popularity. Metadata and query-time weights
belong in that judgment too. Production search evaluation checks those
tradeoffs by segment because nearest-neighbor quality alone isn't enough.
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

Segment-level checks matter more than aggregate metrics alone, so teams should
evaluate exact-match and semantic queries separately. They should also separate
long-tail queries from head queries, new content from stale content, and
permissioned content from high-value business segments.

Content behind permission filters and high-value business segments need their
own checks. A freshness boost can help newsy queries and hurt evergreen results.
A strict filter can enforce a product rule but remove a useful near match.
Those cases need slice-level reports, representative examples, and regression
cases rather than one blended score.

## RAG Answer Quality

RAG evaluation adds answer-level checks on top of retrieval checks. A transcript
chatbot pipeline starts with ingestion, chunking, overlap, and embedding models.
Vectorization belongs in the same setup.

The pipeline then retrieves context, builds a prompt, returns citations, and
uses multi-level metrics. Offline tests and human review complete the
evaluation. When those checks become evidence for a concrete implementation,
use the [[search-and-rag-project-checklist=>Search/RAG Project Checklist]] to
keep corpus and chunking next to the retrieved context. It also keeps citations
and failure labels in the same review.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

The same evaluation boundary appears in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] and [[LLM
Evaluation Workflows]].
The [[rag-evaluation-workflow=>RAG evaluation workflow]] is the more specific
page for that boundary when the product depends on retrieved evidence.
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
retrieval or ranking behavior improves the product outcome named in
[[search-relevance=>search relevance]].

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

## Metrics, Trust, and Diagnosis

Production search evaluation translates the relevance objective into metrics and
diagnostics. A marketplace or ecommerce site may track contact rate and order
rate. It may also track empty-result rate, latency, and revenue. A support
system or internal knowledge base may track solved tickets, escalation, time
saved, and failed refinements. A RAG assistant may track answer acceptance,
citation use, unsupported answers, and refusals.[[cite:building-production-search-systems=>Building Search Systems]]

The metric is only useful when it suggests a fix. Freshness, filters, and
metadata can improve one segment while hurting another. Popularity and business
rules can do the same. Evaluation reports should therefore name the affected
segment and the likely layer. The issue may sit in candidate generation,
ranking, filtering, or personalization. For RAG products, it may sit in prompt
assembly, generation, or policy.[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

For RAG, product fit includes trust. Citation and human-review checks turn answer
quality into a user-facing issue. A fluent answer that hides weak retrieval is
worse than a cautious answer with clear sources when the product depends on
evidence.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

The same evaluation boundaries apply across candidate generation, ranking, and
answer grounding. They also apply to segment checks, monitoring, and failure
diagnosis.
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]
