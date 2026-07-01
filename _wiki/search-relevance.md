---
layout: wiki
title: "Search Relevance"
summary: "How production search teams turn candidate generation, ranking, lexical and vector retrieval, filters, evaluation, experiments, and business goals into useful results."
related:
  - Search
  - Information Retrieval
  - Production Search Evaluation
  - Vector Databases
  - Embeddings
  - Search RAG and Knowledge Systems
  - LLM Evaluation Workflows
  - A/B Testing
  - Metrics
---

Search relevance decides which results should appear for a query. It also
decides how to order them and why that order helps the person or business using
the search product.
It sits inside [search]({{ '/wiki/search/' | relative_url }}) and
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
It also depends on [metrics]({{ '/wiki/metrics/' | relative_url }}),
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}), latency, and
freshness. Permissions and cost matter too.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
most direct framing in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
At 6:20, he treats search as a decision problem. From a large set of
information, the system has to isolate the pieces that matter for the current
query. At 12:45, he splits production search into candidate generation and
ranking. Use that split as the working model for relevance.

## Working Definition

In production search, relevance isn't only semantic similarity. A result can
match the query words and sit near the query in embedding space. It can satisfy
filters, respect permissions, and look fresh enough while still missing the
product goal. Daniel's search-metrics discussion at 1:01:25-1:03:50 ties
relevance work to business outcomes, control groups, offline tests, and
engineer-facing iteration metrics
([Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})).

That definition also keeps relevance separate from model impressiveness.
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) warns in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 17:01-20:27 that teams should start from the use case. They can then choose
vector databases, existing search engines, or combined systems.

Vector search may improve a class of matching failures. It doesn't replace
query understanding or ranking, and it still needs filters, evaluation, and
user metrics.

## Candidate Generation And Ranking

Search systems usually retrieve a small candidate set before ranking those
candidates with more expensive signals. Daniel explains this at 12:45 in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Candidate generation quickly narrows a large corpus to a small set. Ranking
estimates which candidates should be shown first for the query.

That split matters because the failure modes differ. If the right document
never enters the candidate set, the ranker can't rescue it. If the candidate
set contains the right document but the result is buried, the ranking features,
weights, or training data need attention. Teams therefore evaluate
recall-oriented retrieval separately from rank quality. They also check click
quality, conversion quality, and business outcomes.

Candidate generation may use lexical indexes, vector indexes, graph lookups, or
metadata filters. Ranking may use term scores, freshness, popularity, and
personalization. It may also use behavioral signals, learned-to-rank models, or
business rules. Use
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
when the question is how to measure each stage without collapsing the whole
search product into one score.

## Lexical, Vector, And Hybrid Retrieval

Lexical retrieval still matters because exact words and names often matter.
Product codes matter too. So do filters and structured constraints. Daniel
discusses inverted indexes and Lucene at 11:29-17:40 in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
He also covers practical indexing, which shows why teams should use mature
search engines instead of hand-rolling index structures.

Vector retrieval helps when query words and result words differ but the meaning
matches. Daniel introduces [embeddings]({{ '/wiki/embeddings/' | relative_url }})
as shared representations at 21:55-29:00. He then separates vector storage from
vector compute at 29:00-30:22. Document embedding models, query embedding
models, and refresh pipelines all become relevance dependencies. Model swaps
and embedding versioning can change
which results even become candidates.

Hybrid retrieval is the practical middle ground. At 34:00-45:11, Daniel
discusses vector similarity alongside filters and recency. He also covers
metadata and query-time weights
([Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})).
Use
[Vector Search vs Keyword Search]({{ '/comparisons/vector-search-vs-keyword-search/' | relative_url }})
for the retrieval-method boundary and
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
for the storage and serving boundary.

## Filters, Freshness, And Business Rules

Filters can be hard constraints or ranking preferences. Daniel contrasts this
with Lucene-style `must` and `should` clauses at 39:53 in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
A strict freshness filter may remove the best result if it's just outside the
window. A softer freshness signal may keep that result while still favoring new
content when relevance is similar.

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
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [RAG]({{ '/wiki/rag/' | relative_url }}) to keep search constraints visible
before generation.

## Metrics, Offline Tests, And A/B Testing

Production relevance needs more than a relevance label or an embedding score.
Daniel's 1:01:25 answer in
[Building Production Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
starts from business impact. He then covers A/B testing, proxy metrics,
seasonality, and control groups. He also discusses offline evaluation and
metrics that engineers can move during fast iteration.

Offline evaluation is useful when the team needs fast feedback on a ranking
change, embedding model, chunking strategy, or filter rule. It can use judged
query-result pairs, replayed logs, synthetic tasks, or gold examples. Offline
scores aren't the final product answer, though. They need online checks
because user behavior, seasonality, inventory, and presentation can change what
the metric means.

A/B testing connects relevance to actual user and business behavior. It can
measure clicks, conversions, contacts, or orders. It can also measure solved
tickets or another product outcome. Use
[experimentation]({{ '/wiki/experimentation/' | relative_url }}) for broader
product experiment mechanics. Use
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}) when the team needs to
name which decision the metric will change.

## RAG And Agent Retrieval

RAG systems make relevance failures visible in a different way. If retrieval
misses the right chunk, the model may answer fluently from weak context.
Atita's transcript-chatbot example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 38:24-48:09 moves from chunking and embeddings to retrieval strategy,
prompt context, and citations. It then moves to offline tests and human review.
RAG quality starts as a search relevance problem before it becomes an
answer-quality problem.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) gives
the builder workflow in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 23:00-27:38, he recommends representative gold tests and failure analysis.
He also recommends logs and traces.

At 44:26-49:21, he treats chunking and embeddings as a practical business win
for RAG. He also includes a focused interface. If most failures are retrieval
failures, the team should fix retrieval before tuning the generator.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) extends
that boundary to agents in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 29:30-37:39, she treats retrieval as one tool among others. Latency, cost,
and context quality constrain that tool.

At 51:17-56:02, she adds custom datasets, mocked tools, and integration tests.
She also adds regression tests and goal-based assertions. Use
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
when the product combines retrieval, generation, and tool use.

## Related Pages

Use these pages for the neighboring parts of the search relevance stack.

- [Search]({{ '/wiki/search/' | relative_url }}) and
  [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
  cover the broader retrieval vocabulary.
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
  covers relevance labels, offline tests, online experiments, and monitoring.
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) and
  [Embeddings]({{ '/wiki/embeddings/' | relative_url }}) cover vector
  retrieval mechanics.
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
  and [RAG]({{ '/wiki/rag/' | relative_url }}) cover retrieval for LLM
  products.
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}),
  [Experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
  [Metrics]({{ '/wiki/metrics/' | relative_url }}) cover product measurement.
