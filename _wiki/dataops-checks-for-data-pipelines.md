---
layout: article
tags: ["how-to"]
title: "DataOps Checks for Data Pipelines"
keyword: "dataops checks for data pipelines"
secondary_keywords:
  - "data quality checks"
  - "data pipeline checks"
  - "dataops checks"
  - "data quality checks for data pipelines"
  - "pipeline data quality checks"
summary: "A practical checklist for adding DataOps checks to data pipelines: freshness, volume, schema, distribution, uniqueness, business rules, CI/CD, runbooks, and recovery."
search_intent: "People searching for DataOps checks for data pipelines usually want concrete checks they can add to batch or streaming data workflows, plus guidance on how those checks fit CI/CD, observability, runbooks, and recovery."
related_wiki:
  - DataOps
  - Data Quality and Observability
  - DataOps Platforms
  - Data Pipelines
  - CI/CD
  - Orchestration
---

DataOps checks make a data pipeline safer to change and easier to recover. They
don't replace pipeline design, orchestration, or observability. They turn the
most important data assumptions into automated checks that run before and after
production changes.

Before adding tools, define what each critical check measures and where it
runs. Also define what it blocks and who acts when it fails. A freshness check
that only sends a vague alert is weaker than one that stops publication. It
should also name the affected dashboard or model and link to a backfill step.

Use this page after the basic pipeline is clear. The build sequence lives in
[How to Build Data Pipelines]({{ '/wiki/how-to-build-data-pipelines/' | relative_url }}).
The reliability background lives in
[DataOps]({{ '/wiki/dataops/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}), and
[Data Observability for Data Engineering]({{ '/wiki/data-observability-for-data-engineering/' | relative_url }}).

[Barr Moses]({{ '/people/barrmoses/' | relative_url }}) gives the main runtime
signals in
[Data Observability Explained]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }}).
Her framework starts with freshness and volume. It also uses distribution,
schema, and lineage. She warns that engineering jobs can succeed while the data
is still wrong
([good pipelines and bad data at 21:57]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) adds the
delivery path through version control, automated tests, and CI/CD. He connects
those release practices to monitoring, runbooks, and end-to-end deployment
automation
([DataOps steps at 33:47-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

## Start With The Pipeline Agreement

Before writing checks, name the agreement the pipeline must satisfy. A useful
agreement says what dataset is produced and who consumes it. It also names the
readiness window, required columns, key fields, and unsafe output cases.

That agreement connects [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
to [DataOps]({{ '/wiki/dataops/' | relative_url }}), and Bergh frames the same
problem as "done" versus "good." A data product isn't ready until a team can
hand it off and version it. The team also needs tests, monitoring, and a
recovery path
([handoffs and readiness around 38:01-43:06]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

Write the first agreement in plain language:

1. This pipeline publishes `orders_daily`.
2. The marketing dashboard and reverse ETL sync consume it.
3. The table must be fresh by 07:00 local time.
4. `order_id` is unique at the published grain.
5. Required columns are `order_id`, `customer_id`, `order_ts`, `status`, and
   `net_revenue`.
6. A run is unsafe if it publishes zero rows, duplicated orders, negative net
   revenue, or a missing latest partition.
7. Unsafe output stays in quarantine until the owner approves a rerun, backfill,
   or consumer warning.

The same agreement should link to the owner and runbook. It should also name
downstream consumers. Moses connects that ownership layer to RACI-style
accountability. She also ties ownership to data SLAs and operational runbooks
([ownership, SLAs, and runbooks at 29:00-41:03]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

## Check Freshness

Freshness asks whether data arrived when consumers expected it. It's the first
check for daily dashboards and hourly operational tables. It also matters for
feature pipelines, reverse ETL syncs, and customer-facing reports.

Moses describes freshness with a table that normally updates several times an
hour and then stops updating. Don't stop at checking whether the scheduler ran.
Ask whether the latest data is current enough for the use case
([freshness pillar at 16:38]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Add freshness checks at two levels:

1. Source freshness: the source file, API window, CDC batch, or event partition
   arrived.
2. Output freshness: the published table or serving asset has a latest timestamp
   within the agreed window.
3. Consumer freshness: the dashboard, feature table, or activation job sees the
   new partition after publication.

For a batch table, a minimal check can compare `max(event_ts)` or
`max(loaded_at)` with the expected cutoff. For a partitioned table, check that
the expected partition exists and has rows. For streaming or micro-batch flows,
track event-time lag and processing-time lag separately.

Freshness needs priority, not just alerting. Moses uses a five-minute SLA
example to separate urgent and non-urgent incidents. A critical feature table
and a low-use table shouldn't create the same response
([data SLAs at 35:24-40:43]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Set the action in advance. Retry when source delay looks transient, and hold
publication when the output is stale. Notify consumers when the SLA will be
missed.

## Check Volume

Volume asks whether the amount of data is plausible, catching empty outputs and
partial extracts. It also catches duplicated loads, broken filters, and missing
CDC windows.

[Tomasz Hinc]({{ '/people/tomaszhinc/' | relative_url }}) gives the simplest
failure case in
[DataOps and GitOps for Data Teams]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }}):
Airflow jobs can be green while zero records are inserted. A scheduler success
state only proves that the task completed. It doesn't prove that useful data
arrived
([Airflow caveat at 1:02:50]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Start with these volume checks:

1. Output row count is greater than zero.
2. Output row count is within an expected range.
3. Input-to-output count ratios are plausible.
4. New rows aren't far below or above the historical baseline.
5. Incremental loads don't repeat a previous window.
6. Deletes, late-arriving records, and CDC updates reconcile against the source
   window.

Use hard thresholds for safety checks and historical baselines for anomaly
checks. Moses notes that volume expectations can often be inferred from history,
then overridden when a consumer needs a stricter SLA
([threshold automation at 38:14]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
Fail hard for impossible cases such as zero rows in a required daily table. Send
review alerts for plausible but unusual spikes.

## Check Schema

Schema checks protect downstream SQL, dashboards, ML features, and activation
jobs from structural changes. A schema check should fail when required columns
are missing. It should also fail when data types change incompatibly, nested
fields disappear, or a source adds a breaking value structure.

Moses treats schema as one of the five observability pillars. She ties it to
downstream breakage after a missed schema-change notification
([schema case study at 19:10]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) puts schema
automation into the DataOps maturity ladder. He says teams should automate
schema management so incompatible changes don't flow into production unnoticed
([schema automation at 46:52]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

Add schema checks for:

1. Required columns and nested fields.
2. Data types and precision.
3. Allowed nullable columns.
4. Enum-like fields such as `status`, `country`, or `plan`.
5. Backward-compatible changes for streams, CDC feeds, and shared tables.
6. Schema agreement changes that need consumer approval before publication.

For orchestration practice, keep schema checks close to the code that reads or
publishes the data. [Airflow Docker Compose]({{ '/wiki/airflow-docker-compose/' | relative_url }})
shows one local setup. The check should usually live in a test layer such as SQL
or dbt. Python, Great Expectations, and Soda can serve the same role.

Keep the logic out of a large DAG file. For shared streams, connect the same
check to the schema-change rules in
[How to Build Data Pipelines]({{ '/wiki/how-to-build-data-pipelines/' | relative_url }}).

## Check Distribution

Distribution checks ask whether values still look plausible. They catch null
spikes, impossible dates, negative amounts, and extreme values. They also catch
changed category mixes and shifted product or geography groups.

Moses defines distribution as the signal for value ranges and unexpected field
contents. Her examples include values moving far outside the expected range and
fields receiving the wrong kind of content
([distribution pillar at 16:38-19:10]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Use distribution checks where bad values can silently change a metric:

1. Required dimensions aren't mostly null.
2. Numeric values stay within domain limits.
3. Dates are inside the processing window.
4. Category shares don't shift beyond a reviewed threshold.
5. ML features stay inside expected ranges before training or scoring.
6. Currency, unit, timezone, and status-code values still match the business
   definition.

Not every anomaly is bad data, and Moses warns that uncommon data may be
intentional. It still needs context because it can affect a model, report, or customer
workflow
([anomalies and false positives at 1:00:27]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
Treat distribution checks as review triggers when business context matters and
as hard failures when the value is impossible.

## Check Uniqueness And Grain

Uniqueness checks protect the grain of a table. They catch duplicate primary
keys, accidental many-to-many joins, repeated incremental loads, and merged
records that no longer represent one entity.

The check should state the grain in the same language as the consumer:

1. One row per `order_id`.
2. One row per `customer_id` per day.
3. One row per account per subscription period.
4. One latest feature row per entity.
5. No duplicated merge key in the staging data before upsert.
6. No overlapping effective-date windows for slowly changing records.

Put this beside [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
and [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}) because the
check protects meaning, not only mechanics. In the pipeline build guide,
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) emphasizes keys and
foreign keys. She also emphasizes business entities and the question the
pipeline must answer
([modeled entities at 39:23-43:05]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

Hinc warns that successful jobs may still publish wrong rows, so verify merge
keys before publishing
([Airflow and zero records at 1:02:50]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
For a published table, the basic SQL check is `count(*) = count(distinct key)`.
For composite grains, define the exact key tuple and test that tuple.

## Check Business Rules

Business-rule checks encode known truths about the data product. They're more
specific than freshness, volume, schema, or distribution checks. They should
come from the people who use the output.

Examples:

1. Paid orders can't have negative `net_revenue`.
2. A completed trip must have both pickup and dropoff timestamps.
3. A monthly recurring revenue table can't publish two active subscriptions for
   the same customer and product.
4. A campaign audience can't include users who opted out.
5. A feature table can't score entities without the required source event.
6. A financial report can't publish until the period is closed.

Bergh describes this style of test as checking expected row counts and report
values. He also names regression impact. For tooling, he names dbt tests and
Great Expectations. SQL checks can automate the same assertions
([automated production tests at 33:47 and tooling at 48:25]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

Don't try to encode every edge case. Hinc argues for pragmatic edge-case checks
because company data flows constantly and perfection isn't realistic. Focus on
cases that would make a leadership report, customer workflow, or model output
unsafe
([confidence and edge cases at 1:02:28]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).

Write each business rule with an owner, a failure severity, and a default
action. Some rules should block publication. Others should open a ticket because
the business owner needs context before deciding.

## Check Lineage And Impact

With lineage checks, the team should be able to trace a bad output. The trace
should show the upstream source and downstream consumer. It should also show the
code or schema change.

Moses separates detection from diagnosis. Teams need logs, correlations, and
lineage to find the root cause and understand the blast radius
([root cause and lineage at 24:31-26:04]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
She returns to automatic upstream and downstream lineage later in the same
episode
([automatic lineage at 58:51]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Add lineage checks for:

1. The run records source versions, input partitions, code version, and output
   partition.
2. The published dataset links to downstream dashboards, models, syncs, and
   owners.
3. The alert includes the failed check, affected asset, run id, and latest
   successful run.
4. The runbook names which downstream consumers to pause or warn.

[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}) treats
lineage, ownership, and runbooks as part of the operating layer, not separate
documentation. Use lineage to route incidents. Use it to choose a recovery
path. That path may be a rerun or backfill. It may also be rollback,
quarantine, or consumer communication.

## Put Checks In CI/CD

DataOps checks should run before production when the failure is predictable.
That means checking SQL models and Python code. Check DAG definitions, config
files, schema agreements, and infrastructure changes in
[CI/CD]({{ '/wiki/ci-cd/' | relative_url }}).

In Bergh's newer DataOps episode, he recommends robust CI/CD pipelines and
realistic test data. He also recommends infrastructure as code and low-risk
deployment paths. Version control alone isn't enough, so teams need end-to-end
tests and automated checks before production
([CI/CD and test data at 30:55-43:02]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

Use CI/CD for:

1. Unit tests for parsing and transformation helpers.
2. SQL or dbt tests for models and constraints.
3. Schema compatibility tests for source and output agreements.
4. Sample-data regression tests for joins and business rules.
5. DAG validation for missing dependencies, owners, retries, and schedules.
6. Infrastructure checks for permissions, secrets references, and environment
   configuration.
7. Dependency checks for pinned Python packages, container images, and dbt
   packages.
8. Promotion checks that compare staging output with the current production data
   agreement before deployment.

Hinc adds the GitOps path for infrastructure and access changes. In his episode,
teams use Terraform and Terragrunt. Atlantis dry runs, merge requests, and
review make data infrastructure changes reproducible and safer to apply
([GitOps workflow at 20:56-26:21]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
That same review habit should cover pipeline dependencies and secrets.

To keep runs reproducible, pin dependencies. Hinc describes a containerized job
failing because a Python dependency wasn't fixed and the latest version changed
its API
([dependency failure at 1:01:27]({{ '/podcasts/dataops-and-gitops-best-practices-for-data-teams/' | relative_url }})).
Dependency drift is a DataOps check because it can break a pipeline without any
business logic change.

## Connect Checks To Orchestration

[Orchestration]({{ '/wiki/orchestration/' | relative_url }}) coordinates the
work and should expose check failures clearly. A data check that fails
should stop publication, page the right owner when the SLA requires it, and
record enough context for recovery.

Albertsson describes the workflow engine as the component that tracks
dependencies and schedules work. It retries after late data or transient
failures, which keeps a fragile set of processing components sane
([workflow engine at 30:34-35:57]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).
That's the right place to connect checks to retries, backfills, and dependency
state. The processing and validation logic can still live outside the scheduler.

For Airflow projects, make checks visible as tasks or task groups:

1. Validate source arrival.
2. Load or transform data.
3. Run table checks.
4. Record lineage and check results.
5. Publish only after checks pass.
6. Notify consumers or quarantine output when checks fail.
7. Trigger a retry, rollback, or backfill path when the runbook allows it.

For a local Airflow setup, use
[Airflow Docker Compose]({{ '/wiki/airflow-docker-compose/' | relative_url }}).
This rule is broader than Airflow: a green orchestrator run should mean the
data agreement passed, not merely that the Python task exited.

## Build Runbooks And Recovery Paths

Every important check needs a recovery path:

1. A failed freshness check may need a retry, a delayed publication, or a
   consumer warning.
2. A failed schema check may need rollback, source-team escalation, or a
   compatibility patch.
3. A failed business-rule check may need quarantine before a dashboard, model,
   or activation job reads the output.
4. A failed lineage check may need a manual impact review before anyone trusts
   the alert scope.

Moses connects observability to diagnosis and impact analysis. Lineage shows
which downstream tables, reports, models, or customer workflows depend on the
broken asset
([root cause and lineage at 24:31-26:04]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
That impact map should appear in the runbook, not only in an observability UI.

Bergh pushes teams from manual runbooks toward automated playbooks. The manual
runbook is still useful because it names the decision path. Automation should
then handle repeated actions such as retrying, pausing publication, opening an
incident, or running a backfill
([runbooks to automated playbooks at 34:37]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

For each critical pipeline, write a compact runbook:

1. Owner and escalation channel.
2. Freshness SLA and business priority.
3. Downstream dashboards, models, reverse ETL syncs, and consumers.
4. How to rerun the job safely.
5. How to backfill missing data.
6. How to quarantine or roll back bad output.
7. How to notify consumers.
8. Which missing test or alert should be added after the incident.
9. Which CI/CD or orchestration check should prevent the same failure next time.

Recovery should improve the next release. Bergh recommends starting from
production monitoring because real failures show which operating gaps matter
([production monitoring at 50:29]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

## DataOps Check Sequence

Use this sequence for a new or existing pipeline:

1. Name the consumer, dataset, owner, SLA, and unsafe-output cases.
2. Add freshness checks for source arrival and published output.
3. Add volume checks for zero rows, row-count ranges, and incremental load
   windows.
4. Add schema checks for required columns, types, nullability, and compatible
   changes.
5. Add distribution checks for null spikes, impossible values, value ranges, and
   category shifts.
6. Add uniqueness checks for the published grain and merge keys.
7. Add business-rule checks for the decisions, dashboards, models, or workflows
   that consume the data.
8. Add lineage checks for upstream inputs, output partitions, downstream
   consumers, and owners.
9. Run predictable checks in CI/CD with realistic test data.
10. Connect production checks to the orchestrator so failed checks stop unsafe
   publication.
11. Attach every critical check to a runbook, owner, lineage context, and
    recovery path.

Use the checklist as the practical overlap between
[DataOps Platforms]({{ '/wiki/dataops-platforms/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [DataOps]({{ '/wiki/dataops/' | relative_url }}). Run checks before release,
observe data after release, and recover when the data isn't fit for use.

