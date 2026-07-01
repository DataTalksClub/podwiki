---
layout: wiki
title: "Customer Data Platforms"
summary: "How DataTalks.Club guests frame customer data platforms as bundled tools for collecting, segmenting, analyzing, and activating customer data."
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

In DataTalks.Club episodes, CDPs appear as one way to solve
[data activation]({{ '/wiki/data-activation/' | relative_url }}). A team stops
only reporting on customer behavior and starts using that behavior in the tools
where customers and internal teams act.

[Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }}) gives the
clearest CDP framing in
[Data-Led Growth, Event Tracking, and Reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
At 38:20, he describes CDPs as bundled systems where teams can track data, send
it to other tools, and create audiences. Teams can also build models or
segments inside the CDP. He also says CDPs are limited compared with warehouse
modeling. They can still be useful for marketers and growth teams that need to
work with customer data without waiting on a full data team.

That makes CDPs adjacent to
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}). They also sit
near [product analytics]({{ '/wiki/product-analytics/' | relative_url }}),
[reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}), and the
[modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }}). A CDP
isn't just storage. Teams buy or build it to collect, unify, segment, and
activate customer data.

## Bundled Collection, Segmentation, and Activation

A CDP gives business teams a customer data layer they can use without
assembling every part of the stack themselves. Arpit's growth-stack sequence
starts with a
[tracking plan]({{ '/wiki/tracking-plans/' | relative_url }}) at 13:34. It then
moves to collection and storage at 22:50, analysis at 28:52, activation at
30:03, and CDPs at 38:20.

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

## Growth Speed Versus Identity Depth

Arpit frames CDPs from the growth team's side. At 39:54 in the
[data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
he advises teams to define the questions they want to answer before choosing
tools. He accepts that early teams may not have a dedicated data engineer. For
those teams, a CDP can give marketers and growth teams usable customer data
quickly.

[Sonal Goyal]({{ '/people/sonalgoyal/' | relative_url }}) approaches the same
space from the identity side in
[Building an Open-Source ML-Powered Identity Resolution Tool in the Modern Data Stack]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }}).
At 5:47, she explains the problem as deciding whether several warehouse records
refer to the same real-world customer. At 24:32, she says CDPs and master data
management systems sometimes include identity-resolution capabilities. A
dedicated identity-resolution tool can go deeper than that bundled capability.

The boundary question is where the hard problem lives. Arpit's CDP discussion
centers on speed, activation, and tool selection. Sonal's episode shows why the
profile inside the CDP can be hard. Simple joins break when records are
duplicated, identifiers are weak, matches are fuzzy, or teams need a
[customer 360]({{ '/wiki/entity-resolution/' | relative_url }}) view.

## Event Quality and Tracking Plans

A CDP is only as useful as the events flowing into it. At 13:34 in the
[data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
Arpit starts with the tracking plan. Teams should document the events they want
to collect, the event properties, the user properties, and the account or
organization properties. That connects CDPs directly to
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}).

Arpit's examples at 24:43 are deliberately concrete. A SaaS product might track
signup and email verification, while a project-management product might track
project creation, invites, and tasks.

An invoicing product might track clients and invoices. Arpit recommends
reducing the initial list to the events needed to understand the customer
journey from acquisition to activation. That advice prevents a CDP from
becoming a dumping ground for noisy, unused events.

The client-side versus server-side distinction also matters. At 27:00, Arpit
explains that a client-side signup click can fire before a signup succeeds. A
server-side event can wait until the user is actually added to the database. If
a CDP uses the wrong event as the basis for an audience, marketing and support
teams may act on behavior that never happened.

## Identity Resolution and Customer 360

CDPs promise a useful customer profile, but a profile isn't the same thing as a
trusted identity. Sonal's
[identity-resolution episode]({{ '/podcasts/building-open-source-data-product-for-identity-resolution/' | relative_url }})
shows why. At 5:47, she describes enterprises with customer records from
offline channels and online stores. She also names surveys, ticketing systems,
and other interactions. The practical question is whether several records refer
to the same real-world customer.

At 8:02, Sonal separates deduplication from customer 360. Deduplication may
merge or remove duplicate records, while customer 360 keeps enough linked
records to complete the story. That distinction is important for CDPs because
marketers, support teams, and product teams often need a full history, not just
one clean row. It also connects CDPs to
[entity resolution]({{ '/wiki/entity-resolution/' | relative_url }}), where the
same matching problem can apply to suppliers and products. It can also apply to
accounts, locations, and other entities.

At 40:36 and 44:25, Sonal also warns that teams often can't join real-world
customer data by one reliable identifier. Email, name, address, and KYC fields
may vary across systems. That makes CDP profile data overlap with
[data governance]({{ '/wiki/data-governance/' | relative_url }}) and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).
It also connects CDPs to
[data products]({{ '/wiki/data-products/' | relative_url }}) when audiences
drive money movement, compliance, or customer outreach.

## Warehouse-Centered Activation and Reverse ETL

CDPs and reverse ETL solve nearby problems in different shapes. At 37:25 in the
[data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
Arpit names Census, Hightouch, and Grouparoo as reverse ETL or operational
analytics tools. Teams use them to send warehouse data into sales, marketing,
and advertising systems. They can also send warehouse data into support and
product analytics tools. At 38:20, Arpit places CDPs beside that
warehouse-centric path.

The split is practical because a CDP can collect and activate customer data
inside one product. It can also handle modeling and segmentation. Reverse ETL
assumes the team models data in the warehouse first and then syncs it into
operational tools. CDPs can move faster for non-engineering teams, while
warehouse-centered activation gives analysts and engineers more control over
transformations and tests. They also control documentation and ownership.

Arpit's activation examples at 30:03 show why this choice matters. Support
teams can see product behavior in their help desk. Sales teams can see product
signals in their CRM. Marketing and engagement tools can send personalized
emails or onboarding messages. If the CDP profile or warehouse model is wrong,
those mistakes reach customers and customer-facing teams directly.

## Governance for Activated Customer Data

CDPs make customer data easier to use, so teams need stronger governance around
the same data. At 18:27 in the
[data-led growth episode]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}),
Arpit discusses anomaly investigation and source awareness. Teams need to trace
where an event came from before trusting it in a dashboard or activation tool.
At 51:40, he connects self-serve analytics with documentation and data
literacy, which are necessary when non-engineering teams work directly with
customer data.

Sonal's identity-resolution episode adds privacy and correctness risk. At
45:50, she discusses fraud and KYC scenarios where different records for the
same person can hide the real flow of activity. That same identity power can
create risk in ordinary customer systems if teams merge records incorrectly or
send sensitive profile fields into too many tools.

For a CDP, governance covers several decisions:

- which events teams may collect
- which properties may leave the product
- how identity rules work
- who can create or activate audiences
- how teams monitor downstream syncs

Arpit and Sonal don't frame CDPs as a substitute for governance. They frame
CDPs as a place where
[data observability]({{ '/wiki/data-observability/' | relative_url }}),
[privacy engineering]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }}),
and ownership become more visible because customer data starts affecting real
interactions.

## Adjacent Stack Topics

CDP decisions usually depend on event collection and warehouse modeling. They
also depend on operational syncs, identity matching, and governance.

- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Entity Resolution]({{ '/wiki/entity-resolution/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Privacy Engineering for ML]({{ '/wiki/privacy-engineering-for-ml/' | relative_url }})
