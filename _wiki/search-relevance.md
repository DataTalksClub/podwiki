---
layout: wiki
title: "Search Relevance"
summary: "How production search teams define ranking quality, filters, business goals, and useful result order."
related:
  - Search
  - Information Retrieval
  - Production Search Evaluation
  - Vector Databases
  - Vector Search vs Keyword Search
  - Vector Database vs Search Engine
  - Embeddings
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - A/B Testing
  - Metrics
---

Search relevance is the judgment of which results should appear for a query and
how to order them. The order should serve a product outcome. It sits inside
[[Search]] and [[Information Retrieval]]. Latency and freshness can change the
right ranking. Permissions, cost, and product goals can change it too.

Relevance work focuses on ranking quality and product fit. [[Information
Retrieval]] covers retrieval mechanics, [[Vector Search vs Keyword Search]]
covers matching methods, and [[Vector Database vs Search Engine]] covers
infrastructure ownership. [[Production Search Evaluation]] covers testing and
measurement.

Production search splits into candidate generation and ranking, and that split
is the working model for relevance. [[Information Retrieval]] asks whether the
right candidates entered the set. Search relevance asks which of those
candidates deserve the top positions.[[cite:building-production-search-systems=>Building Search Systems]]

## Relevance Boundaries

In production search, relevance isn't only semantic similarity. A result can
match the query words and sit near the query in embedding space. It can satisfy
filters, respect permissions, and look fresh enough while still missing the
product goal. Relevance work connects result quality to the outcome the product
needs.[[cite:building-production-search-systems=>Building Search Systems]]

Teams start from the use case, then choose vector databases, existing search
engines, or combined systems
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Vector search may improve a class of matching failures. Relevance work still
asks whether the final order satisfies filters, permissions, and freshness.
[[Production Search Evaluation]] owns the measurement workflow.

Sadat Anwar's OLX work is a concrete production-search example. The first
problem was operational, with search incidents and onboarding through
firefighting. The fix started with Solr autoscaling after CPU-load analysis. The
team then decoupled search from the monolith. After that, the team could move
relevance and ML work separately
[[cite:from-software-engineering-to-leading-data-science-teams@06:31=>Search Engineering at OLX]]
[[cite:from-software-engineering-to-leading-data-science-teams@08:42=>Solr Autoscaling]]
[[cite:from-software-engineering-to-leading-data-science-teams@10:37=>Decoupling Search from Monolith]].

Sadat's example links relevance to [[Information Retrieval]],
[[Software Engineering]], and operations. The ranking idea has to survive
traffic, ownership, and release constraints.

## Ranking After Candidate Generation

Search systems usually retrieve a small candidate set before ranking those
candidates with more expensive signals. [[Information Retrieval]] covers that
retrieval design. Search relevance starts where the product has to choose which
candidates should be shown first for the query.[[cite:building-production-search-systems=>Building Search Systems]]

The split matters because the failure modes differ. If the right document
never enters the candidate set, the ranker can't rescue it. If the candidate
set contains the right document but the result is buried, the ranking features,
weights, or training data need attention. Teams therefore evaluate
recall-oriented retrieval separately from rank quality. They also check click
quality, conversion quality, and business outcomes.

Ranking may use term scores, freshness, popularity, and
[[machine-learning-personalization=>machine learning personalization]]. It may
also use behavioral signals, learned-to-rank models, or business rules.
[[Production Search Evaluation]] covers measurement for each stage.

Modern search adds LLMs to this older relevance stack rather than skipping it.
Solr and Lucene still explain the lexical candidate layer. Learning-to-rank
explains learned ordering. RAG or answer generation depends on whether that
relevance layer supplied useful evidence first
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@23:00=>Search Evolution]].

## Filters, Freshness, and Business Rules

Filters can be hard constraints or ranking preferences, and Lucene-style `must`
and `should` clauses separate those cases. A strict freshness filter may remove
the best result if it's just outside the window. A softer freshness signal can
keep that result and still favor new content when relevance is
similar.[[cite:building-production-search-systems=>Building Search Systems]]

This is where search relevance becomes product design. A marketplace may care
about seller contact, order delivery, or revenue proxies. A support search
product may care about solved tickets, escalation rate, and current policy. A
RAG assistant may care about source correctness, citation usefulness, and
refusal behavior. The right ranking objective depends on the outcome the team
wants to change, not only on retrieval scores.

Metadata and access rules belong in the same discussion. A result can be
semantically relevant and still unusable because the person isn't allowed to
see it. The result may also be stale or violate a business rule. For
retrieval-heavy LLM systems, [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
keeps those search constraints visible before generation.

## Product Metrics and Experiments

Production relevance needs more than a relevance label or an embedding score.
Teams judge ranking changes with business impact, [[a-b-testing=>A/B testing]],
proxy metrics, and control groups. They also use seasonality checks, offline
evaluation, and fast iteration metrics
[[cite:building-production-search-systems=>Building Search Systems]].

Metrics matter because relevance is a ranking objective, not a raw embedding
score. A relevance metric should say what counts as a better result order and
which product behavior the ranker should improve. [[Production Search
Evaluation]] covers offline tests, online tests, monitoring, and
search-specific measurement.

## RAG and Agent Retrieval

RAG systems make relevance failures visible in a different way. If retrieval
misses the right chunk, the model may answer fluently from weak context. The
answer can only use the evidence that retrieval supplied. RAG quality therefore
starts as a relevance problem before it becomes an answer-quality problem
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].

Agent systems extend the same boundary because retrieval is one tool among
others. Latency, cost, and context quality constrain that tool. Custom datasets
and mocked tools help test retrieval behavior, while integration tests,
regression tests, and goal-based assertions catch relevance regressions
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Agentic AI Systems]].
[[LLM Evaluation Workflows]] covers products that combine retrieval,
generation, and tool use, while [[Production Search Evaluation]] covers the
search-side test and monitoring workflow.

## Related Pages

Neighboring search topics cover the surrounding retrieval and measurement work.

- [[Search]] and
  [[Information Retrieval]]
  cover the broader retrieval vocabulary.
- [[Production Search Evaluation]]
  covers relevance labels, offline tests, online experiments, and monitoring.
- [[Vector Search vs Keyword Search]]
  covers lexical, semantic, and hybrid matching choices.
- [[Vector Databases]] and
  [[Embeddings]] cover vector
  retrieval mechanics.
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers
  retrieval for LLM products.
- [[a-b-testing=>A/B Testing]],
  [[Experimentation]], and
  [[Metrics]] cover product measurement.
