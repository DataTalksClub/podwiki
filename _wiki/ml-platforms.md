---
layout: wiki
title: "ML Platforms"
summary: "Podcast-grounded reference page for shared ML platform systems, internal product strategy, and team enablement."
related:
  - MLOps
  - Platform Engineering
  - Machine Learning Infrastructure
  - Developer Experience
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Reproducibility
---

An ML platform is the shared internal product for teams that train and deploy
models. It helps them monitor and govern those models without rebuilding the
same plumbing in every project. In the podcast archive, the platform layer sits
between
[MLOps]({{ '/wiki/mlops/' | relative_url }}) as an operating discipline and
[Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
as the compute and orchestration foundation.

The archive's strongest platform discussions treat platforms as adoption
systems, not tool catalogs. [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
connects platforms to repeated deployment work, registries, metadata, and
governance in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) adds the product
management view in
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }}).
His platform users are internal data scientists, ML engineers, and
stakeholders. Adoption, quality gates, and release paths decide whether that
platform works.

## Link Map

These wiki pages cover the closest neighbors:

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
  [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
  cover operating discipline and team ownership.
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}) and
  [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
  cover compute, orchestration, and GPU constraints.
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) and
  [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
  cover the internal-user side of the platform.
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
  [Model Registry]({{ '/wiki/model-registry/' | relative_url }}), and
  [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
  cover core lifecycle services.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) and
  [Governance]({{ '/wiki/governance/' | relative_url }}) cover auditability
  and control.

These podcast interviews anchor the page:

- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
  covers platform scope, early wins, governance, and developer experience.
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  with [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
  covers enabling teams and adoption alongside CI/CD, reproducibility, and
  monitoring.
- [ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
  with [Geo Jolly]({{ '/people/geojolly/' | relative_url }}) covers roadmap
  choices, rollout governance, and internal platform usability.
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
  with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
  covers Git, CI/CD, registries, and standard platform guardrails.
- [Scaling Enterprise AI]({{ '/podcasts/scaling-enterprise-ai-mlops-data-first-strategy/' | relative_url }})
  with [Alexander Hendorf]({{ '/people/alexanderhendorf/' | relative_url }})
  covers enterprise readiness, data-first strategy, and long-term platform
  selection.
- [Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})
  with [Andrey Cheptsov]({{ '/people/andreycheptsov/' | relative_url }})
  covers cloud cost, on-prem GPUs, distributed training, and orchestration
  limits.

## Common Definition

Across the archive, an ML platform is the reusable path from experiment to
production. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
Simon starts from self-service compute and experiment tracking. He then moves
to [model registries]({{ '/wiki/model-registry/' | relative_url }}) and serving.
He also covers orchestration, metadata, lineage, and governance.

In
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Raphaël describes the same idea through a centralized enabling team. That team
supports product teams with CI and repository standards.

Raphaël's team also covers tests and reproducibility, then completes the
operating path with serving, monitoring, and feedback loops.

The shared definition is narrower than "all ML tools" and broader than
"Kubernetes for models." [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
puts Git, CI/CD, registries, and reusable repositories at the center.
[Scaling Enterprise AI]({{ '/podcasts/scaling-enterprise-ai-mlops-data-first-strategy/' | relative_url }})
adds data-first readiness and governance.
[Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})
adds GPU economics and distributed-training constraints.

## Disagreements and Boundaries

Guests differ on timing, scope, and infrastructure depth. Simon Stiebellehner
argues for platform investment when repeated training and serving problems show
up across teams. Deployment and governance problems can create the same need.
He also warns against heavy platform work before teams have real models and
business needs
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Raphaël Hoogvliets emphasizes an enabling team that earns adoption by collecting
pain points and delivering quick wins. He also measures deployment frequency
and impact
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

They also differ on how productized the platform function should be. Geo Jolly
frames the ML platform as an internal product. His episode covers roadmap
tradeoffs and user research. It also covers rollout governance, adoption
metrics, and platform usability costs
([ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Maria Vechtomova is more skeptical of chasing new platform layers. She
emphasizes Git, CI/CD, registries, and Kubernetes. She also covers
cookie-cutter repositories and service principals
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

Infrastructure guests draw the boundary differently again. Andrey Cheptsov
treats orchestration and cloud economics as platform design constraints. He
adds GPU allocation, distributed training, and Kubernetes limits
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})).
That view makes the platform closer to
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) when the
workload is large-model training or serving. Smaller product ML teams may stay
closer to [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}).

## Internal Product and Adoption

The archive repeatedly frames ML platforms as internal products, and Geo
Jolly's episode is the clearest product-management version. Platform work
starts with internal users, ROI, adoption, and specs. Roadmap choices and rollout
governance come next, and quality gates matter more than a generic tool
wishlist
([ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

That connects ML platforms to
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }}).
The platform succeeds only when teams can use it without constant bespoke
support.

Raphaël Hoogvliets adds the operating model for adoption. His centralized MLOps
team supports product teams and gathers pain points. It uses feedback loops and
quick wins before pushing broader standards
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
In practice, that makes [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
a platform requirement. Notebooks, CI templates, model handoff paths, and
deployment workflows need to reduce cognitive load.

## Platform Components

The podcast archive keeps returning to a compact platform service set:

- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
  gives teams a run history and supports reproducibility. Simon Stiebellehner
  treats it as an early win in
  [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) creates the
  handoff from training to downstream consumption. Simon connects it to batch
  inference, online serving, and orchestration in
  [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
- CI, repository standards, tests, and parameterization make releases
  repeatable because Raphaël Hoogvliets connects those practices to reproducibility in
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- Serving, monitoring, and dependency management keep models useful after
  deployment because Raphaël covers package registries, Docker, Kubernetes, and
  Databricks tradeoffs in
  [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
- Version control, CI/CD, registries, and reusable repositories make the
  service set consistent across teams. Maria Vechtomova ties those practices to
  standard platform guardrails in
  [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}).

## Standardization and Developer Experience

ML platform standardization is useful when it makes teams faster and safer, not
when it hides all flexibility. Simon Stiebellehner describes thin abstractions
over cloud providers, self-service notebooks, and deployment paths. Product
teams avoid repetitive infrastructure work
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Maria Vechtomova's platform advice points in the same direction because teams
can reuse Kubernetes, Git, and CI/CD. They can then add conventions, templates,
and guardrails where teams repeatedly struggle
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

The strongest platform pages in this repo therefore sit near
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}),
[GitOps for Data Teams]({{ '/wiki/gitops-for-data-teams/' | relative_url }}),
and [MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}). The podcast
evidence doesn't support a one-size-fits-all tool stack. It supports a
product-minded platform team that standardizes work teams shouldn't repeat.
Those tasks include repository layout and release paths. They also include
artifact storage, access rules, monitoring hooks, and basic governance.

## Governance, Reproducibility, and Risk

Enterprise and regulated teams need more than convenience tooling. Simon
Stiebellehner ties platform design to metadata, lineage, and artifact logging.
Security, GDPR implications, deletion rules, and unified prediction schemas
also matter
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Those requirements connect the platform directly to
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}),
[Governance]({{ '/wiki/governance/' | relative_url }}), and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

Alexander Hendorf's enterprise AI discussion reinforces the same lesson from a
strategy view. He emphasizes data-first readiness and retraining. Feedback
loops, MLOps automation, and long-term platform selection also matter. His
episode also ties
enterprise MLOps to standardization and CI/CD. Governance and reproducibility
sit in the same platform discussion
([Scaling Enterprise AI]({{ '/podcasts/scaling-enterprise-ai-mlops-data-first-strategy/' | relative_url }})).

In these discussions, governance isn't a separate compliance afterthought. It
is part of the release path for moving models into production.

## Compute, Orchestration, and AI Infrastructure

The platform boundary expands when model workloads put pressure on compute and
orchestration. Simon Stiebellehner names cloud infrastructure, Kubernetes,
Terraform, and managed compute as core platform skills. He also names notebooks
and batch jobs. Online serving and pipeline orchestration sit in the same
platform skill set
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Raphaël Hoogvliets adds dependency compatibility and package registries. Docker
images, Kubernetes, and Databricks affect reproducibility and team autonomy
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Andrey Cheptsov's AI infrastructure episode pushes the platform discussion into
GPU economics and distributed training. It names PyTorch, NCCL, and
communication bottlenecks. It also covers optimization and cloud versus on-prem
decisions. Kubernetes limits and Slurm-like scheduling needs become platform
concerns. Bare-metal provisioning does too
([Post-ChatGPT AI Infrastructure]({{ '/podcasts/ai-infrastructure-hybrid-cloud-on-prem-distributed-training/' | relative_url }})).

For large model teams, the ML platform can't be separated cleanly from
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}). For more
typical product ML teams, the platform may stay focused on
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
model packaging, and deployment paths. Monitoring and feedback loops still
matter.

## Related Pages

Use these pages for narrower lifecycle, product, and infrastructure topics.

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }})
- [Governance]({{ '/wiki/governance/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [ML Product Manager Role]({{ '/wiki/ml-product-manager-role/' | relative_url }})
