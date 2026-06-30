---
layout: wiki
title: "Model Registry"
summary: "Podcast-grounded reference page for model registries as the handoff point between training, deployment, reproducibility, monitoring, and governance."
related:
  - MLOps
  - ML Platforms
  - Experiment Tracking
  - Model Monitoring
  - Reproducibility
  - Machine Learning Infrastructure
---

A model registry is the tool or convention that makes a trained model
available for later use. In the DataTalks.Club archive, it's the handoff point
between [experiment tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
and [production]({{ '/wiki/production/' | relative_url }}). A team trains and
evaluates a candidate. Then it persists the model, records context, and lets a
job or service consume it.

The archive doesn't treat the registry as a magic production system. In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
places registries next to experiment tracking, metadata stores, and deployment
pipelines. He also connects them to lineage and governance. In

[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }}) makes the
same point with lighter infrastructure. Artifactory, S3, MLflow, or another
storage system can work when teams keep artifacts traceable and reproducible.
The registry also has to fit rollback and deployment workflows.

## Link Map

These wiki pages cover the closest neighboring concepts:

- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }})
  covers the run history before a model is promoted.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) and
  [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})
  cover the shared platform and runtime systems around the registry.
- [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
  [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) cover the
  operating discipline that makes a registry useful.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) depends on
  knowing which model version produced predictions.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) covers code,
  data, and environment recovery.
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) covers
  metadata, retention, and audit questions around stored artifacts.

These podcast interviews anchor the page:

- [Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})
  with [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
  covers model persistence around 30:32, metadata and lineage around 42:48, and
  data-governance constraints around 45:50.
- [Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})
  with [Maria Vechtomova]({{ '/people/mariavechtomova/' | relative_url }})
  covers model registry as part of a minimum MLOps stack around 18:41,
  artifact-store alternatives around 20:49, and rollback context around 22:36.
  It also covers registry-to-serving templates around 32:09.
- [MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})
  with [Raphaël Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
  places registries inside a larger toolset around 51:21. That toolset also
  includes experiment tracking and serving. It also includes monitoring,
  dependency management, and team adoption.
- [MLOps Tools]({{ '/guides/mlops-tools/' | relative_url }}) summarizes
  registry placement for readers comparing tool categories, while this page
  keeps the archive-derived concept focused.

## Common Definition

Across the archive, a model registry is the durable handoff record for a model.
It stores the artifact or links to it. It also gives downstream consumers a
stable lookup path, deployment context, and investigation context.

Simon frames that handoff directly after experiment tracking. Once teams train
and evaluate a model, they need to persist it for downstream usage. That
registry often lives in the same platform family as the tracker or metadata store
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

The shared definition includes metadata, not just files. Simon says managed
platforms can help record job images and connections between pipeline runs.
They can also record inputs and outputs. Teams still need to think through code
versions and data versions end to end
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Maria describes the same requirement through rollback. Teams need to find the
code, compute, and model for each run. They also need the deployment and storage
location
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

The common definition also separates a model registry from the broader
[ML platform]({{ '/wiki/ml-platforms/' | relative_url }}). The registry is one
component in a lifecycle. That lifecycle also needs CI/CD and deployment. It
also needs monitoring, governance, and Docker or package registries
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## Guest Differences

Guests differ most on registry formality. Simon describes a platform version
where experiment tracking, model registry, and metadata tracking arrive
together in SaaS or cloud MLOps tooling. He names MLflow-style tools and
Weights & Biases-style tools. He also names SageMaker, GCP, and Azure
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
That view fits teams with repeated deployment paths, stronger governance needs,
or enough models to justify platform standardization.

Maria gives the lighter-weight implementation boundary. Around 20:49 in
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }}),
she says Artifactory or S3 can be acceptable. Teams need searchable attributes,
later artifact lookup, traceability, and reproducibility. Her point isn't that
registries are optional. Teams can implement the registry principle with
existing infrastructure before they buy or build a specialized system.

Raphaël Hoogvliets draws the boundary from adoption and scale. Around 51:21 in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
he lists model registries with experiment tracking, serving, and monitoring.
He doesn't treat the registry as the first thing to build.

In his framing, the registry belongs to an enabling MLOps platform. That
platform also handles CI, repository structure, testing, and dependency
packaging. It also handles deployment frequency and team pain points
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

## Registry Metadata

The registry record needs enough metadata to answer production questions:

- Which artifact is this?
- Which code produced it?
- Which image or runtime did the job use?
- Which data or query fed training?
- Which outputs were written?

Simon covers those questions around 42:48 when he discusses metadata, lineage,
and reproducibility in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).

That metadata connects the registry to
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}). A stored model
artifact isn't enough to recreate an old result. The team also needs code and
data versions. It needs parameters, job image, and pipeline context too
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Maria's maturity-assessment discussion says the same thing operationally.
Teams need to know how code and compute fit with model deployment and storage.
That context lets them roll back
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

## Handoff to Deployment

A registry becomes useful when prediction code can consume a known artifact.
Simon places the registry immediately before deployment decisions. After the
team persists the model, it chooses a serving path. That path can be batch
inference, online serving, or a managed deployment pipeline
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Maria's standardized-template example shows the handoff. In the online-service
scenario around 32:09, the generated project already has CI/CD and tags. It
also has a deployable structure. The serving code then retrieves the model from
the registry
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).
That connects model registries to
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}) and
[Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}):
the registry should reduce custom handoff work, not become another manual
spreadsheet.

## Registry, Monitoring, and Rollback

Monitoring needs the registry because a team has to know which model version is
running before it can diagnose production signals. Raphaël lists model
registry, serving, and monitoring together in the core MLOps toolset
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).
Simon adds the logging side. Teams can use unified prediction schemas for
requests, predictions, and responses to support monitoring and analytics after
serving
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Rollback is the practical test. Maria says teams need to recover the model
behind a deployment. They also need to know where it was stored because rollback
becomes tedious without that context
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).
That's why a useful registry record should link the model version to the
deployment target and owner. It should also link to approval state, runtime
dependencies, and monitoring dashboards
([MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})).

## Governance and Retention

Registry metadata can create governance obligations. Simon's fintech examples
show why fraud and financial systems may need auditability and explainability.
They may also need fairness checks and evidence for why a decision happened
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).
Those needs connect model registries to
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }}).

Data retention is the sharpest archive-backed warning. Around 45:50 in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
Simon contrasts storing pointers or metadata with duplicating full training
datasets for every model run. Full dataset logging can become costly with large
data and difficult under GDPR-style deletion requests when personal data is
copied into many artifact stores.

The archive supports an evidence-driven boundary. Store enough context to
audit, reproduce, deploy, and monitor the model. Then choose which data
reference belongs in the registry. The options include full datasets and
pointers to immutable data. They also include feature references, query
metadata, and lineage metadata
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

## Minimal Registry Practice

Small teams can use a simple registry convention before building a large
platform. Maria says an object store or package registry can work when
teams add searchable attributes. That lighter convention still needs
traceability and reproducibility
([Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).
Simon also says experiment tracking can pay off for a single team. Other
platform pieces need real users and deployment patterns before heavy investment
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

A minimum archive-grounded registry record should include:

- artifact location
- model version and owner
- code version and runtime image
- data reference
- offline metric
- deployment target
- approval state
- rollback note

Those fields come from Simon's metadata and deployment discussion. They also
come from Maria's rollback discussion and the staged checklist in
[MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }})
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Pragmatic and Standardized MLOps]({{ '/podcasts/pragmatic-and-standardized-mlops/' | relative_url }})).

Teams should add a specialized registry when the convention breaks down.

That usually happens in a few cases:

- multiple teams need the same handoff
- serving code needs stable lookup
- approvals matter
- incidents require quick version tracing
- governance needs durable evidence

Raphaël's platform-team discussion and Simon's platform-design discussion both
support that escalation path
([MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

## Related Pages

These pages cover the adjacent lifecycle and platform topics.

- [Experiment Tracking]({{ '/wiki/experiment-tracking/' | relative_url }}) -
  captures runs before promotion.
- [MLOps]({{ '/wiki/mlops/' | relative_url }}) - frames the full operating
  discipline around model lifecycle work.
- [MLOps Roadmap]({{ '/wiki/mlops-roadmap/' | relative_url }}) - places the
  registry after reproducible experiments and one deployment path.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) - covers shared
  platform services, adoption, metadata, and governance.
- [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}) -
  covers runtime, orchestration, and serving infrastructure.
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) - uses
  model version context to diagnose production behavior.
- [Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}) - covers
  code, data, environment, and artifact recovery.
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) - covers
  metadata, retention, lineage, and compliance constraints.
- [MLOps Tools]({{ '/guides/mlops-tools/' | relative_url }}) - compares tool
  categories for readers choosing an MLOps stack.
