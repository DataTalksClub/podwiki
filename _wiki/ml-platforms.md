---
layout: wiki
title: "ML Platforms"
summary: "A bridge page for podcast evidence about shared ML platform systems and team enablement."
related:
  - MLOps
  - Platform Engineering
  - Machine Learning Infrastructure
  - Developer Experience
---

## Definition and Scope

An ML platform is the shared product surface that helps teams build and train
models. It also helps them deploy and govern models while avoiding repeated
plumbing. In the podcast archive, platform teams provide tracking, registries
and compute access. They also provide orchestration, deployment paths and
prediction logging. Monitoring and support practices fit here too.

Use this page for the platform layer. Use [MLOps]({{ '/wiki/mlops/' | relative_url }})
for the operating discipline and [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
for compute, containers, orchestration, and hardware constraints.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive treats ML platforms as internal products, not tool collections:

- Start with repeated team pain. Simon Stiebellehner describes platform work as
  useful when multiple teams train, serve, or deploy models in different ways
  without a good reason. Raphaël Hoogvliets makes the same point through pain
  point collection and quick wins.
- Build or buy selectively because guests rarely recommend building an
  end-to-end platform from scratch. They more often describe buying managed
  tools and wrapping them in team-specific conventions.
- Experiment tracking and registries are early wins because they preserve run
  history and model handoffs before teams invest in heavier serving or
  governance layers.
- Self-service is a developer-experience problem. Good platforms hide routine
  compute, deployment, and dependency work while still giving data scientists
  enough flexibility to experiment.
- Regulated teams need more than generic tooling. They need lineage, metadata,
  access control, auditability, and deletion rules.

## Episode Evidence

These episodes give the strongest platform evidence:

- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 4:42-17:14, Simon defines MLOps through people, process and technology.
  He frames a platform as a way to reduce cognitive load for product teams. At
  29:41-34:01, he covers tracking, registries, serving and orchestration.
  At 38:40-49:19, he discusses governance, metadata, lineage and thin
  abstractions, and explains when to delay heavy platform work.
  Reuse the [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 23:01-33:13,
  Raphaël describes a centralized enabling MLOps team that supports product
  teams with infrastructure and feedback. At 39:06-56:50, he covers CI,
  repository structure, testing and reproducibility. He also covers registries,
  serving, monitoring and dependency management. Reuse the
  [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [DevRel Role for Machine Learning](https://datatalks.club/podcast.html):
  Hugo Bowne-Anderson describes Metaflow as a human-centric tool for full-stack
  ML. The episode adds AWS, Kubernetes, Argo, and documentation around the
  workflow. Reuse the [summary]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
- [MLOps Architect Guide](https://datatalks.club/podcast.html): Danny Leybzon
  adds production-first monitoring, ETL root causes, build-versus-buy
  decisions, and platform-agnostic observability integrations.
- [Post-ChatGPT AI Infrastructure](https://datatalks.club/podcast.html):
  Andrey Cheptsov adds infrastructure pressure from AI workloads. The episode
  covers cost, cloud versus on-prem, distributed training, and Kubernetes
  limits.
- [Pragmatic and Standardized MLOps](https://datatalks.club/podcast.html):
  Reinforces the archive's preference for Git, CI/CD, Kubernetes, and
  registries before new platform layers.

## Related Pages

Use these pages for narrower lifecycle and infrastructure topics.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/pragmatic-and-standardized-mlops.md`
- `../datatalksclub.github.io/_podcast/mlops-model-monitoring-data-observability.md`
- `../datatalksclub.github.io/_podcast/devrel-open-source-machine-learning.md`
- `../datatalksclub.github.io/_podcast/ai-infrastructure-hybrid-cloud-on-prem-distributed-training.md`

Keep this page platform-wide, and move narrow model lifecycle details to the
tracking, registry, and monitoring pages. Move low-level compute details to
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).
