---
layout: wiki
title: "Product Analytics"
summary: "How DataTalks.Club guests connect product analytics to event tracking, metrics, experimentation, activation, and product decision-making."
related:
  - Data-Led Growth
  - Event Tracking
  - Tracking Plans
  - A/B Testing
  - Experimentation and Causal Inference
  - Metrics
  - Analytics Engineering
  - Business Intelligence
  - Data Product Management
  - Data Product Adoption
  - Data Activation
---

Product analytics studies how people use a product. Teams use it to improve
activation, retention, and product quality. They also use it to understand
engagement and monetization.

In these podcast discussions, product analytics starts with
[[event tracking]] and
[[tracking plans]]. Metrics and
[[a-b-testing|A/B testing]] make it more
trustworthy. Product teams use evidence to change roadmaps and experiments.
They also use it for onboarding, support, and lifecycle messaging.

Product managers share this work with analysts and analytics engineers. Data
engineers and data scientists contribute too.
When the same definitions become recurring dashboards or executive reporting,
the neighboring discipline is
[[Business Intelligence]].

In [[podcast:data-team-roles|Data Team Roles]],
the role discussion puts analysts next to product managers. The product
manager keeps the team close to the user. Analysts quantify the problem and later check
whether a shipped feature improved the posting flow or reduced wrong
categorization
([[podcast:data-team-roles|5:47-11:17]]). The later
episodes add the stack, inference, product-management, and adoption layers.

## Concept Scope

A practical definition has five parts:

- Teams define the product question, such as activation drop-off or roadmap
  priority.
- Teams instrument behavior with named events and properties. They record
  owners, source context, data types, and capture locations.
- Analysts and analytics engineers model product usage into funnels, cohorts,
  dashboards, and experiment metrics.
- Product and growth teams use [[experimentation]]
  or [[Experimentation and Causal Inference]]
  when they need to know whether a product change caused an outcome.
- Teams package the result so someone can make a decision, take an operational
  action, or adopt a [[data-products|data product]].

[[person:arpitchoudhury|Arpit Choudhury]] gives the
stack-oriented version in
[[podcast:data-led-growth-event-tracking-and-reverse-etl|Data-Led Growth, Event Tracking, and Reverse ETL]].
He follows product events from collection through storage, transformation,
analysis, and activation. Product analytics sits beside warehouses and BI. It
also sits beside customer data platforms and
[[reverse ETL]] because the same events
can support dashboards, growth analysis, and CRM enrichment. They can also add
support context and personalize onboarding
([[podcast:data-led-growth-event-tracking-and-reverse-etl|22:50-46:13]]).

[[person:jakobgraff|Jakob Graff]] gives the
inference-oriented version in
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing]].
Behavioral analysis can describe what changed, but product teams need
randomization checks and assignment tracking. They also need A/A tests, stable
metrics, and power analysis before they treat an experiment result as causal
evidence
([[podcast:ab-testing-and-product-experimentation|8:13-40:23]]).

## Instrumentation Before Analysis

Product analytics depends on event definitions before it depends on a charting
tool. Choudhury recommends tracking plans for event names, properties, owners,
and source context. Teams also record data types and capture locations. His
SaaS examples include
signup, project creation, invites, and invoices. He also separates client-side
and server-side events by timing, accuracy, and use case
([[podcast:data-led-growth-event-tracking-and-reverse-etl|13:34-28:52]]).

Product analytics therefore belongs near
[[Event Tracking]] and
[[Tracking Plans]], not under a
separate implementation-only topic. Teams can only trust a funnel drop, signup
spike, or activation metric when they can trace where the event came from.
In Choudhury's anomaly example, source context helps teams decide whether a
spike is real product behavior or a collection problem such as fake signups
([[podcast:data-led-growth-event-tracking-and-reverse-etl|18:27-20:47]]).

[[person:liesbethdingemans|Liesbeth Dingemans]] adds
the product-design side in
[[podcast:ai-ml-product-design-and-experimentation|AI Product Design]].
Algorithm-ready product experiences need interfaces that collect the right
signals. Her examples contrast interaction design with signal collection. She
then connects those signals to design sprints, parallel experiments, scoping
documents, and product roadmaps
([[podcast:ai-ml-product-design-and-experimentation|6:43-18:21]]).
For AI or ML products, instrumentation is part of the product design, not an
analytics task added after launch.

## Metrics And Experiments

Product analytics becomes decision-grade when teams connect descriptive usage
metrics to a decision method. Graff treats
[[a-b-testing|A/B Testing]] as the path from
"users behaved differently" to "this product change caused the difference."
His episode covers traffic splitting, assignment tracking, A/A tests, and
simple two-group designs before teams interpret results
([[podcast:ab-testing-and-product-experimentation|24:54-33:23]]).

[[Metrics]] include product assumptions, so
teams need to choose them before they celebrate a win. Graff's
subscription-versus-points example shows how a revenue metric can change the
interpretation of a product test. He also stresses noise, stability, and
seasonality. Teams need sample-size, duration, and distribution checks before
acting on a result
([[podcast:ab-testing-and-product-experimentation|14:27-44:39]]).

[[person:nikolamaksimovic|Nikola Maksimovic]] shows the
[[analytics engineering]]
version of the same work in
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|From Marketing to Analytics Engineering]].
Product analytics at Ecosia included product support, growth analysis,
retention analysis, and RFM work. It also included NLP experiments, dashboards,
and A/B testing. SQL and dbt backed those product questions. Looker and
Redshift supported the same work, as did Snowplow and data modeling
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|14:14-23:12 and 38:27-39:36]]).

## Product Roles And Ownership

Guests don't make one role own product analytics alone. In
[[podcast:data-team-roles|Data Team Roles]], product
managers prioritize and represent user needs. Analysts quantify the problem,
define KPIs, explain the data, and evaluate whether a feature worked
([[podcast:data-team-roles|5:47-11:17]]). That division
keeps product analytics close to both product judgment and statistical
measurement.

[[person:saramenefee|Sara Menefee's]]
[[podcast:product-designer-to-data-product-manager|Data Product Manager]]
episode connects product analytics to
[[Data Product Management]].
She frames data product work around customer discovery, hypothesis formation,
data quality, and compliance. SQL literacy, documentation, and lifecycle
context also matter, from data sources through warehouses and applications
([[podcast:product-designer-to-data-product-manager|7:04-28:30]]).
For product analytics, that means the product question and the data quality
question need to move together.

Dingemans makes the same cross-functional point for AI and ML products. She
argues for involving data scientists early in problem definition. Otherwise,
teams can discover too late that the product idea, signals, or interface can't
support the model. Product managers then use scoping documents, rapid
experiments, and data-driven pitches to decide which bets deserve investment
([[podcast:ai-ml-product-design-and-experimentation|25:00-35:00 and 46:30-56:36]]).

## Adoption And Activation

Product analytics doesn't end at a dashboard. Choudhury describes activation
work that sends product event data to support and sales tools. Teams can also
send it to onboarding and engagement systems through
[[Data Activation]] and reverse
ETL. The same events that power funnels can enrich CRM records, trigger
lifecycle messages, or give support teams product context
([[podcast:data-led-growth-event-tracking-and-reverse-etl|30:03-41:30]]).

[[person:caitlinmoorman|Caitlin Moorman's]]
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]
episode explains why technically correct analytics can still fail. Teams need
trust, discoverability, and interpretability. They also need data quality and
decision context.

Moorman recommends treating analytics as a product, with user research and
persona-driven design. Teams should start from the decision they need to make,
prototype low-fidelity interfaces, and embed metrics in meetings
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|24:13-39:32]]).
That places product analytics directly next to
[[Data Product Adoption]].

Moorman also connects product analytics to organizational behavior. Adoption
improves when teams scope narrow slices, recruit advocates, and prove impact
with measurable wins or practical proxy metrics
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|41:18-52:45]]).
Those constraints matter because a dashboard that nobody trusts or uses does
not improve the product.

## Boundaries

Use product analytics for product behavior, from events and funnels to cohorts
and activation. It also covers retention and feature use, plus user quality and
product experiments. Use
[[data-led-growth|Data-Led Growth]] when the page
needs the broader growth stack across collection, storage, and analysis. It
also covers activation and customer data infrastructure.

Use [[a-b-testing|A/B Testing]] or
[[Experimentation and Causal Inference]]
when the main question is causal design, power analysis, or randomization. They
also fit statistical testing and experiment interpretation. Use
[[Analytics Engineering]]
when the main question is modeling, transformations, semantic layers, or dbt.
It also fits warehouses and governed metrics.

Use
[[Data Product Management]]
and [[Data Product Adoption]]
when the main question is ownership, discovery, or lifecycle planning. They also
fit decision design and whether teams actually use the analytics.

## Related Pages

The closest adjacent pages are:

- [[Event Tracking]]
- [[Tracking Plans]]
- [[Metrics]]
- [[a-b-testing|A/B Testing]]
- [[Experimentation]]
- [[Experimentation and Causal Inference]]
- [[Analytics Engineering]]
- [[data-led-growth|Data-Led Growth]]
- [[Data Activation]]
- [[Reverse ETL]]
- [[Data Products]]
- [[Data Product Management]]
- [[Data Product Adoption]]
