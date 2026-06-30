---
layout: wiki
title: "CI/CD"
summary: "Podcast-grounded reference page for CI/CD in data, ML, and AI systems."
related:
  - DataOps
  - MLOps
  - GitOps for Data Teams
  - Reproducibility
  - Testing
  - Data Engineering Platforms
  - MLOps Tools
---

CI/CD moves changes through a repeatable path in data, ML, and AI systems.
Teams version code and run automated checks. They produce deployable artifacts
and observe production behavior.

In the DataTalks.Club archive, guests rarely treat CI/CD as a standalone tool
choice. They connect it to
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). They also connect it to
[testing]({{ '/wiki/testing/' | relative_url }}) and
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}). Platform
conventions let teams change pipelines without waiting for one expert.

CI/CD has to prove more than "the code runs." For data work, it has to prove
that transformations still behave against realistic data. For ML work, it has
to preserve the path from training code and data to deployment, monitoring, and
rollback.

## Starting Points

Use these discussions as the core archive path:

- [Mastering DataOps: Automation, Observability & CI/CD for Reliable Data Pipelines]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
  with [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
  covers version control and automated tests, then connects deployment
  automation to test data and end-to-end versioning.
- [DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
  with [Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }})
  revisits the same CI/CD problem through regression tests and infrastructure
  as code. It also covers adoption gaps and observability. Docker, Kubernetes,
  and immutable raw data enter the same deployment discussion.
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
  with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
  frames reusable CI/CD pipelines as central MLOps infrastructure. It places
  them next to registries, deployment targets, monitoring, and code quality
  checks.
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  with [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
  connects CI/CD to team adoption and repository structure. It also covers
  parameterization, data-transformation tests, package registries, and
  deployment frequency.
- [MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})
  with [Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
  shows CI/CD inside regulated environments. Approvals, package governance,
  dev/test/prod separation, and audit trails all constrain the deployment path.

For adjacent concepts, use
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
for pull-request-driven operational changes. Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
for the shared systems CI/CD runs through. Use
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) for registries,
serving, monitoring, and platform workflow categories.

## Shared Meaning

Across the archive, CI/CD means a controlled way to change production data or ML
systems without relying on manual heroics. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
Christopher Bergh lays out a practical sequence at 34:37.

His sequence is:

- put code in version control
- write automated tests that run in production
- run automated tests in development to judge regression or impact
- automate deployment
- count the errors that still happen

At 37:13, he describes the operating idea as code acting on data operations, not
a label fight between DataOps and DevOps.

In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
Bergh makes the same point from the deployment side. At 30:55, he ties safe
change to regression tests and automated deployment. Monitoring, realistic test
data, and infrastructure as code are part of the same safety case. At 42:39, he
warns that Git alone isn't enough. Data engineers, data scientists, and analysts
need the same end-to-end checks.

For MLOps, guests add artifact and lifecycle concerns. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
Maria Vechtomova describes a central MLOps team at 12:42 as the group that
provides shared infrastructure and reusable CI/CD pipelines. That group also
handles authentication and monitoring so product teams don't rebuild the same
path. At 18:41, her minimum stack starts with version control and CI/CD. It also
needs container and model registries, a deployment target, and monitoring.

## Guest Differences

The guests agree that CI/CD matters, but they disagree on where to start.
Bergh starts from reliability waste in data work. Teams lose time to production
errors, rework, unclear ownership, and fragile handoffs. His answer is to
automate the delivery path, then prove the whole data system with realistic data
before anyone calls a change done.

Vechtomova starts from organizational standardization. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she argues at 16:27 that large companies often already have Kubernetes plus
systems for version control, orchestration, and CI/CD. The pragmatic move is to
reuse those systems and avoid spending years integrating another tool. Her
concern isn't whether CI/CD exists, but whether product teams can use it through
templates, guardrails, and deployment conventions.

Hoogvliets starts from adoption in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
where he warns at 37:32 that platform teams lose buy-in when standards block
merges without showing value. At 48:41, he still calls CI/CD the usual starting
point, but only after the team understands the pain. Unknown production behavior
may call for monitoring first, while slow model releases call for deployment
automation first.

Radojkovic starts from regulated delivery. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
he explains at 22:25 that governance and approvals slow early deployments, but
trust improves after reviewers see repeated safe changes. At 23:39, he describes
adapting ML pipelines and CI/CD to existing DevOps rules rather than replacing
the corporate release rules.

## Tests and Test Data

For analytics and data pipelines, CI/CD has to prove that a change still works
with data. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
Bergh says at 44:12 that proving a data system requires pouring realistic data
through the system. Immutable raw data can help because the team can rerun Spark
jobs, transformations, and visualizations end to end. Teams can't stop at
configuring GitHub Actions or another CI tool. They also need compliant test
data, resources for the test environment, and enough maintenance time to keep
those checks useful.

At 48:25 in the same discussion, Bergh treats dbt tests and Great Expectations
as options. Teams can also use SQL checks, row counts, and expectation tests.
Tests should live near the code, run automatically in development, and keep
running in production. That connects CI/CD directly to
[testing]({{ '/wiki/testing/' | relative_url }}) and observability, not just
deployment speed.

For ML systems, CI/CD also has to prove traceability.
In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Hoogvliets says at 39:06 that teams need proper CI, clear ML repository
structure, and standardized parameter handling. They also need test coverage
around preprocessing and post-processing. At 42:31, he adds that exploratory
work shouldn't disappear on someone's desktop because it can later explain
monitoring signals and production behavior.

## Versioning and Rollback

Bergh prefers immutable raw data plus versioned processing logic. In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
he says at 54:05 that teams should keep raw data unchanged and version the code
that acts on it.

In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he expands this at 51:21. Code, models, and visualizations should move with the
related governance and catalog changes when they belong to the same production
change.

MLOps guests put more emphasis on model and data lineage. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
Vechtomova says at 20:49 that Artifactory and S3 can work as artifact stores.
MLflow-like systems can work too if teams can trace and reproduce what was
deployed. At 22:23, she ties reproducibility to the record behind a deployment.
Teams need to know which code, compute, model artifact, and storage location
produced it because rollback becomes painful without that record.

In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
Radojkovic makes the control argument sharper for finance. At 31:57, he says a
minimal ML Ops setup needs dev and production environments. Ideally, the team
also has a test environment and a DevOps platform with audit history. It also
needs monitoring, a model registry, and a
data version registry.

He argues that reproducible ML pipelines matter less because someone expects to
rerun last year's model by hand. They matter more because reproducibility proves
the team controls what's in production.

Use
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) for that broader
thread.

## Deployment Paths

In data CI/CD, teams usually deploy transformations and schedules. They also
deploy reports and data-quality checks, while metadata and infrastructure may
enter the same release path.

In ML CI/CD, teams add model artifacts and serving code. They also add feature
or preprocessing code plus containers. Teams need registries, monitoring, and
rollback paths as well.

That's why CI/CD overlaps with
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

The deployment target depends on the team. In
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
Bergh says at 52:42 that Docker is the first container skill to learn.
Kubernetes helps when a team runs many processes, but smaller teams may not need
it. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
Vechtomova lists Kubernetes, Azure ML, and Databricks as possible deployment
targets at 18:41. She treats the specific tool as secondary to the repeatable
path.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Hoogvliets adds package registries at 53:08 because ML components often share
dependencies and configurations. Docker images still matter, but packaging helps
teams manage version ranges and compatibility when multiple models interact with
the same software environment.

## Adoption Tradeoffs

CI/CD fails when only the platform team can use it. Product and governance
teams need a shared path with analytics and data science teams. Bergh focuses
on shared ownership: if only one data engineer can operate a pipeline, the
pipeline isn't done.

At 43:06 in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
Bergh hears an objection that version control, tests, and CI/CD look
implementable.
His answer at 44:12 is that proving the whole data system is hard. Teams often
optimize their own part instead of the full delivery path.

Vechtomova's answer is to standardize the path without blocking teams. In
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she describes cookie-cutter repositories and reusable CI/CD at 29:55. Those
templates can check repository conventions, permissions, tags, and deployment
structure so data scientists start from a deployable project instead of a blank
repository.

Hoogvliets adds that teams need product thinking. In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
he says at 36:55 that MLOps teams should collect pain points and show value
instead of assuming the best deployment method. A useful CI/CD rollout may
measure models deployed through the platform, reduced deployment lead time, or
fewer release freezes.

Radojkovic adds the governance tradeoff. In
[MLOps in Finance]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }}),
he describes using existing data-engineering deployment patterns at 23:39 and
working through package approval at 25:55. That path is slower than a startup
credit-card tool stack. It can become routine when ML engineers build trust with
reviewers and reuse known platform patterns.

## See Also

Use these pages for the surrounding operating model:

- [DataOps]({{ '/wiki/dataops/' | relative_url }}) for CI/CD as part of reliable
  data-pipeline delivery.
- [MLOps]({{ '/wiki/mlops/' | relative_url }}) for CI/CD across model training,
  registries, deployment, monitoring, and retraining.
- [GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }})
  for reviewable infrastructure and operational changes.
- [Testing]({{ '/wiki/testing/' | relative_url }}) and
  [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) for the checks
  that make CI/CD credible.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  and [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}) for the shared
  systems that CI/CD runs through.
