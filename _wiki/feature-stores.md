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
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}) features.
In
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) defines it
around 6:43 as a system built for production feature problems. Those problems
include moving offline features into online serving, keeping training and
serving consistent, sharing transformation code, and avoiding duplicated
feature logic.

The DataTalks.Club discussions place feature stores inside
[MLOps]({{ '/wiki/mlops/' | relative_url }}),
[ML platforms]({{ '/wiki/ml-platforms/' | relative_url }}), and
[machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).
 [Python Feature Engineering Cookbook]({{ '/books/20210920-python-feature-engineering-cookbook/' | relative_url }})
 by Soledad Galli covers the upstream engineering of the features that flow
 into a store like this.
They aren't a generic replacement for a
[data warehouse]({{ '/wiki/data-warehouse/' | relative_url }}),
[data lake]({{ '/wiki/data-lake/' | relative_url }}), catalog, or
[data pipeline]({{ '/wiki/data-pipelines/' | relative_url }}). Their special
job is to bridge feature creation, training data construction, and low-latency
serving for production ML.

## Operational Definition

The feature-store episode gives a practical definition rather than a
vendor-specific one. A feature store sits between source data and production ML
systems. Willem describes source systems as streams, warehouses, and lakes
around 9:27 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).
The feature-store layer turns selected columns, entities, and transforms into
features that models can use in training and online inference.

The store gives teams a shared place to publish feature definitions and reuse
them across projects. Willem uses the example of fraud and analytics teams both
modeling user entities around 20:52. That duplication becomes an
organizational inefficiency
([Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})).
The store also keeps offline training data and online serving data aligned,
which reduces training-serving skew. Its serving APIs let online models fetch
features by entity key with predictable latency instead of running arbitrary
SQL at request time.

The same theme appears from the production side in
[Production ML, MLOps, and Data Team Building]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}).
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
production ML around 14:25 as either a live API that returns predictions or
batch predictions stored for later consumption. Feature stores are most useful
for the live API case when a model needs fresh entity features before it
can score a request.

## Adoption Boundaries

Teams don't disagree about whether features matter. They differ on how much
machinery a team needs around them.

Willem argues that feature stores solve real technical and organizational
problems. He says around 8:50 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
that Feast leaves transformations outside the tool. Tecton includes
transformations in its broader scope. At 29:14 he frames Feast as a smaller
tool that can fit into a larger stack.
Tecton is a fuller platform for teams that want more of the lifecycle packaged
together.

[Thom Ives]({{ '/people/thomives/' | relative_url }}) gives the adjacent data
science view in
[Feature Engineering and Model Monitoring]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}).
Around 31:44-39:14, he focuses on feature conditioning and feature selection.
He also covers engineered features, scaling, and business interpretation. That
discussion doesn't require a feature store. It explains why feature logic has
to remain meaningful to the business problem, not just convenient to serve.

Rishabh adds another boundary from production ML operations. Around 33:41 in
[Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
he emphasizes data quality, efficient storage, and processing. He also names
lineage and early error detection. A feature store can support those needs for
ML features. It doesn't remove the broader need for reliable
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) and
[data quality]({{ '/wiki/data-quality-and-observability/' | relative_url }})
work upstream.

## Online and Offline Consistency

Online-offline consistency is central here. Willem says around 7:14 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
that models require consistency between offline and online environments. That
means training data and production serving need matching semantics. Around
26:54, he describes Feast as ingesting precomputed batch and stream features.
It builds point-in-time correct training datasets and gives models one
interface for online and offline access.

Production models often need the same feature semantics in different
situations. During training, the team needs historical
feature values aligned with labels. During serving, the model needs the latest
allowed feature values for an entity such as a user or merchant. Orders and
devices can play the same role. A feature store makes that interface explicit
instead of leaving every project to rebuild the path from warehouse tables to
online serving.

The idea also explains why feature stores sit near the
[model registry]({{ '/wiki/model-registry/' | relative_url }}) but don't
replace it. Willem describes a feature-store registry around 31:11 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

Teams register schemas and sources. They also register entities and
transformations so the system can create tables or run jobs. A model registry
tracks model artifacts and release state. The feature registry tracks the data
definitions those models depend on.

## Materialization and Retrieval APIs

Around 10:21-11:30 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
Willem separates feature creation from feature retrieval. Feature creation can
use several interfaces. Willem names SQL and Python. PySpark, Spark SQL, and
warehouse SQL also appear in the discussion. The exact interface depends on the
platform and the existing stack.

After publication, features are materialized into storage systems such as
offline stores and low-latency online stores.

Retrieval has a narrower job. For online inference, Willem argues around
11:02 that an API is usually the right interface because the model needs
key-value enrichment, not arbitrary SQL execution. In the fraud example around
11:59, an e-commerce transaction has a user ID and transaction details. The
model asks the feature store for the relevant user features before scoring the
transaction.

Around 30:09-32:14, Willem names the main architecture components:

- transformation or computation engine
- storage
- serving layer
- registry
- operational monitoring

The storage split matters because online storage is typically low-latency
key-value storage such as Redis or DynamoDB.
Offline storage is usually a data lake or warehouse. Willem names systems such
as Hive and BigQuery. He also names Redshift, Snowflake, and Delta.

## On-Demand and Streaming Features

Feature stores precompute most feature logic and still support request-time
context for some features. Willem uses fraud detection around 11:30 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }})
as the example. An incoming order or booking includes live data that must be
transformed at the moment of prediction.

Streaming and batch transforms are separate operational paths. Around 46:05,
Willem says streaming transformations should be handled differently from batch
transformations. Batch work might use dbt or a similar system. Around 49:22,
he compares Flink, Beam, and Spark for real-time feature engineering. He notes
Spark's ecosystem and connector support in Feast deployments.

For the broader streaming context, see
[Streaming]({{ '/wiki/streaming/' | relative_url }}) and
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}).

Around 39:06-41:16, Willem sets a boundary for unstructured data. Feature
stores are strongest for online tabular models, so storing a raw image in one
usually isn't useful. Storing an image model's output can be useful when a
downstream model can reuse that probability or class flag.

## Validation, Monitoring, and Drift

Feature stores are part of
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) because bad
features can break a model even when the model service is healthy. Around 7:50
and 31:42 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
Willem discusses monitoring features and checking valid data. He also covers
row counts, distributions, and logging served features back to the warehouse
to detect drift.

Around 46:48, he names validation points for streaming ingestion and
transformation. He also names batch validation before offline-store ingestion,
pre-training validation, and pre-serving validation. He mentions tools such as
Great Expectations and TFDV around 46:05-48:07. The feature store doesn't make
validation automatic. It provides hooks and a shared path so teams don't have
to copy the same serving-time checks into every model.

Thom's monitoring discussion gives the reason this matters after launch. Around
47:30 in
[Feature Engineering and Model Monitoring]({{ '/podcasts/feature-engineering-model-monitoring-and-data-governance/' | relative_url }}),
he describes data drift and concept drift. He also describes the need to keep
challenging whether a production model remains the right model. Feature stores
expose feature-level signals that give those maintenance reviews specific data
to look at.

## Feast and Tecton

Willem compares Feast and Tecton through scope rather than a generic vendor
ranking. He created Feast at Gojek and later worked on it at Tecton. He
describes both in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

Feast is presented around 25:47-26:54 as an open-source feature store. Willem
says it addresses online-offline consistency, production feature publishing,
and monitoring. It ingests precomputed features from batch and stream sources.
It also builds point-in-time correct training datasets and gives online and
offline models a unified interface. Feast doesn't own the transformation layer.

Around 34:11-37:18, Willem explains that Feast is added after systems such as
dbt, Airflow, and Spark have already created features. Existing batch and
streaming pipelines can play that upstream role too.

Tecton is presented around 28:18-29:14 as a more complete enterprise platform.
Willem says it covers transformations, UI, monitoring, and security. He also
names auditability, compliance, and on-demand transformations. Streaming and
batch transformations are part of that scope too.

Around 37:00-37:18, he contrasts the operating model. Feast points at tables
that are already transformed, while Tecton can point at raw data in a lake.
Tecton can then apply transformations and compute features.

Migration depends on where transformations live. Around 54:52-57:42, Willem
says that location creates the biggest friction. If a team already has dbt,
Airflow, or Spark pipelines, Feast can often slot on top of them. A greenfield
team may choose to move more feature logic into Tecton.

A brownfield team has to decide whether moving transformations is worth the
cost.

## Overkill Scenarios

These discussions don't support treating feature stores as mandatory for every
ML project. Willem is explicit around 32:56 and 38:01 in
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}).

If a team only needs batch processing or batch scoring, it may be fine with SQL,
BigQuery ML, and dbt. Existing validation checks and warehouse workflows may be
enough. Marketing campaign scoring is one example. Online serving gives the
strongest reason to add a feature store.

Organization size matters because feature stores add shared machinery. Around
52:48-53:49, Willem says they traditionally make sense with multiple use cases
or several data scientists. Multiple teams that need sharing and collaboration
also strengthen the case. A small startup with one model and a few features
usually doesn't need one at the beginning.

The tool becomes more valuable when ML becomes central and model iteration
accelerates. It also helps when use cases multiply and teams start working
independently.

For that reason, feature stores should be evaluated like other
[MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}). Start from repeated
pain, not from a reference architecture checklist. Useful signals include
duplicated feature logic and train-serving skew. Slow handoffs from data
science to engineering matter too. Online tabular models and real-time feature
needs are stronger signals.

The case gets stronger when teams reuse user or merchant entities. Device,
transaction, and product entities can play the same role.

## Related Pages

These pages cover the nearby platform and lifecycle concepts:

- [MLOps]({{ '/wiki/mlops/' | relative_url }}) for the operating discipline
  around production ML.
- [ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }}) for the platform
  services that surround feature stores.
- [Machine Learning Tools]({{ '/wiki/machine-learning-tools/' | relative_url }})
  for where feature stores fit in the broader tooling map.
- [Streaming]({{ '/wiki/streaming/' | relative_url }}) for real-time source
  data and online ML use cases.
- [Model Registry]({{ '/wiki/model-registry/' | relative_url }}) and
  [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) for the
  neighboring lifecycle services.
