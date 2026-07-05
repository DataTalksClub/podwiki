---
layout: wiki
title: "ETL"
summary: "Concept hub for extract-transform-load pipelines, ETL fit, staging, data quality, lineage, and modern platform work."
related:
  - ELT
  - Data Pipelines
  - Data Engineering Platforms
  - Data Quality and Observability
  - DataOps
  - Reverse ETL
---

ETL, or extract-transform-load, transforms source data before loading it into a
warehouse or mart. It starts with source-specific extraction, applies
organization-specific business logic or operational preparation, then finishes
with destination-specific loading routines
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
Matt Palmer's
[[book:20240415-understanding-etl=>Understanding ETL]]
expands on that same lifecycle across batch and event-driven pipelines, from
source extraction and staging to transformation logic, then loading.

ETL owns the flow, fit, operations, and role boundaries around the
transform-before-load concept. [[ELT]] covers load-first warehouse modeling, and
[[ETL vs ELT]] covers the decision between them. [[data pipelines]] covers the
broader ingestion-to-publication lifecycle, while [[modern data stack]] covers the
warehouse-centered tool ecosystem. ETL also sits close to [[data engineering platforms]].
ETL also connects to [[DataOps]]
and [[data quality and observability]]
because teams have to operate ETL jobs, not only define the acronym.

## Definition and Pipeline Flow

ETL starts with selected data from external systems. A marketing example pulls
customer and revenue context from a CRM. It combines that context with ad spend
to calculate customer acquisition cost before reporting
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].

The transformation isn't just format cleanup. It creates a business-specific
measure from sources that don't already share the same meaning.

After transformation, the pipeline writes a destination-ready result. A data
mart answers the customer-acquisition-cost question and feeds tools such as
Looker or Superset for business consumption
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
ETL narrows the payload before consumers see it. The destination receives a
prepared table or mart, not every raw field that arrived from every source.

Enterprise platforms can put an ETL layer between source systems and a
warehouse or lake. Reconciliation after the load compares source and target
counts. That catches records dropped by downtime, filtering, or
exception-handling problems
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].

## ETL Fit

ETL fits when the destination should receive data that has already been joined,
filtered, masked, or shaped for a specific consumer. Large enterprises may
combine many warehouses or sources in one staging layer. The staging layer can
then fan out curated outputs to multiple warehouses or lakes
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].

Not every pre-load action counts as business modeling. Ingestion-stage work can
be cleaning or quality assurance instead of complex transformation.
Deduplication, ordering guarantees, and PII masking fit this boundary
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].

Still, this work changes what appears in Snowflake or another human-facing
destination. Teams can drop duplicates, mask or hash hidden fields, and
preserve record order before the data reaches that destination
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
That's ETL-relevant because some teams need the target to be safe and
constrained before analysts, applications, or downstream systems touch the data.

Compliance and access-control pressure adds another dimension. GDPR-sensitive
datasets may need dynamic data masking, role-based access control, and data
classification
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].
Those controls can live in warehouse features, but the ETL decision still asks
what data a target can receive and expose.

## Operating ETL Reliably

ETL reliability starts with reproducibility. Immutable inputs and functional
transformations make runs easier to explain and repeat
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].
In a mutable ETL run, rows can change between a 6:00 run and a 12:00 run. The
same sequence of steps can then produce different results
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

For ETL teams, that pushes the design toward versioned code, traceable inputs,
and reruns that explain why a target table changed.

Reconciliation shows the same reliability concern. ETL can lose data through
downtime, filtering mistakes, or weak exception handling. Comparing source and
target after batch or real-time loads catches it
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].
ETL quality checks need to cover both the transform logic and the movement. A
correct business formula isn't enough if the pipeline silently drops records
before the warehouse or lake sees them.

Lineage also matters when teams share ETL outputs. Teams handling raw-data
changes may cache old data and recalculate when new inputs arrive
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].
The broader DataOps point: teams need to know which transformation produced a
dataset and whether a rerun should reproduce it
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

## Tool and Role Boundaries

ETL is a pipeline design rather than a scheduler or vendor label.
Orchestration and transformation split across tools. Airflow can run Airbyte
jobs, Airbyte handles extract-load work, and dbt can run SQL transformations
after data arrives
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].

An orchestrator may schedule the steps in an ETL design. The team
still has to decide which step owns extraction, which step owns business logic,
and which target receives the prepared result.

On the career side, Python and SQL are core data engineering skills. Docker and
Airflow matter too, as do warehouses and dbt. Candidates should understand ETL
and data warehouse fundamentals before chasing tool-specific depth
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]].

Hiring advice points in the same direction. Interviewers can test whether
someone understands ETL, warehouses, and lakes before accepting buzzword-heavy
project descriptions
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].

To distinguish ETL from [[reverse ETL]],
follow the direction of movement. Reverse ETL takes transformed warehouse data
and pushes it back into operational tools such as Salesforce. It's still reverse
ETL because the transformation happens before the data leaves the database. The
receiving system doesn't transform it
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
That keeps ETL centered on the position of transformation: before the receiving
system consumes the data.

## Boundary With ELT

Many analytics stacks moved toward [[ELT]], but ETL remains part of pipeline
design. Transform-before-load can be inflexible when business questions change.
Teams may need to re-extract source data if a new field or model becomes important
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
At platform scale, fixed ETL target models can also become tightly coupled as
use cases grow. Teams may then load data first and transform it later in the warehouse
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]].

[[ETL vs ELT]] covers the choice between the two designs. Keep the ETL boundary
narrower. Transform before load for curated, constrained, or compliant targets.

Ingestion can keep safety and quality work before storage.
Analysts and applications then use a constrained target
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
Enterprise staging can still fan out curated outputs to multiple targets
[[cite:data-engineering-tools-modern-data-stack=>Modern Data Stack]].
