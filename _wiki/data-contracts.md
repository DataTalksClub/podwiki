---
layout: wiki
title: "Data Contracts"
summary: "Data contracts as producer-consumer agreements for schemas, quality, ownership, service levels, and change review."
related:
  - Data Mesh
  - Data Products
  - Data Governance
  - Data Quality and Observability
  - DataOps
  - Self-Service Data Platforms
  - Streaming
  - Data Engineering Platforms
  - Data Product Management
---

Data contracts make a data interface explicit before downstream teams depend on
it. They describe what a producer publishes, what consumers can expect, who owns
the data, and how changes should happen. The strongest DataTalks.Club examples
come from [[Data Mesh]], [[self-service-data-platforms=>self-service data
platforms]], and [[data governance]] discussions.

The concept sits between [[Data Products]] and [[DataOps]]. A data product needs
consumer-facing guarantees, so DataOps has to make them reviewable and
testable. It also has to make them observable and recoverable. Andrew Jones's
[[book:20230807-driving-data-quality-with-data-contracts=>Driving Data Quality with Data Contracts]]
adds the book-length version. Define expectations before a pipeline runs, then
use them to catch data-quality failures earlier.

## Producer-Consumer Boundary

Data contracts start with a producer-consumer agreement. The producer exposes
an interface that other teams can trust. The consumer knows the schema and
quality expectations before using the data. Ownership path and service promise
belong in the same agreement.

[[person:zhamakdehghani=>Zhamak Dehghani]] frames this through
[[Data Mesh]]. A domain-owned data product isn't just a table or topic. It
needs ownership, metadata, quality expectations, and consumer-facing guarantees
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]].
The same boundary appears in [[data-product-management=>Data Product
Management]] because someone has to decide which consumer promise the product
should make.

This boundary matters because downstream users often experience data through
interfaces they don't control. The agreement lets them judge whether the
interface is fit for a decision. That connects contracts to
[[data-product-adoption=>Data Product Adoption]]. Users adopt data products
when they can find, understand, and trust them
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]].

## Schemas and Change Review

Contracts become concrete when teams publish schemas and change rules.
[[person:mehdiouazza=>Mehdi OUAZZA]] gives the streaming version. Software
engineers may push events to Kafka while data teams consume those events
downstream. The useful agreement names the schema and type system. It also
names the registry, allowed changes, and review process
[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Scaling Data Engineering Teams]].

Without that agreement, downstream teams inherit loose JSON, unexpected field
changes, and higher parsing or compute cost. The schema registry is only one
part of the answer. The agreement also tells producers which changes are safe.
It tells consumers where to look at the current version. That makes
[[Streaming]] a governance problem, not only a latency problem.

Warehouse tables and metric layers need the same visible change path. So do
[[Feature Stores]] and operational exports. [[DataOps Checks for Data
Pipelines]] covers the release checks. [[Data Quality and Observability]]
covers runtime signals after release.

Freshness, volume, and schema show
whether the interface still behaves as expected. Distribution and lineage add
impact context.

## Quality, SLAs, and Ownership

Data contracts aren't only schemas. In Data Mesh, they also express quality,
service levels, and ownership decisions. Dehghani connects the agreement
conversation to the data product owner or manager. That person talks to
consuming domains and decides whether the product should optimize for
low-latency events or higher-integrity sessions
[[cite:data-mesh-architecture-decentralized-data-products@52:48=>Data Mesh Implementation]].

That framing separates data contracts from static specifications. Consumers may
need timeliness, completeness, and integrity, while retention and access rules
can belong in the same agreement.

Producers need a way to say which promises they can support and which changes
require a review. The agreement should be visible enough for
[[Data Governance]] and [[DataOps]] to enforce.

Observability keeps the agreement honest after launch. Freshness and schema
signals show whether the interface still behaves as promised. Lineage shows
which downstream dashboards, features, or reports are affected when the
producer breaks the promise
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

## Platform Support

Contracts scale when the platform makes the supported path easier than ad hoc
data sharing. [[Self-Service Data Platforms]] give teams shared conventions,
schema rules, onboarding paths, and support channels. They also give producers
and consumers a place to discover current expectations
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]].
That makes contracts part of the broader
[[modern-data-engineering-trends=>Modern Data Engineering Trends]] shift toward
platform-enforced interfaces instead of informal warehouse handoffs.

Data Mesh adds a stronger platform requirement. Domain teams shouldn't rebuild
identity, authorization, and metadata machinery when validation and discovery
need shared support too.

Dehghani describes retention policy as a shared governance primitive.
Each product may choose a value, while the platform can still expose, validate,
and enforce the policy consistently
[[cite:data-mesh-architecture-decentralized-data-products@53:02=>Data Mesh Implementation]].

That places contracts near [[Data Engineering Platforms]], [[Platform
Engineering]], and [[data-architect-role=>Data Architect Role]]. The platform
should encode repeated rules. The domain team should own meaning, quality
choices, and consumer support. Use
[[data-mesh-vs-centralized-data-platform=>Data Mesh vs Centralized Data Platform]]
when the interface design raises a larger question. Those promises may belong
with domain data-product owners or with a central platform team.

The governance team should define shared policy.
When those responsibilities are separate, the agreement becomes an operating
interface instead of a document nobody maintains.

## Limits

Data contracts can't rescue an unclear product. Teams still need [[Data Product
Management]] and [[Data Strategy]] when nobody knows which decision the data
supports. They still need observability and incident ownership when nobody can
monitor the promised interface. They need governance before broad access is safe
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]]
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]].

Contracts also don't remove consumer responsibility. A dashboard or model still
needs to check lineage, freshness, and business meaning before using the data.
An AI feature needs the same check. The agreement gives consumers a starting
point. [[Data Quality and Observability]] and [[Data Trust and Strategy]] show
whether the data still supports the decision.

Use [[DataOps Checks for Data Pipelines]] for test and release gates. Use
[[Data Mesh]] for domain ownership and [[Self-Service Data Platforms]] for
platform conventions. On the product side, [[Data Products]], [[Data Product
Adoption]], and [[Data Product Manager Roadmap]] explain why the agreement has
to serve a real decision.

## Related Pages

Data contracts sit inside a wider ownership, reliability, and platform system.

- [[Data Mesh]]
- [[Self-Service Data Platforms]]
- [[Data Governance]]
- [[Data Quality and Observability]]
- [[DataOps]]
- [[Data Products]]
- [[Data Product Management]]
- [[Streaming]]
- [[Data Engineering Platforms]]
