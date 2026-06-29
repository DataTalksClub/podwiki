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

Analytics engineering builds reliable analytical data models and transformations,
then adds tests, documentation, and semantic interfaces. In the DataTalks.Club
archive, it sits between
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and analytics. Data engineers make data available as a platform. Analytics
engineers turn that data into reusable business definitions and decision-ready
models.

The role isn't only "SQL plus dashboards."
[Victoria Perez Mola's role episode]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
grounds the job in data modeling and quality checks. It also covers the
warehouse and BI stack. The workflow examples include SQL tests and DAGs. In
[Juan Manuel Perafan's foundations episode]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
the role translates business reality into clean data systems with software
engineering discipline.

## Link Map

Use these pages to place analytics engineering in the archive.

- Role boundaries: [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}), [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}), and [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- Adjacent concepts: [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}), [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}), [DataOps]({{ '/wiki/dataops/' | relative_url }}), and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- Transition pages: [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }}) and [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})

Core podcast interviews for this page:

- [Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
- [From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})
- [Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})
- [Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }})
- [DataOps Automation and Reliable Data Pipelines]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
- [Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})
- [ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
- [Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})

People connected to the cited interviews:

- [Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
- [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
- [Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
- [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }})
- [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
- [Tammy Liang]({{ '/people/tammyliang/' | relative_url }})
- [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
- [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})

## Common Definition

Across the archive, analytics engineering means owning the modeled analytical
layer between raw data and users. The common output isn't a one-off query. It's
a maintained model with clear grain, tested assumptions, documented definitions,
and a path into BI or operational use.

Perez Mola places data modeling and dbt tests at the center of the role. She
also connects the job to Looker, Snowflake, and collaboration. Perafan describes
the craft as converting messy business reality into safe data systems
([Perez Mola]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Perafan]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

The archive also agrees that analytics engineering is a response to a team
bottleneck. Analysts and data scientists need trusted definitions but often lose
time rebuilding joins and reconciling dashboards. Data engineers may own
ingestion, orchestration, cloud infrastructure, and platform reliability.
Analytics engineers occupy the middle. They use engineering
practices to make business-facing data reusable
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Disagreements and Boundaries

Guests differ most on whether analytics engineering is a separate role. It can
also be a practice inside adjacent roles. Perez Mola describes a bridge role
that overlaps with analysts, data engineers, BI developers, and platform teams.
Perafan is more explicit that many tasks predate the title.

The name is useful when it clarifies ownership of modeling and testing. It's
less useful when it creates a rigid job boundary
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Guests also differ on tool centrality. dbt is the archive's clearest symbol of
analytics engineering because it made SQL transformations visible as a DAG. It
also made them versioned and testable. Nikola Maksimovic's transition story adds
Looker migration, product analytics, A/B testing, and table design.

Natalie Kwong places dbt inside a broader ELT flow with ingestion and
warehouses. She also connects it to orchestration, CDC, and reverse data flows
([Maksimovic]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Kwong]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Team size changes the boundary. In Tammy Liang's small-team story, early
analytics work started with business-health monitoring and dashboard adoption.
It later included a warehouse, dbt, Data Studio, and Notion documentation. Tests
and forecasting support followed. That work crossed analyst and engineer
responsibilities because the company needed trusted data first
([Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

## Role Boundaries

Analytics engineering is easiest to identify by the problem it owns. The
repeated analytical logic has become too important for scattered dashboards or
ad hoc SQL. Perez Mola compares analytics engineers with data analysts, data
engineers, and BI developers. The practical boundary is that analytics
engineers encode reusable definitions and quality checks. Analysts focus more
on questions, interpretation, and stakeholder recommendations
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})).

The boundary with data engineering is platform ownership. Data engineers often
own ingestion and orchestration, plus raw storage and system reliability.
Analytics engineers depend on that platform. They add domain models, metrics,
semantic layers, and BI-ready marts.

Kwong makes this boundary concrete through ELT. In that ELT flow, source data is
loaded first and warehouse-side transformations serve analytical users
([Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

## Modeling and Semantic Layers

The central craft is data modeling. Analytics engineers decide the grain of a
table and separate staging work from business marts. They choose facts and
dimensions, then weigh wide tables against narrower models. Maksimovic connects
these modeling decisions to growth and product work.

His episode covers Looker
reporting, dbt migration, product support, and A/B testing. It also covers
retention analysis and marketing funnels
([From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

The semantic layer is where analytics engineering becomes product work. A model
is valuable when analysts and product teams can reuse a definition without
copying business logic into new queries. Arpit Choudhury extends this from BI
into activation. Tracking plans and warehouses need source awareness. BI
analysis and reverse ETL need documented definitions
([Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})).

## dbt and the Modern Data Stack

dbt appears repeatedly because it packaged software engineering habits for SQL.
Those habits include version control and dependency graphs. They also include
reusable macros, docs, tests, and repeatable runs. Perez Mola uses dbt to
explain analytics engineering through SQL transformations and tests. She also
connects the workflow to a DAG, Snowflake, and Looker.

Maksimovic shows the implementation side through a dbt migration and practical
data modeling work
([Perez Mola]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Maksimovic]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The archive doesn't reduce the discipline to dbt. Kwong situates dbt after
ingestion and storage, alongside Airbyte and warehouses. Orchestration, CDC, and
schema evolution remain part of the same stack.

Analytics engineering inherits source-system and warehouse-cost constraints from
the full platform. Freshness plus orchestration reliability also matter
([Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Data Quality and DataOps

Analytics engineering quality work is continuous in Perez Mola's examples of
non-null tests and uniqueness tests. She also discusses custom SQL tests and
macros. Source checks, warnings, and alerts matter too. Perafan broadens that
into safety.

His episode asks teams to stop manually validating dashboards. It argues for
engineering rigor in data workflows
([Analytics Engineer Skills and Tools]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Christopher Bergh's DataOps episode gives the operating model behind those
practices. It covers version control, tests, CI/CD, and observability. It also
covers automated runbooks, documentation, and end-to-end delivery.

Analytics engineers don't own every platform reliability concern. Their models
still become production dependencies when dashboards or forecasts rely on them
([DataOps Automation and Reliable Data Pipelines]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }})).

## Business Context and Career Paths

The archive treats business context as an advantage, not a distraction.
Maksimovic's path from marketing into analytics engineering worked because
marketing funnels and stakeholder questions gave the technical work a target.
User journeys and performance feedback loops mattered too.

The missing skills weren't abstract data skills but SQL and BI projects.
Pipeline literacy and Python basics also mattered, along with Looker and dbt.
Modeling practice was another requirement
([Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }}),
[From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Jeff Katz's data engineering curriculum places analytics engineering early in a
career path. The path uses SQL and dbt. It also uses Snowflake, Mode, and
Fivetran. The curriculum covers OLTP versus OLAP concepts and data modeling.

That makes analytics engineering a practical entry point before deeper backend
or cloud specialization. Streaming and ML platforms are later paths
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }}),
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})).

## Team Design and Adoption

Analytics engineering succeeds when modeled data changes how teams work. Liang's
team-building episode starts with dashboards and business-health monitoring. It
then moves into a warehouse, Stitch, GCP, and dbt. Data Studio and Notion docs
make the work usable.

Tests, monitoring, forecasting, and workshops help rebuild trust outside the
data team
([Building and Scaling a Data Team]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

Choudhury's data-led growth stack shows a similar adoption surface for product
and go-to-market teams. Event tracking and tracking plans create demand for
coordination. Warehouse transforms, BI, and reverse ETL add more handoffs. Data
literacy adds a second need. Analytics engineers and data engineers need shared
definitions with analysts and product ops
([Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})).

## Related Pages

Use these pages for role boundaries, platform context, and career paths.

- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
- [Analytics Engineer article]({{ '/articles/analytics-engineer/' | relative_url }})
