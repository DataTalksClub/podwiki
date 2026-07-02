---
layout: wiki
title: "Feature Stores"
summary: "Feature stores as operational ML data systems for reuse, online-offline consistency, materialization, validation, and serving."
related:
  - MLOps
  - ML Platforms
  - Machine Learning Infrastructure
  - Machine Learning Tools
  - Streaming
  - Model Registry
  - Model Monitoring
  - Data Pipelines
---

A feature store is an operational data system for
[[machine learning]] features, built
for production feature problems: moving offline features into online serving,
keeping training and serving consistent, sharing transformation code, and
avoiding duplicated feature logic
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Feature stores sit inside
[[MLOps]],
[[ML platforms]], and
[[machine learning infrastructure]].
 [[book:20210920-python-feature-engineering-cookbook|Python Feature Engineering Cookbook]]
 by Soledad Galli covers the upstream engineering of the features that flow
 into a store like this.
They aren't a generic replacement for a
[[data warehouse]],
[[data lake]], catalog, or
[[data-pipelines|data pipeline]]. Their special
job is to bridge feature creation, training data construction, and low-latency
serving for production ML.

## Operational Definition

A feature store sits between source data and production ML systems, with source
systems being streams, warehouses, and lakes
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
The feature-store layer turns selected columns, entities, and transforms into
features that models can use in training and online inference.

The store gives teams a shared place to publish feature definitions and reuse
them across projects. When fraud and analytics teams both model user entities,
that duplication becomes an organizational inefficiency
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
The store also keeps offline training data and online serving data aligned,
which reduces training-serving skew. Its serving APIs let online models fetch
features by entity key with predictable latency instead of running arbitrary
SQL at request time.

From the production side, ML is either a live API that returns predictions or
batch predictions stored for later consumption
([[podcast:production-ml-mlops-and-data-team-building|Production ML, MLOps, and Data Team Building]]).
Feature stores are most useful for the live API case, when a model needs fresh
entity features before it can score a request.

## Adoption Boundaries

Teams don't disagree about whether features matter. They differ on how much
machinery a team needs around them.

Feature stores solve real technical and organizational problems. Feast leaves
transformations outside the tool, while Tecton includes transformations in its
broader scope
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
Feast is a smaller tool that can fit into a larger stack, while Tecton is a
fuller platform for teams that want more of the lifecycle packaged together.

An adjacent data science view focuses on feature conditioning, feature
selection, engineered features, scaling, and business interpretation
([[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering and Model Monitoring]]).
That work doesn't require a feature store; it explains why feature logic has to
remain meaningful to the business problem, not just convenient to serve.

Another boundary comes from production ML operations, which emphasize data
quality, efficient storage, processing, lineage, and early error detection
([[podcast:production-ml-mlops-and-data-team-building|Production ML, MLOps, and Data Team Building]]).
A feature store can support those needs for ML features, but it doesn't remove
the broader need for reliable
[[data engineering]] and
[[data-quality-and-observability|data quality]]
work upstream.

## Online and Offline Consistency

Online-offline consistency is central. Models require consistency between
offline and online environments, so training data and production serving need
matching semantics
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
Feast ingests precomputed batch and stream features, builds point-in-time
correct training datasets, and gives models one interface for online and offline
access.

Production models often need the same feature semantics in different
situations. During training, the team needs historical
feature values aligned with labels. During serving, the model needs the latest
allowed feature values for an entity such as a user or merchant. Orders and
devices can play the same role. A feature store makes that interface explicit
instead of leaving every project to rebuild the path from warehouse tables to
online serving.

This also explains why feature stores sit near the
[[model registry]] but don't
replace it. A feature store has its own registry
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
Teams register schemas, sources, entities, and transformations so the system can
create tables or run jobs. A model registry tracks model artifacts and release
state; the feature registry tracks the data definitions those models depend on.

## Materialization and Retrieval APIs

Feature creation is separate from feature retrieval
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
Feature creation can use several interfaces, including SQL, Python, PySpark,
Spark SQL, and warehouse SQL. The exact interface depends on the platform and
the existing stack.

After publication, features are materialized into storage systems such as
offline stores and low-latency online stores.

Retrieval has a narrower job. For online inference, an API is usually the right
interface because the model needs key-value enrichment, not arbitrary SQL
execution
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
In a fraud example, an e-commerce transaction has a user ID and transaction
details, and the model asks the feature store for the relevant user features
before scoring the transaction.

The main architecture components are
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]):

- transformation or computation engine
- storage
- serving layer
- registry
- operational monitoring

The storage split matters because online storage is typically low-latency
key-value storage such as Redis or DynamoDB, while offline storage is usually a
data lake or warehouse such as Hive, BigQuery, Redshift, Snowflake, or Delta
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

## On-Demand and Streaming Features

Feature stores precompute most feature logic and still support request-time
context for some features. In fraud detection, an incoming order or booking
includes live data that must be transformed at the moment of prediction
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Streaming and batch transforms are separate operational paths: streaming
transformations should be handled differently from batch transformations, and
batch work might use dbt or a similar system
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
For real-time feature engineering, Flink, Beam, and Spark are the options, with
Spark's ecosystem and connector support noted in Feast deployments.

For the broader streaming context, see
[[Streaming]] and
[[Batch vs Streaming]].

There's a boundary for unstructured data. Feature stores are strongest for
online tabular models, so storing a raw image in one usually isn't useful
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
Storing an image model's output can be useful when a downstream model can reuse
that probability or class flag.

## Validation, Monitoring, and Drift

Feature stores are part of
[[model monitoring]] because bad
features can break a model even when the model service is healthy. Monitoring
covers checking valid data, row counts, distributions, and logging served
features back to the warehouse to detect drift
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Validation points include streaming ingestion and transformation, batch
validation before offline-store ingestion, pre-training validation, and
pre-serving validation, with tools such as Great Expectations and TFDV
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
The feature store doesn't make validation automatic; it provides hooks and a
shared path so teams don't have to copy the same serving-time checks into every
model.

This matters after launch because of data drift and concept drift, and the need
to keep challenging whether a production model remains the right model
([[podcast:feature-engineering-model-monitoring-and-data-governance|Feature Engineering and Model Monitoring]]).
Feature stores expose feature-level signals that give those maintenance reviews
specific data to look at.

## Feast and Tecton

Feast and Tecton compare through scope rather than a generic vendor ranking.
[[person:willempienaar|Willem Pienaar]] created
Feast at Gojek and later worked on it at Tecton
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Feast is an open-source feature store that addresses online-offline consistency,
production feature publishing, and monitoring
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
It ingests precomputed features from batch and stream sources, builds
point-in-time correct training datasets, and gives online and offline models a
unified interface. Feast doesn't own the transformation layer.

Feast is added after systems such as dbt, Airflow, and Spark have already
created features, and existing batch and streaming pipelines can play that
upstream role too
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Tecton is a more complete enterprise platform covering transformations, UI,
monitoring, security, auditability, compliance, and on-demand transformations,
with streaming and batch transformations part of that scope
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

The operating models differ: Feast points at tables that are already
transformed, while Tecton can point at raw data in a lake and then apply
transformations and compute features
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).

Migration depends on where transformations live, which creates the biggest
friction
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
If a team already has dbt, Airflow, or Spark pipelines, Feast can often slot on
top of them. A greenfield team may choose to move more feature logic into
Tecton, while a brownfield team has to decide whether moving transformations is
worth the cost.

## Overkill Scenarios

Feature stores aren't mandatory for every ML project
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
If a team only needs batch processing or batch scoring, it may be fine with SQL,
BigQuery ML, and dbt, and existing validation checks and warehouse workflows may
be enough, as in marketing campaign scoring. Online serving gives the strongest
reason to add a feature store.

Organization size matters because feature stores add shared machinery. They
traditionally make sense with multiple use cases or several data scientists, and
multiple teams that need sharing and collaboration strengthen the case
([[podcast:mlops-feature-stores-feature-stores-feast-tecton|Feature Stores for MLOps]]).
A small startup with one model and a few features usually doesn't need one at
the beginning.

The tool becomes more valuable when ML becomes central and model iteration
accelerates. It also helps when use cases multiply and teams start working
independently.

For that reason, feature stores should be evaluated like other
[[MLOps tools]]. Start from repeated
pain, not from a reference architecture checklist. Useful signals include
duplicated feature logic and train-serving skew. Slow handoffs from data
science to engineering matter too. Online tabular models and real-time feature
needs are stronger signals.

The case gets stronger when teams reuse user or merchant entities. Device,
transaction, and product entities can play the same role.

## Related Pages

These pages cover the nearby platform and lifecycle concepts:

- [[MLOps]] for the operating discipline
  around production ML.
- [[ML Platforms]] for the platform
  services that surround feature stores.
- [[Machine Learning Tools]]
  for where feature stores fit in the broader tooling map.
- [[Streaming]] for real-time source
  data and online ML use cases.
- [[Model Registry]] and
  [[Model Monitoring]] for the
  neighboring lifecycle services.
