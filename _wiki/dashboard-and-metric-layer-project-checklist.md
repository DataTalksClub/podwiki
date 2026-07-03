---
layout: wiki
title: "Dashboard Metric Checklist"
summary: "Build a dashboard and metric-layer project around one decision, with metric specs, lineage, tests, BI use, and adoption evidence."
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

Use a dashboard and metric-layer project to show how a team decides with a
metric, not just how a chart looks. Start with one stakeholder decision. Then
trace the metric from source events or tables through tested transformations, a
BI surface, and evidence that people use the result.

Use this checklist with
[[Analytics Engineering Portfolio Projects]]
when the portfolio target is
[[analytics engineering]],
[[product analytics]], or
[[data products]]. You get the
strongest portfolio signal when the project is more than a chart gallery. It
needs a metric specification, data lineage, tests, and stakeholder adoption.

[[person:caitlinmoorman=>Caitlin Moorman]] sets that
adoption bar by defining the last mile. She then works backward from user
research and outcomes. She places metrics inside the meetings where decisions
happen [[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].

## Stakeholder Decision and Meeting Use

A strong dashboard project names the decision before it names the chart. A
growth manager may choose which onboarding experiment to extend. A finance lead
may decide whether spending is off plan. A product manager may decide which
activation problem to investigate. The stakeholder should be able to say what
changes after they read the metric.

Caitlin's outcome-first discussion supports this structure because her version
starts with adoption. People need to find the dashboard, trust it, and use it in
the meeting where the decision happens [[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].
Use
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

[[person:adamsroka=>Adam Sroka]] gives the metric
standard through KPI definition and gaming risk. He also covers derived KPIs
and dashboard visibility [[cite:ml-engineering-kpis-and-metrics-strategy|ML Engineering KPIs and Metrics Strategy]].

For experimentation-heavy projects,
[[person:jakobgraff=>Jakob Graff]] adds guardrails through randomization,
causality, and A/A tests. He also covers metric stability and power analysis
in the same episode [[cite:ab-testing-and-product-experimentation|A/B Testing and Product Experimentation]].

Use [[Metrics]],
[[Experimentation]], and
[[a-b-testing=>A/B Testing]] when the project needs
deeper measurement definitions.

## Event and Model Lineage

The dashboard should show the full path from raw product behavior or source
tables to reusable models and BI consumption. That path usually starts with a
tracking plan and source events. It then moves through staging models,
intermediate business logic, marts, and metric definitions. Documentation and
lineage make that path inspectable.

[[person:arpitchoudhury=>Arpit Choudhury]] gives the
event path through tracking plans and anomaly investigation. He then connects
data flow and SaaS event examples with warehouse work, BI work, and activation [[cite:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]].
In his framing, event definitions and warehouse transformations belong to the
same growth system as BI and reverse ETL. That makes event ownership part of the
dashboard project.

[[person:nikolamaksimovic=>Nikola Maksimovic]] gives a
portfolio-scale version through product support, A/B testing, and data
modeling. He connects Snowplow, dbt, Looker, and product analytics into one
career-switching project story [[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]].

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

[[person:victoriaperezmola=>Victoria Perez Mola]] and
[[person:juanmanuelperafan=>Juan Manuel Perafan]] give
the analytics engineering version. Victoria connects modeling, data quality,
and Looker. She also covers dbt docs, DAGs, and tests [[cite:analytics-engineer-skills-tools|Master Analytics Engineering]].
Juan adds robustness, generic tests, and singular tests. He also covers CI, KPI
tests, and semantic-layer thinking [[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]].

## BI Surface, Activation, and Adoption Proof

The finished project needs a BI surface, but the dashboard isn't enough.
Include the dashboard or screenshots, the metric definition page, and a usage
note for caveats. The project should also show that the dashboard fits a
recurring business meeting. When the metric triggers operational action, link it
to
[[Data Activation]] as well as the
BI layer.

[[person:tammyliang=>Tammy Liang]] gives the team
version by discussing business health dashboards and reporting collaboration.
She also covers a stack and Notion wiki, dbt tests, and workshops [[cite:building-and-scaling-data-team|Building and Scaling a Data Team]]. Her
examples make the adoption checklist practical. The team defines the metric,
tests the data, documents the dashboard, and teaches people how to use it.

## Adjacent Dashboard Project Paths

For a broader learning path, pair this checklist with the
[[Analytics Engineering Roadmap]].
For a portfolio page, use
[[Analytics Engineering Portfolio Projects]]
to place the dashboard beside projects for source ingestion and transformation.
The same hub also connects it to data quality and stakeholder delivery.
