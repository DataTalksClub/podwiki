---
layout: article
title: "Airflow Docker Compose: Local Setup for Data Pipeline Projects"
keyword: "airflow docker compose"
summary: "A practical setup for running Airflow locally with Docker Compose for data pipeline projects, with DAG structure, mounted code, checks, logs, and limits."
search_intent: "People searching for airflow docker compose usually want a practical local setup for learning or portfolio data pipelines, plus guidance on what belongs in Airflow versus Python, SQL, dbt, or other pipeline code."
related_wiki:
  - Apache Airflow
  - Orchestration
  - Data Pipelines
  - Data Engineering Tools
  - Data Engineering Platforms
  - DataOps
  - Data Quality and Observability
  - End-to-End Data Pipeline Project
---

Use Airflow with Docker Compose after your pipeline has steps that Airflow
should coordinate. Docker Compose can start the Airflow web UI and scheduler on
a laptop. It can also start the metadata database, DAG folder, and logs. That
makes the setup useful for learning, DAG development, teaching, and portfolio
review.

The local setup workflow sits under
[Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}) for the tool
concept and [orchestration]({{ '/wiki/orchestration/' | relative_url }}) for
the broader control-plane structure. The broader pipeline build sequence lives in
[How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }})
and [End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }}).

[Daniel Egbo]({{ '/people/danielegbo/' | relative_url }}) gives concrete
Airflow-in-Compose evidence in
[From Radio Astronomy to Machine Learning and Data Engineering]({{ '/podcasts/from-radio-astronomy-to-machine-learning-and-data-engineering/' | relative_url }}).
At 42:48-46:52, he discusses course projects with Airflow. The local services
include MinIO, Spark, and MySQL. He also covers a warehouse path, Compose setup,
environment variables, and the Airflow web server.

[Gloria Quiceno]({{ '/people/gloriaquiceno/' | relative_url }}) adds the
reproducibility reason. At 21:25 in
[Get a Data Analytics and Data Engineering Job]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}),
she explains how Docker made scripts easier to share and run across machines.

## Start With A Local Airflow Use Case

Start with one local workflow, not a full platform. A good first project has a
source and a raw output. It also has one transformation, one check, and one
published result.
Airflow should coordinate those steps after the work is already clear.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the tool
boundary in
[ETL vs ELT and Modern Data Engineering at 30:59]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Airflow schedules and orchestrates work. Airbyte handles extract-load work, and
dbt handles warehouse transformations. [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
names Airflow, Prefect, Dagster, and Mage as orchestration choices at 26:43 in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
The important decision is how the workflow is broken up, not which scheduler
name appears in the README.

Use Docker Compose when the project needs at least three local Airflow pieces:

1. A scheduler that reads DAGs and creates task runs.
2. A web UI where a reviewer can look at runs and logs.
3. A metadata database that preserves DAG and task state.
4. Mounted folders for DAGs, logs, plugins, and project code.
5. Local services that mimic real dependencies, such as a database or object store.

## Use Compose For Airflow Runtime Pieces

The official Airflow Docker guide provides the current Compose quick start for
learning and exploration. Use the
[Apache Airflow Docker Compose guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
for the exact file and version-specific commands. Don't treat the official
quick-start Compose file as a production deployment because it doesn't provide
production security guarantees.

Daniel's local Airflow project shows why these runtime pieces matter in a
learning setup. His Compose stack included Airflow plus local services such as
MinIO, Spark, and MySQL. The setup also exposed environment variables and the
Airflow web server
([42:48-46:52]({{ '/podcasts/from-radio-astronomy-to-machine-learning-and-data-engineering/' | relative_url }})).

For a portfolio project, keep the setup visible and boring:

```text
project/
  dags/
  logs/
  plugins/
  include/
  src/
  tests/
  docker-compose.yaml
  .env
  README.md
```

Use these folders deliberately:

1. Put DAG definitions in `dags/`.
2. Put normal Python modules in `src/`.
3. Put small sample inputs, SQL files, or config files in `include/`.
4. Persist `logs/` so failed task runs remain visible after a restart.
5. Keep tests outside Airflow so they can run without the scheduler.

The local startup sequence should be easy to explain:

1. Download or copy the official Compose file for the Airflow version you use.
2. Create `dags/`, `logs/`, `plugins/`, and project-code folders.
3. Set the local Airflow user ID in `.env` when the host needs it.
4. Initialize Airflow metadata and the first user.
5. Start the stack.
6. Open the Airflow UI and trigger one DAG.
7. Look at task logs and the output table, file, or dashboard input.

## Keep DAGs Thin

Airflow DAG files should describe order and ownership. They should also describe
retries, parameters, and calls into real work. They shouldn't contain most
extraction, transformation, or validation logic.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
platform version in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
Around 30:34-35:57, he places a workflow engine next to storage and compute. The
engine tracks dependencies and schedules work. It retries after late data,
transient infrastructure failures, or bugs. The compute layer does the real
processing.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) makes the same point for
learners in
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).
Around 55:10, he says good Airflow code keeps most logic in normal Python
instead of relying on Airflow for everything. In a Compose project, that means
the DAG should call tested modules, SQL, or dbt commands. It can also call
containerized jobs. The DAG shouldn't become the only place where the pipeline
logic exists.

## Mount Code, Data, And Logs Deliberately

Mount only the folders that explain the project. A reviewer should see where
DAGs live, where supporting code lives, and where logs appear after a task
fails. A small local database or object store can make the workflow realistic,
but each extra service should support the story.

Daniel's course-project discussion is useful here because he worked through
Airflow with MySQL, MinIO, Spark, and a warehouse in a local learning context.
Not every project needs all of those services. Use Compose when the project
needs to show how orchestration connects the runtime pieces.

Gloria's capstone gives a simpler version. Around 50:15 in
[Get a Data Analytics and Data Engineering Job]({{ '/podcasts/get-data-analytics-and-data-engineering-job/' | relative_url }}),
she discusses a Twitter data pipeline with Docker containers and Slack delivery.
That kind of project can use Airflow later when the run path needs scheduling,
dependency state, retries, or backfills.

Pin dependency versions in the image or requirements file. In
[DataOps and GitOps Best Practices]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) describes an unpinned
Python dependency causing a containerized job failure after an API change around
1:01:27. Local Compose should reduce dependency surprises, not hide them.

## Add Checks, Logs, And Rerun Behavior

A green Airflow run proves that tasks finished, not that the data is correct.

Add checks that can fail the run:

1. Source file or API response exists.
2. Row count is above a minimum.
3. Required columns are present.
4. Primary key or serving-table grain is unique.
5. Freshness is within the expected window.
6. Nulls and accepted values match the consumer expectation.

Tomasz makes this boundary explicit around 1:02:50 in the same DataOps and
GitOps episode. He describes Airflow jobs that were green while the output had
zero rows. Add a data check that fails when the output is wrong instead of
trusting the Airflow UI alone.

Use one deliberate failure in the project. Break the input path, add a duplicate
row, or make a freshness check fail. Then show how Airflow records the failure,
where the log appears, and how the DAG reruns after the input is fixed. This is
the portfolio value of local Compose: a reviewer can see recovery behavior, not
only a successful screenshot.

## Know Where Local Compose Stops

Docker Compose isn't a production Airflow platform. It's a local environment
for learning, development, and repeatable review.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the platform
boundary in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Around 17:22-19:25, he says an Airflow cluster is only one part of a platform.
Teams also need naming conventions and sequence rules. They need playbooks,
onboarding, and support paths too. A local Compose file is further from
production than that.

Avoid Airflow when one simpler scheduler would make the project clearer.
[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) compares Airflow
with CloudWatch and Lambda around 35:46 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 41:06, he recommends starting simple and moving toward Airflow or
Kubernetes when the workflow needs more control. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
makes the same point around 35:37-37:08 in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}):
GitHub Actions can be enough for simple workflows.

Move beyond local Compose when the project needs operational controls:

- shared deployment
- managed secrets
- searchable log retention
- multiple users
- worker isolation or autoscaling
- production alerting
- access control

## Airflow Docker Compose Setup Checklist

The local project checklist is:

1. Name the data product, consumer, and refresh cadence.
2. Keep one DAG focused on one pipeline.
3. Put business logic in `src/`, SQL files, dbt models, or separate containers.
4. Mount `dags/`, `logs/`, `plugins/`, and supporting project code.
5. Persist logs and metadata long enough to look at failures.
6. Pin Python, provider, and system dependencies.
7. Add at least one data check that can fail the run.
8. Show one retry, rerun, or backfill scenario.
9. Document the startup steps in the README.
10. Link back to the production boundary so nobody reads the local stack as a platform.

When you use the page for interview or portfolio preparation, don't stop at "I
ran Airflow." Show that one local command starts the pipeline. Show that the
DAG calls real tested work, a bad input fails visibly, and the project explains
when a simpler scheduler would have been enough.
