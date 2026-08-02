---
layout: wiki
title: "Platform Adoption"
summary: "How shared data and ML platforms earn adoption through pain discovery, self-service, enablement, rollout, and measurement."
related:
  - Platform Engineering
  - Self-Service Data Platforms
  - Developer Experience
  - Data Product Adoption
  - MLOps
  - MLOps Adoption at Scale
  - DataOps
---

Platform adoption means helping people use shared tools, standards, and
workflows. Platform teams don't create adoption with a launch announcement.
They create it through product and enablement work. They need to understand
real pain and reduce the cost of the standard path. They also need to earn
trust with quick wins and measure whether people keep using the platform.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

[[Platform engineering]],
[[self-service-data-platforms=>self-service data platforms]],
and [[developer experience]]
cover the architecture around adoption, but adoption is behavioral. A team can
expose compute and orchestration, then add a model registry or data contracts.
The rollout still fails when data scientists and data engineers don't know when
to use the platform. Analysts and product teams also need a clear reason to
change their work.

For ML-specific adoption, use
[[mlops-adoption-at-scale=>MLOps adoption at scale]] as the deeper path.
There, adoption turns on product-team support and shared deployment practices.
It also turns on reproducibility and governance.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Adoption in Practice

Across the platform episodes, a team has adopted a platform when it changes its
normal way of working. An MLOps platform team can support product teams,
listen to data scientists and ML engineers, and improve [[developer experience]]
through feedback.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Internal ML platforms need product-management work because they have internal
customers and user journeys. They also need roadmaps, rollout plans, and
feedback surveys.[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Platform Strategy]]

Tool coverage alone doesn't create adoption. A platform can expose
self-service compute, [[experiment tracking]], and a [[model registry]], then
add orchestration and serving. Those pieces need to fit notebook work, model
training, and downstream consumption closely enough that the supported path is
easier than a custom path.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

## Start With Pain

Platform teams create buy-in by collecting pain points first. The useful early
work sits where user pain and team capability overlap. A quick win should also
make the before-and-after difference visible to stakeholders.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

This puts platform adoption close to [[developer experience]].
The first useful signal is often friction in CI and repository structure. It
may also appear in deployment, dependency management, or monitoring.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

[[data product adoption=>Data product adoption]] follows the same research
logic. When people don't use a dashboard or analytical product, the team should
do user research and map decisions before it builds.
The team should also prototype, sit in the meetings where decisions happen, and
work backward from the decision the product should improve.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile]]
For a shared platform, that means adoption research should start from repeated
work people already struggle with, not from a catalog of platform features.

## Make the Standard Path Easier

Teams adopt a platform when the standard path removes repeated work. The path
can start with self-service notebook or compute access. It can then add
experiment tracking and a registry for downstream model consumption. Batch and
online deployment choices can come after that.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Thin abstraction layers matter when a company is already committed to a cloud
provider. Data scientists shouldn't have to think about every infrastructure
detail to use the platform.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Data engineering platforms have the same adoption pressure. In a scale-up, a
platform team serves many consumers, so routine work has to be possible without
direct help from the platform team. Onboarding sessions, support channels,
Airflow conventions, and playbooks become part of the platform surface.[[cite:scaling-data-engineering-teams-self-service-platforms=>Self-Service Data Platforms]]

For Kafka and event streaming, he uses schemas and schema registries. Data
contracts let users follow a guideline instead of rediscovering
change-management rules later.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Self-Service Data Platforms]]
Use the [[data-mesh-vs-centralized-data-platform=>mesh vs central platform]]
comparison when adoption becomes the practical test. Domain teams can own more
when shared paths beat bespoke support.

## Docs and Templates

Users meet the platform through examples and guidelines. Templates, repo
conventions, tests, and documentation are part of the same surface. Raphaël's MLOps team
standardizes CI, repository layout, parameterization, and testing. It also
standardizes data versioning, traceability, package registries, and containers.
For ML teams, those templates become part of
[[mlops-adoption-at-scale=>MLOps adoption at scale]] when they help multiple
product teams follow the same supported path.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Mehdi's "driving license" metaphor points in the same direction. Airflow alone
isn't the platform adoption mechanism, because people also need naming
conventions and sequence-handling rules. They need a playbook that explains how
to use the shared system safely.[[cite:scaling-data-engineering-teams-self-service-platforms=>Self-Service Data Platforms]]

This puts platform adoption close to [[documentation]],
[[DataOps]], and
[[data engineering platforms]].
Teams shouldn't treat docs as a separate communication layer after the platform
is done. Docs are part of the self-service product.

## Enablement Teams

Platform teams often work through enablement rather than central control. An
MLOps team can support product teams and ML engineers, but visible problems
give it influence. User feedback keeps the work tied to real needs.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Spotify's DataOps work followed a similar sequence. The core team embedded
with early adopters, then worked on infrastructure and tools. Other teams could
then build and deploy their own data flows.[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

Hinc's GitOps discussion adds a concrete enablement path. Data workers can
propose infrastructure or access changes through branches, plans, and review
instead of waiting on opaque tickets. That makes
[[gitops-for-data-teams=>GitOps for data teams]] part of platform adoption when
the standard path includes Terraform, Terragrunt, Atlantis, and reviewer support.
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]]

Enablement still needs staffing and operating ownership. Simon ties ML platform
work to cloud infrastructure, with Kubernetes and Terraform in that skill set.
He also includes on-call and support capacity. He warns against a heavy platform
before there's business value and repeated need. That operating surface is part
of the [[ml-platform-engineer-role=>ML platform engineer role]].
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Fast-growing data platforms need senior people. Mehdi also warns that they need
niche technology experience to establish practices that can survive scale.[[cite:scaling-data-engineering-teams-self-service-platforms=>Self-Service Data Platforms]]

## Stakeholder Buy-In

Internal platform users aren't the only stakeholders. Internal platform
product managers have to balance data scientists and business data engineers.
They also account for compliance, governance, engineering teams, and release
timing. Platform product managers need to know who will adopt a capability and when.
[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Platform Strategy]]

At company scope, the [[chief-data-officer-role=>chief data officer role]] is
the executive owner for this kind of cross-team platform strategy. Marco De Sa
places infrastructure and governance under one data strategy. Analytics, AI,
and product data needs belong there too. That gives adoption work a business
owner above individual platform teams.
[[cite:chief-data-officer-data-strategy-and-org-design=>Mastering the Chief Data Officer Role]]

Platform teams should map the business value path, not only platform users. If
the platform supports ML products, Vin Vashishta's metrics framing pushes the
team to connect usage and task time with decision quality. That's the same
business-value test covered in
[[machine-learning-for-business=>machine learning for business]], where pricing
impact, revenue, and cost savings matter too. A platform capability has
adoption value when it helps product teams ship or operate those
business-facing decisions.
[[cite:make-money-with-machine-learning-roles-skills@75:14=>ML product adoption metrics]]

MLOps buy-in also depends on the business case, KPIs, user story, and
alternatives. Teams may need someone from the business available for demos,
questions, and decisions.

Stakeholder concerns should turn into mitigations and metrics. Demos should
include feared scenarios, not only happy paths.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]

For platform rollout, the same habit applies to migration risks and governance
approvals. It also applies to service levels and incident communication.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]

## Rollout and Power Users

Guests rarely recommend a big-bang platform rollout. Simon favors incremental
platform pieces when a small team can already get value from them. Sometimes
teams can assemble those pieces from SaaS components.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Geo describes internal rollouts through user journeys, governance, and power
users. Data scientists embedded with the platform team can help with
acceleration and demos. Geo also compares them to developer advocates.[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Platform Strategy]]

In Lars's DataOps story, the team embedded with early adopters before enabling
developer teams and non-technical analysts. He describes the move from a
centralized team handling ad hoc requests toward self-service as a long
journey. Analysts may need engineering partners when the organization isn't
ready for pure self-service.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]
That keeps platform adoption grounded in team maturity instead of assuming
every group can use the same level of abstraction on day one. It also keeps the
[[data-mesh-vs-centralized-data-platform=>data mesh vs centralized data
platform]] choice tied to rollout readiness, not only org-chart design.

## Measuring Use and Value

Platform teams should track use, value and trust signals. Raphaël suggests
deployment frequency and impact tracking as KPIs or OKRs. He also warns that
platform teams can lose buy-in if they can't show value.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Geo adds observability metrics and surveys, including internal platform
"happiness" reports. Those reports help the team understand whether users can
work effectively with the platform.[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Platform Strategy]]

Caitlin's last-mile episode adds a useful caution for platform metrics. Teams
can't measure all adoption work directly. She recommends proxies, time studies,
and small measurable wins. Advocates can show that a data product changed a
decision.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

For platforms, the same idea applies to reduced support load and faster
onboarding. It also applies to repeatable deployments, fewer one-off pipelines,
and users choosing the standard path without being forced.

The platform team should also check whether the standard path reaches the last
decision mile. A self-service notebook or registry is only adopted when it
changes how a product team trains or ships a data product. Orchestration
templates and deployment paths need the same test for monitoring and
explanation. If teams still need one-off help, the platform has solved the
tooling layer but not the gap between outputs and decisions.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@13:24=>Last-Mile Data Delivery]]
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack@24:13=>Last-Mile Data Delivery]]

## Failure Modes

Guests warn that a team can build a technically coherent
[[ml-platforms=>ML platform]]
too early. It may not yet have repeated model work or clear business value.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
It can also build self-service without conventions. Users may then break
schemas, invent incompatible pipeline conventions, or depend on reactive support
from the platform team.[[cite:scaling-data-engineering-teams-self-service-platforms=>Self-Service Data Platforms]]

Adoption can also fail socially. A platform team that doesn't understand user
pain may ship the wrong tooling.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
If stakeholders don't trust the data or model, they may avoid using it. The
same risk appears when they don't trust the release process, even when the
system technically works.[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]

If the platform team measures only feature delivery, it can miss whether users
changed behavior or shortened delivery. It can also miss whether they made
better decisions.[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]
