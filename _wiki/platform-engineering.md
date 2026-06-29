---
layout: wiki
title: "Platform Engineering"
summary: "A bridge page for podcast evidence about internal platform teams, self-service ML workflows, standards, support models, and developer experience."
related:
  - ML Platforms
  - Developer Experience
  - Machine Learning Infrastructure
  - MLOps
---

## Definition and Scope

Platform engineering is the work of building shared internal systems that help
product, data, and ML teams ship reliably without each team inventing its own
infrastructure. In the podcast archive, ML platform engineers work across cloud
infrastructure, MLOps, software engineering, and data science workflows. They
also borrow from internal product management.

Use this page when the evidence is about platform team design, standards, and
support models. It also fits internal customers and adoption. Use [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
for the platform surface and [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
for compute and orchestration details.

## Contents

Use these links to jump between the main parts.

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

The archive presents platform engineering as enablement:

- Platform teams reduce cognitive load. Simon Stiebellehner says platform work
  should streamline how teams develop, deploy, and serve ML products. Raphaël
  Hoogvliets describes a centralized team that helps embedded product teams with
  reusable tools, design documents, deployment, maintenance, and monitoring.
- The team needs a hybrid skill mix. Guests name cloud infrastructure,
  Kubernetes, Terraform, and software engineering. They also name data science
  workflow knowledge, SRE, data engineering, and translation skills.
- Adoption comes from product management habits. Teams need feedback, pain point
  discovery, quick wins, before-and-after evidence, and standards that leave
  enough room for data scientists to work.
- Build-versus-buy is rarely pure. Platform engineers often integrate managed
  tools, open-source components, and custom glue. The work is making them fit
  the company's workflows.
- Operational support changes team size because on-call needs and business
  criticality matter. Platform load and the number of consuming teams affect
  staffing more than a generic headcount rule.

## Episode Evidence

These episodes show platform engineering as internal enablement:

- [Building Production ML Platforms](https://datatalks.club/podcast.html):
  At 8:11-17:14, Simon describes platform engineering as reducing cognitive load
  for teams that ship ML products. He names cloud, Kubernetes, Terraform,
  workflow knowledge, mixed teams, and on-call considerations. At 47:08-51:15,
  he warns against building a large platform before teams have real use cases.
  Reuse the [summary]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [MLOps at Scale](https://datatalks.club/podcast.html): At 23:01-37:32,
  Raphaël describes a centralized enabling team, embedded product-team support,
  adoption through feedback, developer experience, and quick wins. At
  45:10-48:41, he names skills across data science, SRE, DevOps, platform
  engineering, and data engineering. Reuse the [summary]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- [DevRel Role for Machine Learning](https://datatalks.club/podcast.html):
  Hugo connects platform work to education, documentation, demos, and developer
  feedback. Reuse the [summary]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
- [MLOps Architect Guide](https://datatalks.club/podcast.html): Danny
  Leybzon's architect role shows a related bridge function for tooling choices,
  platform integrations, monitoring, and business cases.
- [Data Engineering Platforms](https://datatalks.club/podcast.html): Data
  platform episodes add the same repeated structure on the data side:
  self-service, conventions, contracts, monitoring, and ownership. See
  [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

## Related Pages

Use these pages for adjacent platform and MLOps topics.

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps vs DevOps]({{ '/wiki/mlops-vs-devops/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})

## Maintenance Notes

Use these source files when expanding this page:

- `../datatalksclub.github.io/_podcast/building-production-ml-platform-and-mlops-team.md`
- `../datatalksclub.github.io/_podcast/mlops-at-scale-reproducibility-adoption.md`
- `../datatalksclub.github.io/_podcast/devrel-open-source-machine-learning.md`
- `../datatalksclub.github.io/_podcast/mlops-model-monitoring-data-observability.md`
- `../datatalksclub.github.io/_podcast/scaling-data-engineering-teams-self-service-platforms.md`

Keep this page about team design and enablement. Put specific tooling details
on [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) or the narrower
tracking, registry, monitoring, and infrastructure pages.
