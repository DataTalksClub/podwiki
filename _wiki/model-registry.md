---
layout: wiki
title: "Model Registry"
summary: "Reference page for model registries as the handoff point between training, deployment, reproducibility, monitoring, and governance."
related:
  - MLOps
  - ML Platforms
  - Experiment Tracking
  - Model Monitoring
  - Reproducibility
  - Machine Learning Infrastructure
---

A model registry records which trained model a team can use next. DataTalks.Club
guests place it after
[[experiment tracking]] and
before [[production|deployment]]. A team trains
and evaluates a model, persists the chosen version, then gives batch jobs or
online services a stable way to load it. [[person:simonstiebellehner|Simon Stiebellehner]]
walks through that handoff in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
around 29:41-31:51.

The registry is part of
[[MLOps]], not as a full production system
on its own. A registry helps only when teams can connect it to experiments,
deployment paths, runtime dependencies, and monitoring or rollback context.
Simon places it next to metadata stores and serving choices in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
[[person:mariavechtomova|Maria Vechtomova]] gives the
lighter version in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]].
She says Artifactory, S3, MLflow, or another store can serve the registry role
if teams can find the model later and reproduce why it exists.

## Registry Scope and Metadata

A model registry is the durable record for a model that has moved beyond a
single experiment. It stores the model file or a pointer to it. It also records
enough context for a batch job or service to load, deploy, investigate, or roll
back the model. Simon describes this after the data scientist has pulled data
and evaluated models. At that point, the team needs a persistent model for
downstream services or batch jobs
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Guests include metadata in the definition, not only files. Around 42:48 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
Simon says managed platforms can record the job image and the connections
between pipeline runs. They can also record inputs and outputs. He also warns
that teams still need to think through code and data versions if they want
[[reproducibility]] years later.

Maria's minimum MLOps stack uses the same boundary. Around 18:41-20:49 in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]],
she includes the model registry in a stack with version control and CI/CD. She
also places it next to Docker registry, deployment, and monitoring. She says a
team can use a package registry or S3 if the files have searchable attributes
and remain traceable and reproducible.

A registry belongs inside an
[[ml-platforms|ML platform]], not the whole
platform. [[person:raphaelhoogvliets|Raphaël Hoogvliets]]
places it beside the other operating parts of an MLOps platform in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].

Raphaël's surrounding toolset includes:

- version control and CI/CD
- containerization, experiment tracking, and serving
- monitoring, compute, and package registries

A registry stores release context for
[[ci-cd|CI/CD]], runtime context for
[[machine learning infrastructure]],
and incident context for
[[model monitoring]].

## Formality and Tooling Choices

The main design question is how formal the registry needs to be. Simon describes
a platform version where experiment tracking, model registry, and metadata store
often arrive together in MLOps tooling. Around 30:32-30:58 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
he agrees that MLflow-style tools and Weights & Biases-style tools often package
those parts together. He says cloud platforms such as SageMaker, GCP, and Azure
do this too. That view fits teams with repeated deployment paths, shared
platform work, or stronger governance constraints.

Maria gives the lighter implementation boundary. Around 20:49 in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]],
she says Artifactory or S3 can work when teams add attributes, search, and
traceability. She still treats the registry as a minimum MLOps category, but she
doesn't require a specialized registry product before a team can start.

[[person:nemanjaradojkovic|Nemanja Radojkovic]] adds a
startup and vendor-boundary focus. In
[[podcast:lean-mlops-for-startups|Lean MLOps for Startups]],
he says early teams should keep the stack minimal and use mature tools. Around
48:11-48:29, he argues that vendors should let teams use a strong model registry
as a standalone product instead of forcing a full platform purchase. That
differs from Simon's platform packaging emphasis, but both arguments keep the
registry tied to how teams deploy and operate models.

Raphaël shifts the question from tool choice to adoption. Around 51:21 in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
he lists the registry as one part of a larger MLOps toolset. Earlier in the same
episode, he argues that teams should start with the pain point they can solve,
such as CI/CD or monitoring. He doesn't argue for rolling out every platform
component in one batch. In that view, the registry matters when it removes a
real handoff problem.

## Registry Metadata

Registry metadata should let the team answer concrete production questions:

- Which artifact is this?
- Which code produced it?
- Which image or runtime did the job use?
- Which data or query fed training?
- Which outputs were written?

Simon names those fields around 42:48 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
when he discusses metadata, lineage, and reproducibility. The stored model file
isn't enough on its own. If the team wants to reproduce a result three years
later, it also needs code and data versions. It also needs the runtime image,
parameters, and pipeline context.

Maria's early MLOps example makes the same point through custom metadata. In
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]],
she describes older Teradata Aster work where teams stored parameters,
evaluation metrics, and prediction metadata. That let them search across model
runs. Her later Artifactory and S3 discussion keeps that principle. The storage
choice can be simple, but the registry record still needs enough metadata to
support traceability.

[[person:theofilospapapanagiotou|Theofilos Papapanagiotou]]
gives a related metadata-store version in
[[podcast:mlops-kubeflow-model-monitoring|Mastering MLOps]].
Around 46:58, he ties ML metadata to data and model versioning. Around 59:49,
he describes serving by giving the model location and name to KFServing.
His example reinforces the boundary between storing model identity and using
that identity during deployment.

## Handoff to Deployment

A registry becomes useful when prediction code can load a known model version.
Simon places it immediately before the deployment choice in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
After the team persists the model, it decides whether downstream consumption is
batch inference, online serving, or a managed deployment pipeline. In his batch
example around 31:51, the training job writes a model to the registry. The
batch inference job writes predictions or other data outputs elsewhere.

Maria's standardized-template example shows the handoff from the service side.
Around 32:09 in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]],
an online-service template includes CI/CD, tags, and a deployable `main.py`.
The service can get the model from the registry and start serving.
The service template makes the registry part of
[[developer experience]] and
[[platform engineering]]:
the registry should reduce custom handoff work between training and serving.

Older Kubeflow practice uses the same deployment boundary. Around 59:49 in
[[podcast:mlops-kubeflow-model-monitoring|Mastering MLOps]],
Theofilos says KFServing can create an API endpoint when the team provides the
model name and S3 location. That isn't a full registry definition, but it shows
why the registry record needs a stable artifact location and model identity.

Feature stores use a neighboring registry concept, not a replacement. In
[[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]],
[[person:willempienaar|Willem Pienaar]] describes a
feature-store registry for sources, entities, and transforms. That registry
helps materialize features for training and serving, while a model registry
tracks the trained model that consumes those features. Teams need both concepts
when they manage feature stores and model releases together
([[MLOps Tools]]).

## Registry, Monitoring, and Rollback

Monitoring needs registry context because a team must know which model version
created the predictions it's inspecting. Raphaël lists model registry, serving,
and monitoring together in the core MLOps toolset in
[[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]].
Simon adds the logging side in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
Around 55:29, the discussion covers unified request, prediction, and response
logs so teams can run analytics and monitoring across use cases.

Rollback tests whether the registry record is useful. Maria's minimum-stack discussion
in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]
centers traceability and reproducibility. Teams need to know which model was
stored and where it was stored. They also need to know how it relates to
deployment. Without that record, rolling back a bad release turns into manual
reconstruction.

A useful registry links the model version to the deployment target and owner.
It may also link runtime dependencies and monitoring dashboards when a team has
those systems
([[Model Monitoring]],
[[MLOps Roadmap]]).

## Governance and Retention

Registry metadata can become governance evidence. Simon's fintech and fraud
examples in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]
show why some model releases need auditability and explainability. They may
also need fairness checks and evidence for why a decision happened. For those
releases, registry records sit beside
[[data governance]],
[[security]], and
[[responsible AI and governance]].

Data retention is the sharpest registry warning in Simon's platform episode. Around 45:50 in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]],
Simon contrasts storing pointers or metadata with duplicating full training
datasets for every model run. Copying large datasets into tool-managed storage
can become expensive, and personal-data deletion becomes harder when the same
person appears in many stored training snapshots.

Teams should store enough context for audit, reproduction, deployment, and
monitoring. They can then decide whether the registry should hold a full dataset
or an immutable-data pointer. It might instead hold a query reference, feature
references, or lineage metadata. Simon's discussion supports that boundary for
ML platforms, while
[[Data Quality and Observability]]
covers the broader data reliability side.

## Minimal Registry Practice

Small teams can use a simple registry convention before they adopt a larger
platform. Maria says an object store or package registry can work when teams add
searchable attributes and preserve traceability
([[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]]).

Simon says isolated platform pieces such as experiment tracking can help even a
single team. Larger platform work should follow repeated deployment paths and
real user needs
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

Nemanja's startup discussion says teams should start with mature components.
They can avoid a full platform when one standalone registry or tracking service
would solve the current problem
([[podcast:lean-mlops-for-startups|Lean MLOps for Startups]]).

Across these examples, a minimum registry record includes:

- artifact location
- model version and owner
- code version and runtime image
- data reference
- offline metric
- deployment target
- approval state
- rollback note

Simon supports the code and image fields in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
He also supports the data, input/output, and deployment fields.
Maria supports the searchable storage, traceability, and reproducibility fields
in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic and Standardized MLOps]].
The staged [[MLOps Roadmap]] expands
those fields into a broader release path.

A simple convention should become a specialized registry when the handoff breaks
down.

Teams usually reach that point when:

- multiple teams need the same handoff
- serving code needs stable lookup
- approvals matter
- incidents require quick version tracing
- governance needs durable evidence

Raphaël's platform-team discussion and Simon's platform-design discussion both
support that escalation path
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale]],
[[ML Platforms]]).

## Related Pages

These pages cover the closest lifecycle and platform topics.

- [[Experiment Tracking]] for
  the run history before a model is promoted.
- [[ML Platforms]] and
  [[Platform Engineering]] for
  the shared systems around registries, serving, and developer experience.
- [[Model Monitoring]] for the
  production signals that need model-version context.
- [[Reproducibility]] for the code,
  data, runtime, and parameter record behind a model version.
- [[Data Governance]] and
  [[Responsible AI and Governance]]
  for audit, retention, and decision-evidence constraints.
