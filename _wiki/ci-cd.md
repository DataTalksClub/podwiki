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
checks, and to cover model artifacts and deployment changes. The topic sits
between [[DataOps]] and [[MLOps]], and depends on [[testing]] and
[[reproducibility]].

A green build is not enough. Teams also need evidence that data transformations
and training code still work, and that deployment targets, monitoring, and
rollback paths still work after a change.

CI/CD takes several forms across the archive. As the delivery spine of DataOps
it centers on version control, automated tests, and automated deployment
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]],
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]). As a
standardized MLOps platform it adds shared infrastructure and reusable pipelines
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).
It also drives adoption, repository design, and package management
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]), and in
regulated finance it adapts to approvals, package governance, and audit history
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]).

## Repeatable Delivery

CI/CD is the delivery spine of DataOps: code in version control, automated tests
in both development and production, automated deployment, and then a count of the
errors that remain. The work is code acting on data operations rather than a
naming argument between DataOps and DevOps
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

The same delivery problem recurs with regression tests and automated deployment
supporting safer releases; monitoring, realistic test data, and infrastructure
as code belong to the same safety case. Git alone is not enough, because data
engineers, data scientists, and analysts need end-to-end checks before a pipeline
change reaches consumers
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

For ML teams, CI/CD includes model-lifecycle evidence alongside code quality. A
central MLOps team can provide shared infrastructure and reusable CI/CD
pipelines while also handling authentication and monitoring. A minimum stack
starts with version control and CI/CD, then adds container and model registries,
a deployment target, and monitoring. Those categories overlap with
[[MLOps Tools]] and [[Data Engineering Platforms]] when the same platform runs
data and model releases
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

## Adoption Paths

Teams enter CI/CD from different pain points.

Data-reliability waste is one entry point: after teams lose time to errors,
rework, unclear ownership, and fragile handoffs, the fix is to automate delivery
and then prove the data system with realistic data before any change is called
done ([[person:christopherbergh|Christopher Bergh]],
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

Organizational standardization is another. Large companies often already run
Kubernetes plus systems for version control, orchestration, and CI/CD, and
reusing those systems can save years of integration work. The real question is
whether product teams can use the path through templates, guardrails, and
deployment conventions, not whether the company owns another CI tool
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

Adoption itself is a third. Platform teams lose buy-in when standards block
merges without showing value. CI/CD is still the usual starting point, but only
after the team understands the pain: unknown production behavior may call for
monitoring first, and slow model releases may call for deployment automation
first ([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

See [[Platform Adoption]] and [[Developer Experience]] for the same adoption
tradeoff in wider platform work.

Regulated delivery is a fourth. Governance and approvals slow early deployments,
but trust improves after reviewers see repeated safe changes. ML pipelines and
CI/CD adapt to existing DevOps rules rather than replacing corporate release
rules, which links CI/CD to [[Governance]] and [[Security]]
([[person:nemanjaradojkovic|Nemanja Radojkovic]],
[[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]).

## Tests and Test Data

Analytics and data-pipeline CI/CD has to prove that a change still works with
data. Realistic data must flow through the whole system; immutable raw data
helps, because teams can rerun Spark jobs, transformations, and visualizations
end to end. GitHub Actions or another CI tool is only one part of the release
path — compliant test data, test-environment resources, and time to keep the
checks useful matter as much. dbt tests and Great Expectations are options,
alongside SQL checks, row counts, and expectation tests. Tests should live near
the code, run automatically in development, and keep running in production.
CI/CD is therefore part of [[Testing]] and
[[Data Quality and Observability]], not only a deployment-speed concern
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

ML CI/CD also has to preserve traceability: proper CI, a clear ML repository
structure, standardized parameter handling, and test coverage around
preprocessing and post-processing. Exploratory work should not disappear on
someone's desktop, because it can later explain monitoring signals and
production behavior, which links CI/CD to [[Experiment Tracking]] and
[[Model Monitoring]]
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

## Versioning and Rollback

Immutable raw data plus versioned logic is one preferred pattern: keep raw data
unchanged and version the code that acts on it. Related code, models, and
visualizations should move together, and governance and catalog changes should
move with them when they belong to the same production change
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]],
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

MLOps practice puts more emphasis on model and data lineage. Artifactory and S3
can serve as artifact stores, and MLflow-like systems work too, provided teams
can trace and reproduce what they deployed. Reproducibility ties back to the full
record behind a deployment — the code, compute, model artifact, and storage
location — without which rollback becomes painful
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

In finance the same control argument sharpens. A minimal MLOps setup needs
development and production environments, ideally a test environment and a DevOps
platform with audit history, plus monitoring, a model registry, and a data
version registry. Reproducible ML pipelines matter less because anyone expects to
rerun last year's model by hand, and more because reproducibility proves the team
controls what is in production. See [[Reproducibility]] and [[Model Registry]]
for the broader lineage and rollback thread
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]).

## Deployment Paths

Data CI/CD usually deploys transformations and schedules, and may also deploy
reports and data-quality checks; metadata and infrastructure share the release
path when they affect the same production change.

ML CI/CD adds model artifacts, serving code, and feature or preprocessing code,
with containers and registries on the same release path, along with monitoring
and rollback. CI/CD therefore sits near [[GitOps for Data Teams]],
[[MLOps Tools]], and [[Data Engineering Platforms]].

The deployment target depends on the team. Docker is the first container skill to
learn; Kubernetes helps when a team runs many services, but smaller teams may not
need it ([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).
Kubernetes, Azure ML, and Databricks are all possible deployment targets, with
the specific tool secondary to a repeatable path
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).
Package registries matter because ML components often share dependencies and
configurations; Docker images still count, but packaging helps teams manage
version ranges and compatibility when multiple models interact with the same
software environment
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

## Standardization Without Blocking Teams

CI/CD fails when only the platform team can use it. Product teams, governance
reviewers, analytics engineers, and data scientists all need a shared path.

Shared ownership is the first requirement: if only one data engineer can operate
a pipeline, the pipeline is not done. The objection that version control, tests,
and CI/CD look easy to implement misses the hard part — proving the whole data
system — because teams often optimize their own part instead of the full delivery
path
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

Standardizing the path without blocking teams is the second: cookie-cutter
repositories and reusable CI/CD, with templates that check repository
conventions, permissions, tags, and deployment structure, so data scientists
start from a deployable project instead of a blank repository
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

Product thinking is the third: MLOps teams should collect pain points and show
value instead of assuming the best deployment method, measuring rollout through
deployed models, reduced deployment lead time, or fewer release freezes
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

Governance is the fourth: existing data-engineering deployment habits plus
package approval make the finance path slower than a startup credit-card tool
stack, but ML engineers can make it routine by building trust with reviewers and
reusing known platform standards
([[podcast:mlops-and-ml-engineering-in-finance|MLOps in Finance]]).
