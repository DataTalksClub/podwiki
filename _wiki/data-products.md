---
layout: wiki
title: "Data Products"
summary: "How DataTalks.Club guests describe data products as owned, discoverable, trustworthy data interfaces with users and guarantees."
related:
  - Data Product Management
  - Data Engineering Platforms
  - Data Mesh
  - Analytics Engineering
  - Business Intelligence
  - Data Quality and Observability
  - A/B Testing
---

A data product is a maintained output that helps someone make a decision or run
an operational workflow. It can be a table, event stream, dashboard, or API. It
can also be a model, identity-resolution tool, or activation flow. Guests don't
view it as finished just because data ends up in a warehouse.
When the maintained output is a dashboard, metric layer, or reporting workflow,
it overlaps with [Business Intelligence]({{ '/wiki/business-intelligence/' | relative_url }}).

DataTalks.Club guests use two closely related meanings. In
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
[Zhamak Dehghani](https://datatalks.club/people/zhamakdehghani.html) describes
domain-owned data products with discoverability and guarantees around quality,
latency, and ownership (34:36-39:36). In
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html),
[Caitlin Moorman](https://datatalks.club/people/caitlinmoorman.html) uses product
thinking for analytics outputs that people must find, trust, and use in real
decisions (8:48-26:36). Both views connect data products to
[data product management]({{ '/wiki/data-product-management/' | relative_url }}),
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}), and
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

## Consumer Commitments

Across the interviews, a data product has a consumer and a commitment. The
consumer may be another domain team, an analyst, or a marketing manager. It may
also be a support agent, recommendation API, or ML system. The commitment may be
a schema or an SLA. It may also be a metric definition, dashboard
interpretation, or business outcome.

Dehghani gives the strongest interface-oriented definition. Around 31:05 in
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
she says producers need enough metadata for other teams to discover and judge a
data product. Around 34:36-39:36, she adds consumer-first guarantees around
quality, integrity, and completeness. She also includes ownership and known
limits. That turns
[domain ownership]({{ '/wiki/data-mesh/' | relative_url }}) into a product
interface, not only a team chart.

Moorman gives the strongest usage-oriented definition. In
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html),
she argues that the work isn't complete when a team builds a dashboard or
ships a table. People still need to discover the output, understand it, trust
it, and connect it to a decision (24:13-34:00). This is why
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
belongs inside the definition rather than after it.

[Sara Menefee](https://datatalks.club/people/saramenefee.html) adds the product
manager view in
[How to Transition from Design to Data Product Manager](https://datatalks.club/podcast/product-designer-to-data-product-manager.html).
Her data product management discussion starts with customer discovery and
hypothesis formation (7:04). It then moves through quality, PII, and
compliance. SQL, documentation, and empathy also matter (19:38-56:08). A data
product therefore needs a user problem and an operating plan, not only a
technical owner.

## Architectural Scope

The DataTalks.Club discussions differ most in where they place the center of
gravity. Dehghani starts from architecture, where domain teams publish data
products so other teams can consume them without a central data team mediating
every request. Her episode connects data products to
[schema and quality agreements]({{ '/wiki/data-mesh/' | relative_url }}),
[federated governance]({{ '/wiki/governance/' | relative_url }}), and
[self-service platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
(13:20-17:10 and 41:58-53:02).

Moorman starts from decision behavior. A data product succeeds when it changes
how sales, marketing, or operations teams act. The same applies to product and
finance teams. She recommends
starting with the decision, then working backward to the data sources and
interface design. Teams also need the meeting rituals where the data will be
used (34:00-40:53 in
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).

[Anna Hannemann](https://datatalks.club/people/annahannemann.html) starts from
product ownership in data science. In
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-product-owner-vs-product-manager.html),
she separates product owner and product manager responsibilities (15:11-20:00).
She then grounds the role in recommender systems, price markdown modeling,
domain ownership, and portfolio decisions (22:08-53:09). Her version of a data
product often includes production ML and a business domain owner.

[Ioannis Mesionis](https://datatalks.club/people/ioannismesionis.html) frames data
products through an operating model. In
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html),
he describes intake, Definition of Done, and KPIs. He also includes fail-fast
checks, pilots, [A/B tests]({{ '/wiki/a-b-testing/' | relative_url }}), and
production rollout (14:00-27:25).
That version is
closest to [MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[product analytics]({{ '/wiki/product-analytics/' | relative_url }}), because
the product has to be validated and monitored after launch.

## Data Products in Data Mesh

In Data Mesh, a data product is the unit of ownership. Dehghani describes a
mesh as a graph of value exchange between domains. Producers publish data with
explicit schemas and guarantees. Consumers build on those interfaces (14:55-17:10 in
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).
The data product needs a stable interface because downstream teams shouldn't
reverse-engineer raw operational systems.

The interface includes more than schema. Dehghani names metadata,
discoverability, identity, and authentication as shared requirements.

She also includes retention, validation, quality signals, and automated
governance in the same platform layer
(31:05-32:04 and 49:25-53:02). Those requirements tie data products to
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

This is also where [data mesh vs centralized data platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }})
becomes a real design question. A centralized platform can provide storage,
lineage, access control, and workflow tooling. Data Mesh asks domain teams to
own the product meaning and consumer commitments while the platform removes
repeated infrastructure work.

## Product Ownership

Ownership is what separates a data product from shared data that nobody
maintains. In Dehghani's Data Mesh episode, the product owner negotiates with
consumers and decides what guarantees are realistic. The owner also handles
derived products when consumers need aggregates or specialized forms
(34:36-41:47). They have to understand both the domain and the consuming teams.

Menefee brings the same idea into the product manager role. She describes
customer discovery and product documentation as part of adopting data tools and
products. She also includes Slack help, pairing, and knowledge bases
(49:37-56:08 in
[How to Transition from Design to Data Product Manager](https://datatalks.club/podcast/product-designer-to-data-product-manager.html)).
Product ownership also links data products to the
[data product manager]({{ '/wiki/data-product-manager/' | relative_url }})
role.

Hannemann adds a useful distinction for ML-heavy data products. A product owner
may advocate for delivery teams and make tactical trade-offs. A product manager
may own broader strategy and problem selection (15:11-20:00 in
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-product-owner-vs-product-manager.html)).
When the product is a recommender system or markdown model, ownership also
includes metrics and model quality. It also includes domain knowledge and
operating cost.

## Platform Implications

Data products need platform support because each team shouldn't rebuild the
same ingestion and orchestration templates. Access, testing, and deployment also
need shared paths. In
[Scale Data Engineering Teams](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) describes the data
platform as a self-service layer for onboarding and scale (12:30). He later
argues that tools such as Airflow only become a platform when teams add
conventions, playbooks, templates, and best practices around them (17:22).

This platform view matters for data products because producers need paved paths.
If every new product needs a custom Airflow setup, custom access handling, and a
custom release path, domain ownership becomes too expensive. Mehdi's
platform/use-case split around 52:55 also explains why data teams divide time
between reusable capabilities and product-specific pipelines.

[Natalie Kwong](https://datatalks.club/people/nataliekwong.html) explains the
stack view in
[ETL vs ELT and the Modern Data Stack](https://datatalks.club/podcast/data-engineering-tools-modern-data-stack.html).
She distinguishes raw ingestion, transformations, and warehouses. She also
covers marts, orchestration, CDC, and reverse flows (15:30-35:42 and 45:59).

Her discussion shows why [modern data stack]({{ '/wiki/modern-data-stack/' | relative_url }})
choices determine which data products a team can maintain. A warehouse table or
dbt model may become a product interface. So can a dashboard or reverse ETL sync
when someone owns the consumer commitment.

## Activation and Adoption

Some data products aren't meant for analysts at all. In
[How to Build a Data-Led Growth Stack](https://datatalks.club/podcast/data-led-growth-event-tracking-and-reverse-etl.html),
[Arpit Choudhury](https://datatalks.club/people/arpitchoudhury.html) walks through
event tracking and tracking plans. He also covers warehouses and
transformations, then moves to [data activation]({{ '/wiki/data-activation/' | relative_url }})
(13:34-41:30).

At 30:03-37:25, the product is operational. Event and warehouse
data flows into support, sales, and engagement tools. Marketing tools get the
same operational data through reverse ETL.

Moorman's adoption advice explains why activation alone isn't enough. Teams
should start from the decision and design for personas. They should also test
low-fidelity prototypes and measure whether the product changes behavior
(26:21-45:35 in
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html)).
That keeps a data product from becoming a polished dashboard nobody uses.

Mesionis adds a validation sequence for ML and analytics products. His team uses
intake, KPIs, and Definition of Done before rollout. Pilots and A/B tests also
belong before rollout.
Stakeholder demos and monitoring plans continue the work afterward
(17:37-27:25 and 35:38-41:33 in
[Building Data Products at Scale](https://datatalks.club/podcast/building-data-products-lead-data-scientist.html)).
For ML products, this overlaps with [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
and [production]({{ '/wiki/production/' | relative_url }}).

## Reliability and Operations

A data product needs operating discipline after launch. In
[Mastering DataOps](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html),
[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) connects
data work to error reduction, deployment speed, and team productivity. He also
connects it to monitoring, tests, CI/CD, and end-to-end versioning
(6:42-12:50 and 33:47-51:21). Those
practices turn data product quality into a repeatable system rather than a
one-time QA pass.

Bergh's DataOps framing also exposes a common failure mode. A product can have
users and a strong business case. It can still lose trust if pipelines fail
silently, dashboards show stale numbers, or nobody owns remediation. That's why data
products sit near [DataOps]({{ '/wiki/dataops/' | relative_url }}),
[data observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}), and
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}).

## Adjacent Product Practices

Data products depend on role design, platform choices, activation paths, and
reliability practices.

These pages cover the main adjacent topics:

- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Mesh vs Centralized Data Platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
- [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
- [Data Activation]({{ '/wiki/data-activation/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Product Manager]({{ '/wiki/data-product-manager/' | relative_url }})
