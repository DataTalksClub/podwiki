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

A tracking plan is the specification artifact for product instrumentation. It
records which events a product should collect and which properties belong on
each event. It also records owners, downstream analytics dependencies, event
meanings, and capture semantics. Data types, review expectations, naming
conventions, and change rules belong there too. Teams use it before engineers
implement [[event tracking]] so product actions have a shared meaning before
they reach analytics, dashboards, experiments, and activation tools.

The data-led growth stack starts with this plan before collection begins. Teams
document each event and event property before the data flows into the warehouse
or analytics stack. They also record user and account properties, data types,
semantic meaning, and ownership.
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>How to Build a Data-Led Growth Stack]]

Use tracking plans for names and properties, owners and review paths, plus
shared rules. Those rules coordinate product and engineering work. They also
coordinate analytics and downstream tools.

For captured events moving through client-side and server-side
instrumentation, see [[event tracking]]. The plan matters because analytics
and experiments can depend on the same event definition. Warehouse models,
support views, sales workflows, and reverse ETL can depend on it too.

## Specification Before Instrumentation

A tracking plan gives product, growth, analytics, and engineering teams shared
rules before anyone ships instrumentation. The team decides which product
moments matter, names those events, defines the properties, and records the
required capture semantics. Engineers then instrument the product. Analysts use
the same definitions in funnels, experiments, [[data activation]], and recurring
reports.

When a metric changes, the tracking plan gives teams context for checking event
data. A signup spike can come from a clicked button, a submitted form, a
verified email, or a completed account record. Teams follow up differently on
fake accounts and real users. The plan needs enough context to say which
meaning is valid for the metric. [[Event tracking]] verifies what the running
product actually emitted.
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>Data-led growth tracking-plan definition]]

## Names, Properties, and Meaning

Event names and properties are the first visible parts of a tracking plan. The
data-led growth episode uses signup and email verification as SaaS examples.
Creation events cover projects and teammate invitations. They also cover tasks,
clients, and invoices.
[[cite:data-led-growth-event-tracking-and-reverse-etl@24:43=>Data-led growth SaaS event examples]]

The event name should tell analysts which product action happened, while the
properties explain the context. A `signup` event can mean a clicked button, a
submitted form, an email verification, or a completed server record. The plan
should choose the intended meaning, required properties, allowed source, and
downstream dependencies before analysts have to infer those details later.
Runtime debugging for whether the product emitted the right signal belongs in
[[event tracking]].

Teams also need property names and types. Event, user, and account properties
let analysts segment a funnel by acquisition channel or plan type. They can
also use account size, device, or source without reverse-engineering the event
later.
[[cite:data-led-growth-event-tracking-and-reverse-etl@13:34=>Data-led growth tracking-plan definition]]

## Schema Expectations

Capture location belongs in the specification because it changes what an event
is allowed to mean. A browser event can represent intent, while a server event
can represent completion. The plan should state whether an event is required
from the client, the server, or both. It should also state whether the event
marks an attempted action or a completed business action.
[[cite:data-led-growth-event-tracking-and-reverse-etl@27:00=>Client-side and server-side tracking]]

That distinction matters when events feed [[metrics]]. The plan should tell a
team which event was supposed to fire, where it should fire, and which
properties explain the source. A vague specification can make failed form
submissions, low-quality traffic, and completed accounts look like the same
product behavior.
[[cite:data-led-growth-event-tracking-and-reverse-etl@18:27=>Data-led growth anomaly investigation]]

Teams can start with a spreadsheet or document when the event set is small. The
plan still comes before instrumentation. Avo, Iteratively, and TrackPlan are
collaborative tracking-plan tools for taxonomy and event-quality discussion.
Engineers still need to implement the events, but the plan should make the
expected capture rule reviewable before implementation.
[[cite:data-led-growth-event-tracking-and-reverse-etl@20:47=>Data-led growth tracking-plan tools]]

## Governance and Ownership

Tracking plans need owners because event definitions change as products change,
and ownership is part of the tracking-plan definition. Data engineers,
analysts, analytics engineers, and product operations all touch the stack.
Documentation and data literacy decide whether new team members can interpret
the events.
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth team structure]]

Governance starts with a small set of decisions. The team needs to decide who
can add an event, who reviews the name and properties, and which engineer owns
implementation. It also needs a product or analytics owner who confirms the
meaning and downstream dependencies. When an event changes, the team needs a
notification path. Without those answers, a tracking plan can drift into stale
documentation while the product keeps changing.
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-led growth tracking-plan ownership]]

Before implementation, the plan should say who reviews the event name and who
checks required properties and types. It should also say who approves a
breaking change and who confirms that a deprecated event can be removed. Those
review steps keep naming, ownership, and analytics dependencies visible before
[[event tracking]] turns them into emitted data.

## Naming and Change Control

Kafka schemas and schema registries provide a platform analogy. Schemas and
schema registries help teams control event structure and allowed changes.
Product tracking plans do the same kind of work for analytics events. They make
change review explicit before downstream models, funnels, experiments, or
reverse ETL syncs depend on the event.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]
That platform analogy connects tracking plans to [[Streaming]].

Naming conventions turn the review into visible checks. A plan should prevent
duplicate names, inconsistent casing, vague verbs, and properties that repeat
the same idea under several labels. Change control needs the same discipline.
Before a product release changes the signal, the plan should name the owner
and affected consumers. It should also define the review path for a renamed
event, removed property, or changed capture rule.

Tracking plans are therefore a front-door [[data governance]] and
[[data quality and observability]] control. They don't replace downstream
checks in the modern data stack. Natalie Kwong's modern-stack discussion still
puts raw storage, ingestion guardrails, dbt models, and marts after collection.
She also covers BI work and cleanup.
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]]
The plan gives those later checks a definition to compare against before the
rest of the stack has to clean, model, or activate the events.

## Related Pages

Tracking plans define the event rules for [[event tracking]],
[[data-led-growth=>data-led growth]], [[product analytics]], and
[[experimentation-and-causal-inference=>experimentation]]. They also support
[[data activation]], [[reverse ETL]], and [[customer data platforms]] when
product behavior reaches operational tools.

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
