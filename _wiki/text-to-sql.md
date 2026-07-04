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
---

Text-to-SQL is a conversational interface for asking data questions in plain
language and turning them into SQL that can run against governed tables. It
belongs inside [[business-intelligence=>business intelligence]] rather than
outside it. The interface changes, but the answer still depends on trusted
[[metrics]] and modeled data. It also depends on metadata, permissions, and
review.

In urban transport policy, specialists may need answers from fare-card and
transport data without knowing SQL. A plain-language interface can help them
extract information and analyze policy questions.[[cite:urban-data-science=>Urban Data Science]]

## Working Definition

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

## Failure Modes and Controls

Conversational interfaces are useful only when the surrounding controls match
the failure mode. Metadata, prompt examples, and SQL command restrictions handle
query-generation risk. Evaluation datasets and expected outputs handle the cost
and quality tradeoff of adding more prompt examples. Data trust work handles KPI
definitions, ingestion failures, SQL logic, and lineage problems that a chat
interface can't fix.[[cite:urban-data-science=>Urban Data Science]][[cite:production-ready-ai-engineering=>Production AI Engineering]][[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

## Architecture Patterns

This boundary matters because text-to-SQL fails differently from document RAG.
A document assistant can cite the wrong source. A SQL assistant can join at the
wrong grain, miss a filter, or return a valid result for the wrong business
question.[[cite:urban-data-science=>Urban Data Science]]

Production AI practices still apply because prompt examples help the model
imitate the desired structure. Teams need evaluation data with inputs and
expected outputs to know when more examples stop improving the result and only
add cost.
For text-to-SQL, those examples are question-to-query pairs and expected result
checks.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

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

This puts text-to-SQL near [[data-governance=>data governance]] and
[[metrics]]. Business terms such as "sales", "active user", "trip", and
"student pass" can have more than one definition. The assistant should ask a
clarifying question or choose from governed definitions instead of guessing. The
schema context is part of the answer, not only a prompt prefix.

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

A text-to-SQL assistant can show dashboard-style reliability signals:

- green when the underlying data is reliable
- yellow when the data is under investigation
- red when the data isn't trustworthy enough for the requested decision

These labels keep the answer tied to the current state of the data.
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]]

## Boundaries With Dashboards and RAG

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

The two approaches often work together, but each layer needs its own check:

- retrieval quality for the context
- SQL correctness for the generated query
- data quality for the result

## Related Pages

For adjacent BI, governance, and production AI concepts, start with these pages.

- [[Business Intelligence]]
- [[AI-Powered Business Intelligence]]
- [[Retrieval-Augmented Generation]]
- [[LLM Production Patterns]]
- [[Metrics]]
- [[Data Governance]]
