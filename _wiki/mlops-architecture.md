---
layout: article
tags: ["guide"]
title: "MLOps Architecture"
keyword: "mlops architecture"
summary: "MLOps architecture as a component map for data, training, registries, CI/CD, serving, monitoring, and system interfaces."
related_wiki:
  - MLOps
  - MLOps Roadmap
  - MLOps Tools
  - ML Platforms
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Feature Stores
  - Reproducibility
  - DataOps
  - MLOps vs DataOps
  - Governance
---

MLOps architecture is the component and interface map for machine learning in
production. It names data schemas and training records. It also names artifact
promotion and release controls. It names serving runtimes, monitoring signals,
and feedback routes. It's narrower than [[MLOps]] as an operating topic because
architecture work focuses on how the parts connect.

The diagram should show data entering training, training output entering
release, the released version entering serving, and production evidence
returning. Simon Stiebellehner connects experiment tracking and registries to
batch and online serving. He also places orchestration and governance on the
same production map
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@40:57=>Building Production ML Platforms]]).

Use [[MLOps Roadmap]] for sequencing. Use [[MLOps Tools]] for stack choice and
[[MLOps Engineer]] for ownership. [[ML Platforms]] covers reusable services. The
architecture view stays with component boundaries, records, and interfaces.

## Boundary Map

A useful MLOps architecture has two visible routes. The delivery route runs from
source data through training, registry, release, and serving. The return route
runs from production logs and monitoring signals back to investigation, rollback,
feature repair, or retraining approval.

The minimum production boundary can start with existing Git and CI/CD. Maria
Vechtomova adds package registries, a model registry, deployment automation, and
monitoring as the next production interfaces.
[[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]
Tool breadth matters less than handoff clarity. Every handoff needs a named
input, output, owner, and failure route. Use
[[ml-system-design-documents=>ML System Design Documents]] when that boundary
needs review before implementation.

Customer constraints and technical tradeoffs still have to fit the inference
architecture already in place.
[[cite:mlops-model-monitoring-data-observability@10:32=>MLOps Architect Guide]][[cite:mlops-model-monitoring-data-observability@34:25=>MLOps Architect Guide]]
Teams can place automated retraining or data-driven triggers in the same map.
Those paths need explicit approval and rollback routes rather than hidden
scheduler behavior
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[podcast:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).

## Data Inputs and Feature Pipelines

The data side of the diagram starts with input schemas. Name the producer and
consumer for each product event or operational table. Do the same for file
feeds, third-party sources, analytics tables, and label flows. Also name the
arrival cadence, schema expectation, and validation point.

On the data pipeline side, ML pipelines and analytics data pipelines differ.
MLOps separates from DataOps by the kind of production system being operated.
Feature engineering, model training, and serving are ML pipeline steps
([[person:santonatuli=>Santona Tuli]],
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).
[[MLOps vs DataOps]] covers decisions where parts of the system may belong to
[[DataOps]], [[MLOps]], or both.

Feature and training pipelines transform inputs into model-ready data. The
architecture should show where transformation happens, where the result is
stored, which version reaches training, and which version reaches inference. A
small system may use SQL plus a scheduled Python job. A larger one may add
[[orchestration]] and feature-store conventions. Either way, the map must explain
how training and inference stay consistent when batch and online paths coexist.

Make the upstream dependency explicit by tying model problems back to ETL and
data pipelines. Drift and quality belong in the same monitoring view
([[person:dannyleybzon=>Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).
If the monitoring view stops at the endpoint, the team can miss the
source-system or feature-pipeline change that caused the model to fail.

[[person:willempienaar=>Willem Pienaar]] frames feature platforms around
reusable feature definitions while separating transformation systems from
feature retrieval. His Feast and Tecton discussion uses real-time fraud
detection as an example where online feature lookup matters.
[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]
At the architecture boundary, show which system computes a feature and which
system stores it. Then show the serving path and the monitoring view for
freshness or distribution changes. [[Feature Stores]] covers feature-store
selection.

## Training and Experiment Tracking

The training component produces a run record. That record should connect code and
environment to the data reference and parameters. It should also connect
metrics, artifacts, and review decision. As runs accumulate, [[experiment tracking]]
becomes the shared memory of those records.

Experiment tracking replaces spreadsheet run logs with transparent model history.
Metadata and lineage connect to [[reproducibility]], artifacts, and tracking
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

The same requirement broadens to CI, repository structure, parameterization, and
testing. It also covers data versioning plus traceability
([[person:raphaelhoogvliets=>Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
A simple architectural test applies. Another person should be able to locate the
run inputs and rerun or look at the result. They should also understand why the
artifact is eligible or ineligible for promotion.

## Registry and Release Gates

A [[model registry]] is the promotion interface between training and serving. It
stores the artifact and the context needed to deploy or reject it.

At the architecture level, the registry interface should expose model version,
owner, and artifact location. It should also expose training evidence, approval
state, deployment target, and rollback context. [[Model Registry]] owns the full
record structure.

The registry interface doesn't have to be a large platform product on day one.
Artifact stores or MLflow-style alternatives can work when the team preserves
traceability, reproducibility, and versioning
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops@20:49=>Pragmatic MLOps]]).

Registries connect to downstream consumption
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
The registry's architectural job is to turn a training output into a versioned
dependency that another job, service, or team can consume.

## CI/CD, Packaging, and Deployment

The release path should keep code and dependencies together with the model
artifact, configuration, and infrastructure change. CI/CD can test software and
data transformations in that same route. It can also build containers, publish
packages, run deployment checks, and promote between environments. The
[[mlops-vs-devops=>MLOps vs DevOps]] distinction matters here because the same
release path must include software infrastructure and model-release evidence.

Repository templates and service principals make the release boundary explicit.
The diagram should show where notebook logic becomes a package, CI job, or
deployment unit. For the
[[data-scientist-to-machine-learning-engineer=>data scientist to machine learning engineer]]
transition, that box-and-arrow change is the visible handoff
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops@29:55=>Pragmatic MLOps]]
[[cite:pragmatic-and-standardized-mlops@33:24=>Pragmatic MLOps]]).

The release manifest should reference predeployment checks, package or container
locations, the model version that reaches serving, and the rollback target.
[[MLOps Tools]] covers the CI/CD, registry, and deployment-product choices.

## Orchestration and Serving

[[Orchestration]] coordinates dependencies across preparation, training,
evaluation, and deployment. It also coordinates scoring jobs, monitoring jobs,
and retraining candidates. In the architecture, the orchestrator should expose
dependencies and state. It should also expose retries and failure handling. It
shouldn't hide core business logic inside scheduler callbacks.

Batch inference and online serving separate in the architecture
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Batch serving needs an input dataset schema and preprocessing path. It also
needs model version, output location, and schedule. Online serving needs request
and response schemas.

Online serving also needs latency targets, fallback behavior, reliability
expectations, and prediction logging. API and logging design connect to later
monitoring and analytics.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
Without that logging, the service may look available while the model behaves
badly.

A serving interface should show where shared platform reuse ends and
product-specific integration begins. A reusable API convention, logging library,
or deployment template belongs in the architecture only when it defines that
handoff.
[[cite:ml-product-manager-and-mlops-platform-strategy@18:25=>ML Platform Strategy]]

In a Kubernetes-native view, pipeline automation and model serving can sit
beside feature serving. Tuning and metadata components may join that platform
boundary too
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[podcast:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).
[[Metaflow]] fits the same boundary from the practitioner side because it
connects modeling code to cloud resources and scheduler infrastructure.
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]]
Treat those as architecture options, not default requirements.

## Monitoring and Feedback

[[Model monitoring]] is the return interface. It should record software health,
model behavior, and deployment status. It should also record input quality,
feature distributions, and prediction distributions. Drift, label feedback, and
business outcomes should join the same view when they're available.

Monitoring starts from production behavior and model behavior, then ties
observability back to ETL/data pipelines. Summary profiles can support monitoring
without moving every raw row into the monitoring system
([[person:dannyleybzon=>Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).

On the maintenance side, production models need monitoring for data drift and
concept drift. They also need an explicit maintenance path
([[person:thomives=>Thom Ives]],
[[podcast:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering, Model Monitoring, and Data Governance]]).
Avoid automatic retraining until the architecture names the signal, owner, and
comparison rule. It should also name approval state and rollback path.

A drift alert may mean the data pipeline broke. It may also mean the business
changed or the model needs retraining. Monitoring alerts should route evidence
to someone who can choose the right response.

On the human-centered side, live test sets and small A/B tests support
monitoring, alongside root-cause debugging and feedback channels
([[person:linaweichbrodt=>Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]).
A monitoring architecture is stronger when it supports incident response, not
only dashboards.

For the data side of the same problem, see
[[data-quality-and-observability=>Data Observability]] and
[[DataOps]].

## Governance and Lineage

[[Governance]] changes the architecture when models affect customers, regulated
decisions, private data, or important business processes. It changes what the
system logs and who can approve a model. It also changes metadata retention and
later decision reconstruction.

At the architecture level, governance usually means:

- named control points for datasets, model artifacts, services, and alerts
- access control for data, features, artifacts, and logs
- lineage from source data to features, runs, registry entries, and deployments
- visible approval states, retention rules, incident handling, rollback paths,
  and post-incident review practices

Regulatory constraints tie security and compliance to metadata, lineage, and
GDPR implications
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team@42:48=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@45:50=>Building Production ML Platforms]]).
Raphaël Hoogvliets ties data governance to scale practices
([[person:raphaelhoogvliets=>Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
Reusable CI/CD and repository templates make governance easier. Service
principals and deployment standards also reduce one-off paths
([[person:mariavechtomova=>Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]).

Use [[Data Governance]], [[Responsible AI and Governance]], and
[[Privacy Engineering for ML]] for the policy-specific parts that sit behind
those control points.

## Local or Shared System Boundaries

A small MLOps architecture can keep components local to one model. Code
versioning and scheduled training can stay local. Run tracking and object
storage can stay local too. One deployment target, prediction logs, and a basic
monitoring view can stay local too. The diagram still needs explicit interfaces
between data and training, promotion and serving, plus monitoring and repair.

A shared platform changes the map when several teams depend on the same
interfaces. Templates and self-service compute can become shared services.
Tracking, registry integration, and deployment paths can become shared too.
Logging schemas, monitoring hooks, and support routes may follow.

The architecture should state which interface is shared and what schema, API, or
record it exposes.
[[ML Platforms]] covers the internal-product and adoption side of that
decision. [[ml-platform-engineer-role=>ML Platform Engineer Role]] covers the
engineer who turns repeated interfaces into supported shared services.

Nadia Nahar's team-structure cases add a social architecture layer. An MLOps
platform may need to support API handoffs and ML-engineer bridge roles. Small
mixed teams can need different support from a centralized deployment path.
[[cite:software-engineering-for-machine-learning@36:28=>Software Engineering for ML]]

Keep the architecture focused on the boundary by naming the data or artifact
that crosses it. When identity, approval, or signal is the handoff, name that
too. Then name which downstream service depends on that interface.
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]][[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

The smallest durable component map is better than a platform diagram full of
unused boxes. [[MLOps Roadmap]] covers when to add shared components.

## Interface Checks

An architecture map should cover production interfaces, governance controls, and
the monitoring-to-data-pipeline boundary.
[[cite:building-production-ml-platform-and-mlops-team@21:57=>Production ML Platforms]][[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]][[cite:mlops-at-scale-reproducibility-adoption@42:54=>MLOps at Scale]][[cite:mlops-model-monitoring-data-observability@27:35=>MLOps Architect Guide]]

Before adding another box, check whether the current map covers these points:

- Each data input, feature pipeline, training job, model artifact, service, and
  alert has an owner.
- Training records point to code, data references, parameters, metrics, and
  model artifacts.
- The registry or promotion convention exposes approval state, deployment
  target, and rollback context.
- CI/CD connects code, dependencies, model artifact, configuration, and
  infrastructure.
- Serving paths name batch jobs, online endpoints, edge targets, or hybrid
  routes separately.
- Logs connect predictions to model version, input schema, and serving context.
- Monitoring signals route to investigation, rollback, retraining, or product
  change.
- Governance, lineage, access, retention, and incident practices appear on the
  same map as the model path.
- Repeated interfaces are the only ones promoted into shared services.

Good MLOps architecture is the smallest production map that makes those
interfaces explicit enough to reproduce a model and deploy it safely. The same
map should let the team observe what changed after release and choose rollback,
repair, retraining, or retirement from evidence.
