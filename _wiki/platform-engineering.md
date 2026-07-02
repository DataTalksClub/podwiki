---
layout: wiki
title: "Platform Engineering"
summary: "How DataTalks.Club guests describe internal platform teams and self-service platform ownership."
related:
  - ML Platforms
  - Developer Experience
  - Machine Learning Infrastructure
  - MLOps
  - Platform Adoption
  - Self-Service Data Platforms
  - DataOps Engineer Role
---

Platform engineering is the work of building shared internal systems. Those
systems help other teams ship technical work without rebuilding the same
infrastructure in every project. In DataTalks.Club podcast discussions, the closest
neighbors are [[ML platforms]] and
[[MLOps]]. The topic also connects to
[[developer experience]] and
[[data engineering platforms]].

The platform team isn't only an infrastructure team. It owns paved paths and
templates along with tooling integrations and documentation. It also owns
support models and operating standards.

Platform work spans cloud infrastructure, Kubernetes, and Terraform, and it
starts from data science workflows before moving into self-service compute,
[[experiment tracking]],
[[model registry]], serving, and
orchestration
([[person:simonstiebellehner|Simon Stiebellehner]] in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

## Reusable Internal Paths

Across the interviews, platform engineering means making repeated technical
work reusable. The repeated work can be compute provisioning or a model release
path. It can also be observability setup, repository standards, or a reliable
path for publishing data products.

Platform work answers repeated deployment and governance problems, with
build-versus-buy and standardization as responses to team-level repetition.
There is also room for incremental SaaS components instead of a single large
internal platform
([[person:simonstiebellehner|Simon Stiebellehner]] in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The same idea appears through a centralized enabling team: an MLOps team
supports product teams and ML engineers, and that support becomes concrete
through CI, repository structure, parameterization, and tests. Data versioning
and traceability come next, drawing on a skill mix across data science, SRE,
DevOps, and platform engineering
([[person:raphaelhoogvliets|Raphaël Hoogvliets]] in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

Platform engineering is therefore narrower than "all infrastructure" and broader
than a tool portal. A platform gives teams a supported way to do common work. It
also gives the organization a place to encode standards, security, and
reliability without turning every project into a custom consulting job.

The same pattern appears in the IoT domain as an "operating system for
sensors" — a platform layer that standardizes sensor onboarding, real-time
processing, storage, and data delivery to internal stakeholders. It handles
remote diagnostics and context for sensor data, turning raw signals into
business value through a shared pipeline rather than ad-hoc per-project
integrations
([[person:josemaria|José Figueiredo]] in
[[podcast:remote-data-engineering-work-and-building-iot-platforms|Remote Data Engineering and IoT Platforms]]).

## Build Timing and Product Discipline

Guests diverge most on timing and product discipline. They differ on when a
platform should exist, how productized it should be, and how much infrastructure
the platform team should own.

One caution is against starting too early: teams need real models, business
value, and repeated needs before they build heavy platform layers, keeping
[[machine learning infrastructure]]
close to actual workflow evidence
([[person:simonstiebellehner|Simon Stiebellehner]] in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

A contrasting emphasis starts from adoption and ties platform success to
feedback loops, pain-point discovery, quick wins, and value measurement. The
platform team earns standards by solving visible problems first
([[person:raphaelhoogvliets|Raphaël Hoogvliets]] in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

An internal product-management lens treats internal platform users as customers,
weighs usability costs, and moves to outcome-driven problem definition and user
research for internal platforms. That makes
[[platform adoption]] a product
problem, not only an engineering rollout
([[person:geojolly|Geo Jolly]] in
[[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy]]).

The tooling and integration boundary casts the MLOps architect as a
technical-business bridge, weighing tooling tradeoffs, build-versus-buy
decisions, and platform-agnostic integrations. That's the platform problem from
the buyer and integration side
([[person:dannyleybzon|Danny Leybzon]] in
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).

## Platform Ownership

Platform ownership usually sits with a central or enabling team, but guests
don't describe that team as a command center. It's closer to an internal product
team with infrastructure responsibility.

Raphaël's Eneco example is explicit. His centralized MLOps team supports
product teams, collects pain points, and improves the path to production
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
23:01 through 36:55). That team owns shared practices, but product teams still
own their ML use cases.

Simon makes ownership dependent on workload and operational burden. At 13:50
and 15:34 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
he discusses specialist versus generalist skill balance, team size, and
on-call. Platform ownership therefore includes support capacity. A service that
teams rely on in production needs owners who can maintain it.

Geo's episode shows why ownership also needs roadmap discipline. Internal
platform teams balance stakeholders and backlog, while compliance and rollout
governance sit with adoption. He covers those responsibilities throughout
[[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy]]
from 9:50 through 35:18. Without that product discipline, platform work can
become a pile of useful infrastructure that nobody adopts consistently.

## Developer Experience

Developer experience is where platform engineering becomes visible to users.
The user might be a data scientist, ML engineer, analytics engineer, or data
engineer. The platform is working when that user can complete the standard path
without learning every infrastructure detail first.

Simon starts platform design from data science workflows. At 10:47 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
he talks about understanding how data scientists work with notebooks. At 38:40,
he discusses thin abstraction layers over cloud providers. The useful layer
doesn't hide everything. It removes unnecessary friction while preserving the
cloud choices that matter.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
extends the same idea through education and tool adoption in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
At 13:52, he discusses Metaflow integrations with AWS, Kubernetes, and Argo. At
18:03, he defines DevRel around education, documentation, and a wisdom layer.

At 25:17 and 36:27, he connects feedback and documentation to dogfooding and
reproducible workflows. Those are public-tool examples, but internal platforms
need the same structure. Examples, docs, and feedback loops are part of the
platform.

Developer experience also explains why [[documentation]],
[[technical writing]], and
[[developer relations]] are
nearby topics. A platform with unclear workflows still creates support load,
even if the underlying infrastructure works.

## Self-Service

Self-service is the platform promise. Teams can do common work on their own
while staying inside approved paths. In Simon's ML-platform episode,
self-service starts with compute provisioning at 28:20. It continues through
experiment tracking at 29:41 and model registry at 30:32. At 31:15 and 31:51,
he moves to batch and online deployment plus orchestration
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Self-service doesn't mean no support. Raphaël's team still helps product
teams, gathers feedback, and delivers quick wins
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
25:20 through 36:55). The better definition is "supported autonomy." Teams
can move without opening tickets for routine work, and the platform team can
focus on reusable improvements instead of one-off fixes.

The data-platform version appears in
[[self-service-data-platforms|self-service data platforms]]
and [[data engineering platforms]].
Use
[[Data Mesh vs Centralized Data Platform]]
when the platform question is whether domain teams or a shared platform own the
data-product path.
The ML version appears in [[ML Platforms]],
[[MLOps Tools]], and
[[MLOps Architecture]].
The shared platform decision is whether a repeated path is mature enough to
turn into a supported product.

## MLOps and Data Platform Boundaries

Platform engineering crosses both MLOps and data platforms, but those concepts
shouldn't collapse into one bucket. [[MLOps]]
covers model lifecycle work. It
includes experiments, registries, serving, and monitoring. It also includes
reproducibility and release practice.

Data platforms cover ingestion and transformation. They also cover quality,
governance, access, and shared data products.

Simon and Raphaël sit mostly on the ML side. Simon's platform path includes
experiment tracking, model registry, serving, and orchestration. Metadata,
lineage, and governance belong there too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
29:41 through 45:50). Raphaël's path starts with CI and repository structure.
It then adds parameterization, tests, traceability, and package registries.

The same episode also covers Docker and Kubernetes. Databricks, serving, and
monitoring are part of that platform path too
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
39:06 through 56:50).

Data platform pages use the same platform-engineering logic for a different
asset. [[Data Engineering Platforms]]
and [[DataOps]] focus on reliable data
movement, contracts, conventions, and quality. Platform engineering is the
operating model that can support both sides, but the artifact being served is
different. When a data team owns that operating path as a dedicated job, the
role is the [[dataops-engineer-role|DataOps engineer]],
the data-side counterpart to this platform work.

## Reliability

Reliability turns platform work from convenience into production ownership, so
platform engineers need to think about on-call and observability. They also need
dependency management, release paths, and incident response.

Simon brings reliability into the team-design discussion at 15:34 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
where on-call and operational support affect staffing. Later, at 39:54 through
45:50, he connects platform design to regulatory constraints and metadata.
Lineage, artifact logging, and governance make
reliability both a runtime concern and an audit concern.

Raphaël makes reliability part of adoption. Teams need CI, tests, and
traceability before production ML can be repeatable. Data versioning and
reproducibility belong in the same path. Package registries and containers also
belong there, along with serving and monitoring
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
39:06 through 1:01:58). Those practices connect platform engineering to
[[model monitoring]],
[[reproducibility]], and
[[production]].

Danny adds the operational monitoring focus. At 27:35 and 30:39 in
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]],
he connects model observability to upstream ETL and the shift from "why
monitor" to "how to monitor." At 31:50 and 36:47, he discusses profiling
architecture and platform-agnostic integrations. Platform reliability therefore
depends on data pipelines and model-serving integrations, not only the model
endpoint.

## Related Pages

These pages cover the adjacent platform and operations topics.

- [[ML Platforms]] covers the shared
  ML product surface for experiment tracking, registries, serving, and
  governance.
- [[Machine Learning Infrastructure]]
  covers the infrastructure layer behind ML workloads.
- [[Developer Experience]]
  covers usability, docs, templates, and adoption friction.
- [[Platform Adoption]] covers
  rollout, internal users, and value measurement.
- [[self-service-data-platforms|Self-Service Data Platforms]]
  covers the data-platform version of supported autonomy.
- [[Data Engineering Platforms]]
  covers platform work for data pipelines and shared data products.
- [[MLOps Architecture]]
  covers the architecture decisions that connect MLOps tools to platform
  ownership.
