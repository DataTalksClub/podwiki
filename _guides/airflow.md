---
layout: article
title: "Airflow: When Data Teams Need Workflow Orchestration"
keyword: "airflow"
summary: "A podcast-backed guide to Airflow as workflow orchestration for data pipelines, analytics stacks, platform teams, and batch ML workflows."
search_intent: "People searching for Airflow usually want to know what Airflow does, where it fits in a data stack, when it is worth adopting, and how it differs from dbt, Airbyte, Prefect, Dagster, GitHub Actions, feature stores, and ML pipeline tools."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Data Quality and Observability
  - Batch vs Streaming
---

Airflow is useful when a data team has recurring jobs that depend on each
other. In the DataTalks.Club archive, guests discuss it as an orchestrator. It
schedules work, runs dependent steps, and gives teams a place to look at
pipeline runs. It doesn't store data or define business logic
([Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}),
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59).

A team may use Airflow to trigger ingestion and run transformations. It may
also call Spark jobs and notify an owner. Each underlying tool still owns the
work it runs
([Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[Data Engineering Tools]({{ '/guides/data-engineering-tools/' | relative_url }})).
Airflow becomes a good fit when those steps are hard to run, retry, backfill,
or explain as separate scripts.

For a deeper Apache Airflow production guide, use
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}). For local
learning and DAG development, use
[Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }}).

## Airflow Jobs

Airflow gives data workflows a control plane, and teams define task graph
metadata, retries, and alerts. Airflow records which runs succeeded, which
tasks failed, and which downstream steps are blocked
([Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).

In Natalie's modern stack episode, Airflow appears after she maps the modern
stack. Around 30:59, she explains Airflow as orchestration around those tools.
Around 31:31, she connects Airbyte with extract-load work and dbt-style
transformation
([Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}),
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

So the practical Airflow question isn't whether the team wants a familiar
tool. The question is whether the team needs one place to manage schedule
state and dependency state. Retries, backfills, and run visibility belong in
that decision too
([Orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[DataOps]({{ '/wiki/dataops/' | relative_url }})).

## Stack Fit

In an analytics stack, Airflow usually sits between ingestion and consumption.
It can start connector jobs and warehouse transformations, then trigger tests
and publish modeled tables
([Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[Data Activation]({{ '/wiki/data-activation/' | relative_url }})). Those
tables may feed dashboards, activation, or product analysis.

That doesn't make Airflow the transformation layer. In the same modern stack
discussion, Natalie separates Airbyte-style extract-load work from dbt-style
transformation. She then places Airflow around the workflow
([Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-31:31).

Use Airflow to coordinate the steps. Keep metric definitions and SQL models in
systems where the team can review them. Keep Python modules and Spark jobs
there too, so the team can review and test them
([dbt]({{ '/wiki/dbt/' | relative_url }}),
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }})).

The same split shows up in pipeline architecture. [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
discusses workflow authoring through Airflow and Astronomer around 7:08. Around
26:43, she places orchestration next to Spark and Kafka. She also discusses
feature stores and vector databases
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

Airflow coordinates a pipeline whose responsibilities are already clear, but it
doesn't make unclear ownership disappear.

## Good Fit

Airflow earns its cost when a workflow has dependencies, ownership, recovery,
and history that people need to share. Natalie covers analytics pipelines that
combine Airbyte and dbt
([Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}),
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
Mehdi covers platform teams that need reusable Airflow conventions
([Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}),
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
17:22). Simon covers ML workflows that separate batch inference from online
serving
([Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}),
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
31:15-31:51).

A strong Airflow use case usually has a real pipeline operations need
([Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})):

- several jobs that must run in order
- scheduled backfills or partition reruns
- shared run history for multiple teams
- retries and alert owners
- data quality checks before publication
- batch ML jobs that need reproducible sequencing
- conventions for many similar pipelines

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the platform
version of this point. Around 17:22, he says an Airflow cluster isn't the
whole data platform. Teams also need conventions, playbooks, and best
practices for using Airflow
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).
That connects Airflow to
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}).

In those operating
models, teams make the orchestrator useful through templates and deployment
paths. They also use tests, alerts, and ownership.

## Too Much Airflow

Airflow isn't the right first move for every scheduled job. Around 35:46,
[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) compares
Airflow with cloud schedulers and simpler services. Around
41:06, he recommends starting with simpler infrastructure. Teams can move
toward Airflow or Kubernetes when they need more logging, insight, and control
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})).

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) makes a
similar data engineering point. Around 35:37, he names Airflow beside
Prefect, Dagster, and GitHub Actions. Around 37:08, he says GitHub Actions can
be enough for simple workflows because it avoids the cost of always-on
orchestrators
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

Delay Airflow when the workflow is one small script and the schedule is simple.
It also makes sense to wait when manual reruns are acceptable and no one needs
shared run history
([Data Engineering Tools]({{ '/guides/data-engineering-tools/' | relative_url }}),
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})).
Choose a workflow service such as Airflow, Prefect, or Dagster when informal
scheduling no longer gives the team enough visibility and recovery
([Orchestration]({{ '/wiki/orchestration/' | relative_url }})).

## Airflow vs dbt and Airbyte

Airflow answers a different question than dbt or Airbyte. Airbyte moves data
into storage, dbt transforms models, and Airflow schedules the surrounding
workflow. [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) makes
this split in
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
at 30:59-31:31.

That separation is useful in project design.

A DAG can start ingestion and wait for raw data. It can then run
transformations and publish a checked table. Keep the DAG focused on
orchestration instead of hiding all business logic inside Airflow code.
[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) makes the code-structure
point at 55:10 in
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).
See [Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }})
for local DAG structure.

For learners and portfolio projects, this distinction is important because
Airflow should demonstrate dependencies and retries, plus logging and recovery.
It shouldn't decorate a pipeline that could run as one command
([Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
[Data Engineering Pipeline Project]({{ '/guides/data-engineering-pipeline-project/' | relative_url }})).

## Airflow in ML and Feature Pipelines

Airflow also appears in ML infrastructure when the work is batch-oriented.
Around 31:15, [Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
separates batch inference from online serving. Around 31:51, he discusses
Airflow and production workflows as orchestration choices
([Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[ML Platforms]({{ '/wiki/ml-platforms/' | relative_url }})).

Feature stores create another boundary. [Willem Pienaar]({{ '/people/willempienaar/' | relative_url }})
explains that some feature stores don't handle upstream transformations. Feast
is one example, and teams may keep those transformations in dbt or Spark. They
may also orchestrate them through Airflow before features reach the feature
store
([Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
42:30, and [Machine Learning Infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }})).

So Airflow can coordinate upstream feature generation and batch ML jobs. It
isn't the feature store or model registry. It also isn't the online serving
layer or monitoring system
([MLOps Tools]({{ '/guides/mlops-tools/' | relative_url }}),
[Production]({{ '/wiki/production/' | relative_url }})).

## Operating Airflow Well

A green Airflow run only proves that scheduled tasks reached a successful
state. It doesn't prove that the records are complete or that the metric is
right. It also doesn't prove that the downstream dashboard, feature, or
activation workflow is safe to use
([Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[Data Activation]({{ '/wiki/data-activation/' | relative_url }})).

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) gives the sharpest
warning in the archive. Around 1:02:28, he describes green Airflow jobs that
inserted zero records. He uses the story to argue for pragmatic edge-case
checks and confidence beyond task status
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Good Airflow practice therefore belongs with DataOps:

- version pipeline code
- control dependencies
- test transformations
- check data
- route alerts
- keep runbooks and clear owners

These operating practices connect Airflow to
([DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})).

Airflow supplies the scheduling and run history. The team still has to define
what correct data means and what to do when a run fails.

## Learning Airflow

Learn Airflow after you can already build a small data pipeline with Python and
SQL. Add storage and transformations before Airflow. Add checks too.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) places Airflow after
Python/SQL in the data engineering learning path. He also puts Docker before
Airflow. Cloud basics and warehouses come first too. Around 55:10, he says good
Airflow code keeps most logic in normal Python instead of relying on
Airflow-specific code in
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).
See [Data Engineer Role]({{ '/wiki/data-engineer-role/' | relative_url }}) for
the broader role context.

A useful Airflow learning project should make orchestration visible by showing
the schedule, dependencies, retries and logs. It should also include a backfill
path, data checks and owner notes. Then link those pieces to a real data
engineering pipeline rather than treating Airflow as the whole project
([Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }}),
[Data Engineering Pipeline Project]({{ '/guides/data-engineering-pipeline-project/' | relative_url }})).

If the project is still a single script with no meaningful dependency graph,
start with a command or cron job. A cloud scheduler or GitHub Actions workflow
can fit the same simple case.
Move to Airflow when the pipeline needs shared operational state.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) supports that
staging path in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})
at 35:46-41:06. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
supports the same idea in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})
at 35:37-37:08.
