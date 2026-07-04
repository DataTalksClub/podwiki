---
layout: wiki
title: "CI/CD"
summary: "CI/CD for data, ML, and AI teams: tests, deployment paths, traceability, rollback, and platform adoption."
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
checks. For ML teams, that path also covers model artifacts and deployment
changes. The topic sits between [[DataOps]] and [[MLOps]], and depends on [[Testing]] and
[[Reproducibility]].

A green build isn't enough for data and ML work. Teams also need evidence that
transformations and training code still work. Deployment targets, monitoring,
and rollback paths also have to survive a change.

## CI/CD Scope

In DataOps, CI/CD is the delivery path for version-controlled pipeline code,
automated tests, and automated deployment. The work is code acting on data
operations, not a naming argument between DataOps and DevOps.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

In MLOps, CI/CD extends that path to model artifacts and deployment targets. It
also includes registries, monitoring, and repository conventions. A shared
platform may provide reusable pipelines, authentication, and deployment
templates so product teams can release models through a common path.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

In regulated finance, CI/CD also includes approval rules, package governance, and
audit history. The release path adapts to existing DevOps controls instead of
replacing corporate release rules.
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]

## Team Differences

CI/CD isn't a single tool choice. DataOps discussions focus on full-system proof
with realistic data and production checks. MLOps platform discussions focus on
reusable infrastructure, repository standards, and model lineage.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

The starting point also differs by pain. Unknown production behavior may call
for monitoring first, while slow model releases may call for deployment
automation first. Platform standards lose adoption when they block merges without showing
value, so CI/CD work also belongs with [[Platform Adoption]] and
[[Developer Experience]].
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Repeatable Delivery

DataOps frames CI/CD as the delivery spine. The path starts with code in version
control, automated tests in development and production, automated deployment,
and a count of the errors that remain.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

The same delivery problem recurs with regression tests and automated deployment
supporting safer releases. Monitoring, realistic test data, and infrastructure
as code belong to the same safety case. Git alone isn't enough because data
engineers, data scientists, and analysts need end-to-end checks before a
pipeline change reaches consumers.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

For ML teams, CI/CD includes model-lifecycle evidence alongside code quality. A
minimum stack starts with version control and CI/CD, then adds container and
model registries, a deployment target, and monitoring. Those categories overlap
with [[MLOps Tools]] and [[Data Engineering Platforms]] when the same platform
runs data and model releases.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

## Tests and Test Data

Analytics and data-pipeline CI/CD has to prove that a change still works with
data. Realistic data must flow through the whole system. Immutable raw data helps
because teams can rerun Spark jobs, transformations, and visualizations end to
end. GitHub Actions or another CI tool is only one part of the release path.
Compliant test data, test-environment resources, and time to keep the checks
useful matter as much.

dbt tests and Great Expectations are options alongside SQL checks, row counts,
and expectation tests. Tests should live near the code, run automatically in
development, and keep running in production. CI/CD is therefore part of
[[Testing]] and [[Data Quality and Observability]], not only a deployment-speed
concern.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

ML CI/CD also has to preserve traceability. That means proper CI, a clear ML
repository structure, standardized parameter handling, and test coverage around
preprocessing and post-processing. Exploratory work shouldn't disappear on
someone's desktop. It can later explain monitoring signals and production
behavior, linking CI/CD to [[Experiment Tracking]] and [[Model Monitoring]].
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Versioning and Rollback

Immutable raw data plus versioned logic is one preferred approach. Teams keep
raw data unchanged and version the code that acts on it. Code, models, and
visualizations should move together when they belong to the same production
change. Governance and catalog changes should move with them too.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

MLOps practice puts more emphasis on model lineage and data lineage. Artifactory
and S3 can serve as artifact stores. MLflow-like systems work too, provided
teams can trace and reproduce what they deployed.

Reproducibility ties back to the full record behind a deployment. The record
includes the code, compute, model artifact, and storage location. Without that
record, rollback becomes painful.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

In finance, the control argument sharpens. A minimal MLOps setup needs
development and production environments, ideally a test environment and a DevOps
platform with audit history. It also needs monitoring, a model registry, and a
data version registry.

Reproducible ML pipelines matter less because anyone expects to rerun last
year's model by hand. They matter more because reproducibility proves the team
controls what's in production. See [[Reproducibility]] and [[Model Registry]]
for the broader lineage and rollback thread.
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]

## Deployment Paths

Data CI/CD usually deploys transformations and schedules, and may also deploy
reports and data-quality checks. Metadata and infrastructure share the release
path when they affect the same production change.

ML CI/CD adds model artifacts and serving code. It also includes feature or
preprocessing code, with containers and registries on the same release path.
Monitoring and rollback belong there too. CI/CD therefore sits near [[GitOps for
Data Teams]], [[MLOps Tools]], and [[Data Engineering Platforms]].

The deployment target depends on the team, and Docker is the first container
skill to learn. Kubernetes helps when a team runs many services, but smaller
teams may not need it.
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Kubernetes, Azure ML, and Databricks are all possible deployment targets, with
the specific tool secondary to a repeatable path.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

Package registries matter because ML components often share dependencies and
configurations. Docker images still count, but packaging helps teams manage
version ranges and compatibility when multiple models interact with the same
software environment.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Standardization Without Blocking Teams

CI/CD fails when only the platform team can use it. Product teams, governance
reviewers, analytics engineers, and data scientists all need a shared path.

The first requirement is shared ownership. If only one data engineer can operate
a pipeline, the pipeline isn't done. The objection that version control, tests,
and CI/CD look easy to implement misses the hard part: proving the whole data
system. Teams often optimize their own part instead of the full delivery path.
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Standardizing the path without blocking teams is the second requirement.
Cookie-cutter repositories and reusable CI/CD give data scientists a deployable
project instead of a blank repository. Templates can check repository
conventions, permissions, tags, and deployment structure.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

Product thinking is the third requirement. MLOps teams should collect pain
points and show value instead of assuming the best deployment method. They can
measure rollout through deployed models, reduced deployment lead time, or fewer
release freezes.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Governance is the fourth requirement. Existing data-engineering deployment
habits plus package approval make the finance path slower than a startup
credit-card tool stack. ML engineers can make it routine by building trust with
reviewers and reusing known platform standards.
[[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]

## Related Pages

CI/CD connects most directly to these adjacent pages:

- [[DataOps]]
- [[MLOps]]
- [[GitOps for Data Teams]]
- [[Testing]]
- [[Reproducibility]]
