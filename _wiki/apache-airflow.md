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

[[person:nataliekwong|Natalie Kwong]] gives the
clearest tool boundary in
[[podcast:data-engineering-tools-modern-data-stack|30:59|ETL vs ELT and Modern Data Engineering]].
She places Airflow around scheduling and orchestration. Airbyte handles
extract-load work, while [[dbt]] handles
warehouse-side SQL transformations. That makes Airflow adjacent to
[[ETL]],
[[ELT]], and the
[[ETL vs ELT]] decision.

## Scheduling and Dependency State

Airflow is useful when a workflow needs more than a timer. A team usually
chooses it when several tasks must run in order. It also fits when failures need
visible logs, retries and reruns matter, or a group needs shared run history.

The DAG describes the order, and the scheduler decides which task instances can
run. The metadata database stores DAG runs and task state. It also stores
schedules, retries, connections, and logs.

[[person:larsalbertsson|Lars Albertsson]] describes the
platform version in
[[podcast:dataops-principles-and-scalable-data-platforms|30:34|DataOps 101 for Scaling Data Platforms]].
He puts storage, compute, and a workflow engine at the center of a data
platform. Around 31:18-35:57, he explains that the workflow engine tracks
dependencies and schedules work when data arrives. It can also run on a timer
and retry after late data or transient failures.

In Albertsson's framing, Airflow stays inside
[[orchestration]]. Teams still need
[[data quality and observability]]
because a green DAG run proves that tasks finished. It doesn't prove the data
is fresh, complete, valid, or useful.

## Platform Cost and Simpler Alternatives

Airflow is the common reference point for orchestration, but the interviews do
not treat it as the default answer for every scheduled job. Teams should ask
whether the workflow needs shared run state, dependency control, recovery, and a
team-facing operating surface.

Natalie uses Airflow as the scheduler around a modern analytics stack. Her
example separates Airflow from Airbyte and dbt, so the tool choice doesn't
blur ingestion and transformation. It also keeps orchestration separate
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and Modern Data Engineering]],
30:59-35:42).

Albertsson starts from platform reliability. In his
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps episode]],
Airflow and Luigi sit in the workflow-engine category. The important point is
dependency control, recovery, and reproducible operations, not the brand of the
orchestrator.

[[person:mehdiouazza|Mehdi OUAZZA]] warns against
treating the Airflow cluster as the whole platform. In
[[podcast:scaling-data-engineering-teams-self-service-platforms|17:22|Scaling Data Engineering Teams]],
he adds naming conventions and sequencing rules. He also adds playbooks,
templates, and onboarding. Airflow provides the shared place to run DAGs. The
platform still needs conventions that help many teams use it consistently.

[[person:adrianbrudaru|Adrian Brudaru]] gives the
lightweight alternative. In
[[podcast:trends-in-modern-data-engineering|35:37|Modern Data Engineering Trends]],
he names Airflow and GitHub Actions as workflow options. Prefect and Dagster
appear in the same comparison. Around 37:08, he says GitHub Actions can be
enough for simple workflows because it avoids the cost of always-on
orchestration.

[[person:andreaskretz|Andreas Kretz]] makes a similar
AWS comparison in
[[podcast:production-ml-pipelines-with-aws-and-kafka|35:46|From Notebooks to Production]].
He compares Airflow with CloudWatch scheduling and Lambda. He also names
containers, ECS, AWS Batch, and SageMaker. Around 41:06-42:07, he recommends
starting simple and moving toward Airflow or Kubernetes when the team needs
more logging, insight, and control.

## DAG Design

Airflow workflows are written as directed acyclic graphs. A DAG should describe
the sequence of work, schedule, retry behavior, and owners. Parameters belong
there too. The DAG should call into real processing code. It shouldn't become a
pile of business logic that's hard to test outside Airflow.

[[person:jeffkatz|Jeff Katz]] gives the learner-facing
version in
[[podcast:data-engineering-career-path-and-skills|55:10|Data Engineering Career Path and Skills]].
Good Airflow code keeps most logic in normal Python instead of relying on
Airflow for everything. For a data engineering project, the DAG can call Python
modules, SQL, and dbt commands. It can also call Spark jobs or containerized
steps while tests stay close to the code that owns the logic.

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

[[person:tomaszhinc|Tomasz Hinc]] gives the clearest
failure mode in
[[podcast:dataops-and-gitops-best-practices-for-data-teams|1:02:28|DataOps and GitOps Best Practices for Data Teams]].
He describes Airflow jobs that were green while zero records were inserted.
The run status looked successful, but the data product was wrong. Teams should
add edge-case checks and data assertions before they trust the result.

Teams need this boundary when they add
[[data-quality-and-observability|data observability]] and
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

Albertsson connects this to batch processing and recovery in
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101]].
Around 45:11, he contrasts batch and streaming through explicit dependency
management. Batch workflows are easier to rerun when the team can name the
inputs and dependencies. Airflow fits batch pipelines with backfills especially
well, while [[Batch vs Streaming]]
covers the broader processing tradeoff.

Machine learning pipelines use the same structure. In
[[podcast:building-production-ml-platform-and-mlops-team|31:15|Building Production ML Platforms]],
[[person:simonstiebellehner|Simon Stiebellehner]]
separates batch inference from online serving. Batch inference often uses a
workflow orchestrator such as Airflow or SageMaker Pipelines to load data,
preprocess it, run the model, and write predictions. Teams using Airflow this
way also connect it to
[[MLOps]],
[[ML platforms]], and
[[machine learning infrastructure]].

## Local Learning and Portfolio Use

Airflow is a strong portfolio signal only when it coordinates a real pipeline.
It's weaker when the project is just a DAG screenshot. A useful project should
show why one task waits for another. It should also show what happens when an
input is late. A bad input should fail visibly, and the project should show how
a rerun or backfill works after the issue is fixed.

[[person:danielegbo|Daniel Egbo]] gives a concrete
local setup example in
[[podcast:from-radio-astronomy-to-machine-learning-and-data-engineering|42:48|From Radio Astronomy to Machine Learning and Data Engineering]].
He discusses course projects with Airflow, MinIO, Spark, and MySQL. The setup
also includes Docker Compose and the Airflow web server. He uses environment
variables and a warehouse path in the same project.

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
