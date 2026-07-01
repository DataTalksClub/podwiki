---
layout: wiki
title: "Analytics Engineering"
summary: "How DataTalks.Club episodes describe analytics engineering as the discipline of building trusted analytical models, transformations, metric definitions, tests, documentation, and BI-ready data products."
related:
  - Data Engineering Platforms
  - MLOps and DataOps
  - Data Product Management
  - Career Transitions in Data
  - dbt
  - Metrics
  - Event Tracking
  - Tracking Plans
  - Analytics Engineering Portfolio Projects
---

Analytics engineering builds reliable analytical data models and transformations,
then adds tests, documentation, and semantic interfaces. In the DataTalks.Club
archive, it sits between
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and analytics. Data engineers make data available as a platform. Analytics
engineers turn that data into reusable business definitions and decision-ready
models.

The role isn't only "SQL plus dashboards."
[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) grounds the job in
[data modeling and quality checks]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
It also covers metric definitions, event semantics, the warehouse, and the BI
stack. The workflow examples include SQL tests and DAGs. In
[Juan Manuel Perafan's foundations episode]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Perafan]({{ '/people/juanmanuelperafan/' | relative_url }})
describes the role as translating business reality into clean data systems with
software engineering discipline.

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
Analytics engineers occupy the middle. They use engineering practices to make
business-facing data reusable
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Santona Tuli adds a pipeline-level version of the same definition. Her modern
data pipeline discussion puts dbt after ingestion and orchestration. It then
ties modeled marts to dashboards and business questions at 24:57, 39:23, and
43:05
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

## Guest Differences

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
also made them versioned and testable.
[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) adds
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

Rishabh Bhargava's analytics-to-ML discussion shows another boundary.
Analytics engineering can bridge notebooks and SQL-plus-Python work into
production ML, but the goals still differ. Analytics work explains business
behavior, while ML systems serve predictions under operational constraints
([Production ML and Data Team Building]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})).

## Role Boundaries

Analytics engineering is easiest to identify by the problem it owns. The
repeated analytical logic has become too important for scattered dashboards or
ad hoc SQL. Perez Mola compares analytics engineers with data analysts, data
engineers, and BI developers. The practical boundary is that analytics
engineers encode reusable definitions and quality checks. Analysts focus more
on questions, interpretation, and stakeholder recommendations
([Analytics Engineer Skills and Tools at 14:34-20:19]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})).

The boundary with data engineering is platform ownership. Data engineers often
own ingestion and orchestration, plus raw storage and system reliability.
Analytics engineers depend on that platform. They add domain models, metrics,
semantic layers, and BI-ready marts.

Kwong makes this boundary concrete through ELT. In that ELT flow, source data is
loaded first and warehouse-side transformations serve analytical users
([Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

From the pipeline side, Tuli says ingestion and orchestration handle raw events.
Pre-processing covers ordering, deduplication, and PII masking. Analytics
engineering starts to dominate when teams map entities, foreign keys, business
questions, and metrics into modeled tables
([Modern Data Pipeline Architecture at 37:10-43:05]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

## Role Responsibilities

The archive's practical job description starts with the modeled analytical
layer. Perez Mola describes building tables or views, maintaining pipelines,
checking data quality, and supporting Looker users as day-to-day analytics
engineering work. That responsibility matters because analysts and data
scientists need stable inputs for dashboards, experiments, forecasts, and
decision support
([Analytics Engineer Skills and Tools at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

The output is stronger than a dashboard. It's a governed model with clear
grain, documented columns, and tested assumptions. It also names the consumer.

Perafan contrasts manual dashboard validation with robust data work. His
framing turns repeated business questions into systems that replace recurring
manual checks
([Foundations of the Analytics Engineer Role at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Common responsibilities include SQL transformations and dbt projects, with
dimensional or BI modeling nearby. Tests plus documentation belong in the same
work, along with metric and semantic definitions. Source-change debugging also
belongs there.

The same owner negotiates definitions with analysts and data scientists.
Product managers often join with backend and data engineers.

The role therefore lives close to [metrics]({{ '/wiki/metrics/' | relative_url }})
and [documentation]({{ '/wiki/documentation/' | relative_url }}). It also lives
close to [data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }})
rather than being only a dashboard production role.
([Analytics Engineer Skills and Tools at 14:34-20:19]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

## Core Skills

SQL and modeling are the first skill cluster. Perez Mola starts with SQL, then
adds fact tables and dimension tables. Kimball-style modeling, Snowflake
familiarity, and dbt also matter. So does business-facing data quality.

Perafan uses the same role logic. Models make messy business reality visible
through tables, columns, and relationships.
([Analytics Engineer Skills and Tools at 26:10-30:06 and 42:05-45:16]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations of the Analytics Engineer Role at 20:21-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

The second cluster is software practice applied to SQL. Perez Mola's dbt
discussion puts SQL files in version control. It also links transformations
through a DAG and keeps tests beside transformation code.

Perafan extends that into generic tests and singular SQL tests. Unit tests and
CI checks stop broken assumptions before they reach users.
([Analytics Engineer Skills and Tools at 6:49-10:04 and 36:44-40:42]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Foundations of the Analytics Engineer Role at 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[dbt]({{ '/wiki/dbt/' | relative_url }})).

Communication isn't a soft extra because models have to match the business.
Analytics engineers ask what an entity means and which grain a metric should
use. They also decide which definition stakeholders should share, and which
data-quality failures deserve warnings or hard errors. That makes the role part
technical modeling and part definition stewardship
([Foundations of the Analytics Engineer Role at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

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

## Metric and Event Definitions

Reusable ownership starts before the SQL model. The team has to agree on what
the entities, events, and metrics mean. A revenue mart may need shared
definitions for customer and subscription. It may also need definitions for
invoice, refund, churn, and expansion.

A product mart may need event names, properties, account identity, and
activation definitions. Retention and
experiment exposure definitions often follow.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
archive's clearest product-data version. A tracking plan records events,
properties, types, and owners before instrumentation. Without that plan,
product analytics inherits inconsistent semantics. So do growth reporting and
downstream activation
([Data-Led Growth Stack at 13:34-20:47]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})).

That work belongs close to analytics engineering when the events feed shared
models. Choudhury follows tracked product data through warehouse
transformations and BI. He also connects it to customer-data-platform use cases
and [reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}).

The analytics engineer may not implement the application event, but the role
still protects the model agreement. That agreement covers event meaning,
accepted properties, metric formulas, and grain. It also covers the downstream
surfaces that consume the definition
([Data-Led Growth Stack at 28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Tools in the Stack

dbt appears repeatedly because it packaged software engineering habits for SQL.
Those habits include version control and dependency graphs. They also include
reusable macros, docs, tests, and repeatable runs. Perez Mola uses dbt to
explain analytics engineering through SQL transformations and tests. She also
connects the workflow to a DAG, Snowflake, and Looker.

Maksimovic shows the implementation side through a dbt migration and practical
data modeling work. His stack included Snowplow, dbt, Looker, and Redshift.
Airflow and Airbyte sat nearby.

The useful signal isn't the vendor list. It's
the migration from duplicated dashboard and BI work into modeled layers. LookML,
product analytics, and experiment support came with that migration
([Perez Mola at 6:49-11:48 and 30:06-31:09]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Maksimovic at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

The archive doesn't reduce the discipline to dbt. Kwong situates dbt after
ingestion and storage, alongside Airbyte and warehouses. Orchestration, CDC, and
schema evolution remain part of the same stack.

Analytics engineering inherits source-system and warehouse-cost constraints from
the full platform. Freshness plus orchestration reliability also matter
([Modern Data Stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

Tuli's build-versus-buy discussion adds another constraint. Teams choose tools
based on the pipeline stage they need to control. That choice can include
managed ingestion, Snowflake, and Databricks. It can also include Spark, Kafka
or Kinesis, and orchestrators.

Analytics engineers still need to understand those choices because dbt models
inherit source freshness and late events. They also inherit schema changes and
cost from the platform
([Modern Data Pipeline Architecture at 26:43-37:10]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

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

Tomasz Hinc's GitOps episode makes the handoff with platform teams more
concrete. Data teams can reduce waiting by changing infrastructure through
merge requests. Platform teams still review access and secrets, then set safe
defaults. That operating model matters when analytics engineers maintain
models, warehouses, or scheduled jobs. Those jobs depend on reproducible
environments
([DataOps and GitOps for Data Teams at 12:40-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
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
[From Marketing to Analytics Engineering at 7:18-14:14 and 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Jeff Katz's data engineering curriculum places analytics engineering early in a
career path. The path uses SQL and dbt. It also uses Snowflake, Mode, and
Fivetran. The curriculum covers OLTP versus OLAP concepts and data modeling.

That makes analytics engineering a practical entry point before deeper backend
or cloud specialization. Streaming and ML platforms are later paths
([Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }}),
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})).

For a learning sequence, the archive puts SQL before tool collecting. A
candidate should be able to explain table grain and model one source-to-mart
path. They should add tests and documentation, then expose the model through
BI. After that, the harder work is handling source changes, metric disputes,
and event definition disputes.

Python helps with APIs, orchestration, testing, and glue code. The
analytics-engineering path remains SQL-first in the podcast evidence
([Foundations of the Analytics Engineer Role at 30:35-38:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}),
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})).

Katie Bauer's team-building episode adds a seniority signal for analytics work.
Maintainability, documentation, and peer review turn modeling from personal SQL
skill into team craft. That matters when a data team hires separate product
analysts and analytics engineers. It also matters when marketing scientists own
a distinct surface
([How to Hire, Manage, and Grow a Data Science Team at 6:22-11:58]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).

## Portfolio and Hiring Signals

A strong analytics engineer portfolio proves reusable data work, not only
visualization. Good projects model one business domain from raw source data to
a documented mart. They explain entity grain and transformation layers. They
define metrics, events, and tests.

A good writeup names the BI user or product analyst. For activation work, it
names the workflow that consumes the result.
([Analytics Engineer Skills and Tools at 26:10-30:06 and 36:44-40:42]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

Useful projects include campaign reporting marts and product-events models.
Retention or RFM models, A/B testing metrics layers, and dbt migrations also
work. Maksimovic's dbt migration and product-analytics story support this
portfolio signal. Kwong's ELT episode supports the same
source-to-warehouse-to-mart structure
([From Marketing to Analytics Engineering at 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Modern Data Stack episode at 7:57-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Hiring signals are the reasoning behind the model. A strong resume or project
writeup names the decision owner and source semantics. It also names the model
layers, tests, and failure modes. The dashboard or activation surface matters
too.

For product data projects, include a tracking plan. Show how the same modeled
event data can support BI or reverse ETL. The podcast archive doesn't
present the analytics engineer as a tool
collector. It presents the role as making analytical data safe enough for use
in decisions and workflows.
([Data-Led Growth Stack at 13:34-20:47 and 28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})).

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

Bauer's hiring discussion adds the management view. A team may hire product
analysts, analytics engineers, and marketing scientists as separate roles. Peer
review and maintainable work still make analytics usable after one stakeholder
request becomes repeated team work. Documentation does the same
([How to Hire, Manage, and Grow a Data Science Team]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }}),
[Data Teams]({{ '/wiki/data-teams/' | relative_url }})).

## Related Pages

Use these pages for role boundaries, platform context, and career paths.

- [Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
- [Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [dbt]({{ '/wiki/dbt/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})
