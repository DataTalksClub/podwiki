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
right ranking. Permissions, cost, filters, and business goals can change it too.

Relevance work names the ranking objective before the team measures it.
[[Information Retrieval]] covers retrieval mechanics, [[Vector Search vs
Keyword Search]] covers matching methods, and [[Vector Database vs Search
Engine]] covers infrastructure ownership. [[Production Search Evaluation]]
covers offline and online tests. It also covers segment checks, monitoring, and
failure diagnosis.

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
engines, or combined systems.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Vector search may improve a class of matching failures. Relevance work still
asks whether the final order satisfies filters, permissions, freshness, and the
business objective. [[Production Search Evaluation]] tests whether that
judgment holds.

Sadat Anwar's OLX work is a concrete production-search example. The first
problem was operational, with search incidents and onboarding through
firefighting. The fix started with Solr autoscaling after CPU-load analysis. The
team then decoupled search from the monolith. After that, the team could move
relevance and ML work separately.
[[cite:from-software-engineering-to-leading-data-science-teams@06:31=>Search Engineering at OLX]][[cite:from-software-engineering-to-leading-data-science-teams@08:42=>Solr Autoscaling]][[cite:from-software-engineering-to-leading-data-science-teams@10:37=>Decoupling Search from Monolith]]

Sadat's example links relevance to [[Information Retrieval]],
[[Software Engineering]], and operations. The ranking judgment has to survive
traffic, ownership, and release constraints.

## Ranking After Candidate Generation

Search systems usually retrieve a small candidate set before ranking those
candidates with more expensive signals. [[Information Retrieval]] covers that
retrieval design. Search relevance starts where the product has to choose which
candidates should be shown first for the query.[[cite:building-production-search-systems=>Building Search Systems]]

The split matters because the failure modes differ. If the right document
never enters the candidate set, the ranker can't rescue it. If the candidate
set contains the right document but the result is buried, the ranking features,
weights, or training data need attention. Teams therefore separate
recall-oriented retrieval questions from rank-quality questions before they
compare click quality, conversion quality, or business outcomes in
[[Production Search Evaluation]].

Ranking may use term scores, freshness, popularity, and
[[machine-learning-personalization=>machine learning personalization]]. It may
also use behavioral signals, learned-to-rank models, or business rules.
Search relevance owns the choice of which signals should influence the order.
[[Production Search Evaluation]] tests whether those signals help.

Modern search adds LLMs to this older relevance stack rather than skipping it.
Solr and Lucene still explain the lexical candidate layer. Learning-to-rank
explains learned ordering. RAG or answer generation depends on whether that
relevance layer supplied useful evidence first.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@23:00=>Search Evolution]]

[[person:pauliusztin=>Paul Iusztin]] describes a project-research version of the same split. A
brain-dump query first retrieves a broad set of personal resources, then a
reranking pass orders them relative to the original question before the agent
uses them. The ranking is query-relative rather than a universal quality score,
and a small project corpus keeps context noise manageable.[[cite:s24e09-engineering-your-own-ai-assistant@34:52=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@35:24=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@36:38=>Engineering Your Own AI Assistant]]

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

## Product Objectives and Business Fit

Production relevance needs more than a relevance label or an embedding score.
Teams first decide what the ranking should optimize. A marketplace may value
buyer contact, order completion, or supply freshness. A support search product
may value solved tickets, reduced escalation, or current policy. A RAG
assistant may value source correctness, citation usefulness, and refusal
behavior when the retrieved evidence is weak.
[[cite:building-production-search-systems=>Building Search Systems]][[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Business rules belong in the relevance judgment when they change which result
should rank first. A sponsored result, a safety rule, a permission rule, or a
freshness boost can all be legitimate if the product chooses that objective
explicitly. They create ranking tradeoffs because they may lower lexical or
semantic similarity to satisfy a stronger product constraint.

[[Production Search Evaluation]] then checks that objective with offline
judgment sets, [[a-b-testing=>A/B testing]], segment analysis, and monitoring.
Search relevance owns the judgment of what "better" means for the result order.
Production search evaluation owns the proof that the new order works.

## RAG and Agent Retrieval

RAG systems make relevance failures visible in a different way. If retrieval
misses the right chunk, the model may answer fluently from weak context. The
answer can only use the evidence that retrieval supplied. RAG quality therefore
starts as a relevance problem before it becomes an answer-quality problem.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Agent systems extend the same boundary because retrieval is one tool among
others. Latency, cost, and context quality constrain that tool. Custom datasets
and mocked tools help test retrieval behavior, while integration tests,
regression tests, and goal-based assertions catch relevance regressions.
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Agentic AI Systems]]
[[LLM Evaluation Workflows]] covers products that combine retrieval,
generation, and tool use. [[Production Search Evaluation]] covers the
search-side test, segment, and monitoring workflow.
