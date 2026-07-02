---
layout: article
tags: ["guide"]
title: "Data Roles: Analyst, Data Scientist, Data Engineer, Analytics Engineer, MLE, and Data Product Manager"
keyword: "data roles"
summary: "A podcast-backed guide to common data roles, how their responsibilities differ, how to choose a target role, and what portfolio evidence each role needs."
search_intent: "People searching for data roles want a practical overview of common data job titles, clear boundaries between analyst, data scientist, data engineer, analytics engineer, machine learning engineer, and data product manager, plus guidance on choosing a path and building role-specific portfolio evidence."
related_wiki:
  - Data Analyst Role
  - Data Scientist Role
  - Data Engineer Role
  - Analytics Engineering
  - Machine Learning Engineer Role
  - Data Product Management
  - Career Transitions in Data
---

Data roles are easier to compare by ownership than by title. In
DataTalks.Club role discussions, an analyst explains what happened. A data
scientist turns ambiguous questions into evidence, experiments, and models.

A data engineer makes data reliable enough for other people to use. An
analytics engineer turns raw data into trusted business models. A machine
learning engineer ships model-backed systems. A data product manager decides
which data capability should exist and how success will be measured.

The boundaries move by company size and maturity. The role overview in
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})
separates the team flow, and DataTalks.Club's companion
[Data Team Roles Explained write-up](https://datatalks.club/blog/data-roles.html)
is the canonical role-by-role reference for that breakdown.
Product managers stay close to users, analysts quantify problems and KPIs, and
data scientists predict and evaluate. Data engineers prepare usable data, while
machine learning engineers help scale model-backed services.

In [How to Build and Scale ML Teams]({{ '/podcasts/building-data-team/' | relative_url }}),
[Dat Tran]({{ '/people/dattran/' | relative_url }}) adds the startup version.
Early teams often need generalists first. Specialists become easier to justify
as the product and data platform mature.

Choosing a target role means comparing adjacent responsibilities and building
portfolio evidence that matches the job you want. For deeper role pages,
start with
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}),
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }}), and
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}). Then
compare
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}).

## Common Data Roles

The data analyst role is the best entry point for people who like metrics and
SQL. It also fits people who enjoy dashboards and stakeholder questions.
Analysts help teams understand what happened, why a metric moved, and what
decision should follow.

The role definition episode puts analysts close to product managers because
analysts know company data. They can also quantify whether the team should
solve a problem
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }})).
Podcast discussions on product analytics add experiments to that definition.
They also add funnels, cohorts, and dashboard communication
([Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}),
[Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})).

The data scientist role is broader and less stable. A data scientist may work
on prediction, experimentation, or decision science. The same title can also
mean product analytics or applied machine learning. In the role definition
episode, the simplest split is that analysts explain what happened while data
scientists predict and help integrate predictions into products.

In [CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}), the data science
workflow starts with business understanding. It then moves through data
preparation, modeling, evaluation, and deployment. That makes the job less
about a notebook and more about tested evidence for a decision
([Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})).

The data engineer role owns dependable data movement: engineers ingest and store
data. They transform and orchestrate datasets, then test, document, and operate
them for downstream teams.

The role definition episode describes data engineers as the people who make
user-generated data available in usable form. In
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Roksolana Diachuk]({{ '/people/roksolanadiachuk/' | relative_url }}) grounds
the engineering side in ETL and storage. Spark performance, monitoring, and
schema work also sit on that side
([Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}),
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})).

The analytics engineer role sits between analyst and data engineer. The useful
definition is more precise than "half analyst, half engineer." Analytics
engineers build reusable SQL models and tests. They also own documentation,
semantic definitions, and BI-ready marts.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }})
grounds the role in modeling, data quality, `dbt`, and Looker in
[Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }}).
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) adds
that the role makes business reality visible in safe data systems in
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})
([Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

The machine learning engineer role begins when models need to become reliable
software. MLEs package models and expose inference paths. They build serving
paths, test deployments, and monitor model behavior.

The role definition episode describes MLEs as the people who help data
scientists scale model-backed services. [Ben Wilson]({{ '/people/benwilson/' | relative_url }})
adds the maintainability lens in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
Good ML engineering favors modular systems the team can test and operate
([Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})).

The data product manager role owns product judgment around data capabilities.
That capability might be a dashboard, metric layer, or recommender. It might
also be a data platform or MLOps platform.
[Sara Menefee]({{ '/people/saramenefee/' | relative_url }})
describes the role through customer discovery and hypothesis formation.

Data literacy and launch work also belong in the role. Quality and
documentation appear there too in
[Product Designer to Data Product Manager]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}).
[Greg Coquillo]({{ '/people/gregcoquillo/' | relative_url }}) adds roadmaps
and customer journey mapping. He also adds success metrics and problem-first AI
product work in
[Build & Scale Data Products for AI]({{ '/podcasts/building-and-scaling-ai-data-products-with-mlops/' | relative_url }})
([Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}),
[Data Products]({{ '/wiki/data-products/' | relative_url }})).

## Role Boundaries

Analyst versus data scientist is usually a split between explanation and
prediction, but the boundary is fuzzy. Analysts often own SQL, dashboards, and
metrics. Cohort analysis and experiment readouts can sit there too.

Data scientists add heavier modeling, experiment design, predictive features,
and uncertainty analysis. In
[Hiring Data Scientists and Analysts]({{ '/podcasts/hiring-data-scientists-and-analysts/' | relative_url }}),
[Alicja Notowska]({{ '/people/alicjanotowska/' | relative_url }}) treats title
ambiguity as a hiring reality. The actual responsibilities matter more than the
label
([Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}),
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})).

Data scientist versus data engineer is a split between decision logic and data
systems. Data scientists own framing and feature reasoning. They also own
modeling, evaluation, and interpretation. Data engineers own ingestion and
storage. They also own orchestration, schemas, quality checks, and platform
reliability.

Roksolana Diachuk places data cleaning and feature engineering near data
science. Model cycles sit there too. ETL and storage stay closer to data
engineering, along with Spark optimization, monitoring, and schema changes
([Data Engineer vs Data Scientist]({{ '/wiki/data-engineer-vs-data-scientist/' | relative_url }})).

Data analyst versus analytics engineer is a split between interpreting
questions and maintaining reusable analytical assets. Analysts answer product
and business questions. Analytics engineers encode trusted models, metric
definitions, tests, and documentation so other people don't rebuild the same
logic in every dashboard.

[Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
shows the overlap in
[From Marketing to Analytics Engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}).
Marketing reporting and SQL can sit on the path from analyst-like work into
analytics engineering. Looker, product analytics, `dbt`, and A/B testing can
join the same path
([Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }})).

Data engineer versus analytics engineer is a split between platform paths and
business-facing models. Data engineers tend to own ingestion and orchestration.
Raw storage and runtime reliability sit there too.

Analytics engineers depend
on those paths. They then add modeled domains, semantic definitions, and
BI-ready marts. Tests and documentation sit with that work too.

The boundary is clear in modern-stack discussions such as
[ETL, ELT, and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places data
marts after ingestion and storage. She places ELT transformations before those
marts
([Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})).

Data scientist versus machine learning engineer is a split between model
reasoning and production ownership. Data scientists usually own the problem,
data, features, and model choice. They also own evaluation and interpretation.

ML engineers own packaging and serving, plus scalability and maintainability.
They also own deployment and runtime behavior. The split moves in small teams.
The handoff is visible whenever a model becomes a batch job or API. It's also
visible when a model becomes a monitored service or product feature
([Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }})).

Data product manager versus every technical role is a split between product
decision and implementation. The data product manager decides which user
problem matters, which outcome proves success, which constraints set the
roadmap, and how adoption will happen. Technical leads and contributors decide
how to build the solution. [Geo Jolly]({{ '/people/geojolly/' | relative_url }})
makes that split concrete in
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }}).
The PM defines the problem and target outcome, while the engineering team
defines the solution
([ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }})).

## Choosing a Target Data Role

Choose the role by the work you want to own every week:

- If you like business questions, SQL, dashboards, and metric movement, start
  with the [data analyst role]({{ '/wiki/data-analyst-role/' | relative_url }}).
- If you like prediction, experiments, ambiguity, and model evaluation, compare
  [data science careers]({{ '/wiki/data-science-careers/' | relative_url }}) with
  the [data scientist role]({{ '/wiki/data-scientist-role/' | relative_url }}).
- If you like systems, data movement, and reliability, use the
  [data engineering roadmap]({{ '/wiki/data-engineer-roadmap/' | relative_url }}).

If you like SQL and business meaning, analytics engineering is a strong target
when you want more software rigor than dashboard work usually offers. The
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }})
keeps the sequence practical. Start with SQL and modeling. Then add
`dbt`-style projects, tests, documentation, and BI consumption.
The
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})
is the focused transition path for analysts.

If you already write production software and want to move toward models, use
[Software Engineer to Machine Learning]({{ '/wiki/software-engineer-to-machine-learning/' | relative_url }})
and the
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}).

If you like discovery and stakeholder translation, consider data product
management. Roadmaps, adoption, and measurement belong in that path too. The
path rewards product sense and enough data literacy to make credible tradeoffs.
It doesn't require
replacing the data engineer, data scientist, or ML engineer. It does require
understanding what their work costs and what users need from the result
([Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

Team stage matters too because Dat Tran's team-building episode argues that
early startups often need T-shaped generalists. They may need to move across
product, data engineering, and ML. Later teams can afford more specialization
([How to Build and Scale ML Teams]({{ '/podcasts/building-data-team/' | relative_url }})).
That means a first data hire may do analyst, engineer, scientist, and product
work in the same month. A mature platform team may split those same
responsibilities across several people.

For career changers, DataTalks.Club guests repeatedly advise translating prior
work into role evidence. [Ksenia Legostay]({{ '/people/ksenialegostay/' | relative_url }})
turned project management and KPI work into data science evidence in
[Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}).
Nikola Maksimovic turned marketing funnels and reporting into analytics
engineering evidence. [Santiago Valdarrama]({{ '/people/svpino/' | relative_url }})
turned software engineering into ML system work in
[Software Engineering to Machine Learning]({{ '/podcasts/from-software-engineer-to-machine-learning/' | relative_url }}).
The target role decides which old skill is an asset and which gap you need to
close
([Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})).

## Portfolio Evidence by Role

A data analyst portfolio should prove SQL and metric thinking. It should also
show visualization and recommendation quality. A good project starts with a
business or product question. It then shows data checks, cohort or funnel logic,
and dashboard design. It should finish with a written decision.

Product analytics projects should explain events, segments, and metric
definitions. They should also name caveats
([Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[Experimentation]({{ '/wiki/experimentation/' | relative_url }})).


A data scientist portfolio should prove problem framing and baselines. It should
show data preparation, modeling, evaluation, and communication.

CRISP-DM starts the project with business understanding, which makes it a good
portfolio template.

Luke Whipps gives the hiring version: projects should connect the claimed tech
stack to concrete work and business impact.

A data engineering portfolio should prove that data can run without manual
notebook work. Build a pipeline from source data to modeled tables. Add tests
or quality checks, then document the schema and make reruns inspectable.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) emphasizes SQL, Python,
and cloud fundamentals in his data engineering career and job-prep episodes.
Docker and Airflow also appear there, along with warehouses
([Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}),
[Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})).

An analytics engineering portfolio should prove reusable modeling. Show raw
source assumptions and staging models, then show marts, tests, and
documentation. Add one BI or query layer that consumes the shared model.
Explain table grain and metric definitions.

Victoria Perez Mola's role episode and Juan Manuel Perafan's foundations
episode both reward modeling and tests over dashboard-only proof
([Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})).

A machine learning engineering portfolio should prove that a model-backed
system can run, change, and fail predictably. A training script plus batch
scoring job can be stronger than an advanced model with no run path. Add an API
or CLI, Docker, tests, and evaluation. Add monitoring notes and a simple
deployment path.

Ben Wilson's production ML discussion and
[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }})'s
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})
both make requirements and modular code part of ML engineering evidence. Tests
and deployment gaps matter too
([Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})).

A data product manager portfolio should prove product judgment around a data
capability. Write a short case study that names the user and workflow. Add the
pain point and candidate solution. Include tradeoffs, a roadmap, and a success
metric. Cover launch risk and adoption too.

Greg Coquillo's roadmap and success-metrics discussion supports that structure,
while Geo Jolly's ML platform episode adds the internal-product version.
Interview users and prioritize platform gaps. Define adoption metrics and
explain why a capability should ship now
([Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}),
[ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }})).

## Learning Paths and Next Steps

Start with the role page closest to the work you want, then use one roadmap and
one portfolio page. For analyst or product analytics paths, read
[Data Analyst Role]({{ '/wiki/data-analyst-role/' | relative_url }}),
[Data Analyst Careers]({{ '/wiki/data-analyst-careers/' | relative_url }}),
and [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}). For
data science, use
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }}),
[Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }}),
and [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}).

For data engineering, use
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}),
[Data Engineering Roadmap]({{ '/wiki/data-engineer-roadmap/' | relative_url }}),
and [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}).
For analytics engineering, use
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[Analytics Engineering Roadmap]({{ '/wiki/analytics-engineering-roadmap/' | relative_url }}),
and
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }}).
Analysts can use
[Data Analyst to Analytics Engineer Roadmap]({{ '/wiki/data-analyst-to-analytics-engineer/' | relative_url }})
for the role-specific transition.

For ML engineering, use
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
and [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}).

For product paths, start with
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
and [Data Products]({{ '/wiki/data-products/' | relative_url }}). Then use
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
and
[Data Product Manager]({{ '/wiki/data-product-manager/' | relative_url }}).

The practical sequence is the same across roles. Choose one target, build one
project that proves the target responsibility, and write the case study in the
language of that role. Recruiters and hiring managers shouldn't have to infer
whether you want analytics, data science, or data engineering. They also
shouldn't have to infer whether you want ML engineering or data product work.
Your project, resume, and interview story should make that choice visible.

