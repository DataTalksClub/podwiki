---
layout: article
tags: ["comparison"]
title: "DataOps vs Data Engineering: Who Owns What Day-to-Day"
summary: "How DataTalks.Club podcast guests split day-to-day ownership between data engineering (building pipelines, models, and checks) and DataOps (making changes safe to review, run, observe, and recover), grounded in Tomasz Hinc, Christopher Bergh, and Lars Albertsson interviews."
related_wiki:
  - DataOps
  - Data Engineering
  - Data Engineer Role
  - Data Engineering Platforms
  - DataOps Platforms
  - Data Engineering Tools
  - Data Quality and Observability
  - Orchestration
  - CI/CD
---

For the general definitional comparison of DataOps with data engineering and
data science, see the DataTalks.Club article
[DataOps: Similarities and Differences with Data Engineering and Data Science](https://datatalks.club/blog/dataops-similarities-and-differences-with-data-engineering-and-data-science.html).
This page takes a narrower angle: what data engineering and DataOps each own
day-to-day, based on how DataTalks.Club podcast guests describe the split.

[[Data engineering]] owns building the
data paths other teams use. Day-to-day that means ingestion, storage, and
transformation, plus orchestration and the interfaces that make data usable for
analytics, machine learning, product systems, and operations. The output is
pipelines, models, and schedules.

[[DataOps]] owns making changes to those
paths safe to run. Day-to-day that means review and testing, deployment,
observability, onboarding, and recovery more than writing every pipeline. A
data engineer may do DataOps work, but the two jobs don't fill the same hours.

[[person:nataliekwong|Natalie Kwong]] grounds the
engineering side in ETL, ELT, and orchestration in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
She also covers CDC and warehouse work.
[[person:christopherbergh|Christopher Bergh]] grounds
the DataOps side in version control, tests, CI/CD, and observability in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]
and
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].

[[person:tomaszhinc|Tomasz Hinc]] gives the direct
boundary at 40:44 in
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]]:
data engineering is closer to pipeline coding and quality-check implementation.
DataOps is closer to support and communication. It also covers onboarding,
monitoring, and cross-team enablement.

## Short Comparison

Use data engineering when the team needs someone to design or build the data
path:

- source ingestion
- warehouse, lake, or lakehouse storage
  ([[Data Warehouse vs Data Lakehouse]])
- transformation logic and data models
- orchestration and dependency design
- interfaces for analysts, data scientists, product systems, or AI systems

Use DataOps when the team already has data paths but can't change or repair
them safely:

- code review and version control for data work
- automated tests and realistic test data
- CI/CD for pipeline changes
- observability for freshness, volume, schema, distribution, and lineage
- runbooks, backfills, incident response, and ownership

A mature data engineering team should practice DataOps, so the overlap is
real. The boundary is still useful because "build a pipeline" and "operate
pipeline changes safely" are different failure modes.

## Data Engineering Fit

Choose data engineering when the missing work is structural. The team may need
to collect data from source systems or decide between ETL and ELT. It may also
need to choose storage or model events into reliable tables.

Kwong's modern-stack episode gives the concrete vocabulary. She explains ETL at
3:46 and ELT at 7:57 in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
At 30:59, she places Airflow around scheduled pipeline runs. At 45:59, she
discusses CDC as a way to sync row-level changes.

[[person:santonatuli|Santona Tuli]] adds the pipeline
architecture version in
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]].
At 13:25, she compares ML pipelines with analytics pipelines. At 39:23-43:05,
she moves from transformation and data modeling into marts, dashboards, and
metrics.
Those are data engineering design choices before they become DataOps operating
concerns.

[[person:slawomirtulski|Slawomir Tulski]] makes the
role split explicit in
[[podcast:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for|Data Engineer Career in 2026]].
At 11:54-17:29, he separates platform data engineers from product-facing data
engineers. Platform data engineers build shared infrastructure and standards,
while product data engineers work closer to domain use cases and data products.

Use the [[Data Engineer Role]]
page when the question is about job scope. Use
[[Data Engineering Platforms]]
when the question is shared infrastructure.

## DataOps Fit

Choose DataOps when the team can build data paths but struggles to change them
without breakage. DataOps asks whether a pipeline change can move from review
to production and recovery without depending on one person's memory.

Bergh describes the practical DataOps target at 6:42 in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
Teams should reduce errors, shorten deployment cycles, and improve team
productivity. At 33:47, he covers version control, tests, and CI/CD. At 34:37,
he moves toward automated playbooks.

In
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
Bergh applies the same discipline to modern data engineering teams. At 15:52,
he ties DataOps to automation, observability, and productivity. At 30:55, he
covers CI/CD pipelines, regression tests, and test data. At 42:39 and 50:29,
deployment automation and production monitoring become part of the operating
surface.

[[person:larsalbertsson|Lars Albertsson]] gives the
platform version in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
At 11:50, he defines DataOps through enablement, workflows, and people
alignment. At 16:42 and 20:12, immutable pipeline architecture and
reproducibility become the main operating concerns. At 46:52, he adds quality
and schema automation.

Use [[DataOps Tools]] when the
question is tool categories. Use
[[DataOps Platforms]] when the
question is how operating practices become shared infrastructure.

Hinc gives a more team-facing version at 40:44-43:36 in
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]].
He puts DataOps closer to support, communication, and onboarding. Monitoring
and cross-team education belong there too. That doesn't remove engineering
work. It explains why
DataOps often shows up as enablement around the engineers who write and operate
pipelines.

## Shared Pipeline Work

Data engineering and DataOps meet inside the pipeline lifecycle. A data
engineer may write the ingestion job, transformation model, or scheduler
definition. DataOps practice decides how that change moves through review,
tests, and deployment. It also covers monitoring and repair.

That shared surface includes
[[orchestration]],
[[ci-cd|CI/CD]],
[[data-quality-and-observability|data quality]],
and [[data-quality-and-observability|data observability]].
It also includes ownership and documentation.

[[person:barrmoses|Barr Moses]] shows why the operating
layer matters in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
At 21:57, she describes the good-pipeline, bad-data problem. At 26:04, she
connects root-cause analysis to logs and lineage. At 29:00, ownership turns
signals into action. At 35:24, SLAs do the same.

The practical split is simple: data engineering changes the data path, while
DataOps makes the change safe to run again tomorrow.

## Incident Boundary

The boundary becomes easiest to see during incidents. If a source API changes
or a join creates duplicates, the data engineering fix may involve source
contracts, transformations, or schemas. If an Airflow DAG runs jobs in the
wrong order, the fix may involve orchestration.

DataOps asks why the team learned about the problem late. It asks whether tests
caught the change and whether monitors saw freshness or schema drift. It asks
whether lineage showed affected dashboards, models, or activation workflows. It
also asks who owned the dataset and which runbook should have been used.

Bergh's 38:01 discussion in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]
connects replaceability to handoffs, documentation, and lower on-call burden.
Moses's 38:14 and 1:00:27 sections in
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]]
connect alert thresholds and false-positive reduction to operational trust.

A team that only hires another data engineer may build more pipelines without
fixing release and recovery. A team that only buys a DataOps tool may still
lack the engineering owner who can redesign a broken data path.

## Team Design

Small teams often combine both responsibilities in one person. That can work if
the person keeps the operating habits visible. Those habits include pull
requests, tests, and ownership. They also include lineage, alert routing, and
runbooks.

Growing teams should separate the conversations even when the people overlap.
In
[[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]],
[[person:mehdiouazza|Mehdi Ouazza]] shows why an
Airflow cluster alone isn't a platform. Around 12:30-23:26, teams need naming
conventions and sequencing rules. They also need schema contracts and
onboarding habits.

Tulski's 2026 career episode adds the current role pressure. Platform data
engineers build standards and shared infrastructure, while product data
engineers stay closer to use cases. DataOps practices should support both
paths because both paths can break consumers when changes aren't tested,
observable, or recoverable.

## Related Pages

These pages cover the concepts and neighboring comparisons behind this boundary:

- [[DataOps]]
- [[Data Engineering]]
- [[Data Engineer Role]]
- [[Data Engineering Platforms]]
- [[DataOps Platforms]]
- [[DataOps Tools]]
- [[Data Engineering Tools]]
- [[Data Quality and Observability]]
- [[data-quality-and-observability|Data Observability]]
- [[Orchestration]]
- [[ci-cd|CI/CD]]
- [[MLOps vs DataOps]]

