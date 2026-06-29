---
layout: article
title: "Airflow: Where It Fits in Data Engineering, Pipelines, and the Modern Data Stack"
keyword: "airflow"
summary: "A podcast-backed guide to Airflow as a data orchestration tool: what it does, when teams need it, and how it compares with adjacent choices such as dbt, Airbyte, Prefect, Dagster, GitHub Actions, and feature-store workflows."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Data Quality and Observability
  - Batch vs Streaming
---

Airflow is a workflow orchestration tool for data teams. It schedules jobs,
coordinates dependencies, runs retries, and shows whether a pipeline finished
or failed.

DataTalks.Club guests treat Airflow as part of data engineering, not as the
whole stack. They mention it with ingestion tools, warehouses, and dbt-style
transformations. Feature stores, ML platforms, observability, and team
conventions show up around it too. The practical question isn't "Should we use
Airflow?" It's "Do we have enough recurring data work that an orchestrator will
make the system easier to operate?"

Start with [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
and [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Use [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) and
[DataOps]({{ '/wiki/dataops/' | relative_url }}) for the adjacent operating
model.


## Airflow Jobs

Airflow gives data workflows a control plane. A team can define a directed
workflow and schedule it. It can connect tasks, retry failures, and look at run
history.

That makes Airflow useful when work has dependencies.

- extract data from a source system
- load raw data into a warehouse, lake, or lakehouse
- run transformations or dbt jobs
- check data quality
- backfill historical partitions
- publish a data mart, dashboard table, feature table, or reverse ETL sync
- run batch model training or batch inference

Airflow is often discussed with ETL and ELT, but it isn't the transformation
logic. In the modern stack episode, Natalie Kwong positions Airflow as the
orchestrator that schedules and runs other pieces. Those pieces include
Airbyte jobs and downstream transformations.

That distinction matters because Airflow coordinates the pipeline, while SQL
or dbt may run the work. Spark and Python can do the work too, as can Airbyte,
warehouses, and ML platforms.

## Modern Stack Fit

A common modern analytics flow looks like this:

1. Ingestion brings data from APIs, SaaS tools, databases, event streams, or
   files into raw storage.
2. A warehouse, lake, or lakehouse stores data for analytics and downstream
   systems.
3. Transformations clean, join, model, and document the data.
4. Orchestration schedules and coordinates those jobs.
5. Data quality and observability check freshness, schema, volume, and
   downstream impact.
6. BI, ML, reverse ETL, product analytics, or operational tools consume the
   result.

Airflow usually belongs in step 4. It can call the ingestion job, trigger the
dbt project, wait for upstream tables, and run validation tasks. It can also
alert the owner when a dependency fails.

Modern data stack guests make this split clear. Airbyte handles extract-load
work, dbt handles transformations, and warehouses or lakes store data.
Airflow coordinates the moving parts. Reverse ETL tools push modeled data back
into business systems when the workflow needs activation.

See [Data Engineering Tools]({{ '/articles/data-engineering-tools/' | relative_url }})
for the broader tool map and
[Batch vs Streaming]({{ '/wiki/batch-vs-streaming/' | relative_url }}) for the
latency tradeoff behind many orchestration decisions.

## Good Fit

Airflow becomes useful when pipelines are no longer a few isolated scripts.

Common triggers include these cases:

- multiple recurring jobs with dependencies
- backfills that must run in a controlled order
- shared pipelines that several teams rely on
- data quality checks that should block or warn before publication
- pipeline failures that need run history and ownership
- batch ML jobs that need the same repeatable schedule as analytics pipelines
- platform teams that need conventions for many similar pipelines

In the scale-up data engineering episode, Mehdi OUAZZA argues that an Airflow
cluster alone isn't a platform. Teams also need naming conventions and
sequencing rules. Reusable templates, playbooks, and operating habits matter
too.

His point is useful for Airflow adoption. The tool helps once the team also
invests in how pipelines are structured and maintained.

That's where Airflow connects to [DataOps]({{ '/wiki/dataops/' | relative_url }}).
Retries and scheduling are only part of reliable data delivery. Teams still
need version control, tests, CI/CD, and realistic test data. They also need
observability, runbooks, and clear ownership.

## Too Much

Airflow isn't always the right first tool, and podcast guests give the same
advice. Start from the workflow and operating need, not from the most
recognizable tool name.

Andreas Kretz's production pipeline discussion gives a clear sequence. A team
can start with a simpler queue, script, cloud function, or scheduled job when
it's proving a first workflow. As the project grows and needs more logging,
visibility, and control, moving to Airflow or a similar orchestrator makes more
sense.

Adrian Brudaru's modern data engineering episode makes a similar point for
2025 tooling. He names Airflow as a common choice, but also mentions Prefect,
Dagster, and GitHub Actions. For simple workflows, GitHub Actions can be
enough, especially when an always-on orchestrator would add cost without adding
much value.

Use a smaller scheduler in these cases:

- the workflow is a single daily script
- there are few dependencies
- failures are easy to rerun manually
- no team needs shared run history
- cloud-native scheduled jobs already cover the use case
- the cost of running and maintaining Airflow is larger than the pipeline risk

Use Airflow or another orchestrator when dependencies and ownership become hard
to manage informally. Backfills, auditability, and shared operations push in
the same direction.

## Airflow vs dbt

dbt mainly transforms data through SQL-oriented models and also provides tests,
documentation, and dependency graphs. Airflow is mainly about orchestrating
jobs.

Many teams use both because dbt defines analytical transformations and Airflow
schedules the surrounding work. That work can include ingestion, transforms,
checks, and publication.

In the modern data stack episode, dbt is tied to analytics engineering and
warehouse transformations. Airflow is discussed as the scheduler and
orchestrator around those components.

## Airflow vs Airbyte

Airbyte handles extract-load connector work. Airflow can trigger or coordinate
Airbyte jobs as part of a larger pipeline. Natalie Kwong describes this setup
directly: Airflow integrates with Airbyte so teams can orchestrate the extract
and load step inside a broader workflow.

The useful separation is simple: Airbyte moves data from sources, while Airflow
decides when that movement and related downstream jobs should run.

## Airflow vs Prefect and Dagster

The archive doesn't present one orchestrator as universally best, and Adrian
Brudaru frames the choice as team-dependent. Airflow remains common, while
Prefect and Dagster are popular alternatives. GitHub Actions can be enough for
small or cost-sensitive workflows.

Antonis Maronikolakis, discussing a course project, describes Prefect as an
easier Airflow alternative for the project he wanted to build. That doesn't
make a general rule against Airflow. It's a useful reminder that developer
experience and project size matter.

## Airflow and Feature Stores

Feature-store discussions show Airflow as part of the upstream data
infrastructure. Willem Pienaar explains that Feast doesn't own upstream
transformations. Teams often keep those transformations in dbt, Airflow, or
Spark jobs. They then feed transformed data into the feature store.

Tecton can take more of that workflow into the feature platform. That creates
a build versus adopt decision for existing teams.

This matters for ML teams because batch features, backfills, and online serving
often cross tool boundaries. Airflow may orchestrate upstream feature
pipelines, but it isn't the feature store.

## Airflow and ML Platforms

Simon Stiebellehner's ML platform episode connects Airflow to batch training
and batch inference. A batch model workflow often looks like a sequence of data
loading, preprocessing, and feature engineering. Training or inference comes
next, followed by output storage. Airflow can coordinate that sequence, but
managed ML pipelines or cloud-specific tooling may do the same job depending on
the team's platform strategy.

For ML platform teams, the decision isn't just "Airflow or no Airflow." It's
whether the platform should standardize repeated workflows or leave teams more
flexibility.

## Learning Path

For learners, Airflow is most useful after the basics are clear.

Data engineering career guidance in the archive keeps returning to these
fundamentals:

- SQL and Python
- files, APIs, and database sources
- batch pipeline design
- warehouses, lakes, and lakehouses
- data modeling and transformations
- testing and data quality
- cloud basics and deployment
- logs, alerts, retries, and ownership

Airflow should make a pipeline more operable. It can't rescue a workflow whose
source data, transformations, ownership, or downstream purpose is unclear.

For a portfolio project, avoid adding Airflow only as decoration. A stronger
project shows why orchestration is needed through dependencies, retries, and
backfills. It should also include data quality checks, alerts, and a short
runbook.

## Podcast Evidence

[Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html)
is the clearest Airflow explanation in the archive. Natalie Kwong discusses
ETL, ELT, Airbyte, and dbt. She also covers warehouses, data lakes,
orchestration, and reverse ETL. Her Airflow framing is practical. It schedules
and orchestrates jobs around the stack rather than replacing ingestion or
transformation tools.

[Scaling Data Engineering Teams](https://datatalks.club/podcast.html)
adds the platform view. Mehdi OUAZZA argues that Airflow is only one piece of a
usable data platform. Teams need conventions, templates, playbooks, and
operating rules so pipelines remain maintainable as more users build on the
platform.

[Modern Data Engineering Trends](https://datatalks.club/podcast.html)
adds the current tool-choice caution. Adrian Brudaru names Airflow, Prefect,
Dagster, and GitHub Actions as orchestration options and ties the decision to
team needs and cost.

[From Notebooks to Production](https://datatalks.club/podcast.html)
shows when not to overbuild. Andreas Kretz describes starting with simpler
workflow coordination and moving toward Airflow or similar tooling as a system
needs more insight and operational control.

[Building Production ML Platforms](https://datatalks.club/podcast.html)
connects orchestration to ML workflows. Simon Stiebellehner discusses batch
training and batch inference as sequences of jobs that can be coordinated with
Airflow or managed pipeline services.

[Feature Stores for MLOps](https://datatalks.club/podcast.html)
shows the adjacent feature-store boundary. Willem Pienaar explains that tools
such as Feast often consume transformed data from upstream systems like dbt,
Airflow, or Spark. Other platforms may own more of the transformation and
backfill workflow.

## Practical Takeaway

Airflow is best understood as orchestration infrastructure for recurring,
dependent data work. It helps teams schedule and coordinate pipelines, handles
retries and backfills, and adds visibility. It fits modern data stacks,
analytics engineering workflows, DataOps practices, and batch ML systems.

It's not a replacement for ingestion, transformation, storage, or data quality.
It also doesn't replace platform conventions. Guests give a consistent rule:
choose Airflow when the workflow needs a real control plane. Keep simpler
schedulers or managed tools in play when the workflow doesn't justify the extra
operating burden.
