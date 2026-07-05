---
layout: wiki
title: "Search Relevance"
summary: "How production search teams combine retrieval, ranking, filters, evaluation, experiments, and business goals into useful results."
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

Search relevance decides which results should appear for a query. It also
decides how to order them and why that order helps the person or business using
the search product.
It sits inside [[Search]] and [[Information Retrieval]], and it depends on
[[Metrics]] and [[a-b-testing=>A/B testing]]. Latency, freshness, permissions,
and cost matter too.

Search relevance asks what should rank and why it should rank there. It also
asks which product outcome the ranking should serve.
[[Vector Search vs Keyword Search]] covers matching methods,
[[Vector Database vs Search Engine]] covers infrastructure ownership, and
[[Production Search Evaluation]] covers testing and measurement.

Search is a decision problem: from a large set of information, the system has to
isolate the pieces that matter for the current query. Production search splits
into candidate generation and ranking, and that split is the working model for
relevance.[[cite:building-production-search-systems]]

## Relevance Boundaries

In production search, relevance isn't only semantic similarity. A result can
match the query words and sit near the query in embedding space. It can satisfy
filters, respect permissions, and look fresh enough while still missing the
product goal. Relevance work connects result quality to business outcomes,
control groups, offline tests, and engineer-facing iteration
metrics.[[cite:building-production-search-systems]]

That definition also keeps relevance separate from model impressiveness.
Teams start from the use case, then choose vector databases, existing search
engines, or combined systems.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval]]

Vector search may improve a class of matching failures. It doesn't replace
query understanding or ranking, and it still needs filters, evaluation, and
user metrics.

Sadat Anwar's OLX work is a concrete production-search example. The first
problem was operational, with search incidents and onboarding through
firefighting. The fix started with Solr autoscaling after CPU-load analysis. The
team then decoupled search from the monolith. After that, the team could move
relevance and ML work separately
[[cite:from-software-engineering-to-leading-data-science-teams@6:31=>Search Engineering at OLX]]
[[cite:from-software-engineering-to-leading-data-science-teams@8:42=>Solr Autoscaling]]
[[cite:from-software-engineering-to-leading-data-science-teams@10:37=>Decoupling Search from Monolith]].

Sadat's example links relevance to [[Information Retrieval]],
[[Software Engineering]], and operations. The ranking idea has to survive
traffic, ownership, and release constraints.

## Candidate Generation And Ranking

Search systems usually retrieve a small candidate set before ranking those
candidates with more expensive signals. Candidate generation quickly narrows a
large corpus to a small set. Ranking estimates which candidates should be shown
first for the query.[[cite:building-production-search-systems]]

That split matters because the failure modes differ. If the right document
never enters the candidate set, the ranker can't rescue it. If the candidate
set contains the right document but the result is buried, the ranking features,
weights, or training data need attention. Teams therefore evaluate
recall-oriented retrieval separately from rank quality. They also check click
quality, conversion quality, and business outcomes.

Candidate generation may use lexical indexes, vector indexes, graph lookups, or
metadata filters. Ranking may use term scores, freshness, popularity, and
[[machine-learning-personalization=>machine learning personalization]]. It may
also use behavioral signals, learned-to-rank models, or business rules. Use
[[Production Search Evaluation]]
when the question is how to measure each stage without collapsing the whole
search product into one score.

Modern search adds LLMs to this older relevance stack rather than skipping it.
Solr and Lucene still explain the lexical candidate layer. Learning-to-rank
explains learned ordering. RAG or answer generation depends on whether that
relevance layer supplied useful evidence first
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@23:00=>Search Evolution]].

## Lexical, Vector, And Hybrid Retrieval

Lexical, vector, and hybrid retrieval create different candidate sets before any
reranker or product objective can act. Exact-word matching, filters, semantic
similarity, and query-time weights fail in different ways.
[[cite:building-production-search-systems]] Use
[[Vector Search vs Keyword Search]] for the retrieval-method comparison and
[[Vector Database vs Search Engine]] for the storage and serving boundary.

## Filters, Freshness, And Business Rules

Filters can be hard constraints or ranking preferences, and Lucene-style `must`
and `should` clauses separate those cases. A strict freshness filter may remove
the best result if it's just outside the window. A softer freshness signal can
keep that result and still favor new content when relevance is
similar.[[cite:building-production-search-systems]]

This is where search relevance becomes product design. A marketplace may care
about seller contact, order delivery, or revenue proxies. A support search
product may care about solved tickets, escalation rate, and current policy. A
RAG assistant may care about source correctness, citation usefulness, and
refusal behavior. The right ranking objective depends on the outcome the team
wants to change, not only on retrieval scores.

Metadata and access rules belong in the same discussion. A result can be
semantically relevant and still unusable because the person isn't allowed to
see it. The result may also be stale or violate a business rule. For
retrieval-heavy LLM systems, use
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] to keep
search constraints visible before generation.

## Metrics, Offline Tests, And A/B Testing

Production relevance needs more than a relevance label or an embedding score.
Teams judge ranking changes with business impact, [[a-b-testing=>A/B testing]],
proxy metrics, and control groups. They also use seasonality checks, offline
evaluation, and fast iteration
metrics.[[cite:building-production-search-systems]]

Metrics matter because relevance is a ranking objective, not a raw embedding
score. Use [[Production Search Evaluation]] for offline tests, online tests,
monitoring, and search-specific measurement. Use [[Experimentation]] for broader
product experiment mechanics, and use [[Evaluation]] when the team needs to name
which decision the metric will change.

## RAG And Agent Retrieval

RAG systems make relevance failures visible in a different way. If retrieval
misses the right chunk, the model may answer fluently from weak context.
Transcript-chatbot systems move from chunking and embeddings to retrieval
strategy and prompt context. They also need citations, offline tests, and human
review.
RAG quality starts as a search relevance problem before it becomes an
answer-quality problem.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval]]

Representative gold tests, failure analysis, logs, and traces give RAG builders
a way to see whether retrieval changes improve the system. Chunking and
embeddings can become a practical business win when the interface makes the
retrieved context useful.[[cite:practical-llm-engineering-and-rag]]

Agent systems extend the same boundary because retrieval is one tool among
others. Latency, cost, and context quality constrain that tool. Custom datasets
and mocked tools help test retrieval behavior, while integration tests,
regression tests, and goal-based assertions catch relevance
regressions[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation]].
Use [[LLM Evaluation Workflows]] when the product combines retrieval,
generation, and tool use.

## Related Pages

Use these pages for the neighboring parts of the search relevance stack.

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
