---
layout: wiki
title: "Orchestration"
summary: "Podcast-grounded guide to orchestration across schedules, dependencies, retries, backfills, workflow engines, batch inference, and ETL boundaries."
related:
  - Data Pipelines
  - Data Engineering Platforms
  - DataOps
  - Modern Data Stack
  - Batch vs Streaming
  - ML Platforms
  - Data Quality and Observability
---

Orchestration is the control plane for recurring data and ML work. It decides
when jobs run and which upstream jobs must finish first. It also tracks what
should retry after a transient failure and which run history the team can look
at later.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) gives the
clearest platform definition. In
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
around 30:34, he places storage and compute next to a workflow engine. Those
pieces sit at the center of a data platform. Around 31:18-35:57, he explains that the workflow
engine defines dependencies and schedules work when data arrives or on a timer.
It retries when late data, transient infrastructure, or bugs break a run.

That makes orchestration broader than [Apache Airflow]({{ '/articles/apache-airflow/' | relative_url }}).
Airflow is a common orchestrator, but the archive also discusses Luigi,
Prefect, and Dagster. GitHub Actions appears in the same group. Cloud
schedulers and AWS Batch appear there too. So do SageMaker Pipelines, Kubeflow
Pipelines, and CI/CD pipelines.

[Airflow]({{ '/articles/airflow/' | relative_url }}) and
[Apache Airflow]({{ '/articles/apache-airflow/' | relative_url }}) cover DAG
design, Airflow operations, and Airflow tradeoffs in more detail.

## Orchestration Scope

An orchestrator owns order and run state. It doesn't own every piece of work
inside the pipeline. [Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }})
draws that boundary in
[ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}):
around 30:59-32:11, she places Airflow at the scheduling and orchestration
layer. Airbyte handles extract-load work, while dbt handles warehouse-side SQL
transformations once the data is present. That discussion connects
orchestration to [ETL]({{ '/wiki/etl/' | relative_url }}),
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}), [dbt]({{ '/wiki/dbt/' | relative_url }}),
and the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}).

Albertsson makes the same boundary from the platform side. In his DataOps
episode, the workflow engine records dependencies between transformations.
Spark, Flink, SQL, or another compute system performs the processing. Around
31:18-35:57, he warns against doing the processing inside the orchestration
engine.

That keeps orchestration focused on schedules and dependencies. Retries and
recovery belong there too, while
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) keep extraction
and transformation explicit. They also keep publication and checks explicit.

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) adds the modern
pipeline version in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
Around 26:43-27:07, she names Airflow and Prefect as orchestration engines. She
also names Dagster and Mage. Which one fits depends on how the team breaks up
the workflow and what transformations the pipeline runs.

Around 33:48, she gives a staging example where data is written to object
storage. A later Airflow DAG or dbt model picks it up. The orchestrator
coordinates the handoff. The storage and transformation layers still do their
own jobs.

## Schedules, Dependencies, and Retries

Schedules matter because many data products depend on time-bounded inputs. A
daily warehouse model, an hourly sync, a training dataset, and a batch scoring
table all need timing rules. Dependencies matter because a downstream job
shouldn't publish before the raw input, cleaning step, feature job, or model
artifact exists.

Albertsson's workflow-engine discussion ties those two concerns together. The
engine knows which raw events and source dumps a recommendation job needs. It
then runs the dependent transformations when the data arrives or on a regular
schedule
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
31:18-35:57).

Retries are part of the same design. Albertsson describes
late data and transient failures as normal cases the workflow engine should
repair by trying again. This is why orchestration sits close to
[DataOps]({{ '/wiki/dataops/' | relative_url }}). The team needs reproducible
code and dependency control. It also needs recovery paths, not only a timer that
starts a script
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
31:18-35:57 and 46:52-1:04:18).

Batch processing is where this model is most explicit. Around 45:11,
Albertsson distinguishes batch from streaming by the programmer's ability to
name batches and dependencies directly. That explicit dependency management
makes batch workflows more forgiving when a team needs reruns, retries, or
recovery. Use [Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }})
for the latency tradeoff. Use orchestration when the main question is how runs
depend on each other and how the team recovers from missed or failed work.

## Backfills and Reruns

Backfills turn orchestration from "run today's job" into "recompute a historical
window correctly." The DataTalks.Club archive discusses this most clearly in
feature platforms.

In
[Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
[Willem Pienaar]({{ '/people/willempienaar/' | relative_url }}) separates
upstream transformations from feature serving. Around 24:52-25:22, he says
upstream systems such as dbt, Airflow, or Spark ETL handle transformations.
Kubeflow Pipelines fits model training better than general transformation.
Around 57:42, he explains that Feast relies on upstream jobs to backfill and
then reingest features. Tecton can backfill automatically from a chosen start
date.

That distinction is useful for ordinary data engineering too. If a team changes
a metric or fixes a deduplication rule, the orchestrator may need to rerun old
partitions in the right order. The same applies when a team adds a feature
definition.

The transformation system still owns the business logic, but orchestration owns
the sequence and run state. This is why orchestration belongs next to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
A backfill should tell the team which inputs, code, outputs, and downstream
consumers changed.

## Tool Choices

Airflow remains the common reference point in the archive. Kwong uses it as an
orchestrator around Airbyte and dbt
([ETL vs ELT and Modern Data Engineering]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-35:42). Albertsson compares Luigi and Airflow as workflow orchestrators
inside a broader data platform
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
35:57-39:32).

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) adds the platform
operating view. In
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
around 17:22-19:25, he says an Airflow cluster is only one piece of a data
platform.

Teams also need naming rules and sequencing conventions. Playbooks and
templates keep repeated pipelines from becoming copy-pasted DAGs.

Newer episodes widen the tool set. In
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) says around
35:37 that Airflow is common. Prefect and Dagster are also popular. Around
37:08, he says GitHub Actions can be enough for simple workflows because it's
serverless and cheaper than always-on orchestrators.

In
[Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}),
[Nemanja Radojkovic]({{ '/people/nemanjaradojkovic/' | relative_url }}) gives a
similar small-team rule. Around 44:34-45:01, he keeps the stack minimal and uses
Python for scripts and training. He handles orchestration through CI/CD where
possible. He chooses Dagster when the workflow needs a real orchestrator.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the AWS
version in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 35:46, he compares Airflow with CloudWatch scheduling and Lambda. He
also names containers, ECS, and AWS Batch. SageMaker appears in the same
comparison.

Around 41:06-42:07, he recommends starting with simple infrastructure for early
projects. Teams can move toward Airflow or Kubernetes when they need more
logging. Heavier systems can wait until the team needs more insight and
control.

## ML Pipelines and Batch Inference

Orchestration also appears in [ML platforms]({{ '/wiki/ml-platforms/' | relative_url }})
and [machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

In
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}),
[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }})
separates batch inference from online serving around 31:15-31:51. For batch
inference, a job loads data and preprocesses it. It runs the model and writes
predictions to a table. Simon says teams often choose a workflow orchestrator
such as Airflow or SageMaker Pipelines for that work. They often use tooling
similar to training pipelines.

ML platform products help with some run metadata, but they don't remove the
need to design the end-to-end workflow.

Around 42:48-43:28, Simon says
SageMaker can store metadata such as images, inputs, and outputs. It can also
store pipeline-run connections. A team still has to think through
reproducibility across code and data. Model versions need the same care. That
connects orchestration to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[MLOps Tools]({{ '/articles/mlops-tools/' | relative_url }}).

It also connects orchestration to experiment tracking, model registries, and
lineage rather than replacing them.

Feature stores create another ML boundary. Pienaar says Feast consumes
transformed features from existing batch or streaming pipelines. Tecton can own
more of the transformation and materialization flow
([Feature Stores for MLOps]({{ '/podcasts/mlops-feature-stores-feature-stores-feast-tecton/' | relative_url }}),
24:52-37:00 and 57:42). Orchestration has to respect where that boundary is.

For Feast, upstream jobs and backfills stay in the existing pipeline stack. For
Tecton, the feature platform may own more of the scheduled transformation and
backfill work.

## Platform Conventions

An orchestrator becomes useful at team scale only when people know how to use
it. Mehdi's scale-up episode is the clearest archive example. He treats Airflow
as one platform component and then adds conventions. Teams need to structure
pipelines and handle sequence. They also need to name things and decide when
generic YAML or templates should generate repeated DAGs
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
17:22-19:25).

Around 52:55-53:21, he says a scale-up may spend about half its
data-engineering effort on platform work. The other half may go to use-case
pipelines, because repeated requests should turn into reusable frameworks.

That keeps orchestration tied to
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).
The workflow engine gives teams a place to run and look at jobs. Platform
conventions define owners, schedules, and retries. They also define secrets,
connections, deployment, and recovery paths.

## Quality Boundaries

A successful orchestration run doesn't prove that the data is correct.
[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) gives the warning in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
Around 1:02:28-1:05:41, he describes Airflow jobs that were green while zero
records were inserted. His point is that task status needs edge-case checks.
It also needs data checks before a team presents results with confidence.

This is the main boundary between orchestration and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
The orchestrator can show that a task started, retried, failed, or succeeded.
It can also preserve run history and dependency state. It can't prove
freshness and volume. It can't prove schema validity, distribution, lineage
impact, or business correctness.

Those checks need to run inside the workflow or in adjacent observability
systems. The team needs owners who respond when checks fail.

## Learning and Project Scope

For learners, orchestration should come after the pipeline has real steps to
coordinate. [Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) places Docker
and AWS after Python and SQL. Airflow also comes after data-warehouse
fundamentals in
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).

Around 55:10, he says good Airflow code keeps most logic in normal Python and
doesn't rely on Airflow for everything. That advice fits the broader archive.
Write the extraction and transformation clearly first. Add checks and
publication paths before the orchestrator hides weak ownership.

Then add orchestration when schedules, dependencies, retries, or backfills
become part of the problem. Run history belongs in that decision too.

A useful orchestration project therefore shows more than a DAG screenshot. It
shows why one step waits for another and what happens when an input is late.
It also shows how a failed partition reruns and how a historical window
backfills. The project should show which data checks guard publication and who
owns the alert.

The work may still be one script with one simple schedule. In that case,
Brudaru's GitHub Actions example may fit better than a full Airflow deployment
([Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
35:37-37:08).

Kretz's CloudWatch and Lambda path may fit too
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
35:46-42:07). Nemanja's CI/CD-first startup path is another small-team option
([Lean MLOps for Startups]({{ '/podcasts/lean-mlops-for-startups/' | relative_url }}),
44:34-45:01).
