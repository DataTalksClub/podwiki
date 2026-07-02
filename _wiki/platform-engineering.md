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
---

Platform engineering is the work of building shared internal systems. Those
systems help other teams ship technical work without rebuilding the same
infrastructure in every project. In DataTalks.Club podcast discussions, the closest
neighbors are [ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). The topic also connects to
[developer experience]({{ '/wiki/developer-experience/' | relative_url }}) and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

The platform team isn't only an infrastructure team. It owns paved paths and
templates along with tooling integrations and documentation. It also owns
support models and operating standards.

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
connects platform work to cloud infrastructure, Kubernetes, and Terraform at
8:11. At 10:47, he starts from data science workflows. He then moves into
self-service compute, [experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
[model registry]({{ '/wiki/model-registry/' | relative_url }}), and serving.
At 31:51, he adds orchestration.

## Reusable Internal Paths

Across the interviews, platform engineering means making repeated technical
work reusable. The repeated work can be compute provisioning or a model release
path. It can also be observability setup, repository standards, or a reliable
path for publishing data products.

Simon gives the clearest ML-platform version. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he describes platform work as an answer to repeated deployment and governance
problems. At 16:52 and 17:14, he frames build-versus-buy and standardization
as responses to team-level repetition. At 20:04, he also leaves room for
incremental SaaS components instead of a single large internal platform.

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes the same idea through a centralized enabling team in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
At 23:01 and 25:20, his MLOps team supports product teams and ML engineers. At
39:06, that support becomes concrete through CI and repository structure. He
also names parameterization and tests.

At 42:31 and 45:10, Raphaël adds data versioning and traceability. He also
describes a skill mix across data science, SRE, DevOps, and platform
engineering.

DataTalks.Club guests therefore describe platform engineering as narrower than
"all infrastructure" and broader than a tool portal. A platform gives teams a
supported way to do common work. It also gives the organization a place to
encode standards, security, and reliability without turning every project into a
custom consulting job.

[José Figueiredo]({{ '/people/josemaria/' | relative_url }}) brings the
same pattern into the IoT domain. In
[Remote Data Engineering and IoT Platforms]({{ '/podcasts/remote-data-engineering-work-and-building-iot-platforms/' | relative_url }}),
he describes building an "operating system for sensors" — a platform layer that
standardizes sensor onboarding, real-time processing, storage, and data
delivery to internal stakeholders. The platform handles remote diagnostics and
context for sensor data, turning raw signals into business value through a
shared pipeline rather than ad-hoc per-project integrations.

## Build Timing and Product Discipline

Guests diverge most on timing and product discipline. They differ on when a
platform should exist, how productized it should be, and how much infrastructure
the platform team should own.

Simon is cautious about starting too early. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he argues at 47:08 and 49:19 that teams need real models and business value.
They also need repeated needs before they build heavy platform layers. Simon
keeps [machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
close to actual workflow evidence.

In [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
Raphaël starts from adoption and connects platform success to feedback loops at
27:56. At 32:46, he moves to pain-point discovery and quick wins. At 36:55, he
adds value measurement. His platform team earns standards by solving visible
problems first.

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) puts the internal
product-management lens on the same work. In
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }}),
he discusses internal platform users as customers at 11:24 and usability costs
at 13:44. At 16:44, he moves to outcome-driven problem definition. He returns
to user research for internal platforms at 55:44, which makes
[platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}) a product
problem, not only an engineering rollout.

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) adds the
tooling and integration boundary. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he frames the MLOps architect as a technical-business bridge at 8:11 and
discusses tooling tradeoffs at 10:32. At 34:25 and 36:47, he moves into
build-versus-buy decisions and platform-agnostic integrations. That's the
platform problem from the buyer and integration side.

## Platform Ownership

Platform ownership usually sits with a central or enabling team, but guests
don't describe that team as a command center. It's closer to an internal product
team with infrastructure responsibility.

Raphaël's Eneco example is explicit. His centralized MLOps team supports
product teams, collects pain points, and improves the path to production
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
23:01 through 36:55). That team owns shared practices, but product teams still
own their ML use cases.

Simon makes ownership dependent on workload and operational burden. At 13:50
and 15:34 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he discusses specialist versus generalist skill balance, team size, and
on-call. Platform ownership therefore includes support capacity. A service that
teams rely on in production needs owners who can maintain it.

Geo's episode shows why ownership also needs roadmap discipline. Internal
platform teams balance stakeholders and backlog, while compliance and rollout
governance sit with adoption. He covers those responsibilities throughout
[ML Product Manager and MLOps Platform Strategy]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})
from 9:50 through 35:18. Without that product discipline, platform work can
become a pile of useful infrastructure that nobody adopts consistently.

## Developer Experience

Developer experience is where platform engineering becomes visible to users.
The user might be a data scientist, ML engineer, analytics engineer, or data
engineer. The platform is working when that user can complete the standard path
without learning every infrastructure detail first.

Simon starts platform design from data science workflows. At 10:47 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
he talks about understanding how data scientists work with notebooks. At 38:40,
he discusses thin abstraction layers over cloud providers. The useful layer
doesn't hide everything. It removes unnecessary friction while preserving the
cloud choices that matter.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
extends the same idea through education and tool adoption in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
At 13:52, he discusses Metaflow integrations with AWS, Kubernetes, and Argo. At
18:03, he defines DevRel around education, documentation, and a wisdom layer.

At 25:17 and 36:27, he connects feedback and documentation to dogfooding and
reproducible workflows. Those are public-tool examples, but internal platforms
need the same structure. Examples, docs, and feedback loops are part of the
platform.

Developer experience also explains why [documentation]({{ '/wiki/documentation/' | relative_url }}),
[technical writing]({{ '/wiki/technical-writing/' | relative_url }}), and
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}) are
nearby topics. A platform with unclear workflows still creates support load,
even if the underlying infrastructure works.

## Self-Service

Self-service is the platform promise. Teams can do common work on their own
while staying inside approved paths. In Simon's ML-platform episode,
self-service starts with compute provisioning at 28:20. It continues through
experiment tracking at 29:41 and model registry at 30:32. At 31:15 and 31:51,
he moves to batch and online deployment plus orchestration
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Self-service doesn't mean no support. Raphaël's team still helps product
teams, gathers feedback, and delivers quick wins
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
25:20 through 36:55). The better definition is "supported autonomy." Teams
can move without opening tickets for routine work, and the platform team can
focus on reusable improvements instead of one-off fixes.

The data-platform version appears in
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Use
[Data Mesh vs Centralized Data Platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }})
when the platform question is whether domain teams or a shared platform own the
data-product path.
The ML version appears in [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}),
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}), and
[MLOps Architecture]({{ '/wiki/mlops-architecture/' | relative_url }}).
The shared platform decision is whether a repeated path is mature enough to
turn into a supported product.

## MLOps and Data Platform Boundaries

Platform engineering crosses both MLOps and data platforms, but those concepts
shouldn't collapse into one bucket. [MLOps]({{ '/wiki/mlops/' | relative_url }})
covers model lifecycle work. It
includes experiments, registries, serving, and monitoring. It also includes
reproducibility and release practice.

Data platforms cover ingestion and transformation. They also cover quality,
governance, access, and shared data products.

Simon and Raphaël sit mostly on the ML side. Simon's platform path includes
experiment tracking, model registry, serving, and orchestration. Metadata,
lineage, and governance belong there too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
29:41 through 45:50). Raphaël's path starts with CI and repository structure.
It then adds parameterization, tests, traceability, and package registries.

The same episode also covers Docker and Kubernetes. Databricks, serving, and
monitoring are part of that platform path too
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
39:06 through 56:50).

Data platform pages use the same platform-engineering logic for a different
asset. [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}) focus on reliable data
movement, contracts, conventions, and quality. Platform engineering is the
operating model that can support both sides, but the artifact being served is
different.

## Reliability

Reliability turns platform work from convenience into production ownership, so
platform engineers need to think about on-call and observability. They also need
dependency management, release paths, and incident response.

Simon brings reliability into the team-design discussion at 15:34 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
where on-call and operational support affect staffing. Later, at 39:54 through
45:50, he connects platform design to regulatory constraints and metadata.
Lineage, artifact logging, and governance make
reliability both a runtime concern and an audit concern.

Raphaël makes reliability part of adoption. Teams need CI, tests, and
traceability before production ML can be repeatable. Data versioning and
reproducibility belong in the same path. Package registries and containers also
belong there, along with serving and monitoring
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
39:06 through 1:01:58). Those practices connect platform engineering to
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}).

Danny adds the operational monitoring focus. At 27:35 and 30:39 in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
he connects model observability to upstream ETL and the shift from "why
monitor" to "how to monitor." At 31:50 and 36:47, he discusses profiling
architecture and platform-agnostic integrations. Platform reliability therefore
depends on data pipelines and model-serving integrations, not only the model
endpoint.

## Related Pages

These pages cover the adjacent platform and operations topics.

- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) covers the shared
  ML product surface for experiment tracking, registries, serving, and
  governance.
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
  covers the infrastructure layer behind ML workloads.
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
  covers usability, docs, templates, and adoption friction.
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) covers
  rollout, internal users, and value measurement.
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
  covers the data-platform version of supported autonomy.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  covers platform work for data pipelines and shared data products.
- [MLOps Architecture]({{ '/wiki/mlops-architecture/' | relative_url }})
  covers the architecture decisions that connect MLOps tools to platform
  ownership.
