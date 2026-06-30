---
layout: article
title: "Airflow Docker Compose: Local Development, Learning, and Production Caveats"
keyword: "airflow docker compose"
summary: "A podcast-backed how-to for using Docker Compose as a local Airflow learning and DAG development environment, with clear production boundaries."
related_wiki:
  - Data Engineering
  - Data Pipelines
  - Orchestration
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Production
  - Data Quality and Observability
  - Batch vs Streaming
---

Use Docker Compose for Airflow when you need a local environment that makes the
orchestrator's moving parts visible. You can run the web UI and scheduler. You
can also run the metadata database, DAG files, task logs, and workers when you
need them. The DataTalks.Club podcast archive supports that local-development
use case. It doesn't support treating a Compose file as a production deployment
recipe.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) draws the
Airflow boundary in the modern data stack episode. Around 30:59-31:12, she
explains that Airflow is an
[orchestrator]({{ '/wiki/orchestration/' | relative_url }}) and scheduler around
tools such as Airbyte and dbt. It doesn't own ingestion, transformation,
storage, or quality
([Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
So an Airflow Docker Compose setup should help you learn orchestration and DAG
development. It shouldn't hide weak [data pipeline]({{ '/wiki/data-pipelines/' | relative_url }})
design behind a local cluster.

For the broader Airflow decision, use
[Airflow]({{ '/guides/airflow/' | relative_url }}) and
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}). Use the
Compose workflow here for local work.

## Compose Fit

Use an Airflow Docker Compose setup for a small local dev cycle:

- learning how the scheduler, web UI, metadata database, DAG folder, logs, and
  task execution relate to each other.
- developing DAGs before deploying them to a shared environment.
- testing whether imports, dependency files, and supporting Python modules work
  inside containers.
- teaching orchestration in a course or workshop.
- building a [data engineering portfolio project]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
  where a reviewer can rerun the workflow.
- reproducing a pipeline bug with known services and known local state.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) supports this learning
sequence in
[Data Engineering Career Path and Skills]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).
Around 23:35, he describes extending a data engineering curriculum from Python
and SQL into AWS, Docker, and Airflow. Around 57:36, he says good Airflow code
keeps most logic in Python instead of relying on Airflow for everything. That's
the main Compose rule. Use local containers to expose the orchestration
environment, but keep the pipeline logic reviewable and testable outside the
DAG file.

## Build The Smallest Useful Local Stack

Start with the smallest Airflow stack that teaches the workflow you need. Many
learners need a scheduler, web UI, and metadata database. They also need
mounted `dags/`, mounted `logs/`, and a repeatable initialization path. Add
workers and a broker only when the lesson requires queued or distributed task
execution.

That staged approach follows [Andreas Kretz's]({{ '/people/andreaskretz/' | relative_url }})
production advice in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 35:46, he compares Airflow with simpler schedulers such as CloudWatch,
Lambda, and AWS Batch. Around 41:06, he recommends starting with simple
infrastructure and moving toward Airflow or Kubernetes when the team needs more
logging, insight, and control. Locally, the same rule applies: make one DAG
understandable before adding more services because the Compose file looks more
realistic.

Use this order:

1. Create one DAG that calls real work in Python or SQL.
2. Mount the DAG and supporting code into the Airflow containers.
3. Persist metadata and logs so failed runs can be looked at after restart.
4. Add checks that prove the output is usable, not only that the task ended.
5. Add worker-based execution only when you need to learn task isolation or
   concurrency.
6. Document reset, startup, and expected services so another person can run the
   same local environment.

## Keep DAGs Thin

A useful Compose project is boring to navigate. Put orchestration in `dags/`
and put reusable code in clear project folders. Common choices include `src/`,
`include/`, dbt models, and SQL files. The DAG should describe the schedule,
dependencies, retries, and owners. It should also define task boundaries and
calls into the real work.

The DAG shouldn't become the only place where transformation logic lives.

Natalie's tool boundary supports this split because Airflow schedules and
coordinates. The ingestion tool owns ingestion. The dbt project owns
transformation. Warehouse jobs, Spark jobs, and Python modules own the work they
run
([Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-31:31).

It also fits [Santona Tuli's]({{ '/people/santonatuli/' | relative_url }})
pipeline architecture discussion. Around 26:43-27:07 in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
she names orchestration engines such as Airflow and Prefect. She also names
Dagster and Mage. She ties the choice to how the team breaks up the workflow
and which transformations the pipeline runs.

For adjacent design choices, use
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}),
[Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }}),
and [ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}).

## Persist The Right State

Local Airflow becomes useful when you can look at what happened.

Keep these state categories explicit:

- project code, usually mounted from the working directory.
- Airflow metadata, usually persisted in a local database volume.
- task logs, mounted or stored where the Airflow UI can read them after a
  failure.

The metadata database is why Airflow is more than cron. It records DAG runs,
task states, retries, and scheduling history. Logs show what failed inside a
task. Local persistence lets a learner stop the environment, start it again, and
still look at a failed run.

In shared environments, teams need database backups and log retention. They
also need dependency control, managed secrets, and connection access.
[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }})
connects that operational mindset to [DataOps]({{ '/wiki/dataops/' | relative_url }})
in
[DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
Around 1:02:28-1:05:41, he warns that green Airflow jobs can still insert zero
records. A local Compose setup should therefore include output checks, not only
a successful task state.

## Add Quality Checks Before Trusting Runs

The common local mistake is to celebrate a green DAG run too early. Airflow can
show that a task started, retried, failed, or succeeded. It can't prove whether
data is fresh or complete. It also can't prove schema validity, plausible
counts, or downstream metric correctness unless the workflow includes those
checks.

Add lightweight checks before publishing an output:

- row-count or freshness checks for ingested data.
- schema checks for expected columns and types.
- partition checks for time-bounded pipelines.
- null, duplicate, and range checks for critical fields.
- a clear failure path that leaves logs and data context behind.

This is where the local Compose environment connects to
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
Tomasz's Airflow caveat is the strongest archive example: task success isn't
business confidence
([DataOps and GitOps Best Practices for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}),
1:02:28-1:05:41). Compose can help you practice the check locally, but the
check belongs to the pipeline design.

## Know When Compose Stops Being Enough

Move beyond Docker Compose when the workflow needs shared operations:

- several people deploy or edit DAGs.
- failures need alerts, owners, and recovery steps.
- logs must be retained and searchable.
- secrets and connections need managed access control.
- the Airflow metadata database needs backups and upgrades.
- workers need isolation, concurrency, or autoscaling.
- backfills can compete with current runs.
- production databases, warehouses, queues, or APIs are involved.
- downstream dashboards, ML jobs, product features, or operational decisions
  depend on the output.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the platform
version in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Around 17:22-17:56, he says an Airflow cluster is only one platform component.
Teams still need conventions and playbooks. They also need sequencing rules,
naming rules, and reusable DAG templates. A local Compose file is further from a
platform than a shared Airflow cluster, so it should be treated as a learning
and development tool.

Use [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [Production]({{ '/wiki/production/' | relative_url }}) for the larger
operating model.

## Compare Against Simpler Schedulers

Airflow isn't always the right first scheduler. If the workflow is one small
script with one simple schedule, a cloud scheduler, cron-like service, or GitHub
Actions workflow may be easier to operate.

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) makes that
tradeoff in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
At 35:37 he names Airflow alongside Prefect, Dagster, and GitHub Actions.
Around 37:08, he says GitHub Actions can be enough for simple workflows because
it avoids the cost of always-on orchestrators. An Airflow Docker Compose project
should therefore prove that the workflow has real dependencies, retries, run
history, or backfills to learn from.

## Local Checklist

Before calling the local setup useful, check that it shows the orchestration
behavior the archive keeps emphasizing:

- The DAG calls external pipeline logic instead of hiding all work in the DAG
  file.
- The scheduler, UI, metadata database, and logs can be looked at separately.
- A failed run leaves enough logs to debug the task.
- The project has a documented reset path.
- Dependencies are installed inside the Airflow image, not only on the host.
- Don't copy secrets into a local structure that would be unsafe in production.
- At least one data-quality check guards the output.
- The README explains when to replace the local setup with managed
  infrastructure or a shared Airflow environment.

Keep the standard simple by using Compose to make Airflow local and repeatable.
Use Airflow to coordinate recurring work, then add DataOps and quality checks
before other people depend on the workflow.

## Related Pages

Use these pages for the surrounding Airflow, pipeline, and operations topics:

- [Airflow]({{ '/guides/airflow/' | relative_url }})
- [Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }})
- [How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }})
- [Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
