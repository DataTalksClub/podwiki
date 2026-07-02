---
layout: wiki
title: "DataOps"
summary: "How DataTalks.Club podcast guests describe and practice DataOps: the operating discipline that makes changes to data pipelines, analytics workflows, and data platforms reviewable, testable, observable, and recoverable."
related:
  - DataOps Platforms
  - DataOps Engineer Role
  - Data Engineering Platforms
  - Data Engineering Tools
  - Data Quality and Observability
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
  - LLMOps
  - GitOps for Data Teams
  - MLOps vs DevOps
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

Teams use DataOps to reduce errors, shorten deployment cycles, and improve
team productivity
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
The platform version aligns people and platform design so data teams can scale
without losing reproducibility
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].

DataOps isn't a new job title or a synonym for
[[Data Engineering]]. It's the
operating model around data changes. Version control, tests, and CI/CD guide
release work. Observability, ownership, and recovery keep pipelines and data
products reliable after release. When that operating model has to be owned
across teams rather than adopted inside one, it can become a dedicated
[[dataops-engineer-role|DataOps engineer role]].

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

Version control and tests connect DataOps directly to [[ci-cd|CI/CD]]
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
Automated playbooks and runbook thinking extend the same operating model
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].

The same idea extends to regression tests and realistic test data, framed
around modern pipeline releases
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
Deployment automation and production monitoring are part of the definition too
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].

DataOps also covers the data-specific failure modes that normal application
uptime checks miss. The "good pipeline, bad data" problem is a core example
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
Freshness, volume, and distribution are core observability signals, while schema
and lineage explain where the failure came from
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
Ownership, SLAs, and runbooks connect [[Data Quality and Observability]]
to operational recovery work.

## Platform, Delivery, and GitOps Entry Points

Guests mostly agree on the reliability goal, but they start from different
failure modes.

[[person:larsalbertsson|Lars Albertsson]] starts from platform architecture,
emphasizing immutable pipeline design and reproducibility
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
Storage and compute become platform concerns, and workflow engines, quality
automation, and schema handling matter in the same platform view
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].

[[person:christopherbergh|Christopher Bergh]] starts from fragile delivery
practice, connecting observability to production errors
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
Replaceability ties to handoffs and documentation, and to lower on-call burden
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].

This framing begins with Git and tests, while CI/CD, monitors, and playbooks
complete the delivery view.

[[person:tomaszhinc|Tomasz Hinc]] starts from infrastructure enablement,
covering SQL, secrets, and Infrastructure as Code, with Terraform, Terragrunt,
and Atlantis completing the GitOps example
[[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]].
This version of DataOps makes access, infrastructure, and environment changes
reviewable through merge requests and dry runs.

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

ETL contrasts with ELT, and teams move transformation work into the warehouse
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Airflow, dbt, and orchestration cover the scheduling surface
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
CDC and schema evolution show why data teams need repeatable change handling
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].

The DataOps layer makes those engineering choices operable. Teams review SQL
models and ingestion jobs, plus scheduler definitions and infrastructure
changes that affect consumers.

Teams run tests with realistic data, deploy through repeatable release paths,
and keep a rerun or rollback plan for failed jobs. CI/CD and regression tests
appear together, and test data and deployment automation belong in the same
release path
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].

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
after release). The supported path works only when the whole team uses it, so
newer members can change production without relying on private knowledge
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

## Observability and Recovery

DataOps depends on observability, but it covers more than monitoring. A
monitor can tell the team that a table is stale or a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook to follow, and how to prevent the same failure from returning.

Freshness, volume, and distribution reveal failures that a successful job run
may hide, and schema and lineage reveal structural changes
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
Detection is separate from diagnosis, and root-cause analysis connects to
ownership
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].
SLAs and runbooks make observability actionable
[[podcast:data-quality-data-observability-data-reliability|Data Observability Explained]].

Production monitoring becomes a starting point for operational improvement,
connecting those signals back to delivery practice
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
Monitoring without tests, release controls, owners, and recovery paths leaves
teams reacting to incidents one by one.

For the monitoring layer, see
[[Data Quality and Observability]]
and [[data-quality-and-observability|Data Observability]].
For the tooling layer across checks, alerts, and runbooks, see
[[DataOps Tools]].

## Platform and Self-Service

DataOps becomes shared platform infrastructure when many teams change or
consume data. It connects to self-service analytics
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
Offline processing and storage are platform foundations, with compute and
workflow engines beside them, and embedded engineering support completes the
picture
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].

Self-service only helps when the supported path preserves ownership,
reproducibility, and quality. An Airflow cluster alone doesn't create a
platform; teams also need naming conventions and sequencing rules, and schema
contracts, onboarding habits, and playbooks make the supported path clearer
([[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams and Self-Service Platforms]]).

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

The modern-stack discussion shows the [[Data Engineering]] side: ETL, ELT, and
dbt-style warehouse modeling alongside Airflow orchestration, with CDC and
schema evolution in the same discussion
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Those choices define how data moves, where business logic lives, and how
consumers receive the output.

DataOps adds the operating layer. Teams use version control, tests, and CI/CD
to review and release pipeline changes, while deployment automation and
production monitoring help them recover from failures. Runbooks and on-call
readiness matter too
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].

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

DataOps and MLOps share a DevOps inheritance
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
Shared principles separate from ML-specific requirements
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].

The incident overlap shows up when model monitoring includes ETL, data
pipelines, and upstream root causes
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]].
A model alert may come from model drift, but it may also come from a late table,
a changed schema, a broken feature pipeline, or a missing label. DataOps
responders investigate data delivery, while MLOps responders investigate the
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
