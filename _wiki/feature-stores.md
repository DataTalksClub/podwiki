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
  - Batch vs Streaming
  - Knowledge Graph vs Vector Search
  - Model Registry
  - Model Monitoring
  - Data Pipelines
---

A feature store is an operational data system for
[[machine learning]] features. Teams use it to publish, reuse, materialize, and
serve features for production models. It matters most when the same entity
features must work in both training and online
inference. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

- moving offline features into online serving
- keeping training and serving consistent
- sharing transformation code
- avoiding duplicated feature logic

Feature stores sit inside
[[MLOps]],
[[ML platforms]], and
[[machine learning infrastructure]].
[[book:20210920-python-feature-engineering-cookbook=>Python Feature Engineering Cookbook]]
by Soledad Galli covers the upstream engineering of the features that flow into
a store like this. A feature store isn't a generic replacement for a
[[data warehouse]],
[[data lake]], catalog, or
[[data-pipelines=>data pipeline]]. Its special
job is to bridge feature creation, training data construction, and low-latency
serving for production ML.

## Production Role

A feature store sits between source data and production ML systems, with source
systems such as streams, warehouses, and lakes. The feature-store layer turns
selected columns, entities, and transforms into features that models can use in
training and online inference. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Teams publish feature definitions in the store and reuse them across projects.
Fraud and analytics teams may both model user entities. Without a shared store,
they duplicate feature logic. The store also keeps
offline training data and online serving data aligned. That alignment reduces
training-serving skew. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Serving APIs let online models fetch features by entity key with predictable
latency instead of running arbitrary SQL at request time.

Production ML can return predictions through a live API or store batch
predictions for later consumption. [[cite:production-ml-mlops-and-data-team-building=>Production ML]]
Feature stores are most useful for live APIs that need fresh entity features
before scoring a request.

Fraud systems can still use a hybrid path. Daily batch feature-engineering jobs
can feed a live fraud service. When a member starts a purchase, the service
scores the transaction in real time and can block a suspicious purchase before
completion. [[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@08:51=>Fraud Prevention]]
Feature stores belong in
[[Machine Learning System Design]].
The same feature path has to serve both historical training data and the
point-of-sale decision.

## Tool Boundaries

Teams don't disagree about whether features matter. They differ on how much
machinery a team needs around them. Feast leaves transformations outside the
tool, while Tecton includes transformations in its broader
platform. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
Feast can fit into a larger stack. Tecton packages more of the feature lifecycle
for teams that want that boundary.

An adjacent data science view focuses on feature conditioning and feature
selection. It also covers engineered features, scaling, and business
interpretation. [[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering]]
That work doesn't require a feature store. It explains why feature logic has to
remain meaningful to the business problem, not just convenient to serve.

Production ML work also covers data quality, efficient storage, and processing.
Teams still need lineage and early error
detection. [[cite:production-ml-mlops-and-data-team-building=>Production ML]]
A feature store can support those ML feature needs. It still depends on reliable
[[data engineering]] and
[[data-quality-and-observability=>data quality]]
work upstream.

## Training and Serving Consistency

Models require matching environments, so training data must match production
serving semantics. Feast ingests precomputed batch and stream features, builds
point-in-time correct training datasets, and gives models one interface for
online and offline access. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Production models often need the same feature semantics in different
situations. During training, the team needs historical
feature values aligned with labels. During serving, the model needs the latest
allowed feature values for an entity such as a user or merchant. Orders and
devices can play the same role.

The same online-feature boundary appears in
[[machine-learning-personalization=>machine learning personalization]], where
fresh user and product context can change a ranking decision. A feature store
makes that interface explicit instead of leaving every project to rebuild the
path from warehouse tables to online serving.

A fraud system can precompute feature values in daily batch jobs. At inference
time the service combines those values with live payload features. It returns a
decision almost instantly. [[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@35:02=>Fraud Prevention]]
This makes the design a
[[Batch vs Streaming]]
tradeoff, not a pure streaming requirement. Batch features can still support
instant inference when serving keeps retrieval and scoring fast.

Fraud feature pipelines can also receive graph-derived signals from member,
transaction, and product networks.

Angela Ramirez describes how those networks can become model features or
analysis layers when similar transaction-product patterns relate to known fraud. [[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@29:15=>Fraud Prevention]][[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@31:17=>Fraud Prevention]]

That puts feature stores next to
[[knowledge-graph-vs-vector-search=>knowledge graph]]
and [[Graph Data Science]] decisions. The feature store serves model inputs,
while the graph system preserves the relationship structure behind some of those
inputs.

For fraud and other checkout-time systems, teams should decide feature freshness
from the product action and review path, not from a blanket "real-time"
preference.

Feature stores sit near the
[[model registry]] but don't replace it. A feature store has its own
registry. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Teams register schemas, entities, sources, and transformations so the system can
create tables or run jobs. A model registry tracks model artifacts and release
state, while the feature registry tracks the data definitions that models depend
on.

## Materialization and Retrieval

Feature creation and feature retrieval are separate, so teams can create
features through several
interfaces. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

- SQL
- Python
- PySpark
- Spark SQL
- warehouse SQL

The exact interface depends on the platform and the existing stack.

After publication, features are materialized into storage systems such as
offline stores and low-latency online stores. Retrieval focuses on key-value
enrichment for online inference instead of arbitrary SQL
execution. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

In a fraud example, an e-commerce transaction has a user ID and transaction
details. The model asks the feature store for the relevant user features before
scoring the transaction.

Feature-store architectures usually combine a computation engine with storage,
serving, registry, and monitoring layers. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

The storage split matters because online storage is typically low-latency
key-value storage. Redis or DynamoDB are examples. Offline storage is usually a
data lake or warehouse, such as Hive or BigQuery. Redshift, Snowflake, and
[[Delta Lake]] can play that role. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

## Request-Time Features

Feature stores precompute most feature logic, but some features still need
request-time context.

In fraud detection, an incoming order or booking includes live data that must be
transformed at the moment of
prediction. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

The fraud episode gives the operational version of that split. Daily batch
calculations are already available, and the live service adds calculations from
the transaction payload almost instantaneously.
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@35:02=>Fraud Prevention]]

Streaming and batch transforms are separate operational paths, so streaming
transformations should be handled differently from batch transformations. Batch
work might use dbt or a similar
system. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
For real-time feature engineering, Flink, Beam, and Spark are the options.
Spark's ecosystem and connector support are noted in Feast deployments.

For the broader streaming context, see
[[Streaming]] and
[[Batch vs Streaming]].

Raw images usually don't belong in feature stores for online tabular models.
Model outputs can still be useful when a downstream model can reuse that
probability or class flag. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

## Validation, Monitoring, and Drift

Feature stores are part of
[[model monitoring]] because bad
features can break a model even when the model service is healthy.

Monitoring covers several checks:

- valid data
- row counts
- distributions
- served features logged back to the warehouse to detect drift

[[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Validation points include streaming ingestion and transformation, batch
validation before offline-store ingestion, pre-training validation, and
pre-serving validation. Tools such as Great Expectations and TFDV can support
that work. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
The feature store doesn't make validation automatic. It provides hooks and a
shared path so teams don't have to copy the same serving-time checks into every
model.

The same shared path also helps with operational observability. Logging the
features a model actually saw makes later debugging and reproduction more
concrete. A feature store gives that logging a stable vocabulary of feature
definitions. Incident reviews can then reason from known inputs instead of
reconstructing them from scattered
services. [[cite:human-centered-mlops-and-model-monitoring@49:28=>Human-Centered MLOps]]

That same need appears in
[[manufacturing-predictive-maintenance-yield-analytics=>manufacturing predictive maintenance and yield analytics]].
Fab logs, yield records, and tool state have to be reviewable when an engineer
decides whether to change a qualification schedule
[[cite:from-semiconductor-data-to-applied-machine-learning=>Semiconductor ML]].

After launch, teams can see data drift and concept drift. They also need to keep
challenging whether a production model remains the right
model. [[cite:feature-engineering-model-monitoring-and-data-governance=>Feature Engineering]]
Feature stores expose feature-level signals that give those maintenance reviews
specific data to look at.

## Feast and Tecton

Feast and Tecton compare through platform boundaries rather than a generic
vendor ranking.
[[person:willempienaar=>Willem Pienaar]] created
Feast at Gojek and later worked on it at
Tecton. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Feast is an open-source feature store for online-offline consistency, production
feature publishing, and monitoring. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
It ingests precomputed features from batch and stream sources. It builds
point-in-time correct training datasets, then gives online and offline models a
unified interface. Feast doesn't own the transformation layer.

Feast is added after systems such as dbt, Airflow, and Spark have already
created features. Existing batch and streaming pipelines can play that upstream
role too. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Tecton's enterprise platform covers transformations and UI, plus monitoring and
security. It also covers auditability, compliance, and on-demand
transformations, including streaming and batch transformations. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

The operating models differ because Feast points at tables that are already
transformed. Tecton can point at raw data in a lake and then apply
transformations and compute
features. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]

Migration depends on where transformations live because moving them usually
creates the biggest friction. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
If a team already has a mature pipeline system, Feast can often slot on top of
it. A greenfield team may move more feature logic into Tecton. A brownfield team
has to decide whether moving transformations is worth the cost.

## Overkill Cases

Feature stores aren't mandatory for every ML
project. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
If a team only needs batch processing or batch scoring, SQL-based warehouse
tools may be enough. Existing validation checks and warehouse workflows may
cover marketing campaign scoring. Online serving gives the strongest reason to
add a feature store.

Because feature stores add shared machinery, they usually make sense once a team
has several use cases or data scientists. Multiple teams strengthen the case
when they need sharing and collaboration. [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores]]
A small startup with one model and a few features usually doesn't need one at
the beginning. That early-stage constraint belongs with
[[machine-learning-for-startups=>Machine Learning for Startups]].

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
