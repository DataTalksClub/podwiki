---
layout: wiki
title: "MLOps"
summary: "Podcast-grounded reference page for MLOps as the operating discipline for production machine learning systems."
related:
  - ML Platforms
  - Machine Learning System Design
  - Model Registry
  - Model Monitoring
  - Experiment Tracking
  - Reproducibility
  - Production
  - DataOps
---

MLOps is the operating discipline for machine learning systems after they leave
experimentation. It covers reproducible training, model artifacts, deployment,
serving, monitoring, retraining, governance, and ownership. Use
[DataOps]({{ '/wiki/dataops/' | relative_url }}) for the separate discipline
around data pipelines and analytical delivery. Use
[MLOps vs DataOps]({{ '/articles/mlops-vs-dataops/' | relative_url }}) for the
comparison.

## Link Map

Related wiki pages:
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}).

Core podcast interviews:
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
[Pragmatic MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
[MLOps Architect Guide](https://datatalks.club/podcast/mlops-model-monitoring-data-observability.html),
[Human-Centered MLOps](https://datatalks.club/podcast/human-centered-mlops-and-model-monitoring.html),
[MLOps in Finance](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html), and
[Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html).

## Common Definition

Across the archive, MLOps means the repeatable path from model development to a
maintained production system. In
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
the discussion centers on CI/CD, repository structure, parameterization,
reproducibility, monitoring, and adoption by product teams. In
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
MLOps is framed through people, process, and technology: experiment tracking,
model registries, batch and online serving, orchestration, metadata, lineage,
governance, and developer experience.

The common thread is ownership after training. MLOps does not stop when a
notebook produces a good metric. It asks whether another person can reproduce
the run, approve the artifact, deploy it, monitor it, roll it back, and decide
when to retrain or retire it.

## Where Guests Differ

Guests differ on how much platform to build and how early to build it. In
[Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html),
the emphasis is minimal operational discipline for small teams: ship useful
models without building a heavy platform too soon. In
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
the platform layer becomes more important when multiple teams repeat the same
training, deployment, registry, and monitoring work.

Guests also differ on tooling emphasis. In
[Pragmatic MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
Maria Vechtomova stresses standard engineering primitives such as Git, CI/CD,
registries, Kubernetes, reusable repositories, and monitoring. In
[Human-Centered MLOps](https://datatalks.club/podcast/human-centered-mlops-and-model-monitoring.html),
the emphasis shifts toward business cases, stakeholder buy-in, monitoring, and
incident response. Both views agree that tools are not the strategy.

## Model Lifecycle

MLOps begins when a model must become a maintained system. The lifecycle
includes tracked experiments, model artifacts, approval, deployment, serving,
monitoring, feedback, and retraining decisions. The
[Model Registry]({{ '/wiki/model-registry/' | relative_url }}) and
[Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) pages
cover the handoff from training to production.

[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)
separates batch inference from online serving and ties both to orchestration,
metadata, lineage, and governance. That distinction matters because a daily
batch scoring job, a low-latency API, and a managed endpoint have different
failure modes.

## Monitoring and Feedback

MLOps monitoring covers model behavior, service behavior, and the data around
the model. [MLOps Architect Guide](https://datatalks.club/podcast/mlops-model-monitoring-data-observability.html)
connects model monitoring to upstream ETL, data pipelines, and observability.
A model can degrade because features shifted, labels arrived late, a schema
changed, or the serving path broke.

Use [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
model-specific layer. Use
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
when the root cause sits in the data pipeline rather than the model artifact.

## Governance and Risk

MLOps becomes stricter when models affect regulated decisions, finance,
healthcare, fraud, risk, or customer-facing workflows. In
[MLOps in Finance](https://datatalks.club/podcast/mlops-and-ml-engineering-in-finance.html),
deployment is tied to CI/CD, monitoring, governance, validation, and risk
controls. Those requirements make approval history, lineage, model versioning,
and rollback paths part of the system design.

This is where [Production]({{ '/wiki/production/' | relative_url }}),
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[Governance]({{ '/wiki/governance/' | relative_url }}) connect to MLOps. A team
needs to explain which model produced which output, with which data, under
which approval and monitoring path.

## Related Pages

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
