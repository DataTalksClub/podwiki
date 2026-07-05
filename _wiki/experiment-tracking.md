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
path. Production platforms usually place experiment trackers before registries
and serving. Orchestration and governance round out the later path
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

Experiment tracking for ML and AI work centers on run capture and
reproducibility. It also preserves team memory and connects runs to the wider
platform. It doesn't cover general product
[[a-b-testing=>A/B testing]] or broader
[[experimentation]]. For adjacent
topics, use
[[Evaluation]] for judging runs and
[[Model Monitoring]] for deployed
behavior. Use [[Reproducibility]]
for the wider recovery problem across code, data, environments, and outputs.

## Shared Run History

Experiment tracking moves run history out of private memory. It turns local
notebooks and ad hoc spreadsheets into a shared record. It also captures
one-off terminal output that other people can look at later
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
Teams that evaluate models with metrics need a transparent way to compare runs
and outputs.

That definition is practical rather than tool-branded. The tracker is useful
because it records enough context to compare experiments and reproduce later
work. In the platform sequence, teams explore data and train models, then
evaluate runs. Candidate artifacts move into a
[[model registry]] before teams choose batch
or online serving
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].
That's why experiment tracking belongs with
[[ML Platforms]],
[[MLOps Tools]], and
[[Machine Learning System Design]],
not only with notebook hygiene.

Exploration contains knowledge that can help later monitoring and root-cause
analysis, so original model work shouldn't disappear on a departed employee's
laptop [[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
Reproducibility ties into traceability, data versioning, and legal context, and
sector requirements determine how heavy the practice must become.

## Adoption Timing

Teams differ on when tracking should become the first MLOps move. One platform
sequence starts with experiment tracking. It gives teams a quick reproducibility
and collaboration win before the full release path. Teams can use tracking as a
low-friction platform entry point. They can compare runs and recover context
without redesigning serving, monitoring, or governance first
[[cite:building-production-ml-platform-and-mlops-team@29:41=>Early Experiment Tracking]].

Tracking helps teams move from personal spreadsheets to a shared and
transparent run history. That can help one team before a company needs a full
ML platform. It's especially useful when the team already evaluates models
with repeatable metrics
[[cite:building-production-ml-platform-and-mlops-team@29:41=>Early Experiment Tracking]].

Another sequence starts from team pain points instead of a fixed tool order. A
team might begin with CI/CD, deployment, monitoring, or another visible
bottleneck. Experiment capture can then become part of the operating system for
ML
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Academic research shifts the emphasis again. Reproducible work may combine Git
with environment management, formatting, versioning, and MLflow. Sensitive
clinical data can't simply be pushed to a repository. Metadata, parameters, and
project structure may be shareable even when raw data isn't
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].

[[metaflow=>Metaflow]] interoperates with experiment trackers such as Weights &
Biases and Comet
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Naming a tracker isn't the hard part. The hard work is fitting the tracker
into the data science workflow and the surrounding platform
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

## Run Records

A compact run record beats a generic dashboard wishlist. A useful tracked run
preserves enough model-development context for a teammate or future maintainer
to understand what happened. It can include job images and persistent metadata.
It can also record consumed inputs, written outputs, and connected pipeline runs
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

Exploratory context often gets lost when teams clean up code for deployment.
Visualizations, data checks, and early analysis still help with later monitoring
and root-cause work. Teams still need to separate exploratory notebooks from
production code
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]. That links
experiment tracking to
[[Developer Experience]]:
the system is valuable only if data scientists can use it without bypassing it.

## Data and Governance

Experiment tracking needs data context, but no universal storage rule.

Some tools log only a query or pointer, while others copy the data artifact
[[cite:building-production-ml-platform-and-mlops-team@44:05=>Experiment Data Tracking]].

Copying datasets for every run is risky because the cost can grow and
personal-data deletion can become harder
[[cite:building-production-ml-platform-and-mlops-team@45:50=>GDPR and Dataset Copies]].

Academic open science reaches the same boundary. Neuroimaging work uses
sensitive consortium data, so the reproducible record has to respect access
controls. Parameters, metadata, and project structure travel more easily than
raw clinical data
[[cite:teaching-reproducible-research-and-open-science-coding-practices-for-academia=>Teaching Open Science and Reproducible Research]].
For navigation, this puts experiment tracking near
[[Governance]],
[[Data Governance]], and
[[Responsible AI and Governance]].

## From Experiments to Production

Experiment tracking is most useful before a model is promoted. It becomes more
valuable when connected to the production path. Experiment trackers, model
registries, and metadata stores link together. Metadata and code versions
support reproducing an old model result, with data versions and workflow design
mattering too
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

Experiment tracking sits inside broader MLOps tooling, which includes version
control and CI/CD. It also sits near containers, registries, serving, and
monitoring
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Maturity signals include version control and CI/CD. Other signals include
registries, documentation, reproducibility, and traceability.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]
Tracking doesn't replace testing and packaging. It doesn't replace deployment or
[[production]] monitoring either. It gives those later steps a recoverable
model-history record.

## Tool Choice and Integration

Teams use tools such as MLflow, Weights & Biases, and Comet. They may also use
Neptune or SageMaker. Choosing a tracker by brand alone is the wrong approach.
Most teams should integrate an existing tracker rather than build one from
scratch. The tracker has to fit the data science workflow, data constraints,
and surrounding infrastructure
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

Trackers often arrive bundled with registries and metadata stores. That package
can be useful, but the team still has to decide which data context to log. It
also has to decide which artifacts to persist and how the tracker connects to
the handoff into deployment
[[cite:building-production-ml-platform-and-mlops-team@30:32=>Building Production ML Platforms]].

[[metaflow=>Metaflow]] gives the same ML ecosystem lesson. Workflow tools,
compute backends, and experiment trackers need to interoperate. Practitioners
can then move from local work to reproducible runs without changing every habit
in one step
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].

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
