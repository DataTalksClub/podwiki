---
layout: wiki
title: "Analytics Engineering"
summary: "Analytics engineering turns raw data into tested models, shared metric definitions, documented transformations, and BI-ready data products."
secondary_keywords:
  - analytics engineer
  - analytics engineer role
  - analytics engineering bootcamp
related:
  - Data Engineering Platforms
  - MLOps
  - DataOps
  - Data Teams
  - Data Product Management
  - Career Transitions in Data
  - dbt
  - Metrics
  - Business Intelligence
  - Event Tracking
  - Tracking Plans
  - Analytics Engineering Portfolio Projects
  - AI Powered Business Intelligence
  - Text-to-SQL
---

Analytics engineering builds reliable analytical data models and transformations,
then adds tests, documentation, and semantic interfaces. It sits between
[[data engineering platforms]]
and analytics. Data engineers make data available as a platform. Analytics
engineers turn that data into reusable business definitions and decision-ready
models.

The role isn't only "SQL plus dashboards."
It combines data modeling and quality checks with metric definitions, event
semantics, the warehouse, and the BI stack. Workflow examples include SQL tests
and DAGs
([[cite:analytics-engineer-skills-tools@06:49=>Analytics Engineer Skills and Tools]]).
[[person:juanmanuelperafan=>Juan Manuel Perafan]] frames
the role as translating business reality into clean data systems with software
engineering discipline
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]).

## Modeled Analytical Layer

Analytics engineers own the modeled analytical layer between raw data and the
people using it. They don't stop at a
one-off query. They maintain models with clear grain, tested assumptions,
documented definitions, and a path into BI or operational use.

Data modeling and dbt tests sit at the center of the job, alongside Looker,
Snowflake, and collaboration
([[cite:analytics-engineer-skills-tools@06:49=>Analytics Engineer Skills and Tools]]).
The same work converts messy business reality into safer data systems
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]).

The role is easiest to explain through the team bottleneck it removes. Analysts
and data scientists need trusted definitions. They can lose time rebuilding
joins and reconciling dashboards. Data engineers often own ingestion,
orchestration, cloud infrastructure, and platform reliability. Analytics
engineers work between those groups by making business-facing data reusable
([[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]],
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]]).

The Spotify-origin story names the bottleneck directly. Analysts were spending
too much time cleaning and quality-checking data. They also had to model data
before they could do analysis
([[cite:analytics-engineer-skills-tools@16:54=>Analytics Engineer Skills and Tools]]).

That reusable layer feeds
[[Business Intelligence]]
when modeled tables and metrics become dashboards, reports, and decision
workflows.

In the pipeline view, dbt sits after ingestion and orchestration. The modeled
marts then tie to dashboards and business questions
([[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]],
[[Modern Data Stack]]).

## Team Role and Platform Handoff

The title matters most when it clarifies ownership of reusable analytical data.
Perez Mola frames a bridge role across analysts and data engineers. BI
developers and platform teams also overlap. Perafan makes a different point.
Many analytics engineering tasks existed before teams gave them a separate title
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].

[[Data Analyst vs Analytics Engineer]] defines the analyst-versus-engineer
boundary. [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics
Engineer]] covers the career sequence from analyst work into this practice.

The platform handoff stays stable because data engineers often own ingestion,
orchestration and raw storage, with reliability beside them. Analytics engineers
depend on that platform, then add domain models and metrics. Semantic layers and
BI-ready marts sit with the same work.
The [[data-roles=>role taxonomy]] behind that split says data engineers make
data available in a usable form for analysts and data scientists. Analytics
engineering starts after that handoff, where reusable business definitions and
quality checks become the product
[[cite:data-team-roles@13:58=>Data Team Roles Explained]].

Kwong's ELT framing puts source loading before warehouse-side transformations
for analytical users
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
When source data is already loaded, an analytics engineer can build warehouse
transformations with SQL and dbt
[[cite:data-engineering-tools-modern-data-stack@12:39=>Modern Data Stack]].
The team doesn't have to wait for engineering to change an upstream pipeline.
The same handoff connects [[Data Engineering Platforms]], [[dbt]], and
[[ETL vs ELT]].

The practical job description starts with the modeled analytical layer.
Day-to-day work can include model builds and pipeline maintenance. It can also
include data-quality checks and Looker support.

The output is stronger than a dashboard. It's a governed model with clear grain
and documented columns. The model also needs tested assumptions and named
consumers
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].
Reusable models may have to serve Finance, Supply Chain, Sales, and other
departments from the same underlying data. In that setting, teams need the
[[data-architect-role=>data architect role]] to connect model grain and shared
definitions across consumers
[[cite:from-iot-data-engineering-to-leading-data-architect@36:00=>From IoT Data Engineering to Data Architecture]].

Common responsibilities include SQL transformations and dbt projects, with
dimensional or BI modeling nearby. Tests plus documentation belong in the same
work, along with metric and semantic definitions. Source-change debugging also
belongs there. That puts the role close to [[metrics]],
[[documentation]], and
[[data-quality-and-observability=>data quality]]
rather than only dashboard production
([[cite:data-engineering-tools-modern-data-stack@31:31=>Modern Data Stack]],
[[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]]).

Team size can move the placement. In Tammy Liang's small-team story, early
analytics work started with business-health monitoring and dashboard adoption.
It later included a warehouse plus dbt. Data Studio and Notion documentation
made the work usable. Tests and forecasting support followed because the company
needed trusted data first
([[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]]).

At larger scale, analytics engineers may start in a platform team. They can
then embed into operations or commercial analytics teams. Domain teams can own
models without depending on a central queue
([[cite:analytics-engineer-skills-tools@48:36=>Analytics Engineer Skills and Tools]],
[[data-engineering-platforms=>Data Engineering Platforms]]).

## Core Skills

SQL and modeling are the first skill cluster. Perez Mola starts with SQL, then
adds fact tables and dimension tables. Kimball-style modeling, Snowflake
familiarity, and dbt also matter. So does business-facing data quality
[[cite:analytics-engineer-skills-tools@42:05=>Analytics Engineer Skills and Tools]].

Perafan uses the same role logic. Models make messy business reality visible
through tables, columns, and relationships
([[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]).

The second cluster is software practice applied to SQL. Perez Mola's dbt
discussion puts SQL files in version control. It also links transformations
through a DAG and keeps tests beside transformation code.

Perafan extends that into generic tests and singular SQL tests. Unit tests and
CI checks stop broken assumptions before they reach users
([[cite:analytics-engineer-skills-tools@06:49=>Analytics Engineer Skills and Tools]],
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]],
[[dbt]]).

Communication isn't a soft extra because models have to match the business.
Analytics engineers ask what an entity means and which grain a metric should
use. They also decide which definitions stakeholders should share and which
data-quality failures need warnings or hard errors. That makes the role part
technical modeling and part definition stewardship
([[cite:analytics-engineer-skills-tools@38:53=>Analytics Engineer Skills and Tools]],
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]],
[[Metrics]]).

When those definitions move from stakeholder language into modeled tables and
dashboards, the work overlaps with the [[data-translator-role=>Data Translator Role]].
The same handoff can include alerts and delivery ownership.[[cite:data-translator-role-and-data-strategy=>Data Translator Role]]

## Modeling and Semantic Layers

The central craft is data modeling. Analytics engineers decide the grain of a
table and separate staging work from business marts. They choose facts and
dimensions, then weigh wide tables against narrower models. Maksimovic connects
these modeling decisions to growth and product work.

His episode covers Looker
reporting, dbt migration, product support, and A/B testing. It also covers
retention analysis and marketing funnels
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]],
[[Product Analytics]]).

The semantic layer is where analytics engineering becomes product work. A model
is valuable when analysts and product teams can reuse a definition without
copying business logic into new queries. Arpit Choudhury extends this from BI
into activation. Tracking plans and warehouses need source awareness. BI
analysis and reverse ETL need documented definitions
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]],
[[Data Product Management]]).

The same semantic layer becomes the grounding layer for
[[ai-powered-business-intelligence=>AI in Business Intelligence]]. If an
assistant writes SQL or summarizes a dashboard, analytics engineering still has
to provide tested models and metric definitions. It also has to keep
documentation and ownership clear. That's the analytics-engineering side of
[[text-to-sql=>Text-to-SQL]].

## Metric and Event Definitions

Reusable ownership starts before the SQL model. The team has to agree on what
the entities, events, and metrics mean. A revenue mart may need shared
definitions for customer and subscription. It may also need definitions for
invoice, refund, churn, and expansion.

A product mart may need event names, properties, account identity, and
activation definitions. Retention and
experiment exposure definitions often follow.

[[person:arpitchoudhury=>Arpit Choudhury]] gives the
clearest product-data version. A tracking plan records events,
properties, types, and owners before instrumentation. Without that plan,
product analytics inherits inconsistent semantics. So do growth reporting and
downstream activation
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]],
[[Tracking Plans]],
[[Event Tracking]]).

That work belongs close to analytics engineering when the events feed shared
models. Choudhury follows tracked product data through warehouse
transformations and BI. He also connects it to
[[customer-data-platforms=>Customer Data Platforms]] use cases and
[[reverse ETL]].

The analytics engineer may not implement the application event, but the role
still protects the model agreement. That agreement covers event meaning,
accepted properties, metric formulas, and grain. It also covers the downstream
surfaces that consume the definition
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]]).

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
([[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]],
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]).

Kwong doesn't reduce the discipline to dbt. He situates dbt after ingestion
and storage, alongside Airbyte and warehouses. Orchestration, CDC, and
schema evolution remain part of the same stack.

Analytics engineering inherits source-system and warehouse-cost constraints from
the full platform. Freshness plus orchestration reliability also matter
([[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]],
[[Modern Data Stack]]).

Tuli's build-versus-buy discussion adds another constraint. Teams choose tools
based on the pipeline stage they need to control. That choice can include
managed ingestion, Snowflake, and Databricks. It can also include Spark, Kafka
or Kinesis, and orchestrators.

Analytics engineers still need to understand those choices because dbt models
inherit source freshness and late events. They also inherit schema changes and
cost from the platform
([[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]],
[[Data Engineering Platforms]]).

## Data Quality and DataOps

Quality examples include non-null tests, uniqueness tests, custom SQL tests,
and macros. Source checks, warnings, and alerts add another layer. The broader
goal is safety.

The push is to stop manual dashboard validation. Engineering rigor then moves
into data workflows
([[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]],
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]).

Christopher Bergh's DataOps episode gives the operating model behind those
practices. It covers version control, tests, CI/CD, and observability. It also
covers automated runbooks, documentation, and end-to-end delivery.

Analytics engineers don't own every platform reliability concern. Their models
still become production dependencies when dashboards or forecasts rely on them
([[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation and Reliable Data Pipelines]],
[[Data Quality and Observability]],
[[DataOps]]).

Tomasz Hinc's GitOps episode makes the handoff with platform teams more
concrete. Data teams can reduce waiting by changing infrastructure through
merge requests. Platform teams still review access and secrets, then set safe
defaults. That operating model matters when analytics engineers maintain
models, warehouses, or scheduled jobs. Those jobs depend on reproducible
environments
([[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]],
[[DataOps]]).

## Business Context and Role Transitions

Business context is an advantage, not a distraction.
Maksimovic's path from marketing into analytics engineering worked because
marketing funnels and stakeholder questions gave the technical work a target.
User journeys and performance feedback loops mattered too.

The missing skills weren't abstract data skills but SQL and BI projects.
Pipeline literacy and Python basics also mattered, along with Looker and dbt.
Modeling practice was another requirement
([[Marketing to Analytics Engineering]],
[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>From Marketing to Analytics Engineering]]).
Analysts who already own dashboards and KPI explanations can use the
[[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
for the same move into model ownership.

Jeff Katz's data engineering curriculum places analytics engineering early in a
career path. The path uses SQL and dbt. It also uses Snowflake, Mode, and
Fivetran. The curriculum covers OLTP versus OLAP concepts and data modeling.

That makes analytics engineering a practical entry point before deeper backend
or cloud specialization. Streaming and ML platforms are later paths
([[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]],
[[Career Transitions in Data]],
[[Analytics Engineering Roadmap]]).

Perez Mola and Perafan put SQL before tool collecting. Candidates should be
able to explain table grain and model one source-to-mart path. They should add
tests and documentation, then expose the result through BI
([[cite:analytics-engineer-skills-tools=>Analytics Engineer Skills and Tools]],
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]]).
[[Analytics Engineering Roadmap]] gives the staged learning path.
[[Analytics Engineering Portfolio Projects]] gives proof-of-work examples.

Katie Bauer's team-building episode adds a seniority signal for analytics work.
Maintainability, documentation, and peer review turn modeling from personal SQL
skill into team craft. That matters when a data team hires separate
[[product-analyst=>product analysts]] and analytics engineers. It also matters
when marketing scientists own a distinct surface
([[cite:hiring-and-managing-data-science-teams-in-b2b-saas@11:58=>How to Hire, Manage, and Grow a Data Science Team]],
[[Software Engineering]]).

Her B2B SaaS example also shows why analytics engineering often appears beside
product analysis and marketing science. The modeled data layer has to support
multiple business surfaces without turning every request into bespoke analysis
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas@06:22=>B2B SaaS Data Team]].

## Adoption Surfaces

Analytics engineering succeeds when modeled data changes how teams work. Liang's
team-building episode starts with dashboards and business-health monitoring. It
then moves into a warehouse, Stitch, GCP, and dbt. Data Studio and Notion docs
make the work usable.

Tests and monitoring help rebuild trust outside the data team. Forecasting and
workshops can do the same
([[cite:building-and-scaling-data-team=>Building and Scaling a Data Team]]).

Those workshops can also become public practitioner sessions. Data Makers Fest
organizers use speaker curation and timetable design to keep analytics
engineering talks useful for a mixed audience. The same program also has to
serve data science and AI audiences
[[cite:s23e09-starting-data-conference-data-makers-fest-story@34:54=>Data Makers Fest keynote fit]].
That connects analytics engineering adoption work to
[[data-ai-conference-building=>data and AI conference building]].

Choudhury's data-led growth stack shows a similar adoption surface for product
and go-to-market teams. Event tracking and tracking plans create demand for
coordination. Warehouse transforms, BI, and reverse ETL add more handoffs. Data
literacy adds a second need. Analytics engineers and data engineers need shared
definitions with analysts and product ops
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]],
[[Data Product Management]]).

Bauer's hiring discussion adds the management view. A team may hire
[[product-analyst=>product analysts]], analytics engineers, and marketing
scientists as separate roles
([[cite:hiring-and-managing-data-science-teams-in-b2b-saas@06:22=>B2B SaaS Data Team]]).
Peer review and maintainable work still make analytics usable after one
stakeholder request becomes repeated team work. Documentation does the same
([[cite:hiring-and-managing-data-science-teams-in-b2b-saas@11:58=>B2B SaaS Data Team]]).

[[Data Teams]] covers the broader org model. [[Team Building]] covers hiring
order, adoption rituals, and management practice.

## Related Pages

Analytics engineering connects role transitions, modeling tools, quality
practice, and activation topics.
- [[Data Analyst vs Analytics Engineer]]
- [[Analytics Engineering Roadmap]]
- [[data-analyst-to-analytics-engineer=>Data Analyst to Analytics Engineer Roadmap]]
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
