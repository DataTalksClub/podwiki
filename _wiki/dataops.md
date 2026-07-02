---
layout: wiki
title: "DataOps"
keyword: "what is dataops"
secondary_keywords:
  - what is data ops
  - dataops
  - data ops
summary: "DataOps, also searched as data ops, as the operating discipline for reliable data pipelines, analytics workflows, and data platforms."
related:
  - DataOps Platforms
  - Data Engineering Platforms
  - Data Engineering Tools
  - Data Quality and Observability
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
---

DataOps, sometimes written as data ops, is the operating discipline for
reliable data delivery. Teams use it to review and test data pipelines, then
deploy, monitor, and repair those pipelines. The same habits apply to analytics
workflows and shared data platforms. For a plain-language overview of the
concept, see
[What is DataOps exactly?](https://datatalks.club/blog/what-dataops-exactly.html).
This page focuses on how DataTalks.Club podcast guests define and practice it.

The term sits beside [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}), but it doesn't replace
either one. Data engineering builds the data path. DataOps makes changes to
that path safer to run and recover. MLOps operates the model lifecycle, while
DataOps operates upstream datasets, transformations, and feature pipelines. The
boundary matters most when a model incident may have started in data delivery.

See
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}) and
[DataOps vs Data Engineering]({{ '/wiki/dataops-vs-data-engineering/' | relative_url }})
when the boundary question is ownership, not tool choice.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) gives a
practical definition in
[Mastering DataOps at 6:42]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
Teams use DataOps to reduce errors, shorten deployment cycles, and improve
team productivity. [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
adds the platform version in
[DataOps 101 for Scaling Data Platforms at 11:50]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
DataOps aligns people and platform design so data teams can scale without
losing reproducibility.

DataOps isn't a new job title or a synonym for
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}). It's the
operating model around data changes. Version control, tests, and CI/CD guide
release work. Observability, ownership, and recovery keep pipelines and data
products reliable after release.

[DataOps for Dummies]({{ '/books/20210913-dataops-for-dummies/' | relative_url }})
by Justin Mullen and Guy Adams gives a short overview of the same operating
discipline.

## Repeatable Data Delivery

DataOps makes data delivery repeatable and recoverable. In everyday data ops
work, teams review pipeline code and transformation logic before release. They
also review orchestration definitions and infrastructure changes.

Teams test those changes before release. Then they deploy through CI/CD and
monitor the resulting outputs. Those outputs include tables and dashboards.
They may also include features or data products.

Bergh connects DataOps to version control and tests in
[Mastering DataOps at 33:47]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
That path connects directly to [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}).
He adds automated playbooks and runbook thinking at
[34:37 in the same episode]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).

In
[DataOps for Data Engineering at 30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
he brings the same idea into regression tests and realistic test data. Modern
pipeline releases become the frame. His
[deployment and monitoring chapters at 42:39 and 50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
make deployment automation and production monitoring part of the definition.

DataOps also covers the data-specific failure modes that normal application
uptime checks miss. [Barr Moses]({{ '/people/barrmoses/' | relative_url }})
describes the "good pipeline, bad data" problem in
[Data Observability Explained at 21:57]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
At
[16:38 in that episode]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she names freshness, volume, and distribution as core observability signals.
Schema and lineage explain where the failure came from. Ownership, SLAs, and
runbooks connect [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
to operational recovery work.

## Platform, Delivery, and GitOps Entry Points

Guests mostly agree on the reliability goal, but they start from different
failure modes.

Albertsson starts from platform architecture. In
[DataOps 101 for Scaling Data Platforms at 16:42]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he emphasizes immutable pipeline design. At 20:12 in
[DataOps 101's reproducibility discussion]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he moves into reproducibility problems. At
[the storage, compute, and automation chapters at 30:34 and 46:52]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
storage and compute become platform concerns. Workflow engines, quality
automation, and schema handling matter in the same platform view.

Bergh starts from fragile delivery practice. In
[Mastering DataOps at 7:22]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he connects observability to production errors. Later, at
[the replaceability and documentation chapter at 38:01]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he ties replaceability to handoffs and documentation. He also connects it to
lower on-call burden.

His DataOps framing often begins with Git and tests, while CI/CD, monitors,
and playbooks complete that delivery view.

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) starts from
infrastructure enablement. In
[DataOps and GitOps for Data Teams at 20:56-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
he discusses SQL, secrets, and Infrastructure as Code. Terraform, Terragrunt,
and Atlantis complete the GitOps example. His version of DataOps makes access,
infrastructure, and environment changes reviewable through merge requests and
dry runs.

Those differences are useful rather than contradictory because teams enter
DataOps through different problems. A small team may need Git-based release
habits first. A growing platform team may start with workflow engines and
self-service conventions, while an infrastructure-heavy team may need GitOps
for data access and environments. Across all three versions, teams still check
whether data changes can be reviewed and tested, then observed and recovered.
For stack choices behind those entry points, see
[DataOps Tools]({{ '/wiki/dataops-tools/' | relative_url }}) and
[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}).

## Pipeline Delivery and CI/CD

DataOps applies to ingestion, transformation, orchestration, and analytics
delivery.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) maps that surface
in
[ETL vs ELT and the Modern Data Stack at 3:46-12:39]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
She contrasts ETL with ELT and explains why teams move transformation work into
the warehouse. At
[30:59-31:31]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
she discusses Airflow, dbt, and orchestration. At
[45:59-48:58]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
CDC and schema evolution show why data teams need repeatable change handling.

The DataOps layer makes those engineering choices operable. Teams review SQL
models and ingestion jobs, plus scheduler definitions and infrastructure
changes that affect consumers.

Teams run tests with realistic data, deploy through repeatable release paths,
and keep a rerun or rollback plan for failed jobs. Bergh makes that delivery
path explicit in
[DataOps for Data Engineering at 30:55-42:39]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
where CI/CD and regression tests appear together. Test data and deployment
automation belong in the same release path.

This is where [Orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
connect to DataOps. Another person should be able to review a data change,
test it, and deploy it. They should also be able to observe its outputs and
rerun it after failure without reverse-engineering the whole pipeline.

## Observability and Recovery

DataOps depends on observability, but it covers more than monitoring. A
monitor can tell the team that a table is stale or a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook to follow, and how to prevent the same failure from returning.

Moses defines the monitoring layer in
[Data Observability Explained at 16:38]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
Freshness, volume, and distribution reveal failures that a successful job run
may hide. Schema and lineage reveal structural changes. At
[24:31-29:00]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she separates detection from diagnosis and connects root-cause analysis to
ownership. At
[35:24-41:03]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
SLAs and runbooks make observability actionable.

Bergh connects those signals back to delivery practice in
[DataOps for Data Engineering at 50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
where production monitoring becomes a starting point for operational
improvement. Monitoring without tests, release controls, owners, and recovery
paths leaves teams reacting to incidents one by one.

For the monitoring layer, see
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
For the tooling layer across checks, alerts, and runbooks, see
[DataOps Tools]({{ '/wiki/dataops-tools/' | relative_url }}).

## Platform and Self-Service

DataOps becomes shared platform infrastructure when many teams change or
consume data. Albertsson's
[DataOps 101 for Scaling Data Platforms at 7:52]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
connects DataOps to self-service analytics. At
[28:22-30:34]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he describes offline processing and storage as platform foundations. Compute
and workflow engines sit beside them. At
[the embedded engineering support chapter at 50:13]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
he adds embedded engineering support.

Self-service only helps when the supported path preserves ownership,
reproducibility, and quality. [Mehdi Ouazza]({{ '/people/mehdiouazza/' | relative_url }})
shows the team-scaling version in
[Scaling Data Engineering Teams and Self-Service Platforms at 12:30-23:26]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
An Airflow cluster alone doesn't create a platform. Teams also need naming
conventions and sequencing rules. Schema contracts, onboarding habits, and
playbooks make the supported path clearer.

[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}) covers the
shared infrastructure version of these practices.
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
covers the safer path for analysts, data scientists, software engineers, and
domain teams.

## DataOps vs Data Engineering

[DataOps vs Data Engineering]({{ '/wiki/dataops-vs-data-engineering/' | relative_url }})
covers the full boundary. Data engineering builds the data path, and DataOps
makes changes to that path safer to review and run. It also makes those
changes easier to observe and recover.

Kwong's modern-stack discussion shows the [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
side. She covers ETL, ELT, and dbt-style warehouse modeling alongside Airflow
orchestration. CDC and schema evolution appear in the same discussion:
[ETL vs ELT and the Modern Data Stack at 3:46-12:39 and 30:59-48:58]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Those choices define how data moves, where business logic lives, and how
consumers receive the output.

Bergh's DataOps interviews add the operating layer. Teams use version control,
tests, and CI/CD to review and release pipeline changes. Deployment automation
and production monitoring help them recover from failures. Runbooks and
on-call readiness matter too, as he explains in
[DataOps for Data Engineering at 26:13 and 30:55-50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}).

The boundary shows up during incidents. A data engineer may fix a bad
transformation, source schema, or orchestration dependency. DataOps practice
asks why the team learned about the problem late. It also asks whether
monitors detected the failure, who owned the dataset, which consumers were
affected, and which runbook should prevent a repeat.

## DataOps vs MLOps

DataOps and [MLOps]({{ '/wiki/mlops/' | relative_url }}) overlap because
production ML depends on production data, but they operate different assets.
DataOps covers upstream ingestion, transformations, datasets, and metadata.
Quality checks and recovery paths belong there too. MLOps adds model
artifacts, training jobs, model registries, and serving paths. Retraining
decisions and model behavior belong on the MLOps side.

Bergh makes the shared DevOps inheritance explicit in
[Mastering DataOps at 50:42]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
Albertsson separates shared principles from ML-specific requirements in
[DataOps 101 for Scaling Data Platforms at 53:31]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) shows the
incident overlap in
[MLOps Architect Guide at 25:04-27:35]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
where model monitoring includes ETL, data pipelines, and upstream root causes.
A model alert may come from model drift, but it may also come from a late
table or a changed schema. It may also come from a broken feature pipeline or
a missing label.
DataOps responders investigate data delivery. MLOps responders investigate the
model lifecycle.

The ownership version of that production ML boundary belongs in
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}).

## Related Pages

Adjacent practices, platform topics, and comparison boundaries:

- [DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }})
- [DataOps Tools]({{ '/wiki/dataops-tools/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }})
- [DataOps vs Data Engineering]({{ '/wiki/dataops-vs-data-engineering/' | relative_url }})
