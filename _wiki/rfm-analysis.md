---
layout: wiki
title: "RFM Analysis"
summary: "How DataTalks.Club podcast discussions place recency, frequency, and monetary analysis inside customer segmentation, retention, analytics engineering, product analytics, and warehouse modeling."
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

In DataTalks.Club discussions, RFM connects
[[product analytics]],
[[analytics engineering]],
and [[data-warehouse|data warehouses]] to
retention decisions.

The clearest direct example comes from
[[person:nikolamaksimovic|Nikola Maksimovic]] in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Marketing to Analytics Engineering]].
He describes RFM as a larger user-behavior analysis project run by a small BI
and analytics engineering team. The same team supported product managers,
experiments, and KPI work. It also handled dashboards and data-model changes
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|14:14-18:34]]).

RFM is more than a marketing label because teams can model customer behavior
from it. Product and growth teams can use it when deciding who needs support,
incentives, onboarding, or deeper investigation.

## Behavior Segmentation

In Maksimovic's direct RFM example, the method turns customer actions into
reusable recency, frequency, and value features. Retention, experimentation, and
growth-stack discussions then show how teams interpret or test those segments
after they're built. RFM starts with observable behavior and ends with a
stakeholder choice, not just a ranked customer list.

[[person:nikolamaksimovic|Nikola Maksimovic]] gives the
clearest direct RFM reference in the podcast discussions. His team ran "a big
RFM analysis" as user-behavior analysis, experimented with different options,
and presented insights over several months. He places that work next to
product-team support, cohort sizing, A/B testing, and data-model updates
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|14:20-18:34]]).
That makes RFM adjacent to
[[metrics]] and
[[a-b-testing|A/B testing]], because the segments
should feed decisions about product changes, campaigns, and retention
interventions.

[[person:juanorduz|Juan Orduz]] gives the retention
logic behind the same segmentation method in
[[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|Marketing Data Science]].
He separates acquisition from retention, then explains that non-contractual
products may not have a clean churn event. In those cases, teams model purchase
or usage frequency and ask whether a user's inactivity is unusual for that user's
normal behavior
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|23:04-28:14]]).
RFM is a simpler segmentation form of that question: recent high-frequency
customers and formerly high-value inactive customers shouldn't be treated as
the same population.

## Segments, Causality, and Intervention

Podcast guests draw the boundary around RFM in different places. Maksimovic's
example treats RFM as an analytics and product insight project. The team
compared options, presented findings, and used the work beside product analytics
and KPI decisions
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|14:14-18:34 and 38:27-41:50]]).
That's the right scope when stakeholders need a shared segmentation language
and a reusable customer mart.

[[person:juanorduz|Juan Orduz]] pushes the retention
question further. For churn prevention, he argues that prediction isn't enough
because teams need to know which users can actually be recovered. They also need
to know whether a message, voucher, or other treatment helps. He connects that
to uplift modeling and treatment-control design. Costs and long-term retention
matter in that design
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|29:13-34:12]]).

In that framing, RFM can be a baseline segmenter or feature set. It can't
replace an experiment when the team needs to know whether an intervention caused
the return.

[[person:jakobgraff|Jakob Graff]] adds the product
experimentation boundary in
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
He treats A/B tests as a way to establish whether a change caused a business
metric to move. That matters when revenue and retention metrics are noisy
([[podcast:ab-testing-and-product-experimentation|11:48-18:04 and 33:23-38:09]]).
RFM can identify promising segments. When a team tests a product or lifecycle
change, rollout decisions still need stable metrics, assignment tracking, and
enough observations.

[[person:arpitchoudhury|Arpit Choudhury]] puts the
boundary in the data stack. In
[[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth]],
he argues that product and growth teams need tracking plans, documented events,
and warehouse storage. They also need transformation and activation tools.
Without those pieces, they can't trust event-based decisions
([[podcast:data-led-growth-event-tracking-and-reverse-etl|13:34-22:50 and 35:56-41:30]]).
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

Maksimovic's team used Snowplow for tracking and dbt for transformation. The
same stack used Looker for reporting. Redshift/S3 handled analytical storage.
He describes the dbt model as transformation logic from staging layers through
presentation tables used for analysis
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|18:34-24:51]]).

An RFM model belongs in that same modeled layer when product managers and
analysts will reuse it for cohort sizing and dashboards. The same model can
support campaign readouts or customer lists.

[[person:arpitchoudhury|Arpit Choudhury]] gives the
growth-stack version. He says a warehouse stores large structured data where
teams create models, clean data, and analyze it in BI. He also describes
warehouse-centric product analytics and
[[reverse ETL]]. Teams can send
cleaned warehouse data to sales, marketing, support, and engagement tools
([[podcast:data-led-growth-event-tracking-and-reverse-etl|35:56-41:30]]).

For RFM, start by building the segment in the warehouse and exposing it to BI
for analysis. Activate it downstream only after the definition is documented and
trusted.

## Event Tracking Before Segmentation

RFM is weak when recency and frequency come from vague or inconsistent events.
A team needs to know which event counts as activity, which account or user owns
the event, and which properties explain the behavior. Otherwise the same person
can look active in one tool and inactive in another.

[[person:arpitchoudhury|Arpit Choudhury]]'s
tracking-plan discussion is the strongest support. He recommends documenting
event names, properties, data types, and owners. He also asks teams to record
source context and whether an event is client-side or server-side. He warns that
undocumented events create conflicting names and confusing definitions for new
product or growth people
([[podcast:data-led-growth-event-tracking-and-reverse-etl|13:34-21:16]]).
RFM work should therefore start near
[[event tracking]] and
[[tracking plans]], not only in a
BI layer.

His SaaS examples include signup, email verification, and project creation.
They also include invites, tasks, and invoices. Choudhury recommends narrowing
the first tracking
plan to the events needed to understand the customer journey from acquisition to
activation
([[podcast:data-led-growth-event-tracking-and-reverse-etl|22:50-28:52]]).

Those same choices determine what "recent" and "frequent" mean in an RFM model.
An invoice event supports monetary value. A project-created event may support
activation. A support or product-use event may support retention analysis.

## Retention and Lifecycle Decisions

RFM is most useful when it leads to different actions for different customer
states. A high-frequency customer who paused for a few days may need a different
decision than a low-frequency seasonal customer. A high-monetary customer with
falling recency may deserve a different escalation than a newly acquired user
who hasn't reached activation.

[[person:juanorduz|Juan Orduz]]'s non-contractual churn
discussion explains why a single inactivity rule isn't enough. In an app or
marketplace, a user who orders every day and stops for four days may be
abnormal. A user who orders every Sunday hasn't shown the same signal. He also
adds seasonality and look-alike signals as ways to avoid treating every inactive
period as churn
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|23:43-28:14]]).

RFM gives analysts a simple, explainable starting point for that segmentation:
recency flags potential inactivity. Frequency gives each customer's baseline.
Monetary value helps prioritize attention.

The intervention still needs judgment. Orduz warns that sending every inactive
user an email or push notification can be naive or even damaging. He argues for
learning which users can be recovered. He also asks teams to account for
treatment costs and measure long-term engagement, not only a short voucher spike
([[podcast:machine-learning-in-marketing-attribution-marketing-mix-modeling|28:31-34:12]]).

Use RFM to choose candidate segments. Use
[[experimentation]] and
[[experimentation and causal inference]]
when the team needs to know whether the action worked.

## Product, Marketing, and Stakeholder Use

RFM sits between product and marketing because both groups care about customer
journeys. Maksimovic says his current stakeholders were product managers, even
though his marketing background helped him reason about funnels and touchpoints.
It also helped him reason about growth, retention, signups, and the user journey
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|38:27-41:50]]).
That's why RFM belongs next to
[[Marketing to Analytics Engineering]]
as well as product analytics. The method is easy for stakeholders to understand,
but the implementation depends on analytical modeling.

Choudhury extends that stakeholder path beyond dashboards. Once event or product
data is available through
[[data activation]], teams can use
it for email, support, and sales. They can also use it for engagement and
personalized product experiences.

He gives examples where support sees what users did in the product. Sales can
reach accounts with meaningful product activity. Engagement teams can personalize
experiences based on earlier behavior
([[podcast:data-led-growth-event-tracking-and-reverse-etl|30:03-37:25]]).

An RFM segment can support those workflows, but only when the team has agreed
what the score means and which action each segment should trigger.

[[person:jakobgraff|Jakob Graff]]'s A/B testing
discussion adds the decision discipline. Product teams can use expert judgment
to generate ideas, but experiments help them learn whether a change improved
revenue or retention. Experiments can also test conversion or another chosen
metric. He warns against reacting too early to noisy metrics or stakeholder
pressure while an experiment is still running
([[podcast:ab-testing-and-product-experimentation|18:06-23:54 and 37:44-38:09]]).
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
- [[data-led-growth|Data-Led Growth]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[a-b-testing|A/B Testing]]
- [[Metrics]]
- [[Marketing to Analytics Engineering]]
