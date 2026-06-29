---
layout: wiki
title: "Product Analytics"
summary: "How the podcast archive connects product analytics to event tracking, metrics, experimentation, activation, and product decision-making."
related:
  - Data-Led Growth
  - Event Tracking
  - Tracking Plans
  - A/B Testing
  - Experimentation and Causal Inference
  - Data Activation
---

Product analytics studies product usage so teams can improve activation,
retention, engagement, and monetization. In the podcast archive, product
analytics is broader than funnel reporting: it starts with
[event tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[tracking plans]({{ '/wiki/tracking-plans/' | relative_url }}). It becomes more
reliable through [metrics]({{ '/wiki/metrics/' | relative_url }}) and
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}). Teams get more value
when they connect the findings to product decisions.

Across these episodes, guests treat product analytics as a bridge between
product work and the modern data stack. Arpit Choudhury connects product
analytics to documented events and collection choices. He then follows the data
into warehouses, BI, customer data platforms, and reverse ETL in the
[data-led growth episode at 13:34-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}).
Jakob Graff adds that product analytics is a causal decision discipline when it
is used for experiments. His discussion covers randomization, metric design,
and power analysis in
[the A/B testing episode at 5:11-37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}).

Use this page as the center for product usage analysis. For growth systems, use
[Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }}). For product
signals in operational tools, use
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}). For analytics
outputs that change decisions, use
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).

## Link Map

Start with these podcast discussions:

- [Arpit Choudhury on data-led growth, event tracking, and reverse ETL]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }}) explains how product analytics depends on event definitions, properties, collection tools, warehouses, BI, CDPs, and activation.
- [Jakob Graff on product analytics and A/B testing]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }}) shows why product analytics needs randomization, assignment tracking, A/A tests, metric stability, and power analysis before teams trust experiment results.
- [Nikola Maksimovic on moving from marketing to analytics engineering]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }}) places product analytics inside analytics engineering. That work uses SQL, dbt, Looker, Redshift, Snowplow, dashboards, growth analysis, retention analysis, RFM analysis, and A/B testing.
- [Sara Menefee on becoming a data product manager]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }}) connects analytics to customer discovery, hypothesis formation, data quality, documentation, SQL literacy, and product lifecycle decisions.
- [Caitlin Moorman on last-mile data delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}) explains why technically correct analytics still fail when they're not discoverable. Teams also need trust, interpretation, and decision context.

Guest pages:

- [Arpit Choudhury]({{ '/people/arpitchoudhury/' | relative_url }})
- [Jakob Graff]({{ '/people/jakobgraff/' | relative_url }})
- [Nikola Maksimovic]({{ '/people/nikolamaksimovic/' | relative_url }})
- [Sara Menefee]({{ '/people/saramenefee/' | relative_url }})
- [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})

Adjacent wiki pages:

- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})

## Common Definition

Across the archive, product analytics means turning product behavior into
decisions. Teams first define the product question. Then they choose events and
properties that represent the behavior. They collect the data consistently and
model it where needed.

They use the result for funnels, cohorts, and
dashboards. Experiments, activation, and product planning use the same product
behavior base.

Choudhury's growth-stack discussion gives the infrastructure version of that
definition. He starts with [tracking plans]({{ '/wiki/tracking-plans/' | relative_url }})
for event names and properties. The plan also records ownership and collection
context before product analytics tools enter the picture
([data-led growth at 13:34-24:43]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).
He then follows the same events into warehouses and BI analysis. Product
analytics tools, activation systems, reverse ETL, and CDPs use the same event
base
([data-led growth at 28:52-41:30]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Graff gives the measurement version. Product analytics can describe behavior,
but product decisions often need causal evidence. His episode moves from
econometrics into product analytics. He explains experiments through
randomization, external noise control, and revenue metric design. Assignment
tracking, A/A testing, metric stability, and power analysis
complete the measurement work
([product analytics and A/B testing at 5:11-37:44]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

The role-oriented episodes add that product analytics is shared work. Maksimovic
describes product support and dashboards as part of an analytics engineering
role. Growth analysis, retention analysis, RFM work, and A/B tests sit in the
same role
([marketing to analytics engineering at 14:14 and 38:27]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).
Menefee describes a data product manager using customer discovery and
hypotheses. SQL, data-quality awareness, and documentation literacy help turn
data into product choices
([data product manager at 7:04-26:33]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

## Disagreements and Boundaries

Choudhury is the most stack-oriented. He treats product analytics as one part
of a data-led growth system. Event collection and warehouse storage matter.
Transformation, BI, product analytics, and CDP choices also matter. Reverse ETL
and team ownership affect whether product teams can use behavioral data
([data-led growth at 22:50-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Graff is the most inference-oriented. For him, product analytics is unreliable
when teams skip randomization checks or choose noisy metrics. It also breaks
when teams ignore business cycles or underpower tests. His guidance is narrower
than "analyze usage."
Use experimentation to learn what caused a change, not just what changed
([product analytics and A/B testing at 8:13-40:23]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

Maksimovic connects product analytics with
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
SQL, dbt, Looker, and Redshift support product and growth analysis. Snowplow,
dashboarding, and data modeling support the same work
([marketing to analytics engineering at 18:34-30:28]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Menefee and Moorman focus more on product judgment and adoption. Menefee starts
from customer discovery and hypothesis formation. She also covers data quality
and PII. Compliance, SQL, and the data lifecycle sit in the same product role
([data product manager at 7:04-28:30]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Moorman starts from whether the analysis becomes usable in a decision. Adoption
depends on trust, interpretability, and personas. Teams support that adoption
with outcome-first design, meeting rituals, and narrow slices of measurable
impact
([last-mile data delivery at 20:02-45:35]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

## Instrumentation Before Analysis

Across these episodes, product analytics starts before a dashboard or vendor
tool. Choudhury recommends a tracking plan for event names, properties, and
owners. It also records data types, source context, and capture locations.
His SaaS examples include signup, project creation, invites, and invoices. He
distinguishes client-side from server-side events by timing, accuracy, and use
case
([data-led growth at 13:34-28:52]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

[Event Tracking]({{ '/wiki/event-tracking/' | relative_url }}) and
[Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }}) are prerequisites
for trusted product analytics. The same growth-stack episode uses anomaly
investigation to show the practical value. Teams need to know where an event
came from before they judge a spike. That source context also helps them check
whether a funnel drop or fake-signup case is real
([data-led growth at 18:27-20:47]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Metrics, Funnels, and Experiments

Product analytics is strongest when descriptive usage metrics connect to a
decision method. Graff's episode treats [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
and [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
as the step from "users behaved differently" to "this change caused the
difference." He uses randomization and traffic splitting. Assignment tracking
and A/A tests validate the experiment system before teams interpret product
results
([product analytics and A/B testing at 8:13-30:05]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

Metric design is part of the product decision, not a reporting afterthought.
Graff's subscription-versus-points example shows that revenue metrics can change
the interpretation of a product test. His later sections cover stability and
seasonality. They also cover sample size, duration, and distribution checks
before teams act on a result
([product analytics and A/B testing at 14:27-44:39]({{ '/podcasts/ab-testing-and-product-experimentation/' | relative_url }})).

Maksimovic shows the analytics-engineering side of the same work. Product
analytics at Ecosia included growth analysis, retention analysis, and RFM
analysis. It also included NLP experiments, dashboards, and A/B testing support.
SQL, data modeling, and dbt backed that work. Looker, Redshift, and Snowplow
also appear in the same tooling story
([marketing to analytics engineering at 14:14-23:12 and 38:27-39:36]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

## Warehouse, BI, and Product Analytics Tools

Guests don't draw a hard wall between product analytics tools and
[BI]({{ '/wiki/analytics-engineering/' | relative_url }}) work. Choudhury places
product analytics beside warehouses, transformations, and BI tools. Data
collection platforms, reverse ETL, and CDPs sit nearby. Product analytics tools
make common behavioral questions easier, but warehouses and BI remain important
for joins. They also support governed definitions, custom metrics, and broader
reporting
([data-led growth at 28:52-41:30]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Maksimovic's transition episode shows why this overlap matters in practice. His
analytics engineering work included Looker reporting and dbt migration.
Redshift, Airflow, Airbyte, and Snowplow appear in the same stack. He also
discusses wide-versus-narrow modeling choices and incrementalization tradeoffs.
Those aren't separate from product analytics when product teams depend on
governed dashboards, retention metrics, and experiment readouts
([marketing to analytics engineering at 18:34-33:46]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

Teams trade tool speed against metric control. Product analytics tools can help
product and growth teams ask self-serve behavioral questions.
Warehouse-centric work gives stronger control over transformations and joins.
It also gives stronger control over lineage and metric governance, but it asks
more from analysts, analytics engineers, and data engineers
([data-led growth at 35:27-46:13]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

## Activation and Last-Mile Adoption

Product analytics becomes operational when product events leave the dashboard.
Choudhury describes sending event data to support, sales, engagement, and
onboarding tools through activation and reverse ETL. The same behavioral data
that powers funnels can also personalize lifecycle messages, enrich CRM records,
or provide support context
([data-led growth at 30:03-41:30]({{ '/podcasts/data-led-growth-event-tracking-and-reverse-etl/' | relative_url }})).

Moorman adds that usage isn't guaranteed after data is delivered. Teams still
need discoverability, interpretability, trust, and decision context. Her last
mile framing treats analytics as a data product. Start with the outcome and map
the decision. Then prototype low-fidelity interfaces, embed metrics in meetings,
and build advocacy through narrow measurable wins
([last-mile data delivery at 8:48-45:35]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

For the operational side, use
[Data Activation]({{ '/wiki/data-activation/' | relative_url }}) and
[Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }}). For product framing,
use [Data Products]({{ '/wiki/data-products/' | relative_url }}) and
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}).
Across these episodes, teams work backward from the decision and then choose the
simplest analytics, activation, or product surface that preserves trust.

## Product Roles and Discovery

Product analytics isn't owned by one title in the archive. Menefee's data
product manager episode shows a product-side version. The PM uses customer
discovery to form hypotheses and works through product lifecycle planning with
engineering. They also need data-quality awareness, compliance awareness, SQL,
and enough data-engineering literacy to collaborate with technical teams
([data product manager at 7:04-28:30]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Menefee also makes documentation and empathy part of the role. She describes
daily work across standups, analytics, and customer development. She also
covers product documentation, PRDs, and customer notes. Knowledge bases,
backlog validation, and context switching round out the role
([data product manager at 46:01-60:40]({{ '/podcasts/product-designer-to-data-product-manager/' | relative_url }})).

Maksimovic shows the analyst or analytics engineer side. Domain knowledge from
marketing helped him understand funnels, user journeys, and stakeholder needs.
SQL, dashboards, dbt, and modeling turned that context into reusable analytics
([marketing to analytics engineering at 39:36-45:09]({{ '/podcasts/from-marketing-to-analytics-engineering-sql-dbt-career-switch/' | relative_url }})).

## Related Pages

Useful adjacent pages:

- [Data-Led Growth]({{ '/wiki/data-led-growth/' | relative_url }})
- [Event Tracking]({{ '/wiki/event-tracking/' | relative_url }})
- [Tracking Plans]({{ '/wiki/tracking-plans/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
- [Experimentation and Causal Inference]({{ '/wiki/experimentation-and-causal-inference/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Reverse ETL]({{ '/wiki/reverse-etl/' | relative_url }})
- [Customer Data Platforms]({{ '/wiki/customer-data-platforms/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
