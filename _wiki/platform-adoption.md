---
layout: wiki
title: "Platform Adoption"
summary: "How DataTalks.Club podcast guests describe getting shared data and ML platforms used through pain-point discovery, self-service paths, developer experience, enablement, rollout, and measurement."
related:
  - Platform Engineering
  - Self-Service Data Platforms
  - Developer Experience
  - Data Product Adoption
  - MLOps
  - DataOps
---

Platform adoption means helping people use shared tools, standards, and
workflows. DataTalks.Club guests don't treat adoption as a
launch announcement. They describe it as product and enablement work. Teams
need to understand real pain and reduce the cost of the standard path. They
also need to earn trust with quick wins and measure whether people keep using
the platform
([MLOps at Scale, 27:56-36:55]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}),
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [developer experience]({{ '/wiki/developer-experience/' | relative_url }})
cover the architecture around adoption, but adoption is behavioral. A team can
expose compute and orchestration, then add a model registry or data contracts.
The rollout still fails when data scientists and data engineers don't know when
to use the platform. Analysts and product teams also need a clear reason to
change their work
([Building Production ML Platforms, 10:47-20:04]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Last-Mile Data Delivery, 20:02-26:21]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

## Adoption in Practice

Across the platform episodes, a team has adopted a platform when it changes its
normal way of working. [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes an MLOps team that supports product teams and listens to data
scientists and ML engineers. The same team improves developer experience
through feedback
([MLOps at Scale, 23:01-32:46]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Geo Jolly]({{ '/people/geojolly/' | relative_url }}) uses the product-management
language directly. Even an internal ML platform has customers and user
journeys. It also needs a roadmap, rollout strategy, and feedback surveys
([ML Product Manager and MLOps Platform Strategy, 11:24-16:44 and 55:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Tool coverage isn't the same as adoption. [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
lists self-service compute and [experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}),
then [model registry]({{ '/wiki/model-registry/' | relative_url }}),
orchestration, and serving. He still starts from how data scientists work in
notebooks and how models move from exploration into training and consumption
([Building Production ML Platforms, 10:47-31:51]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Adoption starts when those pieces fit the user's workflow closely enough that
the supported path is easier than a custom path.

## Start With Pain

In Raphaël's MLOps interview, his team creates buy-in by first collecting pain
points. The team maps where platform work can help and picks a quick win where
user pain and team capability overlap. He also recommends showing a
before-and-after picture so stakeholders can see what changed
([MLOps at Scale, 32:46-36:55]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

This puts platform adoption close to [developer experience]({{ '/wiki/developer-experience/' | relative_url }}).
The first useful signal is often friction in CI and repository structure. It
may also appear in deployment, dependency management, or monitoring
([MLOps at Scale, 39:06-53:08]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) makes the same
argument from [data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).
When people don't use a dashboard or analytical product, she recommends user
research, decision mapping, and low-fidelity prototypes before building the
polished system. The team should sit in the meetings where decisions happen and
work backward from the decision the data product should improve
([Last-Mile Data Delivery, 26:21-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).
For a shared platform, that means adoption research should start from repeated
work people already struggle with, not from a catalog of platform features.

## Make the Standard Path Easier

Teams adopt a platform when the standard path removes work they would otherwise
repeat. In Simon's ML platform discussion, that path starts with self-service
notebook or compute access. It can then add experiment tracking, a registry for
downstream model consumption, and batch or online deployment choices
([Building Production ML Platforms, 28:20-31:51]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
He also argues for thin abstraction layers when a company is already committed
to a cloud provider. Data scientists shouldn't have to think about every
infrastructure detail to use the platform
([Building Production ML Platforms, 34:01-38:40]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the data
engineering version. In a scale-up, a data platform team has many consumers. It
must make routine work possible without the platform team's direct help. Mehdi
includes onboarding sessions and support channels in the platform surface. He
also includes Airflow conventions and playbooks for best practices
([Scaling Data Engineering Teams and Self-Service Platforms, 12:30-17:22]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

For Kafka and event streaming, he uses schemas and schema registries. Data
contracts let users follow a guideline instead of rediscovering
change-management rules later
([Scaling Data Engineering Teams and Self-Service Platforms, 23:26]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Docs and Templates

Users meet the platform through examples and guidelines. Templates, repo
conventions, tests, and documentation are part of the same surface. Raphaël's MLOps team
standardizes CI, repository layout, parameterization, and testing. It also
standardizes data versioning, traceability, package registries, and containers.
([MLOps at Scale, 39:06-56:50]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Mehdi's "driving license" metaphor points in the same direction. Airflow alone
isn't the platform adoption mechanism, because people also need naming
conventions and sequence-handling rules. They need a playbook that explains how
to use the shared system safely
([Scaling Data Engineering Teams and Self-Service Platforms, 17:22]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

This puts platform adoption close to [documentation]({{ '/wiki/documentation/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }}), and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Teams shouldn't treat docs as a separate communication layer after the platform
is done. Docs are part of the self-service product.

## Enablement Teams

Several guests describe adoption as enablement rather than central control.
Raphaël's centralized MLOps team supports product teams and ML engineers, but
it earns influence by solving visible problems. The team also maintains
feedback with its users
([MLOps at Scale, 23:01-36:55]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) describes a
similar sequence from Spotify. The core team embedded with early adopters, then
worked on infrastructure and tools. Other teams could then build and deploy
their own data flows
([DataOps 101, 7:52-11:50]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

Enablement still needs staffing and operating ownership. Simon ties ML platform
work to cloud infrastructure, with Kubernetes and Terraform in that skill set.
He also includes on-call and support capacity. He warns against a heavy platform
before there's business value and repeated need
([Building Production ML Platforms, 8:11-20:04 and 47:08-49:19]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Fast-growing data platforms need senior people. Mehdi also warns that they need
niche technology experience to establish practices that can survive scale
([Scaling Data Engineering Teams and Self-Service Platforms, 20:13]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

## Stakeholder Buy-In

Internal platform users aren't the only stakeholders. Geo describes internal
platform product management as a balance between data scientists and business
data engineers. A product manager also has to account for compliance,
governance, engineering teams, and release timing. He frames adoption as "time
to stakeholders". The product manager needs to know who will adopt a platform
capability and when
([ML Product Manager and MLOps Platform Strategy, 9:50-16:44 and 45:18-48:10]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) adds the human
side of MLOps buy-in. Before building, teams should clarify the business case
and KPIs. They should also clarify the user story and alternatives. They may
need someone from the business available for demos and questions. They also
need that person for decisions.

Stakeholder concerns should turn into mitigations and metrics. Demos should
include feared scenarios, not only happy paths
([Human-Centered MLOps and Model Monitoring, 4:50-24:34]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

For platform rollout, the same habit applies to migration risks and governance
approvals. It also applies to service levels and incident communication
([Human-Centered MLOps and Model Monitoring, 24:34-27:14]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

## Rollout and Power Users

Guests rarely recommend a big-bang platform rollout. Simon favors incremental
platform pieces when a small team can already get value from them. Sometimes
teams can assemble those pieces from SaaS components
([Building Production ML Platforms, 20:04 and 49:19]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Geo describes internal rollouts through user journeys, governance, and power
users. Data scientists embedded with the platform team can help with
acceleration and demos. Geo also compares them to developer advocates
([ML Product Manager and MLOps Platform Strategy, 48:10-54:58]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Lars's DataOps story also supports staged rollout. His team embedded with early
adopters first, then enabled developer teams before non-technical analysts. He
describes the move from a centralized team handling ad hoc requests toward
self-service as a long journey. He recommends pairing analysts with engineering
expertise when the organization isn't ready for pure self-service
([DataOps 101, 7:52 and 50:13]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).
That keeps platform adoption grounded in team maturity instead of assuming
every group can use the same level of abstraction on day one.

## Measuring Use and Value

Platform teams should track use, value and trust signals. Raphaël suggests
deployment frequency and impact tracking as KPIs or OKRs. He also warns that
platform teams can lose buy-in if they can't show value
([MLOps at Scale, 36:55]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Geo adds observability metrics and surveys, including internal platform
"happiness" reports. Those reports help the team understand whether users can
work effectively with the platform
([ML Product Manager and MLOps Platform Strategy, 29:23 and 55:44]({{ '/podcasts/ml-product-manager-and-mlops-platform-strategy/' | relative_url }})).

Caitlin's last-mile episode adds a useful caution for platform metrics. Teams
can't measure all adoption work directly. She recommends proxies, time studies,
and small measurable wins. Advocates can show that a data product changed a
decision
([Last-Mile Data Delivery, 41:18-49:25]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

For platforms, the same idea applies to reduced support load and faster
onboarding. It also applies to repeatable deployments, fewer one-off pipelines,
and users choosing the standard path without being forced.

## Failure Modes

Guests warn that a team can build a technically coherent
[ML platform]({{ '/wiki/ml-platforms/' | relative_url }})
too early. It may not yet have repeated model work or clear business value
([Building Production ML Platforms, 47:08-49:19]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
It can also build self-service without conventions. Users may then break
schemas, invent incompatible pipeline conventions, or depend on reactive support
([Scaling Data Engineering Teams and Self-Service Platforms, 17:22-23:26]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

Adoption can also fail socially. If the platform team doesn't understand user
pain, it may ship tooling that solves the wrong problem
([MLOps at Scale, 32:46-36:55]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
If stakeholders don't trust the data or model, they may avoid using it. The
same risk appears when they don't trust the release process, even when the
system technically works
([Human-Centered MLOps and Model Monitoring, 12:22-24:34]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

If the platform team measures only feature delivery, it can miss whether users
changed behavior or shortened delivery. It can also miss whether they made
better decisions
([Last-Mile Data Delivery, 42:18-45:35]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).
