---
layout: wiki
title: "Experiment Tracking"
summary: "Experiment tracking as run history, reproducibility practice, and ML platform capability."
related:
  - MLOps
  - ML Platforms
  - MLOps Tools
  - Model Registry
  - Model Monitoring
  - Reproducibility
  - Developer Experience
  - Governance
---

Experiment tracking records machine-learning and AI model development runs. The
record helps a team compare results, understand how a model was produced, and
recover the context behind a promising or failed experiment. A tracked run
usually includes code version, parameters, metrics, and artifacts. It can also
include environment details, data references, and notes about the modeling
decision.

Experiment tracking sits between exploratory
[[machine learning]] work and
production [[MLOps]]. It isn't the same as a
[[model registry]], but the two
often appear together because a useful run eventually needs an artifact handoff
path. On a production platform, experiment trackers come before registries,
serving, orchestration, and governance
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Experiment tracking for ML and AI work centers on run capture and
reproducibility. It also preserves team memory and connects runs to the wider
platform. It doesn't cover general product
[[a-b-testing|A/B testing]] or broader
[[experimentation]]. For adjacent
topics, use
[[Evaluation]] for judging runs and
[[Model Monitoring]] for deployed
behavior. Use [[Reproducibility]]
for the wider recovery problem across code, data, environments, and outputs.

## Shared Run History

Experiment tracking moves run history out of private memory. It turns local
notebooks and ad hoc spreadsheets into a shared record, and it captures one-off
terminal output that other people can look at later
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Teams that evaluate models with metrics need a transparent way to compare runs
and outputs.

That definition is practical rather than tool-branded. The tracker is useful
because it records enough context to compare experiments and reproduce later
work. In the platform sequence, teams explore data and train models, evaluate
runs, persist candidate artifacts in a
[[model registry]], and choose batch
or online serving
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
That's why experiment tracking belongs with
[[ML Platforms]],
[[MLOps Tools]], and
[[Machine Learning System Design]],
not only with notebook hygiene.

Exploration contains knowledge that can help later monitoring and root-cause
analysis, so original model work shouldn't disappear on a departed employee's
laptop ([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Reproducibility ties into traceability, data versioning, and legal context, and
sector requirements determine how heavy the practice must become.

## Adoption Timing

Guests differ on when teams should add tracking.
[[person:simonstiebellehner|Simon Stiebellehner]] starts early, because tracking
gives teams a quick reproducibility and collaboration win before the full
release path
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

[[person:raphaelhoogvliets|Raphael Hoogvliets]] starts from team pain points
instead of a fixed tool sequence: the first MLOps move depends on the
organization
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). A team
might start with CI/CD, deployment, monitoring, or another visible bottleneck,
then add experiment capture as part of the operating system for ML.

[[person:johannabayer|Johanna Bayer]] gives the research version: a stack of
Git, environments, formatting, versioning, and MLflow
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).
The project uses sensitive clinical data that can't simply be pushed to a
repository, so metadata, parameters, and project structure may be shareable even
when raw data isn't.

Metaflow interoperates with experiment trackers such as Weights & Biases and
Comet
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).
The hard work isn't naming a tracker; it's fitting the tracker into the data
science workflow and the surrounding platform
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

## Run Records

A compact run record beats a generic dashboard wishlist. A useful tracked run
preserves enough model-development context for a teammate or future maintainer
to understand what happened: job images, consumed inputs, written outputs,
persistent metadata, and connected pipeline runs
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Exploratory context often gets lost when teams clean up code for deployment,
yet visualizations, data checks, and early analysis help with later monitoring
and root-cause work, so teams still need to separate exploratory notebooks from
production code
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]). That links
experiment tracking to
[[Developer Experience]]:
the system is valuable only if data scientists can use it without bypassing it.

## Data and Governance

Experiment tracking needs data context, but no universal storage rule.

Some tools log only a query or pointer, while others copy the data artifact
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Copying datasets for every run is risky because the cost can grow and
personal-data deletion can become harder
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Academic open science reaches the same boundary. Neuroimaging work uses
sensitive consortium data, so the reproducible record has to respect access
controls, and parameters, metadata, and project structure travel more easily
than raw clinical data
([[podcast:teaching-reproducible-research-and-open-science-coding-practices-for-academia|Teaching Open Science and Reproducible Research]]).
For navigation, this puts experiment tracking near
[[Governance]],
[[Data Governance]], and
[[Responsible AI and Governance]].

## From Experiments to Production

Experiment tracking is most useful before a model is promoted, and it becomes
more valuable when connected to the production path. Experiment trackers, model
registries, and metadata stores link together, and stored metadata and code
versions support reproducing an old model result, with data versions and process
design mattering too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Experiment tracking sits inside broader MLOps tooling, near version control,
CI/CD, containers, registries, serving, and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
[[person:mariavechtomova|Maria Vechtomova]] makes a related standardization point
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

Version control, CI/CD, registries, documentation, reproducibility, and
traceability all serve as maturity signals
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]). Tracking doesn't
replace testing, packaging, deployment, or [[production]] monitoring, but it
gives those later steps a recoverable model-history record.

## Tool Choice and Integration

The common tools include MLflow, Weights & Biases, Comet, Neptune, and
SageMaker. Choosing a tracker by brand alone is the wrong approach; most teams
should integrate an existing tracker rather than build one from scratch, fitting
it to the data science workflow, data constraints, and surrounding
infrastructure
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Metaflow makes the same point from an ML ecosystem focus: workflow tools,
compute backends, and experiment trackers need to interoperate, letting
practitioners move from local work to reproducible runs without changing every
habit in one step
([[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]).

Teams therefore need to ask what record they need, not which tracker is
fashionable. That record should connect to code and data. It should also
connect to artifacts, serving, monitoring, and governance.

## Related Pages

These pages cover the surrounding lifecycle, platform, and operating decisions.

- [[MLOps]] - operational practices around reproducible training, deployment, monitoring, and ownership.
- [[ML Platforms]] - shared infrastructure for tracking, registries, serving, and governance.
- [[MLOps Tools]] - the surrounding tool categories for tracking, registries, orchestration, monitoring, and deployment.
- [[Model Registry]] - the artifact handoff after a tracked run becomes a candidate.
- [[Model Monitoring]] - production feedback that depends on model versions and run context.
- [[Reproducibility]] - recoverable code, data, environments, and outputs.
- [[Developer Experience]] - adoption of the tracking workflow by data scientists and ML engineers.
- [[Governance]] - audit, lineage, retention, and compliance boundaries.
