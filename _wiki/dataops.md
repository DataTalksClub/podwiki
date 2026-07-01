---
layout: wiki
title: "DataOps"
summary: "Podcast-grounded reference page for DataOps as the operating discipline for reliable data pipelines, analytics workflows, and data platforms."
related:
  - DataOps Platforms
  - Data Engineering Platforms
  - Data Engineering Tools
  - Data Quality and Observability
  - Data Observability
  - Data Engineering
  - Analytics Engineering
  - Orchestration
  - CI/CD
  - MLOps
---

DataOps is the operating discipline for data pipelines, analytics workflows,
and data platforms. It makes data delivery reliable enough to change. Teams use
version control and tests to review changes. They use CI/CD and orchestration
to release them. They use observability, reproducibility, deployment checks,
and recovery paths when a pipeline has to be rerun or repaired.

In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) ties the
practice to error reduction, shorter deployment cycles, and team productivity
around 6:42. He connects observability to production errors around 7:22, then
connects version control and tests to healthier pipelines around 33:47. Around
34:37, he adds CI/CD and runbook automation.

In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) applies the
same operating idea to scalable data platforms. He focuses on immutable
pipelines, reproducibility, and self-service. He also covers workflow engines
and quality automation.

Use [MLOps]({{ '/wiki/mlops/' | relative_url }}) for production machine
learning systems. Use
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}) when the
question is about the boundary between model lifecycle work and data delivery
work. Use
[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
when the question is whether the team needs pipeline-building ownership or a
stronger operating discipline. Use
[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }})
when the question is how DataOps becomes shared platform infrastructure.

## Operating Scope

The archive frames DataOps from two sides: platform architecture and delivery
practice. In
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
Albertsson starts from platform architecture. He covers immutable pipelines,
reproducibility, workflow engines, and schema automation. Self-service sits in
the same platform view.

In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
and
[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }}),
Bergh starts from delivery practice. He covers version control, tests, and
CI/CD. Monitoring, runbooks, and on-call readiness complete that operating view.

Other episodes fill in the systems DataOps has to operate. In
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains ELT and
dbt-style transformations. She also covers orchestration and CDC. Schema
evolution, warehouses, and lake architecture sit in the same discussion. In
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) defines the monitoring
signals DataOps teams use when pipelines silently produce bad data.

## Common Definition

Across the archive, DataOps means making data delivery repeatable and
recoverable. Bergh's two DataOps interviews define that through delivery
practice.
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
connects DataOps to error reduction, deployment cycle time, and productivity.
It also connects DataOps to monitoring, tests, CI/CD, and automated playbooks.

[DataOps for Data Engineering]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})
adds regression tests and realistic test data around 30:55. Bergh also covers
deployment automation at 42:39, production monitoring at 50:29, and on-call
readiness at 26:13.

Data work fails in ways application uptime checks may miss. Sources and schemas
change. Files arrive late. Transformations break. Dashboards or models may
consume the result before the producing team notices.

Moses describes this failure mode in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
Data teams may have "good pipelines" that still deliver bad data. They need
freshness, volume, and distribution signals. They also need schema, lineage,
and ownership. SLAs and runbooks make those signals actionable.

## Platform and Delivery Practice

DataOps can start from platform design or from day-to-day delivery practice.
Albertsson starts from the platform side in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
He discusses workflow engines around 10:48, immutable and functional pipeline
architecture around 16:42, and reproducibility problems around 20:12. Around
30:34, he breaks the platform into storage, compute, and workflow engines. He
then covers batch-versus-streaming tradeoffs around 41:53 and quality or schema
automation around 46:52.

In that framing, teams need self-service data access
without losing reproducibility, ownership, or quality.

Bergh starts from team delivery. In
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}),
he emphasizes version control, tests, and CI/CD. He also discusses
observability, automated playbooks, and replaceability. He connects those
practices to handoffs and end-to-end versioning.

A large data platform may begin with shared infrastructure and conventions. A
smaller data team may begin with Git and tests. It may then add a scheduler,
basic monitors, and a recovery runbook. Both paths are DataOps when they make
data changes reviewable, testable, observable, and recoverable.

## Pipeline Scope

DataOps applies to ingestion jobs and transformations. It also applies to
datasets, dashboards, data products, and analytics workflows. Kwong's
[Data Engineering Tools and Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})
shows the range DataOps has to cover. The modern stack spreads responsibility
across ELT, raw ingestion, and warehouse transformations. It also includes dbt
and orchestration.

It also includes CDC, schema evolution, and warehouse analytics. DataOps is the
operating discipline that keeps that path inspectable and repairable, not a
substitute name for any one tool.

This is where [Orchestration]({{ '/wiki/orchestration/' | relative_url }}),
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}), and
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
connect to DataOps. Another person should be able to review a data change,
test it with realistic data, and rerun it after failure. They should also be
able to observe its outputs and fix it without reverse-engineering the whole
pipeline.

## DataOps vs Data Engineering

[DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
covers the full boundary, while this page gives the reference definition.

[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}) builds the
data path from source systems to consumers. [DataOps]({{ '/wiki/dataops/' | relative_url }})
makes that path reviewable, testable, observable, and recoverable. The
distinction is build work versus operating discipline, not one job title versus
another.

Kwong's modern-stack episode shows the engineering side. She covers ETL and
ELT, dbt-style warehouse modeling, and Airflow orchestration. CDC and schema
evolution belong in the same engineering discussion
([3:46-12:39 and 30:59-48:58]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
Those choices define how data moves, where business logic lives, and how
consumers receive the output.

Bergh's DataOps episodes add the operating layer. Teams use version control and
CI/CD to review and release pipeline changes. Regression tests and realistic
test data check those changes before production.

Deployment automation, production monitoring, runbooks, and on-call readiness
help teams recover
([30:55-50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).
Albertsson adds the platform version. His version uses self-service, immutable
pipelines, reproducibility, and workflow engines. Quality automation and lineage
make the same platform easier to operate
([7:52-46:52]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

The boundary shows up most clearly during incidents. A data engineer may fix a
bad transformation or source schema. DataOps practice makes sure the team
knows who owns the dataset and why the alert fired. The team also needs to know
how to replay the job and prevent the same silent failure next time.

Moses's observability discussion grounds that difference. A scheduled job can
succeed while the data is still wrong. Teams need freshness, volume, and
distribution signals. Schema and lineage signals matter too. SLAs and runbooks
make those signals operational
([16:38-41:03]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

## GitOps and Team Enablement

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) adds the
infrastructure side of DataOps in
[DataOps and GitOps for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}).
He describes DataOps as making data work faster and less scary around 18:59,
then shows how infrastructure practice supports that goal. Around 20:56
through 26:21, he discusses SQL, secrets, and GitOps. He also covers
Infrastructure as Code.

He then connects that workflow to Terraform, Terragrunt, and Atlantis. Teams use
merge requests, dry runs, and applies to make infrastructure changes reviewable.

That episode keeps DataOps connected to enablement rather than management.
Hinc discusses platform teams reviewing changes at 13:07 and onboarding
friction for data scientists at 27:34. He also covers proactive support,
cross-team education, and minimal operational skills. Those operational skills
include Git, command line use, IAM, and password managers.

Operational practice has to fit the people changing the pipelines. It can't
fit only the infrastructure team that owns the platform.

## Observability and Recovery

DataOps depends on observability, but it's broader than observability. Moses
defines data observability through freshness, volume, and distribution at 16:38
in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
She includes schema and lineage in the same framework.
She then connects those signals to root-cause analysis, ownership, and data
SLAs. Later sections cover threshold automation, operational runbooks, and
false-positive reduction.

DataOps uses those signals inside the larger delivery system. Bergh's DataOps
episodes connect monitoring to CI/CD, regression tests, and deployment
confidence. They also connect monitoring to automated playbooks and on-call
readiness.

Use
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}) for
the monitoring layer. Use this DataOps page for the operating model around
tests and releases. It also covers alerts, recovery steps, and ownership.

## Relation to MLOps

DataOps and [MLOps]({{ '/wiki/mlops/' | relative_url }}) overlap because
production ML depends on production data, but they operate different objects.
DataOps teams operate upstream pipelines, datasets, transformations, and
features. They also handle metadata, quality checks, and recovery paths. MLOps
teams add model artifacts, training jobs, and inference paths. They also handle
model registries, retraining decisions, and model behavior.

Bergh makes the shared DevOps inheritance explicit in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})
around 50:42, while Albertsson separates shared principles from ML-specific
requirements in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
around 53:31.

The boundary matters during incidents. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) connects model
monitoring to ETL, data pipelines, and upstream root causes around 27:35.

A model alert may come from model drift. It may also come from a late table, a
changed schema, a broken feature pipeline, or a missing label. DataOps teams
handle the data delivery investigation. MLOps teams handle the model lifecycle
investigation.

## Related Pages

Use these pages for adjacent DataOps topics and the MLOps boundary:

- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }})
- [DataOps Tools]({{ '/guides/dataops-tools/' | relative_url }})
- [Data Engineering Tools]({{ '/wiki/data-engineering-tools/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Orchestration]({{ '/wiki/orchestration/' | relative_url }})
- [CI/CD]({{ '/wiki/ci-cd/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }})
- [DataOps vs Data Engineering]({{ '/comparisons/dataops-vs-data-engineering/' | relative_url }})
