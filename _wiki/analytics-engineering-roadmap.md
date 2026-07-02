---
layout: wiki
tags: ["roadmap"]
title: "Analytics Engineering Roadmap"
summary: "How DataTalks.Club guests describe analytics engineering: SQL modeling, dbt-style workflows, metric ownership, stakeholder trust, and the move from dashboards to governed analytical products."
related:
  - Analytics Engineering
  - Analytics Engineering Portfolio Projects
  - Marketing to Analytics Engineering
  - Modern Data Stack
  - Product Analytics
  - Metrics
  - Data Quality and Observability
  - Data Product Management
---

An analytics engineering roadmap should teach you to turn raw data into
trusted analytical models. It shouldn't become a tool checklist. In the
DataTalks.Club podcast discussions, the role sits between [[data engineering]]
and analytics.

You learn SQL and data modeling first, then add tests, documentation, and
metric ownership. Other people can then use the same business logic in
dashboards, experiments, product analytics, or activation.

[[person:victoriaperezmola|Victoria Perez Mola]]
describes the day-to-day job as modeling data and maintaining pipelines. She
also works on data quality and Looker-facing models
([[podcast:analytics-engineer-skills-tools|role episode at 4:14-6:49]]).
[[person:juanmanuelperafan|Juan Manuel Perafan]]
adds the roadmap principle: analytics engineering takes business reality and
makes data resemble it. The role then applies software-engineering rigor so the
models are testable and robust
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 11:03-18:35]]).

## Modeled Layer Ownership

Across these episodes, analytics engineering readiness means you can own the
modeled layer between raw data and decisions. A dashboard alone isn't enough.
You need to explain table grain, decide where logic belongs, test model
assumptions, and document definitions. Analysts and operators can then use
those modeled definitions for [[metrics]],
BI, [[product analytics]], and
sometimes [[data activation]].

Several guests converge on that definition. [[person:victoriaperezmola|Victoria Perez Mola]]
starts from SQL-based models, dbt documentation, and version control. She also
adds tests and a dependency graph
([[podcast:analytics-engineer-skills-tools|role episode at 5:47-10:04]]).
In the foundations episode, [[person:juanmanuelperafan|Juan Manuel Perafan]]
warns that defining the role only as "between analyst and engineer" misses the
point. The work is data modeling plus engineering practice
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 7:10-13:18]]).

[[person:nataliekwong|Natalie Kwong]] places the same
work inside ELT. Data is loaded into the warehouse first, and analysts or
analytics engineers then transform it with SQL and dbt-style workflows
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 7:57-15:30]]).

This ownership model connects the roadmap to [[Analytics Engineering]],
[[Data Analyst vs Analytics Engineer]],
[[dbt]], and [[Data Quality and Observability]].
The specific analyst transition path is
[[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]].

## Role Boundaries and Tool Choices

Guests differ on role boundaries and tool boundaries. [Victoria Perez
Mola](https://datatalks.club/people/victoriaperezmola.html) puts SQL, data
modeling, and quality checks at the center. Her examples use dbt, Snowflake,
and Looker. She also
notes that some company postings look closer to data engineering than analytics
engineering
([[podcast:analytics-engineer-skills-tools|role episode at 26:10-31:09]]).

[[person:juanmanuelperafan|Juan Manuel Perafan]] makes
the distinction more conceptual. dbt helps you practice data modeling,
stakeholder management, and engineering habits. Knowing dbt doesn't make
someone an analytics engineer
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 49:50-55:01]]).

They also differ on how much Python belongs near the beginning. [Victoria Perez
Mola](https://datatalks.club/people/victoriaperezmola.html) describes Python as
useful but not central in her Tier role. [[person:juanmanuelperafan|Juan Manuel Perafan]]
says most modeling work is still SQL. Python helps with adjacent work such as
ingestion and orchestration. It also helps with APIs, testing, and tool glue
([[podcast:analytics-engineer-skills-tools|role episode at 27:31-29:15]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 31:22-38:35]]).

For a learner, that disagreement leads to a practical sequence. Become
SQL-first and Python-aware, then add Python when ingestion or orchestration
requires it. API work and test automation may require it too.

## SQL and Modeling Roadmap

Start with analytical SQL and table meaning. You should be comfortable with
joins and aggregations, plus window functions and CTEs. You should also
understand dates, nulls, deduplication, and query debugging.

The guests don't frame SQL as syntax trivia. [Nikola
Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) had already taken
a SQL course when she moved toward BI. She then had to read and write more
complex company queries and understand how models fit into the wider pipeline
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 8:45-12:50]]).

Then learn data modeling for reuse. Your first modeling milestone is explaining
entities, facts, dimensions, and grain. You also need to explain duplicate
rows. [[person:victoriaperezmola|Victoria Perez Mola]]
names SQL, fact and dimension tables, Kimball-style modeling, and Snowflake
familiarity as core preparation
([[podcast:analytics-engineer-skills-tools|role episode at 26:10-29:15]]).
[[person:nikolamaksimovic|Nikola Maksimovic]] makes the
same step concrete through a dbt migration, domain model work, wide-versus-narrow
table decisions, and incrementalization tradeoffs
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 18:34-33:46]]).

The first roadmap milestone isn't "finish SQL." It's one source-to-mart model
where you can defend grain, keys, joins, and the business definition. That same
milestone becomes useful portfolio evidence when you show the model, tests,
documentation, and BI surface in an [[analytics-engineering-portfolio-projects|analytics engineering portfolio project]].

## dbt, Tests, and Review

After modeling basics, use version control and review so modeled data can change
without breaking downstream work. Dependency graphs show how models connect.
Model documentation and tests come next. [[person:victoriaperezmola|Victoria Perez Mola]]
explains dbt as SQL files with YAML documentation. She also names GitHub version
control, built-in tests, and DAG visibility
([[podcast:analytics-engineer-skills-tools|role episode at 6:49-10:04]]).

[[person:juanmanuelperafan|Juan Manuel Perafan]] extends
that into generic tests and singular SQL tests. He also covers unit tests and CI
checks that stop broken code from merging
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 38:41-45:09]]).

Use this stage to move from "can write SQL" to "can maintain shared analytical
code." [[dbt]] belongs on the roadmap without
becoming the whole roadmap because the useful skill is reviewable, tested
modeling.

## Stack Context and Activation

Learn enough of the surrounding [[modern data stack]]
to place your models. [[person:nataliekwong|Natalie Kwong]]
separates ingestion from data marts and explains why ELT gives analysts and
analytics engineers warehouse autonomy. She also ties dbt to orchestration,
governance, and reverse data flows
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 12:39-22:30]]).

[[person:adrianbrudaru|Adrian Brudaru]] adds a current
tool-selection caution. dbt shaped the workflow, but teams still need to choose
tools based on architecture and cost. Openness, orchestration needs, and
requirements matter too
([[podcast:trends-in-modern-data-engineering|trends episode at 31:29-45:56]]).

[[person:arpitchoudhury|Arpit Choudhury]] extends the
stack beyond BI. His data-led-growth discussion connects [[event tracking]]
and tracking plans to warehouse transforms, BI, and [[reverse ETL]].
Teams can then return modeled data to sales, support, marketing, or engagement tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode at 13:34-38:20]]).

## Portfolio Project Sequence

Build projects in the same order that DataTalks.Club guests describe the work
becoming more durable.

1. Model one metric from raw data to mart. Pick one domain, define the entities
   and grain, write the SQL, and document the metric definition. This matches
   [[person:victoriaperezmola|Victoria Perez Mola's]]
   description of building tables or views so analysts and data scientists can
   use the data
   ([[podcast:analytics-engineer-skills-tools|role episode at 4:14-5:47]]).
2. Turn repeated dashboard SQL into a dbt-style project. Add staging and
   intermediate layers, then publish marts. Document the project, add tests, and
   expose a dependency graph.
   [[person:nikolamaksimovic|Nikola Maksimovic]] learned
   data modeling through a dbt migration rather than by studying the tool in
   isolation
   ([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 18:34-23:12]]).
3. Prove dashboard trust. Break an upstream assumption, then show which test,
   warning, or documentation note catches it. [[person:victoriaperezmola|Victoria Perez Mola]]
   describes non-null checks, source checks, warning-versus-error behavior, and
   blocking downstream models when source data is wrong
   ([[podcast:analytics-engineer-skills-tools|role episode at 38:53-40:19]]).
4. Resolve a metric conflict. Model two competing definitions first. Then
   explain the stakeholder tradeoff and publish one governed version. [Juan Manuel
   Perafan](https://datatalks.club/people/juanmanuelperafan.html) frames analytics
   engineering as translating business reality into data. The model therefore
   has to encode the business decision, not only the join logic
   ([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 11:03-15:48]]).
5. Activate modeled data outside BI. Send a segment, lifecycle metric, or
   product event state to a sales, support, marketing, or engagement tool. [Arpit
   Choudhury](https://datatalks.club/people/arpitchoudhury.html) connects event
   tracking, warehouse transformations, BI analysis, and reverse ETL into one
   growth stack
   ([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode at 22:50-38:20]]).

These projects should produce [[analytics-engineering-portfolio-projects|portfolio evidence]]
that a hiring manager can look at. Show the model, its tests, and its docs.
Include lineage, a dashboard or semantic surface, and a short explanation of
the business question.

## Role Milestones

Entry-level readiness means you can write analytical SQL and explain grain. You
can also model one source-to-mart path, document columns, and add basic tests.
[[person:victoriaperezmola|Victoria Perez Mola]] names
SQL and data modeling as must-haves. [[person:nikolamaksimovic|Nikola Maksimovic]]
recommends Excel, SQL practice, and access to real BI queries. She also
recommends dashboard building as the early path
([[podcast:analytics-engineer-skills-tools|role episode at 42:05-45:16]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 41:50-45:09]]).

Mid-level readiness means you can own a domain model and handle source changes.
You can review SQL or dbt changes, align metric definitions with stakeholders,
and debug why two dashboards disagree. [[person:nikolamaksimovic|Nikola Maksimovic]]
describes this work through product-team support and A/B testing. Her examples
also include retention analysis and RFM analysis, plus a dbt migration and
modeling decisions
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 14:14-33:46]]).

Senior readiness means you can set modeling conventions, guide reviews, and
reduce duplicate definitions. You can negotiate upstream contracts with data
engineers and treat BI or semantic layers as product surfaces. [Juan Manuel
Perafan](https://datatalks.club/people/juanmanuelperafan.html) anchors that level
in robustness, testability, CI, and documentation. [[person:nataliekwong|Natalie Kwong]]
adds governance, orchestration, and reverse data flows as stack-level concerns
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 16:25-18:35 and 38:41-45:09]],
[[podcast:data-engineering-tools-modern-data-stack|modern stack episode at 21:22-22:30 and 35:42-39:06]]).

## Specialization Paths

Choose a specialization after you can build and test a small mart. Product
analytics is the most direct path if you like funnels and activation. It also
fits retention, experimentation, and event instrumentation. [[person:nikolamaksimovic|Nikola Maksimovic]]
worked with product managers on experiments and growth. She also worked on
retention and RFM analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 14:14 and 38:27-41:50]]).

[[person:arpitchoudhury|Arpit Choudhury]] shows the
same specialization from the data-led-growth side. His stack includes tracking
plans and events. It also includes warehouse transforms, product analytics, BI,
and reverse ETL
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode at 13:34-23:45]]).

Platform analytics engineering is the path if you prefer conventions and shared
models. It also fits repository work, CI, and orchestration. [[person:victoriaperezmola|Victoria Perez Mola]]
describes peer review, guidelines, tests, and quality practices for analysts and
data scientists
([[podcast:analytics-engineer-skills-tools|role episode at 45:16-49:09]]).

[[person:adrianbrudaru|Adrian Brudaru]] widens that path
with orchestration choices such as Airflow, Prefect, Dagster, and GitHub
Actions. He also adds tool-selection caution around the modern stack
([[podcast:trends-in-modern-data-engineering|trends episode at 35:37-45:56]]).

Data activation and data product work fit people who want modeled data to drive
operations, not only dashboards. [[person:arpitchoudhury|Arpit Choudhury]]
describes sending warehouse data back to support, sales, and engagement tools.
He also names the team split across data engineers, analysts, analytics
engineers, and product operations
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode at 30:03-51:40]]).
For analytics engineers, that path points toward [[Data Product Management]]
and [[Data Activation]].

## Study-Build Boundary

Stop studying and build once you can answer one business question with SQL,
name table grain, explain duplicate rows, and use Git. You also need to model
one source-to-mart path. DataTalks.Club guests consistently value applied proof.

[[person:nikolamaksimovic|Nikola Maksimovic]] moved by
using SQL, real BI queries, Looker, and dashboards. Small projects mattered
more than waiting to master every tool
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode at 41:50-45:09]]).

Keep studying when the next project exposes a real constraint. Common
constraints include incremental models and failing tests. They also include
unclear metric ownership, missing event properties, and freshness. Cost,
governance, and stakeholder disagreement belong here too.

[[person:juanmanuelperafan|Juan Manuel Perafan]]
argues for balancing tool knowledge with the concept. [[person:adrianbrudaru|Adrian Brudaru]]
warns against choosing tools without requirements, cost, and architecture in
mind
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode at 51:20-55:01]],
[[podcast:trends-in-modern-data-engineering|trends episode at 44:42-45:56]]).
The practical boundary is simple: learn enough to build the next reliable model,
then let the model reveal the next topic.

## Adjacent Analytics Engineering Paths

The roadmap intersects with role definition, project evidence, stack context,
and adjacent domains.

- [[Analytics Engineering]]
- [[Analytics Engineering Portfolio Projects]]
- [[Data Analyst vs Analytics Engineer]]
- [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
- [[Marketing to Analytics Engineering]]
- [[Modern Data Stack]]
- [[Product Analytics]]
- [[Event Tracking]]
- [[Metrics]]
- [[Data Quality and Observability]]
- [[Data Product Management]]
- [[Data Activation]]
