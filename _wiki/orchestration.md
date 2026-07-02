---
layout: wiki
title: "Orchestration and Airflow"
summary: "Podcast-grounded guide to orchestration and Airflow across schedules, DAGs, dependencies, retries, backfills, platform conventions, batch inference, and ETL boundaries."
related:
  - Apache Airflow
  - Data Pipelines
  - Data Engineering Platforms
  - DataOps
  - Modern Data Stack
  - ML Platforms
  - Data Quality and Observability
---

Orchestration is the control plane for recurring data and ML work. It decides
when jobs run and which upstream jobs must finish first. It also tracks what
should retry after a transient failure and which run history the team can look
at later.

[Lars Albertsson](https://datatalks.club/people/larsalbertsson.html) gives the
clearest platform definition. In
[DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
around 30:34, he places storage and compute next to a workflow engine. Those
pieces sit at the center of a data platform. Around 31:18-35:57, he explains
that the workflow engine defines dependencies and schedules work when data
arrives or on a timer. It retries when late data, transient infrastructure, or
bugs break a run.

That makes orchestration broader than
[Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}). Airflow is a
common orchestrator, but guests also discuss Luigi, Prefect, and Dagster. GitHub
Actions appears in the same group. Cloud schedulers and AWS Batch appear there
too. So do SageMaker Pipelines, Kubeflow Pipelines, and CI/CD pipelines.

Airflow earns its place when a team needs shared run history, dependency state,
retries, and backfills for recurring workflows. Use
[Apache Airflow]({{ '/wiki/apache-airflow/' | relative_url }}) for the
Airflow-specific tool boundary and DAG design. It's often too much when one
small script can run from cron, a cloud scheduler, or GitHub Actions. Teams
should treat that choice as part of [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). It also belongs with
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
not with tool branding alone.

## Orchestration Scope

An orchestrator owns order and run state. It doesn't own every piece of work
inside the pipeline. [Natalie Kwong](https://datatalks.club/people/nataliekwong.html)
draws that boundary in
[ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html):
around 30:59-32:11, she places Airflow at the scheduling and orchestration
layer. Airbyte handles extract-load work, while dbt handles warehouse-side SQL
transformations once the data is present. Her discussion connects orchestration
to [ETL]({{ '/wiki/etl/' | relative_url }}),
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}), [dbt]({{ '/wiki/dbt/' | relative_url }}),
and the [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}).

Albertsson makes the same boundary from the platform side. In his DataOps
episode, the workflow engine records dependencies between transformations.
Spark, Flink, SQL, or another compute system performs the processing. Around
31:18-35:57, he warns against doing the processing inside the orchestration
engine.

With that boundary, orchestration stays focused on schedules and dependencies.
Retries and recovery belong there too, while
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) keep extraction
and transformation explicit. They also keep publication and checks explicit.

[Santona Tuli](https://datatalks.club/people/santonatuli.html) adds the modern
pipeline version in
[Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html).
Around 26:43-27:07, she names Airflow and Prefect as orchestration engines. She
also names Dagster and Mage. Which one fits depends on how the team breaks up
the workflow and what transformations the pipeline runs.

Around 33:48, she gives a staging example where data is written to object
storage. A later Airflow DAG or dbt model picks it up. The orchestrator
coordinates the handoff. The storage and transformation layers still do their
own jobs.

## Airflow Fit

Airflow fits recurring data work where several jobs need ordering, recovery,
and shared visibility. In an analytics pipeline, Airflow may start an
Airbyte-style ingestion job and trigger dbt models. It may then run a warehouse
check and alert an owner. In a machine-learning pipeline, it may run batch
feature generation and training. It may then score entities and publish the
output.

In both cases, Airflow owns the schedule and dependency graph. The ingestion
tool or SQL model owns its own work. Spark jobs, warehouses, feature stores,
and model services do too.

Natalie's modern stack episode gives the clearest archive boundary for
analytics work. Around 30:59-31:31, she separates Airbyte-style extract-load
work from dbt-style transformation. She puts Airflow around that flow
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html)).
With that split, teams can connect Airflow to Airbyte-style ingestion,
[dbt]({{ '/wiki/dbt/' | relative_url }}), and [ELT]({{ '/wiki/elt/' | relative_url }}).
Airflow stays connected to [data engineering tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
without replacing them.

Airflow fits better when the pipeline has more than a timer:

- several jobs that must run in order.
- scheduled backfills or partition reruns.
- shared run history for several teams.
- retries, alerts, and named owners.
- data checks before publication.
- batch ML jobs that need reproducible sequencing.
- conventions for many similar pipelines.

Teams should weigh those operating needs before choosing the tool.
[Andreas Kretz](https://datatalks.club/people/andreaskretz.html) compares Airflow
with CloudWatch scheduling and Lambda around 35:46 in
[From Notebooks to Production](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html).
He also names containers, ECS, and AWS Batch.
Around 41:06-42:07, he recommends starting with simple infrastructure and
moving toward Airflow or Kubernetes when the team needs more logging, insight,
and control.

## Airflow DAG Architecture

Airflow expresses workflows as directed acyclic graphs, usually called DAGs.
Each task is a node. Edges describe which task must finish before another task
can start. DAG files describe the schedule and dependencies. They also record
owners, retry rules, and calls into the real work.

An Airflow deployment also has runtime pieces that explain why it costs more
to operate than cron. The scheduler reads DAG definitions and picks ready task
instances. The executor sends tasks to local processes or queued workers. It
can also send them to containers or Kubernetes pods.

The metadata database stores run state for DAGs and tasks, plus schedules,
connections, and retry history. The web UI lets engineers look at run status,
logs, and failures. It also shows dependencies and retries.

Because Airflow stores run state and logs, people can see what happened after a
failure. The same architecture creates platform work. Someone has to own
upgrades and worker capacity.

They also have to own Python dependencies, secrets, and permissions. Database
backups and log retention need owners too.
[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html)
treats an Airflow cluster as one part of a larger platform, not as the whole
platform
([Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
17:22-19:25).

Good DAGs keep orchestration thin. Put business transformations in dbt, SQL,
Spark, or Python modules where the team can review and test them. Pass durable
references between tasks.

Use table names and partitions as references, along with file paths, model
versions, and run IDs. Add checks before publishing downstream outputs, and
name DAGs and tasks so an on-call engineer can understand an alert quickly.

[Jeff Katz](https://datatalks.club/people/jeffkatz.html) makes the code-structure
version of that advice in
[Data Engineering Career Path and Skills](https://datatalks.club/podcast/data-engineering-career-path-and-skills.html).
Around 55:10, he says good Airflow code keeps most logic in normal Python
instead of relying on Airflow for everything. Santona's pipeline discussion
points the same way. Airflow and Prefect coordinate workflows whose
transformation responsibilities are already clear. Dagster and Mage appear in
the same orchestration set
([Modern Data Pipeline Architecture](https://datatalks.club/podcast/modern-data-pipelines-orchestration-ingestion-modeling.html),
26:43-27:07).

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
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
31:18-35:57).

Retries are part of the same design. Albertsson describes late data and
transient failures as normal cases the workflow engine should repair by trying
again. That's why orchestration sits close to
[DataOps]({{ '/wiki/dataops/' | relative_url }}). The team needs reproducible
code and dependency control. It also needs recovery paths, not only a timer that
starts a script
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
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
window correctly." Guests discuss this most clearly in feature platforms.

In
[Feature Stores for MLOps](https://datatalks.club/podcast/mlops-feature-stores-feature-stores-feast-tecton.html),
[Willem Pienaar](https://datatalks.club/people/willempienaar.html) separates
upstream transformations from feature serving. Around 24:52-25:22, he says
upstream systems such as dbt, Airflow, or Spark ETL handle transformations.
Kubeflow Pipelines fits model training better than general transformation.
Around 57:42, he explains that Feast relies on upstream jobs to backfill and
then reingest features. Tecton can backfill automatically from a chosen start
date.

Ordinary data engineering has the same problem. If a team changes a metric or
fixes a deduplication rule, the orchestrator may need to rerun old partitions
in the right order. The same applies when a team adds a feature definition.

The transformation system still owns the business logic, but orchestration owns
the sequence and run state. That's why orchestration belongs next to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
A backfill should tell the team which inputs, code, outputs, and downstream
consumers changed.

## Tool Choices

Airflow remains the common reference point. Kwong uses it as an
orchestrator around Airbyte and dbt
([ETL vs ELT and Modern Data Engineering](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html),
30:59-35:42). Albertsson compares Luigi and Airflow as workflow orchestrators
inside a broader data platform
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
35:57-39:32).

[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) adds the platform
operating view. In
[Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
around 17:22-19:25, he says an Airflow cluster is only one piece of a data
platform.

Teams also need naming rules and sequencing conventions. Playbooks and
templates keep repeated pipelines from becoming copy-pasted DAGs.

Newer episodes widen the tool set. In
[Modern Data Engineering Trends](https://datatalks.club/podcast/trends-in-modern-data-engineering.html),
[Adrian Brudaru](https://datatalks.club/people/adrianbrudaru.html) says around
35:37 that Airflow is common. Prefect and Dagster are also popular. Around
37:08, he says GitHub Actions can be enough for simple workflows because it's
serverless and cheaper than always-on orchestrators.

In
[Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html),
[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) gives a
similar small-team rule. Around 44:34-45:01, he keeps the stack minimal and uses
Python for scripts and training. He handles orchestration through CI/CD where
possible. He chooses Dagster when the workflow needs a real orchestrator.

[Andreas Kretz](https://datatalks.club/people/andreaskretz.html) gives the AWS
version in
[From Notebooks to Production](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html).
Around 35:46, he compares Airflow with CloudWatch scheduling and Lambda. He
also names containers, ECS, and AWS Batch. SageMaker appears in the same
comparison.

Around 41:06-42:07, he recommends starting with simple infrastructure for early
projects. Teams can move toward Airflow or Kubernetes when they need more
logging. Heavier systems can wait until the team needs more insight and
control.

## Operating Cost and Alternatives

Airflow's metadata database and UI make it more than a scheduler, but those
same pieces create ongoing cost. Workers need capacity for current runs and
backfills. Secrets and connections need managed access.

Python dependencies need versioning and deployment discipline, and logs need to
be available when a task fails. Alerts need clear owners, and the metadata
database needs backups and upgrades.

Those responsibilities are part of the Airflow decision, not cleanup work after
deployment.

Teams should pay that cost when they share tables, dashboards, features, or
batch predictions and need one place to reason about run state. Airflow becomes
ceremony when the workflow is one small script, failures are easy to rerun
manually, and no one needs shared task history.

[Adrian Brudaru](https://datatalks.club/people/adrianbrudaru.html) gives the
lighter-weight option in
[Modern Data Engineering Trends](https://datatalks.club/podcast/trends-in-modern-data-engineering.html).
Around 35:37, he names Airflow alongside Prefect, Dagster, and GitHub Actions.
Around 37:08, he says GitHub Actions can be enough for simple workflows
because it avoids the cost of always-on orchestrators.

[Nemanja Radojkovic](https://datatalks.club/people/nemanjaradojkovic.html) makes a
similar startup argument in
[Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html).
Around 44:34-45:01, he keeps orchestration in CI/CD where possible. He chooses
Dagster when the workflow needs a real orchestrator.

Use a simpler scheduler when a cloud scheduler can start a container or
function. It also fits when no backfill workflow exists yet or when the data
product hasn't proven enough value to justify platform work. Use Airflow or a
peer orchestrator when dependencies, ownership, retries, and recovery become
hard to track informally.

## ML Pipelines and Batch Inference

Orchestration also appears in [ML platforms]({{ '/wiki/ml-platforms/' | relative_url }})
and [machine learning infrastructure]({{ '/wiki/machine-learning-infrastructure/' | relative_url }}).

In
[Building Production ML Platforms](https://datatalks.club/podcast/building-production-ml-platform-and-mlops-team.html),
[Simon Stiebellehner](https://datatalks.club/people/simonstiebellehner.html)
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
reproducibility across code and data. Model versions need the same care. Those
concerns connect orchestration to
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[MLOps Tools]({{ '/wiki/mlops-tools/' | relative_url }}).

It also connects orchestration to experiment tracking, model registries, and
lineage rather than replacing them.

Feature stores create another ML boundary. Pienaar says Feast consumes
transformed features from existing batch or streaming pipelines. Tecton can own
more of the transformation and materialization flow
([Feature Stores for MLOps](https://datatalks.club/podcast/mlops-feature-stores-feature-stores-feast-tecton.html),
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
([Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
17:22-19:25).

Around 52:55-53:21, he says a scale-up may spend about half its
data-engineering effort on platform work. The other half may go to use-case
pipelines, because repeated requests should turn into reusable frameworks.

Those conventions keep orchestration tied to
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}).
The workflow engine gives teams a place to run and look at jobs. Platform
conventions define owners, schedules, and retries. They also define secrets,
connections, deployment, and recovery paths.

Without these conventions, teams copy DAGs and invent naming rules. They also
route alerts inconsistently and make every failure a special case. A shared
Airflow cluster needs onboarding, reusable DAG structures, playbooks, and
guidance on when a DAG should exist. Airflow connects to
[platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}) when teams
can use it without asking platform engineers to design every pipeline by hand.

## Quality Boundaries

A successful orchestration run doesn't prove that the data is correct.
[Tomasz Hinc](https://datatalks.club/people/tomaszhinc.html) gives the warning in
[DataOps and GitOps Best Practices for Data Teams](https://datatalks.club/podcast/dataops-and-gitops-best-practices-for-data-teams.html).
Around 1:02:28-1:05:41, he describes Airflow jobs that were green while zero
records were inserted. His point is that task status needs edge-case checks.
It also needs data checks before a team presents results with confidence.

Tomasz's example marks the main boundary between orchestration and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
The orchestrator can show that a task started, retried, failed, or succeeded.
It can also preserve run history and dependency state. It can't prove
freshness and volume. It can't prove schema validity, distribution, lineage
impact, or business correctness.

Those checks need to run inside the workflow or in adjacent observability
systems. The team needs owners who respond when checks fail.

## Learning and Project Scope

For learners, orchestration should come after the pipeline has real steps to
coordinate. [Jeff Katz](https://datatalks.club/people/jeffkatz.html) places Docker
and AWS after Python and SQL. Airflow also comes after data-warehouse
fundamentals in
[Data Engineering Career Path and Skills](https://datatalks.club/podcast/data-engineering-career-path-and-skills.html).

Around 55:10, he says good Airflow code keeps most logic in normal Python and
doesn't rely on Airflow for everything. Write the extraction and transformation
clearly first. Add checks and publication paths before the orchestrator hides
weak ownership.

Then add orchestration when schedules, dependencies, retries, or backfills
become part of the problem. Run history belongs in that decision too.

Local Docker Compose fits that learning path. Use it to run the Airflow web UI,
scheduler, and metadata database. Add mounted DAG files, logs, and workers when
a local project needs them. The
[Airflow Docker Compose how-to]({{ '/wiki/airflow-docker-compose/' | relative_url }})
keeps the local setup workflow separate from this concept page.

Running those pieces locally helps a learner see the scheduler and UI. It also
shows how task execution, metadata, and logs relate to each other. It's useful
for developing DAGs before deploying them to a shared environment.
It can also test imports inside containers, support teaching, or make a
portfolio project repeatable for a reviewer.

Keep Compose small by starting with one DAG that calls real Python, SQL, dbt,
or Spark work. Mount the DAG and supporting code into the Airflow containers.
Persist metadata and logs so a failed run can be inspected after restart.

Add data checks before trusting a green run. Add worker-based execution only
when the project needs task isolation or concurrency.

Docker Compose isn't a production Airflow deployment.

Move beyond it when the workflow has shared operations:

- several people deploy DAGs.
- logs need retention and search.
- secrets and connections need managed access.
- workers need isolation or autoscaling.
- backfills compete with current runs.
- downstream dashboards, ML jobs, product features, or operational decisions
  depend on the output.

Mehdi's platform discussion applies here too. Even a shared Airflow cluster is
only one platform component. A local Compose file is further from a platform
than that
([Scaling Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
17:22-19:25).

A useful orchestration project therefore shows more than a DAG screenshot. It
shows why one step waits for another and what happens when an input is late.
It also shows how a failed partition reruns and how a historical window
backfills. The project should show which data checks guard publication and who
owns the alert.

The work may still be one script with one simple schedule. In that case,
Brudaru's GitHub Actions example may fit better than a full Airflow deployment
([Modern Data Engineering Trends](https://datatalks.club/podcast/trends-in-modern-data-engineering.html),
35:37-37:08).

Kretz's CloudWatch and Lambda path may fit too
([From Notebooks to Production](https://datatalks.club/podcast/production-ml-pipelines-with-aws-and-kafka.html),
35:46-42:07). Nemanja's CI/CD-first startup path is another small-team option
([Lean MLOps for Startups](https://datatalks.club/podcast/lean-mlops-for-startups.html),
44:34-45:01).
