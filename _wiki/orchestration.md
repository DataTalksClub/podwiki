---
layout: wiki
title: "Orchestration"
summary: "Orchestration as a control-plane practice for schedules, dependencies, retries, backfills, ETL boundaries, and ML pipelines."
related:
  - Apache Airflow
  - Data Pipelines
  - Data Engineering Platforms
  - DataOps
  - Modern Data Stack
  - ML Platforms
  - Data Quality and Observability
---

Teams use orchestration as the control plane for recurring data and ML work
across tools. An orchestrator decides when jobs run and which upstream work
must finish first. It also records what should retry after a transient failure
and which run history the team can look at later.

The broader concept spans workflow engines, CI/CD systems, cloud schedulers,
and ML pipeline services. Across those tools, teams coordinate schedules and
dependencies while tracking run state and recovery. They also track backfills
and ownership.

For the Airflow-specific version, use [[Apache Airflow]] for DAG files and local
Docker setup. It also covers scheduler/executor behavior and metadata. Logs and
shared deployments stay there too. [[Data Pipelines]] describes the
source-to-output system, and [[How to Build Data Pipelines]] gives the
procedural build order.

[[person:larsalbertsson=>Lars Albertsson]] gives the
clearest platform definition. He places storage and compute next to a workflow
engine at the center of a data platform. The workflow engine defines
dependencies and schedules work when data arrives or on a timer. It retries
when late data, transient infrastructure, or bugs break a run [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

That makes orchestration broader than [[Apache Airflow]]. Airflow and Luigi are
workflow engines, and Prefect, Dagster, and Mage sit in the same family. GitHub
Actions and cloud schedulers can coordinate narrower workflows. AWS Batch,
SageMaker Pipelines, Kubeflow Pipelines, and CI/CD pipelines can too.

The tool choice belongs with [[data engineering platforms]], [[DataOps]], and
[[data pipelines]]. It also belongs with [[data quality and observability]], not
with tool branding alone. A team pays for heavier orchestration when shared run
history, dependency state, retries, and backfills matter more than the cost of
operating the tool.

For build order, use [[How to Build Data Pipelines]], and for portfolio proof,
use [[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]].

## Orchestration Scope

An orchestrator owns order and run state, not every pipeline step.

[[person:nataliekwong=>Natalie Kwong]]
shows scheduling around extract-load work and warehouse-side transformations
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
That boundary connects orchestration to [[ETL]],
[[ETL vs ELT]], [[dbt]],
and the [[modern data stack]].

Albertsson makes the same boundary from the platform side. The workflow engine
records dependencies between transformations and schedules them. Spark, Flink,
SQL, or another compute system performs the processing. He warns against doing
the processing inside the orchestration engine [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

With that boundary, orchestration stays focused on schedules and dependencies.
Retries and recovery belong there too, while
[[data pipelines]] keep extraction
and transformation explicit. They also keep publication and checks explicit.

[[person:santonatuli=>Santona Tuli]] adds the modern
pipeline version by grouping Airflow, Prefect, Dagster, and Mage as
orchestration engines. Which one fits depends on how the team breaks up the
workflow and what transformations the pipeline runs [[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

She gives a staging example where data is written to object storage before a
later workflow or transformation step picks it up. The orchestrator coordinates
the handoff. The storage and transformation layers still do their own jobs
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

## Tool Fit

Orchestration fits recurring work where several jobs need ordering, recovery,
and shared visibility. In an analytics pipeline, a workflow engine may start an
ingestion job and trigger transformations. It may then run a warehouse check and
alert an owner. In a machine-learning pipeline, it may coordinate batch feature
generation and training. It may then run scoring and publication.

In each case, the orchestrator owns the schedule and dependency graph. It also
owns run state and recovery path. The ingestion tool or SQL model owns its own
work. Spark jobs and feature platforms do too. Warehouses and model services
keep their own responsibilities.

The need for orchestration increases when the workflow has several ordered
jobs, partition reruns, shared run history, or retries. It also increases when
teams need alerts and named owners. Data checks before publication, batch ML
jobs, and conventions for many similar pipelines also push teams toward
orchestration.

[[person:andreaskretz=>Andreas Kretz]] gives the lightweight end of that choice
by comparing workflow engines with CloudWatch scheduling and Lambda. He also
names containers, ECS, and AWS Batch. Teams can start with simpler
infrastructure and move to heavier workflow control when they need more logging,
insight, and control [[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].

## Schedules, Dependencies, and Retries

Schedules matter because many data products depend on time-bounded inputs. A
daily warehouse model, an hourly sync, a training dataset, and a batch scoring
table all need timing rules. Dependencies matter because a downstream job
shouldn't publish before the raw input, cleaning step, feature job, or model
artifact exists.

Albertsson ties those two concerns together through the workflow engine. The
engine knows which raw events and batch dumps a recommendation job needs. It
then runs the dependent transformations when the data arrives or on a regular
schedule [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Retries are part of the same design. Albertsson describes late data and
transient failures as normal cases the workflow engine should repair by trying
again. That's why orchestration sits close to
[[DataOps]]. The team needs reproducible
code and dependency control. It also needs recovery paths, not only a timer that
starts a script [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

Batch processing is where this model is most explicit. Albertsson
distinguishes batch from streaming by the programmer's ability to name batches
and dependencies directly. That explicit dependency management makes batch
workflows more forgiving when a team needs reruns, retries, or recovery [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Use [[Batch vs Streaming]]
for the latency tradeoff. Use orchestration when the main question is how runs
depend on each other and how the team recovers from missed or failed work.

## Backfills and Reruns

Backfills turn orchestration from "run today's job" into "recompute a historical
window correctly." Feature platforms make that boundary clear.

[[person:willempienaar=>Willem Pienaar]] separates
upstream transformations from feature serving. Upstream systems such as dbt,
Airflow, or Spark ETL handle transformations. Kubeflow Pipelines fits model
training better than general transformation. Feast relies on upstream jobs to
backfill and then reingest features. Tecton can backfill automatically from a
chosen start date [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]].

Ordinary data engineering has the same problem. If a team changes a metric or
fixes a deduplication rule, the orchestrator may need to rerun old partitions
in the right order. The same applies when a team adds a feature definition.

The transformation system still owns the business logic, but orchestration owns
the sequence and run state. That's why orchestration belongs next to
[[data quality and observability]].
A backfill should tell the team which inputs, code, outputs, and downstream
consumers changed.

## Scheduling Choices Across Tools

Guests describe orchestration as a spectrum rather than a single product
choice. Natalie Kwong shows a workflow engine around Airbyte and dbt
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
Albertsson compares Luigi and Airflow inside a broader platform
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
[[person:santonatuli=>Santona Tuli]] groups Airflow, Prefect, Dagster, and Mage
as orchestration engines for modern pipelines
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

The same workflow may run as a DAG or CI job. It may also run as a managed
scheduler, batch job, or ML pipeline. [[person:adrianbrudaru=>Adrian Brudaru]]
says GitHub Actions can be enough for simple workflows because it avoids the
cost of always-on orchestrators [[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]].
[[person:nemanjaradojkovic=>Nemanja Radojkovic]] keeps orchestration in CI/CD
where possible and chooses Dagster when the workflow needs a real orchestrator
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].

Kretz gives the AWS version with CloudWatch, Lambda, containers, and ECS. He
also names AWS Batch, SageMaker, Airflow, and Kubernetes
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]].

The decision turns on shared state. A small pipeline can use serverless
automation when failure recovery is simple. A team should pay for heavier
orchestration when dependencies, retries, owners, and backfills need shared
history.

## Operating Cost and Alternatives

Every orchestrator adds an operating surface. The tool may need worker
capacity, secrets, connections, and logs. It may also need deployment
discipline and alert owners. Backups, upgrades, and managed access can become
part of the same surface. Those responsibilities are part of the
orchestration decision, not cleanup work after deployment.

Teams should pay that cost when they share tables, dashboards, features, or
batch predictions and need central run state. Heavier
orchestration becomes ceremony when the workflow is one small script, failures
are easy to rerun manually, and no one needs shared task history. [[Apache Airflow]]
covers the Airflow-specific operating surface.

Use a simpler scheduler when a cloud scheduler can start a container or
function. It also fits when no backfill workflow exists yet or when the data
product hasn't proven enough value to justify platform work. Use a workflow
engine when dependencies become hard to track informally.

## ML Pipelines and Batch Inference

Orchestration also appears in [[ML platforms]]
and [[machine learning infrastructure]].

[[person:simonstiebellehner=>Simon Stiebellehner]]
separates batch inference from online serving. For batch inference, a job loads
data and preprocesses it. It runs the model and writes predictions to a table.
Simon says teams often choose a workflow orchestrator such as Airflow or
SageMaker Pipelines for that work. They often use tooling similar to training
pipelines [[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

ML platform products help with some run metadata, but they don't remove the
need to design the end-to-end workflow.

Simon says SageMaker can store metadata such as images, inputs, and outputs. It
can also store pipeline-run connections. A team still has to think through
reproducibility across code and data. Model versions need the same care [[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]].

[[metaflow=>Metaflow]] sits near that ML workflow boundary. It connects modeling
code to cloud and scheduler infrastructure while keeping the practitioner
workflow central
[[cite:devrel-open-source-machine-learning=>DevRel Role for Machine Learning]].
Those concerns connect orchestration to
[[MLOps]] and
[[MLOps Tools]].

It also connects orchestration to experiment tracking, model registries, and
lineage rather than replacing them.

Feature stores create another ML boundary. Pienaar says Feast consumes
transformed features from existing batch or streaming pipelines. Tecton can own
more of the transformation and materialization flow [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]].
Orchestration has to respect where that boundary is.

For Feast, upstream jobs and backfills stay in the existing pipeline stack. For
Tecton, the feature platform may own more of the scheduled transformation and
backfill work.

## Platform Conventions

An orchestrator becomes useful at team scale only when people know how to use
it. Mehdi OUAZZA treats the workflow engine as one platform component and then
adds conventions. Teams need to structure pipelines and handle sequence. They
also need to name things and decide when generic YAML or templates should
generate repeated workflows
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

He says a scale-up may spend about half its data-engineering effort on platform
work. The other half may go to use-case pipelines, because repeated requests
should turn into reusable frameworks [[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

Those conventions keep orchestration tied to
[[data engineering platforms]]
and [[self-service-data-platforms=>self-service data platforms]].
The workflow engine gives teams a place to run and look at jobs. Platform
conventions define owners, schedules, and retries. They also define secrets,
connections, deployment, and recovery paths.

Without these conventions, teams copy workflow definitions and invent naming
rules. They also route alerts inconsistently and make every failure a special
case. A shared workflow engine needs onboarding, reusable templates, playbooks,
and guidance on when a scheduled workflow should exist. [[Apache Airflow]]
covers the Airflow-specific version of those conventions. The broader adoption
problem connects orchestration to [[platform adoption]].

## Quality Boundaries

A successful orchestration run doesn't prove that the data is correct.
[[person:tomaszhinc=>Tomasz Hinc]] gives the warning: Airflow jobs can be green
while zero records were inserted. His point is that task status needs edge-case
checks. It also needs data checks before a team presents results with confidence [[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

Tomasz's example marks the main boundary between orchestration and
[[data quality and observability]].
The orchestrator can show that a task started, retried, failed, or succeeded.
It can also preserve run history and dependency state. It can't prove
freshness and volume. It can't prove schema validity, distribution, lineage
impact, or business correctness.

Those checks need to run inside the workflow or in adjacent observability
systems. The team needs owners who respond when checks fail.

## Learning and Project Scope

For learners, orchestration should come after the pipeline has real steps to
coordinate. [[person:jeffkatz=>Jeff Katz]] places Docker
and AWS after Python and SQL, and puts workflow tooling after
data-warehouse fundamentals in
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]].

The same learning boundary applies regardless of tool, so write the extraction
and transformation clearly first. Add checks and publication paths before an
orchestrator hides weak ownership
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]].

Then add orchestration when schedules, dependencies, retries, or run history
become part of the problem. Backfills belong in the same decision. A learner
can prove the concept with any tool that shows the sequence, failure mode,
recovery path, and data checks. Use [[Apache Airflow]] for DAG-specific learning
and local Docker Compose.

Pin container dependencies when they prove reproducibility
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps]].

Move from a learning setup to shared orchestration when operations become
shared:

- several people deploy workflows.
- logs need retention and search.
- secrets need managed access.
- workers need isolation or autoscaling.
- backfills compete with current runs.
- downstream dashboards, ML jobs, product features, or operational decisions
  depend on the output.

Mehdi's platform point applies here too. The workflow engine is only one
platform component [[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

A useful orchestration project shows more than a workflow screenshot. It shows
why one step waits for another and what happens when an input is late. It also
shows how a failed partition reruns and how a historical window backfills. The
project should show which data checks guard publication and who owns the alert.

The work may still be one script with one simple schedule. In that case,
Brudaru's GitHub Actions example may fit better than a full workflow engine [[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]].

Kretz's CloudWatch and Lambda path may fit too [[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].
Nemanja's CI/CD-first startup path is another small-team option [[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].
