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

A tracking plan records the rules for product instrumentation. It lists the
events a product should collect and the properties attached to those events. It
also records data types, owners, and collection context. Teams use it before
engineers implement [[event tracking]]
so that product actions have a shared meaning. The same definitions can then
reach [[product analytics]],
dashboards, experiments, and activation tools.

The data-led growth stack starts with this plan before collection begins. Teams
document each event and event property before the data flows into the warehouse
or analytics stack. They also record user and account properties, data types,
semantic meaning, and ownership.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

Tracking plans overlap with
[[data governance]] and schema
agreements because they set rules at collection time. They prevent downstream
teams from inheriting ambiguous event names, duplicated events, missing
properties, or product metrics that nobody can trace back to a real action.

## Shared Instrumentation Rules

A tracking plan gives product, growth, analytics, and engineering teams shared
instrumentation rules. The team decides which product moments matter and names
those events. It defines the properties and records where each event should
fire. Engineers then instrument the product. Analysts use the same definitions
in funnels, experiments, [[data activation]],
and recurring reports.

When a metric changes, the tracking plan gives teams context for checking event
data. A signup spike can come from a clicked button, a submitted form, or a
verified email. It can also come from a completed server record. Teams follow
up differently on fake accounts and real users. The plan needs enough context to
separate intent signals from completed product
behavior.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan discussion]]

## Different Failure Modes

The relevant podcast discussions agree that teams need shared definitions. They
focus on different failure modes. The data-led growth discussion covers the
collection step before analytics, activation, or reverse ETL depend on the
events.[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]]

The modern data stack discussion focuses on raw storage and ingestion
guardrails. It connects governance with dbt models and data marts. It also
covers BI work and cleanup of unused data after
collection.[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]

The platform discussion uses Kafka schemas, schema registries, allowed changes,
and review as the adjacent discipline for event contracts.[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]

## Event Names and Properties

Event naming is the first visible part of a tracking plan. The data-led growth
episode uses signup and email verification as SaaS examples. Creation events
cover projects and teammate invitations. They also cover tasks, clients, and
invoices.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth SaaS event examples]]

The event name should tell analysts which product action happened, while the
properties explain the context.

A `signup` event can mean a clicked button, a submitted form, an email
verification, or a completed server record. Client-side events work well for
intent signals such as clicks and page interactions. Server-side events work
better for completed business actions. A tracking plan should make that
distinction explicit.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth client-side and server-side tracking]]

Teams also need property names and types. Event, user, and account properties
let analysts segment a funnel by acquisition channel or plan type. They can also
use account size, device, or source without reverse-engineering the event
later.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan definition]]

## Capture Location

Capture location is part of the definition, not an implementation footnote.
A browser event can represent intent, while a server event can represent
completion. Client-side events fit clicks, page interactions, and other
user-interface behavior. Server-side events fit completed actions such as
successful signup or project creation.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Client-side and server-side tracking]]

That distinction matters when events feed [[metrics]]. A team investigating a
spike needs to know which event fired, where it fired, and which properties can
explain the source. A vague event name can make failed form submissions,
low-quality traffic, and completed accounts look like the same product
behavior.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth anomaly investigation]]

## Product Analytics and Experiments

Tracking plans feed [[product analytics]]
because product analytics tools need consistent event names and properties.
The data-led growth stack moves from the tracking plan into collection,
warehouse storage, analysis, and activation.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth collection-to-analysis flow]]

Product analytics and BI use the same documented product events. Teams can study
acquisition, activation, retention, and engagement from a shared event
base.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth collection-to-analysis flow]]

Product analytics also gives the tracking plan a practical test. If analysts
can't use the documented event to build a funnel, cohort, or activation metric,
the event definition is still too vague.

Tracking plans also sit behind experimentation. Experiments need randomization,
assignment tracking, stable metrics, and power analysis.[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]
Those concerns depend on knowing which events mark assignment and exposure.
Teams also need clear outcome events. A tracking plan doesn't replace
experiment design, but it gives experiment metrics a cleaner event base. The
related measurement pages are
[[a-b-testing=>A/B Testing]] and
[[Experimentation and Causal Inference]].

## Data Quality Control

A tracking plan is also a data-quality control. It reduces duplicate event
names, inconsistent casing, and vague meanings. It also reduces missing owners
and undocumented capture points.

After collection, teams still handle raw-data guardrails, governance, and
cleanup of unused data as data quality work.
Product events therefore need front-door documentation through the tracking
plan. Later,
[[data quality and observability]],
[[data-quality-and-observability=>data observability]], and
[[DataOps]] keep the modeled data usable.[[cite:data-engineering-tools-modern-data-stack=>Modern data stack discussion]]

Teams can start with a spreadsheet or document when the event set is small.
The plan still comes before instrumentation. Avo, Iteratively, and TrackPlan are
collaborative tracking-plan tools for taxonomy and event-quality discussion.
Engineers still need to implement the events and confirm where each event should
fire.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan tools]]

## Activation and Reverse ETL

Tracking plans become more important when product events leave dashboards and
drive operational systems. Activation makes product data available in support,
sales, engagement, and product experiences. Support teams can see customer usage
before replying to a ticket. Sales teams can prioritize accounts. Growth teams
can trigger messages or personalize onboarding.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth activation discussion]]

[[Reverse ETL]] sends warehouse data
back into operational systems. Census, Hightouch, and Grouparoo are examples of
tools in that category.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth reverse ETL discussion]]

The modern data stack version describes warehouse tables moving back into source
systems or business tools. In both cases, bad event definitions can become bad
customer-facing actions.[[cite:data-engineering-tools-modern-data-stack=>Modern data stack reverse ETL discussion]]

[[Customer data platforms]]
create a related path because they bundle collection, segmentation, and
activation. They can only segment and activate events the team defined and
collected, so the tracking plan still
matters.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth CDP tradeoff discussion]]

## Governance and Ownership

Tracking plans need owners because event definitions change as products change,
and ownership is part of the tracking-plan definition. Data engineers, analysts,
analytics engineers, and product operations all touch the stack. Documentation
and data literacy decide whether new team members can interpret the
events.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth team structure discussion]]

Governance starts with a small set of decisions. The team needs to decide who
can add an event, who reviews the name and properties, and which engineer owns
implementation. It also needs a product or analytics owner who confirms the
meaning. When an event changes, the team needs a notification path. Without
those answers, a tracking plan can drift into stale documentation while the
product keeps changing.[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan ownership]]

Kafka schemas and schema registries provide a platform analogy. Schemas and
schema registries help teams control event structure and allowed changes.
Product tracking plans do the same kind of work for analytics events. They make
change review explicit before downstream models, funnels, experiments, or
reverse ETL syncs depend on the event.[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]

## Related Pages

Tracking plans are a small page in a larger measurement system. They define the
event layer for [[event tracking]],
[[data-led-growth=>data-led growth]], and
[[product analytics]]. They also
support [[data activation]],
[[reverse ETL]], and
[[customer data platforms]]
when product behavior reaches operational tools.

- [[Event Tracking]]
- [[data-led-growth=>Data-Led Growth]]
- [[Product Analytics]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[Customer Data Platforms]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[data-quality-and-observability=>Data Observability]]
- [[a-b-testing=>A/B Testing]]
- [[Streaming]]
