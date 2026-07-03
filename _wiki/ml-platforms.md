---
layout: wiki
title: "ML Platforms"
summary: "Reference page for shared ML platform systems, internal product strategy, and team enablement."
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

An ML platform is the shared internal product that helps teams move models from
experiments into reliable production systems. It's more than a cluster or a
notebook service. It's also more than a catalog of MLOps tools. The platform
gives teams a reusable path for training and tracking. It then extends that path
to registering, deploying, monitoring, and governing models across teams.

That puts ML platforms between
[[MLOps]] and
[[Machine Learning Infrastructure]].

MLOps gives the operating discipline for production machine learning.
Infrastructure supplies compute and orchestration, along with the storage or
networking behind the platform. The platform turns those capabilities into a
user-facing system.

Adoption has to reach beyond data scientists and ML engineers. Product teams and
governance stakeholders need to use it too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
[[podcast:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager and MLOps Platform Strategy]]).

## Reusable Path from Experiment to Production

ML platforms give teams a reusable path from experimentation to production. One
path begins with self-service compute and notebooks. It adds
[[experiment tracking]] and a [[model registry]] as early shared services. It
then extends to batch inference, online serving, and orchestration. Metadata,
lineage, and governance stay in the same path
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

A similar path runs through a centralized MLOps team that supports product teams
with CI and tests. It also defines repository structure and parameterization. It
then adds experiment capture after data versioning. Serving and monitoring follow
next. Package registries and container choices follow too
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

In this definition, a platform is broader than one tool and narrower than the
whole engineering organization.
[[book:20221107-machine-learning-on-kubernetes=>Machine Learning on Kubernetes]]
by Ross Brigoli and Faisal Masood covers this Kubernetes-native platform
surface. It explains training and serving operators, model registries, and
monitoring on shared infrastructure.

A pragmatic MLOps stack starts with Git, CI/CD, and registries. Reproducibility,
model registries, and reusable repositories come before more specialized layers
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]).
That makes an ML platform close to
[[Platform Engineering]] and
[[Developer Experience]]:
the platform exists to make the supported path easier than a one-off path.

## Platform Boundaries and Investment Timing

The hardest platform questions are when to invest, how much product surface to
own, and how deep into infrastructure the team should go. Platform investment
pays off when repeated training, serving, deployment, or governance problems
appear across teams. Building a heavy platform before the organization has real
models and business needs is a mistake
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

Enablement and adoption matter as much as infrastructure. A platform team earns
trust by collecting pain points and delivering quick wins. It improves developer
experience and measures progress by deployment frequency and impact
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
That view connects ML platforms to
[[Platform Adoption]] as much as
to infrastructure.

An internal ML platform is a product with users, roadmap choices, specs, and
rollout governance. Its usability has real costs. Observability metrics,
surveys, and quality gates are part of the same platform product work
([[person:geojolly|Geo Jolly]],
[[podcast:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager and MLOps Platform Strategy]]).
That pushes the boundary toward
[[ML Product Manager Role]]
and [[self-service-data-platforms|Self-Service Data Platforms]].

Infrastructure draws a different edge around cloud cost, on-prem GPUs, and
distributed training. PyTorch and NCCL also sit on that side of the boundary.
Communication bottlenecks and Kubernetes limits are infrastructure concerns too.
So are Slurm-like scheduling and bare-metal provisioning
([[person:andreycheptsov|Andrey Cheptsov]],
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).

For large-model teams, the ML platform overlaps heavily with
[[AI Infrastructure]]. For
smaller product ML teams, deployment paths and registries can be the center.
Monitoring and reproducibility stay close.

## Self-Service Workflows

The user-facing part of an ML platform starts with routine work that teams
shouldn't have to rebuild: self-service notebooks and compute, then managed
cloud resources. Experiment tracking, model registries, batch jobs, and online
serving form the path from exploration to production. Orchestration ties that
path together
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Thin abstractions over cloud providers help when they reduce repetitive
infrastructure work without hiding every detail
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Self-service is a product problem. The users are internal data scientists and
ML engineers, with business data engineers and stakeholders also influencing the
platform. Poor tooling usability has a productivity cost. Roadmap work needs
user interviews, workshops, and adoption planning. Rollout sequencing matters too
([[person:geojolly|Geo Jolly]],
[[podcast:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager and MLOps Platform Strategy]]).

A platform team should gather pain points, deliver visible improvements, and
keep feedback loops open with product teams
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

For ML platforms, [[Developer Experience]]
isn't a polish layer. It's how notebooks and CI templates become usable, and
model handoffs need the same attention. Deployment workflows, documentation,
and support practices do too.

## Lifecycle Services

A compact platform service set recurs across these discussions, starting with
experiment tracking for run history, collaboration, and reproducibility. It's an
early win before moving to a model registry for downstream consumption
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The registry becomes the handoff point between training and production,
connecting to batch inference, online serving, and orchestration. Metadata and
lineage are part of the same registry-centered path
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

A fuller lifecycle list adds CI, repository structure, parameterization, and
testing. It also adds data versioning, serving, monitoring, and package
registries. Docker, Kubernetes, and Databricks tradeoffs affect deployment
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

Feature stores are a specialized lifecycle service when teams need reliable
real-time features. They reduce duplicated feature logic, training-serving skew,
and slow production handoffs. They sit inside the ML lifecycle alongside
materialization, serving, and validation. Registries and monitoring are part of
that feature platform architecture
([[person:willempienaar|Willem Pienaar]],
[[podcast:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]).
That makes feature platforms useful for online tabular use cases, but not a
default requirement for every ML platform.

## Standardization and Guardrails

Standardization is useful when it removes repeated work and makes releases
safer. Chasing the MLOps tool landscape for its own sake isn't the goal.
Existing infrastructure and Kubernetes form part of the base layer. Git, CI/CD,
and registries belong there too. Cookie-cutter repositories, service principals,
and packaged notebook
logic are part of the same standardized path
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]).

The same warning holds from the adoption side: standards land better after a
team has found tangible pain and delivered quick wins. Deployment frequency and
impact measures help show value
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

The platform should therefore standardize where teams repeatedly struggle. That
can include repository layout, release paths, and artifact storage. Dependency
management, access rules, and monitoring hooks are other common candidates. A
reference architecture alone isn't enough reason to add every component.

In finance, that same standardization can show up as internal libraries and a
FastAPI framework. Those shared pieces let teams reuse serving, integration,
and operational patterns instead of rebuilding them project by project. The
platform value is the shared path and governance surface around that reuse, not
just the framework choice
([[cite:mlops-and-ml-engineering-in-finance|MLOps and ML Engineering in Finance]]).

The evidence favors tool-agnostic engineering fundamentals and a coherent user
path over a fixed universal stack
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

## Governance and Risk Controls

Enterprise ML platforms need more than convenience tooling. Platform design ties
to metadata, lineage, artifact logging, and security. GDPR implications,
dataset retention, and unified prediction schemas guide monitoring and analytics
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Those requirements connect ML platforms directly to
[[Reproducibility]],
[[Governance]], and
[[Data Quality and Observability]].

From the enterprise strategy view, scaled AI rests first on data-first readiness
and realistic experimentation. Retraining and feedback loops are part of that
base too. MLOps automation, standardization, and CI/CD follow from that readiness
work. Governance, reproducibility, and long-term platform selection follow too
([[person:alexanderhendorf|Alexander Hendorf]],
[[podcast:scaling-enterprise-ai-mlops-data-first-strategy=>Scaling Enterprise AI]]).
Governance is part of the release path for production models, not a separate
compliance step after deployment.

Release governance also comes from the product side. Approvals, compliance, and
timing are platform work when the platform controls how models reach users.
Model validation, shadowing, and release checklists belong in the same rollout
path
([[person:geojolly|Geo Jolly]],
[[podcast:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager and MLOps Platform Strategy]]).

## Compute and Orchestration

The platform boundary expands when workloads put pressure on compute and
orchestration. The ML platform skill set includes cloud infrastructure,
Kubernetes, Terraform, and managed compute. It also includes notebooks and batch
jobs. Online serving and pipeline orchestration belong there too
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

On the reproducibility side, dependency compatibility, package registries, and
Docker images affect whether teams can deploy models. Kubernetes and Databricks
choices can prevent or create integration problems
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

Modern large-model work pushes this further. Cloud versus on-prem economics and
GPU allocation become platform design concerns. Teams need distributed training,
communication overhead, and DeepSpeed-style optimization. Kubernetes
limitations, Slurm-like schedulers, and bare-metal automation enter the same
design space when teams train or serve large models
([[person:andreycheptsov|Andrey Cheptsov]],
[[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>Post-ChatGPT AI Infrastructure]]).
That's where ML platforms meet
[[AI Infrastructure]] and
[[Machine Learning System Design]].

## Related Pages

These pages cover narrower lifecycle, product, and infrastructure topics.

- [[MLOps]]
- [[ML Platform Engineer Role]]
- [[Platform Adoption]]
- [[Platform Engineering]]
- [[Machine Learning Infrastructure]]
- [[Developer Experience]]
- [[Experiment Tracking]]
- [[Model Registry]]
- [[Model Monitoring]]
- [[Reproducibility]]
- [[Governance]]
- [[AI Infrastructure]]
- [[self-service-data-platforms=>Self-Service Data Platforms]]
- [[ML Product Manager Role]]
