---
layout: "person"
title: "Barr Moses"
source_person: "../datatalksclub.github.io/_people/barrmoses.md"
person_id: "barrmoses"
summary: "Monte Carlo co-founder whose DataTalks.Club episode defines data downtime, data observability signals, ownership, SLAs, and recovery workflows."
expertise: ["data observability", "MLOps", "data quality", "data reliability"]
podcast_episodes: ["data-quality-data-observability-data-reliability"]
curated: true
source_url: "https://datatalks.club/people/barrmoses.html"
---

## Background

Barr Moses is the CEO and co-founder of Monte Carlo. In
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she grounds her view of data reliability in customer data and analytics work at
GainSight. She also mentions earlier work in data, analytics, consulting, and
the Israeli Air Force. That background matters because her episode isn't mainly
about tool marketing. It's about the operational failures she saw when companies
tried to become data-driven but still learned about broken data from executives,
customers, or downstream teams.

Her contribution sits at the center of
[data observability]({{ '/wiki/data-observability/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). Use her page when the
question is how a data team detects unhealthy data, routes the incident, and
restores trust before consumers lose confidence.

## Data Downtime and Trust

Moses frames unreliable data as "data downtime." Around 5:00 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she describes a familiar failure path. A customer says a dataset looks wrong,
or a CEO questions a board-report number. The data team then starts guessing
whether the report refreshed. They also have to ask whether all data arrived or
whether an upstream schema changed.

That framing turns data quality into a production reliability problem. Data may
exist after the pipeline has completed. A dashboard, ML model, customer
workflow, or board report can still use bad data.

Her episode is useful beside
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}).
Those pages cover whether consumers can rely on data products when they make
decisions.

## Five Data Observability Signals

Around 16:38 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
Moses defines five signals for data observability.

- Freshness asks whether data arrived on time.
- Volume asks whether the amount of data is plausible.
- Distribution checks whether values moved into unexpected ranges or formats.
- Schema watches tables and fields for structural changes.
- Lineage maps upstream causes and downstream impact.

These are data signals, not just pipeline signals.
Around 13:40, Moses discusses silent failures where a job is green but only a
fraction of the expected rows arrived. Values may become null, or numeric fields
may contain unexpected strings.

Around 21:57, she names this the "good pipelines, bad data" problem. A healthy
orchestrator run still needs
[testing]({{ '/wiki/testing/' | relative_url }}), data quality checks, and
runtime observability. The practical checklist version appears in
[DataOps Checks for Data Pipelines]({{ '/how-tos/dataops-checks-for-data-pipelines/' | relative_url }}).

## Monitoring, Diagnosis, and Lineage

Moses separates monitoring from observability around 24:31 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
Monitoring tells the team that something changed, such as a freshness problem.
Observability helps the team understand why it happened, what downstream assets
are affected, and whether the incident should be fixed immediately.

Lineage is the bridge from alert to action. In the schema-change discussion
around 19:10, the episode shows how a source change can be announced in one
place but missed by affected consumers. Moses ties that example to schema and
lineage. An automated dependency map can tell which downstream jobs,
dashboards, models, and reports need notice. Around 26:04 and 58:51, she returns
to the same idea for root cause analysis and upstream or downstream impact.

That makes her episode a useful companion to
[Model Monitoring vs Data Observability]({{ '/comparisons/model-monitoring-vs-data-observability/' | relative_url }}).
When a model behaves badly, the model owner may see the symptom. Lineage may
then show that the cause started in an upstream dataset, feature table, or
schema change.

## Ownership, SLAs, and Runbooks

Moses doesn't treat observability as alerts alone. Around 29:00 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she uses RACI to separate responsible and accountable roles. The same framework
also names who should be consulted or informed across the data lifecycle. In a
small company, one data engineer may own most of the response. In a large
company, decentralized teams need self-service observability while a central
platform group defines the supported approach.

Around 35:24, she connects ownership to data SLAs. A team consuming a feature
table may need data five minutes after a user action, while another table can
wait. That agreement helps responders prioritize incidents. Around 41:03, she
adds runbooks and playbooks. The team should know who gets informed, which
systems the data engineers look at, and which steps they take.

The runbook should also say how the affected consumer is protected while the
incident is being fixed.

This operating model sits close to
[DataOps]({{ '/wiki/dataops/' | relative_url }}). It also complements
[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}), who
emphasizes DataOps automation, tests, and production recovery.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) connects
platform design to repeatable data delivery.

## Testing, Platforms, and False Positives

Moses supports tests, but she warns that tests alone cover only known failure
modes. Around 50:52 in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}),
she discusses test-driven data development, dbt checks, and manually defined
expectations. Those checks help, but teams still need monitoring and
observability for changes they didn't know to encode as tests. That boundary
connects her episode to [dbt]({{ '/wiki/dbt/' | relative_url }}) and the
practical guide
[Data Observability for Data Engineering]({{ '/guides/data-observability-for-data-engineering/' | relative_url }}).

Her platform advice is similarly pragmatic. Around 47:00, she argues that a
strong observability solution needs end-to-end visibility across warehouses and
lakes. It also has to cover ETL, BI, and ML assets.

Around 54:23-57:13, she says data observability should work across cloud
providers and distributed environments. It should still give the organization a
central way to define SLAs and reliability standards.

The final incident nuance comes around 1:00:27. Moses says a data change can be
uncommon without being bad. Teams still need to know because the change may
affect a downstream model, report, or customer workflow. Around 1:02:06, she
warns against alert fatigue.

Useful observability combines data and metadata with lineage, usage, and
dependency context. That context helps teams act on events that matter.
