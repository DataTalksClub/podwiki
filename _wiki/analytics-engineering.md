---
layout: wiki
title: "Analytics Engineering"
summary: "How DataTalks.Club episodes describe analytics engineering as the discipline of building trusted analytical models, transformations, metric definitions, tests, documentation, and BI-ready data products."
related:
  - Data Engineering Platforms
  - MLOps
  - DataOps
  - Data Product Management
  - Career Transitions in Data
  - dbt
  - Metrics
  - Business Intelligence
  - Event Tracking
  - Tracking Plans
  - Analytics Engineering Portfolio Projects
---

Analytics engineering builds reliable analytical data models and transformations,
then adds tests, documentation, and semantic interfaces. In DataTalks.Club
episodes, it sits between
[[data engineering platforms]]
and analytics. Data engineers make data available as a platform. Analytics
engineers turn that data into reusable business definitions and decision-ready
models.

The role isn't only "SQL plus dashboards."
[[person:victoriaperezmola|Victoria Perez Mola]] grounds the job in
[[podcast:analytics-engineer-skills-tools|data modeling and quality checks]].
It also covers metric definitions, event semantics, the warehouse, and the BI
stack. The workflow examples include SQL tests and DAGs. In
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Juan Manuel Perafan's foundations episode]],
[[person:juanmanuelperafan|Perafan]]
describes the role as translating business reality into clean data systems with
software engineering discipline.

## Modeled Analytical Layer

In the DataTalks.Club discussions, analytics engineers own the modeled
analytical layer between raw data and the people using it. They don't stop at a
one-off query. They maintain models with clear grain, tested assumptions,
documented definitions, and a path into BI or operational use.

Perez Mola puts data modeling and dbt tests at the center of the job. She also
connects analytics engineering to Looker, Snowflake, and collaboration. Perafan
describes the same work as converting messy business reality into safer data
systems
([[podcast:analytics-engineer-skills-tools|Perez Mola]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Perafan]]).

Several episodes explain the role through the team bottleneck it removes.
Analysts and data scientists need trusted definitions, but they can lose time
rebuilding joins and reconciling dashboards. Data engineers often own ingestion,
orchestration, cloud infrastructure, and platform reliability. Analytics
engineers work between those groups by making business-facing data reusable
([[podcast:data-engineering-career-path-and-skills|Data Engineering Career Path and Skills]],
[[podcast:data-engineering-tools-modern-data-stack|Modern Data Stack episode]]).

That reusable layer feeds
[[Business Intelligence]]
when modeled tables and metrics become dashboards, reports, and decision
workflows.

Santona Tuli adds the pipeline view. Her modern data pipeline discussion puts
dbt after ingestion and orchestration. It then ties modeled marts to dashboards
and business questions at 24:57, 39:23, and 43:05
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]],
[[Modern Data Stack]]).

## Separate Role or Shared Practice

Guests draw the role boundary differently depending on the team. Perez Mola
describes a bridge role that overlaps with analysts, data engineers, BI
developers, and platform teams. Perafan is more explicit that many analytics
engineering tasks existed before teams gave them a separate title.

The title helps when it clarifies who owns modeling and testing. It's less
useful as a rigid job boundary
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]]).

The same flexibility shows up in tool choices. dbt is the clearest recurring
symbol of analytics engineering because it made SQL transformations visible as a
DAG, versioned, and testable.
[[person:nikolamaksimovic|Nikola Maksimovic]] adds
Looker migration, product analytics, A/B testing, and table design.

Natalie Kwong places dbt inside a broader ELT flow with ingestion and
warehouses. She also connects it to orchestration, CDC, and reverse data flows
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic]],
[[podcast:data-engineering-tools-modern-data-stack|Kwong]]).

Team size can move the boundary again. In Tammy Liang's small-team story, early
analytics work started with business-health monitoring and dashboard adoption.
It later included a warehouse, dbt, Data Studio, and Notion documentation. Tests
and forecasting support followed. That work crossed analyst and engineer
responsibilities because the company needed trusted data first
([[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]]).

Rishabh Bhargava's analytics-to-ML discussion shows another boundary.
Analytics engineering can bridge notebooks and SQL-plus-Python work into
production ML, but the goals still differ. Analytics work explains business
behavior, while ML systems serve predictions under operational constraints
([[podcast:production-ml-mlops-and-data-team-building|Production ML and Data Team Building]],
[[Machine Learning Engineer Role]]).

## Role Boundaries

Analytics engineering is easiest to identify by the problem it owns. The
repeated analytical logic has become too important for scattered dashboards or
ad hoc SQL. Perez Mola compares analytics engineers with data analysts, data
engineers, and BI developers. The practical boundary is that analytics
engineers encode reusable definitions and quality checks. Analysts focus more
on questions, interpretation, and stakeholder recommendations
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 14:34-20:19]],
[[Data Analyst vs Analytics Engineer]]).

The boundary with data engineering is platform ownership. Data engineers often
own ingestion and orchestration, plus raw storage and system reliability.
Analytics engineers depend on that platform. They add domain models, metrics,
semantic layers, and BI-ready marts.

Kwong makes this boundary concrete through ELT. In that ELT flow, source data is
loaded first and warehouse-side transformations serve analytical users
([[podcast:data-engineering-tools-modern-data-stack|Modern Data Stack episode]],
[[Data Engineering Platforms]]).

From the pipeline side, Tuli says ingestion and orchestration handle raw events.
Pre-processing covers ordering, deduplication, and PII masking. Analytics
engineering starts to dominate when teams map entities, foreign keys, business
questions, and metrics into modeled tables
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture at 37:10-43:05]]).

## Role Responsibilities

Perez Mola's practical job description starts with the modeled analytical
layer. She describes building tables or views, maintaining pipelines, checking
data quality, and supporting Looker users as day-to-day analytics engineering
work. That responsibility matters because analysts and data scientists need
stable inputs for dashboards, experiments, forecasts, and decision support
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 4:05-10:04]]).

The output is stronger than a dashboard. It's a governed model with clear
grain, documented columns, and tested assumptions. It also names the consumer.

Perafan contrasts manual dashboard validation with robust data work. His
framing turns repeated business questions into systems that replace recurring
manual checks
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role at 11:03-18:35]]).

Common responsibilities include SQL transformations and dbt projects, with
dimensional or BI modeling nearby. Tests plus documentation belong in the same
work, along with metric and semantic definitions. Source-change debugging also
belongs there.

The same owner negotiates definitions with analysts and data scientists.
Product managers often join with backend and data engineers.

The role therefore lives close to [[metrics]]
and [[documentation]]. It also lives
close to [[data-quality-and-observability|data quality]]
rather than being only a dashboard production role.
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 14:34-20:19]]).

## Core Skills

SQL and modeling are the first skill cluster. Perez Mola starts with SQL, then
adds fact tables and dimension tables. Kimball-style modeling, Snowflake
familiarity, and dbt also matter. So does business-facing data quality.

Perafan uses the same role logic. Models make messy business reality visible
through tables, columns, and relationships.
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 26:10-30:06 and 42:05-45:16]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role at 20:21-26:23]]).

The second cluster is software practice applied to SQL. Perez Mola's dbt
discussion puts SQL files in version control. It also links transformations
through a DAG and keeps tests beside transformation code.

Perafan extends that into generic tests and singular SQL tests. Unit tests and
CI checks stop broken assumptions before they reach users.
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 6:49-10:04 and 36:44-40:42]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role at 38:41-46:34]],
[[dbt]]).

Communication isn't a soft extra because models have to match the business.
Analytics engineers ask what an entity means and which grain a metric should
use. They also decide which definition stakeholders should share, and which
data-quality failures deserve warnings or hard errors. That makes the role part
technical modeling and part definition stewardship
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role at 11:03-18:35]],
[[Metrics]]).

## Modeling and Semantic Layers

The central craft is data modeling. Analytics engineers decide the grain of a
table and separate staging work from business marts. They choose facts and
dimensions, then weigh wide tables against narrower models. Maksimovic connects
these modeling decisions to growth and product work.

His episode covers Looker
reporting, dbt migration, product support, and A/B testing. It also covers
retention analysis and marketing funnels
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]],
[[Product Analytics]]).

The semantic layer is where analytics engineering becomes product work. A model
is valuable when analysts and product teams can reuse a definition without
copying business logic into new queries. Arpit Choudhury extends this from BI
into activation. Tracking plans and warehouses need source awareness. BI
analysis and reverse ETL need documented definitions
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]],
[[Data Product Management]]).

## Metric and Event Definitions

Reusable ownership starts before the SQL model. The team has to agree on what
the entities, events, and metrics mean. A revenue mart may need shared
definitions for customer and subscription. It may also need definitions for
invoice, refund, churn, and expansion.

A product mart may need event names, properties, account identity, and
activation definitions. Retention and
experiment exposure definitions often follow.

[[person:arpitchoudhury|Arpit Choudhury]] gives the
clearest product-data version. A tracking plan records events,
properties, types, and owners before instrumentation. Without that plan,
product analytics inherits inconsistent semantics. So do growth reporting and
downstream activation
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack at 13:34-20:47]],
[[Tracking Plans]],
[[Event Tracking]]).

That work belongs close to analytics engineering when the events feed shared
models. Choudhury follows tracked product data through warehouse
transformations and BI. He also connects it to customer-data-platform use cases
and [[reverse ETL]].

The analytics engineer may not implement the application event, but the role
still protects the model agreement. That agreement covers event meaning,
accepted properties, metric formulas, and grain. It also covers the downstream
surfaces that consume the definition
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack at 28:52-37:25]]).

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
([[podcast:analytics-engineer-skills-tools|Perez Mola at 6:49-11:48 and 30:06-31:09]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic at 18:34-33:46]]).

The podcast discussions don't reduce the discipline to dbt. Kwong situates dbt after
ingestion and storage, alongside Airbyte and warehouses. Orchestration, CDC, and
schema evolution remain part of the same stack.

Analytics engineering inherits source-system and warehouse-cost constraints from
the full platform. Freshness plus orchestration reliability also matter
([[podcast:data-engineering-tools-modern-data-stack|Modern Data Stack episode]],
[[Modern Data Stack]]).

Tuli's build-versus-buy discussion adds another constraint. Teams choose tools
based on the pipeline stage they need to control. That choice can include
managed ingestion, Snowflake, and Databricks. It can also include Spark, Kafka
or Kinesis, and orchestrators.

Analytics engineers still need to understand those choices because dbt models
inherit source freshness and late events. They also inherit schema changes and
cost from the platform
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture at 26:43-37:10]],
[[Data Engineering Platforms]]).

## Data Quality and DataOps

Analytics engineering quality work is continuous in Perez Mola's examples of
non-null tests and uniqueness tests. She also discusses custom SQL tests and
macros. Source checks, warnings, and alerts matter too. Perafan broadens that
into safety.

His episode asks teams to stop manually validating dashboards. It argues for
engineering rigor in data workflows
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools]],
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]]).

Christopher Bergh's DataOps episode gives the operating model behind those
practices. It covers version control, tests, CI/CD, and observability. It also
covers automated runbooks, documentation, and end-to-end delivery.

Analytics engineers don't own every platform reliability concern. Their models
still become production dependencies when dashboards or forecasts rely on them
([[podcast:dataops-automation-and-reliable-data-pipelines|DataOps Automation and Reliable Data Pipelines]],
[[Data Quality and Observability]],
[[DataOps]]).

Tomasz Hinc's GitOps episode makes the handoff with platform teams more
concrete. Data teams can reduce waiting by changing infrastructure through
merge requests. Platform teams still review access and secrets, then set safe
defaults. That operating model matters when analytics engineers maintain
models, warehouses, or scheduled jobs. Those jobs depend on reproducible
environments
([[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams at 12:40-26:21]],
[[DataOps]]).

## Business Context and Career Paths

Guests treat business context as an advantage, not a distraction.
Maksimovic's path from marketing into analytics engineering worked because
marketing funnels and stakeholder questions gave the technical work a target.
User journeys and performance feedback loops mattered too.

The missing skills weren't abstract data skills but SQL and BI projects.
Pipeline literacy and Python basics also mattered, along with Looker and dbt.
Modeling practice was another requirement
([[Marketing to Analytics Engineering]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering at 7:18-14:14 and 38:27-41:50]]).
Analysts who already own dashboards and KPI explanations can use the
[[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
for the same move into model ownership.

Jeff Katz's data engineering curriculum places analytics engineering early in a
career path. The path uses SQL and dbt. It also uses Snowflake, Mode, and
Fivetran. The curriculum covers OLTP versus OLAP concepts and data modeling.

That makes analytics engineering a practical entry point before deeper backend
or cloud specialization. Streaming and ML platforms are later paths
([[podcast:data-engineering-career-path-and-skills|Data Engineering Career Path and Skills]],
[[Career Transitions in Data]],
[[Analytics Engineering Roadmap]]).

For a learning sequence, Perez Mola and Perafan put SQL before tool collecting.
A candidate should be able to explain table grain and model one source-to-mart
path. They should add tests and documentation, then expose the model through BI.
After that, the harder work is handling source changes, metric disputes, and
event definition disputes.

Python helps with APIs, orchestration, testing, and glue code. The
analytics-engineering path remains SQL-first in the podcast evidence
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role at 30:35-38:35]],
[[Analytics Engineering Roadmap]]).

Katie Bauer's team-building episode adds a seniority signal for analytics work.
Maintainability, documentation, and peer review turn modeling from personal SQL
skill into team craft. That matters when a data team hires separate product
analysts and analytics engineers. It also matters when marketing scientists own
a distinct surface
([[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|How to Hire, Manage, and Grow a Data Science Team at 6:22-11:58]]).

## Portfolio and Hiring Signals

A strong analytics engineer portfolio proves reusable data work, not only
visualization. Good projects model one business domain from raw source data to
a documented mart. They explain entity grain and transformation layers. They
define metrics, events, and tests.

A good writeup names the BI user or product analyst. For activation work, it
names the workflow that consumes the result.
([[podcast:analytics-engineer-skills-tools|Analytics Engineer Skills and Tools at 26:10-30:06 and 36:44-40:42]],
[[Analytics Engineering Portfolio Projects]]).

Useful projects include campaign reporting marts and product-events models.
Retention or RFM models, A/B testing metrics layers, and dbt migrations also
work. Maksimovic's dbt migration and product-analytics story support this
portfolio signal. Kwong's ELT episode supports the same
source-to-warehouse-to-mart structure
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering at 14:14-33:46]],
[[podcast:data-engineering-tools-modern-data-stack|Modern Data Stack episode at 7:57-18:47]]).

Hiring signals are the reasoning behind the model. A strong resume or project
writeup names the decision owner and source semantics. It also names the model
layers, tests, and failure modes. The dashboard or activation surface matters
too.

For product data projects, include a tracking plan. Show how the same modeled
event data can support BI or reverse ETL. These podcast discussions don't
present the analytics engineer as a tool collector. They present the role as
making analytical data safe enough for use in decisions and workflows.
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack at 13:34-20:47 and 28:52-37:25]],
[[Dashboard and Metric Layer Project Checklist]]).

## Team Design and Adoption

Analytics engineering succeeds when modeled data changes how teams work. Liang's
team-building episode starts with dashboards and business-health monitoring. It
then moves into a warehouse, Stitch, GCP, and dbt. Data Studio and Notion docs
make the work usable.

Tests, monitoring, forecasting, and workshops help rebuild trust outside the
data team
([[podcast:building-and-scaling-data-team|Building and Scaling a Data Team]]).

Choudhury's data-led growth stack shows a similar adoption surface for product
and go-to-market teams. Event tracking and tracking plans create demand for
coordination. Warehouse transforms, BI, and reverse ETL add more handoffs. Data
literacy adds a second need. Analytics engineers and data engineers need shared
definitions with analysts and product ops
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth Stack]],
[[Data Product Management]]).

Bauer's hiring discussion adds the management view. A team may hire product
analysts, analytics engineers, and marketing scientists as separate roles. Peer
review and maintainable work still make analytics usable after one stakeholder
request becomes repeated team work. Documentation does the same
([[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|How to Hire, Manage, and Grow a Data Science Team]],
[[Data Teams]]).

## Related Pages

These pages cover role boundaries, platform context, and career paths.

- [[Data Analyst vs Analytics Engineer]]
- [[Analytics Engineering Roadmap]]
- [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
- [[Analytics Engineering Portfolio Projects]]
- [[Marketing to Analytics Engineering]]
- [[Modern Data Stack]]
- [[dbt]]
- [[Metrics]]
- [[Event Tracking]]
- [[Tracking Plans]]
- [[Reverse ETL]]
- [[Data Quality and Observability]]
- [[Data Engineering Platforms]]
- [[DataOps]]
- [[Data Product Management]]
- [[Product Analytics]]
- [[Career Transitions in Data]]
