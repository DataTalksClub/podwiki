---
layout: wiki
title: "Tracking Plans"
summary: "Tracking plans as the schema, contract, and governance artifact for product event instrumentation."
related:
  - Event Tracking
  - Data-Led Growth
  - Product Analytics
  - Data Governance
  - Data Quality and Observability
---

A tracking plan is the schema agreement for product instrumentation. It records
which events a product should collect and which properties belong on each
event. It also records event meanings, required capture semantics, data types,
and change owners. Teams use it before engineers implement [[event tracking]]
so that product actions have a shared meaning before they reach analytics,
dashboards, experiments, and activation tools.

The data-led growth stack starts with this plan before collection begins. Teams
document each event and event property before the data flows into the warehouse
or analytics stack. They also record user and account properties, data types,
semantic meaning, and ownership
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>How to Build a Data-Led Growth Stack]].

Use tracking plans for the schema agreement and governance record. For captured
events moving through client-side and server-side instrumentation, see
[[event tracking]]. The downstream path includes analytics and experiments. It
also includes warehouse models, support views, sales workflows, and reverse
ETL. The plan needs to define what each event is allowed to mean before those
systems depend on it.

## Event Specifications

A tracking plan gives product, growth, analytics, and engineering teams shared
rules for event instrumentation. The team decides which product moments matter,
names those events, defines the properties, and records the required capture
semantics. Engineers then instrument the product. Analysts use the same
definitions in funnels, experiments, [[data activation]], and recurring
reports.

When a metric changes, the tracking plan gives teams context for checking event
data. A signup spike can come from a clicked button, a submitted form, a
verified email, or a completed account record. Teams follow up differently on
fake accounts and real users. The plan needs enough context to say which
meaning is valid for the metric. [[Event tracking]] verifies what the running
product actually emitted
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>Data-led growth tracking-plan definition]].

## Plan Fields

Event names and properties are the first visible parts of a tracking plan. The
data-led growth episode uses signup and email verification as SaaS examples.
Creation events cover projects and teammate invitations. They also cover tasks,
clients, and invoices
[[cite:data-led-growth-event-tracking-and-reverse-etl@24:43=>Data-led growth SaaS event examples]].

The event name should tell analysts which product action happened, while the
properties explain the context. A `signup` event can mean a clicked button, a
submitted form, an email verification, or a completed server record. The plan
should choose the intended meaning, required properties, and allowed source
before analysts have to infer those details later.

Teams also need property names and types. Event, user, and account properties
let analysts segment a funnel by acquisition channel or plan type. They can
also use account size, device, or source without reverse-engineering the event
later
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>Data-led growth tracking-plan definition]].

## Required Capture Semantics

Capture location is part of the specification, not an implementation footnote. A
browser event can represent intent, while a server event can represent
completion. The plan should state whether an event is required from the client,
the server, or both. It should also state whether the event marks an attempted
action or a completed business action
[[cite:data-led-growth-event-tracking-and-reverse-etl@27:00=>Client-side and server-side tracking]].

That distinction matters when events feed [[metrics]]. A team investigating a
spike needs to know which event was supposed to fire and where. It also needs
properties that explain the source. A vague specification can make failed form
submissions, low-quality traffic, and completed accounts look like the same
product behavior
[[cite:data-led-growth-event-tracking-and-reverse-etl@18:27=>Data-led growth anomaly investigation]].

Teams can start with a spreadsheet or document when the event set is small. The
plan still comes before instrumentation. Avo, Iteratively, and TrackPlan are
collaborative tracking-plan tools for taxonomy and event-quality discussion.
Engineers still need to implement the events, but the plan should make the
expected capture rule reviewable before implementation
[[cite:data-led-growth-event-tracking-and-reverse-etl@20:47=>Data-led growth tracking-plan tools]].

## Governance and Ownership

Tracking plans need owners because event definitions change as products change,
and ownership is part of the tracking-plan definition. Data engineers,
analysts, analytics engineers, and product operations all touch the stack.
Documentation and data literacy decide whether new team members can interpret
the events
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth team structure]].

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
That platform analogy connects tracking plans to [[Streaming]].

## Front-Door Data Quality

A tracking plan is a front-door data-quality control. It reduces duplicate
event names, inconsistent casing, and vague meanings. It also reduces missing
owners and undocumented capture points before data enters the stack. Product
events still need downstream guardrails after collection, but the plan gives
those later checks a definition to compare against.

Tracking-plan quality starts with shared definitions, then extends into several
failure modes. The data-led growth path covers the collection step before
analytics, activation, or reverse ETL depend on the events
[[cite:data-led-growth-event-tracking-and-reverse-etl=>How to Build a Data-Led Growth Stack]].
The modern data stack path adds raw storage, ingestion guardrails, dbt models,
and data marts. It also covers BI work and cleanup of unused data after
collection
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
The platform schema path uses Kafka schemas, schema registries, allowed changes,
and review as the adjacent discipline for event schemas
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].

After collection, [[data quality and observability]] and
[[data-quality-and-observability=>data observability]] keep the modeled data
usable. [[DataOps]] and [[data governance]] belong in the same quality work
[[cite:data-engineering-tools-modern-data-stack=>Modern data stack cleanup and DataOps]].
The tracking plan doesn't replace those practices. It gives product events
clear rules before the rest of the stack has to clean, model, or activate
them.

## Downstream Obligations

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
The plan doesn't replace experiment design, but it should make assignment,
exposure, and outcome events explicit enough for implementation and review. The
related measurement pages are
[[a-b-testing=>A/B Testing]] and
[[Experimentation and Causal Inference]].

The same specification matters when product events leave dashboards. Activation
makes product data available in support, sales, engagement, and product
experiences
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth activation path]].
[[Reverse ETL]] sends warehouse data back into operational systems
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth reverse ETL path]].
[[Customer data platforms]] create a related path by bundling collection,
segmentation, and activation
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth CDP tradeoff]].
Bad event definitions can become bad customer-facing actions, so the
tracking-plan specification should say which events and properties are safe to
reuse outside analytics.

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
