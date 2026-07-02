---
layout: wiki
title: "DataOps Operating Model"
summary: "How data teams turn DataOps principles into an operating model for releases, tests, observability, ownership, productivity, and day-two data operations."
related:
  - DataOps
  - CI/CD
  - Testing
  - Data Quality and Observability
  - Data Observability
  - Data Pipelines
  - DevOps to Data Engineering
  - Data Engineering Platforms
  - Orchestration
---

A DataOps operating model describes how a data team runs change after a
pipeline exists. The same model applies to dashboards, model inputs, and data
products. It turns the broader
[DataOps]({{ '/wiki/dataops/' | relative_url }}) discipline into roles and
release paths. It also defines checks, observability, and recovery habits. Use
it beside the pipeline-level checklist in
[DataOps Checks for Data Pipelines]({{ '/wiki/dataops-checks-for-data-pipelines/' | relative_url }})
and the monitoring-focused pages
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) frames
the model as a middle path between fear-driven process and unsustainable
heroism. In
[DataOps for Data Engineering at 13:27]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
he describes teams where a few people hold the knowledge. Deployments feel
dangerous, and production recovery depends on heroic work.

At
[15:52 in the same episode]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
he names automation and testing as practices that reduce production errors and
cycle time. Monitoring and observability belong in the same set. Those
practices need management rules. The model says which changes enter the system
and which checks must pass. It also says who responds to failures and how the
team improves the path after each incident.

## Operating Definition

The podcast discussions treat DataOps as operating discipline, not a tool
category. Bergh says data teams need to think beyond the first build. Day one
creates the asset. Day two runs it with new data. Day three changes it as
customer needs evolve
([24:24]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

That makes the operating model broader than [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
but CI/CD is still the release spine. The team reviews code and pipeline
definitions before they affect consumers. Tests, infrastructure, and metadata
changes belong in the same path
([31:45]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

The model also has to fit modern platform boundaries. In
[Trends in Modern Data Engineering at 11:03]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
[Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }}) describes data
engineering splitting into specialties. He names governance, data quality, and
streaming.

At
[21:27]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}),
he separates storage and compute from access, metadata, and lineage. A DataOps
operating model has to assign ownership across those layers. A failed release
may involve SQL logic or orchestration. It may also involve table formats,
catalogs, permissions, or downstream consumers rather than one isolated job.

## Release Path

The practical release path starts with version-controlled changes, but Git
isn't enough. Bergh argues that teams need end-to-end tests and automated
checks before production. He also warns that adoption often stays uneven across
data engineers, analysts, and data scientists
([43:02]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
[46:27]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
The operating model should therefore define one supported path for changes to
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) and dbt models.
It should also cover notebooks that become jobs, orchestration definitions,
quality checks, and infrastructure-as-code changes.

A useful path has four gates:

- Reviewable: the owner, consumer impact, and expected output are visible.
- Testable: regression tests and realistic test data exercise the code and data
  assumptions, following Bergh's CI/CD discussion at
  [30:55]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}).
- Deployable: the release uses an automated path rather than a manual checklist
  ([31:45]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
- Observable: the team can see whether freshness, schema, lineage, and
  downstream behavior remain healthy after release.

For the check catalogue, use
[DataOps Checks for Data Pipelines]({{ '/wiki/dataops-checks-for-data-pipelines/' | relative_url }}).

## Tests and Data Checks

DataOps testing isn't only unit testing around code. Bergh's operating claim is
that teams need test data that reflects real scenarios. They also need
regression tests and automated deployment checks, so newer team members can
change production paths without relying on private knowledge
([26:54]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
[31:45]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
That puts [Testing]({{ '/wiki/testing/' | relative_url }}) inside the operating
model rather than after it.

The model should separate pre-release checks from production checks. Pre-release
checks catch known failure modes such as SQL syntax, model dependencies, and
schema contracts. They also catch expected row counts, business rules, and
unsafe transformations.

Production checks catch behavior that only appears with live data. Bergh's
observability-first turn starts from existing production systems because many
teams already have production assets without development discipline
([50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
That's where the operating model meets
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}):
tests prevent known breakage, while observability notices new breakage.

## Day-Two Operations

Day-two data operations begin when new data keeps arriving after the first
release. Bergh's day-one, day-two, and day-three framing makes ownership
explicit. The team must run the system and notice problems before customers do.
It also has to support safe changes as requirements move
([24:24]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
[26:54]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

In practice, each important dataset or pipeline needs an owner and an expected
update window. It also needs a severity rule, a runbook, and known downstream
consumers.

Observability is the operating signal layer, not the whole model. A monitor can
show late data or a schema change, while the operating model decides who gets
alerted and how impact is assessed. It also decides which fix path is allowed.

Bergh links production monitoring to improvement work at
[50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}), and
Brudaru's catalog discussion adds why metadata matters. Access control,
metadata, and lineage sit beside storage and compute. Responders need more than
scheduler status to understand the blast radius
([21:27]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

## Productivity and Rework

The operating model should reduce rework, not only accelerate creation. Bergh
argues that generating dashboards, models, or ETL code tackles a small part of
the problem. Most time is lost to fixes, miscommunication, and repeated failure
recovery
([39:09]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
He ties productivity to reduced production errors and shorter cycle time at
[16:10]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}), then
returns to version control and automated tests as day-to-day controls.
Observability belongs with them at
[35:36]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}).

That changes how teams should measure DataOps. A useful operating model watches
lead time for data changes and failed deployments. It also watches repeated
incidents, manual handoff steps, diagnosis time, and the number of pipelines
that only one person can operate. Those measures complement
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
because the supported path should make good practice the default, not a heroic
extra step.

## Platform Fit

DataOps doesn't require one heavyweight platform. Brudaru's 2025 tooling
discussion shows why the operating model should be capability-based. He notes
that some teams can run cost-efficient pipelines with DuckDB and GitHub Actions
([27:40]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})),
while orchestration choices depend on the team and workflow. His examples
include Airflow, Prefect, Dagster, and GitHub Actions
([35:37]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }})).

Bergh gives the same sizing principle for deployment targets. Teams can learn
Docker first and use Kubernetes only when the number of processes and services
justifies the complexity
([52:42]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

The operating question is therefore not "which stack is DataOps?" The question
is whether the chosen [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
make changes reviewable and testable. They should also make changes observable,
recoverable, and affordable.

For small workflows, the supported path may be a repository and a scheduled
GitHub Action. SQL tests and a runbook may be enough. Larger teams may add
[Orchestration]({{ '/wiki/orchestration/' | relative_url }}), catalogs, and
lineage. They may also add access controls, environment promotion, and platform
templates.

## DevOps Habits That Transfer

[Agita Jaunzeme]({{ '/people/agitajaunzeme/' | relative_url }}) gives the
human version of the transfer from DevOps habits into data work. In
[From DevOps to Data Engineering at 5:22]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}),
she describes moving into early DevOps and configuration management work where
the team automated operational tasks. At
[14:29]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }}),
she explains how a repetitive manual workflow with printed instructions became
automation, reducing human error and earning trust.

The transferable habit isn't a specific tool. It's the ability to spot
repeatable operational work, encode it, document it, and improve it. Jaunzeme
later names processes and documentation as corporate practices she could apply
in other settings. She also names ticketing, retrospectives, planning, and
problem-solving
([21:03]({{ '/podcasts/from-devops-to-data-engineering-automation-open-source-volunteering/' | relative_url }})).

Bergh's DataOps model applies the same habit to data releases. Teams automate
deployment, keep logic in version control, run development checks before
production, and make the whole team use the path
([43:02]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
For the career and skill boundary, see
[DevOps to Data Engineering]({{ '/wiki/devops-to-data-engineering/' | relative_url }}).
