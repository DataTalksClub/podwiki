---
layout: wiki
title: "Text-to-SQL"
summary: "Podcast takeaways on text-to-SQL, metadata, governed metrics, query safety, and production testing for conversational BI."
related:
  - Business Intelligence
  - AI-Powered Business Intelligence
  - Retrieval-Augmented Generation
  - LLM Production Patterns
  - Metrics
  - Data Governance
  - Analytics Engineering Roadmap
---

Text-to-SQL is a conversational interface for asking data questions in plain
language and turning them into SQL that can run against governed tables. It
belongs inside [[business-intelligence=>business intelligence]] and
[[ai-powered-business-intelligence=>AI-powered BI]], not outside them. The
interface changes, but the answer still depends on trusted [[metrics]] and
modeled data. It also needs metadata, permissions, and review.

Urban transport specialists may need answers from fare-card and transport data
without knowing SQL. A plain-language interface can help them extract
information and analyze policy questions.[[cite:urban-data-science=>Urban Data Science]]
That makes text-to-SQL useful for domain experts. It doesn't remove the BI work
around definitions, dashboards, data quality, and trust.

## Structured Questions Over Governed Tables

Text-to-SQL combines a natural-language question, schema context, and a SQL
generation step. In the urban data example, metadata from data warehouses and
catalogs is chunked, stored in a vector database, and supplied to an LLM. The
model uses that context to translate a plain-English question into SQL and
return the result.[[cite:urban-data-science=>Urban Data Science]]

That makes text-to-SQL a narrow form of
[[retrieval-augmented-generation=>retrieval-augmented generation]]. RAG supplies
the table and column context before the model writes SQL. The generated query
then behaves like a tool call against structured data, not like a summary over
retrieved text.

Text-to-SQL is narrower than conversational BI. A conversational BI assistant
may explain a dashboard or find a metric definition. It may also summarize a
report or route someone to a governed view. A text-to-SQL assistant has one
sharper job. It turns a question into a query, runs it safely, and exposes
enough context for someone to trust or reject the result.

## Architecture Boundaries and Failure Modes

The episodes draw different boundaries around the same idea. Rachel Lim draws
the application boundary around policy specialists asking about fare-card
behavior, concession cards, monthly passes, and transport pricing without
writing SQL. That puts text-to-SQL close to public-sector analytics and
domain-specific decision support.[[cite:urban-data-science=>Urban Data Science]]

Bartosz Mikulski frames the problem as production AI engineering. More prompt
examples can help, but teams still need evaluation data with inputs and
expected outputs. That data shows when extra examples stop improving quality.
After that point, more examples only add cost.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Lior Barak draws the trust boundary around the data product. If a core KPI
dashboard is unreliable, a chat interface will spread the same confusion
faster. The cause might be failed ingestion, wrong SQL logic, or unclear
lineage. A traffic light on the dashboard can tell leaders whether data is
reliable, usable with known issues, or broken.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

Together, these boundaries put text-to-SQL in a practical role because it helps
people reach data. [[data-governance=>Data governance]], metric ownership,
tests, and dashboard reliability decide whether people can use the answer.

## From Question to Query

Rachel's transport example shows the core flow. A policy specialist asks a
plain-English question about fare-card data. The system retrieves metadata from
warehouses and catalogs, uses it as RAG context, asks the LLM to write SQL, and
returns the output.[[cite:urban-data-science=>Urban Data Science]]

This differs from document RAG. A document assistant may retrieve the wrong
passage or summarize a source incorrectly. A SQL assistant can join at the
wrong grain or miss a filter. It can also pick the wrong table or return a
valid number for the wrong business question.[[cite:urban-data-science=>Urban Data Science]]

For text-to-SQL, production evaluation should include question-to-query pairs
and expected outputs. It should also include result checks because prompt
examples only teach the model the desired query style. Evaluation data tells
the team whether that style still works after schema changes, model changes, or
prompt edits.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

## Metadata and Schema Context

Text-to-SQL needs more than table names because the transport policy example
depends on domain context. Fare-card records, concession cards, and monthly
passes matter. Journey rules and policy questions about pricing or public
transport use also affect the query. The same words can refer to cards, people,
or trips. They can also refer to routes or revenue measures depending on the
question.[[cite:urban-data-science=>Urban Data Science]]

Metadata should explain what a table means and who owns it. It should also name
the grain, safe columns, valid joins, and governed definitions. A catalog or
warehouse schema can tell the model that a table exists. Domain metadata tells
it whether that table can answer a question such as "How many students use
monthly passes?"

Schema RAG is a supporting layer, not the answer. It retrieves table names and
column descriptions, plus join hints. It can also retrieve dashboard notes and
example queries so the model can write a better query. The answer still comes
from the structured query against the data warehouse or modeled BI tables.

This puts text-to-SQL near [[data-governance=>data governance]],
[[metrics]], and [[analytics-engineering-roadmap=>analytics engineering]].
Business terms such as "sales", "active user", "trip", and "student pass" can
have more than one definition. The assistant should ask a clarifying question
or choose from governed definitions instead of guessing. The schema context is
part of the answer, not only a prompt prefix.

## Governed Metrics and BI Semantics

Text-to-SQL shouldn't make every raw table equally available for every
question. When the question is about a governed KPI, the assistant should prefer
trusted BI assets. Those assets might be a modeled table, metric definition,
dashboard query, or semantic layer. That matches Lior's warning: leaders lose
trust when the same KPI needs a separate validation chain before they can use
it.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

The governed-metrics boundary also keeps text-to-SQL from becoming a parallel
BI stack. If the assistant invents its own definition of revenue or active
users, it competes with dashboards and metric ownership. The same problem
applies to transport journeys. If it uses the governed definition, it becomes
another access path to the same BI product. It should show the query, filters,
grain, and source tables.

For ambiguous questions, the safer response is a clarification, not a guess.
"Students using monthly passes" could mean cards, people, tap-in events, or
completed journeys. It could also mean revenue impact. Rachel's fare-card
example makes that domain context part of the question, not decoration around
it.[[cite:urban-data-science=>Urban Data Science]]

## Query Safety and Reliability

Analysis assistants shouldn't modify the database. Text-to-SQL systems can
restrict commands such as `insert`, `update`, and
`delete`.[[cite:urban-data-science=>Urban Data Science]] A safer BI assistant
should also inherit the requester's access. It should avoid unrestricted
raw-record exposure and show the query, filters, assumptions, and source tables
before people rely on the result.

Reliability also depends on the data pipeline behind the query. Pipeline tests
make BI behavior easier to trust through snapshot tests and integration-style
checks. Teams can also use Great Expectations, Soda, SQL checks, and test
tables.
[[cite:production-ready-ai-engineering=>Production AI Engineering]]

For text-to-SQL, those checks need to cover both sides of the system. The data
tables need quality checks, and the generated SQL needs evaluation against
known questions and expected outputs. A syntactically valid query isn't enough
when the question depends on business definitions, aggregation grain, or access
rules.

## BI and Data Readiness

Conversational access works best when the BI layer already has usable data. A
core KPI dashboard shouldn't require management to check every day whether the
numbers are accurate enough for decisions. Revenue, sales, stock availability,
and other KPI values lose value when leaders need a separate validation chain
before using them.[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

That warning applies directly to text-to-SQL. A chat interface can make broken
or ambiguous data easier to ask about, but it can't make the answer trustworthy.
When ingestion fails or SQL logic is wrong, the assistant spreads the same
confusion faster. Unclear lineage and conflicting KPI values create the same
problem.
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

A text-to-SQL assistant can include dashboard-style reliability signals in the
answer:

- green when the underlying data is reliable
- yellow when the data is under investigation
- red when the data isn't trustworthy enough for the requested decision

These labels keep the answer tied to the current state of the data.
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

## Boundaries With Conversational BI, RAG, and Dashboards

These layers solve different parts of the same access problem:

- Text-to-SQL turns a natural-language question into a structured query.
- Conversational BI handles the broader chat surface around reports, dashboards,
  metric definitions, and follow-up questions.
- Schema RAG retrieves table, column, catalog, dashboard, and example-query
  context before SQL generation.
- Governed metrics define which business meaning the query should use.
- Dashboards keep repeated KPI reviews and shared operating rituals stable.

Text-to-SQL shouldn't replace every dashboard. Dashboards still fit repeated
KPI reviews, shared operating rituals, and executive reporting, especially when
people need the same metric status every day. The core KPI example keeps the
dashboard as a trust and communication surface, not only a visual query result.
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

Text-to-SQL is strongest for follow-up questions, exploratory breakdowns, and
access for domain experts who know the policy or business problem but not the
schema. In the fare-card example, a policy specialist can ask about student or
senior-citizen pass usage without routing every question through a data
engineer.[[cite:urban-data-science=>Urban Data Science]]

RAG has a different boundary because it retrieves metric definitions and table
documentation. It can also retrieve catalog entries, dashboard notes, and prior
analysis. Use text-to-SQL when the answer requires a fresh structured query.
Use a dashboard when the answer should be the same reviewed KPI view every day.
Use a conversational BI assistant when the first task is navigation,
explanation, or follow-up around existing BI assets.

The layers often work together, but each layer needs its own check:

- retrieval quality for the context
- SQL correctness for the generated query
- metric validity for the business definition
- data quality for the result

## Related Pages

For adjacent BI, governance, and production AI concepts, start with these pages.

- [[Business Intelligence]]
- [[AI-Powered Business Intelligence]]
- [[Retrieval-Augmented Generation]]
- [[LLM Production Patterns]]
- [[Metrics]]
- [[Data Governance]]
- [[Analytics Engineering Roadmap]]
