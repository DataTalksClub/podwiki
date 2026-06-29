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

An analytics engineering portfolio project should prove that the learner can
turn messy source data into trusted analytical models and usable metrics. The
archive frames analytics engineering as a bridge between data engineering and
analysis: SQL, data modeling, transformation workflows, tests, documentation,
BI exposure, and business definitions all matter.

Use this page for dbt-style projects, metric-layer projects, dashboard-backed
models, and career-transition portfolios from marketing, operations, finance,
BI, or analyst work. For the role hub, use
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

## Contents

- [Project Criteria](#project-criteria)
- [Project Shapes](#project-shapes)
- [What the Project Should Demonstrate](#what-the-project-should-demonstrate)
- [Episode Evidence](#episode-evidence)
- [Anti-Patterns](#anti-patterns)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Project Criteria

Good analytics engineering portfolio projects meet these criteria:

- **Business question**: Start with a metric, funnel, cohort, finance process,
  operational workflow, or product decision.
- **Source understanding**: Document event semantics, source systems, update
  cadence, schema owners, and known source defects.
- **Modeled layers**: Separate sources, staging, intermediate, marts, and
  presentation models when the project stack supports it.
- **Metric definitions**: Define grain, dimensions, facts, measures, filters,
  and accepted business logic.
- **Tests and docs**: Add non-null, unique, accepted-values, relationship,
  freshness, and custom tests, plus model and column documentation.
- **BI readiness**: Expose the result through a dashboard, semantic layer,
  notebook, or documented query interface.
- **Operational behavior**: Decide which failures block the build, which warn,
  who gets notified, and how duplicate definitions get deprecated.

## Project Shapes

### Metric Layer and Dashboard Project

Pick a realistic domain such as subscriptions, ecommerce, marketing spend,
SaaS usage, logistics, finance, or nonprofit operations. Build source models,
staging tables, fact and dimension tables, KPI definitions, tests, docs, and a
dashboard that uses only modeled data.

The key evidence is not the chart. It is the path from source semantics to a
trusted metric.

### dbt Migration or Refactor Project

Start with messy SQL scripts or duplicated dashboard queries, then refactor them
into a dbt-style project with model layers, reusable macros, tests, docs,
lineage, and a deployment workflow. Include a migration note that explains what
changed and how stakeholders should validate the numbers.

This mirrors archive episodes where analytics engineering becomes visible
through dbt, version control, tests, DAGs, and documentation.

### Product Analytics Project

Instrument or simulate events, define a tracking plan, model user journeys, and
publish retention, activation, funnel, or experiment-readiness metrics. Include
event-quality checks and a note on how product and analytics teams would use the
data.

This shape fits learners with marketing, product, growth, or operations
backgrounds because domain knowledge becomes part of the evidence.

### Reverse ETL or Activation Project

Model a customer or account segment in the warehouse and push it to a mock CRM,
support tool, or marketing destination. Document ownership, refresh cadence,
privacy assumptions, and what happens if the model is wrong.

This project proves that analytics engineering can support operations, not only
dashboards.

## What the Project Should Demonstrate

Use this checklist as the project review standard:

1. **Metric grain**: What does one row represent, and which joins preserve that
   grain?
2. **Source semantics**: Which fields come from user events, backend systems,
   ads platforms, finance tools, or manual inputs?
3. **Transformation design**: Why are models layered this way, and where does
   business logic live?
4. **Tests**: Which assumptions are enforced, and what is warning-only versus
   build-blocking?
5. **Documentation**: Can another analyst find owner, purpose, caveats, columns,
   dependencies, and examples?
6. **BI consumption**: Does the dashboard or query surface use shared models
   instead of embedding duplicate metric logic?
7. **Stakeholder story**: Which decision does the model support, and how would
   the learner reconcile conflicting numbers?

## Episode Evidence

| Episode | Portfolio Evidence |
| --- | --- |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | At 4:05, Victoria Perez Mola describes data modeling, pipelines, data quality, and Looker as daily work. At 6:49, dbt adds SQL transformations, version control, docs, tests, and DAGs. At 38:53, she discusses dbt tests, upstream checks, warnings, and errors. |
| [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html) | At 9:53, the move into BI depends on SQL and data-pipeline understanding. At 14:14, the transition happens through BI projects alongside marketing work. Later sections cover dbt migration, wide versus narrow tables, incrementalization, product analytics, and domain knowledge. |
| [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) | At 12:39, the episode connects dbt and SQL workflows to analyst autonomy. It also covers data marts, warehouses, orchestration, reverse data flows, CDC, and schema evolution. |
| [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) | Supports projects around event tracking, warehouse transformations, BI, reverse ETL, and team ownership for growth or product analytics. |
| [Build a Data Engineering Career](https://datatalks.club/podcast.html) | At 36:18, Jeff Katz uses dbt, Snowflake, Mode, and Fivetran as an analytics engineering module. At 44:21, SQL mastery and data modeling practice become interview-relevant skills. |

## Anti-Patterns

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

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/analytics-engineer-skills-tools.md`,
  `../datatalksclub.github.io/_podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`,
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`,
  `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`,
  and `../datatalksclub.github.io/_podcast/data-engineering-career-path-and-skills.md`.
- Future expansion should add concrete example rubrics for metric-layer,
  product-analytics, finance, and reverse-ETL projects.
- Keep this page portfolio-focused. The full role synthesis belongs in
  [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
