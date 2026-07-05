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

DataOps is the operating discipline for reliable data delivery. Teams use it to
review and test changes to pipelines, analytics workflows, and data products.
They also use it to release, observe, and recover those changes. For the
authoritative plain-language definition, see the
[DataTalks.Club DataOps definition article](https://datatalks.club/blog/what-dataops-exactly.html).

DataOps sits beside [[Data Engineering]] and [[MLOps]], but it doesn't replace
either one. Use the term when teams review and release data changes. Teams also
observe, recover, and improve those changes.

[[DataOps vs Data Engineering]] covers responsibility boundaries, while
[[MLOps vs DataOps]] covers the model-incident boundary. [[DataOps Platforms]]
covers the shared service layer. [[DataOps Tools]] covers tool categories, and the
[[dataops-engineer-role=>DataOps engineer role]] covers staffing.

Fragile data changes create errors, and Bergh frames DataOps as the response
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps]].
Lars Albertsson adds the scale concern: more teams can build and consume data
only when the delivery path is reproducible
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps Platform]].

[[book:20210913-dataops-for-dummies=>DataOps for Dummies]] by Justin Mullen and
Guy Adams gives a compact overview of the same operating discipline.

## Reliable Data Delivery

DataOps makes data delivery repeatable and recoverable. Teams review pipeline
code, transformation logic, orchestration definitions, and infrastructure
changes before release. Then they test, deploy, and monitor the resulting tables
and data products
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

Version control, tests, CI/CD, and runbooks connect release work to repair
work
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
Regression tests and realistic test data sit beside deployment automation and
production monitoring
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

DataOps also covers the data-specific failures that ordinary application uptime
checks miss. A pipeline can succeed while the data is wrong
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Teams need signals for silent data failures and ownership paths for repair.
[[Data Quality and Observability]] covers freshness, volume, and distribution in
more detail. It also covers schema, lineage, and alert design.

[[DataOps Checks for Data Pipelines]] owns concrete pre-release and post-release
checks. [[DataOps Tools]] owns tests and alerts as tool categories. It also
owns lineage, deployment, and runbook tooling.

## Adoption Patterns

Teams often adopt DataOps from different starting points, but the reliability
goal stays consistent.

Albertsson starts with platform architecture and workflow support
[[cite:dataops-principles-and-scalable-data-platforms=>Platform]].
This path asks whether late data or bugs can be replayed with reproducible
dependencies
[[cite:dataops-principles-and-scalable-data-platforms=>Platform]].

[[person:christopherbergh=>Christopher Bergh]] starts from fragile delivery
practice. Git, tests, and CI/CD make releases repeatable, while monitors and
playbooks make repairs easier. Replaceability reduces handoff and on-call
pressure
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

[[person:tomaszhinc=>Tomasz Hinc]] starts from infrastructure enablement. SQL
changes, secrets, and Infrastructure as Code belong in the review path.
Terraform, Terragrunt, and Atlantis make environment and access changes
reviewable through merge requests and dry runs
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].

These are adoption paths, not competing definitions. A small team may need
Git-based release habits first, while an infrastructure-heavy team may need
reviewable access and environment changes. A growing platform team may need
shared workflow engines, templates, and support paths.

## Pipeline Releases and Strategy

DataOps applies to ingestion, transformation, orchestration, and analytics
delivery. [[ETL]], [[ELT]], and CDC all create changes that teams have to review.
Warehouse modeling and schema evolution create recoverable changes too
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
The DataOps layer makes those engineering choices operable rather than replacing
the engineering choices themselves.

For [[Data Strategy]] work, DataOps turns planned [[Data Products]] and
AI-powered use cases into managed releases instead of static plans. Boyan
Angelov connects DataOps to Lean and Agile habits. CI/CD and waste reduction
belong in the same delivery path.
He also connects it to changing requirements and repeatable data-product
delivery
[[cite:data-strategy-and-dataops-for-ai-powered-products@24:57=>Data Strategy and DataOps for AI-Powered Products]].
He also places DataOps beside impact assessment and portfolio management after
teams choose use cases and a target architecture
[[cite:data-strategy-and-dataops-for-ai-powered-products@18:56=>Strategy delivery]].

Data product intake belongs in the same operating path. Teams need the same
use-case list to survive delivery, measurement, and reprioritization
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
[[Orchestration]], [[ci-cd=>CI/CD]], and [[DataOps Checks for Data Pipelines]]
meet at that release-and-recovery boundary.

## Observability and Recovery

DataOps depends on observability, but monitoring is only the detection layer. A
monitor can tell the team that a table is stale or that a distribution changed.
DataOps asks who owns the dataset, which downstream users are affected, which
runbook applies, and how the team prevents the same failure from returning.

Freshness and volume expose data failures that a successful job run may hide.
Distribution, schema, and lineage explain the structure and source of the failure
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Detection is separate from diagnosis, and root-cause analysis connects to
ownership, SLAs, and runbooks
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Production monitoring also feeds the next release path. Real failures expose
missing tests, weak deployment automation, and unclear ownership
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]. Monitoring
without tests, release controls, owners, and recovery paths leaves teams
reacting to incidents one by one.

[[Data Quality and Observability]] and
[[data-quality-and-observability=>Data Observability]] own the monitoring layer.
[[DataOps Tools]] owns checks, alerts, lineage, and runbook categories.

## Shared Services, Staffing, and ML Boundaries

When many teams need the same operating path, platform teams may package
DataOps as shared services. Albertsson describes the platform as the technology
enabler for workflows and tooling. He also includes continuous deployment,
support, and self-service
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
[[DataOps Platforms]] owns that service design.
For data engineering teams, the
[[data-engineering-manager-role=>data engineering manager]] owns whether that
service path has staffing, quality standards, and stakeholder promises behind it
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].

DataOps becomes a role when one person or team is accountable for the operating
path across other data teams. Hinc puts that work near support, communication,
and onboarding. Monitoring education and troubleshooting sit there too
[[cite:dataops-and-gitops-best-practices-for-data-teams@40:44=>DataOps and GitOps for Data Teams]].
[[dataops-engineer-role=>DataOps engineer role]] owns the staffing question.

DataOps and MLOps overlap because production ML depends on production data.
DataOps covers upstream ingestion, transformations, datasets, and metadata.
Quality checks and data recovery stay there too.

MLOps owns model artifacts, training jobs, and model registries. Serving paths,
retraining decisions, and model behavior stay on the MLOps side. Model
monitoring can still trace an alert back to ETL, data pipelines, and upstream root causes
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]].
