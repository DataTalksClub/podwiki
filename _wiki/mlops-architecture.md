---
layout: article
tags: ["guide"]
title: "MLOps Architecture"
keyword: "mlops architecture"
summary: "Guide to MLOps architecture across data, pipelines, registries, CI/CD, serving, monitoring, and feedback loops."
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

MLOps architecture is the system map for machine learning in production. It
shows the data inputs and feature or training pipelines. It also shows
experiment tracking, artifact storage, and registry handoff. Deployment
targets, monitoring signals, and feedback paths connect the same model
lifecycle.

Use the architecture as a component-and-boundary design, not as a vendor
diagram. The design should name how artifacts move, where approvals happen,
which runtime serves predictions, and how production evidence reaches the next
model decision. Experiment tracking and registries connect to batch inference,
online serving, and orchestration
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]).

When people ask for MLOps frameworks or an MLOps architecture diagram, answer
with this operating map. The diagram should show the forward path from data to
serving and the return path from monitoring to investigation, rollback, or
retraining. Use [[MLOps Engineer]] for role ownership and [[MLOps Roadmap]] for
the learning and rollout sequence. Use [[ML Platforms]] for the shared platform
layer and [[MLOps Tools]] for stack selection after the boundaries are clear.

## Reference Architecture Boundaries

Across these interviews, an MLOps framework is less a named methodology and
more a set of connected boundaries. It has to connect lifecycle stages, shared
platform capabilities, and adoption work without hiding who owns each handoff.

Simon's platform discussion follows the data scientist workflow. Around that
workflow, teams add experiment tracking and a model registry. They also connect
serving, orchestration, and governance
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@40:57=>Building Production ML Platforms]]).
Maria's pragmatic version starts from existing Git and CI/CD. Her minimum stack
also needs package registries, model registry, deployment, and monitoring before
the team chases a larger platform
([[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]).

For an MLOps architect, those boundaries become design checks. The architect
checks whether the team can reproduce training and whether an artifact can
reach deployment. They also check whether serving is observable and whether
every feedback signal has an owner.

Danny Leybzon describes the architect role as a bridge between customer
constraints, business priorities, and technical tradeoffs. Monitoring and data
observability still have to fit the existing inference architecture
([[cite:mlops-model-monitoring-data-observability@10:32=>MLOps Architect Guide]]
[[cite:mlops-model-monitoring-data-observability@34:25=>MLOps Architect Guide]]).

Use [[MLOps Roadmap]] for sequence, [[ML Platforms]] for shared infrastructure
choices, and [[MLOps Engineer]] for day-to-day ownership of each boundary.

## Architecture Flow

A practical MLOps architecture has one forward path and one return path. Draw
that operating flow first. It forces the team to connect the data-to-training
path with registry and release. It also connects serving, monitoring, and
feedback before the team chooses tools.

The forward path starts with data inputs. Source systems feed ingestion and
transformation jobs, which create features or training datasets. A training
pipeline uses that data, records metrics, and stores a model artifact.

Simon describes this as a data-science workflow that starts with pulling data.
Teams then explore and train. They evaluate, track experiments, and persist a
model for downstream use
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]).

A registry or registry-like convention promotes the artifact into a deployable
model. CI/CD then packages the code, dependencies, and serving configuration.
The deployment target may be a batch scoring job, an online endpoint, an edge
deployment, or a hybrid setup.

The return path starts when production evidence contradicts training-time
assumptions. Drift and missing inputs can send the team back to investigation.
Schema changes, latency, and errors can do the same. The team may fix data,
change features, roll back, or retrain. It may also update the product workflow.

Teams usually mature from manual training to pipeline automation. Later they add
data-driven triggers, automated retraining, and monitoring as a source of new
training data
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).
The return path explains how a deployed model keeps learning from the world
without hiding responsibility behind automation.

## Data Inputs and Feature Pipelines

MLOps architecture starts before the model. Data inputs may come from product
events and operational databases. They may also come from files, third-party
feeds, analytics tables, or human labels. The architecture should name the owner,
arrival cadence, schema expectation, and validation point for each source.

On the data pipeline side, ML pipelines and analytics data pipelines differ.
MLOps separates from DataOps by the kind of production system being operated.
Feature engineering, model training, and serving are ML pipeline steps
([[person:santonatuli=>Santona Tuli]],
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).
Use those boundaries when deciding which parts of the system belong to
[[DataOps]], [[MLOps]], or both.

Feature and training pipelines transform inputs into model-ready data. In a
small architecture, that may be SQL plus a scheduled Python job. In a larger
architecture, the team may add
[[orchestration]] and feature-store
conventions. Validation checks and lineage often follow.

The important question isn't whether the diagram includes a feature store. The
team needs to explain how training data and inference data stay consistent
enough for the use case, especially when batch and online paths coexist. Use
[[MLOps Tools]] to compare feature-store and orchestration options only after
that path is clear.

Make the upstream dependency explicit by tying model problems back to ETL and
data pipelines. Drift and quality belong in the same monitoring view
([[person:dannyleybzon=>Danny Leybzon]],
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).
If the monitoring view stops at the endpoint, the team can miss the
source-system or feature-pipeline change that caused the model to fail.

## Training and Experiment Tracking

Training architecture connects code and data to parameters, metrics, artifacts,
and review decisions. At minimum, the team needs a reproducible environment and
version control. It also needs a data reference, saved metrics, and an artifact
location. Once several people compare runs,
[[experiment tracking]] becomes
the shared memory of the system.

Experiment tracking is one of the easier platform wins. Teams move away from
spreadsheet run logs toward transparent model history. Metadata and lineage
connect to [[reproducibility]], artifacts, and tracking
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

The same requirement broadens to CI, repository structure, parameterization, and
testing. It also covers data versioning plus traceability
([[person:raphaelhoogvliets=>Raphaël Hoogvliets]],
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
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

The registry doesn't have to be a large platform product on day one. Early teams
can choose artifact stores or MLflow-style alternatives. Maria describes
Artifactory, S3, and similar stores as workable registry patterns when the team
preserves traceability and reproducibility. Reproducibility, versioning, and
traceability come ahead of more elaborate tooling
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops@20:49=>Pragmatic MLOps]]).

For a small team, object storage plus a structured promotion convention may be
enough if everyone follows the same rule. For a larger or regulated team, access
control and lineage become harder to avoid. Approval history and
deployment-system integration usually follow.

Registries connect to downstream consumption
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
The registry's architectural job is to turn a training output into a model
another job, service, or team can depend on.

## CI/CD, Packaging, and Deployment

CI/CD in MLOps should cover ordinary software checks and model-specific checks.
The pipeline may test code and validate data transformations. It may also build
containers, publish packages, run deployment checks, and promote changes between
environments. The architecture should show how code and model artifacts move
together. Configuration and infrastructure should move with them.

A concrete component set covers version control and CI/CD. Containerization,
model registry, and experiment tracking are part of it too. Monitoring and
compute sit beside serving and package registry
([[person:raphaelhoogvliets=>Raphaël Hoogvliets]],
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

Standardization work includes cookie-cutter repositories and service principals.
It also includes Databricks workflows and moving logic out of notebooks into
packages and CI/CD
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops@29:55=>Pragmatic MLOps]]
[[cite:pragmatic-and-standardized-mlops@33:24=>Pragmatic MLOps]]).

Early teams can keep the release path small and managed while still accounting
for migration and lock-in tradeoffs
([[person:nemanjaradojkovic=>Nemanja Radojkovic]],
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]).
That matters for [[MLOps]]: the simplest repeatable release path usually beats a
broad platform that the team can't yet operate.

For an MLOps architect, this section maps the release path. It should show
predeployment checks and package or container locations. It should also show
how the model version reaches serving and how the team rolls back. Maria's
minimum stack starts with version control and CI/CD. It also
includes Docker or package registries, model registry, deployment, and
monitoring
([[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]).

## Orchestration and Serving

[[Orchestration]] coordinates the
workflow across data preparation, training, evaluation, and deployment. It may
also coordinate batch scoring, monitoring jobs, and retraining. The orchestrator
should describe dependencies and failure handling. It shouldn't hide core
business logic inside scheduler callbacks.

Batch inference and online serving separate in the architecture
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Batch serving looks similar to training. A job loads data, preprocesses it, runs
inference, and stores output.

Online serving changes the architecture because the team must care about request
schemas and response schemas. Latency, fallbacks, and service reliability become
part of the design too. API and logging design connect to later monitoring and
analytics
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
Without that logging, the service may look available while the model behaves
badly.

Serving also decides where platform reuse ends and product ownership begins.
Geo Jolly's platform discussion separates an in-house ML platform from vendor
capabilities that are integrated only when they fit requirements. The platform
team still measures whether data scientists can productionize models faster
([[cite:ml-product-manager-and-mlops-platform-strategy@6:36=>ML Platform Strategy]]
[[cite:ml-product-manager-and-mlops-platform-strategy@8:41=>ML Platform Strategy]]
[[cite:ml-product-manager-and-mlops-platform-strategy@18:25=>ML Platform Strategy]]).
That makes [[Platform Adoption]] and [[Developer Experience]] part of the
serving architecture. A reusable API convention, logging library, or deployment
template only matters when teams actually adopt it.

In a Kubernetes-native view, pipeline automation and model serving can sit
beside feature serving. Tuning and metadata components may join that platform
boundary too
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).
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

Monitoring starts from production behavior and model behavior, then ties
observability back to ETL/data pipelines. Summary profiles can support monitoring
without moving every raw row into the monitoring system
([[person:dannyleybzon=>Danny Leybzon]],
[[cite:mlops-model-monitoring-data-observability=>MLOps Architect Guide]]).

On the maintenance side, production models need monitoring for data drift and
concept drift. They also need an explicit maintenance path
([[person:thomives=>Thom Ives]],
[[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering, Model Monitoring, and Data Governance]]).
The practical release rule is to avoid automatic retraining until the
architecture names the trigger, owner, and approval path.

A drift alert may mean the data pipeline broke. It may also mean the business
changed or the model needs retraining. The feedback loop should route evidence
to someone who can choose the right response.

On the human-centered side, live test sets and small A/B tests support
monitoring, alongside root-cause debugging and feedback channels
([[person:linaweichbrodt=>Lina Weichbrodt]],
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]]).
A monitoring architecture is stronger when it supports incident response, not
only dashboards.

For the data side of the same problem, see
[[data-quality-and-observability=>Data Observability]] and
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
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team@42:48=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@45:50=>Building Production ML Platforms]]).
Data governance is also a maturity concern
([[person:raphaelhoogvliets=>Raphaël Hoogvliets]],
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).
Reusable CI/CD and repository templates make governance easier. Service
principals and deployment standards also reduce one-off paths
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]).

For adjacent pages, use
[[Data Governance]],
[[Responsible AI and Governance]],
and [[Privacy Engineering for ML]].

## Feature Platforms

Feature platforms manage the data used by models. A feature store can provide
offline training data and online low-latency feature serving. It can also
provide point-in-time correctness, feature reuse, feature definitions, and
monitoring around feature freshness or distributions.

[[person:willempienaar=>Willem Pienaar]] frames feature platforms around
reusable feature definitions and separates transformation systems from feature
retrieval. His Feast and Tecton discussion uses real-time fraud detection as
the example. Some use cases need online feature lookup rather than only batch
tables
([[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]).

He separates transformation and storage from the serving layer, while registry
and monitoring responsibilities complete the platform boundary. That split keeps
the feature platform connected to the wider MLOps architecture instead of turning
it into a separate data product.

Use a feature platform when teams repeatedly rebuild the same features or
struggle with training-serving skew. It also helps when teams need
low-latency online features or a shared way to publish feature semantics and
ownership. Avoid it when simple batch scoring, warehouse tables, dbt models,
and validation checks already solve the problem. Willem makes that boundary
explicit by distinguishing online tabular use cases from overkill scenarios
([[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]).

## Local Stack or Shared Platform

A small MLOps architecture can keep components local to one model. Code
versioning, scheduled training, run tracking, and object storage can stay local
at first. One deployment target, prediction logs, and a basic monitoring view
can stay local too.

For the order to add those pieces, use [[MLOps Roadmap]]. For architecture
design, decide which components are local to one model and which become shared
services.

A local stack is often enough for a startup or a prototype moving into
production. It can also fit a team with one important model. It still needs
explicit interfaces between data and training. It also needs interfaces between
registry, serving, monitoring, and repair.

A shared platform makes sense when several teams repeat the same components.
Templates and self-service compute become shared assets. Standard tracking,
registry integration, deployment paths, and logging schemas do too. Monitoring
hooks, documentation, and support routes become part of the shared platform.

Nadia Nahar's team-structure cases add a social architecture layer. An MLOps
platform may need to support API handoffs and ML-engineer bridge roles. Small
mixed teams can need different support from a centralized deployment path
([[cite:software-engineering-for-machine-learning@36:28=>Software Engineering for ML]]).

[[ML Platforms]] covers the internal-product side of that
decision.

Simon and Raphaël are consistent on this tradeoff. Simon warns against heavy
platform investment before model value exists. He favors building minimal
platform pieces alongside real use
([[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).

Raphaël frames a centralized MLOps team as an enabling layer in
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]].
In that discussion, adoption depends on feedback loops and quick wins. Developer
experience matters because adoption is part of the architecture.

Nemanja adds the startup constraint in
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].
Use managed tools when they buy speed. Keep an eye on lock-in, technical debt,
security, and future portability. [[MLOps Tools]] owns the detailed stack
selection question.

Use [[Platform Adoption]] and [[Developer Experience]] when the main risk is
whether teams will use the architecture.

Teams should change the component design by company stage. In a startup,
Nemanja Radojkovic argues for cloud and SaaS-first choices when they help a
small team move quickly. The same team still has to watch portability and
technical debt
([[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]).

In a regulated finance setting, the same architecture needs dev/test/prod
separation and release controls earlier. It also needs monitoring, model
registry, data versioning, and reproducible pipelines
([[cite:mlops-and-ml-engineering-in-finance=>MLOps in Finance]]).
The architecture should expose that context instead of pretending one component
map fits every organization.

## Design Checks by Failure Mode

Use failure modes to test the architecture. For the order to learn or roll out
fixes, use [[MLOps Roadmap]]. In the architecture, each failure shows a missing
component or boundary.

1. Experiments can't be recovered: the architecture needs tracking, artifact
   storage, data references, and dependency discipline
   [[cite:building-production-ml-platform-and-mlops-team@29:41=>Production ML Platforms]].
2. Models can't be handed off: it needs a [[model registry]] convention and one
   deployment path
   [[cite:building-production-ml-platform-and-mlops-team@30:32=>Production ML Platforms]].
3. Training or batch inference is hard to coordinate: it needs orchestration
   with visible dependencies
   [[cite:building-production-ml-platform-and-mlops-team@31:51=>Production ML Platforms]].
4. Serving is fragile: it needs packaging, validation, logging, and rollback
   boundaries
   [[cite:pragmatic-and-standardized-mlops@29:55=>Pragmatic MLOps]].
5. Production behavior is invisible: it needs [[Model Monitoring]] connected to
   data observability
   [[cite:mlops-model-monitoring-data-observability@27:35=>MLOps Architect Guide]].
6. Features are duplicated or inconsistent: it may need a feature platform
   [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]].
7. Every project repeats the same setup: it may need shared templates and CI/CD
   workflows
   [[cite:pragmatic-and-standardized-mlops@29:55=>Pragmatic MLOps]].
8. The organization is regulated or high-risk: it needs governance metadata,
   approvals, lineage, and audit trails early
   [[cite:building-production-ml-platform-and-mlops-team@40:57=>Production ML Platforms]].

[[person:geojolly=>Geo Jolly]] adds the product lens in
[[cite:ml-product-manager-and-mlops-platform-strategy=>ML Product Manager and MLOps Platform Strategy]].
The episode connects in-house platform strategy and vendor evaluation to
observability and KPIs. Use that as the standard for component selection.
Choose tools and conventions that make teams faster, safer, and more
measurable.

Build toward a platform only after repeated work or operational risk justifies
it. Simon's build-versus-buy discussion puts the burden on integration and
workflow fit, even when the team buys an end-to-end platform
([[cite:building-production-ml-platform-and-mlops-team@17:14=>Build vs Buy ML Platforms]]).
Use the smallest component map the team can apply consistently while still
shipping and maintaining reliable models.

## Architecture Checklist

This checklist combines Simon's lifecycle and governance flow with Maria's
minimum standardized stack. It also uses Raphaël's reproducibility and adoption
work and Danny's monitoring-to-data-pipeline boundary
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Production ML Platforms]]
[[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]
[[cite:mlops-at-scale-reproducibility-adoption@42:54=>MLOps at Scale]]
[[cite:mlops-model-monitoring-data-observability@27:35=>MLOps Architect Guide]]).

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
map that lets a team reproduce a model, deploy it safely, and observe what
changes after release. It also gives the team a practical structure for
improving, rolling back, or retiring the model when the evidence demands it.
