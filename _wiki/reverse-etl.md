---
layout: wiki
title: "Reverse ETL"
summary: "How the podcast archive explains reverse ETL as sending modeled warehouse data into sales, marketing, support, analytics, and engagement tools."
related:
  - Data Activation
  - Data-Led Growth
  - Customer Data Platforms
  - Product Analytics
  - Modern Data Stack
---

## Definition

Reverse ETL moves modeled data from a warehouse into operational tools. Common
destinations include sales and marketing tools. Support, advertising, product
analytics, and engagement tools are common too. It reverses the usual
[ELT]({{ '/wiki/elt/' | relative_url }}) flow. After a team collects, stores,
and models data, it sends selected fields back to the systems where people act.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
clearest archive definition in
[How to Build a Data-Led Growth Stack]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
At 37:25, he describes reverse ETL, or operational analytics, as sending
warehouse data into tools such as Salesforce and HubSpot. Intercom, advertising
platforms, and product analytics tools appear in the same discussion.

He names Census and Hightouch as examples, and Grouparoo appears too. That places reverse ETL inside
[data activation]({{ '/wiki/data-activation/' | relative_url }}), not inside
reporting alone.

## Common Definition

Across the relevant episodes, reverse ETL means taking trusted warehouse output
and making it available in the tools that run customer-facing work. The usual
sequence starts with
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) or source-system
ingestion. Teams store the data and transform it into customer, account, or
segment models. Then they sync those models into business tools.

In Arpit's growth-stack discussion, this sequence appears between 22:50 and
41:30. He moves from collection and storage to analysis, then activation. At
30:03, support teams use product events while helping customers. Sales teams
use the same signals to prioritize accounts. Engagement tools use them for
messages and product experiences
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) gives the data
engineering version in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
At 35:42, she describes reverse operational data flows as pushing warehouse
tables back to source systems or business tools. At 36:14-38:01, she contrasts
custom scripts with low-code reverse ETL tools that let sales or marketing
teams use warehouse outputs inside their own systems.

## Guest Differences

Guests mostly differ on where they start the architecture. Arpit starts from
[data-led growth]({{ '/wiki/data-led-growth/' | relative_url }}), so his
reverse ETL discussion follows tracking plans and product events. It then moves
into warehouses and BI. He treats the sync layer as a way to turn customer
behavior into support context and sales prioritization. Onboarding and
personalization use the same signal
([Arpit at 13:34-44:24]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Natalie starts from the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). Her
episode separates extraction and warehouse storage, and it also covers
transformations, orchestration, and reverse data flows. Reverse ETL is one more integration layer in a
best-of-breed stack. Teams get specialized tools, but they also own more
boundaries
([Natalie at 33:45-39:06]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) doesn't
center the term reverse ETL, but her
[last-mile data delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
episode explains the adoption test behind it. At 8:48-13:24, she argues that
data work is unfinished until it reaches the decision point. At 34:00-38:15,
she recommends starting from the decision a team needs to make. Reverse ETL
passes that test only when the synced field changes a sales, support,
marketing, or product action.

## Activation Workflows

Reverse ETL is useful when a modeled signal belongs inside an operational
workflow instead of a dashboard. Arpit gives three examples. Support teams see
product behavior in a help desk. Sales teams see product-qualified accounts in
a CRM. Marketing or engagement tools use segments for lifecycle messages or
onboarding nudges
([Arpit at 30:03-33:41]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

This makes reverse ETL narrower than
[data activation]({{ '/wiki/data-activation/' | relative_url }}). Activation
can happen through embedded product experiences or dashboards in meetings. It
can also happen through customer data platforms or direct integrations. Reverse
ETL is the warehouse-centered version: the warehouse holds the selected model,
and a sync tool distributes it to the downstream system.

Reverse ETL also connects to
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}). Product
analytics helps a team find activation, retention, and segmentation patterns.
Reverse ETL moves the chosen signal into a tool where another team can act.
Arpit ties this to product-led growth at 56:08, where activation events and
personalized onboarding use product behavior directly
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Customer Data Platforms

[Customer data platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
solve a nearby problem with a different center of gravity. Arpit places CDPs
beside reverse ETL at 38:20. A CDP can collect customer data, send it to other
tools, create audiences, and support segmentation inside one product
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

The split is practical because a CDP can be faster for marketers or growth
teams that need bundled collection, segmentation, and activation. Reverse ETL
fits teams that already trust their warehouse models and want those models to
drive business tools. That warehouse-centered path gives analysts and engineers
more control over
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
It also keeps testing, documentation, and ownership near the warehouse, but it
requires more stack maturity.

Arpit discusses the buy-or-build tradeoff at 43:50. He names cost and
maintenance as reasons not to buy tools before the problem is clear. He also
cites open-source alternatives, security, and compliance
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Warehouse Modeling

Reverse ETL depends on the warehouse model because the sync copies modeled
fields into another system. A bad model can become a bad customer-facing
action. That's why the archive connects reverse ETL to
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}), and
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}).

Arpit places reverse ETL after warehousing, transformation, and BI. At 28:52,
he describes warehouses and transformation with tools such as dbt. At 35:27,
he discusses warehouse-centric analytics with Snowflake and BigQuery. Redshift
appears in the same comparison.
At 37:25, reverse ETL appears after those modeling steps
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Natalie gives the same dependency from the data engineering side. Her episode
connects Airbyte-style loading and warehouse-side transformations. It also
covers dbt, data marts, orchestration, and reverse data flows. At 35:42, reverse
ETL depends on the warehouse tables already being useful enough to send back
into business systems
([modern data stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

## Governance And Ownership

Reverse ETL raises the cost of unclear definitions. A stale account-health
score can send a sales team after the wrong account. A broken identity rule can
show support the wrong customer history. An ambiguous event can trigger a
campaign for users who never completed the action.

Arpit recommends at 13:34 a tracking plan documenting event definitions and
event properties. The plan also covers user properties and account properties.
Teams should record data types, capture location, and ownership.

At 18:27, he uses anomaly investigation for the same point. Teams need to know
where an event came from before they act on it
([data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Natalie adds the platform ownership concern. At 43:02, she discusses unused
data and team cleanup, and at 48:58, she covers schema evolution. Both concerns
matter for reverse ETL because downstream tools may keep using a field after
the source changes
([modern data stack episode]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }})).

For that reason, reverse ETL should inherit the same controls as the upstream
warehouse work. Teams need owners, freshness checks, tests, and documentation.
They also need alerting and a rollback plan for bad syncs. Those controls connect the topic to
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data observability]({{ '/wiki/data-observability/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

## Related Pages

These adjacent pages cover the upstream modeling work, activation surface, and
operating controls around reverse ETL.

- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
