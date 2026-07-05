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
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
  - MLOps vs DataOps
  - LLMOps
  - GitOps for Data Teams
---

DataOps is the operating practice for reliable data delivery. Teams use it to
review and test changes to data pipelines, analytics workflows, and data
products before release. They also keep those changes observable and
recoverable. For the authoritative plain-language definition, see the
[DataTalks.Club DataOps definition article](https://datatalks.club/blog/what-dataops-exactly.html).

The term sits beside [[Data Engineering]]
and [[MLOps]], but it doesn't replace
either one. Data engineering builds the data path. DataOps makes changes to
that path safer to run and recover. MLOps operates the model lifecycle, while
DataOps operates upstream datasets, transformations, and feature pipelines. The
boundary matters most when a model incident may have started in data delivery.

See [[MLOps vs DataOps]] and [[DataOps vs Data Engineering]] when the boundary
question is ownership, not tool choice. Use [[DataOps Tools]] for tool
categories and [[DataOps Platforms]] when teams need shared release,
observability, access, and recovery surfaces.

Use the [[dataops-engineer-role=>DataOps engineer role]] page when one person
or team owns the operating path across other data teams. Use
[[DataOps Checks for Data Pipelines]] when the question is which checks should
run before and after a pipeline change.

Teams use DataOps to reduce errors and shorten deployment cycles. Bergh also
ties it to team productivity
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Platform design discussions add the scale concern. When more teams change or
consume data, they need reproducible paths
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

DataOps is the practice layer, not a new job title or a synonym for
[[Data Engineering]]. Version control, tests, and CI/CD guide release work.
Observability, ownership, and recovery keep pipelines and data products reliable
after release. When one person owns that practice across teams, it becomes the
[[dataops-engineer-role=>DataOps engineer role]]. When teams package the
practice into shared infrastructure, the tooling discussion moves to
[[DataOps Platforms]].

[[book:20210913-dataops-for-dummies=>DataOps for Dummies]]
by Justin Mullen and Guy Adams gives a short overview of the same operating
discipline.

## Repeatable Data Delivery

DataOps makes data delivery repeatable and recoverable. In everyday data work,
teams review pipeline code and transformation logic before release. They also
review orchestration definitions and infrastructure changes. They test and
deploy those changes through CI/CD. Then they monitor the resulting tables,
dashboards, features, or data products.

Version control and tests connect DataOps directly to [[ci-cd=>CI/CD]]
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Automation playbooks and runbook thinking extend the same operating model
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

The same idea extends to regression tests and realistic test data, framed
around modern pipeline releases
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].
Deployment automation and production monitoring are part of the definition too
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

DataOps also covers the data-specific failure modes that normal application
uptime checks miss. The "good pipeline, bad data" problem is a core example
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Freshness, volume, and distribution are core observability signals, while schema
and lineage explain where the failure came from
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Ownership, SLAs, and runbooks connect [[Data Quality and Observability]]
to operational recovery work.

## Adoption Paths for Reliable Delivery

The reliability goal stays consistent, but teams often adopt DataOps after
different kinds of delivery pain.

[[person:larsalbertsson=>Lars Albertsson]] starts from platform architecture,
emphasizing immutable pipeline design and reproducibility
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
In that path, teams check whether they can rerun the same pipeline when data
arrives late or a bug appears. The dependencies and data assumptions have to
stay reproducible too
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

[[person:christopherbergh=>Christopher Bergh]] starts from fragile delivery
practice, connecting observability to production errors
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Replaceability ties to handoffs and documentation, and to lower on-call burden
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
This path begins with Git and tests. CI/CD, monitors, and playbooks then make
the release and repair path repeatable.

[[person:tomaszhinc=>Tomasz Hinc]] starts from infrastructure enablement,
covering SQL, secrets, and Infrastructure as Code. Terraform, Terragrunt,
and Atlantis complete the GitOps example
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].
This version of DataOps makes access, infrastructure, and environment changes
reviewable through merge requests and dry runs.

These paths aren't competing definitions, so a small team may need Git-based
release habits first. An infrastructure-heavy team may need reviewable access
and environment changes. A growing platform team may need the same practice
encoded in shared workflow engines, templates, and support paths.

Across those cases, DataOps still asks whether a data change can be reviewed
and tested, then observed and recovered. For the system surfaces behind those
paths, see [[DataOps Platforms]]. For individual categories, see
[[DataOps Tools]].

## Pipeline Delivery and CI/CD

DataOps applies to ingestion, transformation, orchestration, and analytics
delivery because ETL and ELT decisions determine where transformations run.
Warehouse modeling, CDC, and schema evolution add more changes that teams have
to review and recover
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].

The DataOps layer makes those engineering choices operable. Teams review SQL
models and ingestion jobs, plus scheduler definitions and infrastructure
changes that affect consumers. For the tool taxonomy behind those choices, use
[[DataOps Tools]] and [[Data Engineering Tools]].

Teams run tests with realistic data, deploy through repeatable release paths,
and keep a rerun or rollback plan for failed jobs. CI/CD and regression tests
appear together, and test data and deployment automation belong in the same
release path
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

For [[Data Strategy]] work, the same delivery layer turns planned
[[Data Products]] and AI-powered use cases into managed releases instead of a
static deck. DataOps combines Lean and Agile habits with CI/CD practices. That
combination helps the team reduce waste, handle changing requirements, and ship
data products through repeatable delivery practices
[[cite:data-strategy-and-dataops-for-ai-powered-products@24:57=>Data Strategy and DataOps for AI-Powered Products]].

Boyan Angelov emphasizes the Lean side as avoiding known waste in data work, not
only chasing ideal plans. That fits DataOps because failed handoffs, waiting,
unclear requirements, and unmeasured pilots all become operating problems once a
strategy reaches delivery
[[cite:data-strategy-and-dataops-for-ai-powered-products@25:03=>Lean and Agile DataOps]].
He also places DataOps beside impact assessment and portfolio management, after
teams have chosen use cases and a target architecture. Teams therefore connect
DataOps to [[data-product-intake-and-prioritization=>data product intake]]
because the same use-case list has to survive delivery, measurement, and
reprioritization
[[cite:data-strategy-and-dataops-for-ai-powered-products@18:56=>Strategy delivery]].

This is where [[Orchestration]] and [[ci-cd=>CI/CD]] connect to DataOps.
Another person should be able to review a data change, test it, and deploy it.
They should also be able to observe its outputs and rerun it after failure
without reverse-engineering the whole pipeline.

The supported path works only when the whole team can review and test changes.
They should also be able to deploy, observe, and rerun production jobs without
relying on private knowledge
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]. For
data-specific gates and checks, see
[[DataOps Checks for Data Pipelines]].

## Observability and Recovery

DataOps depends on observability, but it covers more than monitoring. A
monitor can tell the team that a table is stale or a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook to follow, and how to prevent the same failure from returning.

Freshness, volume, and distribution reveal failures that a successful job run
may hide, and schema and lineage reveal structural changes
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Detection is separate from diagnosis, and root-cause analysis connects to
ownership
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
SLAs and runbooks make observability actionable
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Production monitoring becomes a starting point for operational improvement,
connecting those signals back to delivery practice
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].
Monitoring without tests, release controls, owners, and recovery paths leaves
teams reacting to incidents one by one.

For the monitoring layer, see
[[Data Quality and Observability]]
and [[data-quality-and-observability=>Data Observability]].
For the tooling layer across checks, alerts, and runbooks, see
[[DataOps Tools]].

## Shared Infrastructure Boundary

DataOps becomes platform work when many teams need the same reliable path for
pipeline, warehouse, access, and recovery changes. Albertsson connects DataOps
to self-service through workflows, tooling, continuous deployment, and platform
support
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Self-service still has to preserve ownership, reproducibility, and quality. An
Airflow cluster alone doesn't give teams a reliable operating path. Teams also
need naming conventions and sequencing rules. Schema contracts, onboarding
habits, and playbooks make the path usable across teams
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams and Self-Service Platforms]].

Use [[DataOps Platforms]] for platform components, release paths, and
observability integrations. Use it too for governance, access, self-service,
and managed-versus-built platform choices.
[[self-service-data-platforms=>Self-Service Data Platforms]] covers the safer
path for analysts, data scientists, software engineers, and domain teams.

## DataOps vs Data Engineering

[[DataOps vs Data Engineering]]
covers the full boundary. Data engineering builds the data path, and DataOps
makes changes to that path safer to review and run. It also makes those
changes easier to observe and recover. Hinc's DataOps/GitOps discussion puts
that boundary in support, communication, onboarding, and operational education.
It isn't only pipeline coding
[[cite:dataops-and-gitops-best-practices-for-data-teams@40:44=>DataOps and GitOps for Data Teams]].

The modern-stack discussion shows the [[Data Engineering]] side through ETL,
ELT, and dbt-style warehouse modeling alongside Airflow orchestration. It also
covers CDC and schema evolution
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
Those choices define how data moves, where business logic lives, and how
consumers receive the output.

DataOps adds the operating layer. Teams use version control, tests, and CI/CD
to review and release pipeline changes, while deployment automation and
production monitoring help them recover from failures. Runbooks and on-call
readiness matter too
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

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
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
They separate shared principles from ML-specific requirements
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

The incident overlap shows up when model monitoring includes ETL, data
pipelines, and upstream root causes
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].
A model alert may come from model drift. It may also come from a late table, a
changed schema, a broken feature pipeline, or a missing label. DataOps responders
investigate data delivery, while MLOps responders investigate the model
lifecycle.

The ownership version of that production ML boundary belongs in
[[MLOps vs DataOps]]. For incident triage use
[[model-monitoring-vs-data-observability=>model monitoring vs data observability]]
when the lead response is unclear. It separates model monitoring from upstream
data observability
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].

## Related Pages

Adjacent practices, platform topics, and comparison boundaries:

- [[DataOps Platforms]]
- [[DataOps Tools]]
- [[DataOps Checks for Data Pipelines]]
- [[Data Engineering]]
- [[Data Engineering Platforms]]
- [[Data Engineering Tools]]
- [[Data Quality and Observability]]
- [[data-quality-and-observability=>Data Observability]]
- [[Orchestration]]
- [[ci-cd=>CI/CD]]
- [[MLOps]]
- [[MLOps vs DataOps]]
- [[DataOps vs Data Engineering]]
