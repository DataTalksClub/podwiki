---
layout: wiki
title: "Apache Airflow"
summary: "How podcast guests use Apache Airflow for scheduled data workflows, DAGs, dependencies, retries, backfills, and the platform work around orchestration."
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

Apache Airflow is a workflow orchestrator for recurring data and machine
learning work. Teams use it to define DAGs, schedule jobs, and track
dependencies. They also use it to retry failed tasks, look at logs, and rerun
historical work. Guests mention Airflow most often around
[[data pipelines]],
[[DataOps]],
[[data engineering platforms]],
and the [[modern data stack]].

Guests usually treat Airflow as coordination infrastructure, not as the place
where all pipeline logic should live. The ingestion tool or warehouse job
should still own the transformation logic. So should the Spark job, dbt project,
feature pipeline, or Python module. Airflow owns the schedule, dependency
graph, run state, and visibility around those steps.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

One modern-stack boundary puts Airflow around scheduling and orchestration while
Airbyte owns extract-load work. In the same stack, [[dbt]] owns
warehouse-side SQL transformations and Airflow stays adjacent to the [[ETL]] and
[[ELT]] workflow boundary captured in [[ETL vs ELT]].
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

## Scheduling and Dependency State

Airflow is useful when a workflow needs more than a timer. A team usually
chooses it when several tasks must run in order. It also fits when failures need
visible logs, retries and reruns matter, or a group needs shared run history.

The DAG describes the order, and the scheduler decides which task instances can
run. The metadata database stores DAG runs and task state. It also stores
schedules, retries, connections, and logs.

Data platform designs often place storage, compute, and a workflow engine at
the center of the operating model. The workflow engine tracks dependencies,
schedules work when data arrives, runs timer-based jobs, and retries after late
data or transient failures.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

In that framing, Airflow stays inside
[[orchestration]]. Teams still need
[[data quality and observability]]
because a green DAG run proves that tasks finished. It doesn't prove the data
is fresh, complete, valid, or useful.

## Platform Cost and Simpler Alternatives

Airflow is the common reference point for orchestration, but the interviews do
not treat it as the default answer for every scheduled job. Teams should ask
whether the workflow needs shared run state, dependency control, recovery, and a
team-facing operating surface.

Airflow can be the scheduler around a modern analytics stack without owning
ingestion or transformation. Separating Airflow from Airbyte and dbt keeps
orchestration distinct from extract-load and warehouse transformation work.
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Engineering Tools]]

Platform reliability discussions put Airflow and Luigi in the workflow-engine
category. The important point is dependency control, recovery, and reproducible
operations, not the brand of the orchestrator.
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]]

An Airflow cluster isn't the whole data platform. Self-service data platforms
also need naming conventions and sequencing rules. Playbooks, templates, and
onboarding help many teams use the shared DAG surface consistently.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]

Simple workflows may not need always-on orchestration. Airflow sits in the same
workflow-options conversation as GitHub Actions, Prefect, and Dagster. GitHub
Actions can be enough when the team only needs a small scheduled workflow.
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]]

AWS workflows can start with CloudWatch scheduling, Lambda, or containers before
the team takes on Airflow or Kubernetes. ECS, AWS Batch, and SageMaker are part
of the same simple-first path. Move toward the heavier orchestrator when
logging, insight, and control justify the extra platform surface.
[[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]]

## DAG Design

Airflow workflows are written as directed acyclic graphs. A DAG should describe
the sequence of work, schedule, retry behavior, and owners. Parameters belong
there too. The DAG should call into real processing code. It shouldn't become a
pile of business logic that's hard to test outside Airflow.

Good Airflow code keeps most logic in normal Python instead of relying on
Airflow for everything. For a data engineering project, the DAG can call Python
modules, SQL, and dbt commands. It can also call Spark jobs or containerized
steps while tests stay close to the code that owns the logic.
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path]]

Thin DAGs also make review easier. A reviewer can read the DAG to understand
the order of steps, then look at the actual transformation code in the
repository. That links Airflow to
[[data engineering portfolio projects]].
DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
is the canonical local setup guide. Use this wiki page for the concept and
operating boundary.

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

Course-style projects can combine Airflow with MinIO, Spark, and MySQL. The
same local setup can include Docker Compose, the Airflow web server,
environment variables, and a warehouse path.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering=>Radio Astronomy to Data Engineering]]

Follow DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
for a local development or portfolio environment. Keep Compose small by
using one DAG and a few real pipeline steps. Mount the code, keep logs visible,
and add one data check that can fail.

Move to a shared Airflow deployment only when more people need it. Secrets,
worker isolation, log
retention, and alerts can also justify the platform work. Backfills can too.

## Related Pages

These pages cover the concepts and comparisons used above.

- [[Orchestration]]
- [[Data Pipelines]]
- [[Data Engineering Tools]]
- [[DataOps]]
- [[Data Quality and Observability]]
- [[dbt]]
- [[ETL vs ELT]]
- [[Batch vs Streaming]]
