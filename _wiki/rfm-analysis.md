---
layout: wiki
title: "RFM Analysis"
summary: "How podcast discussions ground RFM analysis in customer segmentation, retention decisions, analytics engineering, and warehouse-modeled product data."
related:
  - Product Analytics
  - Analytics Engineering
  - Data Warehouse
  - dbt
  - Event Tracking
  - Tracking Plans
  - Data-Led Growth
  - Data Activation
  - Reverse ETL
  - A/B Testing
  - Metrics
  - Marketing to Analytics Engineering
---

RFM analysis segments customers by recency, frequency, and monetary behavior.
Recency asks how recently they acted. Frequency asks how often they act.
Monetary behavior asks how much value they create.

RFM connects
[[product analytics]],
[[analytics engineering]],
and [[data-warehouse=>data warehouses]] to
retention decisions.

A direct example puts RFM inside a larger user-behavior analysis project. The
work happens in a small BI and analytics engineering team supporting product
managers and experiments. It also covers KPI work, dashboards, and data-model
changes
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).

RFM is more than a marketing label because teams can model customer behavior
from it. Product and growth teams can use it when deciding who needs support,
incentives, onboarding, or deeper investigation.

## Behavior Segmentation

RFM turns customer actions into reusable recency, frequency, and value features.
Retention, experimentation, and growth-stack practices then interpret or test
those segments after they're built. RFM starts with observable behavior and ends
with a stakeholder choice, not just a ranked customer list.

In one team, "a big RFM analysis" ran as user-behavior analysis over several
months. The team experimented with options and presented insights. That work sat
next to product-team support, cohort sizing, A/B testing, and data-model updates
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).
That makes RFM adjacent to
[[metrics]] and
[[a-b-testing=>A/B testing]], because the segments
should feed decisions about product changes, campaigns, and retention
interventions.

The retention logic behind the same segmentation method separates acquisition
from retention. Non-contractual products may not have a clean churn event, so
teams model purchase or usage frequency. They ask whether a user's inactivity is
unusual for that user's normal behavior
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).
RFM is a simpler segmentation form of that question: recent high-frequency
customers and formerly high-value inactive customers shouldn't be treated as
the same population.

## Segments, Causality, and Intervention

The boundary around RFM falls in different places. When teams treat it as an
analytics and product insight project, RFM compares options and presents
findings. It also sits beside product analytics and KPI decisions
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).
That's the right scope when stakeholders need a shared segmentation language
and a reusable customer mart.

The retention question goes further because churn prevention needs more than
prediction. Teams need to know which users can actually be recovered and whether
a message, voucher, or other treatment helps. This connects to uplift modeling
and treatment-control design, where costs and long-term retention matter
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).
In that framing, RFM can be a baseline segmenter or feature set. It can't
replace an experiment when the team needs to know whether an intervention caused
the return.

A product experimentation boundary applies too. A/B tests establish whether a
change caused a business metric to move. That matters when revenue and retention
metrics are noisy
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).
RFM can identify promising segments. When a team tests a product or lifecycle
change, rollout decisions still need stable metrics, assignment tracking, and
enough observations.

Another boundary sits in the data stack. Product and growth teams need tracking
plans, documented events, warehouse storage, and transformation and activation
tools. Without those pieces they can't trust event-based decisions
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]).
For RFM, this means the segment is only as useful as the event and transaction
definitions behind it.

## Modeling RFM in the Warehouse

RFM analysis becomes durable when the team models it at the customer/account/user
grain instead of rebuilding it in spreadsheet exports. The table needs a clear
grain and agreed time windows. It also needs definitions for qualifying events
and inactive periods. Order, revenue, and refund definitions matter too.

Those choices connect RFM to [[dbt]] and
[[data warehouse]] work. They also
connect it to
[[business intelligence]].

Teams can reuse RFM only when they agree on the same customer/account/user
grain. They also need shared event and value definitions.

One stack used Snowplow for tracking and dbt for transformation. It used Looker
for reporting and Redshift/S3 for analytical storage. The dbt model held
transformation logic from staging layers through presentation tables used for
analysis
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).

An RFM model belongs in that same modeled layer when product managers and
analysts will reuse it for cohort sizing and dashboards. The same model can
support campaign readouts or customer lists.

In the growth-stack version, a warehouse stores large structured data where
teams create models, clean data, and analyze it in BI. That sits alongside
warehouse-centric product analytics and
[[reverse ETL]]. Reverse ETL sends cleaned
warehouse data to sales, marketing, support, and engagement tools
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]).

For RFM, start by building the segment in the warehouse and exposing it to BI
for analysis. Activate it downstream only after the definition is documented and
trusted.

## Event Tracking Before Segmentation

RFM is weak when recency and frequency come from vague or inconsistent events.
A team needs to know which event counts as activity, which account or user owns
the event, and which properties explain the behavior. Otherwise the same person
can look active in one tool and inactive in another.

A tracking plan is the strongest support because it documents event names,
properties, data types, and owners. It should also record source context and
whether an event is client-side or server-side. Teams avoid conflicting names
and confusing definitions when those events are documented for new product or
growth people
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]).
RFM work should therefore start near
[[event tracking]] and
[[tracking plans]], not only in a
BI layer.

SaaS examples include signup and email verification. They also include project
creation and invites, plus tasks and invoices. The first tracking plan narrows
to the events needed to understand the customer journey from acquisition to
activation
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]).

Those same choices determine what "recent" and "frequent" mean in an RFM model.
An invoice event supports monetary value. A project-created event may support
activation. A support or product-use event may support retention analysis.

## Retention and Lifecycle Decisions

RFM is most useful when it leads to different actions for different customer
states. A high-frequency customer who paused for a few days may need a different
decision than a low-frequency seasonal customer. A high-monetary customer with
falling recency may deserve a different escalation than a newly acquired user
who hasn't reached activation.

Non-contractual churn shows why a single inactivity rule isn't enough. The
signals differ in an app or marketplace. A user who orders every day and stops
for four days may be abnormal. A user who orders every Sunday hasn't shown the
same signal.
Seasonality and look-alike signals help avoid treating every inactive period as
churn
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

RFM gives analysts a simple, explainable starting point for that segmentation:
recency flags potential inactivity. Frequency gives each customer's baseline.
Monetary value helps prioritize attention.

The intervention still needs judgment. Sending every inactive user an email or
push notification can be naive or even damaging. Better teams learn which users
can be recovered, account for treatment costs, and measure long-term engagement,
not only a short voucher spike
([[cite:machine-learning-in-marketing-attribution-marketing-mix-modeling=>Marketing Data Science]]).

Use RFM to choose candidate segments. Use
[[experimentation]] and
[[experimentation and causal inference]]
when the team needs to know whether the action worked.

## Product, Marketing, and Stakeholder Use

RFM sits between product and marketing because both groups care about customer
journeys. In one case the stakeholders were product managers. A marketing
background still helped with funnels, touchpoints, and growth. It also helped
with retention, signups, and the user journey
([[cite:from-marketing-to-analytics-engineering-sql-dbt-career-switch=>Marketing to Analytics Engineering]]).

That's why RFM belongs next to
[[Marketing to Analytics Engineering]]
as well as product analytics. The method is easy for stakeholders to understand,
but the implementation depends on analytical modeling.

The stakeholder path extends beyond dashboards. Once event or product data is
available through
[[data activation]], teams can use
it for email, support, and sales workflows. They can also use it for engagement
and personalized product experiences.

Support sees what users did in the product, and sales can reach accounts with
meaningful product activity. Engagement teams can personalize experiences based
on earlier behavior
([[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth]]).

An RFM segment can support those workflows, but only when the team has agreed
what the score means and which action each segment should trigger.

A/B testing adds decision discipline because product teams can use expert
judgment to generate ideas. Experiments show whether a change improved revenue,
retention, conversion, or another chosen metric. Reacting too early to noisy
metrics or stakeholder pressure while an experiment is still running is a mistake
([[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]).
That matters for RFM because segment-specific messaging, discounts, onboarding,
or product changes can look plausible and still fail on the metric that matters.

## Related Pages

Use these pages for the adjacent product analytics, modeling, and activation
concepts:

- [[Product Analytics]]
- [[Analytics Engineering]]
- [[Data Warehouse]]
- [[dbt]]
- [[Event Tracking]]
- [[Tracking Plans]]
- [[data-led-growth=>Data-Led Growth]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[a-b-testing=>A/B Testing]]
- [[Metrics]]
- [[Marketing to Analytics Engineering]]
