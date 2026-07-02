---
layout: article
tags: ["how-to"]
title: "How to Build Data Pipelines That People Can Trust"
keyword: "build data pipelines"
summary: "A guide to building data pipelines with ingestion, transformation, orchestration, contracts, testing, observability, and last-mile activation."
search_intent: "Help readers who search for how to build data pipelines understand the practical build sequence, tradeoffs, and reliability practices using DataTalks.Club podcast evidence."
related_wiki:
  - Data Engineering Platforms
  - Data Pipelines
  - DataOps
  - Data Quality and Observability
  - Data Activation
---

To build data pipelines that people trust, start with the decision, model, or
workflow the pipeline must support. Then work backward into source ownership and
event definitions. Add ingestion and storage. Then add transformation and
orchestration. Finish with quality checks, observability, and last-mile
delivery.

In the modern pipeline episode,
[[person:santonatuli|Santona Tuli]] describes pipeline
design as a sequence. Data starts with raw arrival, then moves to cleaned
ingestion and modeled business entities. The pipeline finally produces answers
for dashboards or ML systems
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Modern Data Pipeline Architecture on raw-to-answer layers at 37:10-46:01]]).

In the modern stack episode,
[[person:nataliekwong|Natalie Kwong]] makes the same
point through ELT. Teams keep raw data separate from business-facing marts so
they don't invent inconsistent transformations downstream
([[podcast:data-engineering-tools-modern-data-stack|ELT raw-to-marts split at 17:55-19:26]]).
For related background, see
[[Data Engineering Platforms]]
and [[Data Pipelines]].

## Start With The Consumer

A pipeline should answer a real question or power a real workflow. Santona's
pipeline discussion is explicit about this. After data arrives, engineers still
need to identify mapping keys, foreign keys, and business entities. They also
need to name the question the business wants answered. She argues that data and
analytics engineers should talk to end users before deciding which tables and
transformations matter
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|pipeline keys and entities at 39:23-43:05]]).

For product and growth data, that consumer-first work begins even earlier.
[[person:arpitchoudhury|Arpit Choudhury]] recommends a
[[tracking-plans|tracking plan]] before
instrumentation. Teams define events and properties. They also define data types
and ownership. Then product and growth teams know what an event means before it
reaches analytics or activation tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|tracking plan ownership at 13:34-23:27]]).

If teams use vague event names in
[[product analytics]], they
create operational risk. Teams create more risk when they use the same events
for funnels, experiments, or reverse ETL.

Start with this brief before you pick tools:

1. Who uses the output?
2. What decision, model, dashboard, or operational action depends on it?
3. Which source system owns the data?
4. What freshness and quality expectations does the consumer need?
5. What if data is late or missing? What if it's duplicated or structurally changed?

## Design The Ingestion Layer

Ingestion isn't the same as final modeling. Natalie separates the ingestion
layer from data marts because raw data isn't ready for most business users.
If every analyst transforms raw tables differently, the organization gets
conflicting answers. ELT keeps the raw form available while moving shared
business logic into a controlled transformation layer
([[podcast:data-engineering-tools-modern-data-stack|ELT ingestion-to-marts split at 17:55-19:26]]).

Santona adds that ingestion can still perform limited quality work. In her
Upsolver discussion, the early stage handles deduplication and ordering
guarantees. It can also mask or hash PII before the data appears in Snowflake
or another human-facing destination
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|ingestion guardrails at 37:10-39:22]]).
Treat those steps as guardrails, not as the place where every business metric
is defined.

Pick storage from the data structure and each team's needs. Natalie describes
warehouses as a strong fit for structured analytics teams. Lakes help when
engineering or data science teams need unstructured files or logs. They also
help with video and other raw formats.

She warns that lakes and warehouses can become swamps. That happens when teams
store unused or poorly governed data that people can't trust
([[podcast:data-engineering-tools-modern-data-stack|warehouses and data swamps at 19:50-28:07]]).
For that comparison, use
[[Data Warehouse vs Data Lakehouse]].

## Model Data Into Useful Outputs

After ingestion, model data around entities, relationships, and business
questions. Santona describes this as finding the keys and relationships across
multiple sources. Teams then build the modeled layer that can answer real
business questions. She separates ingested data and modeled data from answers.
Marts or dashboard-specific transformations sit after the core business entities
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|modeled data layers at 39:23-43:05]]).

This is where
[[analytics engineering]]
and [[data engineering]] overlap.
Natalie connects ELT to analysts using dbt and SQL inside the warehouse. She
then describes data marts as the business-facing layer. Those marts should be
easier to use than raw ingestion tables
([[podcast:data-engineering-tools-modern-data-stack|dbt and marts at 7:57-18:47]]).

The practical output isn't "a pipeline" in the abstract. It may be a modeled
table or mart, or it may be a feature set, dashboard input, or activation
segment that a consumer understands.

For ML pipelines, Santona says the modeling mindset shifts for machine outputs.
You still deduplicate and handle nulls, and you still transform features for
model training rather than a human-readable business entity
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|ML pipeline outputs at 44:57-46:01]]).
That boundary is why pipeline work often touches
[[MLOps vs DataOps]].

## Orchestrate The Work, Not The Buzzwords

Orchestration coordinates jobs after each pipeline step is clear. Natalie
describes Airflow as an orchestrator that schedules work and runs ingestion
jobs. Tools such as Airbyte focus on the extract-load part, while dbt handles
warehouse transformations
([[podcast:data-engineering-tools-modern-data-stack|Airflow Airbyte and dbt roles at 30:59-33:45]]).

For a local learning or portfolio setup, follow DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
to run the scheduler, UI, and metadata database. It also keeps the DAG folder
and logs in one reviewable environment.

Make dependencies visible and repeatable, and don't rename
the whole pipeline after the scheduler.

At team scale, teams need orchestration conventions. In the scale-up episode,
[[person:mehdiouazza|Mehdi OUAZZA]] says a platform is
more than an Airflow cluster. Teams need naming conventions and sequence
practices. They also need playbooks, support channels, and onboarding. With
those habits, other data users can build without turning the platform team into
a bottleneck
([[podcast:scaling-data-engineering-teams-self-service-platforms|self-service platform conventions at 12:30-17:56]]).

See
[[self-service-data-platforms|Self-Service Data Platforms]]
for that operating model.

Streaming adds stricter schema agreements. Mehdi warns that teams can grow from
a few Kafka topics to hundreds quickly. His recommendation is to define typed
schemas and schema registry usage. Teams should also define allowed changes and
a schema-change process before downstream teams depend on the stream
([[podcast:scaling-data-engineering-teams-self-service-platforms|Kafka schema-change rules at 23:26-26:52]]).
[[Batch vs Streaming]]
covers the latency decision.

## Add Tests, Observability, And Recovery

A pipeline can finish successfully and still deliver bad data. That's the core
warning in [[person:barrmoses|Barr Moses]]'s data
observability episode. She names freshness and volume first. She then adds
distribution, schema, and lineage.

Teams use those signals to see whether data is up to date and complete. They
also use them to check whether values look plausible and schemas stay stable.
Lineage connects the right upstream and downstream assets
([[podcast:data-quality-data-observability-data-reliability|observability signals at 16:38-19:10]]).

Freshness expectations should become explicit SLAs when downstream work depends
on them. Barr uses the example of a dataset that must arrive within five
minutes after a user action. The SLA helps the data team prioritize which
freshness incidents matter first, instead of treating every late table as equal
([[podcast:data-quality-data-observability-data-reliability|freshness SLAs at 35:24-40:43]]).
Link those expectations to
[[Data Quality and Observability]]
and [[data-quality-and-observability|Data Observability]].

[[person:christopherbergh|Christopher Bergh]] turns the
same reliability problem into [[DataOps]].
Teams use automation and tests to reduce errors, while monitoring and
observability show what broke. They add version control and CI/CD so
deployments are safer.

In the DataOps for data engineering episode, he argues that teams need realistic
test data and infrastructure as code. End-to-end checks should run before
changes reach production
([[podcast:dataops-for-data-engineering|DataOps tests at 15:52-16:10 and 30:55-43:02]]).

His earlier DataOps episode adds runbooks and automated playbooks. It also
covers end-to-end versioning for code and models, plus visualizations and
governance
([[podcast:dataops-automation-and-reliable-data-pipelines|runbooks and versioning at 33:47-51:21]]).

## Deliver Data Where People Act

A table may not be enough when the business action happens outside the
warehouse. Arpit says a data-led growth stack starts with collection and
storage. Teams then analyze and activate the data
([[podcast:data-led-growth-event-tracking-and-reverse-etl|collection-to-activation flow at 22:50-30:03 and 56:08-1:00:29]]).

Product events can power support context and sales prioritization. They can also
power engagement campaigns and personalized onboarding when teams define the
events and properties clearly enough.

Reverse ETL is one concrete last-mile mechanism. Natalie describes teams moving
modeled warehouse outputs back into operational systems such as Salesforce.
Salespeople or marketers can then act on lead scores and other modeled outputs
([[podcast:data-engineering-tools-modern-data-stack|reverse ETL into Salesforce at 35:42-38:36]]).
Arpit names the same operational-analytics path and connects it to tools such
as Census, Hightouch, and Grouparoo
([[podcast:data-led-growth-event-tracking-and-reverse-etl|reverse ETL tools at 37:25-44:24]]).
[[Data Activation]]
and [[Reverse ETL]] cover the delivery
side of the pipeline.

## Build Sequence

This sequence gives a practical starting point:

1. Define the consumer, decision, and freshness need, using Santona's link
   between pipeline design, the business question, and the entities that answer it
   ([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|pipeline keys and entities at 39:23-43:05]]).
2. Document product events or source agreements before collection, following
   Arpit's tracking-plan discussion of event names, properties, types, and
   ownership before instrumentation
   ([[podcast:data-led-growth-event-tracking-and-reverse-etl|tracking plan ownership at 13:34-23:27]]).
3. Write raw data to a warehouse, lake, or lakehouse that fits the data
   structure, since Natalie separates raw ingestion from marts and contrasts
   warehouse and lake use cases
   ([[podcast:data-engineering-tools-modern-data-stack|ELT raw-to-marts split at 17:55-19:26]]).
4. Apply ingestion guardrails such as deduplication, ordering, masking, and
   basic validation, echoing Santona's ingestion-stage protections before
   human-facing destinations
   ([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|ingestion guardrails at 37:10-39:22]]).
5. Model entities, relationships, metrics, marts, or features around the
   consumer's question, because Santona places modeled business entities between
   raw ingestion and final answers
   ([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|modeled data layers at 39:23-43:05]]).
6. Orchestrate extraction, loading, transformation, tests, and delivery with
   visible dependencies, as Natalie separates Airflow, Airbyte, and dbt by job
   responsibility
   ([[podcast:data-engineering-tools-modern-data-stack|Airflow Airbyte and dbt roles at 30:59-33:45]]).
7. Publish schemas, ownership, and change rules, using Mehdi's Kafka example
   where schemas define types and change processes before streams become shared
   dependencies
   ([[podcast:scaling-data-engineering-teams-self-service-platforms|Kafka schema-change rules at 23:26-26:52]]).
8. Add tests, CI/CD, observability signals, SLAs, and runbooks, turning Barr's
   observability signals into explicit checks and recovery paths
   ([[podcast:data-quality-data-observability-data-reliability|observability signals at 16:38-19:10]]).
9. Deliver modeled outputs to dashboards, ML systems, support tools, sales
   tools, or product experiences, following Arpit's collection-to-activation
   flow
   ([[podcast:data-led-growth-event-tracking-and-reverse-etl|collection-to-activation flow at 22:50-30:03 and 56:08-1:00:29]]).
10. Review usage, incidents, and stale data so the pipeline keeps matching the
    workflow it supports, since Barr's SLA framing makes ongoing review part of
    trust, not cleanup after the fact
    ([[podcast:data-quality-data-observability-data-reliability|freshness SLAs at 35:24-40:43]]).

That sequence isn't a universal stack prescription. Teams start by building the
smallest pipeline that satisfies the use case. They add
platform conventions, automation, and observability as more people and systems
depend on it.

