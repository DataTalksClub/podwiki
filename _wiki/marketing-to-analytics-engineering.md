---
layout: wiki
title: "Marketing to Analytics Engineering"
summary: "Podcast-backed transition notes for marketers moving into analytics engineering through SQL, BI, dbt, product analytics, dashboards, and metric ownership."
related:
  - Career Transition
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Product Analytics
  - dbt
---

Marketing to analytics engineering is one of the archive's clearest adjacent
role transitions. The marketer already knows campaigns, funnels, and users.
They also know conversion pressure, reporting pressure, and stakeholder
questions. They turn that domain knowledge into SQL and BI. Data models, tests,
and documentation become the next proof points.

The archive doesn't frame this path as "become technical from scratch." It
frames it as a move from optimizing marketing decisions with data to owning the
models, dashboards, and metric definitions that other teams reuse.

## Contents

Use these sections to compare prior marketing work with analytics engineering
proof.

- [Transition Profile](#transition-profile)
- [Transferable Skills](#transferable-skills)
- [Missing Skills](#missing-skills)
- [Portfolio Evidence](#portfolio-evidence)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Transition Profile

This path fits marketers who already work with campaign data and product
funnels. It also fits people who work on customer acquisition, retention, or
marketing reporting. Performance marketing is especially close because the work
already asks whether a channel or campaign changed a metric. Country and
audience splits matter too.

The strongest path in the archive is internal. In
[From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html),
Nikola Maksimovic first helped with reporting and a Looker migration. She then
used conversations with the BI team to identify the missing skills. The move
passed through a marketing analyst role before becoming analytics engineering.

## Transferable Skills

Marketers bring several skills that analytics engineers can reuse.

- Funnel and user-journey knowledge: marketers already know acquisition,
  activation, retention, and conversion, and many also know attribution and
  audience segmentation.
- KPI pressure: marketing teams feel metric ambiguity quickly because campaign
  decisions depend on daily or weekly numbers.
- Stakeholder empathy: marketers know how non-data teams ask for answers and
  how dashboard definitions affect decisions.
- Experimentation instincts: A/B testing, campaign comparison, and growth work
  map naturally to product analytics and metric design.
- Communication: marketing experience helps explain why a metric matters, not
  only how the SQL works.

## Missing Skills

The archive names a concrete skill stack rather than a vague "learn data" plan.

- SQL beyond simple selects: joins, windows, CTEs, dates, nulls, performance,
  and reading existing complex queries.
- BI tool fluency: Looker, Tableau, Redash, or similar tools, with attention to
  dashboard grain and definitions.
- Data modeling: source, staging, intermediate, mart, and BI-facing tables.
- dbt-style practice: transformations, model dependencies, incremental logic,
  tests, docs, and review.
- Pipeline literacy: enough Airflow, Airbyte, warehouse, and ingestion context
  to debug where modeled data comes from.
- Python basics: useful for small checks, scripts, or exploration, but the
  marketing-to-analytics path in the archive stays SQL-first.

## Portfolio Evidence

A strong portfolio should prove that the candidate can turn ambiguous marketing
data into trusted analytical products.

Good projects include:

- a campaign reporting mart with documented grain and metric definitions
- a product funnel model that separates events, users, sessions, and
  conversions
- a dbt-style project with tests, docs, lineage, and a small CI check
- a dashboard trust exercise that shows how one upstream definition changes a
  KPI
- an A/B testing or retention project that explains the data model before the
  chart
- a marketing activation project that sends modeled audiences or metrics to a
  downstream tool

The archive warns against treating the portfolio as a dashboard gallery.
Analytics engineering proof is stronger when the candidate shows the model,
the assumptions, the test cases, and the business question.

## Episode Evidence

These episodes anchor the transition path.

- [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html):
  At 2:53, performance marketing becomes a data-heavy role through reporting
  and campaign optimization. At 7:18, the pivot moves toward BI and analytics.
  At 9:53, conversations with the BI team identify SQL and pipeline
  understanding as gaps. Python basics are also a gap. At 14:14, the transition
  happens through BI projects alongside marketing work.

  At 41:50, the playbook starts with Excel and SQL before dashboard practice and
  small projects.
- [Analytics Engineering Roadmap](https://datatalks.club/podcast.html):
  Analytics engineering episodes support the same roadmap. Candidates need SQL
  fluency and reusable models, plus tests and documentation. Stakeholder
  definitions and domain specialization come next.
- [Data-Led Growth Stack](https://datatalks.club/podcast.html):
  Growth and activation episodes connect event tracking, warehouse
  transformations, reverse ETL, and customer data platforms. They also connect
  modeled data to operational workflows. This gives marketers a natural data
  activation extension.
- [Becoming Data Freelancer](https://datatalks.club/podcast.html):
  Dimitri's path starts with business administration and marketing, then shifts
  into data because startup founders value the data work. This supports the
  adjacent-domain route even though the target is freelance data work rather
  than analytics engineering.

## Related Pages

Use these pages for the broader role and adjacent skills.

- [Career Transition]({{ '/wiki/career-transition/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})

## Maintenance Notes

Future edits should preserve the transition focus.

- Primary source episode:
  `../datatalksclub.github.io/_podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`.
- Keep this page focused on the transition path. Put general analytics
  engineering material in [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
  or [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}).
- Add more evidence when future episodes discuss marketing operations,
  lifecycle marketing, growth analytics, attribution, or reverse ETL as a
  bridge into analytics engineering.
