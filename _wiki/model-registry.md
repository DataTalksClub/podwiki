---
layout: wiki
title: "Model Registry"
summary: "A bridge page for podcast evidence about model artifact storage and handoff."
related:
  - MLOps
  - ML Platforms
  - Experiment Tracking
  - Model Monitoring
---

## Definition and Scope

A model registry is the system or convention that stores model artifacts and
their operational context so another job, service, or team can use them. In the
archive, a registry isn't just a folder of pickles. It sits near experiment
tracking, metadata stores, deployment workflows, and approvals. It also sits
near lineage and monitoring.

Use this page when the archive evidence is about model artifact handoff,
versioning, stages, and approvals. It also fits reproducibility and downstream
consumption. Use [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
for run capture before a model is promoted.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive uses registries as lifecycle glue:

- Registries turn training output into a reusable production artifact. Simon
  Stiebellehner places model registries after experiment tracking and before
  serving decisions such as batch inference or online serving.
- Registries usually come with tracking and metadata tooling. The platform
  episode mentions MLflow, Weights & Biases, SageMaker, and cloud tools, which
  may bundle tracking with registry features.
- A registry alone doesn't make a run reproducible. Teams also need the code
  version, input data reference, job image, parameters, outputs, and lineage.
- Governance and retention matter. If teams store datasets or metadata with
  model runs, privacy and deletion rules can turn a simple registry into a
  compliance concern.
- Registries support monitoring and analytics when deployment logs include a
  model version and a common prediction schema.

## Episode Evidence

These episodes connect registries to handoff and reproducibility:

- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 30:32, Simon discusses persisting models for downstream consumption. At
  42:48-45:50, he connects the registry to metadata, lineage, and code
  versions. At 54:15-55:29, the discussion connects model serving to unified
  prediction logs for monitoring and analytics. Reuse the
  [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 51:21, Raphaël
  includes registries in the core MLOps toolset with tracking, serving, and
  monitoring. He also names compute, container registries, and package
  registries. At 53:08-56:50, he adds dependency packaging and containers as
  registry-adjacent reproducibility concerns. Reuse the
  [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [MLOps Roadmap](https://datatalks.club/podcast.html): The archive synthesis
  treats a registry as the stage where teams record owner, training data
  reference, evaluation metric, and approval status. Deployment targets and
  rollback notes also belong there. See [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}).
- [MLOps in Finance](https://datatalks.club/podcast.html): Add regulated ML
  evidence here when it discusses model validation, approval, audit trails, or
  controlled deployment.

## Related Pages

Use these pages for adjacent lifecycle topics.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/mlops-and-ml-engineering-in-finance.md`
- `../datatalksclub.github.io/_podcast/pragmatic-and-standardized-mlops.md`

Add evidence only when the source mentions model artifacts, promotion,
versioning, or metadata. Approvals, lineage, deployment handoff, and
model-versioned logs also fit. Generic "MLOps uses registries" mentions belong
on [MLOps]({{ '/wiki/mlops/' | relative_url }}).
