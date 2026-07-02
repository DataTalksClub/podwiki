---
layout: wiki
title: "DataOps"
summary: "How DataTalks.Club podcast guests describe and practice DataOps: the operating discipline that makes changes to data pipelines, analytics workflows, and data platforms reviewable, testable, observable, and recoverable."
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

For the authoritative, plain-language definition of the term, see the
DataTalks.Club article
[What is DataOps exactly?](https://datatalks.club/blog/what-dataops-exactly.html).
This page is the concept hub for how DataTalks.Club podcast guests actually
describe and practice DataOps: the operating discipline that makes changes to
data pipelines, analytics workflows, and shared data platforms reviewable,
testable, observable, and recoverable. Teams use it to review and test data
changes, then deploy, monitor, and repair them.

The term sits beside [[Data Engineering]]
and [[MLOps]], but it doesn't replace
either one. Data engineering builds the data path. DataOps makes changes to
that path safer to run and recover. MLOps operates the model lifecycle, while
DataOps operates upstream datasets, transformations, and feature pipelines. The
boundary matters most when a model incident may have started in data delivery.

See
[[MLOps vs DataOps]] and
[[DataOps vs Data Engineering]]
when the boundary question is ownership, not tool choice.

[[person:christopherbergh|Christopher Bergh]] gives a
practical definition in
[[podcast:dataops-automation-and-reliable-data-pipelines|6:42|Mastering DataOps]].
Teams use DataOps to reduce errors, shorten deployment cycles, and improve
team productivity. [[person:larsalbertsson|Lars Albertsson]]
adds the platform version in
[[podcast:dataops-principles-and-scalable-data-platforms|11:50|DataOps 101 for Scaling Data Platforms]].
DataOps aligns people and platform design so data teams can scale without
losing reproducibility.

DataOps isn't a new job title or a synonym for
[[Data Engineering]]. It's the
operating model around data changes. Version control, tests, and CI/CD guide
release work. Observability, ownership, and recovery keep pipelines and data
products reliable after release.

[[book:20210913-dataops-for-dummies|DataOps for Dummies]]
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
[[podcast:dataops-automation-and-reliable-data-pipelines|33:47|Mastering DataOps]].
That path connects directly to [[ci-cd|CI/CD]].
He adds automated playbooks and runbook thinking at
[[podcast:dataops-automation-and-reliable-data-pipelines|34:37 in the same episode]].

In
[[podcast:dataops-for-data-engineering|30:55|DataOps for Data Engineering]],
he brings the same idea into regression tests and realistic test data. Modern
pipeline releases become the frame. His
[[podcast:dataops-for-data-engineering|deployment and monitoring chapters at 42:39 and 50:29]]
make deployment automation and production monitoring part of the definition.

DataOps also covers the data-specific failure modes that normal application
uptime checks miss. [[person:barrmoses|Barr Moses]]
describes the "good pipeline, bad data" problem in
[[podcast:data-quality-data-observability-data-reliability|21:57|Data Observability Explained]].
At
[[podcast:data-quality-data-observability-data-reliability|16:38 in that episode]],
she names freshness, volume, and distribution as core observability signals.
Schema and lineage explain where the failure came from. Ownership, SLAs, and
runbooks connect [[Data Quality and Observability]]
to operational recovery work.

## Platform, Delivery, and GitOps Entry Points

Guests mostly agree on the reliability goal, but they start from different
failure modes.

Albertsson starts from platform architecture. In
[[podcast:dataops-principles-and-scalable-data-platforms|16:42|DataOps 101 for Scaling Data Platforms]],
he emphasizes immutable pipeline design. At 20:12 in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101's reproducibility discussion]],
he moves into reproducibility problems. At
[[podcast:dataops-principles-and-scalable-data-platforms|the storage, compute, and automation chapters at 30:34 and 46:52]],
storage and compute become platform concerns. Workflow engines, quality
automation, and schema handling matter in the same platform view.

Bergh starts from fragile delivery practice. In
[[podcast:dataops-automation-and-reliable-data-pipelines|7:22|Mastering DataOps]],
he connects observability to production errors. Later, at
[[podcast:dataops-automation-and-reliable-data-pipelines|38:01|the replaceability and documentation chapter]],
he ties replaceability to handoffs and documentation. He also connects it to
lower on-call burden.

His DataOps framing often begins with Git and tests, while CI/CD, monitors,
and playbooks complete that delivery view.

[[person:tomaszhinc|Tomasz Hinc]] starts from
infrastructure enablement. In
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams at 20:56-26:21]],
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
[[DataOps Tools]] and
[[DataOps Platforms]].

## Pipeline Delivery and CI/CD

DataOps applies to ingestion, transformation, orchestration, and analytics
delivery.

[[person:nataliekwong|Natalie Kwong]] maps that surface
in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack at 3:46-12:39]].
She contrasts ETL with ELT and explains why teams move transformation work into
the warehouse. At
[[podcast:data-engineering-tools-modern-data-stack|30:59-31:31]],
she discusses Airflow, dbt, and orchestration. At
[[podcast:data-engineering-tools-modern-data-stack|45:59-48:58]],
CDC and schema evolution show why data teams need repeatable change handling.

The DataOps layer makes those engineering choices operable. Teams review SQL
models and ingestion jobs, plus scheduler definitions and infrastructure
changes that affect consumers.

Teams run tests with realistic data, deploy through repeatable release paths,
and keep a rerun or rollback plan for failed jobs. Bergh makes that delivery
path explicit in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering at 30:55-42:39]],
where CI/CD and regression tests appear together. Test data and deployment
automation belong in the same release path.

This is where [[Orchestration]],
[[ci-cd|CI/CD]], and
[[Data Engineering Platforms]]
connect to DataOps. Another person should be able to review a data change,
test it, and deploy it. They should also be able to observe its outputs and
rerun it after failure without reverse-engineering the whole pipeline.

A practical way to make that concrete is to require every change to a pipeline,
dbt model, notebook-turned-job, or infrastructure definition to pass four gates:
reviewable (owner, consumer impact, and expected output are visible), testable
(regression tests and realistic test data exercise the code and data
assumptions), deployable (an automated path rather than a manual checklist), and
observable (freshness, schema, lineage, and downstream behavior stay visible
after release). Bergh ties this supported path to the whole team using it, so
newer members can change production without relying on private knowledge
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering at 30:55-46:27]]).

## Observability and Recovery

DataOps depends on observability, but it covers more than monitoring. A
monitor can tell the team that a table is stale or a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook to follow, and how to prevent the same failure from returning.

Moses defines the monitoring layer in
[[podcast:data-quality-data-observability-data-reliability|16:38|Data Observability Explained]].
Freshness, volume, and distribution reveal failures that a successful job run
may hide. Schema and lineage reveal structural changes. At
[[podcast:data-quality-data-observability-data-reliability|24:31-29:00]],
she separates detection from diagnosis and connects root-cause analysis to
ownership. At
[[podcast:data-quality-data-observability-data-reliability|35:24-41:03]],
SLAs and runbooks make observability actionable.

Bergh connects those signals back to delivery practice in
[[podcast:dataops-for-data-engineering|50:29|DataOps for Data Engineering]],
where production monitoring becomes a starting point for operational
improvement. Monitoring without tests, release controls, owners, and recovery
paths leaves teams reacting to incidents one by one.

For the monitoring layer, see
[[Data Quality and Observability]]
and [[data-quality-and-observability|Data Observability]].
For the tooling layer across checks, alerts, and runbooks, see
[[DataOps Tools]].

## Platform and Self-Service

DataOps becomes shared platform infrastructure when many teams change or
consume data. Albertsson's
[[podcast:dataops-principles-and-scalable-data-platforms|7:52|DataOps 101 for Scaling Data Platforms]]
connects DataOps to self-service analytics. At
[[podcast:dataops-principles-and-scalable-data-platforms|28:22-30:34]],
he describes offline processing and storage as platform foundations. Compute
and workflow engines sit beside them. At
[[podcast:dataops-principles-and-scalable-data-platforms|50:13|the embedded engineering support chapter]],
he adds embedded engineering support.

Self-service only helps when the supported path preserves ownership,
reproducibility, and quality. [[person:mehdiouazza|Mehdi Ouazza]]
shows the team-scaling version in
[[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms at 12:30-23:26]].
An Airflow cluster alone doesn't create a platform. Teams also need naming
conventions and sequencing rules. Schema contracts, onboarding habits, and
playbooks make the supported path clearer.

[[DataOps Platforms]] covers the
shared infrastructure version of these practices.
[[self-service-data-platforms|Self-Service Data Platforms]]
covers the safer path for analysts, data scientists, software engineers, and
domain teams.

## DataOps vs Data Engineering

[[DataOps vs Data Engineering]]
covers the full boundary. Data engineering builds the data path, and DataOps
makes changes to that path safer to review and run. It also makes those
changes easier to observe and recover.

Kwong's modern-stack discussion shows the [[Data Engineering]]
side. She covers ETL, ELT, and dbt-style warehouse modeling alongside Airflow
orchestration. CDC and schema evolution appear in the same discussion:
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack at 3:46-12:39 and 30:59-48:58]].
Those choices define how data moves, where business logic lives, and how
consumers receive the output.

Bergh's DataOps interviews add the operating layer. Teams use version control,
tests, and CI/CD to review and release pipeline changes. Deployment automation
and production monitoring help them recover from failures. Runbooks and
on-call readiness matter too, as he explains in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering at 26:13 and 30:55-50:29]].

The boundary shows up during incidents. A data engineer may fix a bad
transformation, source schema, or orchestration dependency. DataOps practice
asks why the team learned about the problem late. It also asks whether
monitors detected the failure, who owned the dataset, which consumers were
affected, and which runbook should prevent a repeat.

## DataOps vs MLOps

DataOps and [[MLOps]] overlap because
production ML depends on production data, but they operate different assets.
DataOps covers upstream ingestion, transformations, datasets, and metadata.
Quality checks and recovery paths belong there too. MLOps adds model
artifacts, training jobs, model registries, and serving paths. Retraining
decisions and model behavior belong on the MLOps side.

Bergh makes the shared DevOps inheritance explicit in
[[podcast:dataops-automation-and-reliable-data-pipelines|50:42|Mastering DataOps]].
Albertsson separates shared principles from ML-specific requirements in
[[podcast:dataops-principles-and-scalable-data-platforms|53:31|DataOps 101 for Scaling Data Platforms]].

[[person:dannyleybzon|Danny Leybzon]] shows the
incident overlap in
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide at 25:04-27:35]],
where model monitoring includes ETL, data pipelines, and upstream root causes.
A model alert may come from model drift, but it may also come from a late
table or a changed schema. It may also come from a broken feature pipeline or
a missing label.
DataOps responders investigate data delivery. MLOps responders investigate the
model lifecycle.

The ownership version of that production ML boundary belongs in
[[MLOps vs DataOps]].

## Related Pages

Adjacent practices, platform topics, and comparison boundaries:

- [[DataOps Platforms]]
- [[DataOps Tools]]
- [[Data Engineering]]
- [[Data Engineering Platforms]]
- [[Data Engineering Tools]]
- [[Data Quality and Observability]]
- [[data-quality-and-observability|Data Observability]]
- [[Orchestration]]
- [[ci-cd|CI/CD]]
- [[MLOps]]
- [[MLOps vs DataOps]]
- [[DataOps vs Data Engineering]]
