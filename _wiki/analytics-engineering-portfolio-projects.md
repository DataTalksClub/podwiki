---
layout: wiki
title: "Analytics Engineering Portfolio Projects"
summary: "Archive-backed guidance for choosing analytics engineering portfolio projects that prove SQL modeling, metric definitions, dbt-style tests, documentation, BI readiness, and stakeholder judgment."
related:
  - Analytics Engineering
  - Data Engineering
  - Data Product Management
  - Job Search
  - Career Transition
---

## Definition and Scope

An analytics engineering portfolio project should turn messy source data into
trusted analytical models and usable metrics. The archive frames analytics
engineering as a bridge between data engineering and analysis. SQL, data
modeling, transformation workflows, tests, documentation, BI exposure, and
business definitions all matter.

Learners can use this page for dbt-style projects, metric-layer projects, and
dashboard-backed models. It also fits career-transition portfolios from
marketing, operations, finance, BI, or analyst work. For the role hub, use
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).


## Project Criteria

Good analytics engineering portfolio projects meet these criteria.

- Business question: start with a metric, funnel, cohort, finance process,
  operational workflow, or product decision.
- Source understanding: document event semantics, source systems, update
  cadence, schema owners, and known source defects.
- Modeled layers: separate sources, staging, intermediate, marts, and
  presentation models when the stack supports it.
- Metric definitions: define grain, dimensions, facts, measures, filters, and
  accepted business logic.
- Tests and docs: add non-null, unique, accepted-values, relationship,
  freshness, and custom tests. Include model and column documentation.
- BI readiness: expose the result through a dashboard, semantic layer, notebook,
  or documented query interface.
- Operational behavior: decide which failures block the build, which warn, who
  gets notified, and how duplicate definitions get deprecated.

## Project Types

Choose a project type that makes the analytics engineering role visible.

- Metric layer and dashboard project: pick a realistic domain such as
  subscriptions, ecommerce, marketing spend, SaaS usage, logistics, finance, or
  nonprofit operations. Build source models, staging tables, fact and dimension
  tables, KPI definitions, tests, docs, and a dashboard that uses only modeled
  data.
- dbt migration or refactor project: start with messy SQL scripts or duplicated
  dashboard queries. Refactor them into model layers, reusable macros, tests,
  docs, lineage, and a deployment workflow. Include a migration note that
  explains how stakeholders should validate changed numbers.
- Product analytics project: instrument or simulate events, define a tracking
  plan, model user journeys, and publish retention or activation metrics. Add
  event-quality checks and a note on how product teams would use the data.
- Reverse ETL or activation project: model a customer or account segment in the
  warehouse and push it to a mock CRM, support tool, or marketing destination.
  Document ownership, refresh cadence, privacy assumptions, and wrong-model
  consequences.

## Project Proof

Use this checklist as the project review standard.

1. Metric grain: state what one row represents and which joins preserve that
   grain.
2. Source semantics: name fields from user events, backend systems, ads
   platforms, finance tools, or manual inputs.
3. Transformation design: explain why models are layered this way and where
   business logic lives.
4. Tests: name enforced assumptions and warning-only checks.
5. Documentation: make owner, purpose, caveats, columns, dependencies, and
   examples findable by another analyst.
6. BI consumption: make the dashboard or query surface use shared models instead
   of embedded duplicate metric logic.
7. Stakeholder story: explain which decision the model supports and how to
   reconcile conflicting numbers.

## Episode Evidence

These episodes anchor the project criteria.

- [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html):
  at 4:05, Victoria Perez Mola describes data modeling, pipelines, data quality,
  and Looker as daily work. At 6:49, dbt adds SQL transformations, version
  control, docs, tests, and DAGs. At 38:53, she discusses dbt tests, upstream
  checks, warnings, and errors.
- [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html):
  at 9:53, the move into BI depends on SQL and data-pipeline understanding.
  At 14:14, the transition happens through BI projects alongside marketing work.
  Later sections cover dbt migration, wide versus narrow tables,
  incrementalization, product analytics, and domain knowledge.
- [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}):
  at 12:39, the episode connects dbt and SQL workflows to analyst autonomy.
  It also covers data marts, warehouses, orchestration, reverse data flows, CDC,
  and schema evolution.
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}):
  supports projects around event tracking, warehouse transformations, BI,
  reverse ETL, and team ownership for growth or product analytics.
- [Build a Data Engineering Career](https://datatalks.club/podcast.html):
  at 36:18, Jeff Katz uses dbt, Snowflake, Mode, and Fivetran as an analytics
  engineering module. At 44:21, SQL mastery and data modeling practice become
  interview-relevant skills.

## Anti-Patterns

Avoid these weak portfolio signals.

- A dashboard built directly from raw tables with metric logic hidden in charts.
- A dbt repository with many models but no docs, tests, owners, or business
  definitions.
- A project that copies a public template but cannot explain grain, joins,
  slowly changing dimensions, or incremental logic.
- Only showing final KPI values without source caveats, data-quality checks, or
  reconciliation notes.
- Treating analytics engineering as "SQL plus dashboard" while skipping version
  control, reviews, lineage, and deployment.

## Related Pages

Use these pages for adjacent project and role context.

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})
