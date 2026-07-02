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
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). It also depends on
[testing]({{ '/wiki/testing/' | relative_url }}) and
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}).

Teams need more than a green build. They also need evidence that data
transformations and training code still work. Deployment targets, monitoring,
and rollback paths need to work after a change too.

[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) gives the
DataOps version in
[Mastering DataOps: Automation, Observability & CI/CD for Reliable Data Pipelines](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
and
[DataOps for Data Engineering](https://datatalks.club/podcast/dataops-for-data-engineering.html).
[Maria Vechtomova](https://datatalks.club/people/mariavechtomova.html) adds the
standardized MLOps platform version in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html).
[Raphaël Hoogvliets](https://datatalks.club/people/raphaelhoogvliets.html) links
CI/CD to adoption, repository design, and package management in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).
[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) shows
how regulated finance teams adapt CI/CD to approvals, package governance, and
audit history in
[MLOps in Finance](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html).

## Repeatable Delivery

Bergh describes CI/CD as the delivery spine of DataOps. In
[Mastering DataOps at 34:37](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he starts with code in version control, adds automated tests in development and
production, and automates deployment. He then counts the errors that remain. At
[37:13 in the same discussion](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he frames the work as code acting on data operations, not a naming argument
between DataOps and DevOps.

He revisits the same delivery problem in
[DataOps for Data Engineering at 30:55](https://datatalks.club/podcast/dataops-for-data-engineering.html),
where regression tests and automated deployment support safer releases.
Monitoring, realistic test data, and infrastructure as code belong to the same
safety case. At
[42:39](https://datatalks.club/podcast/dataops-for-data-engineering.html), he warns
that Git alone isn't enough because data engineers, data scientists, and
analysts need end-to-end checks before a pipeline change reaches consumers.

For ML teams, CI/CD includes model lifecycle evidence alongside code quality.
In
[Pragmatic and Standardized MLOps at 12:42](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
Vechtomova describes a central MLOps team that provides shared infrastructure
and reusable CI/CD pipelines. The same team handles authentication and
monitoring.

At
[18:41](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html), her
minimum stack starts with version control and CI/CD. It then adds container and
model registries, a deployment target, and monitoring. Those categories overlap
with [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
when the same platform runs data and model releases.

## Adoption Paths

Teams enter CI/CD from different pain points. Bergh starts from data reliability
waste after teams lose time to errors, rework, unclear ownership, and fragile
handoffs. His answer in
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
is to automate delivery, then prove the data system with realistic data before
anyone calls a change done.

Vechtomova starts from organizational standardization. In
[Pragmatic and Standardized MLOps at 16:27](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she argues that large companies often already have Kubernetes plus systems for
version control, orchestration, and CI/CD. Reusing those systems can save years
of integration work. Her concern is whether product teams can use the path
through templates, guardrails, and deployment conventions, not whether the
company owns another CI tool.

Hoogvliets starts from adoption in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).
At [37:32](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
he warns that platform teams lose buy-in when standards block merges without
showing value. At
[48:41](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
he still calls CI/CD the usual starting point, but only after the team
understands the pain. Unknown production behavior may call for monitoring first.
Slow model releases may call for deployment automation first.

See
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) for
the same adoption tradeoff in wider platform work.

Radojkovic starts from regulated delivery. In
[MLOps in Finance at 22:25](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
he explains that governance and approvals slow early deployments, but trust
improves after reviewers see repeated safe changes. At
[23:39](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
he describes adapting ML pipelines and CI/CD to existing DevOps rules rather
than replacing corporate release rules. Those constraints link CI/CD to
[Governance]({{ '/wiki/governance/' | relative_url }}) and
[Security]({{ '/wiki/security/' | relative_url }}).

## Tests and Test Data

Analytics and data-pipeline CI/CD has to prove that a change still works with
data. In
[Mastering DataOps at 44:12](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
Bergh says teams need to pour realistic data through the system. Immutable raw
data helps because teams can rerun Spark jobs, transformations, and
visualizations end to end. GitHub Actions or another CI tool is only one part of
the release path. Teams also need compliant test data, test-environment
resources, and time to keep those checks useful.

At
[48:25 in Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
Bergh treats dbt tests and Great Expectations as options. Teams can also use
SQL checks, row counts, and expectation tests. Tests should live near the code,
run automatically in development, and keep running in production. CI/CD is
therefore part of [Testing]({{ '/wiki/testing/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
not only a deployment-speed concern.

ML CI/CD also has to preserve traceability. In
[MLOps at Scale at 39:06](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
Hoogvliets says teams need proper CI, clear ML repository structure, and
standardized parameter handling. They also need test coverage around
preprocessing and post-processing. At
[42:31](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
he adds that exploratory work shouldn't disappear on someone's desktop because
it can later explain monitoring signals and production behavior. Hoogvliets
therefore links CI/CD to [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

## Versioning and Rollback

Bergh prefers immutable raw data plus versioned logic. In
[DataOps for Data Engineering at 54:05](https://datatalks.club/podcast/dataops-for-data-engineering.html),
he says teams should keep raw data unchanged and version the code that acts on
it.

In
[Mastering DataOps at 51:21](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
Bergh adds that related code, models, and visualizations should move together.
Governance and catalog changes should move with them when they belong to the
same production change.

MLOps guests put more emphasis on model and data lineage. In
[Pragmatic and Standardized MLOps at 20:49](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
Vechtomova says Artifactory and S3 can work as artifact stores. MLflow-like
systems can work too if teams can trace and reproduce what they deployed.

At
[22:23](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html), she
ties reproducibility to the record behind a deployment. Teams need the code,
compute, model artifact, and storage location. Without that record, rollback
gets painful.

Radojkovic sharpens the same control argument for finance. In
[MLOps in Finance at 31:57](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
he says a minimal ML Ops setup needs dev and production environments. Ideally,
the team also has a test environment and a DevOps platform with audit history.
It also needs monitoring, a model registry, and a data version registry.

Radojkovic argues that reproducible ML pipelines matter less because someone
expects to rerun last year's model by hand. They matter more because
reproducibility proves the team controls what's in production. See
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) and
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}) for the broader
lineage and rollback thread.

## Deployment Paths

Data CI/CD usually deploys transformations and schedules, and it may also deploy
reports and data-quality checks. Metadata and infrastructure may share the
release path when they affect the same production change.

ML CI/CD adds model artifacts, serving code, and feature or preprocessing code.
Containers and registries belong to the same release path,
along with monitoring and rollback paths. CI/CD therefore sits near
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}),
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}), and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

The deployment target depends on the team. In
[DataOps for Data Engineering at 52:42](https://datatalks.club/podcast/dataops-for-data-engineering.html),
Bergh says Docker is the first container skill to learn. Kubernetes helps when a
team runs many services, but smaller teams may not need it. In
[Pragmatic and Standardized MLOps at 18:41](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
Vechtomova lists Kubernetes, Azure ML, and Databricks as possible deployment
targets. She treats the specific tool as secondary to the repeatable path.

In
[MLOps at Scale at 53:08](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
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
[Mastering DataOps at 43:06](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
he hears the objection that version control, tests, and CI/CD look
implementable. His answer at
[44:12](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)
is that proving the whole data system is hard. Teams often optimize their own
part instead of the full delivery path.

Vechtomova's answer is to standardize the path without blocking teams. In
[Pragmatic and Standardized MLOps at 29:55](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she describes cookie-cutter repositories and reusable CI/CD. Templates can check
repository conventions, permissions, tags, and deployment structure so data
scientists start from a deployable project instead of a blank repository.

Hoogvliets adds product thinking in
[MLOps at Scale at 36:55](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).
He says MLOps teams should collect pain points and show value instead of
assuming the best deployment method. A useful rollout may measure deployed
models, reduced deployment lead time, or fewer release freezes.

Radojkovic adds the governance constraint. In
[MLOps in Finance at 23:39](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
he describes using existing data-engineering deployment habits. At
[25:55](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
he adds package approval. The finance path is slower than a startup credit-card
tool stack. ML engineers can make it routine when they build trust with
reviewers and reuse known platform standards.
