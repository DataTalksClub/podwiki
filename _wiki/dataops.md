---
layout: wiki
title: "DataOps"
summary: "DataOps is the practice of making data delivery reviewable, testable, observable, and recoverable."
related:
  - DataOps Platforms
  - DataOps Tools
  - DataOps vs Data Engineering
  - DataOps Engineer Role
  - DataOps Checks for Data Pipelines
  - Data Engineering Platforms
  - Data Engineering Tools
  - Data Quality and Observability
  - Data Contracts
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
  - MLOps vs DataOps
  - LLMOps
  - GitOps for Data Teams
---

DataOps is the operating discipline for reliable data delivery. Teams use it to
review and test changes to pipelines, analytics workflows, and data products.
They also use it to release, observe, and recover those changes. For the
authoritative plain-language definition, see the
[DataTalks.Club DataOps definition article](https://datatalks.club/blog/what-dataops-exactly.html).

DataOps sits beside [[Data Engineering]] and [[MLOps]], but it doesn't replace
either one. Data engineering builds the data path. MLOps operates the model
path. DataOps names the release-and-recovery habits that keep data changes
safe enough for other teams to depend on.

Use [[DataOps vs Data Engineering]] for responsibility boundaries and
[[MLOps vs DataOps]] for the model-incident boundary. Use [[DataOps Platforms]]
when repeated DataOps work becomes a shared service surface. Use
[[dataops-engineer-role=>DataOps engineer role]] when the question is staffing
and day-to-day ownership.

[[person:christopherbergh=>Christopher Bergh]] frames DataOps as the response to
fragile data delivery
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps]].
[[person:larsalbertsson=>Lars Albertsson]] adds the scale concern: more teams
can build and consume data only when the delivery path is reproducible
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps Platform]].
[[book:20210913-dataops-for-dummies=>DataOps for Dummies]] by Justin Mullen and
Guy Adams gives a compact overview of the same operating discipline.

## Review, Test, Release, Observe, Recover

DataOps makes every data change pass through five practice questions:

- Who reviews the change before it affects downstream users?
- What tests catch broken logic, schema drift, missing data, or bad assumptions?
- How does the team release the change through a repeatable path?
- Which signals show whether the data is still fit to use?
- How does the team recover, rerun, or backfill after a failure?

Bergh connects version control and tests to CI/CD, monitoring, and playbooks
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Regression tests and realistic test data sit beside deployment automation and
production monitoring
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

Teams also use DataOps for data failures that ordinary application uptime
checks miss. A pipeline can finish successfully while the produced data is wrong
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
DataOps therefore treats [[Data Contracts]], [[Data Quality and Observability]],
and recovery paths as part of delivery, not as afterthoughts. For pipeline-level
examples, use [[DataOps Checks for Data Pipelines]]. For tool categories, use
[[DataOps Tools]].

The discipline still asks how those tools change review, release, observation,
and recovery habits.

## Adoption Paths

Teams can adopt DataOps from different starting points without changing the
discipline. A team with fragile releases may start with Git, tests, CI/CD, and
playbooks. Bergh ties those habits to lower handoff pressure and easier repair
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

A team with infrastructure-heavy data work may start by making SQL,
configuration, secrets, and environment changes reviewable. Tomasz Hinc's
GitOps discussion puts merge requests and dry runs in that route
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].
That makes [[gitops-for-data-teams=>GitOps for data teams]] a practical
DataOps adoption path when platform changes need the same review discipline as
pipeline code.

A growing organization may start from reproducibility and workflow support.
Albertsson asks whether late data or bugs can be replayed with reproducible
dependencies
[[cite:dataops-principles-and-scalable-data-platforms=>Platform]].
When that route becomes a product used by many teams, [[DataOps Platforms]]
covers the shared surface. For the discipline, ask whether every team can
review and test its data changes. Ask whether it can release, observe, recover,
and improve the next change.

## Pipeline Delivery

DataOps applies across ingestion and transformation, orchestration and warehouse
modeling, metrics, and analytics delivery. [[ETL]], [[ELT]], and [[cdc=>CDC]]
all create changes that teams have to review. Warehouse
modeling and schema evolution create changes that teams may need to replay or
recover
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
DataOps makes those engineering choices operable without replacing the
engineering choices themselves.

For [[Data Strategy]] work, DataOps turns planned [[Data Products]] and
AI-powered use cases into managed releases. Boyan Angelov connects DataOps to
Lean and Agile habits, changing requirements, and repeatable data-product
delivery
[[cite:data-strategy-and-dataops-for-ai-powered-products@24:57=>Data Strategy and DataOps for AI-Powered Products]].
He also places DataOps beside impact assessment and portfolio management after
teams choose use cases and a target architecture
[[cite:data-strategy-and-dataops-for-ai-powered-products@18:56=>Strategy delivery]].

Teams should keep data product intake in the same operating path as delivery
and measurement. They need use cases, release checks, and reprioritization to
survive contact with real data work
[[cite:data-strategy-and-dataops-for-ai-powered-products@18:56=>Strategy delivery]].
For [[ai-powered-business-intelligence=>AI-powered BI]], teams also have to
release metric-layer changes and dashboard trust states through DataOps.
Generated-query checks matter because AI answers depend on tested tables and
visible reliability signals
[[cite:mindful-data-strategy-for-business-impact=>Mindful Data Strategy]][[cite:production-ready-ai-engineering=>Production AI Engineering]].

Once a strategy reaches delivery, failed handoffs and waiting become operating
problems. Unclear requirements and unmeasured pilots do too
[[cite:data-strategy-and-dataops-for-ai-powered-products@25:03=>Lean and Agile DataOps]].
Another person should be able to review and test a data change. They should
also be able to deploy, observe, and rerun it without reverse-engineering the
whole pipeline
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

## Observability and Recovery

DataOps depends on observability, but monitoring is only the detection layer. A
monitor can tell the team that a table is stale or that a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook applies, and how the team prevents the same failure from returning.

Freshness and volume expose data failures that a successful job run may hide.
Distribution, schema, and lineage explain the structure and source of the
failure
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Teams should separate detection from diagnosis. They connect signals to
ownership, service expectations, and runbooks during root-cause analysis
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Production monitoring should feed the next release path. Real failures expose
missing tests, weak deployment automation, and unclear ownership
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]. Monitoring
without tests, release controls, owners, and recovery paths leaves teams
reacting to incidents one by one.

Use [[Data Quality and Observability]] and
[[data-quality-and-observability=>Data Observability]] for the monitoring layer.
Use [[data-observability-for-data-engineering=>data observability for data engineering]]
for the engineering view of where those checks belong. DataOps keeps those
signals tied to review, release, repair, and prevention.

## Boundaries With Data Engineering and MLOps

DataOps stays at the operating-practice level because it names how teams review
and release data changes. It also names how they detect bad data and recover.
It doesn't take over ingestion or transformation design. It doesn't own
warehouse modeling, dashboard design, or model serving.

With [[Data Engineering]], DataOps separates build work from operating practice.
Data engineers design pipelines and schemas, then implement transformations,
marts, and orchestration. DataOps gives those changes a repeatable path through
review and tests. Deployment, observability, and recovery stay in the same
path. [[DataOps vs Data Engineering]] covers the fuller comparison.

With [[MLOps]], the boundary appears when production ML depends on production
data. DataOps covers upstream ingestion and transformations. It also covers
datasets, metadata, quality checks, and data recovery.

MLOps owns model artifacts and training jobs. It also owns model registries,
serving paths, retraining decisions, and model behavior.
Model monitoring can still trace an alert back to ETL, data pipelines, and
upstream root causes
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].
[[MLOps vs DataOps]] narrows that split.

When the operating path needs a dedicated person or team,
[[dataops-engineer-role=>DataOps engineer role]] covers the staffing question.
When many teams need a supported shared route, [[DataOps Platforms]] covers the
platform question. The DataOps discipline remains the same in both cases. Teams
review and test changes. They release, observe, recover, and improve the next
change.
