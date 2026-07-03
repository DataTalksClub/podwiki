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
language and turning them into SQL that can run against governed tables. In the
podcast discussions, it sits inside
[[business-intelligence=>business intelligence]]
rather than outside it. The interface changes, but the answer still depends on
trusted [[metrics]] and modeled data. It also
needs metadata, permissions, and review.

[[person:rachellim=>Rachel Lim]] gives the most direct
example in her urban data science episode. Policy specialists may need answers
from fare-card and transport data but not know SQL. Her team is exploring a
plain-language tool to help them extract information and analyze data
[[cite:urban-data-science|Urban Data Science]].

## Architecture Patterns

Rachel describes the core architecture as metadata retrieval plus SQL
generation. The system uses metadata from data warehouses and data catalogs,
chunks that information, stores it in a vector database, and puts an LLM on top.
The LLM takes a plain-English question, translates it into SQL, and returns the
result to the requester [[cite:urban-data-science|Urban Data Science]].

That makes text-to-SQL a narrow form of
[[retrieval-augmented-generation=>RAG]].
RAG supplies the table and column context before the model writes SQL. The
generated query then acts as a tool call against structured data, not as a
summary over retrieved text.

This boundary matters because the failure modes are different. A RAG answer can
cite the wrong document, whereas text-to-SQL can join the wrong table grain or
miss a filter. It can also return a valid result for the wrong business
question.

Production AI concerns still apply. [[person:bartoszmikulski=>Bartosz Mikulski]]
connects prompt work to examples, expected outputs, and evaluation datasets. For
text-to-SQL, examples of good question-to-query pairs help the model follow the
desired structure. Teams still need tests to learn when more examples stop
improving the output and only increase cost
[[cite:production-ready-ai-engineering|Production AI Engineering]].

## Metadata and Schema Context

Text-to-SQL needs more than table names because Rachel's transport example
depends on domain context.

In the episode, that context includes:

- fare-card records and concession cards
- monthly passes for students and senior citizens
- journey logic
- policy questions about pricing or public transport use

These concepts determine whether the generated SQL answers the intended question
[[cite:urban-data-science|Urban Data Science]].

Metadata should explain what a table means and who owns it. It should also name
the grain, safe columns, and valid joins. A catalog or warehouse schema can tell
the model that a table exists. Domain metadata tells it whether the table
answers "How many students use monthly passes?" or a different question about
trips and cards rather than people, routes, or revenue measures.

This puts text-to-SQL near [[data-governance=>data governance]]
and [[metrics]]. Business terms such as "sales",
"active user", "trip", and "student pass" can have more than one definition.
The assistant should ask a clarifying question or choose from governed
definitions instead of guessing. The schema context is part of the answer, not
only a prompt prefix.

## Query Safety and Reliability

Rachel says teams should restrict write commands so the assistant can't modify
the database when people only asked for analysis. She names `insert`, `update`,
and `delete` as examples [[cite:urban-data-science|Urban Data Science]].
Beyond that, a safer BI assistant should inherit the requester's access and
avoid unrestricted raw-record exposure. It should show the query, filters,
assumptions, and source tables before people rely on the result.

Reliability also depends on the data pipeline behind the query. Bartosz's
testing discussion starts from a familiar BI failure: someone says a dashboard
number doesn't look correct, and the team loses trust. His response is to make
pipeline behavior testable through snapshot and integration-style tests. Teams
can also use Great Expectations, Soda, SQL checks, and test tables
[[cite:production-ready-ai-engineering|Production AI Engineering]].

For text-to-SQL, those checks need to cover both sides of the system. The data
tables need quality checks, and the generated SQL needs evaluation against
known questions and expected outputs. A syntactically valid query isn't enough
when the question depends on business definitions, aggregation grain, or access
rules.

## BI and Data Readiness

Conversational access works best when the BI layer already has usable data.
[[person:liorbarak=>Lior Barak]] frames the core risk as data trust. Teams may
have governance and monitoring tools, yet business users still don't trust the
numbers. He uses the core KPI dashboard example to show how trust breaks when
management has to check KPI accuracy. In his example, those KPIs include
revenue, sales, and stock
[[cite:mindful-data-strategy-for-business-impact|Mindful Data Strategy]].

That warning applies directly to text-to-SQL. A chat interface can make broken
or ambiguous data easier to ask about, but it can't make the answer
trustworthy. When ingestion fails or SQL logic is wrong, the assistant will
spread the same confusion faster. Unclear lineage or conflicting KPI values
create the same problem
[[cite:mindful-data-strategy-for-business-impact|Mindful Data Strategy]].

Lior's reliability signals fit conversational BI well. A dashboard can show
green, yellow, or red status for data reliability.

A text-to-SQL assistant can use the same idea:

- green when the underlying data is reliable
- yellow when the data is under investigation
- red when the data isn't trustworthy enough for the requested decision

These status labels keep the answer tied to the state of the data
[[cite:mindful-data-strategy-for-business-impact|Mindful Data Strategy]].

## Boundaries With Dashboards and RAG

Text-to-SQL shouldn't replace every dashboard. Dashboards still fit repeated
KPI reviews, shared operating rituals, and executive reporting, especially when
people need the same metric status every day. Lior's core KPI example shows why
the dashboard remains a trust and communication surface, not only a visual
query result [[cite:mindful-data-strategy-for-business-impact|Mindful Data Strategy]].

Text-to-SQL is strongest for follow-up questions, exploratory breakdowns, and access
for domain experts who know the policy or business problem but not the schema.
Rachel's fare-card example fits that case. A policy specialist can ask about
student or senior-citizen pass usage without routing every question through a
data engineer [[cite:urban-data-science|Urban Data Science]].

RAG has a different boundary because it retrieves metric definitions and table
documentation. It can also retrieve catalog entries, dashboard notes, and prior
analysis. Use text-to-SQL when the answer requires a fresh structured query.

The two approaches often work together, but teams should evaluate each layer:

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
