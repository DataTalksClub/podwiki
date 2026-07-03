---
layout: wiki
tags: ["roadmap"]
title: "Analytics Engineering Roadmap"
summary: "A podcast-grounded roadmap for analytics engineering: SQL modeling, dbt workflows, metric ownership, quality checks, and trusted analytics products."
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
trusted analytical models, not become a tool checklist. The role sits between
[[data engineering]] and analytics.

You learn SQL and data modeling first, then add tests, documentation, and
metric ownership. Other people can then use the same business logic in
dashboards, experiments, product analytics, or activation.

The day-to-day job is modeling data and maintaining pipelines. It also includes
data quality work and Looker-facing models
([[podcast:analytics-engineer-skills-tools|role episode]]).
Analytics engineering turns business reality into data models. It then applies
software-engineering rigor so the models are testable and robust
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]]).

## Modeled Layer Ownership

Readiness means you can own the modeled layer between raw data and decisions. A
dashboard alone isn't enough. You need to explain table grain, decide where
logic belongs, test model assumptions, and document definitions. Analysts and
operators can then use those modeled definitions for
[[metrics]], BI,
[[product analytics]], and
sometimes [[data activation]].

The core work combines SQL-based models and dbt documentation. It also includes
version control, tests, and a dependency graph
([[podcast:analytics-engineer-skills-tools|role episode]]).
Defining the role only as "between analyst and engineer" misses the point: the
work is data modeling plus engineering practice
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]]).
The same work lives inside ELT: data is loaded into the warehouse first, then
transformed with SQL and dbt-style workflows
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode]]).

This ownership model connects the roadmap to
[[Analytics Engineering]],
[[Data Analyst vs Analytics Engineer]],
[[dbt]], and
[[Data Quality and Observability]].
The specific analyst transition path is
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]].

## Role Boundaries and Tool Choices

Role and tool boundaries are contested. One view puts SQL, data modeling, and
quality checks at the center. It treats dbt, Snowflake, and Looker as examples,
while noting that some job postings look closer to data engineering than
analytics engineering
([[podcast:analytics-engineer-skills-tools|role episode]]).
A more conceptual view says dbt helps you practice data modeling, stakeholder
management, and engineering habits. Knowing dbt alone doesn't make someone an
analytics engineer
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]]).

How much Python belongs near the beginning also differs. Python is useful but
not central because most modeling work is still SQL. It helps with ingestion and
orchestration. It also helps with APIs, testing, and tool glue
([[podcast:analytics-engineer-skills-tools|role episode]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>foundations episode]]).

For a learner, that disagreement leads to a practical sequence. Become
SQL-first and Python-aware. Add Python when ingestion or orchestration requires
it. Add it for API work or test automation too.

## SQL and Modeling Roadmap

Start with analytical SQL and table meaning. You should be comfortable with
joins, aggregations, window functions, and CTEs. You should also understand
dates, nulls, deduplication, and query debugging.

SQL isn't syntax trivia because a completed SQL course was only the start. The
next step was reading company queries and understanding how models fit into the
wider pipeline
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).

Then learn data modeling for reuse. The first modeling milestone is explaining
entities, facts, and dimensions. It also means explaining grain and duplicate
rows.

Core preparation covers SQL, fact tables, and dimension tables. It also covers
Kimball-style modeling and Snowflake familiarity
([[podcast:analytics-engineer-skills-tools|role episode]]).
A dbt migration turns that preparation into domain modeling. The work includes
wide-versus-narrow table decisions and incrementalization tradeoffs
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).

The first roadmap milestone isn't "finish SQL." It's one source-to-mart model
where you can defend grain, keys, joins, and the business definition. That same
milestone becomes useful portfolio evidence when you show the model, tests,
documentation, and BI surface in an
[[analytics-engineering-portfolio-projects=>analytics engineering portfolio project]].

## dbt, Tests, and Review

After modeling basics, use version control and review so modeled data can change
without breaking downstream work. Dependency graphs show how models connect.
Model documentation and tests come next. dbt is SQL files with YAML
documentation, GitHub version control, built-in tests, and DAG visibility
([[podcast:analytics-engineer-skills-tools|role episode]]).
That extends into generic tests, singular SQL tests, unit tests, and CI checks
that stop broken code from merging
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]]).

Use this stage to move from "can write SQL" to "can maintain shared analytical
code." [[dbt]] belongs on the roadmap without
becoming the whole roadmap, because the useful skill is reviewable, tested
modeling.

## Stack Context and Activation

Learn enough of the surrounding [[modern data stack]]
to place your models. ELT separates ingestion from data marts and gives analysts
and analytics engineers warehouse autonomy. That ties dbt to orchestration,
governance, and reverse data flows
([[podcast:data-engineering-tools-modern-data-stack|modern stack episode]]).

A tool-selection caution applies because dbt shaped the workflow, but teams
still need to choose tools based on architecture, cost, and openness.
Orchestration needs and requirements matter too
([[podcast:trends-in-modern-data-engineering|trends episode]]).

The stack extends beyond BI.
[[event tracking]] and tracking plans
connect to warehouse transforms and BI.
[[reverse ETL]] returns modeled data to sales, support, marketing, or
engagement tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).

## Portfolio Project Sequence

Build projects in the order the work becomes more durable.

1. Model one metric from raw data to mart. Pick one domain, define the entities
   and grain, write the SQL, and document the metric definition. This matches
   building tables or views so analysts and data scientists can use the data
   ([[podcast:analytics-engineer-skills-tools|role episode]]).
2. Turn repeated dashboard SQL into a dbt-style project. Add staging and
   intermediate layers, then publish marts. Document the project, add tests, and
   expose a dependency graph. Data modeling is best learned through a dbt
   migration rather than by studying the tool in isolation
   ([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).
3. Prove dashboard trust. Break an upstream assumption, then show which test,
   warning, or documentation note catches it. Use non-null checks, source
   checks, warning-versus-error behavior, and blocked downstream models when
   source data is wrong
   ([[podcast:analytics-engineer-skills-tools|role episode]]).
4. Resolve a metric conflict. Model two competing definitions first, then
   explain the stakeholder tradeoff and publish one governed version. Analytics
   engineering translates business reality into data, so the model has to encode
   the business decision, not only the join logic
   ([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]]).
5. Activate modeled data outside BI. Send a segment, lifecycle metric, or
   product event state to a sales, support, marketing, or engagement tool. Event
   tracking, warehouse transformations, BI analysis, and reverse ETL form one
   growth stack
   ([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).

These projects should produce
[[analytics-engineering-portfolio-projects=>portfolio evidence]]
a hiring manager can look at. Show the model, tests, docs, and lineage. Include
a dashboard or semantic surface and a short explanation of the business
question.

## Role Milestones

Entry-level readiness means you can write analytical SQL and explain grain. You
can model one source-to-mart path, document columns, and add basic tests. SQL
and data modeling are must-haves. Excel, SQL practice, and access to real BI
queries form the early path. Dashboard building belongs there too
([[podcast:analytics-engineer-skills-tools|role episode]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>marketing transition episode]]).

Mid-level readiness means you can own a domain model and handle source changes.
You can review SQL or dbt changes and align metric definitions with
stakeholders. You can also debug why two dashboards disagree. This shows up
through product-team support, A/B testing, retention analysis, and RFM analysis.
A dbt migration with modeling decisions is another signal
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).

Senior readiness means you can set modeling conventions, guide reviews, reduce
duplicate definitions, and negotiate upstream contracts with data engineers. You
can also treat BI or semantic layers as product surfaces. That level is anchored
in robustness, testability, CI, and documentation. Governance, orchestration,
and reverse data flows become stack-level concerns
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]],
[[podcast:data-engineering-tools-modern-data-stack=>modern stack episode]]).

## Specialization Paths

Choose a specialization after you can build and test a small mart. Product
analytics is the most direct path if you like funnels and activation. It fits
retention, experimentation, and event instrumentation. The work often happens
with product managers on experiments, growth, retention, and RFM analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).

The data-led-growth side shows the same specialization through tracking plans,
events, and warehouse transforms. Product analytics, BI, and reverse ETL
complete the loop
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).

Platform analytics engineering is the path if you prefer conventions and shared
models. It centers on repository work, CI, and orchestration. Peer review,
guidelines, tests, and quality practices support analysts and data scientists
([[podcast:analytics-engineer-skills-tools|role episode]]).

That path widens with orchestration choices such as Airflow and Prefect. Dagster
and GitHub Actions can sit in the same decision set. Tool-selection caution
around the modern stack still applies
([[podcast:trends-in-modern-data-engineering|trends episode]]).

Data activation and data product work fit people who want modeled data to drive
operations, not only dashboards. The work sends warehouse data back to support,
sales, and engagement tools. Teams may split the work across data engineers,
analysts, analytics engineers, and product operations
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).
For analytics engineers, that path points toward
[[Data Product Management]]
and [[Data Activation]].

## Study-Build Boundary

Stop studying and build once you can answer one business question with SQL. You
should be able to name table grain, explain duplicate rows, use Git, and model
one source-to-mart path. The proof has to be applied. Progress comes from using
SQL, real BI queries, Looker, and dashboards. Small projects matter more than
waiting to master every tool
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|marketing transition episode]]).

Keep studying when the next project exposes a real constraint. Common
constraints include incremental models, failing tests, and unclear metric
ownership. Missing event properties and freshness count too. Cost, governance,
and stakeholder disagreement also matter.

Balance tool knowledge with the concept. Avoid choosing tools without
requirements, cost, and architecture in mind
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|foundations episode]],
[[podcast:trends-in-modern-data-engineering=>trends episode]]).

The practical boundary is simple: learn enough to build the next reliable model,
then let the model reveal the next topic.

## Adjacent Analytics Engineering Paths

The roadmap intersects with role definition, project evidence, stack context,
and adjacent domains.

- [[Analytics Engineering]]
- [[Analytics Engineering Portfolio Projects]]
- [[Data Analyst vs Analytics Engineer]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
- [[Marketing to Analytics Engineering]]
- [[Modern Data Stack]]
- [[Product Analytics]]
- [[Event Tracking]]
- [[Metrics]]
- [[Data Quality and Observability]]
- [[Data Product Management]]
- [[Data Activation]]
