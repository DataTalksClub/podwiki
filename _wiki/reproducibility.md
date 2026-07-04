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
after the original work has moved on. It isn't just a research virtue or a
tooling label. It's the operating habit that connects an output to the code,
data, environment, and parameters behind it. It also preserves the tests,
approvals, and people who shaped the result.

Reproducibility appears in research, DataOps, and MLOps settings. The research
version packages code with papers while preserving data and environments so another
researcher can recreate the result
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].
The [[DataOps]] version relies on immutable
datasets and functional transformations
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

The [[MLOps]] version runs through
[[Experiment Tracking]],
[[Model Registry]], metadata, and lineage. It connects reproducibility to data
references, containers, and
deployment records
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]],
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

That makes reproducibility a bridge across engineering, operations, and
platform work. The engineering side includes
[[Software Engineering]],
[[ci-cd=>CI/CD]], and
[[Testing]]. The operating side includes
[[Data Quality and Observability]],
[[Data Governance]], and
[[ML Platforms]].

The exact capture mechanism changes by domain, but the standard converges. A
reproducible team can explain how a result was produced. It can also identify
what must be rerun, reviewed, or changed.

## Reproducibility Records

A reproducible team can recover the path from input to result. The result may
be a paper figure or analytics table. It may also be a model artifact,
dashboard, or prediction. Someone other than the original author can look at the
assumptions, rerun the work, or explain why the result changed.

In research, a reproducible-paper example packages code with the manuscript.
Another person can start from the data and regenerate the paper.

In engineering practice, the same idea becomes project structure and
environments. It also uses Git branches and formatting. The record can include
MLflow for model version control. It can also preserve metadata or model
parameters when sensitive clinical data can't be shared
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].

A lighter record can still improve reproducibility when it captures experiment
intent and outcomes. In a machine learning competition, Christoph Molnar used an
Obsidian logbook for short daily notes. The notes recorded what he tried and
where he got stuck. They also captured why a failed attempt such as adding
weather data let him move to the next experiment
[[cite:interpretable-machine-learning@36:21=>Interpretable Machine Learning]].

On a data platform, mutable warehouse-style tables make reruns unstable because
the same ETL process can produce different results at different times. The
answer is immutable raw data plus functional transformations, orchestrated as
pipelines that create new datasets instead of overwriting old ones
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

Full reproducibility is hard in ML delivery. Tying code to data versions helps
teams reverse-engineer what happened. Maturity is part of the definition:
smaller teams may not need full data versioning on day one. Work with regulation
or customer-facing decisions may need it earlier
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

## Capture Priorities

Priorities differ most on scope and timing. Some approaches start from teaching,
while others start from operations or platform risk.

From a teaching standpoint, researchers and junior data scientists need Git,
data management, and reproducible examples. They also need an end-to-end view of
a project before they enter teams that depend on their work
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

From an operations standpoint, one emphasis is architectural immutability and
raw-data history. Another is delivery discipline. Teams put code, reports, and
transformations in version control. They run automated tests, use CI/CD, and run
the whole system against test data when possible
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

From an ML platform standpoint, the focus is experiment tracking and model
registries. It also includes metadata, data references, and deployment records.
Package registries and monitoring belong in the same record. Copying every
training dataset into an experiment tracker is risky. Large datasets can make
that approach unworkable, and cost and GDPR deletion requests can do the same
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

The disagreement isn't about whether reproducibility matters but about where to
spend the next unit of effort. A research lab may need tests and a reproducible
paper template. A data platform may need immutable raw inputs and workflow
orchestration.

An ML platform may need experiment tracking first. As model risk grows, the
same platform may also need data versioning, dependency management, and
lineage.

## Research and Teaching

In academia, reproducibility is a skill gap as much as a tooling gap. Academia
faces a reproducibility crisis. People publish papers that others can't
recreate, especially in fields such as neuroimaging
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].
A course sequence for this starts with Git and reproducible publications, then
moves into tests, open source contribution, and packaging. Environments and
requirements files come next.

Johanna Bayer describes what students practice. Students need packaging and
environments, plus formatting and tests instead of only a finished notebook. Her normative
brain-model example adds folder structure and Cookiecutter-style project layout
as part of the reproducibility habit
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia@27:38=>Core coding practices]]
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia@38:50=>Project structure case study]].

The same gap appears in data science education. Labs often lack training for
long-lived data management, collaboration, and complete reproduction of code.
DVC work at Iterative and later teaching help applied data science students make
project-management choices. Those choices matter before they enter industry
[[cite:devrel-data-science-open-source-tools=>DevRel for Data Science]].

The research-to-production bridge matters too. Researchers use notebooks,
benchmarks, and tools such as Weights & Biases to validate hypotheses. That
contrasts with the ML engineer's responsibility for deployment, uptime, and
monitoring. It also includes Docker, cloud infrastructure, and web services.
Reproducibility
improves when researchers learn engineering fundamentals and engineers learn how
to reproduce models and track experiments
[[cite:research-to-production-ml-systems-roadmap=>From Research to Production]].

In space-resource research, Daynan Crull framed notebooks as useful for telling
the story of data. He said he doesn't develop in them because they can teach bad
developer habits. Teams can treat notebooks as narrative evidence, then move
reviewable work into regular code
[[cite:machine-learning-for-asteroid-mining-and-water-detection@1:00:11=>Asteroid Mining and Water Detection]].

## Data Pipelines

Pipeline reproducibility starts with stable inputs, and immutable raw data is the
foundation. Teams should transform immutable datasets into new datasets rather
than mutate tables in place. They should add workflow orchestration so pipelines
have explicit dependencies and late data, transient failures, and bugs can be
retried and repaired
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

From the delivery path, practical steps include version control, automated
tests, and development tests. They also include deployment automation and error
tracking. Beyond unit tests, data teams should run the system end to end against
realistic test data. They should keep tests close to the code and run checks in
development and production
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

Infrastructure belongs in the same reproducibility conversation. Infrastructure
as code keeps environments reproducible when Terraform, Terragrunt, and Atlantis
are paired with merge requests. Review and dry runs make that path safer. In one
dependency example, an unspecified Python package version caused a Dockerized
application to fail after it fetched a newer API. Pinning versions isn't
ceremony there because it prevents a future run from silently becoming a
different run
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].

## MLOps and Platforms

ML reproducibility extends the pipeline record with experiment and artifact
history. Experiment tracking is an early win for collaboration. The tracked run
sits near the model registry because a useful run may become an artifact that
downstream systems consume
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

The record expands from there. A platform may need to store which job image ran,
which inputs it consumed, which outputs it wrote, and how metadata connects
across pipeline runs. The model registry alone isn't enough to reproduce a model
result from three years ago. Code versions, data versions, metadata, and
workflow design all matter.

This becomes an adoption sequence that groups CI, repository structure, and
parameterization with testing and experiment preservation. It starts from a real
pain point. Examples include CI/CD when deployment takes months, monitoring when
models are opaque in production, and missing version control that escalates
immediately
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Teams should add experiment tracking and model registries when they remove a
concrete delivery risk. The same applies to serving, monitoring, package
registries, and containers.

## Data Boundaries and Governance

Reproducibility can conflict with privacy, cost, and governance. In research,
sensitive consortium data can't simply be pushed to a repository. Model
parameters and metadata may still be shareable
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].

On a platform, metadata logging differs from copying the full dataset artifact.
Copying a 50 GB training dataset for every run can create cost problems. It can
also create GDPR deletion problems because the team may need to remove one
person's data across many duplicated artifacts
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

Lakes raise a similar point: raw dumps and history help teams reproduce past
states, but personal data requires separation and governance. Full database
dumps preserve more history than mutable tables, yet they also require clear
handling for GDPR and change capture
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

## Risk-Based Capture

Reproducibility works as a risk-based capture set rather than one universal tool
stack.

- Code and workflow definitions, including reports, transformations, model
  code, infrastructure code, and orchestration dependencies
  [[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]],
  [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].
- Inputs or input references. Teams may use immutable raw data, versioned
  datasets, query metadata, or controlled-access data depending on privacy and
  scale
  [[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
- Environment and dependency records, including package versions, Docker
  images, requirements files, and package registries
  [[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]],
  [[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
- Run metadata, experiment logs, parameters, metrics, and model registry
  entries
  [[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]],
  [[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
- Tests and checks, including data transformation tests, end-to-end tests,
  production data quality checks, and development regression checks
  [[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]],
  [[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
- Governance and downstream artifacts, including model outputs,
  visualizations, catalogs, and data governance changes when those artifacts
  change together
  [[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

Use the capture set only when it matches the risk. A tutorial project can use a
small, fully bundled dataset. A bank model, clinical dataset, or
customer-facing fraud decision may need stricter metadata and lineage. It may
also need stricter approval, deletion, and audit paths.

## Related Pages

These pages connect reproducibility to the platform, pipeline, governance, and
software practices that preserve rerunnable work.

- [[MLOps]]
- [[DataOps]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[ML Platforms]]
- [[Data Lake]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[ci-cd=>CI/CD]]
- [[Testing]]
- [[Software Engineering]]
