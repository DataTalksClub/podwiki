---
layout: article
title: "Airflow Docker Compose: Local Development, Learning, and Production Caveats"
keyword: "airflow docker compose"
summary: "A podcast-backed guide to using Docker Compose for Airflow learning, local DAG development, persistence, executors, project structure, parity, and production caveats."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Production
  - Data Quality and Observability
  - Batch vs Streaming
---

`airflow docker compose` is usually a local-development question. You want to
run Airflow without turning your laptop into a full platform project.

You also want to understand the moving parts:

- scheduler
- web UI
- metadata database
- DAG files
- logs
- workers
- local dependencies
- surrounding containers

Docker Compose helps because you can start, stop, look at, and reset those
parts together. It's useful for learning Airflow and for developing DAGs before
they move to a shared environment. It isn't a production strategy.

The DataTalks.Club podcast archive draws that line in several episodes. Start
with the workflow. Keep the setup simple while the work is small. Move to
stronger orchestration or managed infrastructure when you need logging,
visibility, recovery, and team ownership.

For the broader Airflow decision, use
[Apache Airflow]({{ '/articles/apache-airflow/' | relative_url }}) and
[Airflow]({{ '/articles/airflow/' | relative_url }}). For the operating model
around pipelines, start with
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [DataOps]({{ '/wiki/dataops/' | relative_url }}).


## Article Outline

Use this page as a local-development guide, not as a copy-paste production
runbook.

1. Docker Compose as an Airflow learning environment.
2. Airflow services that matter in local development.
3. Persistence for metadata, logs, and project code.
4. Executors at a high level.
5. Local project structure.
6. Environment parity and its limits.
7. The point where teams should move beyond Compose.
8. Podcast-backed evidence for Airflow, Docker, and production caveats.

## Compose Benefits

Airflow is easier to understand when you can see its parts running together.
Compose gives you that view. One service can run the web UI, and another can
run the scheduler. A database can keep Airflow state. A worker service can run
tasks when you use an executor that separates scheduling from task execution.

You can mount shared folders for DAGs, logs, plugins, and configuration. That
makes the local feedback loop fast. You edit a DAG on your machine and see how
the containerized Airflow environment handles it.

Airflow is an orchestrator, not the pipeline's business logic. Natalie Kwong
makes this distinction in
[Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html).
Around 31:12, she describes Airflow as the tool that schedules and
orchestrates work around systems such as Airbyte. Airflow coordinates the
flow, while the actual pipeline work belongs in the right tool for that job.

Docker Compose also teaches reproducibility. In
[From Notebooks to Production](https://datatalks.club/podcast.html), Andreas
Kretz describes a practical path out of notebooks. Around 34:16-35:46, he
talks about moving Python code into a Docker container, scheduling it, and
storing the model or output somewhere durable.

That maps well to local Airflow development. You can turn a manual script into
a task, mount it into the environment, and test whether the workflow still
makes sense outside your notebook.

Use Compose when you need a sandbox for:

- DAG parsing and scheduling
- task dependencies
- retries and failure states
- task logs
- connection and variable configuration
- local database state
- a repeatable example another developer can run

Don't use Compose only to make an impressive architecture diagram. If a single
script is enough, a smaller scheduler or a direct container run may teach the
same lesson with less machinery.

## Local Services

A local Airflow Compose setup usually teaches five service concepts.

The web UI shows DAGs, task states, logs, and configuration. It gives you the
visible part of Airflow. The scheduler still handles the decision about what
should run next.

The scheduler reads DAG definitions and creates task instances when schedules
and dependencies say work is ready. If the scheduler is down, the UI may still
load. New scheduled work won't progress as expected.

The metadata database stores Airflow's memory by keeping DAG runs and task
states. It also keeps retries, connections, variables, and other operating
state. This database is what makes Airflow more than a cron file. It also
becomes a production responsibility later.

Workers run task code when the executor model uses separate task execution. In
a small local setup, you may not need a separate worker service. In a queued
setup, you may also run a broker between the scheduler and workers.

You mount project folders for DAG files, logs, plugins, and supporting code.
Those mounts make local development quick.

Keep those concepts separate, because treating the Compose file as one black
box hides the operating model.

Airflow problems often come from the boundaries between services:

- a DAG import error
- a missing package in the task environment
- a lost database volume
- a worker that can't reach a service
- a log path that exists in only one container

## Persistence

Persistence is where local Airflow starts to feel real.

If you run everything with throwaway state, you can reset quickly. That's
useful while learning. It also hides the cost of operating Airflow. Once you
care about run history and retry state, you need persistent storage. The same
is true for connections, variables, and logs.

For local development, think about three kinds of persistence:

- Airflow metadata, usually held in a database volume
- task logs, usually mounted or stored where the UI can read them
- project code, usually mounted from your working directory

Metadata persistence tells you what happened before. It records failed tasks,
retries, backfills, and runs that no worker picked up. Without persistent
metadata, you lose that history each time the environment resets.

Log persistence matters because a green or red task box isn't enough.

You need the detail that explains the state:

- task output
- error messages
- SQL
- API responses
- row counts
- validation failures

The archive's [Production]({{ '/wiki/production/' | relative_url }}) page
names the broader threshold. Once people rely on a system, teams need logs and
monitoring. They also need ownership and recovery.

Project-code persistence is different because you want code changes to be easy.
You also want the container to run with known dependencies. Avoid a setup where
your machine has a Python package that the Airflow task container doesn't.
Docker should expose that hidden dependency instead of hiding it.

## Executors

You don't need to master every Airflow executor before using Docker Compose.
You do need the high-level distinction.

An executor controls where tasks run. A simple local executor can run work in
the same environment as the scheduler process. That path is easier to learn and
works for small examples.

A distributed or queued executor separates scheduling from task execution. It
can send tasks to workers. That setup is closer to what teams use when they
need concurrency, isolation, and scale.

For learning, start with the simplest executor that teaches DAGs and
dependencies. It should also teach retries and logs. Move to a worker-based
setup when you need to learn how task execution behaves across services.

The podcast archive supports this staged approach. In
[From Notebooks to Production](https://datatalks.club/podcast.html), Andreas
Kretz argues around 35:46 that simple scheduled containers can be enough before
you run a whole framework like Airflow. Around 41:06-42:07, he says teams can
move toward Airflow or bigger infrastructure when they need more logging,
insight, and control.

That advice applies inside Airflow too. Don't add a distributed local setup
before the simpler one has taught you which problem the extra services solve.

## Project Structure

A good local Airflow project should be easy to look at and easy to rerun. Keep
the project boring.

Use separate places for these concerns:

- `dags/` for DAG definitions
- `include/`, `src/`, or another clear folder for reusable Python code
- `plugins/` only when you actually need Airflow plugins
- `logs/` for local task logs if your setup mounts them
- `.env` or environment-specific files for local configuration
- `requirements.txt`, `pyproject.toml`, or an image build step for Python
  dependencies
- `README.md` for setup, commands, expected services, and reset steps

Put business logic outside the DAG file when you can.

Keep DAG files focused on orchestration:

- schedules
- dependencies
- task definitions
- owners
- retries
- calls into the real work

Put extract logic, validation logic, SQL-building code, and transformation
helpers in testable modules. You can also put that work in dbt, SQL, Spark, or
a Python package.

This follows Natalie Kwong's Airflow distinction in the modern stack episode:
Airflow coordinates while other tools do the pipeline work.

Use local Compose to practice data engineering portfolio discipline. Jeff
Katz's job-prep guidance emphasizes Python, SQL, Docker, and Airflow. It also
emphasizes warehouses and clean code. Small functions, descriptive names, and
tests matter too. A local Airflow project that another person can run is
stronger than a screenshot of a DAG grid.

## Environment Parity

Docker Compose gives you useful parity within limits.

It helps when everyone on a course or portfolio project needs to run the same
services. The same is true for a small team. The same local database name and
Airflow image reduce "works on my machine" problems. The mounted DAG path,
dependency file, and startup command help too.

It also helps you notice missing dependencies. A DAG may import a library that
exists on your laptop but not in the Airflow container. In that case, the
import fails where you can fix it. That's better than discovering the problem
after a deployment.

But Compose doesn't reproduce all production behavior.

It usually doesn't match these production concerns:

- identity and access management
- secrets storage
- network policies
- autoscaling
- remote logging
- backups
- alert routing
- high availability
- managed database behavior

Compose also can't prove that a workflow will handle real production volume.
It can't prove behavior with late data, flaky sources, or several teams
deploying DAGs at the same time.

Use Compose to align the developer loop. Don't use it as proof that the
production operating model is solved.

In [DataOps]({{ '/wiki/dataops/' | relative_url }}), teams turn a runnable
workflow into a maintained data system. They add version control and tests.
They also add CI/CD, observability, runbooks, and recovery practices.

## Compose Fit

Docker Compose is enough for learning and local feedback.

Use it for:

- learning Airflow's architecture
- developing DAGs before deployment
- testing task imports and small task runs
- building a data engineering portfolio project
- teaching orchestration in a bootcamp or workshop
- demoing dependencies, retries, and logs
- reproducing a bug in a small environment

Compose can also support a small internal proof of concept when nobody depends
on the output yet. Stay honest about the boundary. If a dashboard or report
relies on the data, you've crossed into production responsibility. The same is
true for a model or business workflow.

## Beyond Compose

Move beyond Docker Compose when the orchestration environment needs to be
operated, not merely started.

Common signals include:

- several people deploy or edit DAGs
- failures need alerts and owners
- logs must be retained and searchable
- secrets need managed storage and access controls
- the metadata database needs backups and upgrades
- workers need more isolation, concurrency, or scaling
- backfills can compete with current runs
- the workflow calls production databases, warehouses, queues, or APIs
- users depend on the output for reports, ML jobs, product features, or
  operational decisions

Adrian Brudaru gives the current tool-choice version in
[Modern Data Engineering Trends](https://datatalks.club/podcast.html). Around
35:37, he names Airflow as a common orchestration choice but also mentions
Prefect, Dagster, and GitHub Actions. Around 37:08, he says GitHub Actions can
be enough for simple workflows because it avoids the cost of always-on
orchestrators.

GitHub Actions doesn't replace Airflow in every case, so match the
orchestrator to the workflow and the team.

Compose is one local option.

Other options may fit better once you know what you're operating:

- a cloud scheduler
- a managed Airflow service
- a Kubernetes deployment
- Prefect
- Dagster
- GitHub Actions
- another platform

For platform context, see
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}).

## Common Mistakes

The common mistakes come from using Compose as a shortcut around design.

- Treating Airflow as the ETL logic instead of the orchestrator.
- Putting large transformations directly in DAG files.
- Forgetting that metadata and logs need persistence.
- Installing dependencies on the host machine but not in the Airflow task
  environment.
- Storing secrets in a local file and then copying the same habit into
  production.
- Adding distributed workers before you understand the simple executor path.
- Assuming a local green run proves production readiness.
- Keeping no reset instructions, so the next developer can't reproduce the
  setup.
- Skipping data-quality checks because the Airflow task status is green.

The most important mistake is confusing a local orchestration demo with an
operated pipeline. Compose can show that the workflow runs. It can't prove that
downstream users can trust the result unless the workflow includes tests and
freshness checks. Validation, ownership, and a recovery path matter too.

## Podcast Evidence

[Data Engineering Tools and Modern Data Stack](https://datatalks.club/podcast.html)
is the best starting point for Airflow's role. Around 31:12, Natalie Kwong
positions Airflow as an orchestrator that schedules and runs other tools,
including Airbyte jobs.

[From Notebooks to Production](https://datatalks.club/podcast.html) explains
why Docker and orchestration should be staged. Around 34:16, Andreas Kretz
describes moving notebook code into a Docker container and scheduling it.
Around 35:46, he says simple scheduled containers can avoid running a whole
Airflow framework too early. Around 41:06-42:07, he recommends starting simple.
Teams can add Airflow or larger infrastructure when logging, insight, control,
and platform needs justify it.

[Modern Data Engineering Trends](https://datatalks.club/podcast.html) adds the
current orchestration comparison. Around 35:37-37:08, Adrian Brudaru mentions
Airflow and Prefect, and he also mentions Dagster and GitHub Actions. He ties
simple workflows to cost and team needs.

[DataOps 101](https://datatalks.club/podcast.html),
[Mastering DataOps](https://datatalks.club/podcast.html), and
[DataOps for Data Engineering](https://datatalks.club/podcast.html) provide
the operating layer behind the caveats. They cover automation, observability,
tests, and CI/CD. They also cover recovery and realistic test data.

## Practical Takeaway

Use Docker Compose for Airflow when you need a local environment for the moving
parts and repeatable DAG development. You can learn schedulers, metadata, logs,
and dependencies. You can also learn task execution and project structure
without starting from a full platform deployment.

Move beyond Compose when people depend on the workflows. At that point, the
question is no longer "Can I start Airflow locally?" The better question is who
owns the orchestrator and deployment path. Teams also need clear owners for
secrets, metadata, failure alerts, and recovery steps.
