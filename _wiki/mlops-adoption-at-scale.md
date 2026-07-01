---
layout: wiki
title: "MLOps Adoption at Scale"
summary: "How larger organizations get MLOps practices adopted through platform teams, support models, translators, reproducibility, governance, and DataOps-style operations."
related:
  - MLOps
  - ML Platforms
  - Platform Adoption
  - Reproducibility
  - DataOps
  - Platform Engineering
  - CI/CD
  - Model Monitoring
  - Governance
  - Data Governance
  - Production
---

MLOps adoption at scale gets many teams onto a shared path for model
development and production change. It combines
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}), and
[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}). Data
scientists and ML engineers need to use the path in normal delivery work.
Product teams and governance stakeholders need to trust it too
([MLOps at Scale, 23:01-38:44]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes a centralized MLOps team that helps product teams with tooling and
deployment. The same team supports maintenance, monitoring, and best practices
([MLOps at Scale, 23:01-25:20]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }})
shows the regulated finance version, where ML workflows must fit existing
DevOps and approval flows. On-premises platforms and governance also constrain
the path
([MLOps in Finance, 14:57-24:22]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) adds the
[DataOps]({{ '/wiki/dataops/' | relative_url }}) operating lens. Teams need
testing and monitoring after the first model reaches production. They also need
automation and safe deployment paths
([DataOps for Data Engineering, 23:56-30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

## Scaled Operating Model

Teams adopt MLOps at scale when production ML becomes a repeatable practice.
An enabling group can provide CI, repository structure, packaging, and
deployment paths. It can also support monitoring and
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}). The work
still has to fit how product teams build and maintain models
([MLOps at Scale, 31:07-33:13]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

The same path needs enough [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
testing, observability, and automation. New team members should be able to make
changes without putting production at risk
([DataOps for Data Engineering, 26:54-30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Teams adopt at workflow level, not one model at a time. Raphaël talks about
supporting dozens of product teams while ML engineers stay embedded near them
([MLOps at Scale, 23:01-25:20]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
Nemanja describes two or three data scientists working with one ML engineer on
project structure and CI/CD. Deployment and code review stay in the same
collaboration loop
([MLOps in Finance, 14:57-16:24]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).
At scale, the supported path has to become easier than every team inventing its
own release and support approach.

## Adoption Tradeoffs

The guests start from different problems, and Raphaël starts from
[platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}) and
developer experience. His team talks to users, collects pain points, and looks
for quick wins where platform priorities overlap with data-scientist pain
([MLOps at Scale, 32:46-38:44]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja starts from finance constraints. Release management, OpenShift or
on-premises platforms, and internal package registries affect how ML enters
corporate DevOps. Governance rules matter in the same rollout
([MLOps in Finance, 17:55-25:55]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Bergh starts from operating quality. DataOps reduces fear-based work while
lowering errors through automation plus testing. Monitoring and observability
support the same goal
([DataOps for Data Engineering, 11:53-16:10]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Those starting points change the first move, so Raphaël starts with CI/CD when
deployment takes too long. He starts with
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) when
production models are opaque
([MLOps at Scale, 48:41-50:04]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja proposes a minimal viable stack for larger organizations that includes
development, test, and production environments. It also includes an audit trail
and basic monitoring. A model registry, data versioning, and reproducible
pipelines complete his minimum
([MLOps in Finance, 31:57-35:05]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Bergh pushes teams beyond Git and basic CI/CD when testing and tool integration
remain uneven across the team
([DataOps for Data Engineering, 42:39-46:27]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

## Centralized Platform Teams

A centralized MLOps team works best as an enabling layer. Raphaël's team helps
ML engineers define best practices, write design documentation, build reusable
tools, and improve deployment paths. The team also has to stay flexible enough
that product teams don't reject the standards
([MLOps at Scale, 23:01-25:20]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
That makes the team close to an internal
[ML platform]({{ '/wiki/ml-platforms/' | relative_url }}) group. It owns the
paved road, while product teams still own the models and business use cases.

Centralization doesn't remove embedded support. Raphaël describes a centralized
MLOps group alongside ML engineers in product teams
([MLOps at Scale, 25:20]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja's finance example uses direct project support. The ML engineer works
with data scientists on repository structure and CI/CD. Deployment and code
review also happen inside the collaboration, rather than after a handoff
([MLOps in Finance, 16:24 and 42:45]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).
Both models keep platform work close enough to users to find friction early.

## Support and Value

Support at scale begins with listening. Raphaël recommends treating the MLOps
platform like an internal product. The team should talk to data scientists, map
their pain points, and compare those pains with platform priorities. Work
should start where the two overlap
([MLOps at Scale, 32:46-33:13]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

He also warns that pre-commit hooks and type checks can destroy buy-in. Tests
and branch rules cause the same problem when they block work before users see
value
([MLOps at Scale, 36:55-37:32]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Adoption needs visible before-and-after evidence. Raphaël suggests showing
saved deployment time, reduced risk, or less pipeline debugging for data
scientists
([MLOps at Scale, 33:13]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
He also names deployment count through the platform as a simple value signal
([MLOps at Scale, 37:32-38:44]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Bergh adds an operations view. A better process should reduce errors and cycle
time while also reducing rework. Safer deployments are part of the same value
([DataOps for Data Engineering, 16:10 and 34:13-39:09]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

## Technical Leads and Translators

Large organizations need people who can translate, advocate, and guide
technical decisions. Raphaël calls out evangelists who build executive support.
He also calls out tech translators who bridge technical and non-technical
stakeholders, while technical leads bring the MLOps principles
([MLOps at Scale, 16:58-20:33]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Those roles make MLOps legible inside non-IT organizations. Business teams may
otherwise see it as secondary to the main product or operations work
([MLOps at Scale, 18:37-18:54]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

The technical skill mix also matters. Raphaël recommends data science and
software engineering experience inside the MLOps team. SRE or DevOps,
platform engineering, and data engineering experience also help
([MLOps at Scale, 45:10-47:33]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja's finance example narrows that into daily collaboration. Data
scientists bring business-specific modeling work, while the ML engineer makes
APIs repeatable and handles deployment. The same support work covers
authentication and framework accommodation. It also covers modularity and tests
([MLOps in Finance, 41:14-43:39]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

## Traceability and Reproducibility

At scale, [reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) is
less about perfect reruns and more about control over the ML process. Raphaël
says exploratory work can be valuable enough to keep in version control. Mature
teams should link code to data versions. Deployment records add traceability
for reverse-engineering production behavior
([MLOps at Scale, 42:13-44:46]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

The timing depends on context. Data versioning may be overkill for a small
team with a few models. Legal obligations or customer requirements can move it
earlier
([MLOps at Scale, 44:22-44:46]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja gives the regulated version. In finance, the minimal stack includes an
audit-trailed DevOps platform and model registry. It also includes a data
version registry, monitoring, and reproducible pipelines. If a team can't
reproduce or trace what it shipped, it doesn't know what's in production
([MLOps in Finance, 31:57-35:05]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Bergh's DataOps advice takes a different route to traceability by keeping raw
data immutable and versioning the processing logic. Tests and monitoring then
make changes safer
([DataOps for Data Engineering, 54:05-56:17]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

## Regulated Constraints and Tactical Solutions

Large finance organizations often adopt MLOps through existing constraints. Nemanja
describes finance environments with on-premises core systems, OpenShift
clusters, and firewall questions. Internal package registries, approval
chains, and established DevOps governance sit in the same environment
([MLOps in Finance, 16:24-25:55]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).
Release approval gets faster after repeated successful deployments because
governance stakeholders learn to trust the people, code, and process
([MLOps in Finance, 22:25-24:22]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

The finance discussion is pragmatic about tooling. Nemanja treats an S3 bucket
as a valid tactical model registry or data-versioning workaround. The team can
wait for a strategic MLflow solution. Databricks or another vendor-backed
platform can come later
([MLOps in Finance, 34:40-35:05]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Raphaël gives a similar adoption rule for corporate tooling. Start with tools
the organization already has when procurement is slow. Escalate missing version
control because it blocks basic MLOps practice
([MLOps at Scale, 48:41-50:04]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## DataOps Habits for Day Two

MLOps adoption at scale borrows from DataOps once models are live. Bergh
separates day one from later operation because teams need to run systems on new
data as customer needs evolve
([DataOps for Data Engineering, 23:56-24:24]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

For ML teams, day two means models run reliably with new data. Issues should
surface before customers feel them. New team members should be able to make
small changes while tests, monitoring, and automation protect production
([DataOps for Data Engineering, 26:13-30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Those habits keep adoption from becoming a one-time migration. Bergh argues
that teams need more than Git, including end-to-end tests and automated checks
before production. Data engineers, data scientists, and analysts need the same
path rather than isolated pockets
([DataOps for Data Engineering, 42:39-46:27]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Raphaël's component list shows the same operating surface for ML. It includes
version control and CI/CD. Containerization plus model registry sit beside
experiment tracking and monitoring. Compute, serving, and package registry
complete the surface
([MLOps at Scale, 51:21-53:27]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## Keeping Platform Work Tied to Adoption

The repeated warning across the episodes is that platform work can drift away
from users. Raphaël says an MLOps team loses buy-in when it rolls out
engineering controls that don't solve product-team pain. He recommends
measuring platform use and impact while continuing to talk to users
([MLOps at Scale, 36:55-38:44]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Nemanja's project model keeps ML engineers close to data scientists. Code
review and modularity show that support in practice. Tests, framework
accommodation, and production deployment paths do too
([MLOps in Finance, 41:14-43:39]({{ '/podcasts/mlops-and-ml-engineering-in-finance/' | relative_url }})).

Bergh's operating model keeps the focus on whether teams can deploy quickly
with low risk. It also asks whether they can find problems before production
and reduce waste from rework or miscommunication
([DataOps for Data Engineering, 30:55-39:09]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

For adjacent detail, use [MLOps]({{ '/wiki/mlops/' | relative_url }}) for the
production ML lifecycle. Use
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) for shared services
and [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) for
internal product rollout. Use
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) for
rerunnable work and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for the
data-side operating discipline.
