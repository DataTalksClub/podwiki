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
pipeline, or model that depends on it. They use data observability to notice
when that fitness changes and diagnose the cause. The closest adjacent wiki
pages are
[[DataOps]] and
[[Data Observability for Data Engineering]].
Platform and governance links include
[[Data Engineering Platforms]],
[[Data Governance]], and
[[Model Monitoring]].

Quality and observability are production reliability work, not dashboard polish.
The failure mode is "data downtime": analytics teams, ML models, and business
workflows receive data that exists but is late, incomplete, malformed, or
shifted
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

Andy Petrella's
[[book:20240429-fundamentals-of-data-observability|Fundamentals of Data Observability]]
develops the same signal set into a full reference covering metadata
collection, anomaly detection, and incident triage.
[[book:20210621-cleaning-data-for-effective-data-science|Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

The same failures connect to tests and CI/CD, and reliability ties to version
control, observability, runbooks, and automated playbooks
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

Use this page for the combined reliability concept. For narrower topics, follow
[[DataOps]] for data pipeline delivery,
[[MLOps]] for deployed model failures, and
[[Data Observability for Data Engineering]]
for practical implementation guidance including stack placement, ownership
metadata, and rollout steps.

## Reliable Data Work

Reliable data teams try to prevent avoidable bad data, detect unhealthy data
quickly, and make the recovery path obvious. The core signals are freshness,
volume, distribution, schema, and lineage. Monitoring and observability differ:
monitoring detects that something changed, while observability helps the team
find the cause
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

The operating version groups automation, observability, and productivity as core
DataOps practices, and adds CI/CD pipelines, regression tests, and test data for
analytics. Data quality becomes a delivery concern, not a manual check after a
dashboard or model fails
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

The ML episodes add another layer. Production model maintenance connects to data
drift and concept drift
([[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]]).
Production AI systems inherit reliability problems from data pipelines, prompt
inputs, and evaluation checks, which is why testing comes first
([[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]]).
[[book:20210621-cleaning-data-for-effective-data-science|Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

## Failure Modes

Quality requires more than "the job ran", and different failure modes are the
starting points.

The first is invisible data failure: silent failures where only part of the
expected data arrives, and engineering jobs that succeed while the data they
publish is still bad
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

The second is how teams deliver changes. Quality ties to reducing production
errors, deployment cycle time, and team toil, then to version control, tests,
and CI/CD, and finally to moving teams from runbooks toward automated playbooks
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

The third is ML reliability. Platform work reaches metadata and lineage and data
governance
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]),
and feature design and clean data sit beside governance, with drift and business
explanation part of the same production work
([[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]]).

The fourth is the modern data platform boundary. Data engineering has split into
specialties such as data governance, data quality, and streaming, and catalogs
connect to access control, metadata, and lineage
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]]).

## Quality Checks and Delivery

Quality work starts before an alert fires. Robust CI/CD pipelines and realistic
test data come first, along with infrastructure as code and low-risk deployment.
Version control alone isn't enough: teams need end-to-end tests and automated
checks before production
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

The same point holds for pipeline work. Observability and monitoring reduce
production errors, and dbt, Great Expectations, SQL tests, and different testing
strategies encode assumptions
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).
Those practices sit beside
[[Analytics Engineering]]
and [[DataOps]] because transformations,
models, and reports share the same reliability problem.

The boundary is clear: tests and dbt checks help teams encode known assumptions,
but they don't catch every late, missing, shifted, or unexpected dataset
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

Quality checks reduce known failure modes, while observability watches running
data products for unexpected ones.

## Observability Signals and Diagnosis

Five recurring signals define observability
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]):

- Freshness asks whether data arrived when consumers expected it.
- Volume asks whether the amount of data is plausible.
- Distribution asks whether values moved outside expected ranges.
- Schema asks whether tables or fields changed.
- Lineage maps upstream causes and downstream impact.

Lineage matters because an alert alone doesn't tell a team what to fix first. A
freshness alert can be diagnosed using downstream correlations and query logs to
reason about the cause, with lineage adding upstream and downstream impact.
Automatic lineage spans warehouses and lakes, BI tools, and downstream assets
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

Responders need platform metadata before they can act, so observability sits
beside
[[Data Engineering Platforms]].

Not every anomaly is bad data. Uncommon data differs from bad data: a spike,
drop, or schema change may be intentional, but teams still need context because a
downstream dashboard, customer report, or ML model can break anyway
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

For ML systems, distribution monitoring sits next to model monitoring. Model
monitoring links to upstream ETL and data-pipeline causes, so a model incident
may begin with feature data or delayed labels rather than model code. Data
profiling architecture lets profiles summarize behavior over time, and WhyLogs
and WhyLabs separate open-source profiling from managed observability
([[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).
[[MLOps Tools]] covers that tooling
layer, while pipeline checks live closer to
[[DataOps Tools]].

## Ownership, SLAs, and Triage

Observability only helps when the right team can act. RACI separates responsible
or accountable roles from consulted or informed roles, and quality connects to
data SLAs. A data scientist may need a feature table five minutes after a user
action, while another table can wait; platform and pipeline teams use that SLA to
decide which freshness incident deserves immediate response
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).

Naive alerting is a trap: a useful observability system should reduce false
positives by combining data, metadata, lineage, and incident context
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).
[[Data Governance]] and
[[Data Product Management]]
meet quality here. Teams need ownership, meaning, usage, and priority before
they can decide whether an anomaly is urgent.

Runbooks are a step toward automation. Moving from manual checklists to automated
playbooks means a useful alert names an owner, a diagnosis path, and a
remediation path
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

A maturity curve runs from reactive work toward proactive, automated, and
scalable recovery, with operational runbooks along the way
([[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]).
The DataOps discipline adds the operational lifecycle and on-call readiness for
data science
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]),
and versioning should cover code, models, visualizations, and governance
together
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).
Incident response is more than a tool — it requires clear ownership, automation,
and post-incident improvements.

## ML and AI Reliability

Model quality depends on data quality after deployment. Feature engineering ties
to business understanding, and production monitoring makes data quality dynamic:
a feature can be valid during training and less valid once the business activity
or population changes
([[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]]).

The platform side adds several reproducibility wins: experiment tracking is
low-friction, model registries persist models for downstream use, metadata and
lineage help teams reproduce runs and understand artifacts, and API design and
logging give model predictions a shared schema for monitoring and analytics
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The same reliability logic extends to production AI: data trust and the "this
number doesn't look correct" failure, snapshot and integration tests, and Great
Expectations, Soda, SQL tests, and Spark tests
([[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]]).

For AI systems, those checks sit next to prompt evaluation, caching, and cost
controls. The data pipeline is still the reliability base.

## Platform Boundaries

Modern platforms can make quality work easier or harder. Apache Iceberg is a
table format for storing data independently of databases, with storage as one
layer and compute as another, plus access, metadata, catalogs, and lineage. That
matters for quality because checks, ownership, and impact analysis need metadata
that survives across tools
([[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]]).

Thin abstraction layers over cloud providers help too. For quality and
observability, platform teams should standardize logging, metadata, lineage,
tests, and deployment paths without making incidents hard to debug
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

## Related Topics

Adjacent topics cover the narrower operating disciplines and platform areas:

- [[DataOps]]
- [[Data Engineering Platforms]]
- [[Data Governance]]
- [[Model Monitoring]]
- [[MLOps]]
- [[Data Observability for Data Engineering]]
- [[MLOps vs DataOps]]
