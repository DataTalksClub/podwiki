---
layout: wiki
title: "Apache Airflow"
keyword: "airflow"
secondary_keywords:
  - "apache airflow"
  - "airflow docker compose"
  - "airflow standalone docker"
  - "lightweight airflow"
summary: "Apache Airflow for DAG-based workflows, scheduler and executor operations, local Docker setup, backfills, and shared deployments."
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

Apache Airflow is the concrete scheduler and orchestrator for recurring data and
machine-learning work that teams want to express as DAGs. Use this page when the
question is Airflow-specific: DAG structure and task retries. It also covers
backfills, scheduler/executor behavior, local Docker Compose setup, and shared
Airflow operations.

[[Orchestration]] covers the broader control-plane concept across workflow
engines, CI/CD systems, cloud schedulers, and ML pipeline services. Use that page
for cross-tool scheduling choices. [[Data Pipelines]] describes the
source-to-output system Airflow coordinates, and [[How to Build Data Pipelines]]
gives the build sequence. Guests mention Airflow most often around
[[data pipelines]], [[DataOps]], [[data engineering platforms]], and the
[[modern data stack]].

DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
remains canonical for Docker Compose setup. In the wiki, local Airflow is useful
when the discussion is about runnable DAGs and visible task handoffs. It also
helps explain logs and the point where a learner's local stack starts to look
like a platform to operate.
[[cite:data-engineering-tools-modern-data-stack@31:12=>Modern Data Engineering Tools]]
[[cite:data-engineering-career-path-and-skills@57:36=>Data Engineering Career Path]]
[[cite:scaling-data-engineering-teams-self-service-platforms@17:56=>Scaling Data Engineering Teams]]

Guests usually treat Airflow as coordination infrastructure, not as the whole
pipeline. Teams keep transformation logic in the ingestion tool or warehouse
job. It can also live in a Spark job, dbt project, feature pipeline, or Python
module. They use Airflow for the schedule, dependency graph, run state, and
visibility around those steps.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

One modern-stack boundary puts Airflow around scheduling and orchestration while
Airbyte owns extract-load work. In the same stack, [[dbt]] owns
warehouse-side SQL transformations and Airflow stays adjacent to the [[ETL]] and
[[ELT]] workflow boundary captured in [[ETL vs ELT]].
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

## Job Scheduling and Dependency State

Airflow is useful when a workflow needs more than a timer. A team usually
chooses it when several tasks must run in order. It also fits when failures need
visible logs, retries and reruns matter, or a group needs shared run history.

The DAG describes the order, schedule, retry behavior, and owners. It also
calls into the real work. The scheduler decides which task instances can run.
The executor sends work to local processes, queued workers, containers, or
Kubernetes pods.

The metadata database stores DAG runs and task state alongside schedule, retry,
connection, and log records. The web UI gives engineers a place to look at
failures.

This is where Lars Albertsson's workflow-engine framing maps onto Airflow. The
scheduler tracks which work is ready. The metadata database stores task state.
The executor gives the team a recoverable way to run work after late data or
transient failures.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

In that framing, Airflow stays inside
[[orchestration]]. Teams still need
[[data quality and observability]]
because a green DAG run proves that tasks finished. It doesn't prove the data
is fresh, complete, valid, or useful.

## Airflow Fit

Airflow fits when a team wants a shared scheduler and run-history surface
around existing data work. In a modern analytics stack, Airflow can schedule
Airbyte and dbt without taking over extract-load or warehouse transformation.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

Platform reliability discussions place Airflow and Luigi in the workflow-engine
category. In Airflow, the team runs the scheduler and executor. It also runs
workers and the metadata database.

The team also owns the web UI and connections. Logs need owners too, along with
Python dependencies and secrets. Deployment steps need the same ownership.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

Airflow can also become a self-service surface. Then the platform team needs
conventions, templates, playbooks, and onboarding so similar DAGs don't get
copied by hand. That puts shared Airflow close to
[[self-service-data-platforms=>self-service data platforms]] and
[[platform-engineering=>platform engineering]], not only scheduling.
[[cite:scaling-data-engineering-teams-self-service-platforms@17:56=>Scaling Data Engineering Teams]]

Airflow is a poor fit when the deployment surface is heavier than the workflow. A
one-script project may start with GitHub Actions or a cloud scheduler. On AWS,
CloudWatch and Lambda can be enough. Use Airflow when shared logging, dependency
state, reruns, and recovery justify running Airflow services. Those services
include the scheduler and workers, plus the metadata database, web UI, and
deployment work.

Use [[Orchestration]] for the broader comparison with adjacent
workflow engines, ML pipeline services, and cloud-native schedulers.
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]]
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]

## DAG Design

Airflow workflows are written as directed acyclic graphs. A DAG should describe
the sequence of work, schedule, retry behavior, and owners. Parameters belong
there too. The DAG should call into real processing code. It shouldn't become a
pile of business logic that's hard to test outside Airflow.

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

Airflow can show that a task succeeded, but it can't prove that the output is
correct. Teams need checks for row counts, freshness, schema, and nulls. They
also need checks for accepted values, uniqueness, and business rules. Those
checks can run inside an Airflow task, but they still belong to
[[data quality and observability]],
not only to orchestration.

Airflow jobs can be green while zero records are inserted. The run status can
look successful while the data product is wrong, so teams need edge-case checks
and data assertions before they trust the result.
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps]]

Teams need this boundary when they add
[[data-quality-and-observability=>data observability]] and
[[DataOps tools]], because the
orchestrator can preserve task state and logs. Observability tells the team
whether freshness or volume failed, and it can also flag schema issues or
downstream consumer problems.

## Backfills and Batch ML

Airflow becomes more valuable when the workflow needs reruns and backfills. A
daily job can fail because late data arrived or a source schema changed. A bug
can also create bad output. The team may need to rerun old partitions in the
correct order. Then it may need to republish downstream tables, dashboards,
features, or predictions.

Batch workflows are easier to rerun when the team can name the inputs and
dependencies. Airflow fits batch pipelines with backfills especially well,
while [[Batch vs Streaming]]
covers the broader processing tradeoff.[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

Machine learning pipelines use the same structure. Batch inference is separated
from online serving and often uses Airflow or SageMaker Pipelines as the
orchestrator. That job loads data and preprocesses it. Then it runs the model
and writes predictions. Teams using Airflow this way also connect it to
[[MLOps]],
[[ML platforms]], and
[[machine learning infrastructure]].[[cite:building-production-ml-platform-and-mlops-team=>Production ML Platforms]]

## Local Learning and Portfolio Use

Airflow is a strong portfolio signal only when it coordinates a real pipeline.
It's weaker when the project is just a DAG screenshot. A useful project should
show why one task waits for another. It should also show what happens when an
input is late. A bad input should fail visibly, and the project should show how
a rerun or backfill works after the issue is fixed.

A course-style project can combine Airflow with MinIO, Spark, and MySQL. The
portfolio value comes from the path from source data to local object storage,
Spark processing, and a warehouse-style destination. In that project, Airflow
coordinates handoffs between real steps instead of standing alone.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@42:48=>Radio Astronomy to Data Engineering]]
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@45:15=>Radio Astronomy to Data Engineering]]

Use DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
for local development or portfolio work. Use the tutorial to set up Airflow.
Keep the portfolio about the pipeline.

Local Docker evidence matters when it proves another person can run the same
code and see the same handoffs. One portfolio example used separate containers
to fetch data, clean it, and publish results on a schedule. Another work
handoff needed scripts rebuilt as Docker images before they could run reliably
on AWS.
[[cite:get-data-analytics-and-data-engineering-job@21:25=>Get a Data Analytics and Data Engineering Job]]
[[cite:get-data-analytics-and-data-engineering-job@50:30=>Get a Data Analytics and Data Engineering Job]]

The distinct Airflow signal isn't the Docker Compose file because it comes from
visible orchestration behavior. The project shows task order, logs, failure
handling, and rerun or backfill evidence attached to a real pipeline. Course
projects are less convincing than a customized project with a specific purpose
and candidate-owned choices.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]
[[cite:get-data-analytics-and-data-engineering-job@51:42=>Get a Data Analytics and Data Engineering Job]]

Move to a shared Airflow deployment only when more people need it. Secrets and
worker isolation can justify the platform work. Log retention, alerts, and
backfills can too. For a one-script project, [[orchestration]] may recommend a
simpler scheduler first. GitHub Actions or a cloud scheduler can fit before
Airflow is worth the operating surface.
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]]
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]]

## Connected Pipeline Topics

Use these pages for related pipeline concepts and build paths.

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
