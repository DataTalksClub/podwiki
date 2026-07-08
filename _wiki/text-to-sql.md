---
layout: wiki
title: "Text-to-SQL"
summary: "Podcast takeaways on text-to-SQL, metadata retrieval, governed metrics, query safety, and production testing for conversational BI."
related:
  - Business Intelligence
  - AI-Powered Business Intelligence
  - Retrieval-Augmented Generation
  - Metrics
  - Data Governance
  - Analytics Engineering
---

Text-to-SQL is a conversational interface that translates plain-language data
questions into SQL. It works as a practical access layer for people who
understand the policy or business question but don't know the warehouse schema.

Text-to-SQL fits inside [[business-intelligence=>business intelligence]] and
[[ai-powered-business-intelligence=>AI-powered BI]], not beside them. The chat
interface can make structured data easier to reach. The answer still depends on
modeled data, trusted [[metrics]], and the same [[data-products=>data product]]
boundaries that make analytical outputs usable. Metadata, access controls, and
data quality still matter. In the transport example, policy specialists ask plain-language
questions about fare-card data and fare changes. They also ask about concession
cards and monthly passes.[[cite:urban-data-science=>Urban Data Science]]

## Core Query Flow

A text-to-SQL system starts with a user question and schema or catalog context.
An LLM generates SQL, and a guarded execution path runs it. The transport
architecture retrieves metadata from warehouses and catalogs, then chunks that
context into a vector database. The LLM uses the retrieved context to choose the
relevant tables and produce SQL.[[cite:urban-data-science=>Urban Data Science]]

Text-to-SQL is a narrow form of
[[retrieval-augmented-generation=>retrieval-augmented generation]] because
retrieval supplies table, column, and metadata context before generation. The
generated SQL then runs against structured data, so the failure mode isn't only a
weak summary. It can also be a wrong table, missing filter, incorrect join, or
valid query for the wrong business question.[[cite:urban-data-science=>Urban Data Science]]

Teams shouldn't frame the goal as "chat over all data." They should build a
governed query path over a known analytical surface.
[[analytics-engineering=>Analytics engineering]] matters because modeled tables,
documented grain, and tested transformations give the assistant safer objects to
query than raw operational tables. The platform layer matters too.

[[data-engineering-platforms=>Data engineering platforms]] provide catalog
metadata, warehouse access, permissions, and operational interfaces. Those pieces
make text-to-SQL more than a prompt wrapped around a database.

## Boundaries and Tradeoffs

The episodes don't present a direct dispute about whether text-to-SQL is useful,
but they draw different boundaries around it.

The urban data discussion treats text-to-SQL as an access problem.
Subject-matter experts often ask to extract data or run analysis. When several
people relay those questions, the original intent can dilute. A plain-language
interface lets the domain expert keep more control over the question while the
system translates it into SQL.[[cite:urban-data-science=>Urban Data Science]]

The production AI discussion treats the same capability as an evaluation problem.
Prompt examples help the model imitate the desired conversion, but teams still
need an evaluation dataset with inputs and expected outputs. More examples stop
being useful once measured quality no longer improves, and larger prompts add
cost.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

The data strategy discussion puts the boundary at trust in the underlying data
product. A core KPI dashboard won't become trustworthy just because the access
interface changes. The problem remains when leaders already distrust it because
ingestion failed, SQL logic broke, lineage is missing, or teams report competing
numbers.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

## Architecture

The transport example gives the clearest architecture:

- Collect domain data such as fare-card events, sensor feeds, and journey
  aggregations into a warehouse.
- Store warehouse and catalog metadata in chunks that can be retrieved through a
  vector database.
- Retrieve the relevant metadata for a plain-English question.
- Ask the LLM to generate SQL against the retrieved schema context.
- Restrict unsafe commands and return the result with enough context for review.

Singapore fare-card data shows why the domain logic matters. It contains
millions of daily passenger-flow records, but journey logic goes beyond raw
tap-in and tap-out events. Transfers within a time window can become one journey,
and fares depend on total distance. Policy questions may refer to students or
senior citizens. They may also involve concession cards, monthly passes, or
peak-time pricing.[[cite:urban-data-science=>Urban Data Science]]

Schema retrieval helps the model find tables, but it doesn't define the business
meaning on its own. The assistant needs metadata for table grain, safe joins, and
governed definitions. It also needs owners and known limitations. This connects
text-to-SQL to [[data-governance=>data governance]] because catalogs, lineage,
ownership, and permissions decide which data the assistant can safely expose.

## Governed Metrics and BI Semantics

Text-to-SQL shouldn't make every raw table equally available for every question.
When a question is about a governed KPI, the assistant should prefer a trusted BI
asset. That might be a modeled table, dashboard query, metric definition, or
approved analytical view. Otherwise it can become a parallel BI stack with its
own unreviewed definition of revenue, active users, trips, or student-pass usage.

This is the same trust problem as a broken KPI dashboard. Leaders may need to
verify daily sales, revenue, or stock availability before using a dashboard. In
that case, the organization has a data product problem rather than an interface
problem.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

For ambiguous questions, the safer response is clarification. "Students using
monthly passes" could refer to cards or people. It could also mean tap events,
completed journeys, fare revenue, or policy uptake. The assistant should expose
the chosen definition, filters, source tables, and query grain instead of
presenting one number as self-evident.[[cite:urban-data-science=>Urban Data Science]]

## Query Safety and Reliability

Read-only constraints are a basic safety boundary. The transport text-to-SQL
project explicitly restricts commands such as `insert`, `update`, and `delete`
so generated SQL doesn't modify the database.[[cite:urban-data-science=>Urban Data Science]]

Reliability needs two test layers, starting with data-pipeline checks that make
warehouse outputs defensible. Snapshot-style tests and integration tests can sit
alongside SQL checks, Great Expectations, and Soda-style validations. These
checks catch nulls, missing columns, join problems, and other pipeline issues
before a dashboard or assistant uses the data. Those checks connect text-to-SQL
to [[data-quality-and-observability=>data quality and observability]]. A
generated query is only as reliable as the tables and definitions it touches
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

The generated SQL also needs evaluation. A test set should include natural
language questions and expected SQL or expected outputs. It should also check
format, filters, joins, and business definitions. Prompt examples are useful, but
measured evaluations show when examples improve quality and when they only
increase cost. This is the structured-data version of
[[llm-evaluation-workflows=>LLM evaluation workflows]].

Teams keep a known test set, compare outputs, and use measurements before
expanding the prompt
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

## Data Readiness Limits

Text-to-SQL can widen access to analysis, but it can't repair weak data
readiness. If ingestion is failing or upstream structures keep changing, the
assistant will surface the same problem faster. The same risk applies when SQL
logic is wrong or lineage is unclear.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

Reliability status should travel with the answer. A dashboard traffic-light
model can mark reliable data green, usable data with known issues yellow, and
broken or untrusted data red. That same reliability signal fits conversational BI
responses, especially when an analyst or automated scan has flagged a data
quality issue.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

Data readiness also has a product boundary. An imperfect assistant can be useful
when it creates measurable value and has a plan for improvement. Teams should
judge readiness by impact and user trust, not by the novelty of the LLM
interface.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

## Boundaries With BI, RAG, and Dashboards

Text-to-SQL, conversational BI, RAG, and dashboards solve adjacent but different
problems:

- Text-to-SQL turns a natural-language question into a structured query.
- Conversational BI covers the broader chat surface around dashboards, reports,
  metric definitions, summaries, and follow-up questions.
- Schema RAG retrieves table, column, catalog, dashboard, and example-query
  context before SQL generation.
- Governed metrics define the business meaning that the query should use.
- Dashboards remain the stable surface for repeated KPI reviews and shared
  operating rituals.

Text-to-SQL is strongest for exploratory follow-up questions and domain-expert
access. Dashboards remain stronger when the organization needs the same reviewed
KPI view every day. RAG supports the assistant by retrieving metadata, metric
definitions, dashboard notes, or approved examples before writing SQL
[[cite:urban-data-science=>Urban Data Science]]
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]].
Teams should treat text-to-SQL as one query path inside
[[ai-powered-business-intelligence=>AI in Business Intelligence]], not as the
whole BI system.

Each layer needs a different check
[[cite:production-ready-ai-engineering=>Production AI Engineering]]
[[cite:urban-data-science=>Urban Data Science]]:

- Retrieval needs quality checks for context.
- Generated SQL needs correctness checks for the query.
- Governed metrics need validity checks for business meaning.
- Access control needs exposure checks.
- Results need data quality checks.

## Related Pages

Text-to-SQL sits between BI semantics, data platform work, and LLM evaluation:
- [[Business Intelligence]]
- [[AI-Powered Business Intelligence]]
- [[Retrieval-Augmented Generation]]
- [[Data Products]]
- [[Data Engineering Platforms]]
- [[Data Quality and Observability]]
- [[LLM Evaluation Workflows]]
- [[Data Governance]]
- [[Analytics Engineering]]
- [[Metrics]]
