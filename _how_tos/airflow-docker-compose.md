---
layout: article
title: "Airflow Docker Compose: Local Development, Learning, and Production Caveats"
keyword: "airflow docker compose"
summary: "A podcast-backed guide to using Docker Compose for Airflow learning, local DAG development, persistence, executors, and production caveats."
search_intent: "People searching for airflow docker compose usually want a practical local Airflow setup. They may be learning Airflow, building a portfolio project, debugging DAGs, or comparing local Compose with production deployment. Keep the public page focused on how Compose helps learners see Airflow services locally and where it stops being enough."
related_wiki:
  - Data Engineering
  - Data Engineering Platforms
  - Modern Data Stack
  - DataOps
  - Production
  - Data Quality and Observability
  - Batch vs Streaming
---

`airflow docker compose` is a local-development question before it's an
Airflow architecture question.

You want a runnable Airflow environment with the core services visible:

- web UI
- scheduler
- metadata database
- DAG folder
- logs
- workers, when the executor needs them

You also want to learn those pieces without building a shared data platform on
day one.

Docker Compose is a good fit for that learning loop. It can start the Airflow
services together, mount your DAGs from the local checkout, preserve metadata
between restarts, and make missing dependencies visible inside containers. It
isn't proof that the same workflow is production-ready.

That distinction is consistent with the DataTalks.Club archive.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) places Airflow
in the orchestration layer in the
[modern data stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Around 30:59, she discusses Airflow next to Airbyte and dbt. She also places
it beside warehouses, CDC, and reverse ETL. She treats Airflow as the scheduler
and dependency layer. It doesn't replace ingestion, transformation, storage, or
data quality.

For the broader Airflow decision, use
[Airflow]({{ '/guides/airflow/' | relative_url }}) and
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}). Here, use
the local Docker Compose setup to learn Airflow's pieces and the point where
teams should move beyond it.

## Local Use Case

Use Docker Compose for Airflow when you need to see the system work as a small
local environment:

- learning Airflow's scheduler, web UI, metadata database, and task logs
- developing DAGs before deploying them to a shared environment
- testing DAG imports and dependency files inside containers
- building a reproducible data engineering portfolio project
- teaching orchestration in a course or workshop
- reproducing a small bug with known services and known state

Compose helps because Airflow has separate services. The web UI can load
while the scheduler is unhealthy. A DAG can parse in one container but fail in
a worker because a package is missing. A task can also turn green while the
output data is wrong. Running the pieces locally makes those boundaries easier
to look at.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) explains why Docker and
Airflow appear together in learning paths in
[Build a Data Engineering Career]({{ '/podcasts/data-engineering-career-path-and-skills/' | relative_url }}).
Around 21:52, he describes extending a data engineering curriculum from Python
and SQL into cloud, Docker, and Airflow. Around 55:10, he warns that good
Airflow code should keep most logic in normal Python rather than relying on
Airflow. A local Compose setup should teach that separation.

## Local Services

A local Airflow Compose setup usually teaches the main service boundaries.

The web UI shows DAG and task status, logs, retries, and configuration.
Learners can use it to look at failures, while the scheduler still decides
what should run next.

The scheduler reads DAG definitions and creates task instances when schedules
and dependencies say work is ready. If the scheduler is down, the UI may still
open, but scheduled work won't progress normally.

The metadata database stores Airflow's memory:

- DAG runs and task states
- connections and variables
- retries and scheduling history

That database is why Airflow is more than cron, and it becomes an operating
responsibility in a real platform.

Workers run task code when the executor sends work away from the scheduler
process. A simple local setup may not need a separate worker. A queued setup
usually adds workers and a broker, so task execution can happen outside the
scheduler service.

Folder mounts connect your local project to the containers. A typical local
project mounts `dags/` and `logs/`, and it may also mount plugins,
configuration, and supporting Python code. Those mounts create fast feedback,
but they can also hide a weak project structure if every transformation lives
inside a DAG file.

This is where Compose connects to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}) practice:
the local environment should teach orchestration, not become the place where
all pipeline logic is buried.

## DAG Project Structure

A useful Airflow Docker Compose project is boring to navigate. Keep the
orchestration files separate from the work they call.

Use `dags/` for DAG definitions and use `src/`, `include/`, or another clear
folder for reusable Python code. Keep SQL, dbt models, validation logic, and
extract/load helpers in places where they can be reviewed outside Airflow.
They should be testable there too. Use `requirements.txt`, `pyproject.toml`,
or an image build step for dependencies. Document startup, reset, and expected
services in the project README.

The DAG file should mostly describe orchestration:

- schedule
- dependencies
- retries
- owners
- task definitions
- calls into the real work

This follows Natalie's orchestration boundary. Airflow can trigger Airbyte and
dbt, and it can also trigger Python, Spark, or warehouse work. Each tool should
still own its part of the pipeline.

For adjacent stack decisions, see
[Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }}) and
[ETL vs ELT]({{ '/wiki/etl-vs-elt/' | relative_url }}). Also use
[Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }}).

## Persistence and Logs

Persistence is where local Airflow starts to feel like a real system.

For learning, it's useful to reset everything often. You can delete local
volumes and restart the containers to see how Airflow initializes. For DAG
development, you usually want more state. The metadata database should survive
container restarts so you can look at previous DAG runs, failed tasks, retries,
and backfills. Logs should be mounted or stored where the UI can read them
after a task fails.

Think about three local persistence categories:

- Airflow metadata, usually in a database volume
- task logs, usually mounted or written to a shared path
- project code, usually mounted from the working directory

The same categories become production responsibilities later. Teams need
metadata database backups, durable task logs, managed access to secrets, and
managed access to connections. Alert owners and recovery steps need the same
attention.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) ties
that local-to-production jump to DataOps in
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}).
The episode frames reliable data work around automation and observability. It
also covers CI/CD, tests, and recovery. Airflow can show a task state, but
[DataOps]({{ '/wiki/dataops/' | relative_url }}) is what turns the workflow
into a maintained data system.

## Executors and Scale

You don't need to master every Airflow executor before using Docker Compose.
You do need the high-level distinction.

A simple local executor can run work in the same local environment. It's
enough for learning DAG structure, dependencies, retries, and logs. A queued
or distributed executor separates scheduling from task execution. It usually
adds workers and a broker, and it's closer to how teams think about
concurrency, isolation, and scale.

Start with the smallest setup that teaches the workflow. Add workers when you
need to understand task execution across services, not because a larger
Compose file looks more realistic.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) gives the same
staged approach in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 34:16, he describes moving code out of notebooks into Docker
containers and scheduled production work. Around 35:46, he says simpler
scheduled containers can be enough before adopting a framework such as
Airflow. Around 41:06, he recommends adding bigger infrastructure when teams
need more logging, insight, and control.

For Airflow Docker Compose, that means the learning order matters. First make
a simple DAG understandable. Then make the task environment reproducible.
Then add persistence and logs. Only after that should a learner add
worker-based execution, brokers, or production-like deployment concerns.

## Production Boundary

Docker Compose is a local tool. It can model services and dependencies, but it
doesn't solve production operations.

Move beyond a local Compose setup when any of these become true:

- several people deploy or edit DAGs
- failures need alerts and owners
- logs must be retained and searchable
- secrets need managed storage and access controls
- the metadata database needs backups and upgrades
- workers need isolation, concurrency, or autoscaling
- backfills can compete with current runs
- workflows call production databases, warehouses, queues, or APIs
- downstream users depend on the outputs for reports, ML jobs, product
  features, or operational decisions

[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) gives the
tool-choice version in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
Around 35:37, he names Airflow and Prefect as orchestration choices. He also
mentions Dagster and GitHub Actions. Around 37:08, he notes that GitHub
Actions can be enough for simple workflows because it avoids always-on
orchestrator cost.

That doesn't make GitHub Actions a replacement for every Airflow use case. It
sets the selection standard. Match the orchestrator to the workflow and
dependency graph. Then account for team size, failure cost, and operating
burden.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) adds the platform
view in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
Around 17:22, he talks about Airflow together with conventions, playbooks, and
best practices. An Airflow cluster alone isn't a platform.

A local Compose file is even further from one. Teams need naming rules and
reusable patterns, plus alert routing, ownership, and onboarding.

Use [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Production]({{ '/wiki/production/' | relative_url }}) for those broader
operating questions.

## Failure Modes

The common mistakes come from treating Docker Compose as a shortcut around
design.

- Treating Airflow as the ETL logic instead of the orchestrator.
- Putting large transformations directly in DAG files.
- Installing dependencies on the host machine but not in the Airflow image.
- Forgetting that metadata and logs need persistence.
- Storing secrets in local files and later copying that habit into production.
- Adding distributed workers before learning the simple execution path.
- Assuming a green local run proves production readiness.
- Keeping no reset instructions, so another developer can't reproduce the
  environment.
- Skipping data-quality checks because the Airflow task status is green.

The practical standard is simple: use Docker Compose to make Airflow's moving
parts visible and repeatable. Use Airflow to coordinate recurring workflows.
Use [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
with tests, ownership, and recovery practices. That combination decides whether
the workflow is ready for other people to depend on it.

## Related Pages

For the Airflow decision, read
[Airflow]({{ '/guides/airflow/' | relative_url }}) and
[Apache Airflow]({{ '/guides/apache-airflow/' | relative_url }}). For a
learning sequence, use
[Data Engineering Roadmap]({{ '/wiki/data-engineering-roadmap/' | relative_url }})
and
[Fundamentals of Data Engineering]({{ '/guides/fundamentals-of-data-engineering/' | relative_url }}).
For operating practices, use
[DataOps]({{ '/wiki/dataops/' | relative_url }}),
[Data Observability]({{ '/wiki/data-observability/' | relative_url }}), and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
