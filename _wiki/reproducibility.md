---
layout: wiki
title: "Reproducibility"
summary: "How DataTalks.Club podcast guests make data science, ML, research, and data pipeline work rerunnable, reviewable, and explainable."
related:
  - MLOps
  - DataOps
  - Experiment Tracking
  - Data Quality and Observability
  - ML Platforms
  - Practices
  - Software Engineering
---

Reproducibility means a team can rerun a data result, review it, or explain it
after the original work has moved on. It is not just a research virtue or a
tooling label. It's the operating habit that connects an output to the code,
data, environment, and parameters behind it. It also preserves the tests,
approvals, and people who shaped the result.

Reproducibility appears in three connected settings. The research version
packages code and papers and preserves data and environments so another
researcher can recreate the result
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).
The [[DataOps]] version relies on immutable
datasets and functional transformations
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).

The [[MLOps]] version runs through
[[Experiment Tracking]],
[[Model Registry]], metadata, and
lineage, connecting reproducibility to data references, containers, and
deployment records
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

That makes reproducibility a bridge across engineering, operations, and
platform work. The engineering side includes
[[Software Engineering]],
[[ci-cd|CI/CD]], and
[[Testing]]. The operating side includes
[[Data Quality and Observability]],
[[Data Governance]], and
[[ML Platforms]].

The exact capture mechanism changes by domain, but the standard converges. A
reproducible team can explain how a result was produced. It can also identify
what must be rerun, reviewed, or changed.

## The Reproducibility Record

A reproducible team can recover the path from input to result. The result may
be a paper figure or analytics table. It may also be a model artifact,
dashboard, or prediction. Someone other than the original author can look at the
assumptions, rerun the work, or explain why the result changed.

In research, a reproducible-paper example packages code with the manuscript so
another person can start from the data and regenerate the paper. Turned into
engineering practice, this means project structure, environments, Git branches,
and formatting, plus MLflow for model version control and preserved metadata or
model parameters when sensitive clinical data can't be shared
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).

On a data platform, mutable warehouse-style tables make reruns unstable because
the same ETL process can produce different results at different times. The
answer is immutable raw data plus functional transformations, orchestrated as
pipelines that create new datasets instead of overwriting old ones
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).

In ML delivery, full reproducibility is hard, but tying code to data versions
helps teams reverse-engineer what happened. Maturity is part of the definition:
smaller teams may not need full data versioning on day one, but work with
regulation or customer-facing decisions may need it earlier
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

## Domain Priorities

Priorities differ most on scope and timing. Some approaches start from teaching,
while others start from operations or platform risk.

From a teaching standpoint, researchers and junior data scientists need Git,
data management, and reproducible examples, along with an end-to-end view of a
project before they enter teams that depend on their work
([[podcast:devrel-data-science-open-source-tools|DevRel for Data Science]]).

From an operations standpoint, one emphasis is architectural immutability and
raw-data history, and another is delivery discipline: teams put code, reports,
and transformations in version control, run automated tests, use CI/CD, and run
the whole system against test data when possible
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

From an ML platform standpoint, the focus is experiment tracking, model
registries, metadata, data references, deployment records, package registries,
and monitoring. Copying every training dataset into an experiment tracker is
risky: large datasets can make that approach unworkable, and cost and GDPR
deletion requests can do the same
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The disagreement is not about whether reproducibility matters but about where to
spend the next unit of effort. A research lab may need tests and a reproducible
paper template. A data platform may need immutable raw inputs and workflow
orchestration.

An ML platform may need experiment tracking first. As model risk grows, the
same platform may also need data versioning, dependency management, and
lineage.

## Research and Teaching

In academia, reproducibility is a skill gap as much as a tooling gap. Academia
faces a reproducibility crisis: people publish papers that others can't
recreate, especially in fields such as neuroimaging
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).
A course sequence for this starts with Git and reproducible publications, then
moves into tests, open source contribution, packaging, environments, and
requirements files.

The same gap appears in data science education: labs often lack training for
long-lived data management, collaboration, and complete reproduction of code.
DVC work at Iterative and later teaching help applied data science students make
educated choices about managing projects before they enter industry
([[podcast:devrel-data-science-open-source-tools|DevRel for Data Science]]).

The research-to-production bridge matters too. Researchers use notebooks,
benchmarks, and tools such as Weights & Biases to validate hypotheses, which
contrasts with the ML engineer's responsibility for deployment, uptime,
monitoring, Docker, cloud infrastructure, and web services. Reproducibility
improves when researchers learn engineering fundamentals and engineers learn how
to reproduce models and track experiments
([[podcast:research-to-production-ml-systems-roadmap|From Research to Production]]).

## Data Pipelines

Pipeline reproducibility starts with stable inputs. Immutable raw data is the
foundation: teams should transform immutable datasets into new datasets rather
than mutate tables in place, and add workflow orchestration so pipelines have
explicit dependencies and late data, transient failures, and bugs can be retried
and repaired
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).

From the delivery path, practical steps are version control, automated tests,
development tests, deployment automation, and error tracking. Beyond unit tests,
data teams should run the system end to end against realistic test data, keep
tests close to the code, and run checks in development and production
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

Infrastructure belongs in the same reproducibility conversation. Infrastructure
as code with Terraform, Terragrunt, and Atlantis, plus merge requests, review,
and dry runs, keeps environments reproducible. In one dependency example, an
unspecified Python package version caused a Dockerized application to fail after
it fetched a newer API. Pinning versions isn't ceremony there because it
prevents a future run from silently becoming a different run
([[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]]).

## MLOps and Platforms

ML reproducibility extends the pipeline record with experiment and artifact
history. Experiment tracking is an early win for collaboration, and the tracked
run sits near the model registry because a useful run may become an artifact
that downstream systems consume
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
The record expands from there: a platform may need to store which job image ran,
which inputs it consumed, which outputs it wrote, and how metadata connects
across pipeline runs. The model registry alone isn't enough to reproduce a model
result from three years ago; code versions, data versions, metadata, and
workflow design all matter.

This becomes an adoption sequence that groups CI, repository structure, and
parameterization with testing and experiment preservation, and starts from a
real pain point: CI/CD when deployment takes months, monitoring when models are
opaque in production, and missing version control escalated immediately
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

Teams should add experiment tracking and model registries when they remove a
concrete delivery risk. The same applies to serving, monitoring, package
registries, and containers.

## Data Boundaries and Governance

Reproducibility can conflict with privacy, cost, and governance. In research,
sensitive consortium data can't simply be pushed to a repository, though model
parameters and metadata may still be shareable
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).

On a platform, tools that log a query or metadata differ from tools that copy
the full dataset artifact. Copying a 50 GB training dataset for every run can
create cost problems, and GDPR deletion problems too, because the team may need
to find and remove one person's data across many duplicated artifacts
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Lakes raise a similar point: raw dumps and history help teams reproduce past
states, but personal data requires separation and governance. Full database
dumps preserve more history than mutable tables, yet they also require clear
handling for GDPR and change capture
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).

## Risk-Based Capture

Reproducibility works as a risk-based capture set rather than one universal tool
stack.

- Code and workflow definitions, including reports, transformations, model
  code, infrastructure code, and orchestration dependencies
  ([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]],
  [[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]]).
- Inputs or input references. Teams may use immutable raw data, versioned
  datasets, query metadata, or controlled-access data depending on privacy and
  scale
  ([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
- Environment and dependency records, including package versions, Docker
  images, requirements files, and package registries
  ([[podcast:dataops-and-gitops-best-practices-for-data-teams|DataOps and GitOps for Data Teams]],
  [[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
- Run metadata, experiment logs, parameters, metrics, and model registry
  entries
  ([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]],
  [[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
- Tests and checks, including data transformation tests, end-to-end tests,
  production data quality checks, and development regression checks
  ([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]],
  [[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
- Governance and downstream artifacts, including model outputs,
  visualizations, catalogs, and data governance changes when those artifacts
  change together
  ([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]]).

Use the capture set only when it matches the risk. A tutorial project can use a
small, fully bundled dataset. A bank model, clinical dataset, or
customer-facing fraud decision may need stricter metadata and lineage. It may
also need stricter approval, deletion, and audit paths.

## Related Pages

These related pages cover the operating layers around reproducibility.

- [[MLOps]]
- [[DataOps]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[ML Platforms]]
- [[Data Lake]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[ci-cd|CI/CD]]
- [[Testing]]
- [[Software Engineering]]
