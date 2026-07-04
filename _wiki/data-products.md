---
layout: wiki
title: "Data Products"
summary: "How data products work as owned, discoverable, trustworthy data interfaces with users and guarantees."
related:
  - Data Product Management
  - Data Engineering Platforms
  - Data Mesh
  - Analytics Engineering
  - Business Intelligence
  - Data Quality and Observability
  - A/B Testing
---

A data product is a maintained data output that helps someone make a decision
or run an operational workflow. It can be a table or event stream. It can also
be a dashboard, API, or model. Identity-resolution tools and activation flows
can also be data products. The output becomes a product only when someone owns
the consumer problem, quality expectations, release path, and adoption work.

The concept sits between [[Data Product Management]], [[Data Engineering
Platforms]], [[Analytics Engineering]], and [[Business Intelligence]]. When the
product is a domain-owned interface, it also sits close to [[Data Mesh]]. When
the product changes behavior in a business workflow, it depends on [[Data
Product Adoption]], [[Product Analytics]], and sometimes [[a-b-testing=>A/B
Testing]].

## Data Product Boundary

Across the cited episodes, a data product has a consumer and a commitment. The
consumer may be a domain team, analyst, marketing manager, or support agent. It
may also be a recommendation API or ML system. The commitment may be a schema,
SLA, metric definition, or dashboard interpretation. It may also be a quality
signal or business outcome.

In the data mesh definition, domain teams publish data products with enough
metadata and quality guarantees for other teams to discover and consume them
safely. Latency expectations, ownership, and known limits belong in that
interface too [[cite:data-mesh-architecture-decentralized-data-products=>Data
Mesh Implementation]]. That turns [[data-mesh=>domain ownership]] into a
product interface, not only a team chart.

The usage-oriented definition starts from analytics adoption. A dashboard or
table isn't finished when it reaches the warehouse. People still need to find
it, understand it, trust it, and connect it to a decision
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile
Data Delivery]]. This is why [[Data Product Adoption]] belongs inside the
definition rather than after launch.

For IoT products, teams start even earlier. Raw sensor streams become useful
only after the team understands the collection purpose and the business process.
The team also needs to know which pipeline or platform output should expose the
data
[[cite:remote-data-engineering-work-and-building-iot-platforms@24:04=>Remote Data Engineering and IoT Platforms]].

Data product management adds the product operating model. Customer discovery,
hypothesis formation, and data quality determine whether the team solves a real
user problem. PII and compliance matter too. SQL, documentation, and empathy
also matter
[[cite:product-designer-to-data-product-manager=>Product Designer to Data
Product Manager]].

## Different Centers of Gravity

The cited discussions place the center of gravity in different parts of the
work.

[[person:zhamakdehghani=>Zhamak Dehghani]] starts from architecture. Domain teams
publish data products so other teams can consume them without a central data
team mediating every request. That view connects data products to [[data
mesh=>schema and quality agreements]], [[governance=>federated governance]],
and [[data-engineering-platforms=>self-service platforms]]
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh
Implementation]].

[[person:caitlinmoorman=>Caitlin Moorman]] starts from decision behavior. A data
product succeeds when sales and marketing teams change how they act. The same
standard applies to operations, product, and finance teams. The work starts from
the decision, then works backward to the data sources and interface design. It
also works back to the meeting rituals where people will use the data
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile
Data Delivery]].

[[person:annahannemann=>Anna Hannemann]] starts from product ownership in data
science. Product owners and product managers make different tradeoffs, and
ML-heavy products such as recommender systems or markdown models need domain
ownership and portfolio decisions. They also need model-quality and operating
cost judgment
[[cite:building-data-products-product-owner-vs-product-manager=>Building Data
Products at Scale]].

[[person:ioannismesionis=>Ioannis Mesionis]] frames data products through an
operating model. Intake, Definition of Done, KPIs, and fail-fast checks happen
before pilots and A/B tests. Rollout, demos, and monitoring then turn analytics
and ML work into a managed product lifecycle
[[cite:building-data-products-lead-data-scientist=>Building
Data Products at Scale]].

## Data Products in Data Mesh

In [[Data Mesh]], the data product is the unit of ownership. Producers publish
data with explicit schemas and guarantees. Consumers build on those interfaces
instead of reverse-engineering raw operational systems
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh
Implementation]].

The interface includes more than schema. Metadata, discoverability, identity,
and authentication belong in the shared platform layer. Retention, validation,
quality signals, and automated governance belong there too
[[cite:data-mesh-architecture-decentralized-data-products=>Data
Mesh Implementation]]. Those requirements tie data products to [[Data
Governance]], [[Data Quality and Observability]], and [[Data Engineering
Platforms]].

Teams face the [[Data Mesh vs Centralized Data Platform]] choice when they
decide who owns meaning and who owns shared infrastructure. A centralized
platform can provide storage, lineage, access control, and workflow tooling.
Data mesh asks domain teams to own product meaning and consumer commitments
while the platform removes repeated infrastructure work.

## Product Ownership

Ownership separates a data product from shared data that nobody maintains. In
the data mesh version, the product owner negotiates with consumers and decides
which guarantees are realistic. The owner also handles derived products when
consumers need aggregates or specialized forms
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh
Implementation]].

The product-manager version puts discovery, documentation, education, and
support inside ownership. Data product teams use customer notes, PRDs, and
knowledge bases so people can adopt new data tools in daily work. Pairing and
Slack help support the same adoption work
[[cite:product-designer-to-data-product-manager=>Product Designer to Data Product
Manager]]. This connects the artifact to the [[Data Product Manager]] role and
the broader [[Data Product Management]] discipline.

ML-heavy data products add another ownership boundary. A product owner may
protect delivery and make tactical release tradeoffs. A product manager may own
broader strategy and problem selection. A domain owner may coordinate data
science work across product and business areas
[[cite:building-data-products-product-owner-vs-product-manager=>Building Data
Products at Scale]].

## Platform Implications

Data products need platform support because each team shouldn't rebuild
ingestion, orchestration, and access handling from scratch. Testing and
deployment need shared paths too. Self-service platforms give teams reusable
conventions and playbooks. They also provide templates and best practices around
tools such as Airflow
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data
Engineering Teams]].

That platform work matters because domain ownership becomes too expensive when
every data product needs a custom scheduler, access model, and release path. The
same platform can support reusable capabilities and product-specific pipelines
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data
Engineering Teams]].

The [[Modern Data Stack]] determines which data products a team can maintain.
Raw ingestion, transformations, warehouses, and marts set one boundary.
Orchestration, CDC, and reverse flows set another.

Teams use those boundaries to decide whether a table or dbt model can become a
stable product interface. A dashboard or reverse ETL sync can also become one
[[cite:data-engineering-tools-modern-data-stack=>ETL
vs ELT and the Modern Data Stack]].
IoT platform work shows the same platform implication in a physical-data
setting. Teams define the product surface through sensor onboarding and
registration as much as storage. Real-time processing and internal stakeholders
matter too
[[cite:remote-data-engineering-work-and-building-iot-platforms@31:04=>Remote Data Engineering and IoT Platforms]].

## Activation and Adoption

Some data products are operational rather than analytical. Event tracking,
tracking plans, warehouses, and transformations can push customer and product
data into support and sales tools. Reverse ETL can feed the same data into
engagement and marketing tools
[[cite:data-led-growth-event-tracking-and-reverse-etl=>Data-Led Growth Stack]].
That places data products near [[Data Activation]] and [[Reverse ETL]].

Activation alone doesn't prove adoption. Teams need personas, low-fidelity
prototypes, meeting rituals, and narrow wins. They also need impact measures
that show whether people changed behavior
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile
Data Delivery]].

ML and analytics products need validation before rollout. Intake, KPIs, and
Definition of Done set the early gate. Pilots, A/B tests, stakeholder demos, and
monitoring plans help teams decide whether a product is ready to operate
[[cite:building-data-products-lead-data-scientist=>Building Data Products at
Scale]]. For ML products, this overlaps with [[Model Monitoring]], [[MLOps]],
and [[Production]].

## Reliability and Operations

A data product needs operating discipline after launch. DataOps connects data
work to error reduction, deployment speed, and team productivity. Monitoring,
tests, CI/CD, and end-to-end versioning make those practices repeatable
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering
DataOps]].

That discipline protects trust because a product can have users and a strong
business case, then lose credibility when pipelines fail silently. Stale
dashboards and unclear remediation ownership create the same risk. Data products
therefore sit close to [[DataOps]], [[data-quality-and-observability=>Data
Quality and Observability]], and [[Model Monitoring]].

## Related Pages

These pages cover adjacent roles, platforms, operating practices, and adoption
work:

- [[Data Product Management]]
- [[Data Product Adoption]]
- [[Data Engineering Platforms]]
- [[Data Mesh]]
- [[Data Mesh vs Centralized Data Platform]]
- [[Modern Data Stack]]
- [[Analytics Engineering]]
- [[Data Activation]]
- [[Data Quality and Observability]]
- [[DataOps]]
- [[Data Product Manager]]
