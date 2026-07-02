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

DataTalks.Club guests treat quality and observability as production reliability
work, not as dashboard polish. In
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
[[person:barrmoses|Barr Moses]] frames the failure mode
as "data downtime." Analytics teams, ML models, and business workflows can
receive data that exists but is late or incomplete. The data may also be
malformed or shifted.

Andy Petrella's
[[book:20240429-fundamentals-of-data-observability|Fundamentals of Data Observability]]
develops the same signal set into a full reference covering metadata
collection, anomaly detection, and incident triage.
[[book:20210621-cleaning-data-for-effective-data-science|Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

Across the DataOps episodes,
[[person:christopherbergh|Christopher Bergh]] connects
the same failures to tests and CI/CD. He also ties reliability to version
control, observability, runbooks, and automated playbooks in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]
and
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].

Use this page for the combined reliability concept. For narrower topics, follow
[[DataOps]] for data pipeline delivery,
[[MLOps]] for deployed model failures, and
[[Data Observability for Data Engineering]]
for practical implementation guidance including stack placement, ownership
metadata, and rollout steps.

## Reliable Data Work

Reliable data teams try to prevent avoidable bad data, detect unhealthy data
quickly, and make the recovery path obvious. In
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
[[person:barrmoses|Barr Moses]] names freshness and
volume at 16:38. She also names distribution, schema, and lineage. At 24:31,
she separates monitoring from observability. Monitoring detects that something
changed, while observability helps the team find the cause.

[[person:christopherbergh|Christopher Bergh]] gives the
operating version of the same idea in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
At 15:52, he groups automation, observability, and productivity as core DataOps
practices. At 30:55, the discussion moves to CI/CD pipelines, regression tests,
and test data for analytics. That makes data quality a delivery concern, not a
manual check after a dashboard or model fails.

The ML episodes add another layer. In
[[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]],
[[person:thomives|Thom Ives]] connects production model
maintenance to data drift and concept drift at 47:30. In
[[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]],
[[person:bartoszmikulski|Bartosz Mikulski]] starts with
testing because production AI systems inherit reliability problems from data
pipelines, prompt inputs, and evaluation checks.
[[book:20210621-cleaning-data-for-effective-data-science|Cleaning Data for Effective Data Science]]
by David Mertz covers the same data preparation and quality discipline that
underlies reliable analytics and ML.

## Failure Modes

The podcast discussions agree that quality requires more than "the job ran",
but the guests start from different failure modes.

[[person:barrmoses|Barr Moses]] starts from invisible
data failure. At 13:40 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
the discussion covers silent failures where only part of the expected data
arrives. At 21:57, she makes the distinction explicit: engineering jobs can
succeed while the data they publish is still bad.

[[person:christopherbergh|Christopher Bergh]] starts
from how teams deliver changes. In
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]],
he ties quality to reducing production errors, deployment cycle time, and team
toil. At 33:47, he moves into version control, tests, and CI/CD. At 34:37, he
pushes teams from runbooks toward automated playbooks.

[[person:simonstiebellehner|Simon Stiebellehner]] and
[[person:thomives|Thom Ives]] start from ML reliability.
In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
the platform discussion reaches metadata and lineage at 42:48 and data
governance at 45:50. In
[[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]],
feature design and clean data sit beside governance. Drift and business
explanation are part of the same production work.

[[person:adrianbrudaru|Adrian Brudaru]] starts from the
modern data platform boundary. In
[[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]],
he says at 11:03 that data engineering has split into specialties such as data
governance, data quality, and streaming. At 21:27, he connects catalogs to
access control, metadata, and lineage.

## Quality Checks and Delivery

Quality work starts before an alert fires. In
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
[[person:christopherbergh|Christopher Bergh]] argues at
30:55 for robust CI/CD pipelines and realistic test data. He also includes
infrastructure as code and low-risk deployment. At 42:39, he adds that version
control alone isn't enough: teams need end-to-end tests and automated checks
before production.

The earlier
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]
episode grounds the same point in pipeline work. At 7:22,
[[person:christopherbergh|Christopher Bergh]] frames
observability and monitoring as ways to reduce production errors. At 48:25, he
discusses dbt and Great Expectations. He also covers SQL tests and different
testing strategies. Those practices sit beside
[[Analytics Engineering]]
and [[DataOps]] because transformations,
models, and reports share the same reliability problem.

[[person:barrmoses|Barr Moses]] makes the boundary clear
at 50:52 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
Tests and dbt checks help teams encode known assumptions. They don't catch every
late or missing dataset. They also don't catch every shifted or unexpected
dataset.

Quality checks reduce known failure modes, while observability watches running
data products for unexpected ones.

## Observability Signals and Diagnosis

[[person:barrmoses|Barr Moses]] names five recurring
signals at 16:38 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]:

- Freshness asks whether data arrived when consumers expected it.
- Volume asks whether the amount of data is plausible.
- Distribution asks whether values moved outside expected ranges.
- Schema asks whether tables or fields changed.
- Lineage maps upstream causes and downstream impact.

Lineage matters because an alert alone doesn't tell a team what to fix first.
At 26:04 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
[[person:barrmoses|Barr Moses]] describes a freshness
alert. She then uses downstream correlations and query logs to reason about the
cause. Lineage adds upstream and downstream impact.

At 58:51, she returns to automatic lineage across warehouses and lakes. She also
includes BI tools and downstream assets.

Responders need platform metadata before they can act, so observability sits
beside
[[Data Engineering Platforms]].

Not every anomaly is bad data. At 1:00:27 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
[[person:barrmoses|Barr Moses]] discusses the difference
between uncommon data and bad data. A spike or drop may be intentional. A
schema change may be intentional too, but teams still need context because a
downstream dashboard, customer report, or ML model can break anyway.

For ML systems, distribution monitoring sits next to model monitoring.
[[person:dannyleybzon|Danny Leybzon]] links model
monitoring to upstream ETL and data-pipeline causes at 27:35 in the
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]].
A model incident may begin with feature data or delayed labels rather than
model code. His 31:50 discussion of data profiling architecture shows how
profiles can summarize behavior over time. At 55:50, he compares WhyLogs and
WhyLabs, separating open-source profiling from managed observability.
[[MLOps Tools]] covers that tooling
layer, while pipeline checks live closer to
[[DataOps Tools]].

## Ownership, SLAs, and Triage

Observability only helps when the right team can act. In
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]],
[[person:barrmoses|Barr Moses]] introduces RACI at 29:00
to separate responsible or accountable roles from consulted or informed roles.
At 35:24, she connects quality to data SLAs. A data scientist may need a
feature table five minutes after a user action, while another table can wait.
Platform and pipeline teams use that SLA to decide which freshness incident
deserves immediate response.

At 47:00, [[person:barrmoses|Barr Moses]] warns against
naive alerting. She says a useful observability system should reduce false
positives by combining data, metadata, lineage, and incident context.
[[Data Governance]] and
[[Data Product Management]]
meet quality here. Teams need ownership, meaning, usage, and priority before
they can decide whether an anomaly is urgent.

Runbooks matter, but Bergh treats them as a step toward automation. At
34:37 in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]],
[[person:christopherbergh|Christopher Bergh]] describes
the move from manual checklists to automated playbooks. A useful alert should
name an owner, a diagnosis path, and a remediation path.

Moses lays out a maturity curve at 43:00 in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
Teams move from reactive work toward proactive, automated, and scalable
recovery. She also describes operational runbooks at 41:03. Bergh's DataOps
episodes add the operating discipline: in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
he discusses the operational lifecycle at 23:56 and on-call readiness for data
science at 26:13. Versioning should cover code, models, visualizations, and
governance together, as he argues at 51:21 in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
That makes incident response more than a tool — it requires clear ownership,
automation, and post-incident improvements.

## ML and AI Reliability

Model quality depends on data quality after deployment. In
[[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]],
[[person:thomives|Thom Ives]] ties feature engineering
to business understanding at 34:54 and then discusses production monitoring at
47:30. His drift discussion makes data quality dynamic: a feature can be valid
during training and less valid once the business activity or population
changes.

[[person:simonstiebellehner|Simon Stiebellehner]] adds
the platform side in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
At 29:41, experiment tracking appears as a low-friction reproducibility win. At
30:32, model registries persist models for downstream use. At 42:48, metadata
and lineage help teams reproduce runs and understand artifacts. At 54:15, API
design and logging give model predictions a shared schema for monitoring and
analytics.

[[person:bartoszmikulski|Bartosz Mikulski]] extends the
same reliability logic to production AI in
[[podcast:production-ready-ai-engineering|Production-Ready AI Engineering]].
At 9:05, he discusses data trust and the "this number doesn't look correct"
failure. At 11:47 and 13:14, he covers snapshot and integration tests. He also
covers Great Expectations, Soda, SQL tests, and Spark tests.

For AI systems, those checks sit next to prompt evaluation, caching, and cost
controls. The data pipeline is still the reliability base.

## Platform Boundaries

Modern platforms can make quality work easier or harder. In
[[podcast:trends-in-modern-data-engineering|Trends in Modern Data Engineering]],
[[person:adrianbrudaru|Adrian Brudaru]] describes Apache
Iceberg at 18:17 as a table format for storing data independently of databases.
At 21:27, he describes storage as one layer and compute as another. He then
covers access, metadata, catalogs, and lineage. That matters for quality
because checks, ownership, and impact analysis need metadata that survives
across tools.

In
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[person:simonstiebellehner|Simon Stiebellehner]] argues
at 38:40 for thin abstraction layers over cloud providers. For quality and
observability, platform teams should standardize logging and metadata. They
should also standardize lineage, tests, and deployment paths without making
incidents hard to debug.

## Related Topics

Adjacent topics cover the narrower operating disciplines and platform areas:

- [[DataOps]]
- [[Data Engineering Platforms]]
- [[Data Governance]]
- [[Model Monitoring]]
- [[MLOps]]
- [[Data Observability for Data Engineering]]
- [[MLOps vs DataOps]]
