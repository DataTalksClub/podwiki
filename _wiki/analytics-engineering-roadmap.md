---
layout: wiki
title: "Analytics Engineering Roadmap"
summary: "A podcast-backed roadmap for analytics engineering: SQL modeling, dbt-style workflows, metric ownership, stakeholder trust, and the move from dashboards to governed analytical products."
related:
  - Analytics Engineering
  - Analytics Engineering Portfolio Projects
  - Data Analyst vs Analytics Engineer
  - Marketing to Analytics Engineering
  - Modern Data Stack
  - Product Analytics
  - Metrics
  - Data Quality and Observability
  - Data Product Management
---

An analytics engineering roadmap should teach you to turn raw data into
trusted analytical models, not only to collect tools. The DataTalks.Club archive
places the role between [data engineering]({{ '/wiki/data-engineering/' | relative_url }})
and analytics. In the stronger definition, you own modeled business data. That
means table grain, reusable SQL, tests, and documentation. It also means metric
definitions and BI or activation surfaces.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes the day-to-day job as modeling data and maintaining pipelines. She
also works on data quality and Looker-facing models
([role episode at 4:14-6:49]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
adds the roadmap principle. Analytics engineering takes business reality and
makes data resemble it. It then applies software-engineering rigor so the
result is testable and robust
([foundations episode at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Link Map

Use these pages alongside the roadmap:

- Role and boundary pages: [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}), [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}), and [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- Practice pages: [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }}), [dbt]({{ '/wiki/dbt/' | relative_url }}), [Metrics]({{ '/wiki/metrics/' | relative_url }}), and [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- Stack and domain pages: [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}), [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}), [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}), [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }}), [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}), and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- Adjacent article: [Analytics Engineer]({{ '/guides/analytics-engineer/' | relative_url }})

Core podcast discussions:

- [Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}) with [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) on modeling, dbt, tests, Looker, Snowflake, SQL, and role fit.
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}) with [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) on business reality, engineering rigor, SQL, Python, tests, CI, and dbt as a practice vehicle.
- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}) with [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) on a SQL-first career switch, Looker work, dbt migration, data modeling, product analytics, and mentorship.
- [ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) with [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) on ELT, warehouses, data marts, dbt, orchestration, governance, and reverse data flows.
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) with [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) on event tracking, tracking plans, warehouse transforms, BI, reverse ETL, and team responsibilities.
- [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}) with [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) on tool selection, dbt's influence, orchestration choices, and why SQL, Python, business requirements, and portfolio work still matter.

## Common Definition

Across the archive, analytics engineering readiness means you can own the
modeled layer between raw data and decisions. A dashboard alone isn't enough.
You need to explain table grain, decide where logic belongs, and test model
assumptions. You also need to document definitions and make the result usable by
analysts, product managers, executives, or operational tools.

Several guests converge on that definition. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
starts from SQL-based models, dbt documentation, and version control. She also
adds tests and a dependency graph
([role episode at 5:47-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
In the foundations episode, [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
warns that defining the role only as "between analyst and engineer" misses the
point. The work is data modeling plus engineering practice
([foundations episode at 7:10-13:18]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places the same
work inside ELT. Data is loaded into the warehouse first, and analysts or
analytics engineers then transform it with SQL and dbt-style workflows
([modern stack episode at 7:57-15:30]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Guest Differences

Guests differ on role boundaries and tool boundaries. [Victoria Perez
Mola]({{ '/people/victoriaperezmola/' | relative_url }}) puts SQL, data
modeling, and quality checks at the center. Her examples use dbt, Snowflake,
and Looker. She also
notes that some company postings look closer to data engineering than analytics
engineering
([role episode at 26:10-31:09]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) makes
the distinction more conceptual. dbt helps you practice data modeling,
stakeholder management, and engineering habits. Knowing dbt doesn't make
someone an analytics engineer
([foundations episode at 49:50-55:01]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

They also differ on how much Python belongs near the beginning. [Victoria Perez
Mola]({{ '/people/victoriaperezmola/' | relative_url }}) describes Python as
useful but not central in her Tier role. [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
says most modeling work is still SQL. Python helps with adjacent work such as
ingestion and orchestration. It also helps with APIs, testing, and tool glue
([role episode at 27:31-29:15]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[foundations episode at 31:22-38:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

The roadmap should therefore be SQL-first and Python-aware, not Python-first.

## Learning Sequence

Start with analytical SQL and table meaning. You should be comfortable with
joins and aggregations, plus window functions and CTEs. You should also
understand dates, nulls, deduplication, and query debugging.

The archive's emphasis isn't syntax trivia. [Nikola
Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) had already taken
a SQL course when she moved toward BI. She then had to read and write more
complex company queries and understand how models fit into the wider pipeline
([marketing transition episode at 8:45-12:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Then learn data modeling for reuse. Your first modeling milestone is explaining
entities, facts, dimensions, and grain. You also need to explain duplicate
rows. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
names SQL, fact and dimension tables, Kimball-style modeling, and Snowflake
familiarity as core preparation
([role episode at 26:10-29:15]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) makes the
same step concrete through a dbt migration, domain model work, wide-versus-narrow
table decisions, and incrementalization tradeoffs
([marketing transition episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

After modeling basics you can use version control and review. Dependency graphs
show how models connect. Model documentation and tests come next. [Victoria Perez
Mola]({{ '/people/victoriaperezmola/' | relative_url }}) explains dbt as SQL
files with YAML documentation. She also names GitHub version control, built-in
tests, and DAG visibility
([role episode at 6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) extends
that into generic tests and singular SQL tests. He also covers unit tests and CI
checks that stop broken code from merging
([foundations episode at 38:41-45:09]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Finally, learn enough of the surrounding stack to place your models. [Natalie
Kwong]({{ '/people/nataliekwong/' | relative_url }}) separates ingestion from
data marts and explains why ELT gives analysts and analytics engineers
warehouse autonomy. She also ties dbt to orchestration, governance, and reverse
data flows
([modern stack episode at 12:39-22:30]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) adds a current
tool-selection caution. dbt shaped the workflow, but teams still need to choose
tools based on architecture and cost. Openness, orchestration needs, and
requirements matter too
([trends episode at 31:29-45:56]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

## Project Sequence

Build projects in the same order the archive treats the work as becoming more
durable.

1. Model one metric from raw data to mart. Pick one domain, define the entities
   and grain, write the SQL, and document the metric definition. This matches
   [Victoria Perez Mola's]({{ '/people/victoriaperezmola/' | relative_url }})
   description of building tables or views so analysts and data scientists can
   use the data
   ([role episode at 4:14-5:47]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
2. Turn repeated dashboard SQL into a dbt-style project. Add staging and
   intermediate layers, then publish marts. Document the project, add tests, and
   expose a dependency graph.
   [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) learned
   data modeling through a dbt migration rather than by studying the tool in
   isolation
   ([marketing transition episode at 18:34-23:12]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
3. Prove dashboard trust. Break an upstream assumption, then show which test,
   warning, or documentation note catches it. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
   describes non-null checks, source checks, warning-versus-error behavior, and
   blocking downstream models when source data is wrong
   ([role episode at 38:53-40:19]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
4. Resolve a metric conflict. Model two competing definitions first. Then
   explain the stakeholder tradeoff and publish one governed version. [Juan Manuel
   Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) frames analytics
   engineering as translating business reality into data. The model therefore
   has to encode the business decision, not only the join logic
   ([foundations episode at 11:03-15:48]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
5. Activate modeled data outside BI. Send a segment, lifecycle metric, or
   product event state to a sales, support, marketing, or engagement tool. [Arpit
   Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) connects event
   tracking, warehouse transformations, BI analysis, and reverse ETL into one
   growth stack
   ([data-led growth episode at 22:50-38:20]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

These projects should produce [portfolio evidence]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
that a hiring manager can look at. Show the model, its tests, and its docs.
Include lineage, a dashboard or semantic surface, and a short explanation of
the business question.

## Role Milestones

Entry-level readiness means you can write analytical SQL and explain grain. You
can also model one source-to-mart path, document columns, and add basic tests.
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) names
SQL and data modeling as must-haves. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
recommends Excel, SQL practice, and access to real BI queries. She also
recommends dashboard building as the early path
([role episode at 42:05-45:16]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[marketing transition episode at 41:50-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Mid-level readiness means you can own a domain model and handle source changes.
You can review SQL or dbt changes, align metric definitions with stakeholders,
and debug why two dashboards disagree. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
describes this work through product-team support and A/B testing. Her examples
also include retention analysis and RFM analysis, plus a dbt migration and
modeling decisions
([marketing transition episode at 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Senior readiness means you can set modeling conventions, guide reviews, and
reduce duplicate definitions. You can negotiate upstream contracts with data
engineers and treat BI or semantic layers as product surfaces. [Juan Manuel
Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) anchors that level
in robustness, testability, CI, and documentation. [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
adds governance, orchestration, and reverse data flows as stack-level concerns
([foundations episode at 16:25-18:35 and 38:41-45:09]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[modern stack episode at 21:22-22:30 and 35:42-39:06]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Specialization Paths

Choose a specialization after you can build and test a small mart. Product
analytics is the most direct path if you like funnels and activation. It also
fits retention, experimentation, and event instrumentation. [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
worked with product managers on experiments and growth. She also worked on
retention and RFM analysis
([marketing transition episode at 14:14 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) shows the
same specialization from the data-led-growth side. His stack includes tracking
plans and events. It also includes warehouse transforms, product analytics, BI,
and reverse ETL
([data-led growth episode at 13:34-23:45]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Platform analytics engineering is the path if you prefer conventions and shared
models. It also fits repository work, CI, and orchestration. [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
describes peer review, guidelines, tests, and quality practices for analysts and
data scientists
([role episode at 45:16-49:09]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) widens that path
with orchestration choices such as Airflow, Prefect, Dagster, and GitHub
Actions. He also adds tool-selection caution around the modern stack
([trends episode at 35:37-45:56]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

Data activation and data product work fit people who want modeled data to drive
operations, not only dashboards. [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
describes sending warehouse data back to support, sales, and engagement tools.
He also names the team split across data engineers, analysts, analytics
engineers, and product operations
([data-led growth episode at 30:03-51:40]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
This connects the roadmap to [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
and [Data Activation]({{ '/wiki/data-activation/' | relative_url }}).

## Study-Build Boundary

Stop studying and build once you can answer one business question with SQL,
name table grain, explain duplicate rows, and use Git. You also need to model
one source-to-mart path. The archive consistently rewards applied proof.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) moved by
using SQL, real BI queries, Looker, and dashboards. Small projects mattered
more than waiting to master every tool
([marketing transition episode at 41:50-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Keep studying when the next project exposes a real constraint. Common
constraints include incremental models and failing tests. They also include
unclear metric ownership, missing event properties, and freshness. Cost,
governance, and stakeholder disagreement belong here too.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
argues for balancing tool knowledge with the concept. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
warns against choosing tools without requirements, cost, and architecture in
mind
([foundations episode at 51:20-55:01]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[trends episode at 44:42-45:56]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).
The practical boundary is simple: learn enough to build the next reliable model,
then let the model reveal the next topic.

## Related Pages

Use these pages for the role, stack, projects, and adjacent domains.

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Analytics Engineer article]({{ '/guides/analytics-engineer/' | relative_url }})
