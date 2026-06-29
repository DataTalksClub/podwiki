---
layout: wiki
title: "Tracking Plans"
summary: "How the podcast archive frames tracking plans as shared event-instrumentation rules for product, growth, analytics, and engineering teams."
related:
  - Event Tracking
  - Data-Led Growth
  - Product Analytics
  - Data Governance
  - Data Quality and Observability
---

## Definition

A tracking plan records the rules for product instrumentation. It lists the
events a product should collect and the properties attached to those events. It
also records data types, owners, and collection context.

Product, growth, analytics, and engineering teams use the plan before they
implement [event tracking]({{ '/wiki/event-tracking/' | relative_url }}).
Everyone should know what a product action means before the data reaches
dashboards, experiments, or activation tools.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
clearest DataTalks.Club definition in
[How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
At 13:34, he starts the growth stack with a tracking plan. Teams document each
event and event property before they collect the data. They also document user
and account properties, data types, semantics, and ownership.

Tracking plans overlap with
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and schema
agreements because they set rules at collection time. They prevent downstream
teams from inheriting ambiguous event names, duplicated events, missing
properties, or product metrics that nobody can trace back to a real action.

## Common Definition

Across the relevant episodes, a tracking plan is less a spreadsheet and more a
shared agreement. The team decides which product moments matter, names those
events, defines the properties, and records where the event should fire. Then
engineers instrument the product and analysts use the same definitions in
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
funnels, experiments, and [data activation]({{ '/wiki/data-activation/' | relative_url }}).

Arpit ties this to data skepticism at 10:45-18:27 in the data-led growth
episode. A data-led professional should know where data comes from and should
question whether it's accurate. A tracking plan gives that person the context
to investigate a signup spike. The spike may come from real users, fake
accounts, a client-side button click, or a server-side completion event.

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) explains the
downstream reason in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
At 17:55-21:22, she discusses raw storage, guardrails, and governance. A
tracking plan gives product events enough meaning for warehouse layers and dbt
models. Data marts and BI work use the same definitions later.

## Guest Differences

Guests agree that teams need explicit event definitions, but they start from
different problems.

Arpit starts from [data-led growth]({{ '/wiki/data-led-growth/' | relative_url }}).
He wants product and growth teams to collect the right behavior data, analyze
it, and then activate it. Support, sales, engagement and product tools use the
same data. His
tracking-plan discussion at 13:34-28:52 focuses on event choice and event
properties. He also covers collection location and engineer feedback
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Natalie starts from the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). Her
episode doesn't center tracking plans, but it explains why product events need
structure before they become warehouse data. Raw ingestion, transformations,
governance, and cleanup all depend on knowing what data means
([modern data stack at 15:30-21:22 and 43:02-43:45]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the adjacent
platform version in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
At 23:26, he discusses Kafka schemas and schema registries. He also covers
allowed changes and change review. That's not product analytics tooling, but it
supports the same principle. Teams need explicit agreements before event data
becomes a dependency for other teams.

## Event Naming

Event naming is the first visible part of a tracking plan. At 24:43, Arpit
uses SaaS examples such as signup, email verification, and project creation.
He also mentions teammate invitations, task creation, client creation, and
invoice creation
([data-led growth at 24:43]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
The event name should tell analysts which product action happened, while the
properties explain the context.

Arpit's signup example shows the naming problem. A `signup` event can mean a
clicked button, a submitted form, an email verification, or a completed server
record. At 27:00, he separates client-side and server-side events. Client-side
events work well for intent signals such as clicks and page interactions, while
server-side events work better for completed business actions. A tracking plan
should make that distinction explicit.

Teams also need property names and types. At 13:34, Arpit includes event
properties and user properties in the plan. He also includes account properties
and data types.
Those details let analysts segment a funnel by acquisition channel or plan
type. They can also use account size, device, or source without
reverse-engineering the event later.

## Product Analytics

Tracking plans feed [product analytics]({{ '/wiki/product-analytics/' | relative_url }})
because product analytics tools need consistent event names and properties.
Arpit places product analytics after collection and storage. At 22:50-30:03,
he moves from the tracking plan into collection and warehouse storage. Product
analytics and BI use the same documented product events. Teams can then study
acquisition, activation, retention, and engagement
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

This also connects tracking plans to experimentation. In
[Product Analytics and A/B Testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}),
[Jakob Graff]({{ '/people/jakobgraff/' | relative_url }}) explains that
experiments need randomization and assignment tracking. They also need stable
metrics and power analysis.

At 24:44-37:44, those concerns depend on knowing which events mark assignment
and exposure. Teams also need clear outcome events. A tracking plan doesn't
replace experiment design, but it gives experiment metrics a cleaner event
base.

## Data Quality

A tracking plan is also a data-quality control. It reduces duplicate event
names, inconsistent casing, and vague meanings. It also reduces missing owners
and undocumented capture points.

Arpit's fake-signup example at 18:27 shows the operational value. When a metric
spikes, the team needs to know which event fired and where it came from. The
team also needs properties that can explain the source
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

That quality work continues after collection. Natalie describes raw-data
guardrails and governance at 17:55-21:22 in the modern-stack episode. She also
recommends cleanup of unused data at 43:02. Product events therefore need both
front-door documentation through the tracking plan and downstream controls in
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[data observability]({{ '/wiki/data-observability/' | relative_url }}), and
[DataOps]({{ '/wiki/dataops/' | relative_url }}).

Teams can start with a spreadsheet or document when the event set is small.
Arpit still recommends creating the plan before instrumentation. At 20:47, he
mentions Avo, Iteratively, and TrackPlan as collaborative tracking-plan tools.
Those tools help teams discuss taxonomy and event quality. Engineers still need
to implement the events and confirm where each event should fire.

## Reverse ETL And Activation

Tracking plans become more important when product events leave dashboards and
drive operational systems. Arpit defines activation at 30:03 as making product
data available in support, sales, engagement, and product experiences. Support
teams can see customer usage before replying to a ticket. Sales teams can
prioritize accounts. Growth teams can trigger messages or personalize
onboarding
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

[Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}) sends warehouse data
back into operational systems. At 37:25, Arpit names Census, Hightouch, and
Grouparoo for this job.

Natalie gives the data engineering version at 35:42-39:06 in the modern-stack
episode. She describes warehouse tables moving back into source systems or
business tools. In both cases, bad event definitions can become bad
customer-facing actions.

[Customer data platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
create a related path. At 38:20, Arpit describes CDPs as bundled systems for
collection, segmentation, and activation. A tracking plan still matters in that
setup because the CDP can only segment and activate the events the team
defined and collected.

## Governance And Ownership

Tracking plans need owners because event definitions change as products change.
Arpit includes ownership in the tracking-plan definition at 13:34 and returns
to team structure at 46:13-56:08. Data engineers, analysts, analytics
engineers, and product operations all touch the stack. Documentation and data
literacy decide whether new team members can interpret the events
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Governance starts with a small set of decisions. The team needs to decide who
can add an event, who reviews the name and properties, and which engineer owns
implementation. It also needs a product or analytics owner who confirms the
meaning. When an event changes, the team needs a notification path. Without
those answers, a tracking plan can drift into stale documentation while the
product keeps changing.

Mehdi's Kafka discussion gives a useful platform analogy. At 23:26 in the
scale-up episode, schemas and schema registries help teams control event
structure and allowed changes. Product tracking plans do the same kind of work for
analytics events. They make change review explicit before downstream models,
funnels, experiments, or reverse ETL syncs depend on the event.

## Related Pages

These pages cover the concepts that tracking plans define or support.

- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
