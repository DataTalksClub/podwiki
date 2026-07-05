---
layout: wiki
title: "Apache Airflow"
keyword: "airflow"
secondary_keywords:
  - "apache airflow"
  - "airflow docker compose"
  - "airflow standalone docker"
  - "lightweight airflow"
summary: "Apache Airflow for DAG authoring, task-instance state, scheduler and executor operations, local Docker setup, and shared deployments."
related:
  - Orchestration
  - Data Pipelines
  - Data Engineering Tools
  - Data Engineering Platforms
  - DataOps
  - Data Quality and Observability
  - dbt
  - ETL
  - ELT
  - ETL vs ELT
  - Batch vs Streaming
  - Data Engineering Portfolio Projects
  - Modern Data Stack
---

Apache Airflow is the DAG-based workflow engine for data and machine-learning work
that teams choose to express as DAGs. Use this page for Airflow-specific
practice. It covers DAG files and operators. It also covers task-instance state
plus scheduler and executor behavior. Metadata state, local Docker Compose setup,
and shared deployment work belong here too.

Use [[Orchestration]] for scheduler decisions that aren't specifically about
Airflow. [[Data Pipelines]] describes the source-to-output system Airflow
coordinates, and [[How to Build Data Pipelines]] gives the build sequence.
Airflow appears most often around [[data pipelines]], [[DataOps]],
[[data engineering platforms]], and the [[modern data stack]].

DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
remains the setup reference for Docker Compose. Local Airflow matters when a
learner needs runnable DAGs, visible task handoffs, logs, and the first operating
surface around a data pipeline.
[[cite:data-engineering-tools-modern-data-stack@31:12=>Modern Data Engineering Tools]]
[[cite:data-engineering-career-path-and-skills@57:36=>Data Engineering Career Path]]
[[cite:scaling-data-engineering-teams-self-service-platforms@17:56=>Scaling Data Engineering Teams]]

In an Airflow stack, DAG tasks call the work owned elsewhere. Airbyte can own
extract-load work, [[dbt]] can own warehouse-side SQL transformations, and Spark
or Python code can own heavier processing. Airflow wraps those tools with
operators, task-instance state, logs, and metadata database records.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

## Airflow Runtime Surface

Inside Airflow, the useful unit is a DAG run. Task instances, retries, logs, and
the web UI show what happened in that run. The DAG file names the tasks and
calls into the real work. The scheduler decides which task instances can run.
The executor sends work to local processes, queued workers, containers, or
Kubernetes pods.

The metadata database stores DAG runs and task state alongside schedule, retry,
connection, and log records. The web UI gives engineers a place to look at
failures. Use [[Orchestration]] when the answer may be a runner other than
Airflow.

Lars Albertsson's workflow-engine framing maps onto these Airflow pieces. The
scheduler tracks which work is ready, and the metadata database stores task
state. The executor gives the team a recoverable way to run work after late data
or transient failures.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

In that framing, Airflow stays inside
[[orchestration]]. Teams still need
[[data quality and observability]]
because a green DAG run proves that tasks finished. It doesn't prove the data
is fresh, complete, valid, or useful.

## Shared Airflow Deployments

Airflow fits when a team wants a shared DAG authoring, scheduling, and
run-history surface around existing data work. In a modern analytics stack,
Airflow can schedule Airbyte and dbt without taking over extract-load or
warehouse transformation.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

The Airflow deployment surface includes the scheduler, executor, workers, and
metadata database. The web UI gives the team the shared view. The team also owns
connections, logs, Python dependencies, and secrets.

Deployment steps need owners too, so a shared deployment needs owners for each
piece.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

Airflow can also become a self-service surface. Then the platform team needs
conventions, templates, playbooks, and onboarding so similar DAGs don't get
copied by hand. A shared Airflow deployment sits close to
[[self-service-data-platforms=>self-service data platforms]] and
[[platform-engineering=>platform engineering]], not only scheduling.
[[cite:scaling-data-engineering-teams-self-service-platforms@17:56=>Scaling Data Engineering Teams]]

Airflow is a poor fit when its operating surface is heavier than the workflow.
That surface includes scheduler tuning and executor choice. It also includes
worker capacity, metadata database care, Python dependency isolation, and
secrets. Team-level operations add another cost.

For one-script or early-stage workflows, use [[Orchestration]] for lighter
runners and managed services.
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]]
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]

## DAG Design

Airflow workflows are written as directed acyclic graphs. A DAG should expose
task names, operators, and upstream or downstream edges. It should also set
parameters, schedules, retries, and owners.

The DAG should call into real processing code. It shouldn't become a pile of
business logic that's hard to test outside Airflow.

Keep most Airflow logic in normal Python modules. In a project, the DAG can call
Python or SQL code. It can also trigger dbt, Spark, or containerized steps.
Tests stay close to the code that owns the logic.

Useful Airflow practice still leans on Python and SQL. Docker plus cloud skills
support the run environment instead of replacing the pipeline code.
[[cite:data-engineering-career-path-and-skills@57:36=>Data Engineering Career Path]]

Thin DAGs also make review easier. A reviewer can read the DAG to understand
the order of steps, then look at the processing code that owns the real logic.
That links Airflow to
[[data engineering portfolio projects]]
and [[end-to-end-data-pipeline-project=>end-to-end data pipeline projects]].
For a build sequence, use [[How to Build Data Pipelines]].
[[cite:data-engineering-career-path-and-skills@57:36=>Data Engineering Career Path]]

## Data Quality Boundary

An Airflow task can succeed while the output is wrong. Teams can run row-count,
freshness, and schema checks as Airflow tasks. They can run null checks,
accepted-value checks, uniqueness checks, and business-rule checks there too.
Those checks still belong to [[data quality and observability]]. Use
[[dataops-checks-for-data-pipelines=>DataOps checks for data pipelines]] when
the Airflow run needs explicit pipeline gates before publication.

Tomasz Hinc gives the Airflow version of that boundary: jobs can be green while
zero records are inserted. The Airflow UI can show a successful task while the
data product is wrong. Teams still need edge-case checks and data assertions
before they trust the result.
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps]]

Airflow preserves task state and logs. Observability tells the team whether
freshness, volume, schema, or downstream consumers failed.

## Backfills and Batch ML

Airflow becomes more valuable when DAG runs need reruns and backfills. In
Airflow, the DAG should make partition boundaries and upstream datasets visible.
It should show catchup behavior and downstream publication steps too. The
cross-tool recovery model belongs in [[Orchestration]], while
[[Batch vs Streaming]] covers the broader processing tradeoff.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

Machine learning pipelines can use Airflow when the batch job fits an Airflow
DAG. If the real question is whether that job belongs in Airflow or a managed ML
pipeline service, use [[Orchestration]], [[ML platforms]], and
[[machine learning infrastructure]].
[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]

## Local Learning and Portfolio Use

Airflow is a strong portfolio signal only when it coordinates a real pipeline.
It's weaker when the project is just a DAG screenshot. A useful Airflow project
shows task order, logs, failure handling, and rerun or backfill evidence.
[[Orchestration]] owns the same learning boundary across non-Airflow tools.

A course-style project can combine Airflow with MinIO, Spark, and MySQL. The
portfolio value comes from the path from source data to local object storage,
Spark processing, and a warehouse-style destination. In that project, Airflow
coordinates handoffs between real steps instead of standing alone.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@42:48=>Radio Astronomy to Data Engineering]]
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@45:15=>Radio Astronomy to Data Engineering]]

DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
sets up local Airflow for development or portfolio work. The portfolio still
has to be about the pipeline.

Local Docker evidence matters when it proves another person can run the same
code and see the same handoffs. One portfolio example used separate containers
to fetch data, clean it, and publish results on a schedule. Another work
handoff needed scripts rebuilt as Docker images before they could run reliably
on AWS.
[[cite:get-data-analytics-and-data-engineering-job@21:25=>Get a Data Analytics and Data Engineering Job]]
[[cite:get-data-analytics-and-data-engineering-job@50:30=>Get a Data Analytics and Data Engineering Job]]

The distinct Airflow signal comes from visible DAG behavior, not the Docker
Compose file. Course projects are less convincing than a customized project with
a specific purpose and candidate-owned choices.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]
[[cite:get-data-analytics-and-data-engineering-job@51:42=>Get a Data Analytics and Data Engineering Job]]

Move from local Airflow to a shared Airflow deployment only when more people
need the same scheduler, secrets, worker isolation, or log retention. Alerts and
backfill capacity can justify it too. For a one-script project,
[[orchestration]] may make a lighter scheduler the better choice before Airflow
is worth the operating surface.
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]]
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]

## Related Pages

- [[Orchestration]]
- [[Data Pipelines]]
- [[Data Engineering Tools]]
- [[DataOps]]
- [[Data Quality and Observability]]
- [[dbt]]
- [[ETL vs ELT]]
- [[Batch vs Streaming]]
- [[How to Build Data Pipelines]]
- [[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]]
