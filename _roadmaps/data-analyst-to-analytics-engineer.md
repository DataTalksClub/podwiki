---
layout: article
title: "Data Analyst to Analytics Engineer Roadmap"
keyword: "data analyst to analytics engineer"
summary: "A podcast-backed roadmap for analysts moving into analytics engineering through SQL modeling, dbt-style workflows, metric ownership, tests, documentation, and portfolio evidence."
search_intent: "People searching for data analyst to analytics engineer usually want a practical transition path: which analyst skills transfer, what modeling and dbt skills to add, and what project evidence proves readiness."
related_wiki:
  - Data Analyst Role
  - Data Analyst vs Analytics Engineer
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Analytics Engineering Portfolio Projects
  - dbt
  - Metrics
  - Product Analytics
  - Data Quality and Observability
---

Moving from data analyst to analytics engineer means moving upstream from
analysis into reusable analytical data. Analyst skills still matter because
SQL and KPI definitions transfer directly. Dashboards, experiment readouts, and
stakeholder explanations transfer too.

[Data Team Roles]({{ '/podcasts/data-team-roles/' | relative_url }}) describes
analysts as people who know company data and KPIs. Analysts also know
dashboards and product evaluation at 7:51-10:39. The transition begins when
repeated dashboard logic, cleaning rules, or metric definitions need to become
shared data assets.

Use
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
for the role boundary and
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
for the broader learning sequence.

## Transferable Skills

Analysts bring user context into analytics engineering because they know which
fields stakeholders ask about. They also know which dashboards matter and which
definitions cause confusion.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) gives the
transition route in
[Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
At 8:45-12:50, he describes using business and BI experience to move toward
analytics engineering. At 14:14-23:12, the work expands into product support
and A/B testing. It also expands into data modeling, dbt migration, Looker, and
LookML.

SQL and dashboard ownership are the strongest transferable skills, and KPI
definitions matter too. Experiment readouts and source knowledge also transfer.

## Missing Skills

The missing skills are model ownership and engineering practice. SQL needs to
be reusable and reviewable, and it also needs tests. dbt matters because it packages SQL
models with version control and documentation. It also adds lineage, tests, and
repeatable runs.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) gives
that standard in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
At 4:05-10:04, she describes modeling data for analysts and data scientists.
She also covers dbt SQL transformations and docs. GitHub version control,
tests, and DAGs are part of the same workflow. At 26:10-29:15, she names SQL
and dimensional modeling as core
preparation.

[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) adds
the engineering bar in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
At 7:56-18:35, he frames the work as turning business reality into data
models. At 38:41-46:34, he covers tests and CI-style workflows. He also covers
reproducibility and robustness.

## Learning Sequence

Start by refactoring analyst SQL. Pick a dashboard query and split it into
staging, intermediate, and mart layers. Define the grain and primary key for
each model. Add uniqueness and accepted-value tests. Add null checks,
relationship checks, and row-count expectations.

Then learn the ELT context around the model.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains in
[ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
that ELT loads raw data first. Analysts and analytics engineers then model data
in the warehouse with SQL and dbt-style workflows at 7:57-15:30.

Add product analytics and event semantics when the work touches user behavior.
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) covers
tracking plans and event ownership. He also covers warehouse transformations,
BI, and activation in
[Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})
at 13:34-30:03.

Use [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) for those
concepts.

## Portfolio Evidence

The strongest transition project starts from analyst work and turns it into a
reusable model layer.

Good project choices include:

- a dashboard query refactored into dbt-style models
- a governed metric definition with tests and documentation
- a funnel or retention mart built from event data
- a tested metric layer for one named stakeholder

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) grounds
the reliability side in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
At 33:47-38:01 and 43:06-51:21, he covers version control and automated tests.
He also covers CI/CD, runbooks, documentation, and end-to-end versioning. That
evidence makes tests and docs part of the portfolio.

[Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }}) adds the
transition-project standard in
[Get a Data Analytics and Data Engineering Job]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}).
At 50:15-53:34, she describes a custom capstone and data quality thinking. A
custom project stands out more than a repeated course project when it explains
why the data and checks matter.

Use
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
and
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
to choose the project scope.

## First Job Targets

Look for roles that sit close to your analyst experience. Good targets include
analytics engineer and BI engineer. A data analyst role with dbt ownership can
also work. Product analytics engineer and data modeler roles fit the same path.

The move is easiest when the story is concrete. You explained metrics to
stakeholders, then moved upstream and made the metric reusable. That matches
Nikola's path from BI and marketing work into dbt migration and product
analytics
([Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
14:14-38:27).

Use [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[dbt]({{ '/wiki/dbt/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
as supporting reference pages.

## Related Pages

Use these pages to follow the transition and adjacent role boundaries.

- [Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }})
- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Data Analyst vs Analytics Engineer Comparison]({{ '/comparisons/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
