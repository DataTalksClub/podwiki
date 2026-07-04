---
layout: wiki
title: "Data Quality and Observability"
summary: "How DataTalks.Club guests frame reliable data systems: tests, freshness, lineage, monitoring, triage, and recovery practices."
related:
  - DataOps
  - Data Engineering Platforms
  - Data Governance
  - Model Monitoring
  - MLOps
  - Data Product Management
  - Data Observability for Data Engineering
---

Teams call data high-quality when it fits the downstream decision, product,
pipeline, or model that depends on it. Data observability helps teams notice
when that fitness changes and diagnose the cause. This topic connects most
directly to [[DataOps]] and [[Data Observability for Data Engineering]]. It
also depends on [[Data Engineering Platforms]], [[Data Governance]], and
[[Model Monitoring]].

Quality and observability are production reliability work, not dashboard polish.
During data downtime data exists but arrives late, incomplete, malformed, or
shifted. Analytics teams, ML models, and business workflows can all receive that
bad data.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Andy Petrella's
[[book:20240429-fundamentals-of-data-observability=>Fundamentals of Data Observability]]
develops the same signal set into a full reference covering metadata
collection, anomaly detection, and incident triage.
[[book:20210621-cleaning-data-for-effective-data-science=>Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

The same failures connect to tests and CI/CD. Reliability also ties to version
control, observability, runbooks, and automated
playbooks.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

For narrower operating views, [[DataOps]] covers data pipeline delivery and
[[MLOps]] covers deployed model failures. [[Data Observability for Data Engineering]]
covers stack placement, ownership metadata, and rollout steps.

## Reliability Meaning

Reliable data teams try to prevent avoidable bad data. They detect unhealthy
data quickly and make the recovery path obvious. Monitoring detects that
something changed. Observability helps the team find the
cause.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

DataOps adds the delivery version of this reliability work. Teams use
automation, observability, and productivity practices alongside CI/CD pipelines.
Regression tests and test data make data quality part of delivery, not a manual
check after a dashboard or model fails.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

ML systems add another layer. Production model maintenance connects to data
drift and concept drift.
[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Governance]]

Production AI systems inherit reliability problems from data pipelines and
prompt inputs. Evaluation checks make testing part of the reliability base.
[[cite:production-ready-ai-engineering@9:05=>Production-Ready AI Engineering]]

[[book:20210621-cleaning-data-for-effective-data-science=>Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

## Reliability Boundaries

Podcast discussions don't treat quality as one discipline with one owner. Data
observability focuses on runtime health and impact analysis. DataOps focuses on
delivery practices, tests, and automation. ML platform work focuses on
reproducibility, feature health, metadata, and deployed model
behavior.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]][[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The boundary also shifts by consumer. A BI dashboard can fail because a table is
late or malformed. A model can fail because feature distributions move or labels
arrive late. An AI product can fail when tests, prompt inputs, retrieved data,
or evaluation checks don't catch bad behavior before
release.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Governance]][[cite:production-ready-ai-engineering=>Production-Ready AI Engineering]]

## Failure Modes

Invisible failures happen when only part of the expected data arrives. Jobs can
still succeed while they publish bad
data.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Delivery failures show up as production errors, slow deployments, and team toil.
Teams reduce them with version control, tests, CI/CD, and a shift from runbooks
to automated playbooks.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

ML failures add feature and model context. Platform work brings in metadata and
lineage, along with data governance.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Feature design and clean data sit beside drift monitoring and business
explanation.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Governance]]

Modern data platforms add another boundary. Data engineering has split into
specialties such as governance, quality, and streaming. Catalogs connect access
control to metadata and lineage.[[cite:trends-in-modern-data-engineering=>Trends in Modern Data Engineering]]

## Quality Checks and Delivery

Quality work starts before an alert fires because robust CI/CD pipelines and
realistic test data come first. Infrastructure as code helps teams deploy with
lower risk. Version control alone isn't enough. Teams need end-to-end tests and
automated checks before production.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Teams apply the same rule to pipelines because observability and monitoring
reduce production errors. dbt and Great Expectations encode assumptions, as do
SQL tests and other testing strategies.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
Fraud-detection teams use the production version. They can combine Great
Expectations, cloud-native checks, custom unit tests, and profiling layers.
Teams place checks inside the pipeline so they can catch bad input before
operational decisions use it
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@43:28=>Fraud Prevention]].

Those practices sit beside [[Analytics Engineering]] and [[DataOps]] because
transformations, models, and reports share the same reliability problem.

Tests and dbt checks help teams encode known assumptions. They don't catch every
late, missing, shifted, or unexpected
dataset.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Quality checks reduce known failure modes, while observability watches running
data products for unexpected ones.

Internal data platforms can measure quality work with operational outcomes, not
only test counts. Greg Coquillo suggests tracking whether pipeline failures
fall. He also suggests tracking whether business-critical failures are resolved
inside an agreed SLA. One example target is 98% of incidents within 48 hours
[[cite:building-and-scaling-ai-data-products-with-mlops@53:27=>AI Data Products with MLOps]].
That links [[DataOps]] reliability to [[KPIs]] because the metric has an owner,
a threshold, and a downstream customer.

Tammy Liang gives the small-team version of this practice. After dashboard
accuracy issues, the team rebuilt trust with a data accuracy playbook and dbt
tests. Regular dashboard checks replaced ad hoc review. That makes testing both
a technical control and a trust-repair mechanism for business-facing analytics.
[[cite:building-and-scaling-data-team@35:38=>Building and Scaling a Data Team]]
[[cite:building-and-scaling-data-team@40:09=>Building and Scaling a Data Team]]

The same playbook also has a source-system side. Business teams may enter
product costs, campaign plans, or other operational inputs in formats that break
downstream reports. The data team can pair input guidelines and stakeholder
communication with warehouse-side dbt tests, outlier checks, and manual
dashboard review. That keeps data quality from becoming only a warehouse concern.
[[cite:building-and-scaling-data-team@40:24=>Building and Scaling a Data Team]]

## Observability Signals and Diagnosis

Five recurring signals define observability.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

- Freshness asks whether data arrived when consumers expected it.
- Volume asks whether the amount of data is plausible.
- Distribution asks whether values moved outside expected ranges.
- Schema asks whether tables or fields changed.
- Lineage maps upstream causes and downstream impact.

Lineage matters because an alert alone doesn't tell a team what to fix first. A
freshness alert can be diagnosed with downstream correlations and query logs.
Lineage adds upstream and downstream impact. Automatic lineage spans warehouses,
lakes, BI tools, and downstream
assets.[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Responders need platform metadata before they can act, so observability sits
beside [[Data Engineering Platforms]].

An anomaly can be unusual without being bad when a spike, drop, or schema
change is intentional. Teams still need context because a dashboard, customer
report, or ML model can break anyway.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

Lior Barak adds the stakeholder-facing layer. When quality is uncertain, teams
should proactively alert users before they discover the issue themselves. They
can also expose uncertainty through confidence intervals or QA dashboards. That
preserves decision confidence while the system is being repaired. This is
observability as communication, not only alert routing: the affected user learns
whether the number is safe before using it in a meeting.
[[cite:data-translator-role-and-data-strategy@07:46=>Data Translator Role]]
[[cite:data-translator-role-and-data-strategy@10:48=>Data Translator Role]]

For ML systems, distribution monitoring sits next to model monitoring. Model
monitoring links to upstream ETL and data-pipeline causes, so a model incident
may begin with feature data or delayed labels rather than model code. Data
profiles summarize behavior over time. WhyLogs and WhyLabs separate
open-source profiling from managed
observability.[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]
[[MLOps Tools]] covers that tooling layer, while pipeline checks live closer to
[[DataOps Tools]].

## Ownership, SLAs, and Triage

Observability only helps when the right team can act. RACI separates responsible
or accountable roles from consulted or informed roles, and quality also connects
to data SLAs. A data scientist may need a feature table five minutes after a
user action, while another table can wait. Platform and pipeline teams use that
SLA to decide which freshness incident needs immediate
response.[[cite:data-quality-data-observability-data-reliability@29:00=>Data Observability Explained]][[cite:data-quality-data-observability-data-reliability@35:24=>Data Observability Explained]]

Naive alerting is a trap. A useful observability system reduces false positives
by combining data, metadata, lineage, and incident
context.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

[[Data Governance]] and [[Data Product Management]] meet quality here. Teams
need ownership, meaning, usage, and priority before they can decide whether an
anomaly is urgent.

Runbooks are a step toward automation. Moving from manual checklists to automated
playbooks means a useful alert names an owner, a diagnosis path, and a
remediation path.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Teams mature when they move from reactive fixes toward proactive recovery, with
operational runbooks along the
path.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

The DataOps discipline adds the operational lifecycle and on-call readiness for
data science.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Versioning should cover code, models, visualizations, and governance together
across the lifecycle.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Incident response requires more than a tool because teams need clear ownership,
automation, and post-incident improvement.

## ML and AI Reliability

Model quality depends on data quality after deployment. Feature engineering ties
to business understanding, while production monitoring makes data quality
dynamic. A feature can be valid during training and less valid once the business
activity or population
changes.[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering and Governance]]

ML platforms add reproducibility through experiment tracking and model
registries. Metadata and lineage help teams reproduce runs and understand
artifacts. API design and logging give model predictions a shared schema for
monitoring and
analytics.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The same reliability logic extends to production AI. The failure can be a data
trust problem where a number doesn't look correct. Testing includes snapshot and
integration tests.

Teams can add framework-backed checks such as Great Expectations or Soda. SQL
and Spark tests can cover execution details too.

[[cite:production-ready-ai-engineering@9:05=>Production AI]]
[[cite:production-ready-ai-engineering@11:47=>Pipeline testing]]
[[cite:production-ready-ai-engineering@13:14=>Testing tools]]

The operating point is trust: once users see obviously wrong data, tests and
observability become part of rebuilding confidence, not only catching defects.

Responsible AI makes data quality part of fairness work. Supreet Kaur frames
bias detection as EDA and monitoring before it becomes a model-explanation
problem. Teams check skewness, missingness, and coverage. They also review
sensitive-feature handling, demographic drift, and feedback loops.
[[cite:responsible-explainable-ai-bias-detection@11:36=>Responsible and Explainable AI]]
[[cite:responsible-explainable-ai-bias-detection@37:31=>Responsible and Explainable AI]]

For AI systems, those checks sit next to prompt evaluation, caching, and cost
controls. The data pipeline is still the reliability base.

## Platform Boundaries

Modern platforms can make quality work easier or harder. Apache Iceberg is a
table format for storing data independently of databases, with storage as one
layer and compute as another. It also involves access, metadata, catalogs, and
lineage. That matters for quality because checks and ownership need durable
metadata. Impact analysis also needs metadata
that survives across
tools.[[cite:trends-in-modern-data-engineering=>Trends in Modern Data Engineering]]

Thin abstraction layers over cloud providers help too. For quality and
observability, platform teams should standardize logging and metadata. They also
need standard lineage, tests, and deployment paths without making incidents hard
to debug.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

## Related Pages

These pages cover narrower operating disciplines and platform areas:

- [[DataOps]]
- [[Data Engineering Platforms]]
- [[Data Governance]]
- [[Model Monitoring]]
- [[MLOps]]
- [[Data Observability for Data Engineering]]
- [[MLOps vs DataOps]]
