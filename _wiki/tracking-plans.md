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

A tracking plan documents the events, properties, data types, owners, and
implementation details a product should capture. In the archive, it is the
bridge between business questions and instrumentation work. It lets product,
growth, analytics, and engineering teams agree on what an event means before it
appears in dashboards, campaigns, support tools, or reverse ETL syncs.

Tracking plans overlap with governance and data contracts. They govern product
behavior data at collection time, before downstream teams inherit ambiguous or
duplicated event names.

## Contents

- [Recurring Archive Themes](#recurring-archive-themes)
- [Episode Evidence](#episode-evidence)
- [Tradeoffs](#tradeoffs)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Recurring Archive Themes

### Plans preserve source context

Arpit links tracking plans to data skepticism. People can only question an
event's accuracy when they know where it came from, how it was collected, and
what action triggered it.

### A plan should exist before instrumentation

The growth-stack episode recommends creating the plan before implementing a
product analytics tool or event-based engagement tool. The plan describes what
to capture, then engineers implement it.

### Useful plans include implementation details

The archive examples include event names, event properties, data types, user and
account properties, client-side versus server-side capture, engineer ownership,
and discussion between the requester and developer.

### Collaboration beats spreadsheet drift

Spreadsheets and docs can work early. Purpose-built tools such as Avo,
Iteratively, and TrackPlan appear in the episode because they support
collaboration, taxonomy, data quality, and event-level discussion.

### Tracking plans are quality controls

The plan reduces duplicated names, inconsistent casing, vague event meanings,
and missing ownership. It also gives analysts and growth teams a path for
investigating anomalies.

## Episode Evidence

| Episode | Evidence |
| --- | --- |
| [Data-Led Growth Stack](https://datatalks.club/podcast.html), 13:34-16:01 | Defines tracking plans as documentation for every captured event, properties, data types, and event semantics such as completed signup versus button click. Source: `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`. |
| [Data-Led Growth Stack](https://datatalks.club/podcast.html), 16:01-19:12 | Argues that companies should document instrumentation early so new people can interpret events, spot conflicts such as casing differences, and debug anomalies. |
| [Data-Led Growth Stack](https://datatalks.club/podcast.html), 20:47-22:50 | Mentions Avo, Iteratively, and TrackPlan as collaborative tools, then clarifies that engineers still need to implement the events. |
| [Data-Led Growth Stack](https://datatalks.club/podcast.html), 23:27-28:52 | Walks through event selection, property definition, engineer feedback, event ownership, and client-side versus server-side choices. |
| [Scaling Data Engineering Teams](https://datatalks.club/podcast.html), 23:26-27:04 | Provides adjacent evidence from Kafka: schemas, schema registries, allowed changes, and change processes prevent downstream parsing and modeling pain. Source: `../datatalksclub.github.io/_podcast/scaling-data-engineering-teams-self-service-platforms.md`. |

## Tradeoffs

A simple spreadsheet is often enough for an early team. It becomes fragile when
many teams request events, engineers implement them independently, and
downstream tools depend on consistent taxonomy. Purpose-built tracking-plan
tools can reduce drift, but they add another system to maintain.

The plan should not become a wish list of every possible event. Arpit recommends
cutting early plans to the events needed for near-term journey analysis, then
iterating as the product and use cases mature.

## Related Pages

- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Streaming]({{ '/wiki/streaming/' | relative_url }})

## Maintenance Notes

- Primary source file:
  `../datatalksclub.github.io/_podcast/data-led-growth-event-tracking-and-reverse-etl.md`.
- Good future additions: screenshots or examples are not appropriate unless the
  user requests a website PR. Keep this page as podcast-backed synthesis, not a
  template library.
- If future episodes discuss data contracts for events, add them here only when
  they apply to product or behavioral instrumentation. Broader producer-consumer
  contracts belong on [Data Products]({{ '/wiki/data-products/' | relative_url }})
  or [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
