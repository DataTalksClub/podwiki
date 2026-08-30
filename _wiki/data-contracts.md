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
needs ownership, metadata, quality expectations, and consumer-facing guarantees.
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]]
The same boundary appears in [[data-product-management=>Data Product
Management]] because someone has to decide which consumer promise the product
should make.

This boundary matters because downstream users often experience data through
interfaces they don't control. The agreement lets them judge whether the
interface is fit for a decision. That connects contracts to
[[data-product-adoption=>Data Product Adoption]]. Users adopt data products
when they can find, understand, and trust them.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data Delivery]]

## Schemas and Change Review

Contracts become concrete when teams publish schemas and change rules.
[[person:mehdiouazza=>Mehdi OUAZZA]] gives the streaming version. Software
engineers may push events to Kafka while data teams consume those events
downstream. The useful agreement names the schema and type system. It also
names the registry, allowed changes, and review process.
[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Scaling Data Engineering Teams]]

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
low-latency events or higher-integrity sessions.
[[cite:data-mesh-architecture-decentralized-data-products@52:48=>Data Mesh Implementation]]

That framing separates data contracts from static specifications. Consumers may
need timeliness, completeness, and integrity, while retention and access rules
can belong in the same agreement.

Producers need a way to say which promises they can support and which changes
require a review. The agreement should be visible enough for
[[Data Governance]] and [[DataOps]] to enforce.

Observability keeps the agreement honest after launch. Freshness and schema
signals show whether the interface still behaves as promised. Lineage shows
which downstream dashboards, features, or reports are affected when the
producer breaks the promise.
[[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

## Platform Support

Contracts scale when the platform makes the supported path easier than ad hoc
data sharing. [[Self-Service Data Platforms]] give teams shared conventions,
schema rules, onboarding paths, and support channels. They also give producers
and consumers a place to discover current expectations.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scaling Data Engineering Teams]]
That makes contracts part of the broader
[[modern-data-engineering-trends=>Modern Data Engineering Trends]] shift toward
platform-enforced interfaces instead of informal warehouse handoffs.

Data Mesh adds a stronger platform requirement. Domain teams shouldn't rebuild
identity, authorization, and metadata machinery when validation and discovery
need shared support too.

Dehghani describes retention policy as a shared governance primitive.
Each product may choose a value, while the platform can still expose, validate,
and enforce the policy consistently.
[[cite:data-mesh-architecture-decentralized-data-products@53:02=>Data Mesh Implementation]]

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

## A First-Contract Rollout

A first contract should be a small, end-to-end, business-driven pilot rather
than an attempt to redesign every data interface. The Data Mesh adoption advice
starts with a readiness assessment, allies, and a use case touching one or two
domains. It recommends collaborative ways of working before teams become fully
autonomous, and warns against beginning with a use case that depends on every
domain at once.[[cite:data-mesh-architecture-decentralized-data-products@57:27=>Data Mesh Implementation]]

### Start With One Decision

Before writing a schema, name the producer domain, consumer, data asset, and
decision that the consumer needs to make. Record the current path and the
smallest useful slice of data. Data as a product starts from the consumer's
needs: the producer has to understand what users need to know in order to judge
whether the data is usable.[[cite:data-mesh-architecture-decentralized-data-products@34:59=>Data Mesh Implementation]]

Use the first conversation to choose the right tradeoff instead of promising
everything. A low-latency event stream may be right for operational monitoring,
while another consumer may need a slower but higher-integrity aggregate. That
choice determines the contract's freshness, completeness, and integrity
guarantees, as well as who should build the derived product.[[cite:data-mesh-architecture-decentralized-data-products@39:36=>Data Mesh Implementation]]

### Write The Minimum Contract

Capture the agreement in a versioned record that a producer and consumer can
review together. At minimum, include:

1. the asset, grain, keys, schema, types, and current version;
2. freshness or delivery target, completeness and integrity expectations, and
   known limitations;
3. the changes that are compatible, the changes that require consumer review,
   and the location of the latest version;
4. producer, consumer, accountable owner, support contact, retention, and
   access expectations; and
5. the check, notification, and recovery path when a promise is missed.

The streaming example makes the change rules concrete: use typed schemas and a
registry, publish the current version, and state which schema changes are
allowed and how they are reviewed. Without that guideline, an apparently easy
JSON change can create parsing and compute problems for downstream teams.
[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Scaling Data Engineering Teams]]
The broader Data Mesh contract also exposes guarantees such as quality, time
limits, integrity, and completeness, and treats them as values that can change
as consumer needs change.[[cite:data-mesh-architecture-decentralized-data-products@34:59=>Data Mesh Implementation]]

### Put The Contract In The Delivery Path

Keep the contract, implementation, and checks under version control. Add
compatibility and data-quality tests before release, then run regression or
impact tests when a producer changes the interface. The DataOps sequence is
explicit about version control, production checks, and testing a development
change for downstream impact; realistic, immutable test data makes an
end-to-end replay more trustworthy.[[cite:dataops-automation-and-reliable-data-pipelines@33:47=>Mastering DataOps]][[cite:dataops-automation-and-reliable-data-pipelines@44:12=>Mastering DataOps]]

The GitOps episode describes a branch, merge request, dry run, approval, and
apply sequence for infrastructure. Applying that same sequence to a contract
change is a practical way to make compatibility results and ownership reviewable
before publication. Require the producer and consumer to review changes that
alter the promised interface; involve the platform or governance owner when a
shared seam, access rule, or policy changes.[[cite:dataops-and-gitops-best-practices-for-data-teams@26:21=>DataOps and GitOps for Data Teams]][[cite:data-mesh-architecture-decentralized-data-products@49:25=>Data Mesh Implementation]]

### Publish, Observe, And Recover

Publish the current contract beside the discoverable data product, not in a
private document. Consumers need the schema, guarantees, metadata, and access
path before they can self-assess the interface. Shared platform conventions can
make that discovery and onboarding repeatable while leaving the producer's
business meaning with the domain team.[[cite:data-mesh-architecture-decentralized-data-products@31:19=>Data Mesh Implementation]][[cite:scaling-data-engineering-teams-self-service-platforms@15:40=>Scaling Data Engineering Teams]]

At runtime, check the promises that can make the consumer's decision unsafe:
freshness, volume or completeness, schema, distribution, and lineage. A failed
check should block or quarantine the unsafe output, notify the named owner and
affected consumer, and point to a tested rerun, backfill, rollback, or warning
path. This is the operational boundary between a contract and a static schema:
DataOps discussions move teams from manual checklists toward automated checks,
fast diagnosis, and documented handoff so one person is not indispensable.
[[cite:dataops-automation-and-reliable-data-pipelines@38:01=>Mastering DataOps]][[cite:dataops-and-gitops-best-practices-for-data-teams@62:28=>DataOps and GitOps for Data Teams]]

### Check The Pilot Before Expanding

Treat the first contract as complete only when the consumer can find the current
version, make the intended decision, and tell whether the data is inside its
guarantees. The producer should be able to see failures, identify the affected
consumers, and change or recover the interface without relying on a hero. These
gates combine the consumer-first contract conversation with DataOps's definition
of a system that can be run, tested, changed, and handed off.[[cite:data-mesh-architecture-decentralized-data-products@34:59=>Data Mesh Implementation]][[cite:dataops-automation-and-reliable-data-pipelines@19:56=>Mastering DataOps]][[cite:dataops-automation-and-reliable-data-pipelines@38:01=>Mastering DataOps]]

Continue to a second consumer or domain when those gates hold and the pilot has
shown a real reduction in ambiguity or breakage. Stop and re-scope when there is
no named consumer decision, no producer accountable for the promise, no way to
test the end-to-end path, or no support for the required change and recovery
process. A successful first contract demonstrates a useful interface; it does
not by itself prove that the organization is ready for a fully decentralized
Data Mesh.[[cite:data-mesh-architecture-decentralized-data-products@57:27=>Data Mesh Implementation]]

The rollout should leave a small, reviewable bundle: a versioned contract record,
compatibility and quality checks with representative test data, an approved
change record, a consumer-facing discovery entry, and an owner-linked operating
runbook. Keep the next decision visible in the same bundle: expand the contract,
create a higher-integrity derived product, or stop until ownership and platform
support are ready.[[cite:scaling-data-engineering-teams-self-service-platforms@23:26=>Scaling Data Engineering Teams]][[cite:dataops-automation-and-reliable-data-pipelines@44:12=>Mastering DataOps]][[cite:data-mesh-architecture-decentralized-data-products@39:36=>Data Mesh Implementation]]

## Limits

Data contracts can't rescue an unclear product. Teams still need [[Data Product
Management]] and [[Data Strategy]] when nobody knows which decision the data
supports. They still need observability and incident ownership when nobody can
monitor the promised interface. They need governance before broad access is safe.
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh Implementation]][[cite:data-quality-data-observability-data-reliability=>Data Observability Explained]]

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
