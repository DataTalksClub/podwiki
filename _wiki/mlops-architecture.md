---
layout: article
tags: ["guide"]
title: "MLOps Architecture: Production Map for Models, Pipelines, Platforms, and Feedback"
keyword: "mlops architecture"
summary: "A podcast-backed MLOps architecture guide covering data inputs, training and feature pipelines, experiment tracking, registries, CI/CD, serving, monitoring, feedback loops, governance, and the tradeoff between simple stacks and shared platforms."
related_wiki:
  - MLOps
  - MLOps Roadmap
  - ML Platforms
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Reproducibility
  - DataOps
  - Governance
---

MLOps architecture is the production map for data, training, deployment, and
model improvement. It should show how a model moves from raw inputs to
predictions. It should also show how teams reproduce and approve the model,
monitor what happens after release, and route production evidence back into the
next decision.

This architecture is a production operating system for machine learning work,
not a vendor diagram. MLOps rests on people, process, and technology, and
experiment tracking and registries connect to batch inference, online serving,
and orchestration
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Operationally, a useful stack starts with version control and CI/CD, with
registries, a model registry, and monitoring following before the work becomes a
large platform program
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

For the broader discipline, start with
[[MLOps]]. Use
[[MLOps Roadmap]] for build order,
[[ML Platforms]] for the shared
platform layer, and [[MLOps Tools]]
for stack selection.

## Architecture Flow

A practical MLOps architecture has one forward path and one return path.

The forward path starts with data inputs. Source systems feed ingestion and
transformation jobs, which create features or training datasets. A training
pipeline uses that data, records metrics, and stores a model artifact.

A registry or registry-like convention promotes the artifact into a deployable
model. CI/CD then packages the code, dependencies, and serving configuration.
The deployment target may be a batch scoring job, an online endpoint, an edge
deployment, or a hybrid setup.

The return path starts when production evidence contradicts training-time
assumptions. Drift and missing inputs can send the team back to investigation.
Schema changes, latency, and errors can do the same. The team may fix data,
change features, roll back, or retrain. It may also update the product workflow.

This is a maturity progression: manual training gives way to pipeline
automation, then data-driven triggers, automated retraining, and monitoring as a
source of new training data
([[person:theofilospapapanagiotou|Theofilos Papapanagiotou]],
[[podcast:mlops-kubeflow-model-monitoring|Mastering MLOps]]).
The return path explains how a deployed model keeps learning from the world
without hiding responsibility behind automation.

## Data Inputs and Feature Pipelines

MLOps architecture starts before the model. Data inputs may come from product
events and operational databases. They may also come from files, third-party
feeds, analytics tables, or human labels. The architecture should name the owner,
arrival cadence, schema expectation, and validation point for each source.

On the data pipeline side, ML pipelines and analytics data pipelines differ, and
MLOps separates from DataOps by the kind of production system being operated;
feature engineering, model training, and serving are ML pipeline steps
([[person:santonatuli|Santona Tuli]],
[[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).
Use those boundaries when deciding which parts of the system belong to
[[DataOps]], [[MLOps]], or both.

Feature and training pipelines transform inputs into model-ready data. In a
small architecture, that may be SQL plus a scheduled Python job. In a larger
architecture, the team may add
[[orchestration]] and feature-store
conventions. Validation checks and lineage often follow.

The important question isn't whether the diagram includes a feature store. The
team needs to explain how training data and inference data
stay consistent enough for the use case, especially when batch and online paths
coexist.

The upstream dependency is explicit: model problems tie back to ETL and data
pipelines, and drift and quality belong in the same monitoring view
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).
If the monitoring view stops at the endpoint, the team can miss the
source-system or feature-pipeline change that caused the model to fail.

## Training and Experiment Tracking

Training architecture connects code and data to parameters, metrics, artifacts,
and review decisions. At minimum, the team needs a reproducible environment and
version control. It also needs a data reference, saved metrics, and an artifact
location. Once several people compare runs,
[[experiment tracking]] becomes
the shared memory of the system.

Experiment tracking is a low-hanging platform win — a move away from spreadsheet
run logs toward transparent model history — and metadata and lineage connect to
[[reproducibility]], artifacts, and tracking
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

The same requirement broadens to CI and repository structure, plus
parameterization, testing, data versioning, and traceability
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
A team shouldn't treat training output as production-ready until another person
can reproduce it and understand the evidence behind it.

## Registry and Release Gates

A [[model registry]] is the handoff
point between training and production. It stores the artifact and the context
needed to deploy it safely.

A useful registry record includes:

- model version and owner
- artifact location and code version
- training-data reference and evaluation result
- approval state and deployment target
- rollback note

The registry doesn't have to be a large platform product on day one. Registry
choices include artifact stores and MLflow-style alternatives, and for early
teams reproducibility, versioning, and traceability come ahead of more elaborate
tooling
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

For a small team, object storage plus a structured promotion convention may be
enough if everyone follows the same rule. For a larger or regulated team, access
control and lineage become harder to avoid. Approval history and
deployment-system integration usually follow.

Registries connect to downstream consumption
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
The registry's architectural job is to turn a training output into a model
another job, service, or team can depend on.

## CI/CD, Packaging, and Deployment

CI/CD in MLOps should cover ordinary software checks and model-specific checks.
The pipeline may test code and validate data transformations. It may also build
containers, publish packages, run deployment checks, and promote changes between
environments. The architecture should show how code and model artifacts move
together. Configuration and infrastructure should move with them.

A concrete component set covers version control, CI/CD, and containerization,
model registry, experiment tracking, and monitoring, plus compute, serving, and
package registry
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).

Standardization work includes cookie-cutter repositories, service principals,
Databricks workflows, and moving logic out of notebooks into packages and CI/CD
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

The startup version is a minimal stack with Python, CI/CD orchestration, and
Dagster; managed services can accelerate a young team while creating migration
and lock-in tradeoffs
([[person:nemanjaradojkovic|Nemanja Radojkovic]],
[[podcast:lean-mlops-for-startups|Lean MLOps for Startups]]).
That matters for [[MLOps]]: the simplest repeatable release path usually beats a
broad platform that the team can't yet operate.

## Orchestration and Serving

[[Orchestration]] coordinates the
workflow across data preparation, training, evaluation, and deployment. It may
also coordinate batch scoring, monitoring jobs, and retraining. The orchestrator
should describe dependencies and failure handling. It shouldn't hide core
business logic inside scheduler callbacks.

Batch inference and online serving separate in the architecture
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Batch serving looks similar to training: a job loads data, preprocesses it, runs
inference, and stores output.

Online serving changes the architecture because the team must care about request
schemas and response schemas. Latency, fallbacks, and service reliability become
part of the design too. API and logging design connect to later monitoring and
analytics
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Without that logging, the service may look available while the model behaves
badly.

In a Kubernetes-native view, Kubeflow Pipelines and KFServing appear as
production options, along with Feast, Katib, and TFX-style orchestration
([[person:theofilospapapanagiotou|Theofilos Papapanagiotou]],
[[podcast:mlops-kubeflow-model-monitoring|Mastering MLOps]]).
Treat those as architecture options, not default requirements. Use them when the
team needs pipeline automation, model serving, metadata, or platform integration
at that level of complexity.

## Monitoring and Feedback

[[Model monitoring]] should watch
software health and model behavior. Service health, latency, errors, and
resource use show whether the serving path works. Deployment status belongs in
that same view. Input quality and feature distributions show whether production
data still resembles the expected data. Prediction distributions, drift, label
feedback, and business outcomes show whether the model still fits the world.

Monitoring is production-first, focused on production and model monitoring,
tying observability back to ETL and data pipelines; profiling architecture and
summary profiles can support monitoring without moving every raw row into the
monitoring system
([[person:dannyleybzon|Danny Leybzon]],
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]]).

On the maintenance side, production models need monitoring for data drift,
concept drift, and maintenance
([[person:thomives|Thom Ives]],
[[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering, Model Monitoring, and Data Governance]]).
The practical release rule is to avoid automatic retraining until the
architecture names the trigger, owner, and approval path.

A drift alert may mean the data pipeline broke. It may also mean the business
changed or the model needs retraining. The feedback loop should route evidence
to someone who can choose the right response.



On the human-centered side, live test sets and small A/B tests support
monitoring, alongside root-cause debugging and feedback channels
([[person:linaweichbrodt|Lina Weichbrodt]],
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps]]).
A monitoring architecture is stronger when it supports incident response, not
only dashboards.

For the data side of the same problem, see
[[data-quality-and-observability|Data Observability]] and
[[DataOps]].

## Governance, Lineage, and Ownership

[[Governance]] belongs in the
architecture when models affect customers, regulated decisions, private data, or
important business processes. It changes what teams log and who can approve a
model. It also changes how long metadata lives and how a team explains a
decision later.

At the architecture level, governance usually means:

- named owners for datasets, model artifacts, services, and alerts
- access control for data, features, artifacts, and logs
- lineage from source data to features, runs, registry entries, and deployments
- visible approval states, retention rules, incident handling, rollback paths,
  and post-incident review practices

Regulatory constraints tie security and compliance to metadata, lineage, and
GDPR implications
([[person:simonstiebellehner|Simon Stiebellehner]],
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
Data governance is also a maturity concern
([[person:raphaelhoogvliets|Raphaël Hoogvliets]],
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]]).
Reusable CI/CD, repository templates, service principals, and deployment
standards make governance easier because they reduce one-off paths
([[person:mariavechtomova|Maria Vechtomova]],
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

For adjacent pages, use
[[Data Governance]],
[[Responsible AI and Governance]],
and [[Privacy Engineering for ML]].

## Feature Platforms

Feature platforms manage the data used by models. A feature store can provide
offline training data and online low-latency feature serving. It can also
provide point-in-time correctness, feature reuse, feature definitions, and
monitoring around feature freshness or distributions.

[[person:willempienaar|Willem Pienaar]] defines the
core problem around 6:30 in
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]].
He then separates transformations and retrieval between 11:00 and 14:30. He
also covers on-demand computation. Around 16:30, he uses real-time fraud
detection to show why online feature lookup matters.

Around 36:30, he breaks the platform into a transform engine and storage.
Serving, registry, and monitoring complete that architecture.

Use a feature platform when teams repeatedly rebuild the same features or
struggle with training-serving skew. It also helps when teams need
low-latency online features or a shared way to publish feature semantics and
ownership. Avoid it when simple batch scoring, warehouse tables, dbt models,
and validation checks already solve the problem. Willem makes that boundary
explicit around 40:00, where the episode distinguishes online tabular use cases
from overkill scenarios.

## Simple Stack or Shared Platform

Start with a reproducible path for one model. A small architecture can use Git
and a scheduled training job. Add an experiment tracker, object storage, and a
registry convention. One deployment path and prediction logs come next. Add a
basic monitoring view after that.

That's often enough for a startup or a prototype moving into production. It can
also be enough for a team with one important model.

A shared platform makes sense when several teams repeat the same work. Then the
organization benefits from shared templates and self-service compute. Standard
tracking and registry integration become shared assets. Deployment paths,
logging schemas, and monitoring hooks do too. Documentation and support become
part of the platform.

Simon and Raphaël are consistent on this tradeoff. Simon warns against heavy platform
investment before model value exists around 47:08 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Around 49:19, he favors building minimal platform pieces alongside real use.

Raphaël frames a centralized MLOps team as an enabling layer in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
In that discussion, adoption depends on feedback loops and quick wins. Developer
experience matters because adoption is part of the architecture.

Nemanja adds the startup constraint in
[[podcast:lean-mlops-for-startups|Lean MLOps for Startups]].
Use managed tools when they buy speed. Keep an eye on lock-in, technical debt,
security, and future portability.

Use [[Platform Adoption]],
[[Developer Experience]], and
[[MLOps Architecture]] when the
main risk is whether teams will use the architecture.

## Choosing a Framework Sequence

Start from the failure mode instead of the framework name.

1. If experiments can't be recovered, add tracking, artifact storage, data
   references, and dependency discipline.
2. If models can't be handed off, add a registry convention and one deployment
   path.
3. If training or batch inference is hard to coordinate, add orchestration.
4. If serving is fragile, standardize packaging, validation, logging, and
   rollback.
5. If production behavior is invisible, add monitoring and connect it to data
   observability.
6. If features are duplicated or inconsistent, evaluate a feature platform.
7. If every project repeats the same setup, create templates and CI/CD
   workflows.
8. If the organization is regulated or high-risk, add governance metadata,
   approvals, lineage, and audit trails early.

[[person:geojolly|Geo Jolly]] adds the product lens in
[[podcast:ml-product-manager-and-mlops-platform-strategy|ML Product Manager and MLOps Platform Strategy]].
Around 8:41, the episode discusses in-house MLOps platform strategy and vendor
evaluation. Around 18:25, it connects observability and KPIs to platform impact.
Use that as the standard for framework selection. Choose tools and conventions
that make teams faster, safer, and more measurable.

Build toward a platform only after repeated work or operational risk justifies
it. Use the smallest framework the team can apply consistently while still
shipping and maintaining reliable models.

## Architecture Checklist

Before adding another platform component, check whether the current architecture
covers these points:

- Each data input, feature pipeline, training job, model artifact, service, and
  alert has an owner.
- The team can reproduce the model from code, data reference, parameters,
  metrics, and artifact.
- The artifact has a promotion path, approval state, and rollback option.
- CI/CD tests, packages, and deploys the model path repeatably.
- Serving covers the batch jobs, online endpoints, edge targets, or hybrid path
  the product actually uses.
- Logs connect each prediction to a model version, input schema, and serving
  context.
- Monitoring signals trigger investigation, rollback, retraining, or product
  change.
- Governance, lineage, access, retention, and incident practices are visible in
  the architecture.
- Repeated work stays local only when that flexibility is useful.

Good MLOps architecture isn't the largest diagram. It's the smallest production
map that lets a team reproduce a model and deploy it safely. It also lets the
team observe what changes after release, then improve or retire the model when
the evidence demands it.

