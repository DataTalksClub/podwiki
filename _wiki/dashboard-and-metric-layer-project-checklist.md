---
layout: wiki
title: "Dashboard and Metric Layer Project Checklist"
summary: "Archive-backed checklist for a dashboard or metric-layer portfolio project that proves stakeholder decisions, event definitions, metric ownership, tested models, BI consumption, and adoption."
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

## Definition

A dashboard and metric-layer project proves that analytical data helps people
make a decision. The project should start with one stakeholder decision. Then
it should show source definitions, metric grain, and tested transformations.
It should also show a BI surface and adoption evidence.

Use this checklist with
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
when the target work is
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), or
[data products]({{ '/wiki/data-products/' | relative_url }}).

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) gives the
adoption standard in
[Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}).
At 8:48, she defines the last mile. At 26:21 and 34:00, she works backward
from user research and outcomes. At 38:15, she places metrics inside the
meetings where decisions happen.

## Common Definition

Guests treat a dashboard as the final surface of a data product. The useful
proof is the path from events or source tables to tested models, metric
definitions, dashboard consumption, and stakeholder behavior.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
event path in
[Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
He covers tracking plans at 13:34 and anomaly investigation at 18:27. He covers
data flow at 22:50, SaaS event examples at 24:43, warehouse and BI work at
28:52, and activation at 30:03.

[Adam Sroka]({{ '/people/adamsroka/' | relative_url }}) gives the metric
standard in
[ML Engineering KPIs and Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }}).
At 22:41, he discusses KPI definition. At 28:04, he covers gaming risk. At
30:30, he covers derived KPIs. At 41:07, he discusses dashboards and
visibility.

## Guest Differences

For Caitlin, adoption is the starting point. A dashboard fails when people
can't find it or trust it. It also fails when the meeting workflow never uses it.

Arpit starts from product and growth data. He ties event definitions, warehouse
transformations and BI into the same system. Reverse ETL belongs there too.
That makes event
ownership part of the project.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) start
from analytics engineering. Victoria connects modeling, data quality, and
Looker. She also covers dbt docs, DAGs, and tests
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
4:05-38:53). Juan adds robustness, generic tests, and singular tests. He also
covers CI, KPI tests, and semantic-layer thinking
([Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
38:41-1:14:40).

## Stakeholder Decision

Start with one named decision. A growth manager or finance lead should be able
to explain what changes after looking at the metric. A support team, product
manager, or executive sponsor works too.

Caitlin's outcome-first discussion at 34:00 supports this structure. Use
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
when the project needs adoption and stakeholder framing.

## Metric Definitions

The project should define metric grain, units, dimensions, and filters. It
should also define ownership, refresh cadence, and caveats. Separate primary
decision metrics from diagnostics and guardrails.

[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) gives the
experimentation guardrails in
[A/B Testing and Product Experimentation]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).
He covers randomization at 8:13 and causality at 11:48. He covers A/A tests at
27:52, metric stability at 33:23, and power analysis at 37:44.

Use [Metrics]({{ '/wiki/metrics/' | relative_url }}),
[Experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}) for the deeper
measurement topics.

## Tested Model Layer

A dashboard-only artifact is weak unless the metrics sit on reusable and
tested models. Show staging models, intermediate logic, and marts. Also show
metric definitions, tests, documentation, and lineage.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) gives a
practical version in
[Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
He describes product support and A/B testing at 14:14. He covers data modeling
at 18:34, Snowplow, dbt, and Looker at 20:34. He covers product analytics at
38:27.

Use [dbt]({{ '/wiki/dbt/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
to connect the model layer to source quality.

## Trust And Adoption

The project should show how errors are detected and how stakeholders learn to
use the dashboard. Include a usage guide, definition page, warning note, or
meeting workflow.

[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) gives the team
version in
[Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }}).
She discusses business health dashboards at 7:22 and reporting collaboration at
8:51. She covers a stack and Notion wiki at 22:32, dbt tests at 40:09, and
workshops at 49:00.

## Related Pages

Use these pages to follow the analytics and product context.

- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
