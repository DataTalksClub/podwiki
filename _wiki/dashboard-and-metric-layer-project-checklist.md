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

The adoption bar is the last mile. Users can find the dashboard, trust the
metric, and use it inside the meeting where decisions happen.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

## Stakeholder Decision and Meeting Use

A strong dashboard project names the decision before it names the chart. A
growth manager may choose which onboarding experiment to extend. A finance lead
may decide whether spending is off plan. A product manager may decide which
activation problem to investigate. The stakeholder should be able to say what
changes after they read the metric.

This structure starts with adoption. People need to find the dashboard, trust
it, and use it in the meeting where the decision happens.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]
Use
[[Data Product Adoption]]
and
[[Data Product Management]]
when the project needs stronger stakeholder framing.

Make the meeting concrete in the project writeup. Name the attendee who owns
the decision, the review cadence, and the action that follows a metric change.
The last-mile discussion treats dashboard adoption as a behavior change. A good
project should show the metric inside the recurring workflow rather than only on
a standalone BI page.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@38:15=>Last-Mile Data Delivery]]
This connects the checklist to [[Business Intelligence]] and
[[data-product-adoption=>data product adoption]].

## Metric Specification and Guardrails

The metric layer needs a written specification with these fields:

- metric grain and units
- owner and refresh cadence
- dimensions, filters, and caveats

Separate the primary decision metric from diagnostics and guardrails so the
dashboard doesn't encourage a single number at the expense of product or
business health.

Metric definitions need ownership, derived-KPI rules, dashboard visibility, and
explicit attention to gaming risk.
[[cite:ml-engineering-kpis-and-metrics-strategy=>ML Engineering KPIs and Metrics Strategy]]
Treat the metric layer as a small operating vocabulary, not a wall of numbers.
For a portfolio project, include one primary [[kpis=>KPI]], a few diagnostics,
and a review rule for retiring metrics that no longer change decisions. That
matches the podcast guidance that KPIs need visibility, ownership, review
cadence, and a short enough list for teams to use.
[[cite:ml-engineering-kpis-and-metrics-strategy=>ML Engineering KPIs and Metrics Strategy]]

For experimentation-heavy projects, guardrails start with randomization,
causality checks, and A/A tests. They also include metric stability and power
analysis.
[[cite:ab-testing-and-product-experimentation=>A/B Testing and Product Experimentation]]

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

Tracking plans and anomaly investigation belong in the same growth system as
warehouse work, BI work, and activation.
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]]
That makes event ownership part of the dashboard project.

For event-backed dashboards, the project should say where each event fires and
which event marks the completed business action. A signup chart built from a
button click answers a different question than one built from a verified
account. The tracking-plan episode uses this distinction to explain why
capture location and property definitions matter before the data reaches
product analytics. The same definitions also feed BI and reverse ETL.
[[cite:data-led-growth-event-tracking-and-reverse-etl@27:00=>Data-Led Growth Stack]]
Use [[Tracking Plans]] and [[Event Tracking]] to document that boundary.

A portfolio-scale version can connect product support, A/B testing, and data
modeling. Snowplow, dbt, Looker, and product analytics can become one project
story.
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]

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

The analytics engineering version connects modeling, data quality, and Looker.
It also covers dbt docs, DAGs, and tests.
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
Robust projects also include generic tests, singular tests, and CI. KPI tests
and semantic-layer boundaries make the metric definition explicit.
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]

## BI Surface, Activation, and Adoption Proof

The finished project needs a BI surface, but the dashboard isn't enough.
Include the dashboard or screenshots, the metric definition page, and a usage
note for caveats. The project should also show that the dashboard fits a
recurring business meeting. When the metric triggers operational action, link it
to
[[Data Activation]] as well as the
BI layer.

Team-scale dashboard projects combine business-health reporting and stakeholder
collaboration. The supporting system includes a documented stack, a shared wiki,
dbt tests, and workshops.
[[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]]
The team defines the metric, tests the data, documents the dashboard, and
teaches people how to use it.

Add a visible trust state when the dashboard supports executive or operational
decisions. The data strategy discussion uses a traffic-light status for core
KPI dashboards. Green means users can rely on the data. Yellow means the team is
investigating known issues. Red means the metric is broken.

That status makes
the project stronger because it shows [[data-trust-and-strategy=>data trust]],
incident communication, and [[data-quality-and-observability=>data quality]]
instead of assuming every dashboard number is safe.
[[cite:mindful-data-strategy-for-business-impact@30:47=>Mindful Data Strategy]]

## Related Pages

For a broader learning path, pair this checklist with the
[[Analytics Engineering Roadmap]].
For a portfolio page, use
[[Analytics Engineering Portfolio Projects]]
to place the dashboard beside projects for source ingestion and transformation.
The same hub also connects it to data quality and stakeholder delivery.
