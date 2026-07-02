---
layout: wiki
title: "Dashboard and Metric Layer Project Checklist"
summary: "Checklist for a dashboard or metric-layer portfolio project that proves stakeholder decisions, event definitions, metric ownership, tested models, BI consumption, and adoption."
related:
  - Analytics Engineering Portfolio Projects
  - Analytics Engineering
  - Metrics
  - Product Analytics
  - Event Tracking
  - Tracking Plans
  - Data Product Adoption
  - A/B Testing
---

## Dashboard Project Definition

A dashboard and metric-layer project proves that analytical data helps people
make a specific decision. It starts with one stakeholder decision. Then it
traces the metric from source events or tables through tested transformations,
a BI surface, and evidence that people use the result.

Use this checklist with
[[Analytics Engineering Portfolio Projects]]
when the portfolio target is
[[analytics engineering]],
[[product analytics]], or
[[data products]]. You get the
strongest portfolio signal when the project is more than a chart gallery. It
needs a metric specification, data lineage, tests, and stakeholder adoption.

[[person:caitlinmoorman|Caitlin Moorman]] sets that
adoption bar in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].
At 8:48, she defines the last mile. At 26:21 and 34:00, she works backward from
user research and outcomes. At 38:15, she places metrics inside the meetings
where decisions happen.

## Stakeholder Decision and Meeting Use

A strong dashboard project names the decision before it names the chart. A
growth manager may choose which onboarding experiment to extend. A finance lead
may decide whether spending is off plan. A product manager may decide which
activation problem to investigate. The stakeholder should be able to say what
changes after they read the metric.

Caitlin's outcome-first discussion at 34:00 supports this structure because her
version starts with adoption. People need to find the dashboard, trust it, and
use it in the meeting where the decision happens. Use
[[Data Product Adoption]]
and
[[Data Product Management]]
when the project needs stronger stakeholder framing.

## Metric Specification and Guardrails

The metric layer needs a written specification with these fields:

- metric grain and units
- owner and refresh cadence
- dimensions, filters, and caveats

Separate the primary decision metric from diagnostics and guardrails so the
dashboard doesn't encourage a single number at the expense of product or
business health.

[[person:adamsroka|Adam Sroka]] gives the metric
standard in
[[podcast:ml-engineering-kpis-and-metrics-strategy|ML Engineering KPIs and Metrics Strategy]].
At 22:41, he discusses KPI definition. At 28:04, he covers gaming risk. At
30:30, he covers derived KPIs. At 41:07, he discusses dashboards and
visibility.

For experimentation-heavy projects,
[[person:jakobgraff|Jakob Graff]] adds guardrails in
[[podcast:ab-testing-and-product-experimentation|A/B Testing and Product Experimentation]].
He covers randomization at 8:13, causality at 11:48, and A/A tests at 27:52.
He also covers metric stability at 33:23 and power analysis at 37:44.

Use [[Metrics]],
[[Experimentation]], and
[[a-b-testing|A/B Testing]] when the project needs
deeper measurement definitions.

## Event and Model Lineage

The dashboard should show the full path from raw product behavior or source
tables to reusable models and BI consumption. That path usually starts with a
tracking plan and source events. It then moves through staging models,
intermediate business logic, marts, and metric definitions. Documentation and
lineage make that path inspectable.

[[person:arpitchoudhury|Arpit Choudhury]] gives the
event path in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]].
He covers tracking plans at 13:34 and anomaly investigation at 18:27. He covers
data flow at 22:50, SaaS event examples at 24:43, warehouse and BI work at
28:52, and activation at 30:03. In his framing, event definitions and warehouse
transformations belong to the same growth system as BI and reverse ETL. That
makes event ownership part of the dashboard project.

[[person:nikolamaksimovic|Nikola Maksimovic]] gives a
portfolio-scale version in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]].
He describes product support and A/B testing at 14:14. He covers data modeling
at 18:34. At 20:34, he discusses Snowplow, dbt, and Looker. At 38:27, he
returns to product analytics.

Use
[[dbt]],
[[Tracking Plans]],
[[Event Tracking]], and
[[Data Quality and Observability]]
to connect the dashboard back to source quality.

## Tests, Documentation, and Semantic Layer Choices

A dashboard-only project is weak when the numbers live only inside BI formulas.
The project is stronger when the metric sits on reusable models with tests,
documentation, and a clear semantic-layer boundary. Show generic tests for
expected data properties, singular tests for business rules, and a CI check
where the portfolio format allows it.

[[person:victoriaperezmola|Victoria Perez Mola]] and
[[person:juanmanuelperafan|Juan Manuel Perafan]] give
the analytics engineering version. Victoria connects modeling, data quality,
and Looker. She covers dbt docs, DAGs, and tests in
[[podcast:analytics-engineer-skills-tools|Master Analytics Engineering]]
from 4:05 to 38:53. Juan adds robustness, generic tests, and singular tests. He
also covers CI, KPI tests, and semantic-layer thinking in
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]]
from 38:41 to 1:14:40.

## BI Surface, Activation, and Adoption Proof

The finished project needs a BI surface, but the dashboard isn't enough.
Include the dashboard or screenshots, the metric definition page, and a usage
note for caveats. The project should also show that the dashboard fits a
recurring business meeting. When the metric triggers operational action, link it
to
[[Data Activation]] as well as the
BI layer.

[[person:tammyliang|Tammy Liang]] gives the team
version in
[[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]].
She discusses business health dashboards at 7:22 and reporting collaboration at
8:51. She covers a stack and Notion wiki at 22:32, dbt tests at 40:09, and
workshops at 49:00. Her examples make the adoption checklist practical. The
team defines the metric, tests the data, documents the dashboard, and teaches
people how to use it.

## Adjacent Dashboard Project Paths

For a broader learning path, pair this checklist with the
[[Analytics Engineering Roadmap]].
For a portfolio page, use
[[Analytics Engineering Portfolio Projects]]
to place the dashboard beside projects for source ingestion and transformation.
The same hub also connects it to data quality and stakeholder delivery.
