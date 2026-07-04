---
layout: article
tags: ["how-to"]
title: "DataOps Pipeline Checks"
keyword: "dataops checks for data pipelines"
secondary_keywords:
  - "data quality checks"
  - "data pipeline checks"
  - "dataops checks"
  - "data quality checks for data pipelines"
  - "pipeline data quality checks"
summary: "Checklist for DataOps pipeline checks: freshness, volume, schema, distribution, business rules, CI/CD, runbooks, and recovery."
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

Start with a clear pipeline design before adding these checks. For the build
sequence, use [[How to Build Data Pipelines]].
For reliability context, use [[DataOps]] and
[[Data Quality and Observability]]. For platform and observability context, use
[[DataOps Platforms]] and [[Data Observability for Data Engineering]].

Freshness and volume checks usually come first. Distribution, schema, and
lineage checks catch failures that a green engineering job can still miss
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Release checks belong in version control, automated tests, and CI/CD. Production
checks need monitoring, runbooks, and deployment automation so a failed check
has a recovery path [[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].

## Start With The Pipeline Agreement

Before writing checks, name the agreement the pipeline must satisfy. A useful
agreement says what dataset is produced and who consumes it. It also names the
readiness window, required columns, key fields, and unsafe output cases.

That agreement connects [[data pipelines]]
to [[DataOps]]. A data product isn't ready when the code merely runs. It also
needs a handoff and versioning. Tests, monitoring, and a recovery path make it
operable
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].

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
downstream consumers. RACI-style accountability, data SLAs, and operational
runbooks keep the check attached to the team that can act on it
[[cite:data-quality-data-observability-data-reliability@29:00=>Data Observability Explained]].

## Check Freshness

Freshness asks whether data arrived when consumers expected it. It's the first
check for daily dashboards and hourly operational tables. It also matters for
feature pipelines, reverse ETL syncs, and customer-facing reports.

Freshness failures can hide behind a successful scheduler run when a table that
normally updates several times an hour stops receiving new data. Don't stop at
checking whether the scheduler ran. Ask whether the latest data is current
enough for the use case
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

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

Freshness needs priority, not just alerting. A five-minute SLA should create a
different response from a low-use table with a loose expectation
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Set the action in advance. Retry when source delay looks transient, and hold
publication when the output is stale. Notify consumers when the SLA will be
missed.

## Check Volume

Volume asks whether the amount of data is plausible, catching empty outputs and
partial extracts. It also catches duplicated loads, broken filters, and missing
CDC windows.

Airflow jobs can be green while zero records are inserted. A scheduler success
state only proves that the task completed. It doesn't prove that useful data
arrived [[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].

Start with these volume checks:

1. Output row count is greater than zero.
2. Output row count is within an expected range.
3. Input-to-output count ratios are plausible.
4. New rows aren't far below or above the historical baseline.
5. Incremental loads don't repeat a previous window.
6. Deletes, late-arriving records, and CDC updates reconcile against the source
   window.

Use hard thresholds for safety checks and historical baselines for anomaly
checks. Volume expectations can often be inferred from history, then overridden
when a consumer needs a stricter SLA
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
Fail hard for impossible cases such as zero rows in a required daily table. Send
review alerts for plausible but unusual spikes.

## Check Schema

Schema checks protect downstream SQL, dashboards, ML features, and activation
jobs from structural changes. A schema check should fail when required columns
are missing. It should also fail when data types change incompatibly, nested
fields disappear, or a source adds a breaking value structure.

Schema is one of the five observability pillars because a missed schema-change
notification can break downstream consumers
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
DataOps maturity also depends on automated schema management so incompatible
changes don't flow into production unnoticed
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps Principles and Scalable Data Platforms]].

Add schema checks for:

1. Required columns and nested fields.
2. Data types and precision.
3. Allowed nullable columns.
4. Enum-like fields such as `status`, `country`, or `plan`.
5. Backward-compatible changes for streams, CDC feeds, and shared tables.
6. Schema agreement changes that need consumer approval before publication.

For orchestration practice, keep schema checks close to the code that reads or
publishes the data. DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
shows one local setup. The check should usually live in a test layer such as SQL
or dbt. Python, Great Expectations, and Soda can serve the same role.

Keep the logic out of a large DAG file. For shared streams, connect the same
check to the schema-change rules in
[[How to Build Data Pipelines]].

## Check Distribution

Distribution checks ask whether values still look plausible. They catch null
spikes, impossible dates, negative amounts, and extreme values. They also catch
changed category mixes and shifted product or geography groups.

Distribution checks cover value ranges and unexpected field contents. They catch
values moving far outside the expected range and fields receiving the wrong kind
of content [[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Use distribution checks where bad values can silently change a metric:

1. Required dimensions aren't mostly null.
2. Numeric values stay within domain limits.
3. Dates are inside the processing window.
4. Category shares don't shift beyond a reviewed threshold.
5. ML features stay inside expected ranges before training or scoring.
6. Currency, unit, timezone, and status-code values still match the business
   definition.

Not every anomaly is bad data. Uncommon data may be intentional, but it still
needs context because it can affect a model, report, or customer workflow
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
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

Put this beside [[analytics engineering]]
and [[data pipelines]] because the
check protects meaning, not only mechanics. Keys, foreign keys, business
entities, and the question the pipeline must answer define the grain
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipelines]].

Successful jobs may still publish wrong rows, so verify merge keys before
publishing [[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].
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

Business-rule tests can check expected row counts, report values, and regression
impact. dbt tests, Great Expectations, and SQL checks can automate the same
assertions [[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].

In a dbt workflow, a test is still a query. Failing rows can create a warning or
an error. Source tests can stop dependent models from building on bad input
[[cite:analytics-engineer-skills-tools@38:53=>Analytics Engineer Skills and Tools]].

For production fraud pipelines, teams can use Great Expectations, cloud-native
checks, and custom tests. Teams use those checks to put quality gates inside the
pipeline rather than only after a job fails
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@43:28=>Fraud Prevention]].

For [[data pipelines]], one practical strategy is to get the pipeline running
first, then observe outputs and decide what's acceptable. Those accepted outputs
become checks, and sample data can run through the flow so the result can be
compared with expected snapshots. In that frame, [[Testing]] for pipelines leans
more on integration and snapshot tests than isolated unit tests
[[cite:production-ready-ai-engineering@11:47=>Production-Ready AI Engineering]].

Great Expectations and Soda can run after each pipeline step. SQL checks and
Spark tests can enforce column counts and null rules. Teams can use templated
test tables for joins and business-rule expectations
[[cite:production-ready-ai-engineering@13:14=>Production-Ready AI Engineering]].

Don't try to encode every edge case. Company data flows constantly, so pragmatic
edge-case checks matter more than an unrealistic attempt at perfect coverage.
Focus on cases that would make a leadership report, customer workflow, or model
output unsafe
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].

Write each business rule with an owner, a failure severity, and a default
action. Some rules should block publication. Others should open a ticket because
the business owner needs context before deciding.

## Check Lineage And Impact

With lineage checks, the team should be able to trace a bad output. The trace
should show the upstream source and downstream consumer. It should also show the
code or schema change.

Detecting a failure is only the first step, so teams need logs and correlations
to find the root cause. Upstream and downstream lineage shows the blast radius
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Add lineage checks for:

1. The run records source versions, input partitions, code version, and output
   partition.
2. The published dataset links to downstream dashboards, models, syncs, and
   owners.
3. The alert includes the failed check, affected asset, run id, and latest
   successful run.
4. The runbook names which downstream consumers to pause or warn.

[[DataOps Platforms]] treats
lineage, ownership, and runbooks as part of the operating layer, not separate
documentation. Use lineage to route incidents. Use it to choose a recovery
path. That path may be a rerun or backfill. It may also be rollback,
quarantine, or consumer communication.

## Put Checks In CI/CD

DataOps checks should run before production when the failure is predictable.
That means checking SQL models and Python code. Check DAG definitions, config
files, schema agreements, and infrastructure changes in
[[ci-cd=>CI/CD]].

Version control alone isn't enough because CI/CD needs realistic test data and
infrastructure as code. It also needs low-risk deployment paths, end-to-end
tests, and automated checks before production
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

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

GitOps extends the same release path to infrastructure and access changes.
Terraform and Terragrunt define changes. Atlantis dry runs, merge requests, and
review make data infrastructure changes reproducible and safer to apply
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].
That same review habit should cover pipeline dependencies and secrets.

To keep runs reproducible, pin dependencies. A containerized job can fail when a
Python dependency isn't fixed and the latest version changes its API
[[cite:dataops-and-gitops-best-practices-for-data-teams=>DataOps and GitOps for Data Teams]].
Dependency drift is a DataOps check because it can break a pipeline without any
business logic change.

## Connect Checks To Orchestration

[[Orchestration]] coordinates the
work and should expose check failures clearly. A data check that fails
should stop publication, page the right owner when the SLA requires it, and
record enough context for recovery.

A workflow engine tracks dependencies, schedules work, and retries after late
data or transient failures
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps Principles and Scalable Data Platforms]].
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

For a local Airflow setup, follow DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html).
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

Observability connects detection to diagnosis and impact analysis. Lineage shows
which downstream tables, reports, models, or customer workflows depend on the
broken asset
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].
That impact map should appear in the runbook, not only in an observability UI.

Manual runbooks should become automated playbooks where the action is repeated.
The manual runbook is still useful because it names the decision path.
Automation should then handle repeated actions such as retrying, pausing
publication, opening an incident, or running a backfill
[[cite:dataops-automation-and-reliable-data-pipelines=>DataOps Automation]].

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

Recovery should improve the next release. Production monitoring shows which
operating gaps matter because real failures expose the missing checks
[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]].

## Roll Checks Into The Pipeline

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
[[DataOps Platforms]],
[[Data Quality and Observability]],
and [[DataOps]]. Run checks before release,
observe data after release, and recover when the data isn't fit for use.
