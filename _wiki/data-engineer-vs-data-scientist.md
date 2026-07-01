---
layout: wiki
title: "Data Engineer vs Data Scientist"
summary: "A podcast-backed comparison of the data engineer and data scientist role boundary: data paths, modeling, feature work, production handoffs, hiring signals, and team ownership."
related:
  - Data Engineer Role
  - Data Scientist Role
  - Data Engineering
  - Data Science
  - Machine Learning Engineer Role
  - MLOps
---

A data engineer owns dependable data paths through ingestion, storage, and
transformation. The role also covers orchestration, access, monitoring, and
documentation.
At 13:58 in
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
data engineers make user-generated data usable without burdening production
systems. See the broader
[Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}) and
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) pages for
the full role hub.

A data scientist owns the reasoning path from question to evidence. That means
problem framing, exploratory analysis, and feature reasoning. It also means
method choice, evaluation, and product interpretation. The same role episode
separates
analysts from data scientists at 11:17. Analysts explain what happened, while
data scientists predict and help turn predictions into product behavior
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})).

The useful boundary is ownership, not tool usage. Both roles may use SQL,
Python, notebooks, and cloud services. Workflow tools can appear on both sides.
The question is whether the work primarily makes data dependable for others or
turns data into a decision. It may also turn data into a model, experiment, or
product feature
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Engineer vs Data Scientist comparison]({{ '/comparisons/data-engineer-vs-data-scientist/' | relative_url }})).

Use the short
[Data Engineer vs Data Scientist comparison]({{ '/comparisons/data-engineer-vs-data-scientist/' | relative_url }})
when you need a decision page. For the broader archive reference, follow the
role boundary through [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[Data Science]({{ '/wiki/data-science/' | relative_url }}), and [Data Quality
and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
Engineering-heavy cases connect to
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) and
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}). Title
ambiguity connects to [Job Descriptions]({{ '/wiki/job-descriptions/' | relative_url }})
and [Hiring]({{ '/wiki/hiring/' | relative_url }}).

## Common Definition

Across the archive, data engineering starts when a team needs data to be
available repeatedly and safely. The work includes pipelines, storage, and
query performance. It also includes cluster resources, schema changes,
freshness checks, and documentation.

Diachuk's direct comparison puts ETL, HDFS or S3, and Impala on the engineering
side. Parquet and Spark optimization are there too. Kubernetes and Prometheus
appear in the same discussion. Grafana and schema monitoring appear there at
4:26-7:18 and 39:09-43:37
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})).

Data science starts when a team needs an answer, model, or experiment. It also
starts when a team needs a prediction. Diachuk places data cleaning, feature
engineering, the model cycle, and deployment awareness on the data scientist
side at 13:56. Grigorev's role
episode frames data scientists through prediction and product integration at
11:17
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Machine Learning]({{ '/wiki/machine-learning/' | relative_url }})).

The two roles meet when a project needs both a trustworthy data supply and a
trustworthy model or decision. A recommendation system needs events, training
data, feature transformations, and offline evaluation. It also needs batch or
streaming jobs, serving paths, and monitoring. Diachuk uses recommendation
systems and Parquet file interfaces to explain this collaboration at 16:26-23:40
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Products]({{ '/wiki/data-products/' | relative_url }})).

Production often adds a third owner. Grigorev separates machine learning
engineers from data scientists at 17:04 and uses batch scoring at 40:10 to show
where predictions must move into systems. Stiebellehner gives the platform
version. Experiment tracking, registries, and batch inference sit around the
data scientist's work.

Online serving, orchestration, and lineage sit there too.
Prediction logging belongs in the same layer
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})).

## Common Decision Rule

Choose a data engineer owner when the main risk is unavailable or inconsistent
data. Late and slow data fit too. The same owner fits undocumented or expensive
data. Hard-to-reprocess data fits too.

That covers:

- source ingestion and schemas
- storage layout and orchestration
- permissions and freshness
- lineage, monitoring, and recovery
([Data Team Roles Explained at 13:58]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Big Data Engineer vs Data Scientist at 39:09 and 58:05]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

Choose a data scientist owner when the main risk is answering the wrong
question or choosing the wrong metric. The same owner fits weak features, a
model where a simpler method would do. It also fits results that don't connect
to a decision. Novikov's interview guide starts case studies from business goals and
evaluation metrics at 32:03. Diachuk places feature reasoning and model
iteration on the data scientist side at 13:56
([Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }})).

Make shared ownership explicit when the work crosses the boundary.

Feature pipelines, batch scoring, and prediction tables need named handoffs.
Recommender systems need them too. The same is true for data-quality incidents
that affect model behavior and production monitoring. Those handoffs often
include data engineering and data science. They often include ML engineering or
MLOps too
([Data Team Roles Explained at 40:10]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Building Production ML Platforms at 31:15 and 54:15]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }})).

## Guest Differences

Guests differ on how specialized the data engineer role should be. Diachuk's
version is large-scale and infrastructure-heavy. Spark jobs and file formats
are central. Cluster resources and cloud or HDFS storage are central too.
Monitoring and schema governance are also part of that version.

Tulski's newer episode splits the title into platform data engineering and
product-facing data engineering at 11:54. He then ties senior judgment to cost
awareness. Avoiding over-engineered platforms is part of the same discussion at
25:33-30:56
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

Guests also differ on how much engineering a data scientist should do.
Diachuk says data scientists should understand pipeline inputs and outputs at
24:49 and should care about code quality and reproducibility at 46:14. That
doesn't make the data scientist the pipeline owner. It makes collaboration
possible
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})).

Iofciu treats title ambiguity as the main warning. Her job-description episode
asks candidates to look at the team, objectives, and responsibilities. It also
asks them to look at data infrastructure and analytics or data engineering
support at 20:06-27:18. In that framing, "data scientist" can hide analytics
work or platform cleanup. It can also hide first-data-hire work or a role with
no clear owner
([Data Science Jobs]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }}),
[Job Descriptions]({{ '/wiki/job-descriptions/' | relative_url }})).

Recruiting guests make the same point from the candidate side.
[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }}) says data scientist
hiring varies by company at 7:02. He rewards industry and use-case alignment at
16:15-25:04. Novikov separates product data science from
ML-engineering-heavy roles at 15:29. He then tells candidates to tailor
applications to the actual job at 17:13
([Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}),
[Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Hiring]({{ '/wiki/hiring/' | relative_url }})).

Stiebellehner moves the disagreement into platform design. His episode says an
ML platform should understand data science notebooks and ways of working at
10:47. Platform investment should come from repeated deployment needs at
16:52-17:14. Standardization needs belong in that trigger too, but one model
isn't enough
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}),
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})).

## Practical Boundary by Work Item

For raw events and source data, data engineering owns collection and contracts.
It also owns storage and access.

Grigorev's role definition says data engineers make product data usable for
analysts and data scientists at 13:58. Diachuk's tooling discussion adds S3 or
HDFS, Parquet, and Spark. It also adds Impala and schema monitoring.
Documentation appears there too
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})).

For exploratory feature work, data science usually owns the first version
because feature relevance belongs to the model question. Diachuk names data
cleaning and feature engineering in the data scientist scope at 13:56. When the
same transformations become scheduled or monitored, ownership shifts toward
data engineering or ML platform work. The same shift happens when other teams
reuse model inputs
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})).

For batch scoring, split the artifact from the path. Data science owns model
logic and evaluation, while data engineering may own the scheduled movement of
inputs and predictions. ML engineering or MLOps may own packaging, registry,
deployment, and monitoring. Grigorev's 40:10 batch-scoring example and
Stiebellehner's 31:15 deployment section both support this split
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})).

For online prediction services, the boundary moves away from pure data
engineering. Machine learning engineers usually own serving, APIs, and latency.
They also own runtime behavior and production maintainability.

Data engineers
still own upstream data availability and feature freshness. This follows
Grigorev's 17:04 machine-learning-engineer role split and Stiebellehner's
platform discussion of online serving and registries. Stiebellehner also
includes unified prediction logging
([Data Team Roles Explained]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Production]({{ '/wiki/production/' | relative_url }})).

For data quality incidents, data engineering owns the upstream fix when the
problem is freshness, schema change, or duplication. It also owns delayed
ingestion and reprocessing.

Data science owns the impact assessment when those issues affect features or
model outputs. It also owns the impact assessment for experiment conclusions
and stakeholder decisions. Diachuk connects engineering quality to spikes,
schema changes, and alerts. She also connects it to documentation and
historical reprocessing.

Stiebellehner's monitoring section covers prediction logs. It also shows why
analytics need consistent schemas
([Big Data Engineer vs Data Scientist quality sections]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Building Production ML Platforms at 54:15]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }})).

For dashboards, reports, and product metrics, the title alone isn't enough.
Data engineering owns the dependable datasets, while analysts and product data
scientists own interpretation and recommendations.

Analytics engineers may own the reusable analytical model layer. That happens
when metric logic becomes shared
([Data Team Roles Explained at 7:51-13:58]({{ '/podcasts/data-team-roles/' | relative_url }}),
[Data Analyst vs Analytics Engineer]({{ '/wiki/data-analyst-vs-analytics-engineer/' | relative_url }}),
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})).

## Career and Hiring Signals

A data engineer signal is evidence that the candidate can make other people's
work dependable. Strong examples include repeatable ingestion, SQL and Python
depth, orchestration, and storage choices. Tests and documentation matter too.
Monitoring and recovery from schema or freshness problems matter too.

Diachuk's comparison and Jeff Katz's job-prep episodes connect that evidence to
pipelines, databases, Docker, and Airflow. Warehouses and code quality appear
there too. Operational judgment does as well
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})).

A data scientist signal is evidence that the candidate can move from a business
or product question to useful evidence. Strong examples include problem
framing, metric choice, SQL, and modeling. Feature reasoning and evaluation
matter too. Communication matters too.

Novikov's case-study section starts from business goals and metrics, so a
project narrative needs real use-case context. Whipps rewards portfolios that
connect tools to projects and industry context. Business impact matters there
too
([Data Science Interview Guide]({{ '/podcasts/data-science-interview-and-cv-guide/' | relative_url }}),
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}),
[Data Scientist Interview Roadmap]({{ '/wiki/data-scientist-interview-roadmap/' | relative_url }})).

For candidates choosing between the roles, the archive suggests looking at the
failure mode they want to own. If broken pipelines or missing data sound like
the core problem, the data-engineering path fits the archive's engineering
examples. Schema drift, cost, and platform reliability point the same way.

If ambiguous questions, feature
tradeoffs, or model evaluation sound like the core problem, the data-science
path fits the archive's data scientist examples. Experiments and stakeholder
interpretation point the same way
([Big Data Engineer vs Data Scientist]({{ '/podcasts/big-data-engineer-vs-data-scientist/' | relative_url }}),
[Data Science Jobs]({{ '/podcasts/data-science-job-red-flags-and-mismatched-roles/' | relative_url }}),
[Career Transitions in Data]({{ '/wiki/career-transitions-in-data/' | relative_url }})).

## Related Pages

Use these pages for adjacent role boundaries, tools, and career paths.

- [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }})
- [Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [Data Science Careers]({{ '/wiki/data-science-careers/' | relative_url }})
- [Machine Learning Engineer Role]({{ '/wiki/machine-learning-engineer-role/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
- [Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Job Descriptions]({{ '/wiki/job-descriptions/' | relative_url }})
- [Data Engineer vs Data Scientist comparison]({{ '/comparisons/data-engineer-vs-data-scientist/' | relative_url }})
