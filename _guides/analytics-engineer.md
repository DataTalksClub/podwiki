---
layout: article
title: "Analytics Engineer: Role, Skills, Tools, and Career Path"
keyword: "analytics engineer"
summary: "A podcast-backed guide to what an analytics engineer does, how the role differs from data analyst and data engineer jobs, which skills matter, and how to build a career path."
related_wiki:
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Data Analyst vs Analytics Engineer
  - Marketing to Analytics Engineering
  - dbt
  - Data Quality and Observability
  - Modern Data Stack
---

An analytics engineer turns raw or messy business data into trusted analytical
models. The role sits between analytics and data engineering, but the useful
definition is more specific than "half analyst, half engineer." In the
DataTalks.Club archive, analytics engineers own reusable SQL models, tests, and
metric definitions. They also prepare BI-ready data so analysts, product teams,
and data scientists don't rebuild the same joins
([Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
grounds the job in data modeling, pipeline maintenance, and data quality in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
She also ties the role to Looker, `dbt`, and warehouse work. [Juan Manuel
Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) adds the deeper
craft in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }}).
Analytics engineering turns business reality into data systems with enough
software rigor to make those systems testable and safe.

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
clear grain, documented columns, and tested assumptions. Teams should be able
to push that model into BI or activation. Perafan contrasts fast manual
checking with robust data work. Teams need models and tests so every dashboard
doesn't become a one-off validation exercise
([foundations episode at 11:03-18:35 and 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

Common responsibilities include SQL transformations, `dbt` projects, tests, and
data documentation. They also include dimensional modeling, metric definitions,
BI modeling, and debugging source changes. Perez Mola's role episode connects
those tasks to collaboration with analysts, data scientists, and backend
engineers. The
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})
comparison expands that boundary.

## Role Boundaries

A data analyst usually owns the question, interpretation, and recommendation.
An analytics engineer owns the reusable model behind repeated analysis. Perez
Mola places the analytics engineer between analyst and data engineer because
analysts shouldn't spend most of their time cleaning the same data. Data
engineers often focus on ingestion, infrastructure, and platform reliability
([role episode at 14:34-19:05]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})'s example is messier.
The role mixed BI and dashboards with `dbt`, Looker, product analytics, and
A/B testing. Use ownership as the rule because teams still need to separate
exploratory analysis from reusable data assets. That stays true when one person
answers the question and maintains the model
([marketing transition episode at 14:14-28:40]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

For data engineering, platform ownership sets the boundary. Data engineers tend
to own ingestion, orchestration, storage, and platform reliability.

Analytics engineers depend on that platform. They add business models, tests,
semantic definitions, and BI-ready marts. That keeps the role close to metric
meaning and stakeholder use. The same boundary connects analytics engineering
to the [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

## Core Skills

Start with SQL and data modeling. Perez Mola names SQL, fact tables, and
dimension tables as core preparation. She also names Kimball-style modeling, Snowflake
familiarity, and business-facing data quality
([role episode at 26:10-29:15 and 42:05-45:16]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).
Perafan makes the same point in role terms. Teams use modeling to make messy
business reality visible in tables, columns, and relationships
([foundations episode at 11:03-26:23]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

After SQL and modeling, add software habits such as version control and tests.
Perez Mola's `dbt` discussion places SQL files in version control. Model
dependencies form a DAG, and documentation and tests travel with the
transformation code
([role episode at 6:49-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Perafan extends that into generic tests and singular SQL tests. He also covers
unit tests and CI checks that stop broken assumptions before they reach users
([foundations episode at 38:41-46:34]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).
For a deeper tool-specific branch, use the
[dbt]({{ '/wiki/dbt/' | relative_url }}) page.

Communication is also part of the skill set because models have to match the
business. Analytics engineers ask what an entity means, what grain a metric
should use, and which definition stakeholders should share. That's why the
[Metrics]({{ '/wiki/metrics/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
topics belong in the role, not outside it.

## Tools in the Stack

The archive treats `dbt` as the clearest tool associated with analytics
engineering, but not as the whole job. Perez Mola uses `dbt` to explain SQL
transformations, documentation, tests, and dependency graphs. She also uses it
to explain version control. In her day-to-day stack, `dbt` sits beside
Snowflake and Looker
([role episode at 6:49-11:48 and 30:06-31:09]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})).

Maksimovic's stack included Snowplow, `dbt`, and Looker, with Redshift as the
warehouse and Airflow plus Airbyte nearby.
She learned data modeling through a `dbt` migration rather than through tool
study alone. She worked through transformation layers, wide-versus-narrow table
choices, and incrementalization tradeoffs
([marketing transition episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

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

The most practical path is SQL first, then modeling, then tested and documented
projects. Maksimovic's transition from digital marketing started with Excel,
marketing reporting, and a SQL course. She then moved through BI-team
conversations, real company queries, and dashboard work. Looker and eventually
`dbt` modeling came next
([marketing transition episode at 7:18-14:14 and 41:50-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
That route is covered in more detail in
[Marketing to Analytics Engineering]({{ '/wiki/marketing-to-analytics-engineering/' | relative_url }}).

Domain knowledge can help if you convert it into technical proof. Maksimovic's
marketing background gave her funnel context, user-journey intuition, and
stakeholder empathy. She made that background useful by pairing it with SQL and
BI projects. Product analytics support, A/B testing, and data modeling came
with the role
([marketing transition episode at 38:27-41:50]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

For a learning sequence, start with the
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
and write analytical SQL before anything else. Then explain table grain, model
one source-to-mart path, add tests and documentation, and expose the model
through BI. After that, handle source changes or metric disputes. Python helps
with APIs, orchestration, testing, and glue code. The archive's
analytics-engineering path is still SQL-first rather than Python-first
([foundations episode at 30:35-38:35]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

## Portfolio and Hiring Signals

A strong analytics engineer portfolio should prove that you can make data
reusable, not only visualize it. Good projects model one business domain from
raw source data to a documented mart. They explain entity grain, metric
definitions, and transformation layers. They also show tests and how a BI user
would consume the result. Perez Mola's role definition and Maksimovic's `dbt`
migration story both support that standard
([role episode at 4:05-10:04]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}),
[marketing transition episode at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Useful project themes include a campaign reporting mart, a product events
model, a retention or RFM model, and an A/B testing metrics layer. You can also
show a migration from duplicated dashboard SQL into a tested `dbt` project.
Show the reasoning behind the model. Explain why the grain is correct, which
assumptions are tested, which metric definition users should trust, and how the
model handles source changes. For more project shapes, use
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }}).

Hiring managers should see SQL skill and modeling judgment in your resume or
project writeup. They should also see BI awareness, tests, documentation, and
business context. The DataTalks.Club episodes don't present the analytics
engineer as a tool collector. They present the role as the person who makes
analytical data safe enough for other people to build decisions on.
