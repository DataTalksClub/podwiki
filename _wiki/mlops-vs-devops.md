---
layout: wiki
title: "MLOps vs DevOps"
summary: "A podcast-backed comparison of software delivery operations and the extra model, data, experiment, and monitoring concerns introduced by machine learning systems."
related:
  - MLOps
  - MLOps and DataOps
  - Software Engineering
  - Production
---

## Definition and Scope

DevOps is the operating discipline for shipping and running software systems:
version control, CI/CD, infrastructure automation, observability, incident
response, and fast recovery. MLOps inherits much of that discipline, then adds
machine learning concerns: data versioning, experiment tracking, model
registries, feature pipelines, model deployment, drift monitoring, retraining,
and governance.

The podcast archive does not present MLOps as a rejection of DevOps. It treats
MLOps as a specialized extension of software and platform engineering for systems
whose behavior depends on data and model artifacts as well as code.

## Contents

- [Comparison](#comparison)
- [What MLOps Borrows From DevOps](#what-mlops-borrows-from-devops)
- [What MLOps Adds](#what-mlops-adds)
- [When Each Side Matters](#when-each-side-matters)
- [Podcast Evidence](#podcast-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Comparison

| Question | DevOps | MLOps |
| --- | --- | --- |
| Primary artifact | Application code, services, infrastructure definitions, containers, packages. | Code plus datasets, features, parameters, experiments, model artifacts, registries, and evaluation records. |
| Main lifecycle | Build, test, deploy, observe, recover, iterate. | Explore, train, evaluate, register, deploy, monitor data and model behavior, retrain, govern. |
| Monitoring focus | Availability, latency, errors, saturation, logs, traces, service health. | Service health plus data quality, feature drift, prediction drift, model performance, fairness, and feedback loops. |
| Reproducibility problem | Rebuild the same service from code and dependencies. | Rebuild the same model from code, data, parameters, environment, feature logic, and training context. |
| Organizational pattern | Platform, SRE, infrastructure, and product engineering teams. | ML platform, MLOps, ML engineering, data science, data engineering, and product teams. |

## What MLOps Borrows From DevOps

MLOps guests repeatedly recommend familiar engineering primitives before new tool
shopping. Git, CI/CD, standardized repositories, tests, package registries,
containers, Kubernetes, infrastructure-as-code, monitoring, and on-call practices
all show up in the archive. These practices reduce the fear of deployment and
make repeated releases possible.

This is why the archive's MLOps guidance often sounds like software engineering:
move logic out of notebooks when it needs to run repeatedly, package code,
version dependencies, create deployment paths, and make failures observable.

## What MLOps Adds

### Models are not only code

A model is an artifact produced by code, data, parameters, features, and training
state. Reproducibility therefore needs experiment capture, data traceability,
artifact storage, and model registry practices. A code commit alone is usually
not enough to explain why a model behaves a certain way.

### Data changes after deployment

Production software can fail because code changed. ML systems can also fail
because input distributions, upstream schemas, feature pipelines, labels, or
user behavior changed. Monitoring has to look upstream, not only at serving
infrastructure.

### The path starts in exploration

Data scientists often begin in notebooks, experiments, and informal feature
logic. MLOps needs to preserve useful exploratory knowledge while turning the
work into repeatable jobs, services, and deployment workflows.

### Governance can be model-specific

Regulated ML systems may need lineage, approval workflows, model validation,
explainability, audit records, retention rules, and controlled retraining. DevOps
practices help, but they do not by themselves answer whether the model is still
valid for the business or risk context.

## When Each Side Matters

Use DevOps framing when the main problem is service delivery: CI/CD, cloud
infrastructure, containers, deployment safety, observability, incident response,
permissions, or platform reliability.

Use MLOps framing when the system includes learned behavior whose quality depends
on data and model lifecycle: training, feature pipelines, model artifacts,
registries, batch or online inference, drift, retraining, evaluation, or model
governance.

Most production ML work needs both. The practical archive pattern is to reuse
DevOps foundations, then add the ML-specific lifecycle pieces where the model
creates new risk.

## Podcast Evidence

| Episode | Evidence |
| --- | --- |
| [Building Production ML Platforms](https://datatalks.club/podcast.html) | At 4:42-6:55, MLOps is defined as people, processes, and technology, not only tooling. At 8:11-13:50, platform skills include cloud infrastructure, Kubernetes, Terraform, and software engineering fundamentals. |
| [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html) | At 11:10-14:45, MLOps is framed as enablement and standardized infrastructure for data scientists. At 16:27-20:49, the guest recommends existing infrastructure such as Kubernetes, Git, CI/CD, registries, deployment paths, and monitoring. |
| [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html) | At 35:21-38:01, the episode covers DevOps buy-in, standards, permissions, and internal audit as organizational dependencies for MLOps. |
| [MLOps at Scale](https://datatalks.club/podcast.html) | At 39:06-44:22, core practices include CI, repository structure, parameterization, testing, data versioning, traceability, and experiment capture. |
| [MLOps Architect Guide](https://datatalks.club/podcast.html) | At 25:04-31:50, production-first monitoring, ETL root causes, data pipelines, and the shift from "why monitor" to "how to monitor" distinguish ML operations from generic service monitoring. |
| [DataOps for Data Engineering](https://datatalks.club/podcast.html) | Provides the data-side analog: automation, CI/CD, observability, realistic test data, and recovery practices for pipelines and analytics workflows. |

## Related Pages

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
- [Software Engineering]({{ '/wiki/software-engineering/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})

## Maintenance Notes

- Highest-value source files:
  `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`,
  `../datatalksclub.github.io/_podcast/pragmatic-and-standardized-mlops.md`,
  `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`,
  `../datatalksclub.github.io/_podcast/mlops-model-monitoring-data-observability.md`,
  and `../datatalksclub.github.io/_podcast/dataops-and-gitops-best-practices-for-data-teams.md`.
- Avoid making this a generic DevOps explainer. Add DevOps material only when it
  clarifies what MLOps borrows or extends.
- Future improvement: add a compact evidence table for SRE/on-call patterns
  when more archive clips discuss incident response around model systems.
