---
layout: wiki
title: "Customer Data Platforms"
summary: "Customer data platforms as bundled tools for collecting, segmenting, analyzing, and activating customer data."
related:
  - Data Activation
  - Reverse ETL
  - Data-Led Growth
  - Product Analytics
  - Event Tracking
  - Entity Resolution
---

## Customer Profile and Activation Layer

A customer data platform, or CDP, collects customer events and profile data. It
joins those records around customers or accounts and makes the result available
for customer-facing work. Teams use CDPs for segmentation and personalization.
They also use them in support, sales, marketing, and product decisions.

CDPs are one way to solve
[[data activation]]. A team stops
only reporting on customer behavior and starts using that behavior in the tools
where customers and internal teams act.

A CDP bundles tracking, routing, audience creation, and in-platform modeling or
segmentation. CDPs are limited compared with warehouse modeling. They can still
help marketers and growth teams work with customer data without waiting on a
full data team.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

That makes CDPs adjacent to
[[event tracking]] and
[[tracking plans]]. They also sit
near [[product analytics]],
[[reverse ETL]], and the
[[modern data stack]]. A CDP
isn't just storage. Teams buy or build it to collect, unify, segment, and
activate customer data.

## Bundled Collection, Segmentation, and Activation

A CDP gives business teams a customer data layer they can use without
assembling every part of the stack themselves. The growth-stack sequence starts
with a [[tracking-plans=>tracking plan]]. It then moves through collection and
storage before analysis, activation, and CDPs.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

In that order, a CDP is a shortcut through several jobs:

- collect product and customer events
- attach event properties, user properties, and account properties
- route data to analytics, support, sales, marketing, and engagement tools
- build audiences, models, or segments
- activate those segments in customer-facing channels

This definition separates CDPs from narrower tools. A product analytics tool
helps teams understand funnels, retention, and feature usage. A warehouse gives
analysts and engineers a controlled place to model data. A reverse ETL tool
sends warehouse-modeled data back to operational tools. A CDP can include parts
of all three, but the bundle is the product.

Teams can also model audiences in the warehouse first. In that path,
[[RFM Analysis]] is one customer-segmentation method they can move into a CDP
or reverse ETL destination for activation[[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]].

## Growth Speed Versus Identity Depth

CDPs make most sense from the growth team's side. Teams should define the
questions they want to answer before choosing tools. When early teams lack a
dedicated data engineer, a CDP can give marketers and growth teams usable
customer data quickly.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

Identity-resolution work starts by deciding whether several warehouse records
refer to the same real-world customer. CDPs and master data management systems
sometimes include identity-resolution capabilities. A dedicated
identity-resolution tool can go deeper than that bundled capability.[[cite:building-open-source-data-product-for-identity-resolution=>Identity Resolution Tool]]

Tool choice moves the hard problem because CDP work centers on speed and
activation while identity-resolution work puts profile construction under
pressure. Simple joins break when records are duplicated or identifiers are
weak. They also break when matches are fuzzy or teams need a
[[entity-resolution=>customer 360]] view.[[cite:building-open-source-data-product-for-identity-resolution@40:36=>Identity Resolution Tool]]

## Event Quality and Tracking Plans

A CDP depends on the events flowing into it. Before collection, teams should
document four parts of the tracking plan.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

- event names
- event properties
- user properties
- account or organization properties

CDPs depend on
[[event tracking]] and
[[tracking plans]].

The examples are deliberately concrete. A SaaS product might track signup and
email verification, while a project-management product might track project
creation, invites, and tasks.

An invoicing product might track clients and invoices. The recommendation is to
reduce the initial list to the events needed to understand the customer journey
from acquisition to activation. That advice prevents a CDP from becoming a
dumping ground for noisy, unused events.

Client-side and server-side events can describe different moments. A client-side
signup click can fire before a signup succeeds. Server-side instrumentation can
wait for the database insert.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]
Wrong events create wrong audiences. Marketing and support teams may act on
behavior that never happened.

## Identity Resolution and Customer 360

CDPs promise a useful customer profile. A profile still isn't the same thing as
a trusted identity. Enterprises hold customer records from offline channels and
online stores. They also hold surveys, ticketing systems, and other
interactions. Teams still need to decide whether several records refer to the
same real-world customer.[[cite:building-open-source-data-product-for-identity-resolution=>Identity Resolution Tool]]

Deduplication may merge or remove duplicate records. Customer 360 preserves
linked records.[[cite:building-open-source-data-product-for-identity-resolution=>Identity Resolution Tool]]
That distinction is important for CDPs because marketers, support teams, and
product teams often need a full history. One clean row isn't enough. It also
connects CDPs to
[[entity resolution]], where the
same matching problem can apply to suppliers and products. It can also apply to
accounts, locations, and other entities.

Teams often can't join real-world customer data by one reliable identifier.
Identifiers vary across systems.[[cite:building-open-source-data-product-for-identity-resolution=>Identity Resolution Tool]]
Email, name, address, and KYC fields may all describe the same person
differently.
That makes CDP profile data overlap with
[[data governance]] and
[[data quality and observability]].
It also connects CDPs to
[[data products]] when audiences
drive money movement, compliance, or customer outreach.

## Warehouse-Centered Activation and Reverse ETL

CDPs and reverse ETL solve nearby problems in different shapes. Census,
Hightouch, and Grouparoo are reverse ETL or operational analytics tools. They
send warehouse data into sales, marketing, and advertising systems. They can
also sync support and product analytics tools. CDPs sit beside that
warehouse-centric path.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

The split is practical because a CDP can collect and activate customer data
inside one product. It can also handle modeling and segmentation. Reverse ETL
assumes the team models data in the warehouse first and then syncs it into
operational tools. CDPs can move faster for non-engineering teams.
A warehouse-centered activation path gives analysts and engineers more control
over transformations, tests, documentation, and ownership.

Activation reaches customer-facing teams directly.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

- support teams can see product behavior in their help desk
- sales teams can see product signals in their CRM
- marketing and engagement tools can send personalized emails or onboarding
  messages

If the CDP profile or warehouse model is wrong, those mistakes reach customers
and customer-facing teams directly.

## Governance for Activated Customer Data

CDPs make customer data easier to use, so teams need stronger governance around
the same data. Teams need to trace where an event came from before trusting it
in a dashboard or activation tool. Self-serve analytics also depends on
documentation and data literacy when non-engineering teams work directly with
customer data.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]

Identity resolution adds privacy and correctness risk. Separate records can hide
fraud, anti-money-laundering, and KYC activity
[[cite:building-open-source-data-product-for-identity-resolution@45:50=>Identity Resolution Tool]].
The same identity power can create risk in ordinary customer systems. Teams may
merge records incorrectly or send sensitive profile fields into too many tools.

For a CDP, governance covers several decisions:

- which events teams may collect
- which properties may leave the product
- how identity rules work
- who can create or activate audiences
- how teams monitor downstream syncs

CDPs aren't a substitute for governance. They're a place where
[[data-quality-and-observability=>data observability]],
[[privacy-engineering-for-ml=>privacy engineering]],
and ownership become more visible because customer data starts affecting real
interactions.

## Related Pages

CDP decisions usually depend on event collection and warehouse modeling. They
also depend on operational syncs, identity matching, and governance.

- [[Data Activation]]
- [[Reverse ETL]]
- [[data-led-growth=>Data-Led Growth]]
- [[Product Analytics]]
- [[Event Tracking]]
- [[Tracking Plans]]
- [[Entity Resolution]]
- [[Modern Data Stack]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[Privacy Engineering for ML]]
