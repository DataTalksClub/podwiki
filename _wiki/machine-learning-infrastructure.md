---
layout: wiki
title: "Machine Learning Infrastructure"
summary: "A bridge page for podcast evidence about compute, containers, orchestration, cloud, on-prem, GPUs, dependency management, and serving foundations for ML and AI systems."
related:
  - ML Platforms
  - Platform Engineering
  - AI Infrastructure
  - MLOps
---

## Definition and Scope

Machine learning infrastructure is the compute, storage, networking,
orchestration, packaging, and serving foundation that lets teams train and run
models. In the podcast archive, teams discuss cloud services, Kubernetes,
Terraform, Docker, package registries, and notebooks with managed compute. They
also discuss batch jobs, online serving, GPUs, distributed training, and cloud
versus on-prem tradeoffs.

Use this page for the infrastructure layer below [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}).
Use [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) for the
broader AI and LLM infrastructure hub when that page is expanded.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive makes infrastructure practical rather than decorative:

- Infrastructure work starts with cost, access, and reliability. Andrey
  Cheptsov frames AI infrastructure around cloud cost, on-prem utilization,
  ownership, and the cost of running large workloads.
- Kubernetes is both standard and incomplete. Guests treat Kubernetes as a
  common deployment base, but AI workflows may need GPU-aware orchestration,
  training abstractions, and tools beyond general container scheduling.
- Platform engineers need cloud and infrastructure skills. Simon
  Stiebellehner names AWS, GCP, Azure, Kubernetes, and Terraform. He also names
  notebooks, managed compute, orchestration, and serving paths.
- Packaging and dependency management are infrastructure too. Raphaël
  Hoogvliets discusses package registries, Docker images, version ranges, and
  deployment compatibility as reproducibility concerns.
- Batch and online serving have different infrastructure shapes. The platform
  episode warns that some vendor platforms call a temporary endpoint "batch",
  which may not fit large batch inference needs.

## Episode Evidence

These episodes give the strongest infrastructure evidence:

- [Post-ChatGPT AI Infrastructure](https://datatalks.club/podcast.html): At
  5:27-10:00, Andrey discusses cloud versus on-prem cost, Terraform,
  Kubernetes, Docker, and cost of ownership. At 30:16-36:00, he covers GPU
  requirements, distributed training, PyTorch, NCCL, and communication
  bottlenecks. At 44:33-51:16, he discusses Kubernetes as a foundational
  deployment tool and its limits for AI workflows.
- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 8:11-13:25, Simon names cloud infrastructure, Kubernetes, Terraform, AWS
  services, notebooks, and data science workflow knowledge. At 28:20-34:01, he
  covers managed compute, batch versus online serving, and orchestration. Reuse
  the [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 53:08-56:50,
  Raphaël discusses package registries, dependency compatibility, Docker,
  Kubernetes, Databricks, and whether containerized components make teams more
  autonomous or add complexity. Reuse the [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [DevRel Role for Machine Learning](https://datatalks.club/podcast.html):
  Hugo describes full-stack ML infrastructure as something scientists shouldn't
  have to configure from scratch. Metaflow integrates AWS, Kubernetes, Argo, and
  production workflows. Reuse the [summary]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
- [From Notebooks to Production](https://datatalks.club/podcast.html): Adds
  practical pipeline infrastructure: Dockerized training, model storage,
  inference strategies, scheduling, and simple orchestration before heavier
  systems.

## Related Pages

Use these pages for adjacent infrastructure and operating topics.

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps vs DevOps]({{ '/wiki/mlops-vs-devops/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/ai-infrastructure-hybrid-cloud-on-prem-distributed-training.md`
- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/devrel-open-source-machine-learning.md`
- `../datatalksclub.github.io/_podcast/s24e03-from-notebook-to-production-building-end-to-end-ai-systems.md`

Keep this page focused on infrastructure constraints and primitives. Put team
adoption on [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
and lifecycle practices on [MLOps]({{ '/wiki/mlops/' | relative_url }}).
