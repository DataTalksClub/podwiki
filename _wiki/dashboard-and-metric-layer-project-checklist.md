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
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
when the portfolio target is
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), or
[data products]({{ '/wiki/data-products/' | relative_url }}). You get the
strongest portfolio signal when the project is more than a chart gallery. It
needs a metric specification, data lineage, tests, and stakeholder adoption.

[Caitlin Moorman](https://datatalks.club/people/caitlinmoorman.html) sets that
adoption bar in
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html).
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
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
and
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
when the project needs stronger stakeholder framing.

## Metric Specification and Guardrails

The metric layer needs a written specification with these fields:

- metric grain and units
- owner and refresh cadence
- dimensions, filters, and caveats

Separate the primary decision metric from diagnostics and guardrails so the
dashboard doesn't encourage a single number at the expense of product or
business health.

[Adam Sroka](https://datatalks.club/people/adamsroka.html) gives the metric
standard in
[ML Engineering KPIs and Metrics Strategy](https://datatalks.club/podcast/ml-engineering-kpis-and-metrics-strategy.html).
At 22:41, he discusses KPI definition. At 28:04, he covers gaming risk. At
30:30, he covers derived KPIs. At 41:07, he discusses dashboards and
visibility.

For experimentation-heavy projects,
[Jakob Graff](https://datatalks.club/people/jakobgraff.html) adds guardrails in
[A/B Testing and Product Experimentation](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html).
He covers randomization at 8:13, causality at 11:48, and A/A tests at 27:52.
He also covers metric stability at 33:23 and power analysis at 37:44.

Use [Metrics]({{ '/wiki/metrics/' | relative_url }}),
[Experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) when the project needs
deeper measurement definitions.

## Event and Model Lineage

The dashboard should show the full path from raw product behavior or source
tables to reusable models and BI consumption. That path usually starts with a
tracking plan and source events. It then moves through staging models,
intermediate business logic, marts, and metric definitions. Documentation and
lineage make that path inspectable.

[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) gives the
event path in
[Data-Led Growth Stack](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html).
He covers tracking plans at 13:34 and anomaly investigation at 18:27. He covers
data flow at 22:50, SaaS event examples at 24:43, warehouse and BI work at
28:52, and activation at 30:03. In his framing, event definitions and warehouse
transformations belong to the same growth system as BI and reverse ETL. That
makes event ownership part of the dashboard project.

[Nikola Maksimovic](https://datatalks.club/people/nikolamaksimovic.html) gives a
portfolio-scale version in
[Marketing to Analytics Engineering](https://datatalks.club/podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.html).
He describes product support and A/B testing at 14:14. He covers data modeling
at 18:34. At 20:34, he discusses Snowplow, dbt, and Looker. At 38:27, he
returns to product analytics.

Use
[dbt]({{ '/wiki/dbt/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
to connect the dashboard back to source quality.

## Tests, Documentation, and Semantic Layer Choices

A dashboard-only project is weak when the numbers live only inside BI formulas.
The project is stronger when the metric sits on reusable models with tests,
documentation, and a clear semantic-layer boundary. Show generic tests for
expected data properties, singular tests for business rules, and a CI check
where the portfolio format allows it.

[Victoria Perez Mola](https://datatalks.club/people/victoriaperezmola.html) and
[Juan Manuel Perafan](https://datatalks.club/people/juanmanuelperafan.html) give
the analytics engineering version. Victoria connects modeling, data quality,
and Looker. She covers dbt docs, DAGs, and tests in
[Master Analytics Engineering](https://datatalks.club/podcast/analytics-engineer-skills-tools.html)
from 4:05 to 38:53. Juan adds robustness, generic tests, and singular tests. He
also covers CI, KPI tests, and semantic-layer thinking in
[Foundations of the Analytics Engineer Role](https://datatalks.club/podcast/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices.html)
from 38:41 to 1:14:40.

## BI Surface, Activation, and Adoption Proof

The finished project needs a BI surface, but the dashboard isn't enough.
Include the dashboard or screenshots, the metric definition page, and a usage
note for caveats. The project should also show that the dashboard fits a
recurring business meeting. When the metric triggers operational action, link it
to
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}) as well as the
BI layer.

[Tammy Liang](https://datatalks.club/people/tammyliang.html) gives the team
version in
[Building and Scaling a Data Team](https://datatalks.club/podcast/building-and-scaling-data-team.html).
She discusses business health dashboards at 7:22 and reporting collaboration at
8:51. She covers a stack and Notion wiki at 22:32, dbt tests at 40:09, and
workshops at 49:00. Her examples make the adoption checklist practical. The
team defines the metric, tests the data, documents the dashboard, and teaches
people how to use it.

## Adjacent Dashboard Project Paths

For a broader learning path, pair this checklist with the
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).
For a portfolio page, use
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
to place the dashboard beside projects for source ingestion and transformation.
The same hub also connects it to data quality and stakeholder delivery.
