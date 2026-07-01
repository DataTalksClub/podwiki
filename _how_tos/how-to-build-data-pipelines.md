---
layout: article
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
[Santona Tuli]({{ '/people/santonatuli/' | relative_url }}) describes pipeline
design as a sequence. Data starts with raw arrival, then moves to cleaned
ingestion and modeled business entities. The pipeline finally produces answers
for dashboards or ML systems
([Modern Data Pipeline Architecture on raw-to-answer layers at 37:10-46:01]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

In the modern stack episode,
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) makes the same
point through ELT. Teams keep raw data separate from business-facing marts so
they don't invent inconsistent transformations downstream
([ELT raw-to-marts split at 17:55-19:26]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
For related background, see
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}).

## Start With The Consumer

A pipeline should answer a real question or power a real workflow. Santona's
pipeline discussion is explicit about this. After data arrives, engineers still
need to identify mapping keys, foreign keys, and business entities. They also
need to name the question the business wants answered. She argues that data and
analytics engineers should talk to end users before deciding which tables and
transformations matter
([pipeline keys and entities at 39:23-43:05]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

For product and growth data, that consumer-first work begins even earlier.
[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) recommends a
[tracking plan]({{ '/wiki/tracking-plans/' | relative_url }}) before
instrumentation. Teams define events and properties. They also define data types
and ownership. Then product and growth teams know what an event means before it
reaches analytics or activation tools
([tracking plan ownership at 13:34-23:27]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

If teams use vague event names in
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), they
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
([ELT ingestion-to-marts split at 17:55-19:26]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

Santona adds that ingestion can still perform limited quality work. In her
Upsolver discussion, the early stage handles deduplication and ordering
guarantees. It can also mask or hash PII before the data appears in Snowflake
or another human-facing destination
([ingestion guardrails at 37:10-39:22]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).
Treat those steps as guardrails, not as the place where every business metric
is defined.

Pick storage from the data structure and each team's needs. Natalie describes
warehouses as a strong fit for structured analytics teams. Lakes help when
engineering or data science teams need unstructured files or logs. They also
help with video and other raw formats.

She warns that lakes and warehouses can become swamps. That happens when teams
store unused or poorly governed data that people can't trust
([warehouses and data swamps at 19:50-28:07]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
For that comparison, use
[Data Warehouse vs Data Lakehouse]({{ '/comparisons/data-warehouse-vs-data-lakehouse/' | relative_url }}).

## Model Data Into Useful Outputs

After ingestion, model data around entities, relationships, and business
questions. Santona describes this as finding the keys and relationships across
multiple sources. Teams then build the modeled layer that can answer real
business questions. She separates ingested data and modeled data from answers.
Marts or dashboard-specific transformations sit after the core business entities
([modeled data layers at 39:23-43:05]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).

This is where
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
and [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) overlap.
Natalie connects ELT to analysts using dbt and SQL inside the warehouse. She
then describes data marts as the business-facing layer. Those marts should be
easier to use than raw ingestion tables
([dbt and marts at 7:57-18:47]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

The practical output isn't "a pipeline" in the abstract. It may be a modeled
table or mart, or it may be a feature set, dashboard input, or activation
segment that a consumer understands.

For ML pipelines, Santona says the modeling mindset shifts for machine outputs.
You still deduplicate and handle nulls, and you still transform features for
model training rather than a human-readable business entity
([ML pipeline outputs at 44:57-46:01]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }})).
That boundary is why pipeline work often touches
[MLOps vs DataOps]({{ '/comparisons/mlops-vs-dataops/' | relative_url }}).

## Orchestrate The Work, Not The Buzzwords

Orchestration coordinates jobs after each pipeline step is clear. Natalie
describes Airflow as an orchestrator that schedules work and runs ingestion
jobs. Tools such as Airbyte focus on the extract-load part, while dbt handles
warehouse transformations
([Airflow Airbyte and dbt roles at 30:59-33:45]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

For a local learning or portfolio setup, use
[Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }})
to run the scheduler, UI, and metadata database. It also keeps the DAG folder
and logs in one reviewable environment.

Make dependencies visible and repeatable, and don't rename
the whole pipeline after the scheduler.

At team scale, teams need orchestration conventions. In the scale-up episode,
[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) says a platform is
more than an Airflow cluster. Teams need naming conventions and sequence
practices. They also need playbooks, support channels, and onboarding. With
those habits, other data users can build without turning the platform team into
a bottleneck
([self-service platform conventions at 12:30-17:56]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

See
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
for that operating model.

Streaming adds stricter schema agreements. Mehdi warns that teams can grow from
a few Kafka topics to hundreds quickly. His recommendation is to define typed
schemas and schema registry usage. Teams should also define allowed changes and
a schema-change process before downstream teams depend on the stream
([Kafka schema-change rules at 23:26-26:52]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
covers the latency decision.

## Add Tests, Observability, And Recovery

A pipeline can finish successfully and still deliver bad data. That's the core
warning in [Barr Moses]({{ '/people/barrmoses/' | relative_url }})'s data
observability episode. She names freshness and volume first. She then adds
distribution, schema, and lineage.

Teams use those signals to see whether data is up to date and complete. They
also use them to check whether values look plausible and schemas stay stable.
Lineage connects the right upstream and downstream assets
([observability signals at 16:38-19:10]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).

Freshness expectations should become explicit SLAs when downstream work depends
on them. Barr uses the example of a dataset that must arrive within five
minutes after a user action. The SLA helps the data team prioritize which
freshness incidents matter first, instead of treating every late table as equal
([freshness SLAs at 35:24-40:43]({{ '/podcasts/data-quality-data-observability-data-reliability/' | relative_url }})).
Link those expectations to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [Data Observability]({{ '/wiki/data-observability/' | relative_url }}).

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) turns the
same reliability problem into [DataOps]({{ '/wiki/dataops/' | relative_url }}).
Teams use automation and tests to reduce errors, while monitoring and
observability show what broke. They add version control and CI/CD so
deployments are safer.

In the DataOps for data engineering episode, he argues that teams need realistic
test data and infrastructure as code. End-to-end checks should run before
changes reach production
([DataOps tests at 15:52-16:10 and 30:55-43:02]({{ '/podcasts/dataops-for-data-engineering/' | relative_url }})).

His earlier DataOps episode adds runbooks and automated playbooks. It also
covers end-to-end versioning for code and models, plus visualizations and
governance
([runbooks and versioning at 33:47-51:21]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }})).

## Deliver Data Where People Act

A table may not be enough when the business action happens outside the
warehouse. Arpit says a data-led growth stack starts with collection and
storage. Teams then analyze and activate the data
([collection-to-activation flow at 22:50-30:03 and 56:08-1:00:29]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Product events can power support context and sales prioritization. They can also
power engagement campaigns and personalized onboarding when teams define the
events and properties clearly enough.

Reverse ETL is one concrete last-mile mechanism. Natalie describes teams moving
modeled warehouse outputs back into operational systems such as Salesforce.
Salespeople or marketers can then act on lead scores and other modeled outputs
([reverse ETL into Salesforce at 35:42-38:36]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).
Arpit names the same operational-analytics path and connects it to tools such
as Census, Hightouch, and Grouparoo
([reverse ETL tools at 37:25-44:24]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
[Data Activation]({{ '/wiki/data-activation/' | relative_url }})
and [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) cover the delivery
side of the pipeline.

## Build Sequence

This sequence gives a practical starting point:

1. Define the consumer, decision, and freshness need.
2. Document product events or source agreements before collection.
3. Write raw data to a warehouse, lake, or lakehouse that fits the data structure.
4. Apply ingestion guardrails such as deduplication, ordering, masking, and basic validation.
5. Model entities, relationships, metrics, marts, or features around the consumer's question.
6. Orchestrate extraction, loading, transformation, tests, and delivery with visible dependencies.
7. Publish schemas, ownership, and change rules.
8. Add tests, CI/CD, observability signals, SLAs, and runbooks.
9. Deliver modeled outputs to dashboards, ML systems, support tools, sales tools, or product experiences.
10. Review usage, incidents, and stale data so the pipeline keeps matching the workflow it supports.

That sequence isn't a universal stack prescription. Teams start by building the
smallest pipeline that satisfies the use case. They add
platform conventions, automation, and observability as more people and systems
depend on it.
