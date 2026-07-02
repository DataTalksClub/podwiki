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
experiments into reliable production systems. DataTalks.Club interviews frame
the platform as more than a cluster, a notebook service, or a catalog of MLOps
tools. The platform gives teams a reusable path for training and tracking. It
then extends that path to registering, deploying, monitoring, and governing
models across teams.

That puts ML platforms between
[[MLOps]] and
[[Machine Learning Infrastructure]].

MLOps gives the operating discipline for production machine learning.
Infrastructure supplies compute and orchestration, along with the storage or
networking behind the platform. The platform turns those capabilities into a
user-facing system.

Data scientists and ML engineers need to adopt it. Product teams and governance
stakeholders do too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 10:47-31:51]],
[[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy, 11:24-18:25]]).

## Reusable Path from Experiment to Production

ML platforms give teams a reusable path from experimentation to production.
[[person:simonstiebellehner|Simon Stiebellehner]]
starts that platform surface with self-service compute and notebooks. He
treats [[experiment tracking]]
and a [[model registry]] as early
shared services. He then extends the platform to batch inference, online
serving, and orchestration. Metadata, lineage, and governance sit in the same
discussion
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 28:20-45:50]]).

[[person:raphaelhoogvliets|Raphaël Hoogvliets]]
describes a similar platform path through a centralized MLOps team. His team
supports product teams with CI, repository structure, parameterization, and
tests. It also works on data versioning and experiment capture. Serving and
monitoring follow. Package registries and container choices follow too
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 23:01-56:50]]).

In this definition, a platform is broader than one tool and narrower than the
whole engineering organization.
[[book:20221107-machine-learning-on-kubernetes|Machine Learning on Kubernetes]]
by Ross Brigoli and Faisal Masood covers the Kubernetes-native implementation of this platform surface: from training and serving operators to model registries and monitoring on shared infrastructure.

[[person:mariavechtomova|Maria Vechtomova]] reinforces
that pragmatic boundary. Her MLOps stack starts with Git, CI/CD, registries,
and model registries. Reproducibility and reusable repositories come before
more specialized layers
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps, 16:27-33:24]]).
That makes an ML platform close to
[[Platform Engineering]] and
[[Developer Experience]]:
the platform exists to make the supported path easier than a one-off path.

## Platform Boundaries and Investment Timing

The hardest platform questions are when to invest, how much product surface to
own, and how deep into infrastructure the team should go. Simon
argues for platform investment when repeated training, serving, deployment, or
governance problems appear across teams. He also warns against building a heavy
platform before the organization has real models and business needs
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 16:52-20:04 and 47:08-49:19]]).

Raphaël puts more emphasis on enablement and adoption. His platform team earns
trust by collecting pain points and delivering quick wins. It also improves
developer experience. Deployment frequency and impact give the team measurement
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 27:56-36:55]]).
That view connects ML platforms to
[[Platform Adoption]] as much as
to infrastructure.

[[person:geojolly|Geo Jolly]] makes the product
management version explicit. He treats an internal ML platform as a product with
users, roadmap choices, specs, and rollout governance. He also covers usability
costs. Observability metrics, surveys, and quality gates are part of the same
platform product work
([[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy, 9:50-18:25 and 55:44-57:20]]).
That pushes the boundary toward
[[ML Product Manager Role]]
and [[self-service-data-platforms|Self-Service Data Platforms]].

Infrastructure guests draw a different edge. [[person:andreycheptsov|Andrey Cheptsov]]
focuses on cloud cost, on-prem GPUs, and distributed training. He also covers
PyTorch and NCCL. Communication bottlenecks, Kubernetes limits, and Slurm-like
scheduling are infrastructure concerns too. Bare-metal provisioning is another
concern
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure, 8:25-56:53]]).

For large-model teams, the ML platform overlaps heavily with
[[AI Infrastructure]]. For
smaller product ML teams, deployment paths and registries can be the center.
Monitoring and reproducibility stay close.

## Self-Service Workflows

The user-facing part of an ML platform starts with routine work that teams
shouldn't have to rebuild. Simon describes self-service notebooks and compute,
then managed cloud resources. Experiment tracking, model registries, batch
jobs, and online serving form the path from exploration to production.
Orchestration ties that path together
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 21:03-34:01]]).
He also argues for thin abstractions over cloud providers when they reduce
repetitive infrastructure work without hiding every detail
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 38:40]]).

Geo's platform PM discussion explains why self-service is a product problem.
The users are internal data scientists and ML engineers. Business data
engineers and stakeholders also influence the platform. Poor tooling usability has
a productivity cost, so roadmap work needs user interviews and workshops.
Adoption plans and rollout sequencing matter too
([[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy, 11:24-21:06 and 35:18-40:14]]).

Raphaël adds the operating model. A platform team should gather pain points and
deliver visible improvements. It should also keep feedback loops open with
product teams
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 23:01-36:55]]).

For ML platforms, [[Developer Experience]]
isn't a polish layer. It's how notebooks and CI templates become usable, and
model handoffs need the same attention. Deployment workflows, documentation,
and support practices do too.

## Lifecycle Services

Guests repeatedly name a compact platform service set, starting with experiment
tracking for run history, collaboration, and reproducibility. Simon treats it as
an early win before moving to a model
registry for downstream consumption
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 29:41-30:32]]).

The registry becomes the handoff point between training and production. Simon
connects it to batch inference, online serving, and orchestration. Metadata
and lineage are part of the same registry-centered platform path
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 30:32-42:48]]).

Raphaël's lifecycle list adds CI, repository structure, parameterization, and
testing. It also includes data versioning and serving, while monitoring and
package registries belong in that path. Docker, Kubernetes, and Databricks
tradeoffs affect deployment
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 39:06-56:50]]).

Feature stores are a specialized lifecycle service when teams need reliable
real-time features. [[person:willempienaar|Willem Pienaar]]
describes feature stores as a way to reduce duplicated feature logic,
training-serving skew, and slow production handoffs. He places them inside the
ML lifecycle alongside materialization, serving, and validation. Registries and
monitoring also belong in that feature platform architecture
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps, 6:30-40:00]]).
That makes feature platforms useful for online tabular use cases, but not a
default requirement for every ML platform.

## Standardization and Guardrails

Standardization is useful when it removes repeated work and makes releases
safer. Maria argues against chasing the MLOps tool landscape for its own sake.
She emphasizes existing infrastructure, Kubernetes, Git, and CI/CD. Registries
are part of that base layer. Cookie-cutter repositories, service principals,
and packaged notebook logic are part of the same standardized path
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps, 14:45-35:21]]).

Raphaël's adoption story gives the same warning from another direction.
Standards land better after a team has found tangible pain and delivered quick
wins. Deployment frequency and impact measures help the team show value
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 32:46-48:41]]).

The platform should therefore standardize where teams repeatedly struggle. That
can include repository layout, release paths, and artifact storage. Dependency
management, access rules, and monitoring hooks are other common candidates. A
reference architecture alone isn't enough reason to add every component.

The podcast evidence supports tool-agnostic engineering fundamentals. It also
supports a coherent user path more strongly than a fixed universal stack
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps, 39:29-57:14]]).

## Governance and Risk Controls

Enterprise ML platforms need more than convenience tooling. Simon ties platform
design to metadata, lineage, artifact logging, and security. GDPR implications,
dataset retention, and unified prediction schemas also guide monitoring and
analytics
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 39:54-54:15]]).
Those requirements connect ML platforms directly to
[[Reproducibility]],
[[Governance]], and
[[Data Quality and Observability]].

[[person:alexanderhendorf|Alexander Hendorf]] adds the
enterprise strategy view. He frames scaled AI around data-first readiness,
realistic experimentation, retraining, and feedback loops. MLOps automation,
standardization, and CI/CD follow from that readiness work. Governance,
reproducibility, and long-term platform selection follow too
([[podcast:scaling-enterprise-ai-mlops-data-first-strategy|Scaling Enterprise AI, 49:10-58:51]]).
In these discussions, governance is part of the release path for production
models, not a separate compliance step after deployment.

Geo adds release governance from the product side. Approvals, compliance, and
timing are platform work when the platform controls how models reach users.
Model validation, shadowing, and release checklists belong in the same rollout
path
([[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy, 31:28-35:18 and 57:20]]).

## Compute and Orchestration

The platform boundary expands when workloads put pressure on compute and
orchestration. Simon includes cloud infrastructure, Kubernetes, Terraform, and
managed compute in the ML platform skill set. Notebooks and batch jobs are part
of the same skill set. Online serving and pipeline orchestration are too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms, 8:11-13:50 and 28:20-34:01]]).

Raphaël adds the reproducibility view. Dependency compatibility, package
registries, and Docker images affect whether teams can deploy models.
Kubernetes and Databricks choices can also prevent or create integration
problems
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale, 51:21-57:56]]).

Andrey's AI infrastructure episode pushes this section further for modern
large-model work. Cloud versus on-prem economics and GPU allocation become
platform design concerns. Teams also need distributed training, communication
overhead, and DeepSpeed-style optimization. Kubernetes limitations, Slurm-like
schedulers, and bare-metal automation enter the same design space when teams
train or serve large models
([[podcast:ai-infrastructure-hybrid-cloud-on-prem-distributed-training|Post-ChatGPT AI Infrastructure, 30:16-56:53]]).
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
- [[self-service-data-platforms|Self-Service Data Platforms]]
- [[ML Product Manager Role]]
