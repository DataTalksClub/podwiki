---
layout: wiki
title: "Tracking Plans"
summary: "How the podcast archive frames tracking plans as the schema, contract, and governance artifact for product event instrumentation."
related:
  - Event Tracking
  - Data-Led Growth
  - Product Analytics
  - Data Governance
  - Data Quality and Observability
---

A tracking plan is the schema agreement for product instrumentation. It records
which events a product should collect and which properties belong on each
event. It also records event meanings, capture points, and change owners. Teams
use it before engineers implement [[event tracking]] so that product actions
have a shared meaning before they reach analytics, dashboards, experiments, and
activation tools.

The data-led growth stack starts with this plan before collection begins. Teams
document each event and event property before the data flows into the warehouse
or analytics stack. They also record user and account properties, data types,
semantic meaning, and ownership
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].

Use tracking plans for the schema agreement and governance record. For captured
events moving through client-side and server-side instrumentation, see
[[event tracking]]. The downstream path includes analytics and experiments. It
also includes warehouse models, support views, sales workflows, and reverse
ETL.

## Shared Event Rules

A tracking plan gives product, growth, analytics, and engineering teams shared
rules for event instrumentation. The team decides which product moments matter,
names those events, defines the properties, and records where each event should
fire. Engineers then instrument the product. Analysts use the same definitions
in funnels, experiments, [[data activation]], and recurring reports.

When a metric changes, the tracking plan gives teams context for checking event
data. A signup spike can come from a clicked button, a submitted form, a
verified email, or a completed server record. Teams follow up differently on
fake accounts and real users. The plan needs enough context to separate intent
signals from completed product behavior
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan discussion]].

## Plan Fields

Event names and properties are the first visible parts of a tracking plan. The
data-led growth episode uses signup and email verification as SaaS examples.
Creation events cover projects and teammate invitations. They also cover tasks,
clients, and invoices
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth SaaS event examples]].

The event name should tell analysts which product action happened, while the
properties explain the context. A `signup` event can mean a clicked button, a
submitted form, an email verification, or a completed server record. The plan
should choose the intended meaning instead of leaving analysts to infer it
later.

Teams also need property names and types. Event, user, and account properties
let analysts segment a funnel by acquisition channel or plan type. They can
also use account size, device, or source without reverse-engineering the event
later
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan definition]].

## Capture Rules

Capture location is part of the rule, not an implementation footnote. A
browser event can represent intent, while a server event can represent
completion. Client-side events fit clicks, page interactions, and other
user-interface behavior. Server-side events fit completed actions such as
successful signup or project creation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Client-side and server-side tracking]].

That distinction matters when events feed [[metrics]]. A team investigating a
spike needs to know which event fired, where it fired, and which properties can
explain the source. A vague event name can make failed form submissions,
low-quality traffic, and completed accounts look like the same product behavior
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth anomaly investigation]].

Teams can start with a spreadsheet or document when the event set is small. The
plan still comes before instrumentation. Avo, Iteratively, and TrackPlan are
collaborative tracking-plan tools for taxonomy and event-quality discussion.
Engineers still need to implement the events and confirm where each event
should fire
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan tools]].

## Governance and Ownership

Tracking plans need owners because event definitions change as products change,
and ownership is part of the tracking-plan definition. Data engineers,
analysts, analytics engineers, and product operations all touch the stack.
Documentation and data literacy decide whether new team members can interpret
the events
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth team structure discussion]].

Governance starts with a small set of decisions. The team needs to decide who
can add an event, who reviews the name and properties, and which engineer owns
implementation. It also needs a product or analytics owner who confirms the
meaning. When an event changes, the team needs a notification path. Without
those answers, a tracking plan can drift into stale documentation while the
product keeps changing
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan ownership]].

Kafka schemas and schema registries provide a platform analogy. Schemas and
schema registries help teams control event structure and allowed changes.
Product tracking plans do the same kind of work for analytics events. They make
change review explicit before downstream models, funnels, experiments, or
reverse ETL syncs depend on the event
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

## Data Quality Boundary

A tracking plan is a front-door data-quality control. It reduces duplicate
event names, inconsistent casing, and vague meanings. It also reduces missing
owners and undocumented capture points before data enters the stack. Product
events still need downstream guardrails after collection, but the plan gives
those later checks a definition to compare against.

The relevant podcast discussions agree on shared definitions while focusing on
different failure modes. The data-led growth discussion covers the collection
step before analytics, activation, or reverse ETL depend on the events
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
The modern data stack discussion focuses on raw storage, ingestion guardrails,
dbt models, and data marts. It also covers BI work and cleanup of unused data
after collection
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
The platform discussion uses Kafka schemas, schema registries, allowed changes,
and review as the adjacent discipline for event schemas
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

After collection, [[data quality and observability]] and
[[data-quality-and-observability=>data observability]] keep the modeled data
usable. [[DataOps]] and [[data governance]] belong in the same quality work
[[cite:data-engineering-tools-modern-data-stack=>Modern data stack discussion]].
The tracking plan doesn't replace those practices. It gives product events
clear rules before the rest of the stack has to clean, model, or activate
them.

## Analytics and Activation Use The Rules

Tracking plans support [[product analytics]] because product analytics tools
need consistent event names and properties. The data-led growth stack moves
from the tracking plan into collection, warehouse storage, analysis, and
activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth collection-to-analysis flow]].
If analysts can't use the documented event to build a funnel, cohort, or
activation metric, the event definition is still too vague.

Tracking plans also sit behind experimentation. Experiments need
randomization, assignment tracking, stable metrics, and power analysis
[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]].
The plan doesn't replace experiment design, but it clarifies which events mark
assignment, exposure, and outcomes. The related measurement pages are
[[a-b-testing=>A/B Testing]] and
[[Experimentation and Causal Inference]].

The same rule set matters when product events leave dashboards. Activation
makes product data available in support, sales, engagement, and product
experiences
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth activation discussion]].
[[Reverse ETL]] sends warehouse data back into operational systems
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth reverse ETL discussion]].
[[Customer data platforms]] create a related path by bundling collection,
segmentation, and activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth CDP tradeoff discussion]].
Bad event definitions can become bad customer-facing actions, so the
tracking-plan rules still matter after capture.

## Related Pages

Tracking plans define the event rules for [[event tracking]],
[[data-led-growth=>data-led growth]], and [[product analytics]]. They also
support [[data activation]], [[reverse ETL]], and
[[customer data platforms]] when product behavior reaches operational tools.

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
