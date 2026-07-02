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
[experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) and
before [deployment]({{ '/wiki/production/' | relative_url }}). A team trains
and evaluates a model, persists the chosen version, then gives batch jobs or
online services a stable way to load it. [Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
walks through that handoff in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)
around 29:41-31:51.

The registry is part of
[MLOps]({{ '/wiki/mlops/' | relative_url }}), not as a full production system
on its own. A registry helps only when teams can connect it to experiments,
deployment paths, runtime dependencies, and monitoring or rollback context.
Simon places it next to metadata stores and serving choices in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
[Maria Vechtomova](https://datatalks.club/people/mariavechtomova.html) gives the
lighter version in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html).
She says Artifactory, S3, MLflow, or another store can serve the registry role
if teams can find the model later and reproduce why it exists.

## Registry Scope and Metadata

A model registry is the durable record for a model that has moved beyond a
single experiment. It stores the model file or a pointer to it. It also records
enough context for a batch job or service to load, deploy, investigate, or roll
back the model. Simon describes this after the data scientist has pulled data
and evaluated models. At that point, the team needs a persistent model for
downstream services or batch jobs
([Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)).

Guests include metadata in the definition, not only files. Around 42:48 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
Simon says managed platforms can record the job image and the connections
between pipeline runs. They can also record inputs and outputs. He also warns
that teams still need to think through code and data versions if they want
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) years later.

Maria's minimum MLOps stack uses the same boundary. Around 18:41-20:49 in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she includes the model registry in a stack with version control and CI/CD. She
also places it next to Docker registry, deployment, and monitoring. She says a
team can use a package registry or S3 if the files have searchable attributes
and remain traceable and reproducible.

A registry belongs inside an
[ML platform]({{ '/wiki/ml-platforms/' | relative_url }}), not the whole
platform. [Raphaël Hoogvliets](https://datatalks.club/people/raphaelhoogvliets.html)
places it beside the other operating parts of an MLOps platform in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).

Raphaël's surrounding toolset includes:

- version control and CI/CD
- containerization, experiment tracking, and serving
- monitoring, compute, and package registries

A registry stores release context for
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), runtime context for
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}),
and incident context for
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

## Formality and Tooling Choices

The main design question is how formal the registry needs to be. Simon describes
a platform version where experiment tracking, model registry, and metadata store
often arrive together in MLOps tooling. Around 30:32-30:58 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
he agrees that MLflow-style tools and Weights & Biases-style tools often package
those parts together. He says cloud platforms such as SageMaker, GCP, and Azure
do this too. That view fits teams with repeated deployment paths, shared
platform work, or stronger governance constraints.

Maria gives the lighter implementation boundary. Around 20:49 in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she says Artifactory or S3 can work when teams add attributes, search, and
traceability. She still treats the registry as a minimum MLOps category, but she
doesn't require a specialized registry product before a team can start.

[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) adds a
startup and vendor-boundary focus. In
[Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html),
he says early teams should keep the stack minimal and use mature tools. Around
48:11-48:29, he argues that vendors should let teams use a strong model registry
as a standalone product instead of forcing a full platform purchase. That
differs from Simon's platform packaging emphasis, but both arguments keep the
registry tied to how teams deploy and operate models.

Raphaël shifts the question from tool choice to adoption. Around 51:21 in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
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
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)
when he discusses metadata, lineage, and reproducibility. The stored model file
isn't enough on its own. If the team wants to reproduce a result three years
later, it also needs code and data versions. It also needs the runtime image,
parameters, and pipeline context.

Maria's early MLOps example makes the same point through custom metadata. In
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she describes older Teradata Aster work where teams stored parameters,
evaluation metrics, and prediction metadata. That let them search across model
runs. Her later Artifactory and S3 discussion keeps that principle. The storage
choice can be simple, but the registry record still needs enough metadata to
support traceability.

[Theofilos Papapanagiotou](https://datatalks.club/people/theofilospapapanagiotou.html)
gives a related metadata-store version in
[Mastering MLOps](https://datatalks.club/podcast/mlops-kubeflow-model-monitoring.html).
Around 46:58, he ties ML metadata to data and model versioning. Around 59:49,
he describes serving by giving the model location and name to KFServing.
His example reinforces the boundary between storing model identity and using
that identity during deployment.

## Handoff to Deployment

A registry becomes useful when prediction code can load a known model version.
Simon places it immediately before the deployment choice in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
After the team persists the model, it decides whether downstream consumption is
batch inference, online serving, or a managed deployment pipeline. In his batch
example around 31:51, the training job writes a model to the registry. The
batch inference job writes predictions or other data outputs elsewhere.

Maria's standardized-template example shows the handoff from the service side.
Around 32:09 in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
an online-service template includes CI/CD, tags, and a deployable `main.py`.
The service can get the model from the registry and start serving.
The service template makes the registry part of
[developer experience]({{ '/wiki/developer-experience/' | relative_url }}) and
[platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}):
the registry should reduce custom handoff work between training and serving.

Older Kubeflow practice uses the same deployment boundary. Around 59:49 in
[Mastering MLOps](https://datatalks.club/podcast/mlops-kubeflow-model-monitoring.html),
Theofilos says KFServing can create an API endpoint when the team provides the
model name and S3 location. That isn't a full registry definition, but it shows
why the registry record needs a stable artifact location and model identity.

Feature stores use a neighboring registry concept, not a replacement. In
[Feature Stores for MLOps](https://datatalks.club/podcast/mlops-feature-stores-feature-stores-feast-tecton.html),
[Willem Pienaar](https://datatalks.club/people/willempienaar.html) describes a
feature-store registry for sources, entities, and transforms. That registry
helps materialize features for training and serving, while a model registry
tracks the trained model that consumes those features. Teams need both concepts
when they manage feature stores and model releases together
([MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }})).

## Registry, Monitoring, and Rollback

Monitoring needs registry context because a team must know which model version
created the predictions it's inspecting. Raphaël lists model registry, serving,
and monitoring together in the core MLOps toolset in
[MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html).
Simon adds the logging side in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
Around 55:29, the discussion covers unified request, prediction, and response
logs so teams can run analytics and monitoring across use cases.

Rollback tests whether the registry record is useful. Maria's minimum-stack discussion
in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)
centers traceability and reproducibility. Teams need to know which model was
stored and where it was stored. They also need to know how it relates to
deployment. Without that record, rolling back a bad release turns into manual
reconstruction.

A useful registry links the model version to the deployment target and owner.
It may also link runtime dependencies and monitoring dashboards when a team has
those systems
([Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})).

## Governance and Retention

Registry metadata can become governance evidence. Simon's fintech and fraud
examples in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)
show why some model releases need auditability and explainability. They may
also need fairness checks and evidence for why a decision happened. For those
releases, registry records sit beside
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[security]({{ '/wiki/security/' | relative_url }}), and
[responsible AI and governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

Data retention is the sharpest registry warning in Simon's platform episode. Around 45:50 in
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
Simon contrasts storing pointers or metadata with duplicating full training
datasets for every model run. Copying large datasets into tool-managed storage
can become expensive, and personal-data deletion becomes harder when the same
person appears in many stored training snapshots.

Teams should store enough context for audit, reproduction, deployment, and
monitoring. They can then decide whether the registry should hold a full dataset
or an immutable-data pointer. It might instead hold a query reference, feature
references, or lineage metadata. Simon's discussion supports that boundary for
ML platforms, while
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
covers the broader data reliability side.

## Minimal Registry Practice

Small teams can use a simple registry convention before they adopt a larger
platform. Maria says an object store or package registry can work when teams add
searchable attributes and preserve traceability
([Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)).

Simon says isolated platform pieces such as experiment tracking can help even a
single team. Larger platform work should follow repeated deployment paths and
real user needs
([Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html)).

Nemanja's startup discussion says teams should start with mature components.
They can avoid a full platform when one standalone registry or tracking service
would solve the current problem
([Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html)).

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
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html).
He also supports the data, input/output, and deployment fields.
Maria supports the searchable storage, traceability, and reproducibility fields
in
[Pragmatic and Standardized MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html).
The staged [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) expands
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
([MLOps at Scale](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

## Related Pages

These pages cover the closest lifecycle and platform topics.

- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) for
  the run history before a model is promoted.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
  [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}) for
  the shared systems around registries, serving, and developer experience.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
  production signals that need model-version context.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) for the code,
  data, runtime, and parameter record behind a model version.
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
  [Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
  for audit, retention, and decision-evidence constraints.
