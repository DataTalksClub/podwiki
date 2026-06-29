---
layout: wiki
title: "Analytics Engineering"
summary: "How DataTalks.Club episodes describe analytics engineering as the discipline of building trusted analytical models, transformations, tests, documentation, and BI-ready data products."
related:
  - Data Engineering Platforms
  - MLOps and DataOps
  - Data Product Management
  - Career Transitions in Data
---

## Definition

Analytics engineering is the discipline of building reliable analytical data
models for analysts, data scientists, product teams, and business users. It sits
between data engineering and analytics: close enough to the business to
understand definitions and decisions, but engineering-oriented enough to use
version control, tests, modular transformations, documentation, and deployment
workflows.

In the DataTalks.Club archive, analytics engineering is not merely "SQL plus
dashboards." It is the work of turning raw events, product data, ERP records,
marketing data, and warehouse tables into reusable, trusted semantic layers. The
role exists because analysts and data scientists lose time cleaning data, while
data engineers often focus on infrastructure, ingestion, and platform
reliability rather than domain-specific modeling.


## Scope

This page covers analytics engineering as an archive-derived concept: data
modeling, dbt-style transformations, testing, documentation, warehouse-centric
analytics, BI exposure, event tracking dependencies, and the role boundary with
analysts, data engineers, data scientists, and product teams.

It does not replace [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Data engineering platforms cover ingestion, orchestration, storage, contracts,
governance, cost, streaming, and self-service infrastructure. Analytics
engineering uses those platforms to create business-facing data models and
trusted analytical interfaces.

## Recurring Patterns From Episodes

### The role is a bridge, not a fixed job description

The role-definition episode describes analytics engineers as being in the
middle between data analysts and data engineers. The exact balance varies by
company. Some analytics engineers lean toward pipeline work and platform
modeling. Others stay closer to product analytics, dashboards, experimentation,
and KPI definitions.

This variability is not a defect in the archive. It is the core organizational
pattern: the role appears where domain knowledge, SQL modeling, data quality,
and engineering practices need the same owner.

### dbt made the work visible, but did not invent the work

Several episodes connect analytics engineering with dbt because dbt brought
software-development practices into SQL transformation work: repositories,
modular models, YAML documentation, dependency graphs, tests, and scheduled
runs. The marketing-to-analytics-engineering episode is especially clear that
many teams did similar work before adopting the title or the tool.

The concept is therefore larger than dbt. A team can do analytics engineering
with homegrown SQL orchestration, dbt, SQLMesh-style tooling, or warehouse-native
workflows if the same responsibilities are present: modeled data, tests,
documentation, lineage awareness, and stakeholder-facing definitions.

### Data modeling is the central craft

The archive repeatedly distinguishes analytics engineering from ad hoc SQL by
the attention to data modeling. Guests discuss dimensions and facts, schema
design, domain models, staging layers, presentation tables, wide versus narrow
tables, incrementalization, and BI-ready structures.

This is where analytics engineering compounds. A good model lets many analysts,
dashboards, experiments, and product decisions reuse a definition instead of
copying business logic into scattered queries.

### Quality work is continuous

Analytics engineering episodes do not promise perfect data. They describe a
cycle: expose source issues, clean and standardize where appropriate, add tests,
decide warning versus error behavior, respond when stakeholders find mismatched
numbers, and improve tests or upstream contracts over time.

The role-definition episode gives concrete dbt examples: non-null and uniqueness
tests, custom SQL tests, macros for standardization, source checks before
downstream models build, and alerts when assumptions fail.

### The semantic layer is a product surface

Looker, dashboards, self-service BI, reverse ETL, and data activation appear as
consumption layers. Analytics engineering does not stop when a model builds.
The model has to be understandable and usable by analysts, business users,
product teams, data scientists, and sometimes operational tools.

This links analytics engineering to [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}):
definitions, KPIs, and modeled tables are products when other teams depend on
them for decisions.

### Domain knowledge is an advantage

The career-transition episodes show marketing, ERP, finance, and product
backgrounds as useful paths into analytics engineering. Domain experience helps
people understand funnels, KPIs, user journeys, operational records, and why a
model needs to be shaped a certain way.

The archive therefore treats analytics engineering as more accessible than
deep-infrastructure data engineering for some career switchers, while still
requiring strong SQL, modeling discipline, and engineering habits.

## Implementation Checklist

Use this checklist when building or evaluating analytics engineering work:

1. **Source understanding**: Identify the system of origin, event semantics,
   schema owners, refresh cadence, and known quality gaps.
2. **Business definitions**: Define metrics, dimensions, entities, and grain
   with analysts and stakeholders before encoding them in SQL.
3. **Layering**: Separate raw/source, staging, intermediate/domain, mart, and
   BI-facing layers where the stack supports it.
4. **Modeling choices**: Choose facts, dimensions, wide/narrow tables,
   incremental models, and materializations based on consumption needs and cost.
5. **Testing**: Add uniqueness, non-null, accepted values, referential,
   freshness, and custom business-rule tests where failures would affect users.
6. **Documentation**: Document model purpose, owner, grain, columns, metric
   definitions, upstream dependencies, and known caveats.
7. **Deployment workflow**: Use version control, code review, CI checks, and
   scheduled runs or orchestration rather than manual warehouse changes.
8. **BI and activation**: Expose models through dashboards, semantic layers,
   notebooks, reverse ETL, or operational tools with clear ownership.
9. **Incident handling**: Decide what blocks builds, what warns, who is alerted,
   and how downstream users are informed.
10. **Lifecycle**: Deprecate unused models, resolve duplicate definitions, and
    keep documentation close to the transformation code.

## Episode Evidence

| Episode | Evidence for this concept |
| --- | --- |
| [Analytics Engineer: New Role in a Data Team](https://datatalks.club/podcast.html) | Defines day-to-day analytics engineering around data modeling, pipelines, quality, Looker, dbt, Snowflake, SQL, tests, DAGs, collaboration, and role boundaries. The strongest sections cover daily responsibilities, dbt workflow, and data testing strategy. |
| [From Digital Marketing to Analytics Engineering](https://datatalks.club/podcast.html) | Shows a transition path through SQL, BI, Looker migration, dbt implementation, domain knowledge, product analytics, A/B testing, data modeling, wide/narrow table choices, and incrementalization. |
| [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}) | Connects analytics engineering to ELT, warehouse transformations, dbt, analyst autonomy, data marts, orchestration, Airbyte, reverse data flows, CDC, and schema evolution. |
| [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) | Shows how event tracking, tracking plans, warehouse transformations, BI, reverse ETL, and team composition create demand for analysts, analytics engineers, data engineers, and product ops. |
| [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}) | Adds a later critique: the modern data stack is partly vendor packaging; dbt influenced workflows, but teams should still choose tools based on requirements, cost, openness, and architecture. |
| [Data Engineering Career Path and Skills](https://datatalks.club/podcast.html) | Presents analytics engineering as a practical early data curriculum: SQL, dbt, Snowflake, Mode, Fivetran, data modeling, OLTP/OLAP concepts, and interview-relevant SQL. |
| [DataOps Automation and Reliable Data Pipelines](https://datatalks.club/podcast.html) | Provides reliability practices that analytics engineering inherits: version control, tests, CI/CD, observability, dbt, Great Expectations, SQL tests, and end-to-end data delivery. |
| [Building and Scaling a Data Team](https://datatalks.club/podcast.html) | Shows a small-team stack with Stitch, GCP, dbt, Data Studio, Notion documentation, dbt tests, monitoring, forecasting, and production ML support. |

## Tradeoffs and Disagreements

### Role title versus actual work

The archive preserves skepticism about the title. In smaller teams, the split
between data analyst and analytics engineer may be overhyped because the same
people do dashboards, KPI work, modeling, experiments, and stakeholder support.
In larger teams, specialization becomes useful because shared models,
standards, tests, and BI layers need dedicated ownership.

### Tooling versus discipline

dbt is central in the episodes, but the recurring pattern is discipline rather
than tool worship. Versioned SQL, dependency graphs, tests, documentation,
review, and clear ownership matter more than the brand of transformation tool.

### Central platform versus embedded ownership

The role-definition episode describes both platform analytics engineers and
analytics engineers embedded in commercial or operations teams. Central teams
create base models and standards. Embedded roles bring domain context and faster
stakeholder feedback. The healthy pattern is explicit ownership between base
data, domain marts, and BI-facing models.

### Cleaning downstream versus fixing upstream

Analytics engineers often clean and standardize data in transformation layers,
but the archive does not treat downstream cleaning as a complete answer. Source
systems, backend events, tracking plans, schemas, and data contracts remain
important. A model can hide source quality issues temporarily, but durable data
quality requires upstream collaboration.

## Related Pages

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
- [Analytics Engineer article]({{ '/articles/analytics-engineer/' | relative_url }})

## Agent Maintenance Notes

- Highest-value source files for future expansion:
  `../datatalksclub.github.io/_podcast/analytics-engineer-skills-tools.md`,
  `../datatalksclub.github.io/_podcast/from-marketing-to-analytics-engineering-sql-dbt-career-switch.md`,
  `../datatalksclub.github.io/_podcast/data-engineering-tools-modern-data-stack.md`,
  and `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- Existing local summaries already cover the broader platform evidence:
  [ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
  [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
  and [Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
- Good future additions: a table comparing analytics engineer, data analyst,
  data engineer, BI developer, and data product owner; examples of model layers
  from dbt projects; more evidence from data quality and governance episodes;
  and people links for Victoria Perez Mola, Nikola Maksimovic, Natalie Kwong,
  Arpit Choudhury, and Adrian Brudaru where useful.
- Avoid converting this wiki page into a career article. The SEO-facing
  explanation belongs in [Analytics Engineer]({{ '/articles/analytics-engineer/' | relative_url }}).
  Keep this page focused on archive synthesis, operational patterns, tradeoffs,
  and reusable evidence for future agents.
