---
layout: article
title: "Apache Airflow: Workflow Orchestration for Data Pipelines"
keyword: "apache airflow"
summary: "A podcast-backed guide to Apache Airflow as a workflow orchestrator: where it fits in data pipelines, how to design DAGs, and when a simpler scheduler or another orchestrator is enough."
intent_notes: "People searching for apache airflow usually want to understand what Airflow does, where it fits in a data platform, how DAGs work, and whether Airflow is worth the operating overhead compared with dbt jobs, Prefect, Dagster, GitHub Actions, or managed schedulers."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Data Quality and Observability
  - Batch vs Streaming
---

Apache Airflow is a workflow orchestrator for recurring data work. Teams use it
to schedule jobs, define dependencies, retry failed tasks, and look at pipeline
runs. It doesn't store analytical data, transform business logic, or prove that
a table is correct. It coordinates tools that do those jobs.

That distinction shows up clearly in
[Natalie Kwong's]({{ '/people/nataliekwong/' | relative_url }})
[modern data stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Around 30:59, Natalie places Airflow next to ingestion and transformation tools
such as Airbyte and dbt. Airflow schedules work around those tools. It doesn't
replace the [ETL and ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}) design, the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}), or the
quality checks that make downstream data usable.

For a shorter tool comparison, use
[Airflow]({{ '/guides/airflow/' | relative_url }}), and for local development
use [Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }}).
Here, treat Apache Airflow as a production orchestration choice.

## Airflow Fit

A data pipeline usually has several separate jobs. One job extracts source
data, another loads raw records, and another runs warehouse transformations.
A later job may check or publish outputs. Airflow gives the team a control
plane for that sequence.

In a typical analytics pipeline, Airflow may start an Airbyte sync and trigger
dbt models. It may then run a warehouse check and alert an owner if the run
fails. In a machine learning pipeline, it may run batch feature generation,
trigger model training, and score entities. It may then write predictions.

In both cases, Airflow owns the schedule and the dependencies. The ingestion
tool owns ingestion. The SQL model owns transformation. The Spark job,
warehouse, feature store, or model service owns its part of the work.

This is why Airflow often appears in discussions of
[data engineering tools]({{ '/guides/data-engineering-tools/' | relative_url }})
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
It becomes useful when several teams need shared run history, retry behavior,
and a visible dependency graph. It becomes expensive ceremony when one small
script could run from cron, a cloud scheduler, or a GitHub Actions workflow.

## Architecture

Airflow turns workflows into directed acyclic graphs, usually called DAGs. Each
task is a node. Edges describe what must finish before another task can start.

The main pieces are simple to name:

- DAG files describe the tasks, dependencies, schedule, owners, and retry
  rules.
- The scheduler reads DAG definitions and picks the task instances that are
  ready to run.
- The executor sends tasks to local processes, queued workers, containers, or
  Kubernetes pods, depending on how the team runs Airflow.
- The metadata database stores DAG runs, task states, schedules, connections,
  and retry history.
- The web UI lets engineers look at run status, logs, failures, dependencies,
  and retries.

The metadata database and web UI are why Airflow is more than cron. They also
explain the operating cost. Someone has to own Airflow upgrades, secrets,
worker capacity, and logging. Someone also has to own permissions and database
backups. Airflow is infrastructure, not just a Python package.

## DAG Design

Good DAGs make pipelines easier to operate. Poor DAGs turn Airflow into a large
Python script runner with a web page.

Design DAGs around explicit units of work:

- Keep each task focused on one job.
- Make tasks idempotent so reruns don't corrupt outputs.
- Put business transformations in dbt, SQL, Spark, or Python modules instead
  of burying them inside DAG glue.
- Pass durable references between tasks, such as table names, partitions, file
  paths, model versions, or run IDs.
- Add data checks before publishing downstream outputs.
- Name DAGs and tasks so an on-call engineer can understand an alert quickly.
- Document owners, inputs, outputs, schedule, and recovery steps.
- Treat backfills as a normal path, not an emergency workaround.

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) discusses this
connection in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Around 7:08, she discusses workflow authoring and orchestration through
Airflow and Astronomer. Later, around 26:43, she places orchestrators next to
Spark and Kafka. She also discusses feature stores and vector databases.

Use Airflow to coordinate a pipeline whose responsibilities are already clear.
It shouldn't hide unclear ownership.

## Platform Conventions

Installing Airflow doesn't create a data platform. A team still needs naming
rules and reusable DAG structures. It also needs onboarding, alert routing, and
guidance on when a DAG should exist.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) makes that point
in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Around 12:30, he describes a platform as a self-service layer that helps teams
move faster without asking the platform team for every change. Around 17:22,
he talks about Airflow, conventions, and playbooks as part of the platform
anatomy. He also emphasizes shared best practices.

Airflow connects to [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
through those conventions. Airflow gives teams a place to run and look at
workflows, but conventions tell
teams how to structure those workflows. Without the conventions, teams copy
DAGs and invent naming rules. They also route alerts inconsistently and make
every failure a special case.

## Operations

Airflow helps when pipelines need shared state and recovery. It tracks which
runs succeeded, which tasks failed, which retries are still pending, and which
downstream tasks are blocked. That history matters when several teams depend on
the same tables, dashboards, features, or batch predictions.

The same operating model creates responsibilities:

- Workers need enough capacity for current runs and backfills.
- Secrets and connections need access control.
- Python dependencies need versioning and deployment discipline.
- Logs need to be available when a task fails.
- Alerts need clear owners.
- The metadata database needs backups and upgrades.

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) adds the DataOps
version in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
Around 1:01:27, he discusses reproducibility and dependency control. Around
1:02:28, he warns that Airflow can create false confidence if a successful run
doesn't include checks for edge cases. Link Airflow to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
instead of treating green tasks as proof that the data product is correct.

## Analytics Pipelines

In analytics workflows, Airflow often wraps ingestion and warehouse loading. It
may also coordinate dbt models, tests, and publication. It coordinates when
data should move. It doesn't define the business meaning of a metric.

Natalie's modern stack episode is the main DataTalks.Club reference for this
boundary. She explains ETL, ELT, data lakes, and warehouses in the same
conversation. She also covers Airbyte, dbt, and reverse ETL. She then places
Airflow at the orchestration layer. Use Airflow for sequencing and reliability,
but keep transformations reviewable in the tool where the team already manages
SQL models, Python modules, or Spark jobs.

This separation keeps ownership visible because analysts and analytics
engineers can reason about dbt models. Data engineers can reason about
ingestion, orchestration, and platform behavior. The DAG connects the steps
without turning every step into a custom Airflow task.

## ML and Feature Pipelines

Airflow also appears in ML workflows, especially batch training and batch
inference. A batch job may load data and build features. It may then train or
load a model, score entities, and write predictions. It may also publish
monitoring signals. That sequence has dependencies, retries, and backfills like
an analytics pipeline.

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
discusses this platform boundary in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Around 31:15, he separates batch inference from online serving. Around 31:51,
he discusses Airflow, pipelines, and production workflows as orchestration
choices inside an [ML platform]({{ '/wiki/ml-platforms/' | relative_url }}).

Feature stores create another boundary. In
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) explains
around 42:30 that feature platforms may integrate with dbt, Kubeflow, and
Airflow. They may also connect to warehouses and ML pipelines. Airflow can
orchestrate upstream feature jobs. It isn't the feature store, online serving
layer, or model registry.

## Alternatives

Airflow isn't always the right first scheduler.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives a clear
staging path in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 35:46, he compares Airflow with CloudWatch, Lambda, and AWS Batch. He
also discusses simpler scheduling options. Around 41:06, he recommends starting
with simpler infrastructure. Teams can move toward Airflow or Kubernetes when
they need more logging, insight, and control.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) gives the
current data engineering version in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
Around 35:37, he names Airflow alongside Prefect, Dagster, and GitHub Actions.
Around 37:08, he notes that GitHub Actions can be enough for simple workflows
because it avoids the cost of always-on orchestrators.

Use a simpler scheduler when:

- one script runs daily or weekly.
- a cloud scheduler can start a container or function.
- failures are rare and easy to rerun manually.
- no team needs shared task history.
- there's no backfill workflow yet.
- the data product hasn't proven enough value to justify platform work.

Use Airflow, Prefect, Dagster, or a managed pipeline service when dependencies
and ownership become hard to track informally. The choice isn't Airflow
versus nothing. The real question is whether the team needs a persistent
workflow control plane.

## Failure Modes

DataTalks.Club guests describe several recurring Airflow failure modes:

- treating Airflow as the ETL engine instead of the orchestrator.
- adding Airflow before the pipeline has enough complexity to justify it.
- putting too much transformation logic inside DAG files.
- copying many similar DAGs without templates or conventions.
- skipping data quality checks because task status is green.
- ignoring owners, alerts, and recovery steps.
- treating an Airflow cluster as proof that the team has a data platform.

The most damaging mistake is confusing a successful Airflow run with useful
data. Airflow can show that tasks finished. It can't prove that a dashboard,
feature, model, or business process is correct unless the workflow includes
checks that encode those expectations.

## Choosing Airflow

Choose Apache Airflow when the team needs to operate recurring and dependent
data work with shared visibility. It earns its place when run history, retries,
and backfills reduce confusion for real teams. Ownership and recovery paths
matter too.

Delay Airflow when the workflow is still a small script with a simple schedule.
Start with the pipeline's dependencies, users, recovery needs, and operating
model. Move to Airflow when those needs require a real orchestrator, not just a
tool name on an architecture diagram.
