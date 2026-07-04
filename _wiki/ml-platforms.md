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
governance stakeholders need to use it too[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]][[cite:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager]].

## Reusable Path from Experiment to Production

ML platforms give teams a reusable path from experimentation to production. One
path begins with self-service compute and notebooks. It adds
[[experiment tracking]] and a [[model registry]] as early shared services. It
then extends to batch inference, online serving, and orchestration. Metadata,
lineage, and governance stay in the same path[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

A similar path runs through a centralized MLOps team that supports product teams
with CI and tests. It also defines repository structure and parameterization. It
then adds experiment capture after data versioning. Serving and monitoring follow
next. Package registries and container choices follow too[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

In this definition, a platform is broader than one tool and narrower than the
whole engineering organization.
[[book:20221107-machine-learning-on-kubernetes=>Machine Learning on Kubernetes]]
by Ross Brigoli and Faisal Masood covers this Kubernetes-native platform
surface. It explains training and serving operators, model registries, and
monitoring on shared infrastructure.

A pragmatic MLOps stack starts with Git, CI/CD, and registries. Reproducibility,
model registries, and reusable repositories come before more specialized
layers[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]].
That makes an ML platform close to
[[Platform Engineering]] and
[[Developer Experience]]:
the platform exists to make the supported path easier than a one-off path.

## Platform Boundaries and Investment Timing

The hardest platform questions are when to invest, how much product surface to
own, and how deep into infrastructure the team should go. Platform investment
pays off when repeated training, serving, deployment, or governance problems
appear across teams. Building a heavy platform before the organization has real
models and business needs is a mistake[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Single teams may still need platform pieces before the company needs a full
platform. An experiment tracker, a managed registry, or a thin cloud wrapper can
create value before a company-wide ML platform exists. Teams should invest in
heavier platform work when they need repeated standardization across teams, not
only because one model reached production.

Buying SageMaker, Vertex AI, or another managed platform still leaves
integration work. The team has to fit the tool to its data-science workflow,
deployment patterns, security constraints, and monitoring schemas[[cite:building-production-ml-platform-and-mlops-team@20:04=>Production ML Platforms]].

Enablement and adoption matter as much as infrastructure. A platform team earns
trust by collecting pain points and delivering quick wins. The team improves
developer experience and measures progress by deployment frequency and
impact[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
That view connects ML platforms to
[[Platform Adoption]] as much as
to infrastructure.

An internal ML platform is a product with users. Platform teams make roadmap
choices, write specs, and plan rollout governance. Because usability has costs,
observability metrics, surveys, and quality gates belong to platform product
work[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager]].
That pushes the boundary toward
[[ML Product Manager Role]]
and [[self-service-data-platforms=>Self-Service Data Platforms]].

Infrastructure draws a different edge around cloud cost, on-prem GPUs, and
distributed training. PyTorch and NCCL also sit on that side of the boundary.
Communication bottlenecks and Kubernetes limits are infrastructure concerns too.
So are Slurm-like scheduling and bare-metal provisioning[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>AI Infrastructure]].

For large-model teams, the ML platform overlaps heavily with
[[AI Infrastructure]]. For
smaller product ML teams, deployment paths and registries can be the center.
Monitoring and reproducibility stay close.

## Self-Service Workflows

Teams shouldn't have to rebuild routine work. The user-facing part of an ML
platform starts with self-service notebooks and compute, then managed cloud
resources. Experiment tracking, model registries, batch jobs, and online
serving form the path from exploration to production. Orchestration ties that
path together[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].
Thin abstractions over cloud providers help when they reduce repetitive
infrastructure work without hiding every detail[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

Self-service is a product problem. The users are internal data scientists and
ML engineers, with business data engineers and stakeholders also influencing the
platform. Poor tooling usability has a productivity cost. Roadmap work needs
user interviews, workshops, and adoption planning. Rollout sequencing matters too[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager]].

A platform team should gather pain points, deliver visible improvements, and
keep feedback loops open with product teams[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

For ML platforms, [[Developer Experience]]
isn't a polish layer. It's how notebooks and CI templates become usable, and
model handoffs need the same attention. Deployment workflows, documentation,
and support practices do too.

## Lifecycle Services

A compact platform service set recurs across these discussions, starting with
experiment tracking for run history, collaboration, and reproducibility. It's an
early win before moving to a model registry for downstream consumption[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

The registry becomes the handoff point between training and production,
connecting to batch inference, online serving, and orchestration. Metadata and
lineage are part of the same registry-centered path[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].
That handoff matters because downstream jobs and services need a promoted model
record they can load predictably. The registry isn't only storage for a model
file. It's the stable production reference that monitoring, rollback, and
deployment automation can agree on[[cite:building-production-ml-platform-and-mlops-team@30:32=>Production ML Platforms]].

A fuller lifecycle list adds CI, repository structure, parameterization, and
testing. It also adds data versioning, serving, monitoring, and package
registries. Docker, Kubernetes, and Databricks tradeoffs affect deployment[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Feature stores are a specialized lifecycle service when teams need reliable
real-time features. They reduce duplicated feature logic and training-serving
skew. They also reduce slow production handoffs.

They sit inside the ML lifecycle alongside materialization, serving, and
validation. Registries and monitoring are part of that feature platform
architecture[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]].
That makes feature platforms useful for online tabular use cases, but not a
default requirement for every ML platform.

## Standardization and Guardrails

Standardization is useful when it removes repeated work and makes releases
safer. Chasing the MLOps tool landscape for its own sake isn't the goal.
Existing infrastructure and Kubernetes form part of the base layer. Git, CI/CD,
and registries belong there too. Cookie-cutter repositories, service principals,
and packaged notebook
logic are part of the same standardized path[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]].

The same warning holds from the adoption side: standards land better after a
team has found tangible pain and delivered quick wins. Deployment frequency and
impact measures help show value[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

The platform should therefore standardize where teams repeatedly struggle. That
can include repository layout, release paths, and artifact storage. Dependency
management, access rules, and monitoring hooks are other common candidates. A
reference architecture alone isn't enough reason to add every component.

In finance, that same standardization can show up as internal libraries and a
FastAPI framework. Those shared pieces let teams reuse serving, integration,
and operational patterns instead of rebuilding them project by project. The
platform value is the shared path and governance surface around that reuse, not
just the framework choice[[cite:mlops-and-ml-engineering-in-finance=>ML Engineering in Finance]].

Tool-agnostic engineering fundamentals and a coherent user path matter more than
a fixed universal stack[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]].

## Governance and Risk Controls

Enterprise ML platforms need more than convenience tooling. Teams need metadata,
lineage, artifact logging, and security in the platform. GDPR implications,
dataset retention, and unified prediction schemas guide monitoring and
analytics[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].
Those requirements connect ML platforms directly to
[[Reproducibility]],
[[Governance]], and
[[Data Quality and Observability]].

The governance boundary is practical. A platform can log metadata about a query
and pipeline run. It can also log the image, data version, and output. It
doesn't have to copy every training dataset into managed storage. Copying full
datasets for every run creates cost and deletion problems when personal data
appears in the artifacts.

In regulated settings, platform design has to decide what's persisted as
metadata and what's stored as a pointer. It also has to decide what remains
under the original data-governance controls[[cite:building-production-ml-platform-and-mlops-team@45:50=>Production ML Platforms]].

From the enterprise strategy view, scaled AI rests first on data-first readiness
and realistic experimentation. Retraining and feedback loops are part of that
base too. MLOps automation, standardization, and CI/CD follow from that readiness
work. Governance, reproducibility, and long-term platform selection come
next[[cite:scaling-enterprise-ai-mlops-data-first-strategy=>Scaling Enterprise AI]].
Governance is part of the release path for production models, not a separate
compliance step after deployment.

Release governance also comes from the product side. Approvals, compliance, and
timing are platform work when the platform controls how models reach users.
Model validation, shadowing, and release checklists belong in the same rollout
path[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager]].

## Compute and Orchestration

The platform boundary expands when workloads put pressure on compute and
orchestration. The ML platform skill set includes cloud infrastructure,
Kubernetes, Terraform, and managed compute. It also includes notebooks and batch
jobs. Online serving and pipeline orchestration belong there too[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]].

On the reproducibility side, dependency compatibility, package registries, and
Docker images affect whether teams can deploy models. Kubernetes and Databricks
choices can prevent or create integration problems[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].

Modern large-model work pushes this further. Cloud versus on-prem economics and
GPU allocation become platform design concerns. Large-model teams need
distributed training, communication overhead, and DeepSpeed-style optimization.
Kubernetes limitations, Slurm-like schedulers, and bare-metal automation enter
the same design space when teams train or serve large models[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training=>AI Infrastructure]].
That's where ML platforms meet
[[AI Infrastructure]] and
[[Machine Learning System Design]].

## Related Pages

Use these pages for narrower lifecycle, product, and infrastructure details.

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
