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

A model registry records which trained model a team can reuse, deploy, look at,
or roll back. In DataTalks.Club MLOps discussions, it sits after
[[experiment tracking]] and before [[production=>deployment]]. Experiments
create candidate models, the registry preserves the promoted version, and batch
jobs or online services load that version through a stable handoff.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

A registry belongs within [[MLOps]], but it isn't a complete production system.
It helps when teams connect model artifacts to experiments and runtime
dependencies. Teams also need links to deployment paths, monitoring, and
governance context. Small teams can start with a package registry or object
store. They can also use MLflow, Artifactory, S3, or a managed platform if the
record is searchable and reproducible.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

## Registry Role

A model registry is the durable record for a model that has moved beyond a
single experiment. It stores the model file or a pointer to the file. It also
adds enough context for a service to load and deploy that model. Batch jobs and
platform workflows use the same record to investigate or roll back a model.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The registry exists because downstream consumers need a persisted model, not
only a promising experiment. A batch job should be able to find the approved
model through the registry. Online services and deployment pipelines should use
the same handoff instead of reconstructing it from a notebook run
[[cite:building-production-ml-platform-and-mlops-team@30:32=>Building Production ML Platforms]].

The record usually belongs beside [[experiment tracking]] and metadata stores.
It also connects to serving, [[ci-cd=>CI/CD]], and [[model monitoring]]. Those
systems answer production questions that a bare artifact can't answer. Teams
need to know which code produced the model and which runtime image ran the job.
They also need the training data, promotion metrics, and current deployment
target.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

The storage backend can be simple when the operating rule is clear. A team can
use an object store or package registry as a registry if it preserves attributes
and search. It also needs traceability and [[reproducibility]].

The same boundary appears in standardized MLOps templates, where version control
and CI/CD frame the minimum release path. A Docker registry, model storage, and
deployment complete that path. Monitoring sits beside it once the model is running.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

## Tooling Tradeoffs

Teams differ on how much platform to introduce with the registry. One view
treats the registry, experiment tracking, metadata store, and serving as
packaged parts of a shared [[ml-platforms=>ML platform]]. That fits repeated
deployment paths, centralized platform teams, managed cloud ML services, and
stronger governance requirements.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Many tools package the tracker, registry, and metadata store together, so the
purchase decision can look simple. The integration decision is still separate.
The team must make the package consumable by its training, serving, governance,
and monitoring flows
[[cite:building-production-ml-platform-and-mlops-team@34:01=>Building Production ML Platforms]].

A lighter view keeps the registry as a convention or standalone service until
the handoff problem justifies more platform work. A small team can use mature
components and avoid buying a full platform when one registry or tracking tool
solves the current release problem.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]

The adoption-focused view starts from the pain point rather than the tool list.
The registry matters when it removes a real handoff problem between training,
serving, monitoring, or audit. Rolling out every MLOps component in one batch can
miss that adoption constraint.
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Registry Metadata

Registry metadata should let the team answer concrete production questions:

- Which model artifact is this?
- Which code produced it?
- Which image or runtime did training use?
- Which data, query, or feature set fed training?
- Which parameters and metrics describe the run?
- Which deployment target, owner, and approval state apply?
- Which previous version should the team use for rollback?

The model file isn't enough on its own. Reproducing a result later also depends
on code versions, data references, runtime images, and parameters. Inputs,
outputs, and pipeline context turn the registry from storage into a release
record.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Searchable metadata is especially important when the backend is a general store
instead of a specialized registry product. Parameters, evaluation metrics, and
prediction metadata let teams search across runs and trace why a model exists.
That keeps a simple storage choice compatible with traceability and
reproducibility.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

[[documentation]] artifacts sit next to registry metadata rather than replacing
it. Model cards, data factsheets, and review checklists preserve model context
and data context. They also preserve product use and
[[responsible AI and governance]] evidence, while the registry preserves artifact
identity and promotion state.
[[cite:software-engineering-for-machine-learning@42:47=>Software Engineering for ML]]

## Handoff to Deployment

A registry becomes useful when prediction code can load a known model version.
After a team persists the promoted model, the team chooses whether batch
inference, online serving, or a managed deployment pipeline consumes it.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Teams use the registry as a production handoff, not only as a training artifact
folder. Downstream batch jobs, services, monitoring dashboards, and rollback
paths need to agree on the same promoted model record. Downstream consumers use
the registry after experimentation produces a model for reuse.

If the approved model is only a file in an experiment run, each consumer has to
reconstruct release state from local knowledge. A registry gives consumers a
durable handoff instead
[[cite:building-production-ml-platform-and-mlops-team@30:32=>Building Production ML Platforms]].

Service templates make that handoff part of [[developer experience]] and
[[platform engineering]]. The service shouldn't need custom knowledge about each
training run. It should be able to get the approved model from the registry and
deploy through the same CI/CD and runtime path as other services.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

Kubeflow-style serving shows the same boundary in a narrower form. The serving
system needs a stable model name and artifact location before it can create an
endpoint. That narrower example shows why model identity and storage location
must survive outside the training job.
[[cite:mlops-kubeflow-model-monitoring=>Mastering MLOps]]

Feature stores use a neighboring registry concept, not a replacement. A
feature-store registry tracks sources, entities, and transforms for training and
serving features. A model registry tracks the trained model that consumes those
features. Teams need both concepts when they manage [[feature stores]] and model
releases together.
[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]]

## Monitoring, Rollback, and Incidents

[[model monitoring]] needs registry context because each prediction belongs to a
model version. Request logs, prediction logs, response logs, and dashboards
become more useful when teams can connect them to the model artifact. Incident
reviews need the same link to deployment target, runtime, and owner.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Rollback tests whether the registry record works. A team needs to know which
model was stored, where it was stored, which release consumed it, and which
previous version can safely replace it. Without that record, a bad release turns
into manual reconstruction across storage, deployment, and monitoring systems.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]

The registry should therefore link the model version to the deployment target
and owner. Mature teams may also link runtime dependencies, monitoring
dashboards, approvals, and rollback notes. The staged [[MLOps Roadmap]] expands
that release path, while [[Machine Learning Infrastructure]] covers the
runtime systems that make the handoff work.

## Governance and Retention

Registry metadata can become governance evidence when models affect regulated,
financial, fraud, or fairness-sensitive decisions. Those releases may need
auditability, explainability, fairness checks, and durable evidence about why a
model version existed and how it reached production.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Data retention is the sharpest registry boundary. Storing pointers or metadata
is different from copying full training datasets into tool-managed storage for
every run. Dataset copies can become expensive, and personal-data deletion gets
harder when the same person appears in many stored training snapshots.
[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

Teams should store enough context for audit, reproduction, deployment, and
monitoring. They can then choose whether the registry holds a full dataset, an
immutable data pointer, or a query reference. Feature references and lineage
metadata can hold the same context. That choice
connects the registry to [[data governance]], [[security]],
[[responsible AI and governance]], and [[Data Quality and Observability]].

## Minimal Registry Practice

Small teams can use a simple registry convention before they adopt a larger
platform.

A minimum record usually includes:

- artifact location
- model version and owner
- code version and runtime image
- data or feature reference
- offline metric
- deployment target
- approval state
- rollback note

That simple convention should become a specialized registry when the handoff
breaks down. Teams usually reach that point when multiple teams use the same
release path or serving code needs stable lookup. Mandatory approvals, incidents,
and governance evidence can force the same change.
[[cite:pragmatic-and-standardized-mlops=>Pragmatic and Standardized MLOps]]
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]]
[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

## Related Pages

These pages cover the closest lifecycle and platform topics.

- [[Experiment Tracking]] covers the run history before a model is promoted.
- [[ML Platforms]] and [[Platform Engineering]] cover the shared systems around
  registries, serving, and developer experience.
- [[Model Monitoring]] covers the production signals that need model-version
  context.
- [[Reproducibility]] covers the code, data, runtime, and parameter record
  behind a model version.
- [[Data Governance]] and [[Responsible AI and Governance]] cover audit,
  retention, and decision-evidence constraints.
