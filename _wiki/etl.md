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

DataTalks.Club guests use ETL to mean extract-transform-load. Teams use ETL
when they pull data from source systems and apply business logic or
operational preparation before the destination receives it. They then load the
curated result into a warehouse or mart.
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the clearest
podcast definition in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}):
at 3:46-4:30, she breaks ETL into source-specific extraction. She then adds
organization-specific business logic and destination-specific loading routines.
Matt Palmer's
[Understanding ETL]({{ '/books/20240415-understanding-etl/' | relative_url }})
expands on that same extract-transform-load lifecycle: source extraction,
staging, transformation logic, and loading patterns across batch and
event-driven pipelines.

This topic covers the transform-before-load side of the pipeline. Use
[ELT]({{ '/wiki/elt/' | relative_url }}) for load-first warehouse modeling and
[ETL vs ELT]({{ '/comparisons/etl-vs-elt/' | relative_url }}) for the reference
comparison. Use the shorter
[ETL vs ELT decision guide]({{ '/comparisons/etl-vs-elt/' | relative_url }})
when the choice is the question. ETL
also sits close to [data pipelines]({{ '/wiki/data-pipelines/' | relative_url }})
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Guests in these episodes connect ETL to [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
because teams have to operate ETL jobs, not only define the acronym.

## Definition and Pipeline Flow

Kwong's ETL definition starts with selected data from external systems. Her
marketing example pulls customer and revenue context from a CRM. The pipeline
then combines that context with ad spend from Google AdWords or Facebook. This
calculates customer acquisition cost before the result reaches a reporting layer
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
5:32-7:18).

The transformation isn't just format cleanup. It creates a business-specific
measure from sources that don't already share the same meaning.

After transformation, the pipeline writes a destination-ready result. Kwong
describes a data mart that answers the customer-acquisition-cost question. That
mart feeds tools such as Looker or Superset for business consumption
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:18-7:57). ETL narrows the payload before consumers see it. The destination
receives a prepared table or mart, not every raw field that arrived from every
source.

[Rahul Jain]({{ '/people/16rahuljain/' | relative_url }}) describes the same
flow from an enterprise platform view in
[Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}).
His team pulled data from source systems into a warehouse or lake, with an ETL
layer between the source and target. After the load, they reconciled source and
target counts. That check helped them find records dropped by downtime,
filtering, or exception-handling problems
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
28:04-28:46).

## ETL Fit

ETL fits when the destination should receive data that has already been joined,
filtered, masked, or shaped for a specific consumer. Kwong says ETL remains
useful in large enterprises where teams combine many warehouses or sources and
then propagate prepared data to multiple warehouses or lakes. She frames that
as an intermediary staging need. Many inputs enter one place, and curated
outputs fan out again
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
41:30-43:04).

[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) adds a boundary that
keeps this page from treating every pre-load action as business modeling. In
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
she treats ingestion-stage work as cleaning or quality assurance, not complex
transformation. Her examples include deduplication, ordering guarantees, and
PII masking.

Still, this work changes what appears in Snowflake or another human-facing
destination. Teams can drop duplicates, mask or hash hidden fields, and
preserve record order before the data reaches that destination
([Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}),
37:10-39:02). That's ETL-relevant because some teams need the target to be
safe and constrained before analysts, applications, or downstream systems touch
the data.

Jain's platform example adds compliance and access-control pressure. His team
used dynamic data masking, role-based access control, and data classification
for GDPR-sensitive datasets
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
29:01-30:45). Those controls can live in warehouse features, but the ETL
decision still asks what data a target can receive and expose.

## Operating ETL Reliably

Albertsson gives the strongest ETL warning in these episodes: reproducibility.
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) argues for
immutable inputs and functional transformations in
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
His problem case is a mutable ETL run. Rows can change between a 6:00 run and
a 12:00 run. The same sequence of steps can then produce different results
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
20:12-21:29).

For ETL teams, that pushes the design toward versioned code, traceable inputs,
and reruns that explain why a target table changed.

Jain's reconciliation workflow shows the same reliability concern. ETL can lose
data through downtime, filtering mistakes, or weak exception handling. His team
therefore compared source and target after batch or real-time loads
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
28:04-28:46). ETL quality checks therefore need to cover both the transform
logic and the movement. A correct business formula isn't enough if the
pipeline silently drops records before the warehouse or lake sees them.

When teams share ETL outputs, they also need lineage. Jain says his team
maintained lineage while handling raw-data changes. The team cached old data
and recalculated data when new inputs arrived
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
33:06-33:15). Albertsson makes the broader DataOps point. Teams need to know
which transformation produced a dataset and whether a rerun should reproduce it
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
1:04:18).

## Tool and Role Boundaries

ETL is a pipeline design rather than a scheduler or vendor label. Kwong
separates orchestration from transformation by assigning different work to each
tool. Airflow can run Airbyte jobs. Airbyte handles extract-load work, while
dbt can run SQL transformations after data arrives
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
30:59-33:45).

An orchestrator may schedule the steps in an ETL design. The team
still has to decide which step owns extraction, which step owns business logic,
and which target receives the prepared result.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) explains the career side
in
[Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}).
He names Python and SQL as core data engineering skills. He adds Docker,
Airflow, warehouses, and dbt. He later advises candidates to understand ETL and
data warehouse fundamentals before chasing tool-specific depth
([Data Engineering Job Prep and Interview Guide]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}),
1:20-2:22 and 54:34-57:29).

Jain's hiring advice points in the same direction.
Interviewers can test whether someone understands basic terms such as ETL,
warehouses, and lakes before accepting buzzword-heavy project descriptions
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
49:35-54:34).

To distinguish ETL from [reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}),
follow the direction of movement. Kwong describes reverse ETL as taking
transformed warehouse data and pushing it back into operational tools such as
Salesforce. She still calls it reverse ETL because the transformation happens
before the data leaves the database. The receiving system doesn't transform it
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
35:42-39:06). That keeps ETL centered on the position of transformation: before
the receiving system consumes the data.

## Relationship to ELT

Guests in these episodes don't present ETL as obsolete. They still explain why
many analytics stacks moved toward ELT. Kwong argues that transform-before-load
can be inflexible when business questions change. Teams may need to re-extract
source data if a new field or model becomes important
([ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}),
7:57-12:39).

Jain reports the same scaling pressure from his own platform. A fixed ETL target
model became tightly coupled as use cases grew. His team moved toward loading
data first and transforming it later in the warehouse
([Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}),
30:50-32:29).

That doesn't remove ETL from the design vocabulary. Tuli's ingestion discussion
keeps some safety and quality work before human-facing storage. Kwong keeps
enterprise staging and fan-out as valid ETL cases.

Across these episodes, guests place the transform where it reduces the actual
risk. They place it before load when the target must be curated, constrained,
or compliant. They place it after load when preserving raw source detail makes
future modeling safer.
