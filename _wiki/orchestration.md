---
layout: wiki
title: "Orchestration"
summary: "Orchestration as run coordination across workflow engines, CI jobs, cloud schedulers, managed batch services, analytics refreshes, and ML pipelines."
related:
  - Apache Airflow
  - Data Pipelines
  - Data Engineering Platforms
  - DataOps
  - Modern Data Stack
  - ML Platforms
  - Data Quality and Observability
---

Teams use orchestration to coordinate recurring data, analytics, and ML work
across tools. The orchestrated run names when work starts, which upstream work
must finish first, and what should retry after a transient failure. It also
keeps run history that the team can look at later
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

The broader concept spans several operating surfaces. Workflow engines and
CI/CD systems can coordinate work, and cloud schedulers can cover narrower jobs.
Analytics refresh jobs, batch-processing services, and ML pipeline services can
do the same. Across those tools, teams coordinate schedules and dependency
state. They also track recovery, backfills, and ownership.

Use orchestration for the decision layer, including trigger policy and
dependency state. Recovery behavior, run history, and owner handoff fit there
too. Tool-specific pages such as [[Apache Airflow]] cover product details.

The control-plane question appears when schedules and dependencies span a
workflow engine or CI/CD system. It also appears across cloud schedulers, managed
jobs, and ML pipeline services. Recovery, backfills, ownership, and run history
belong in the same decision. [[Apache Airflow]] owns the concrete DAG-engine
version of that discussion, including local Docker Compose setup and shared
Airflow deployments.
[[Data Pipelines]] describes the source-to-output system, and
[[How to Build Data Pipelines]] gives the procedural build order.

[[person:larsalbertsson=>Lars Albertsson]] gives the
clearest platform definition. He places storage and compute next to a workflow
engine at the center of a data platform. The workflow engine defines
dependencies and schedules work when data arrives or on a timer. It retries
when late data, transient infrastructure, or bugs break a run [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].

That makes orchestration broader than [[Apache Airflow]]. Airflow and Luigi are
workflow engines, while Prefect, Dagster, and Mage sit in the same family.
GitHub Actions and cloud schedulers can coordinate narrower workflows. AWS Batch
and SageMaker Pipelines can coordinate ML or batch work. Kubeflow Pipelines and
CI/CD pipelines can do the same when their operating model fits the team's
recovery needs.

The tool choice belongs with [[data engineering platforms]], [[DataOps]], and
[[data pipelines]]. It also belongs with [[data quality and observability]], not
with tool branding alone. A team pays for heavier orchestration when shared run
history matters. Dependency state, retries, and backfills need to matter more
than the cost of operating the chosen control plane.

[[How to Build Data Pipelines]] owns build order, while
[[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]] owns
portfolio proof.

## Orchestration Scope

Teams use an orchestrator to track order and run state, not to perform every
pipeline step.

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

With that boundary, teams keep orchestration focused on schedules and
dependencies. Retries and recovery fit there too. [[Data pipelines]] keep
extraction, transformation, publication, and checks explicit.

[[person:santonatuli=>Santona Tuli]] adds the modern
pipeline version by grouping Airflow, Prefect, Dagster, and Mage as
orchestration engines. The choice depends on how the team breaks up the work and
what transformations the pipeline runs [[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

She gives a staging example where data is written to object storage before a
later workflow or transformation step picks it up. The orchestrator coordinates
the handoff. The storage and transformation layers still do their own jobs
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

## Control Plane Fit Across Schedulers

Orchestration fits recurring work where several jobs need ordering, recovery,
and shared visibility. In an analytics pipeline, the control plane may start
ingestion and trigger transformations. It may then run a warehouse check and
alert an owner. In a machine-learning pipeline, it may coordinate batch feature
generation and training. It may then run scoring and publication.

In each case, the scheduler coordinates the schedule and dependency graph. It
tracks run state and the recovery path. The ingestion tool or SQL model still
performs its own work. Spark jobs and feature platforms do too. Warehouses and
model services keep their own responsibilities.

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

Use [[dataops-vs-data-engineering=>DataOps vs Data Engineering]] when that
same workflow raises an ownership question. Data engineering defines the jobs
and dependencies. DataOps keeps repeated runs reviewed, checked, and
recoverable.

Batch processing is where this model is most explicit. Albertsson
distinguishes batch from streaming by the programmer's ability to name batches
and dependencies directly. That explicit dependency management makes batch
workflows more forgiving when a team needs reruns, retries, or recovery [[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
[[Batch vs Streaming]] owns the latency tradeoff. Orchestration owns the
question of how runs depend on each other and how the team recovers from missed
or failed work.

## Cross-Tool Backfills and Reruns

Backfills turn orchestration from "run today's job" into "recompute a historical
window correctly." Feature platforms make that boundary clear.

[[person:willempienaar=>Willem Pienaar]] separates
upstream transformations from feature serving. Upstream systems such as dbt,
Airflow, or Spark ETL handle transformations. Kubeflow Pipelines fits model
training better than general transformation. Feast relies on upstream jobs to
backfill and then reingest features. Tecton can backfill automatically from a
chosen start date [[cite:mlops-feature-stores-feature-stores-feast-tecton=>Feature Stores for MLOps]].

Ordinary data engineering has the same problem. If a team changes a metric or
fixes a deduplication rule, the chosen control plane may need to rerun old
partitions in the right order. The same applies when a team adds a feature
definition. [[Apache Airflow]] covers the DAG-run version of this recovery
work.

The transformation system still runs the business logic, but the orchestrator
tracks the sequence and run state. That's why orchestration belongs next to
[[data quality and observability]].
A backfill should tell the team which inputs, code, outputs, and downstream
consumers changed.

## Scheduling Choices Across Tool Families

Orchestration choices form a spectrum rather than a single product choice. One
modern-stack example puts a workflow engine around Airbyte and dbt
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
Albertsson compares Luigi and Airflow inside a broader platform
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]].
Airflow, Prefect, Dagster, and Mage all appear as orchestration engines for
modern pipelines
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

The same workflow may run as a DAG or CI job. It may also run as a managed
scheduler, batch job, or ML pipeline. Use [[Apache Airflow]] for Airflow-specific
DAG and deployment tradeoffs. Use this section to compare the broader tool
families.

[[person:adrianbrudaru=>Adrian Brudaru]] says GitHub Actions can be enough for
simple workflows.
It avoids the cost of always-on orchestrators
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]].
That lightweight-runner choice belongs in
[[modern-data-engineering-trends=>modern data engineering trends]] when
orchestration is part of a broader platform-cost decision.
The [[lean-mlops-for-startups=>Lean MLOps for Startups]] example keeps
orchestration in CI/CD where possible. [[person:nemanjaradojkovic=>Nemanja
Radojkovic]] chooses Dagster when the workflow needs a real orchestrator
[[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].

Kretz gives the AWS version with CloudWatch, Lambda, containers, and ECS. He
also names AWS Batch, SageMaker, Airflow, and Kubernetes
[[cite:production-ml-pipelines-with-aws-and-kafka@35:46=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@41:06=>From Notebooks to Production]].

The decision turns on shared state. A small pipeline can use serverless
automation when failure recovery is simple. A team should pay for heavier
orchestration when dependencies, retries, owners, and backfills need shared
history.

## Operating Cost

Every orchestrator adds an operating surface. The tool may need worker
capacity, secrets, connections, and logs. It may also need deployment
discipline and alert owners. Backups, upgrades, and managed access can become
part of the same surface. Those responsibilities are part of the
orchestration decision, not cleanup work after deployment.

Teams should pay that cost when shared tables, dashboards, or features need
central run state. Batch predictions can need the same shared history. Heavier
orchestration becomes ceremony when the workflow is one small script. It also
adds ceremony when failures are easy to rerun manually and no one needs shared
task history.

[[Apache Airflow]] covers the Airflow-specific version of this operating surface.
That includes DAG authoring and scheduler behavior. It also includes executor
behavior, workers, metadata state, and logs. Connections, dependencies, and
secrets live there too.

A simpler scheduler can fit when a cloud scheduler can start a container or
function. It can also fit when no backfill workflow exists yet or the data
product hasn't proven enough value to justify platform work. A workflow engine
fits when dependencies become hard to track informally
[[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]]
[[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].

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

A scale-up may spend about half its data-engineering effort on platform work.
The other half may go to use-case pipelines, because repeated requests
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

An orchestration run doesn't prove that the data is correct.
[[person:tomaszhinc=>Tomasz Hinc]] gives that warning through an Airflow
example: a job can be green while zero records were inserted. Task status needs
edge-case checks and data checks before a team presents results with confidence
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps Best Practices for Data Teams]].

That example marks the main boundary between orchestration and
[[data quality and observability]]. The orchestrator can show task starts,
retries, failures, and successes. It can also preserve run history and
dependency state. It can't prove freshness, volume, or schema validity. It also
can't prove distribution, lineage impact, or business correctness.

Use
[[dataops-checks-for-data-pipelines=>DataOps checks for data pipelines]] for the
checks that need to surround an orchestrated run.

Those checks need to run inside the workflow or in adjacent observability
systems. The team needs owners who respond when checks fail.

## Learning and Project Scope

For learners, orchestration should come after the pipeline has real steps to
coordinate. [[person:jeffkatz=>Jeff Katz]] places Docker and AWS after Python
and SQL, and puts workflow tooling after data-warehouse fundamentals in
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]].

The same learning boundary applies regardless of tool: write the extraction and
transformation clearly first. Add checks and publication paths before an
orchestrator hides weak ownership
[[cite:data-engineering-career-path-and-skills=>Data Engineering Career Path and Skills]].

Then add orchestration when schedules, dependencies, retries, or run history
become part of the problem. Backfills belong in the same decision. A learner can
prove the concept with any tool that shows the sequence, failure mode, recovery
path, and data checks. [[Apache Airflow]] owns Airflow-specific DAG behavior and
local Docker setup.

The same proof standard keeps
[[data-engineering-certification=>Data Engineering Certification]] useful but
secondary. Certificate study should end in a runnable workflow with visible
dependencies, checks, and recovery behavior.

Pin container dependencies when they prove reproducibility
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps]].

Move from a learning setup to shared orchestration when the team shares
operations:

- several people deploy workflows.
- engineers need retained, searchable logs.
- secrets need managed access.
- workers need isolation or autoscaling.
- backfills compete with current runs.
- downstream dashboards, ML jobs, product features, or operational decisions
  depend on the output.

Mehdi's platform point applies here too. The workflow engine is only one
platform component [[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

A useful orchestration project shows more than a workflow screenshot. It shows
why one step waits for another and what happens when an input is late. It also
shows how a failed partition reruns and how a historical window backfills. It
should show which data checks guard publication and who owns the alert. For
Airflow projects, [[Apache Airflow]] owns the DAG-level version of that
portfolio signal.

The work may still be one script with one simple schedule. In that case,
Brudaru's GitHub Actions example may fit better than a full workflow engine [[cite:trends-in-modern-data-engineering@35:37=>Modern Data Engineering Trends]].

Kretz's CloudWatch and Lambda path may fit too [[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].
Nemanja's CI/CD-first startup path is another small-team option [[cite:lean-mlops-for-startups=>Lean MLOps for Startups]].
