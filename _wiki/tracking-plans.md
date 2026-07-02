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

[[person:arpitchoudhury|Arpit Choudhury]] gives the most
direct DataTalks.Club definition in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|How to Build a Data-Led Growth Stack]].
At 13:34, he starts the growth stack with a tracking plan. Teams document each
event and event property before they collect the data. They also document user
and account properties, data types, semantics, and ownership.

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

Arpit ties those rules to data skepticism at 10:45-18:27 in the
data-led-growth episode. A data-led professional should know where data comes
from and question whether it's accurate. A tracking plan gives that person the
context to investigate a signup spike. Real users and fake accounts are
different signals. So are a client-side button click and a server-side
completion event, even when a dashboard labels all of them as signup.

[[person:nataliekwong|Natalie Kwong]] explains the
warehouse reason in
[[podcast:data-engineering-tools-modern-data-stack|ETL vs ELT and the Modern Data Stack]].
At 17:55-21:22, she discusses raw storage, ingestion guardrails, and governance.
Product events need enough meaning to support warehouse layers, dbt models,
data marts, and BI work. Her cleanup discussion at 43:02-43:45 makes stale or
unused data a quality concern, which is why tracking-plan decisions shouldn't
stop at the collection tool.

[[person:mehdiouazza|Mehdi OUAZZA]] gives the platform
analogy in
[[podcast:scaling-data-engineering-teams-self-service-platforms|Scaling Data Engineering Teams]].
At 23:26, he discusses Kafka schemas and schema registries. He also covers
allowed changes and change review. Tracking plans apply the same discipline to
product analytics. Teams need explicit agreements before event data becomes a
dependency for models, dashboards, experiments, or operational tools.

## Event Names and Properties

Event naming is the first visible part of a tracking plan. At 24:43, Arpit
uses SaaS examples such as signup, email verification, and project creation.
He also mentions teammate invitations, task creation, client creation, and
invoice creation
([[podcast:data-led-growth-event-tracking-and-reverse-etl|24:43|data-led growth]]).
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
and data types. Those details let analysts segment a funnel by acquisition
channel or plan type. They can also use account size, device, or source without
reverse-engineering the event later.

## Capture Location

Capture location is part of the definition, not an implementation footnote.
Arpit's `signup` example shows why: a browser event can represent intent, while
a server event can represent completion. At 27:00, he says client-side events
fit clicks, page interactions, and other user-interface behavior. Server-side
events fit completed actions such as successful signup or project creation
([[podcast:data-led-growth-event-tracking-and-reverse-etl|client-side and server-side tracking]]).

That distinction matters when events feed [[metrics]].
At 18:27, Arpit uses fake signups as an anomaly example. A team investigating a
spike needs to know which event fired, where it fired, and which properties can
explain the source. A vague event name can make failed form submissions,
low-quality traffic, and completed accounts look like the same product
behavior.

## Product Analytics and Experiments

Tracking plans feed [[product analytics]]
because product analytics tools need consistent event names and properties.
Arpit places product analytics after collection and storage. At 22:50-30:03, he
moves from the tracking plan into collection and warehouse storage.

Product analytics and BI use the same documented product events. Teams can study
acquisition and activation. They can also study retention and engagement
([[podcast:data-led-growth-event-tracking-and-reverse-etl|collection-to-analysis flow]]).

Product analytics also gives the tracking plan a practical test. If analysts
can't use the documented event to build a funnel, cohort, or activation metric,
the event definition is still too vague.

Tracking plans also sit behind experimentation. In
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]],
[[person:jakobgraff|Jakob Graff]] explains that
experiments need randomization and assignment tracking. They also need stable
metrics and power analysis.

At 24:44-37:44, those concerns depend on knowing which events mark assignment
and exposure. Teams also need clear outcome events. A tracking plan doesn't
replace experiment design, but it gives experiment metrics a cleaner event
base. The related measurement pages are
[[a-b-testing|A/B Testing]] and
[[Experimentation and Causal Inference]].

## Data Quality Control

A tracking plan is also a data-quality control. It reduces duplicate event
names, inconsistent casing, and vague meanings. It also reduces missing owners
and undocumented capture points.

Natalie's modern-stack discussion shows what happens after collection: at
17:55-21:22, she describes raw-data guardrails and governance, and at 43:02 she
recommends cleanup of unused data. Product events therefore need front-door
documentation through the tracking plan. Later,
[[data quality and observability]],
[[data-quality-and-observability|data observability]], and
[[DataOps]] keep the modeled data usable
([[podcast:data-engineering-tools-modern-data-stack|modern data stack discussion]]).

Teams can start with a spreadsheet or document when the event set is small.
Arpit still recommends creating the plan before instrumentation. At 20:47, he
mentions Avo, Iteratively, and TrackPlan as collaborative tracking-plan tools.
Those tools help teams discuss taxonomy and event quality. Engineers still need
to implement the events and confirm where each event should fire.

## Activation and Reverse ETL

Tracking plans become more important when product events leave dashboards and
drive operational systems. Arpit defines activation at 30:03 as making product
data available in support, sales, engagement, and product experiences. Support
teams can see customer usage before replying to a ticket. Sales teams can
prioritize accounts. Growth teams can trigger messages or personalize
onboarding
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).

[[Reverse ETL]] sends warehouse data
back into operational systems. At 37:25, Arpit names Census, Hightouch, and
Grouparoo for this job.

Natalie gives the data engineering version at 35:42-39:06 in the modern-stack
episode. She describes warehouse tables moving back into source systems or
business tools. In both cases, bad event definitions can become bad
customer-facing actions.

[[Customer data platforms]]
create a related path. At 38:20, Arpit describes CDPs as bundled systems for
collection, segmentation, and activation. A tracking plan still matters in that
setup because the CDP can only segment and activate the events the team
defined and collected.

## Governance and Ownership

Tracking plans need owners because event definitions change as products change.
Arpit includes ownership in the tracking-plan definition at 13:34 and returns
to team structure at 46:13-56:08. Data engineers, analysts, analytics
engineers, and product operations all touch the stack. Documentation and data
literacy decide whether new team members can interpret the events
([[podcast:data-led-growth-event-tracking-and-reverse-etl|data-led growth episode]]).

Governance starts with a small set of decisions. The team needs to decide who
can add an event, who reviews the name and properties, and which engineer owns
implementation. It also needs a product or analytics owner who confirms the
meaning. When an event changes, the team needs a notification path. Without
those answers, a tracking plan can drift into stale documentation while the
product keeps changing.

Mehdi's Kafka discussion gives a useful platform analogy. At 23:26 in the
scale-up episode, schemas and schema registries help teams control event
structure and allowed changes. Product tracking plans do the same kind of work
for analytics events. They make change review explicit before downstream
models, funnels, experiments, or reverse ETL syncs depend on the event.

## Adjacent Topics

Tracking plans are a small page in a larger measurement system. They define the
event layer for [[event tracking]],
[[data-led-growth|data-led growth]], and
[[product analytics]]. They also
support [[data activation]],
[[reverse ETL]], and
[[customer data platforms]]
when product behavior reaches operational tools.

- [[Event Tracking]]
- [[data-led-growth|Data-Led Growth]]
- [[Product Analytics]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[Customer Data Platforms]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[data-quality-and-observability|Data Observability]]
- [[a-b-testing|A/B Testing]]
- [[Streaming]]
