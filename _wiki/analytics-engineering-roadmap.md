---
layout: wiki
title: "Analytics Engineering Roadmap"
summary: "A podcast-backed roadmap for analytics engineering: SQL modeling, dbt-style workflows, metric ownership, stakeholder trust, and the move from dashboards to governed analytical products."
related:
  - Analytics Engineering
  - Data Engineering
  - Data Product Management
  - Product Analytics
  - Metrics
  - Data Quality and Observability
---

## Definition

The archive treats analytics engineering as the work of turning raw business
and product data into trusted analytical models. A roadmap for this role should
move from SQL and business context into data modeling, tests, documentation,
semantic layers, stakeholder trust, and ownership of reusable metrics.

Analytics engineering is not a lighter version of data engineering. It is a
different center of gravity. Data engineers often own ingestion and platform
reliability. Analytics engineers own modeled data that analysts, executives,
experiments, and operational tools can use without reimplementing business
logic.

## Contents

- [Roadmap Stages](#roadmap-stages)
- [What to Build](#what-to-build)
- [Role Milestones](#role-milestones)
- [When to Stop Studying and Build](#when-to-stop-studying-and-build)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Roadmap Stages

### Stage 1: Become fluent in analytical SQL

Start with joins, aggregations, windows, CTEs, date handling, null behavior,
deduplication, and performance basics. Add enough Python to inspect data,
generate fixtures, or automate small checks, but do not make Python the center
of the roadmap too early.

Use real business questions: revenue by cohort, funnel conversion, retention,
customer acquisition cost, support volume, or product usage. The point is to
learn how data changes meaning when grain, filters, and joins change.

### Stage 2: Model data for reuse

Move from one-off queries to layered models. Practice raw/source, staging,
intermediate, mart, and BI-facing layers. Write down each model's grain,
owner, refresh cadence, and intended consumer.

The analytics engineering role episode warns against defining the role only as
"between analyst and engineer." The positive definition is cleaner: encode
business reality in models that other people can trust.

### Stage 3: Add tests and documentation close to the models

Use uniqueness, non-null, accepted-values, referential, freshness, and custom
business-rule tests. Document columns, metric definitions, known caveats, and
upstream assumptions. Build failure behavior into the project: what blocks a
release, what warns, and who gets notified.

This stage matters because dashboards are easy to make and hard to trust. The
archive connects analytics engineering to software engineering rigor: version
control, review, tests, docs, and deployment routines.

### Stage 4: Own metrics and semantic interfaces

Define metrics with stakeholders before encoding them. Build models and
dashboards that expose the same definitions across teams. Connect the work to
BI tools, notebooks, reverse ETL, or operational workflows.

At this stage, analytics engineering becomes data product work. A metric layer
or mart is valuable because many decisions reuse it, not because the SQL is
impressive.

### Stage 5: Specialize by domain or platform boundary

Choose one growth direction:

- product analytics: funnels, activation, retention, experimentation, and event
  tracking
- finance or operations: ERP data, reconciliations, revenue logic, and audit
  constraints
- platform analytics engineering: base models, dbt conventions, CI, and shared
  modeling standards
- data activation: reverse ETL, customer data platforms, and operational use of
  warehouse data
- governance: ownership, lineage, contracts, access, and metric definitions

The archive's career-transition episodes show that domain knowledge can be a
strength. A marketer, analyst, ERP specialist, or scientist can become useful
faster when they combine SQL with domain-specific definitions.

## What to Build

Build projects in this order:

1. **Metric model**: choose one business domain, define entities and grain, then
   produce documented marts.
2. **dbt-style analytics project**: add model layers, tests, documentation,
   lineage, and a small CI check.
3. **Dashboard trust exercise**: build a dashboard, intentionally change an
   upstream assumption, and show how tests or docs catch the issue.
4. **Metric conflict resolver**: model two competing definitions of a metric,
   explain the tradeoff, and publish one canonical version.
5. **Activation project**: send modeled segments or metrics to a product,
   sales, support, or marketing workflow.

Do not make the project only a dashboard gallery. The archive values evidence
that you can turn ambiguous business concepts into tested models and reusable
definitions.

## Role Milestones

**Entry-level readiness** means you can write analytical SQL, explain grain,
build a small mart, document columns, and add basic tests that catch common
data mistakes.

**Mid-level readiness** means you can own a domain model, align definitions
with stakeholders, review dbt or SQL changes, handle breaking source changes,
and debug metric disagreements.

**Senior readiness** means you can set modeling conventions, reduce duplicate
metrics, guide embedded analysts, work with data engineers on upstream
contracts, and treat BI or semantic layers as product surfaces.

## When to Stop Studying and Build

Stop studying and build when you can already:

- write SQL with joins, windows, CTEs, and aggregate logic
- explain table grain and why duplicate rows appear
- use Git for changes and review
- model at least one source-to-mart path
- name the business question your model answers

Do not wait until you know every dbt feature, semantic layer, and BI tool. Build
one domain model and let the problems teach the next topic: incrementalization,
testing, documentation, cost, metric ambiguity, or stakeholder review.

## Episode Evidence

| Episode | Roadmap evidence |
| --- | --- |
| [Foundations of Analytics Engineer Role](https://datatalks.club/podcast.html) | At 7:10-9:06, the episode frames the role as sitting between analysts and engineers but warns that this negative definition is incomplete. Later sections cover business reality, data modeling, data safety, Python, SQL, testing dashboards, software engineering rigor, dbt, warehouses, and community. |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | Defines day-to-day work around data modeling, pipelines, quality, Looker, dbt, Snowflake, SQL, DAGs, collaboration, tests, and role boundaries. |
| [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html) | Shows how domain knowledge, SQL, BI, Looker migration, dbt implementation, product analytics, A/B testing, and data modeling can form a transition path. |
| [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) | At 12:39, the episode connects dbt and warehouse transformations to analyst autonomy and the emergence of analytics engineering. |
| [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) | Links event tracking, tracking plans, warehouse transformations, BI, reverse ETL, customer data platforms, and data activation. |
| [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}) | Adds tool-selection caution: dbt shaped modern workflows, but teams should still choose based on requirements, cost, openness, and architecture. |

## Related Pages

- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.md`,
  `../datatalksclub.github.io/_podcast/analytics-engineer-skills-tools.md`,
  `../datatalksclub.github.io/_podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`,
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`,
  and `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- Future updates should add concrete interview and portfolio evidence for
  analytics engineering roles when more episodes mention hiring signals.
- Keep SEO-style explanations in the analytics engineer article. This page
  should stay focused on roadmap sequence, role milestones, and archive-backed
  project choices.
