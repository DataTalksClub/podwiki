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

MLOps architecture is the component map for machine learning in production. It
shows the data interfaces, training path, and artifact handoff. It also shows
the release boundary, serving target, monitoring signals, and feedback path.
Architecture work names where those components meet, not who staffs them or
which product to buy.

The map should name how artifacts move, where approvals happen, which runtime
serves predictions, and how production evidence reaches the next model
decision. Experiment tracking and registries connect to batch inference, online
serving, and orchestration
([[person:simonstiebellehner=>Simon Stiebellehner]],
[[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]).

MLOps architecture names the system structure across interfaces, handoffs, and
feedback loops. Role accountability belongs with [[MLOps Engineer]], learning
and rollout sequence belong with [[MLOps Roadmap]], and stack selection belongs
with [[MLOps Tools]]. Internal platform adoption belongs with [[ML Platforms]].

An architecture diagram should show the forward path from data to serving and
the return path from monitoring to investigation, rollback, or retraining.

## Production Boundaries

An MLOps architecture connects lifecycle stages through explicit interfaces, so
the boundary matters more than the framework name.

The data-scientist workflow needs experiment tracking and a model registry
around it. Serving, orchestration, and governance connect to the same map
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]
[[cite:building-production-ml-platform-and-mlops-team@40:57=>Building Production ML Platforms]]).
Existing Git and CI/CD can anchor the first release boundary. Package registries,
model registry, deployment, and monitoring then define the minimum production
route
([[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]).

The architecture needs reproducible training, an approved artifact path to
deployment, observable serving, and routed feedback signals. Customer constraints,
business priorities, and technical tradeoffs still have to fit the existing
inference architecture
([[cite:mlops-model-monitoring-data-observability@10:32=>MLOps Architect Guide]]
[[cite:mlops-model-monitoring-data-observability@34:25=>MLOps Architect Guide]]).

[[ML Platforms]] covers shared infrastructure choices. [[MLOps Engineer]]
covers day-to-day ownership, and [[MLOps Roadmap]] covers rollout sequence.

## Architecture Flow

A practical MLOps architecture has one forward path and one return path. Draw
that operating flow first. It forces the team to connect the data-to-training
path with registry and release. It also connects serving, monitoring, and
feedback before the team chooses tools.

The forward path starts with data inputs. Source systems feed ingestion and
transformation jobs, which create features or training datasets. A training
pipeline uses that data, records metrics, and stores a model artifact.

The data-science workflow starts with pulling data. It then moves through
exploration and training before evaluation, experiment tracking, and model
persistence
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Building Production ML Platforms]]).

A registry or registry-like convention promotes the artifact into a deployable
model. CI/CD then packages the code, dependencies, and serving configuration.
The deployment target may be a batch scoring job, an online endpoint, an edge
deployment, or a hybrid setup.

The return path starts when production evidence contradicts training-time
assumptions. Drift and missing inputs can send the team back to investigation.
Schema changes, latency, and errors can do the same. The team may fix data,
change features, roll back, or retrain. It may also update the product workflow.

Pipeline automation and data-driven triggers can sit in the same architecture.
Teams can add automated retraining and monitoring too, but each one needs an
owner and approval path
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).
That return path keeps automation from hiding who approves retraining,
rollback, or product changes.

## Data Inputs and Feature Pipelines

MLOps architecture starts before the model. Data inputs may come from product
events and operational databases. They may also come from files, third-party
feeds, analytics tables, or human labels. Teams should name the producer, arrival
cadence, schema expectation, and validation point for each source.

On the data pipeline side, ML pipelines and analytics data pipelines differ.
MLOps separates from DataOps by the kind of production system being operated.
Feature engineering, model training, and serving are ML pipeline steps
([[person:santonatuli=>Santona Tuli]],
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).
[[MLOps vs DataOps]] covers decisions where parts of the system may belong to
[[DataOps]], [[MLOps]], or both.

Feature and training pipelines transform inputs into model-ready data. In a
small architecture, that may be SQL plus a scheduled Python job. In a larger
architecture, the team may add
[[orchestration]] and feature-store
conventions. Validation checks and lineage often follow.

The important question isn't whether the diagram includes a feature store. The
team needs to explain how training data and inference data stay consistent
enough for the use case, especially when batch and online paths coexist.

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

Experiment tracking replaces spreadsheet run logs with transparent model history.
Metadata and lineage connect to [[reproducibility]], artifacts, and tracking
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
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]).
The registry's architectural job is to turn a training output into a model
another job, service, or team can depend on.

## CI/CD, Packaging, and Deployment

CI/CD in MLOps should cover ordinary software checks and model-specific checks.
The pipeline may test code and validate data transformations. It may also build
containers, publish packages, run deployment checks, and promote changes between
environments.

Teams should show how code and model artifacts move together.
Configuration and infrastructure should move with them. The
[[mlops-vs-devops=>MLOps vs DevOps]] distinction matters here because the same
release path must include software infrastructure and model-lifecycle evidence.

Repository templates and service principals make the release boundary explicit.
Moving logic out of notebooks into packages and CI/CD keeps deployment from
depending on manual handoffs
([[person:mariavechtomova=>Maria Vechtomova]],
[[cite:pragmatic-and-standardized-mlops@29:55=>Pragmatic MLOps]]
[[cite:pragmatic-and-standardized-mlops@33:24=>Pragmatic MLOps]]).

The release path should show predeployment checks, package or container
locations, the model version that reaches serving, and the rollback path.
[[MLOps Tools]] covers the CI/CD, registry, and deployment-product choices.

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

A serving interface should show where shared platform reuse ends and
product-specific integration begins. A reusable API convention, logging library,
or deployment template belongs in the architecture only when it defines that
handoff
[[cite:ml-product-manager-and-mlops-platform-strategy@18:25=>ML Platform Strategy]].

In a Kubernetes-native view, pipeline automation and model serving can sit
beside feature serving. Tuning and metadata components may join that platform
boundary too
([[person:theofilospapapanagiotou=>Theofilos Papapanagiotou]],
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]).
[[Metaflow]] fits the same boundary from the practitioner side because it
connects modeling code to cloud resources and scheduler infrastructure
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Treat those as architecture options, not default requirements. They fit when the
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
changed or the model needs retraining. Monitoring alerts should route evidence
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

## Governance and Lineage

[[Governance]] belongs in the
architecture when models affect customers, regulated decisions, private data, or
important business processes. It changes what teams log and who can approve a
model. It also changes how long metadata lives and how a team explains a
decision later.

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
Feature-store selection and examples belong with [[Feature Stores]].

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

At the architecture boundary, name the feature interfaces. Show which system
computes the feature and which system stores it. Show which path serves it and
how training and inference stay consistent. [[Feature Stores]] covers
feature-store selection and use-case fit
([[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]).

## Local or Shared System Boundaries

A small MLOps architecture can keep components local to one model. Code
versioning, scheduled training, run tracking, and object storage can stay local.
One deployment target, prediction logs, and a basic monitoring view can stay
local too. Architecture work decides which components stay local and which
become shared services.

A local stack may still need explicit interfaces between data and training. It
also needs interfaces between registry, serving, monitoring, and repair.

A shared platform changes the architecture when several teams depend on the
same interfaces. Templates, self-service compute, tracking, and registry
integration can then become shared services. Deployment paths, logging schemas,
monitoring hooks, and support routes can become shared too. Teams decide which
interfaces are shared and what each shared service exposes.
[[ML Platforms]] covers the internal-product and adoption side of that
decision.

Nadia Nahar's team-structure cases add a social architecture layer. An MLOps
platform may need to support API handoffs and ML-engineer bridge roles. Small
mixed teams can need different support from a centralized deployment path
([[cite:software-engineering-for-machine-learning@36:28=>Software Engineering for ML]]).

Keep the architecture focused on which interfaces are local and which become
shared. [[MLOps Engineer]] and [[ML Platforms]] cover staffing and enablement.
Use architecture work to decide whether repeated work needs a shared interface.
Then name what data or artifact crosses it and how downstream services depend on it
([[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]).

The team should keep the smallest component map it can apply consistently while
still shipping and maintaining reliable models. [[MLOps Roadmap]] covers when
to add shared components. [[MLOps Tools]] covers build-versus-buy and stack
selection.

## Production Map Checks

An architecture map should cover lifecycle interfaces, governance controls, and
the monitoring-to-data-pipeline boundary
([[cite:building-production-ml-platform-and-mlops-team@21:57=>Production ML Platforms]]
[[cite:pragmatic-and-standardized-mlops@18:56=>Pragmatic MLOps]]
[[cite:mlops-at-scale-reproducibility-adoption@42:54=>MLOps at Scale]]
[[cite:mlops-model-monitoring-data-observability@27:35=>MLOps Architect Guide]]).

Before adding another platform component, check whether the current
architecture covers these points:

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

Good MLOps architecture isn't the largest diagram. It's the smallest production
map that lets a team reproduce a model, deploy it safely, and observe what
changes after release. It also gives the team a practical structure for
improving, rolling back, or retiring the model when the evidence demands it.
