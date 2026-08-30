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
summary: "Procedure for adding pipeline checks: data agreements, freshness, volume, schema, business rules, lineage, CI/CD, and recovery."
search_intent: "People searching for DataOps checks for data pipelines usually want concrete checks they can add to batch or streaming data workflows, plus guidance on how those checks fit CI/CD, observability, runbooks, and recovery."
related_wiki:
  - DataOps
  - Data Quality and Observability
  - Data Observability for Data Engineering
  - DataOps Platforms
  - Data Contracts
  - Data Pipelines
  - CI/CD
  - Orchestration
  - Analytics Engineering
  - dbt
---

Start after you know the pipeline's source, transformation path, and published
output. [[How to Build Data Pipelines]] covers that design work. Here, turn the
pipeline's assumptions into checks that run before release, during
orchestration, and after publication. A scheduler can finish successfully while
the data is stale, empty, shifted, or structurally wrong. The check must test
the data product rather than the job status alone.
[[cite:data-quality-data-observability-data-reliability@21:57=>Data Observability Explained]]

Keep the page distinct from the [[DataOps]] definition by treating every check
as a release gate with a response path. For each check, name where it runs and
what it blocks. Name who responds and how the owner recovers. That's the
practical layer between
[[data-quality-and-observability=>data quality and observability]],
[[ci-cd=>CI/CD]], [[Orchestration]], and [[DataOps Platforms]].
[[cite:dataops-automation-and-reliable-data-pipelines@33:47=>DataOps Automation]]

## Write The Check Record

Start with one published asset rather than the whole platform, then name the
dataset and consumer. Add the owner, freshness promise, required keys, and
unsafe output cases.
RACI-style ownership, SLAs, and runbooks make alerts actionable because they
separate the response roles. The record names who fixes the issue, who's
accountable, who's consulted, and who only needs to know that data may be
unreliable.
[[cite:data-quality-data-observability-data-reliability@29:00=>Data Observability Explained]]

Use a compact check record like this:

1. This pipeline publishes `orders_daily`.
2. The marketing dashboard and reverse ETL sync consume it.
3. The table must be ready by 07:00 local time.
4. `order_id` is unique at the published grain.
5. Required columns are `order_id`, `customer_id`, `order_ts`, `status`, and
   `net_revenue`.
6. A run is unsafe if it publishes zero rows, duplicated orders, negative net
   revenue, or a missing latest partition.
7. Unsafe output stays in quarantine until the owner approves a rerun, backfill,
   rollback, or consumer warning.

Store the condition and runtime location beside the pipeline code or metadata.
Add the responder and recovery command. Include the blocking behavior and
escalation path.

DataOps relies on version control, tests, and CI/CD, while monitoring and
runbooks complete the release-and-recovery path. Those details shouldn't live
in separate documents someone has to rediscover during an incident.
[[cite:dataops-for-data-engineering@42:39=>DataOps for Data Engineering]]

## Version The Data Agreement Before The Pipeline Grows

A check record protects one published asset; a data contract protects the
boundary between the producer and every consumer. For a shared stream, partner
feed, or widely used table, record the typed schema, current version, allowed
changes, delivery cadence, owner, and escalation contact. Validate the proposed
change against that agreement in CI and staging before a consumer sees it.
Teams that put schemas and change rules in a registry can add consumers by
reading the same guideline instead of reverse-engineering an evolving payload.
[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Data Platform Contracts]]

Treat the contract as a release input, not a static page. When a producer adds,
removes, or retypes a field:

1. classify the change as compatible, warning-level, or breaking;
2. run the schema and representative-data checks against the producer and
   affected consumers;
3. obtain consumer approval for a breaking change and publish the new contract
   version;
4. update lineage, owners, downstream assumptions, and the recovery runbook;
5. keep the previous version or a replayable input long enough to backfill or
   roll back safely.

This is especially important when an upstream team owns the feed. A working job
can still publish incorrect data after an unannounced source change, so logs,
documentation, and a runbook need to explain whether the repair belongs to the
source, pipeline, or platform owner. [[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@44:41=>Schema Changes and Job Failures]][[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@48:21=>Error Documentation and Runbooks]]

## Place Checks Where They Can Block Damage

Run predictable checks before production. Use [[Testing]], SQL tests, and
[[dbt]] tests where the checks sit close to models. Use Great Expectations,
Soda, Python tests, or Spark tests where they fit the pipeline. These checks
catch schema, join, null, and business-rule failures before deployment.
[[cite:dataops-automation-and-reliable-data-pipelines@48:25=>DataOps Automation]][[cite:production-ready-ai-engineering@13:14=>Production-Ready AI Engineering]]

Run runtime checks inside [[Orchestration]] when a failure should stop a
downstream task. A workflow engine tracks dependencies, schedules work, and
handles retries. Use it to stop publication or trigger a safe rerun. It can
also start a backfill when late data or transient failures appear.
[[cite:dataops-principles-and-scalable-data-platforms@30:34=>DataOps Principles and Scalable Data Platforms]]

Run observability checks after publication when the failure depends on live
behavior. Freshness and volume cover arrival or completeness. Distribution,
schema, and lineage cover data downtime cases that ordinary task status checks
miss.
[[cite:data-quality-data-observability-data-reliability@16:38=>Data Observability Explained]]
For an engineering-focused rollout, use
[[data-observability-for-data-engineering=>data observability for data engineering]]
to connect those signals to owners, SLAs, and runbooks.

## Check Freshness And Volume First

Freshness asks whether the latest usable data arrived when consumers expected
it. Volume asks whether the amount of data is plausible. These checks catch
missing files, delayed API windows, partial extracts, and duplicated loads.
They also catch broken filters and empty outputs. Airflow or another scheduler
can report success even when zero useful rows reach the target.
[[cite:dataops-and-gitops-best-practices-for-data-teams@62:28=>DataOps and GitOps for Data Teams]]

Run freshness checks in three places:

1. Source arrival: the file, API page, CDC batch, or event partition arrived.
2. Published output: the table, feature set, mart, or serving asset has a
   current `max(event_ts)`, `max(loaded_at)`, or partition.
3. Consumer read path: the dashboard, activation job, or model feature lookup
   can see the new partition after publication.

Run volume checks beside the load or transform that can lose rows:

1. Output row count is greater than zero.
2. Row count stays within an expected range.
3. Input-to-output ratios stay plausible.
4. Incremental windows don't repeat or skip a previous window.
5. Deletes, late records, and CDC updates reconcile against the source window.

Block publication when a required daily table is empty or a current partition is
missing. Block it when a promised five-minute table misses its SLA. Send a
review alert when the data is unusual but still plausible. Observability
thresholds need business context to avoid false positives.
[[cite:data-quality-data-observability-data-reliability@35:24=>Data Observability Explained]][[cite:data-quality-data-observability-data-reliability@60:27=>Data Observability Explained]]

The data owner responds first. Source owners and platform owners join when the
runbook names their systems. Consumers join when the SLA will be missed.

## Check Schema Before Consumers Read It

Schema checks fail when required columns disappear or data types change
incompatibly. They also fail when nested fields move, nullable rules change, or
a source adds a breaking value structure. Barr Moses names schema as one of the five
observability pillars because missed schema-change notifications can break
downstream consumers.
[[cite:data-quality-data-observability-data-reliability@19:10=>Data Observability Explained]]

Run schema checks in CI for declared agreements and in staging before
promotion. Run them again in the production pipeline before publishing a shared
table. Include required columns, types, precision, and nullability. Add
enum-like fields and compatibility rules for streams, CDC feeds, and shared
marts. Lars Albertsson ties DataOps maturity to tested, automated quality and
schema practices rather than manual inspection.
[[cite:dataops-principles-and-scalable-data-platforms@46:52=>DataOps Principles and Scalable Data Platforms]]

Block when a breaking schema change would reach a dashboard, model feature,
activation job, or shared table without consumer approval. Route source changes
to the producer. Route transformation changes to the pipeline owner. Route
metadata or permissions failures to the platform owner.

Keep the check logic in SQL, [[dbt]], Python, or a schema registry. Great
Expectations and Soda can run the same kind of check. Keep the [[Orchestration]]
task small enough to show pass and fail states. It should also show quarantine
and rollback state.

External APIs and partner feeds need the same contract, even when the source is
outside the company. [[person:angelaramirez=>Angela Ramirez]] describes checking
who owns the feed, how often it arrives, whether its documentation is current,
and whether a field can silently change from a number to a string. Record the
delivery cadence, schema, compatibility promise, and escalation contact before
the first downstream job depends on it. A contract is useful only when a schema
or freshness check can enforce it.
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@56:19=>External Data Integration]][[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@59:03=>Data Contract Stability]]

## Check Distribution And Business Rules

Distribution checks catch values that are structurally valid but unsafe for the
decision that consumes them. Common failures include null spikes, impossible
dates, negative amounts, and new categories. They also include shifted product
mixes and feature values outside expected ranges. Distribution is another
observability pillar because a pipeline can run while the produced values no
longer match consumer expectations.
[[cite:data-quality-data-observability-data-reliability@16:38=>Data Observability Explained]]

Run distribution checks after transformations that change meaning and before
serving layers that make the data operational. Block impossible values, such as
negative revenue for paid orders or future timestamps in a closed period. Send
review alerts for rare but possible values. Unusual data can be valid and may
need business context before anyone changes the pipeline.
[[cite:data-quality-data-observability-data-reliability@60:27=>Data Observability Explained]]

Business-rule checks encode the consumer's known truths. A campaign audience
must exclude opted-out users, and a feature table must include the source event
needed for scoring. A financial report must wait until the period is closed.
[[dbt]] tests can turn those rules into warning or failure queries.
Source tests can stop dependent models from building on bad input.
[[cite:analytics-engineer-skills-tools@38:53=>Analytics Engineer Skills and Tools]]

For a new [[data pipelines=>data pipeline]], first run the flow with realistic
sample data. Then observe acceptable outputs and turn those examples into
snapshot or integration checks. Bartosz Mikulski frames pipeline testing this
way: expected outputs from representative data often matter more than isolated
unit tests.
[[cite:production-ready-ai-engineering@11:47=>Production-Ready AI Engineering]]
The pipeline owner responds to failed mechanics. The business owner responds
when the data could be valid but the decision rule needs context.

## Check Grain, Joins, And Reconciliation

Grain checks protect what one row means. They catch duplicate primary keys,
accidental many-to-many joins, and repeated incremental loads. They also catch
overlapping effective-date ranges and merge keys that no longer identify one
entity. Santona Tuli connects pipeline design to entities, foreign keys,
business mappings, and marts. Dashboards and business questions guide the same
design work.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@39:23=>Modern Data Pipelines]]

State the grain in consumer language, then test it:

1. One row per `order_id`.
2. One row per `customer_id` per day.
3. One row per account per subscription period.
4. One latest feature row per entity.
5. No duplicated merge key in staging before upsert.
6. No overlapping effective-date windows in slowly changing records.

Run these checks before upsert, after joins, and before publishing marts or
feature tables. Block when duplicate keys, row explosion, or source-target
reconciliation failures would make the published asset unsafe. Source-target
comparison catches downtime, leakage, filters, and exception-handling gaps after
batch or real-time loads.
[[cite:data-engineering-leadership-and-modern-data-platforms@28:09=>Data Engineering Leadership and Modern Data Platforms]]
The responder is usually the pipeline owner, with the source owner pulled in
when the source emits duplicate, missing, or late records.

## Add Lineage To Every Alert

Lineage checks make a failed check diagnosable. The alert should name the
failed condition, upstream source, input partition, and code version. It should
also name the output asset, downstream dashboards or models, and owner. Include
the run id and latest successful run.
Observability separates detection from diagnosis, and lineage helps teams find
root cause and downstream blast radius.
[[cite:data-quality-data-observability-data-reliability@26:04=>Data Observability Explained]][[cite:data-quality-data-observability-data-reliability@58:51=>Data Observability Explained]]

Run lineage capture as part of the production task group and store it with
check results. Block publication when the team can't identify which input
created a regulated, financial, ML, or customer-facing output. Route the
failure to the platform owner when lineage collection broke, and to the
pipeline owner when lineage shows a specific upstream change. [[DataOps
Platforms]] should make this metadata visible to responders instead of leaving
it in a separate document.

## Put Predictable Failures In CI/CD

[[ci-cd=>CI/CD]] should catch failures that are knowable before production,
including broken SQL and incompatible schema changes. It should also catch
invalid DAG definitions, missing owners, and missing retries. Bad secrets
references, unpinned dependencies, and sample-data regressions belong here too.

Christopher Bergh ties DataOps to version control, tests, and CI/CD. He also
includes realistic test data, monitoring, and deployment automation.
[[cite:dataops-for-data-engineering@30:55=>DataOps for Data Engineering]]

Add these gates to pull requests and promotion jobs:

1. Unit tests for parsing and transformation helpers.
2. SQL or dbt tests for constraints and business rules.
3. Schema compatibility tests for source and output agreements.
4. Sample-data regression tests for joins, grain, and expected snapshots.
5. DAG validation for dependencies, owners, schedules, retries, and alerts.
6. Infrastructure checks for permissions, secrets, and environment config.
7. Dependency checks for Python packages, container images, and dbt packages.
8. Staging-to-production checks against the current data agreement.

Tomasz Hinc also calls out fixed versions and Docker because dependency drift
can break a containerized job without a business-logic change.
[[cite:dataops-and-gitops-best-practices-for-data-teams@61:27=>Dependency drift]]

## Connect Production Checks To Orchestration

Production checks should be visible in the orchestrator as tasks or task groups.
A successful run should mean the data agreement passed, not only that Python,
SQL, or Spark exited cleanly. Workflow engines belong here because they expose
dependencies, retries, schedules, and rerun state.
[[cite:dataops-principles-and-scalable-data-platforms@10:48=>DataOps Principles and Scalable Data Platforms]]

Use this production sequence:

1. Validate source arrival.
2. Load or transform data.
3. Run freshness, volume, schema, distribution, grain, and business-rule checks.
4. Record lineage, check results, and the output version.
5. Publish only after blocking checks pass.
6. Quarantine output or stop downstream tasks when a blocking check fails.
7. Notify the owner and consumers named in the check record.
8. Trigger retry, rollback, or backfill only when the runbook allows it.

Keep validation logic in the tool that fits the check, but make the orchestrator
show the state clearly. The responder can then see whether the pipeline is
waiting on late data, blocked by quality, quarantined for review, or ready for
a safe backfill. The
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
shows a small Docker Compose setup.

## Build Recovery Into The Check

A check is incomplete until the owner knows what to do after it fails. Barr
Moses connects observability maturity to operational runbooks and remediation
workflows. Christopher Bergh describes the move from manual runbooks to
automated playbooks.
[[cite:data-quality-data-observability-data-reliability@41:03=>Data Observability Explained]][[cite:dataops-automation-and-reliable-data-pipelines@34:37=>DataOps Automation]]

Attach these recovery details to every critical check:

1. Owner and escalation channel.
2. SLA, priority, and consumer impact.
3. Downstream dashboards, models, reverse ETL syncs, and customer workflows.
4. Safe rerun command.
5. Backfill command and allowed date range.
6. Quarantine or rollback step.
7. Consumer notification text or channel.
8. The missing test, alert, or CI/CD gate to add after the incident.

Keep a replayable source or staging boundary when the pipeline can wait for late
data or suffer a catastrophic downstream failure. A staging area can hold the
raw input while a service recovers; ingestion-time deduplication, ordering, and
PII masking can make that replay safer before data reaches human-facing models.
[[cite:modern-data-pipelines-orchestration-ingestion-modeling@32:57=>Staging for Recovery]][[cite:modern-data-pipelines-orchestration-ingestion-modeling@37:10=>Ingestion Quality and PII Controls]]

Use severity to choose the response. A stale exploratory table can open a
ticket, while a missing partition in a finance report can block publication. A
bad feature table can quarantine scoring inputs and page the owner. A broken
lineage record can block regulated or customer-facing outputs until someone
checks impact manually.

Monitoring production also shows which operating gaps matter. Feed incident
learnings back into CI/CD checks, orchestration tasks, and runbooks.
[[cite:dataops-for-data-engineering@50:29=>DataOps for Data Engineering]]

[[person:christopherbergh=>Christopher Bergh]] frames the same procedure as
three operating days: day one builds for the customer, day two runs with new
data, and day three changes the system as customer needs evolve. Checks,
monitoring, and safe deployment therefore belong in the first release plan,
not in a later reliability project. A team can start with basic environments,
tests, and logs, then add stronger approvals, registries, and support controls
as its risk and scale grow.
[[cite:dataops-for-data-engineering@23:56=>Day Two and Day Three Operations]][[cite:dataops-for-data-engineering@30:55=>CI/CD and Test Data]]

## Apply The Procedure

Apply this sequence to a new or existing pipeline:

1. Name the asset, consumer, owner, SLA, grain, and unsafe output cases.
2. Decide which checks run in CI/CD, staging, orchestration, and observability.
3. Add freshness checks for source arrival, published output, and consumer read
   paths.
4. Add volume and reconciliation checks for zero rows, row-count ranges,
   incremental windows, and source-target comparison.
5. Add schema checks for columns, types, nullability, enum-like fields, and
   compatibility rules.
6. Add distribution and business-rule checks for values that can make a report,
   model, or workflow unsafe.
7. Add grain and join checks before upsert, after joins, and before publication.
8. Add lineage to every alert so responders can see upstream inputs, code
   version, output version, downstream consumers, and owner.
9. Make predictable failures block pull requests or promotion jobs in CI/CD.
10. Make runtime failures stop publication, quarantine output, or trigger a
    recovery path that the runbook approves.
11. Update the runbook after incidents so the next release includes the missing
    check.

For a contract change, apply the same sequence to the new version: test the
producer and representative consumers, replay a safe staging window, publish
only after compatibility and ownership are clear, and retain a rollback or
backfill path. This keeps schema governance connected to the quality and
recovery checks instead of treating them as separate projects.
[[cite:dataops-principles-and-scalable-data-platforms@46:52=>Test-Certified Data Quality]][[cite:dataops-for-data-engineering@30:55=>CI/CD and Representative Test Data]]

After this sequence, the pipeline checks known assumptions before release,
observes the published data after release, and gives responders a recovery
path. They can use it when the data isn't fit for use.
[[cite:dataops-automation-and-reliable-data-pipelines@33:47=>DataOps Automation]][[cite:dataops-for-data-engineering@42:39=>DataOps for Data Engineering]]

## Related Pages

These related pages connect the check workflow to the rest of the wiki.

- [[DataOps]] defines the operating discipline around these checks.
- [[data-quality-and-observability=>Data quality and observability]] explains
  freshness and volume alongside schema, distribution, lineage, and alert
  design.
- [[data-observability-for-data-engineering=>Data observability for data engineering]]
  covers the engineering rollout for ownership, SLAs, and runbooks.
- [[ci-cd=>CI/CD]], [[Orchestration]], and [[Testing]] cover where checks run.
- [[DataOps Platforms]] and [[DataOps Tools]] cover the shared tooling layer.
