---
layout: wiki
title: "Tracking Plans"
summary: "How the podcast archive frames tracking plans as the contract between product, growth, analytics, and engineering for event instrumentation."
related:
  - Event Tracking
  - Data-Led Growth
  - Product Analytics
  - Data Governance
  - Data Quality and Observability
---

## Definition and Scope

A tracking plan documents the events and properties a product should capture.
It also records data types, owners, and implementation details. In the archive,
it's the bridge between business questions and instrumentation work. It lets
product, growth, analytics, and engineering teams agree on event meaning before
the data reaches downstream tools.

Tracking plans overlap with governance and data contracts. They govern product
behavior data at collection time, before downstream teams inherit ambiguous or
duplicated event names.


## Recurring Archive Themes

Plans preserve source context. Arpit links tracking plans to data skepticism
because people can only question an event's accuracy when they know where it
came from, how it was collected, and what action triggered it.

A plan should exist before instrumentation. The growth-stack episode
recommends creating the plan before implementing product analytics or
event-based engagement tools. The plan describes what to capture, then
engineers implement it.

Useful plans include implementation details. The archive examples include event
names, event properties, and data types. User and account properties matter
too, along with capture location and engineer ownership.

Collaboration beats spreadsheet drift. Spreadsheets and docs can work early,
but purpose-built tools such as Avo, Iteratively, and TrackPlan support
collaboration, taxonomy, data quality, and event-level discussion.

Tracking plans are quality controls. The plan reduces duplicated names,
inconsistent casing, vague event meanings, and missing ownership. It also gives
analysts and growth teams a path for investigating anomalies.

## Episode Evidence

These episodes give the strongest evidence:

- [Data-Led Growth Stack](https://datatalks.club/podcast.html), 13:34-16:01:
  defines tracking plans as documentation for every captured event, its
  properties, data types, and semantics. Source:
  `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- [Data-Led Growth Stack](https://datatalks.club/podcast.html), 16:01-19:12:
  argues that companies should document instrumentation early so new people can
  interpret events, spot conflicts, and debug anomalies.
- [Data-Led Growth Stack](https://datatalks.club/podcast.html), 20:47-22:50:
  mentions Avo, Iteratively, and TrackPlan as collaborative tools. It also
  clarifies that engineers still need to implement the events.
- [Data-Led Growth Stack](https://datatalks.club/podcast.html), 23:27-28:52:
  walks through event selection, property definition, and engineer feedback. It
  also covers event ownership and client-side versus server-side choices.
- [Scaling Data Engineering Teams](https://datatalks.club/podcast.html),
  23:26-27:04: provides adjacent evidence from Kafka. Schemas, schema
  registries, allowed changes, and change processes prevent downstream parsing
  and modeling pain. Source:
  `../datatalksclub.github.io/_podcast/scaling-data-engineering-teams-self-service-platforms.md`.

## Tradeoffs

A simple spreadsheet is often enough for an early team. It becomes fragile when
many teams request events, engineers implement them independently, and
downstream tools depend on consistent taxonomy. Purpose-built tracking-plan
tools can reduce drift, but they add another system to maintain.

The plan shouldn't become a wish list of every possible event. Arpit recommends
cutting early plans to the events needed for near-term journey analysis. Teams
can iterate as the product and use cases mature.

## Related Pages

Useful adjacent pages:

- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})
