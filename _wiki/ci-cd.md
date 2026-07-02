---
layout: wiki
title: "CI/CD"
summary: "Reference page for CI/CD in data, ML, and AI systems."
related:
  - DataOps
  - MLOps
  - GitOps for Data Teams
  - Reproducibility
  - Testing
  - Data Engineering Platforms
  - MLOps Tools
---

Data teams use CI/CD to move code and pipeline definitions through repeatable
checks. They use it for model artifacts and deployment changes too. In
DataTalks.Club discussions, the topic sits between
[[DataOps]] and
[[MLOps]]. It also depends on
[[testing]] and
[[reproducibility]].

Teams need more than a green build. They also need evidence that data
transformations and training code still work. Deployment targets, monitoring,
and rollback paths need to work after a change too.

[[person:christopherbergh|Christopher Bergh]] gives the
DataOps version in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps: Automation, Observability & CI/CD for Reliable Data Pipelines]]
and
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
[[person:mariavechtomova|Maria Vechtomova]] adds the
standardized MLOps platform version in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]].
[[person:raphaelhoogvliets|Raphaël Hoogvliets]] links
CI/CD to adoption, repository design, and package management in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
[[person:nemanjaradojkovic|Nemanja Radojkovic]] shows
how regulated finance teams adapt CI/CD to approvals, package governance, and
audit history in
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]].

## Repeatable Delivery

Bergh describes CI/CD as the delivery spine of DataOps. In
[[podcast:dataops-automation-and-reliable-data-pipelines|34:37|Mastering DataOps]],
he starts with code in version control, adds automated tests in development and
production, and automates deployment. He then counts the errors that remain. At
[[podcast:dataops-automation-and-reliable-data-pipelines|37:13 in the same discussion]],
he frames the work as code acting on data operations, not a naming argument
between DataOps and DevOps.

He revisits the same delivery problem in
[[podcast:dataops-for-data-engineering|30:55|DataOps for Data Engineering]],
where regression tests and automated deployment support safer releases.
Monitoring, realistic test data, and infrastructure as code belong to the same
safety case. At
[[podcast:dataops-for-data-engineering|42:39]], he warns
that Git alone isn't enough because data engineers, data scientists, and
analysts need end-to-end checks before a pipeline change reaches consumers.

For ML teams, CI/CD includes model lifecycle evidence alongside code quality.
In
[[podcast:pragmatic-and-standardized-mlops|12:42|Pragmatic and Standardized MLOps]],
Vechtomova describes a central MLOps team that provides shared infrastructure
and reusable CI/CD pipelines. The same team handles authentication and
monitoring.

At
[[podcast:pragmatic-and-standardized-mlops|18:41]], her
minimum stack starts with version control and CI/CD. It then adds container and
model registries, a deployment target, and monitoring. Those categories overlap
with [[MLOps Tools]] and
[[Data Engineering Platforms]]
when the same platform runs data and model releases.

## Adoption Paths

Teams enter CI/CD from different pain points. Bergh starts from data reliability
waste after teams lose time to errors, rework, unclear ownership, and fragile
handoffs. His answer in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]
is to automate delivery, then prove the data system with realistic data before
anyone calls a change done.

Vechtomova starts from organizational standardization. In
[[podcast:pragmatic-and-standardized-mlops|16:27|Pragmatic and Standardized MLOps]],
she argues that large companies often already have Kubernetes plus systems for
version control, orchestration, and CI/CD. Reusing those systems can save years
of integration work. Her concern is whether product teams can use the path
through templates, guardrails, and deployment conventions, not whether the
company owns another CI tool.

Hoogvliets starts from adoption in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
At [[podcast:mlops-at-scale-reproducibility-adoption|37:32]],
he warns that platform teams lose buy-in when standards block merges without
showing value. At
[[podcast:mlops-at-scale-reproducibility-adoption|48:41]],
he still calls CI/CD the usual starting point, but only after the team
understands the pain. Unknown production behavior may call for monitoring first.
Slow model releases may call for deployment automation first.

See
[[Platform Adoption]] and
[[Developer Experience]] for
the same adoption tradeoff in wider platform work.

Radojkovic starts from regulated delivery. In
[[podcast:mlops-and-ml-engineering-in-finance|22:25|MLOps in Finance]],
he explains that governance and approvals slow early deployments, but trust
improves after reviewers see repeated safe changes. At
[[podcast:mlops-and-ml-engineering-in-finance|23:39]],
he describes adapting ML pipelines and CI/CD to existing DevOps rules rather
than replacing corporate release rules. Those constraints link CI/CD to
[[Governance]] and
[[Security]].

## Tests and Test Data

Analytics and data-pipeline CI/CD has to prove that a change still works with
data. In
[[podcast:dataops-automation-and-reliable-data-pipelines|44:12|Mastering DataOps]],
Bergh says teams need to pour realistic data through the system. Immutable raw
data helps because teams can rerun Spark jobs, transformations, and
visualizations end to end. GitHub Actions or another CI tool is only one part of
the release path. Teams also need compliant test data, test-environment
resources, and time to keep those checks useful.

At
[[podcast:dataops-automation-and-reliable-data-pipelines|48:25 in Mastering DataOps]],
Bergh treats dbt tests and Great Expectations as options. Teams can also use
SQL checks, row counts, and expectation tests. Tests should live near the code,
run automatically in development, and keep running in production. CI/CD is
therefore part of [[Testing]] and
[[Data Quality and Observability]],
not only a deployment-speed concern.

ML CI/CD also has to preserve traceability. In
[[podcast:mlops-at-scale-reproducibility-adoption|39:06|MLOps at Scale]],
Hoogvliets says teams need proper CI, clear ML repository structure, and
standardized parameter handling. They also need test coverage around
preprocessing and post-processing. At
[[podcast:mlops-at-scale-reproducibility-adoption|42:31]],
he adds that exploratory work shouldn't disappear on someone's desktop because
it can later explain monitoring signals and production behavior. Hoogvliets
therefore links CI/CD to [[Experiment Tracking]]
and [[Model Monitoring]].

## Versioning and Rollback

Bergh prefers immutable raw data plus versioned logic. In
[[podcast:dataops-for-data-engineering|54:05|DataOps for Data Engineering]],
he says teams should keep raw data unchanged and version the code that acts on
it.

In
[[podcast:dataops-automation-and-reliable-data-pipelines|51:21|Mastering DataOps]],
Bergh adds that related code, models, and visualizations should move together.
Governance and catalog changes should move with them when they belong to the
same production change.

MLOps guests put more emphasis on model and data lineage. In
[[podcast:pragmatic-and-standardized-mlops|20:49|Pragmatic and Standardized MLOps]],
Vechtomova says Artifactory and S3 can work as artifact stores. MLflow-like
systems can work too if teams can trace and reproduce what they deployed.

At
[[podcast:pragmatic-and-standardized-mlops|22:23]], she
ties reproducibility to the record behind a deployment. Teams need the code,
compute, model artifact, and storage location. Without that record, rollback
gets painful.

Radojkovic sharpens the same control argument for finance. In
[[podcast:mlops-and-ml-engineering-in-finance|31:57|MLOps in Finance]],
he says a minimal ML Ops setup needs dev and production environments. Ideally,
the team also has a test environment and a DevOps platform with audit history.
It also needs monitoring, a model registry, and a data version registry.

Radojkovic argues that reproducible ML pipelines matter less because someone
expects to rerun last year's model by hand. They matter more because
reproducibility proves the team controls what's in production. See
[[Reproducibility]] and
[[Model Registry]] for the broader
lineage and rollback thread.

## Deployment Paths

Data CI/CD usually deploys transformations and schedules, and it may also deploy
reports and data-quality checks. Metadata and infrastructure may share the
release path when they affect the same production change.

ML CI/CD adds model artifacts, serving code, and feature or preprocessing code.
Containers and registries belong to the same release path,
along with monitoring and rollback paths. CI/CD therefore sits near
[[GitOps for Data Teams]],
[[MLOps Tools]], and
[[Data Engineering Platforms]].

The deployment target depends on the team. In
[[podcast:dataops-for-data-engineering|52:42|DataOps for Data Engineering]],
Bergh says Docker is the first container skill to learn. Kubernetes helps when a
team runs many services, but smaller teams may not need it. In
[[podcast:pragmatic-and-standardized-mlops|18:41|Pragmatic and Standardized MLOps]],
Vechtomova lists Kubernetes, Azure ML, and Databricks as possible deployment
targets. She treats the specific tool as secondary to the repeatable path.

In
[[podcast:mlops-at-scale-reproducibility-adoption|53:08|MLOps at Scale]],
Hoogvliets adds package registries because ML components often share
dependencies and configurations. Docker images still matter, but packaging helps
teams manage version ranges and compatibility when multiple models interact
with the same software environment.

## Standardization Without Blocking Teams

CI/CD fails when only the platform team can use it. Product teams and governance
reviewers need a shared path. Analytics engineers and data scientists need the
same path.

Bergh focuses on shared ownership. If only one data engineer can operate a
pipeline, the pipeline isn't done. In
[[podcast:dataops-automation-and-reliable-data-pipelines|43:06|Mastering DataOps]],
he hears the objection that version control, tests, and CI/CD look
implementable. His answer at
[[podcast:dataops-automation-and-reliable-data-pipelines|44:12]]
is that proving the whole data system is hard. Teams often optimize their own
part instead of the full delivery path.

Vechtomova's answer is to standardize the path without blocking teams. In
[[podcast:pragmatic-and-standardized-mlops|29:55|Pragmatic and Standardized MLOps]],
she describes cookie-cutter repositories and reusable CI/CD. Templates can check
repository conventions, permissions, tags, and deployment structure so data
scientists start from a deployable project instead of a blank repository.

Hoogvliets adds product thinking in
[[podcast:mlops-at-scale-reproducibility-adoption|36:55|MLOps at Scale]].
He says MLOps teams should collect pain points and show value instead of
assuming the best deployment method. A useful rollout may measure deployed
models, reduced deployment lead time, or fewer release freezes.

Radojkovic adds the governance constraint. In
[[podcast:mlops-and-ml-engineering-in-finance|23:39|MLOps in Finance]],
he describes using existing data-engineering deployment habits. At
[[podcast:mlops-and-ml-engineering-in-finance|25:55]],
he adds package approval. The finance path is slower than a startup credit-card
tool stack. ML engineers can make it routine when they build trust with
reviewers and reuse known platform standards.
