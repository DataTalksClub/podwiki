---
layout: article
title: "Analytics Engineer: Role, Skills, Tools, and Career Path"
keyword: "analytics engineer"
summary: "A podcast-backed guide to reusable analytics model ownership, metric and event definitions, dbt-style testing, portfolio proof, and the analytics engineer career path."
related_wiki:
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Data Analyst vs Analytics Engineer
  - Marketing to Analytics Engineering
  - dbt
  - Metrics
  - Event Tracking
  - Tracking Plans
  - Reverse ETL
  - Analytics Engineering Portfolio Projects
  - Data Quality and Observability
  - Modern Data Stack
---

An analytics engineer turns raw or messy business data into trusted analytical
models. The role sits between analytics and data engineering. The useful
definition is more specific than "half analyst, half engineer." In the
DataTalks.Club archive, analytics engineers own reusable SQL models and tests.
They also own metric definitions.

They prepare data for BI and activation. That keeps analysts, product teams,
growth teams, and data scientists from rebuilding the same joins or arguing
from different definitions
([Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
grounds the job in data modeling, pipeline maintenance, data quality, and
Looker support in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She also ties the role boundary to analysts, data engineers, data scientists,
and backend engineers at 14:34-20:19. [Juan Manuel
Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) adds the deeper
craft in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
He frames analytics engineering as translating business reality into data
systems with enough software rigor to make those systems testable
([11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Use this article when you want the practical role guide. For broader archive
synthesis, start with
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
then use the
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
for a learning sequence.

## Role Responsibilities

An analytics engineer usually owns the modeled analytical layer between raw
source data and business-facing use. Perez Mola describes daily work around
building tables or views and modeling data. She also describes maintaining
pipelines, checking data quality, and supporting Looker users
([role episode at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
That work matters because analysts and data scientists need stable inputs for
dashboards, experiments, forecasts, and decision support.

The output isn't just a dashboard. A stronger output is a governed model with
clear grain, documented columns, tested assumptions, and a named consumer.
Perafan contrasts quick manual checking with robust data work. Teams need
models and tests so every dashboard doesn't become a one-off validation
exercise
([foundations episode at 11:03-18:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Common responsibilities include SQL transformations, `dbt` projects, tests, and
data documentation. The same ownership covers dimensional modeling, metric and
semantic definitions, BI modeling, and source-change debugging. Perez Mola's
role episode connects those tasks to collaboration with analysts, data
scientists, data engineers, and backend engineers
([role episode at 14:34-20:19]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
The
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
comparison expands that boundary.

## Role Boundaries

A data analyst usually owns the question, interpretation, and recommendation.
An analytics engineer owns the reusable model behind repeated analysis. Perez
Mola places the analytics engineer between analyst and data engineer because
analysts shouldn't spend most of their time cleaning the same data. Data
engineers often focus on ingestion, infrastructure, and platform reliability
([role episode at 14:34-20:19]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }}) shows why
the boundary can still blur in real teams. The work mixed BI and dashboards
with `dbt` migration and Looker. It also included LookML, product analytics,
and A/B testing. Use
ownership as the rule because teams still need to separate exploratory analysis
from reusable data assets. That stays true when one person answers the question
and maintains the model
([marketing transition episode at 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

For data engineering, platform ownership sets the boundary. Data engineers tend
to own ingestion, orchestration, storage, and platform reliability.

Analytics engineers depend on that platform. They add business models, tests,
semantic definitions, and BI-ready marts. That keeps the role close to metric
meaning and stakeholder use. The same boundary connects analytics engineering
to [ELT]({{ '/wiki/elt/' | relative_url }}) and
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}). It also
connects the role to
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) makes that ELT
split explicit because teams load raw data first. Analysts and analytics
engineers then transform it in the warehouse with SQL and `dbt`-style work
([ETL, ELT, and the Modern Data Stack at 7:57-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Core Skills

Start with SQL and data modeling. Perez Mola names SQL, fact tables, and
dimension tables as core preparation. She also names Kimball-style modeling,
Snowflake familiarity, `dbt`, and business-facing data quality
([role episode at 26:10-30:06 and 42:05-45:16]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
Perafan makes the same point in role terms. Teams use modeling to make messy
business reality visible in tables, columns, and relationships
([foundations episode at 11:03-18:35 and 20:21-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

After SQL and modeling, add software habits such as version control and tests.
Perez Mola's `dbt` discussion places SQL files in version control. Model
dependencies form a DAG, and documentation and tests travel with the
transformation code
([role episode at 6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Perafan extends that into generic tests and singular SQL tests. He also covers
unit tests and CI checks that stop broken assumptions before they reach users
([foundations episode at 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
Perez Mola gives the practitioner version through `dbt` tests, custom tests,
warnings, and errors
([role episode at 36:44-40:42]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
For a deeper tool-specific branch, use the
[dbt]({{ '/wiki/dbt/' | relative_url }}) page.

Communication is also part of the skill set because models have to match the
business. Analytics engineers ask what an entity means, what grain a metric
should use, and which definition stakeholders should share. That's why the
[Metrics]({{ '/wiki/metrics/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
topics belong in the role, not outside it.

## Metric and Event Definitions

Reusable ownership starts before the SQL model. The team has to agree on what
the entities, events, and metrics mean.

For a revenue mart, that means defining
customer and subscription. Also define invoice, refund, and churn. For a
product mart, define event names and properties. Also define account identity
and the moment a user counts as activated.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
clearest product-data version. A tracking plan records events, properties,
types, and owners before instrumentation. Without that plan, product analytics
inherits inconsistent semantics. So do growth reporting and downstream
activation
([Data-Led Growth Stack at 13:34-20:47]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}),
[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})).

That work belongs close to analytics engineering when the events feed shared
models. Arpit follows tracked product data through warehouse transformations
and BI. He also connects it to customer-data-platform use cases and
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
([28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

The analytics engineer doesn't always implement the event in the application,
but the role should protect the model agreement. That agreement covers event
meaning and grain. It also covers accepted properties, metric formulas, and the
downstream surfaces that consume them.

## Tools in the Stack

The archive treats `dbt` as the clearest tool associated with analytics
engineering, but not as the whole job. Perez Mola uses `dbt` to explain SQL
transformations, documentation, tests, and dependency graphs. She also uses it
to explain version control. In her day-to-day stack, `dbt` sits beside
Snowflake and Looker
([role episode at 6:49-11:48 and 30:06-31:09]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Maksimovic's stack included Snowplow, `dbt`, and Looker, with Redshift as the
warehouse and Airflow plus Airbyte nearby. The useful signal isn't the vendor
list. It's the migration from dashboard and BI work into modeled layers,
LookML, product analytics, and experiment support. The work included
wide-versus-narrow table choices and incrementalization tradeoffs
([marketing transition episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Kwong explains why this stack became common in ELT teams. Raw data arrives in
the warehouse first. SQL with `dbt` then helps analysts and analytics engineers
build modeled tables and marts for business use
([Modern Data Stack episode at 7:57-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }})).

Analytics engineers also borrow reliability habits from DataOps.
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) describes
version control, tests, CI/CD, and observability in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
He also ties runbooks and documentation to dependable data pipelines. Analytics
engineers may not own every platform concern. Their models still become
production dependencies when dashboards, forecasts, or activation flows rely on
them
([DataOps episode at 33:47-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }})).

## Career Path

The most practical path starts with SQL and modeling, then adds tested and
documented projects. Maksimovic's transition from digital marketing started
with Excel, marketing reporting, and a SQL course. The path then moved through
BI-team conversations and real company queries. Dashboard work, Looker, and
eventually `dbt` modeling followed
([marketing transition episode at 7:18-14:14 and 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
That route is covered in more detail in
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }}).

Domain knowledge can help if you convert it into technical proof. Maksimovic's
marketing background supplied funnel context, user-journey intuition, and
stakeholder empathy. That background became useful when paired with SQL and BI
projects. Product analytics support, A/B testing, and data modeling came with
the role
([marketing transition episode at 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

For a learning sequence, start with the
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
and write analytical SQL before anything else. Then explain table grain, model
one source-to-mart path, add tests and documentation, and expose the model
through BI. After that, handle source changes, metric disputes, and event
definition disputes. Python helps with APIs, orchestration, testing, and glue
code. The archive's
analytics-engineering path is still SQL-first rather than Python-first
([foundations episode at 30:35-38:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Portfolio and Hiring Signals

A strong analytics engineer portfolio should prove that you can make data
reusable, not only visualize it. Good projects model one business domain from
raw source data to a documented mart. They explain entity grain and
transformation layers. They also define metrics and events. They show tests and
how a BI user, product analyst, or activation workflow would consume the
result.

Perez Mola's role definition supports that standard
([role episode at 26:10-30:06 and 36:44-40:42]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
So do Maksimovic's `dbt` migration story and Kwong's ELT explanation
([marketing transition episode at 14:14-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[ELT episode at 7:57-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Useful project themes include a campaign reporting mart, a product events
model, a retention or RFM model, and an A/B testing metrics layer. You can also
show a migration from duplicated dashboard SQL into a tested `dbt` project.

Show the reasoning behind the model. Explain why the grain is correct and which
assumptions are tested. Name the metric definition users should trust. Also
show how the model handles source changes.

If the project uses product data, include a tracking plan. Then show how the
same modeled event data can support BI or reverse ETL
([Data-Led Growth Stack at 13:34-20:47 and 28:52-37:25]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
For more project shapes, use
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
and the
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }}).

Hiring managers should see SQL skill and modeling judgment in your resume or
project writeup. They should also see BI awareness, tests, documentation, and
business context. A strong writeup names the decision owner and source
semantics. It also names the model layers, tests, dashboard or activation
surface, and failure modes.

The DataTalks.Club episodes don't present the analytics engineer as a tool
collector. Instead, analytics engineers make analytical data safe enough for
downstream decisions and workflows
([Foundations of the Analytics Engineer Role at 11:03-18:35 and 20:21-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
