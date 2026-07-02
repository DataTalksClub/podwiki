---
layout: wiki
title: "ETL"
summary: "Podcast-grounded guide to extract-transform-load pipelines, ETL fit, staging, data quality, lineage, and modern platform work."
related:
  - ELT
  - Data Pipelines
  - Data Engineering Platforms
  - Data Quality and Observability
  - DataOps
  - Reverse ETL
---

ETL means extract-transform-load. Teams use ETL when they pull data from source
systems and apply business logic or operational preparation before the
destination receives it, then load the curated result into a warehouse or mart.
ETL breaks into source-specific extraction, organization-specific business
logic, and destination-specific loading routines
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
Matt Palmer's
[[book:20240415-understanding-etl|Understanding ETL]]
expands on that same extract-transform-load lifecycle: source extraction,
staging, transformation logic, and loading patterns across batch and
event-driven pipelines.

This topic covers the transform-before-load side of the pipeline. Use
[[ELT]] for load-first warehouse modeling and
[[ETL vs ELT]] for the reference
comparison. Use the shorter
[[etl-vs-elt|ETL vs ELT decision guide]]
when the choice is the question. ETL
also sits close to [[data pipelines]]
and [[data engineering platforms]].
Guests in these episodes connect ETL to [[DataOps]]
and [[data quality and observability]]
because teams have to operate ETL jobs, not only define the acronym.

## Definition and Pipeline Flow

ETL starts with selected data from external systems. A marketing example pulls
customer and revenue context from a CRM, then combines that context with ad
spend from Google AdWords or Facebook to calculate customer acquisition cost
before the result reaches a reporting layer
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

The transformation isn't just format cleanup. It creates a business-specific
measure from sources that don't already share the same meaning.

After transformation, the pipeline writes a destination-ready result. A data
mart answers the customer-acquisition-cost question and feeds tools such as
Looker or Superset for business consumption
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
ETL narrows the payload before consumers see it. The destination receives a
prepared table or mart, not every raw field that arrived from every source.

An enterprise platform view shows the same flow: data pulled from source systems
into a warehouse or lake, with an ETL layer between source and target. After the
load, reconciling source and target counts helped find records dropped by
downtime, filtering, or exception-handling problems
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).

## ETL Fit

ETL fits when the destination should receive data that has already been joined,
filtered, masked, or shaped for a specific consumer. ETL remains useful in large
enterprises where teams combine many warehouses or sources and then propagate
prepared data to multiple warehouses or lakes — an intermediary staging need
where many inputs enter one place and curated outputs fan out again
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

A boundary keeps every pre-load action from counting as business modeling:
ingestion-stage work is cleaning or quality assurance, not complex
transformation, with examples such as deduplication, ordering guarantees, and
PII masking
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).

Still, this work changes what appears in Snowflake or another human-facing
destination. Teams can drop duplicates, mask or hash hidden fields, and
preserve record order before the data reaches that destination
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]).
That's ETL-relevant because some teams need the target to be safe and
constrained before analysts, applications, or downstream systems touch the data.

Compliance and access-control pressure adds another dimension: dynamic data
masking, role-based access control, and data classification for GDPR-sensitive
datasets
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).
Those controls can live in warehouse features, but the ETL decision still asks
what data a target can receive and expose.

## Operating ETL Reliably

The strongest reliability warning is reproducibility.
[[person:larsalbertsson|Lars Albertsson]] argues for
immutable inputs and functional transformations
[[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]].
In a mutable ETL run, rows can change between a 6:00 run and a 12:00 run, so the
same sequence of steps can produce different results
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

For ETL teams, that pushes the design toward versioned code, traceable inputs,
and reruns that explain why a target table changed.

A reconciliation workflow shows the same reliability concern. ETL can lose data
through downtime, filtering mistakes, or weak exception handling, so comparing
source and target after batch or real-time loads catches it
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).
ETL quality checks need to cover both the transform logic and the movement. A
correct business formula isn't enough if the pipeline silently drops records
before the warehouse or lake sees them.

When teams share ETL outputs, they also need lineage. Maintaining lineage while
handling raw-data changes means caching old data and recalculating when new
inputs arrive
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).
The broader DataOps point: teams need to know which transformation produced a
dataset and whether a rerun should reproduce it
([[podcast:dataops-principles-and-scalable-data-platforms|DataOps 101 for Scaling Data Platforms]]).

## Tool and Role Boundaries

ETL is a pipeline design rather than a scheduler or vendor label. Orchestration
and transformation split across tools: Airflow can run Airbyte jobs, Airbyte
handles extract-load work, and dbt can run SQL transformations after data
arrives
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

An orchestrator may schedule the steps in an ETL design. The team
still has to decide which step owns extraction, which step owns business logic,
and which target receives the prepared result.

On the career side, Python and SQL are core data engineering skills, alongside
Docker, Airflow, warehouses, and dbt; candidates should understand ETL and data
warehouse fundamentals before chasing tool-specific depth
([[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]]).

Hiring advice points in the same direction: interviewers can test whether
someone understands basic terms such as ETL, warehouses, and lakes before
accepting buzzword-heavy project descriptions
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).

To distinguish ETL from [[reverse ETL]],
follow the direction of movement. Reverse ETL takes transformed warehouse data
and pushes it back into operational tools such as Salesforce. It's still reverse
ETL because the transformation happens before the data leaves the database; the
receiving system doesn't transform it
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).
That keeps ETL centered on the position of transformation: before the receiving
system consumes the data.

## Relationship to ELT

ETL isn't obsolete, but many analytics stacks moved toward ELT.
Transform-before-load can be inflexible when business questions change, since
teams may need to re-extract source data if a new field or model becomes
important
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

The same scaling pressure appears at platform scale: a fixed ETL target model
became tightly coupled as use cases grew, prompting a move toward loading data
first and transforming it later in the warehouse
([[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership]]).

That doesn't remove ETL from the design vocabulary. Ingestion keeps some safety
and quality work before human-facing storage
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture]]),
and enterprise staging and fan-out remain valid ETL cases
([[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]]).

Across these episodes, the transform goes where it reduces the actual risk. It
goes before load when the target must be curated, constrained, or compliant. It
goes after load when preserving raw source detail makes future modeling safer.
