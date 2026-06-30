---
layout: wiki
title: "Data Mesh vs Centralized Data Platform"
summary: "A podcast-grounded comparison of domain-owned data products and centralized platform ownership through architecture, governance, self-service, reliability, and organizational maturity."
related:
  - Data Mesh
  - Data Engineering Platforms
  - Self-Service Data Platforms
  - Data Products
  - Data Governance
  - DataOps
  - Platform Engineering
---

## Definition and Scope

Data Mesh is an operating model where business domains own the data products
they publish. In
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
[Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }}) frames it as a
decentralized socio-technical approach. Domains get autonomy, but the system
still needs interoperability. It also needs data contracts and metadata.
Identity, authorization, and federated governance are part of the same design.

Use
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}) for the full model and
[Data Products]({{ '/wiki/data-products/' | relative_url }}) for the product
interface.

A centralized data platform keeps more ownership in a shared data or platform
team. In
[DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) describes the
platform foundation through storage and compute. Workflow engines and
self-service analytics are part of that foundation. He also ties the platform
to lineage and versioning.
Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [DataOps]({{ '/wiki/dataops/' | relative_url }}) for that operating layer.

The comparison isn't "modern versus old." The podcast archive treats it as a
boundary decision about ownership. One side asks which teams own meaning, quality, data
contracts, and consumer support. The other asks which capabilities stay shared
so the organization doesn't duplicate governance or infrastructure work.

## Link Map

Use these pages for the main concepts in this comparison.

- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}) explains domain-owned
  data products, self-serve platforms, and federated governance.
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
  covers the shared platform stack for ingestion, orchestration, access, and
  support.
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
  covers the platform operating model behind safe autonomy.
- [Data Products]({{ '/wiki/data-products/' | relative_url }}) defines the
  consumer-facing interface that both models need.
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) covers
  ownership, catalogs, lineage, and access controls.
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
  covers the trust signals that make shared or domain-owned data usable.
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) and
  [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
  cover rollout, internal users, and paved paths.

These podcast discussions anchor the comparison.

- [Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }})
  with [Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }})
  is the archive's main domain-ownership discussion. It covers enterprise data
  friction at 7:35 and decoupled pipelines at 13:20. It then covers domain
  ownership at 16:34 and data as a product at 34:36. Self-serve platforms
  appear at 41:58. Platform federation appears at 47:35, and federated
  governance appears at 49:25.
- [DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})
  with [Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }})
  gives the central-platform caution. It covers platform primitives at 30:34
  and self-service analytics at 50:13. It then covers Data Mesh risks at 57:46
  and the centralize-or-split question at 1:03:02.
- [Scaling Data Engineering Teams and Self-Service Platforms]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})
  with [Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) shows how a
  platform team enables autonomy. The mechanisms are onboarding and Airflow
  conventions. Playbooks, Kafka schemas, schema registry practice, and data
  contracts support the same platform path.
- [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }})
  with [Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }})
  ties the comparison to catalogs, lineage, access requests, and ownership
  models. It also covers masking, filtering, review, and revocation.
- [Data Engineering Leadership and Modern Data Platforms]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})
  with [Rahul Jain]({{ '/people/16rahuljain/' | relative_url }}) adds the
  leadership view, covering stakeholder prioritization and data culture. Quality
  metrics, GDPR, role-based access control, and lineage are part of the same
  platform work.
- [Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
  with [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) keeps
  both architectures tied to adoption. Data outputs need discovery and trust,
  plus interpretation and decision use.

## Common Decision Rule

Use Data Mesh when the bottleneck is ownership and domain context. Zhamak
Dehghani's episode starts from long centralized pipelines to value. It moves
ownership toward domains that understand the data they produce
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
7:35 and 16:34). The model is strongest when domains can own product meaning
and quality expectations. They also need to own consumer support and data
contracts instead of sending every change through a central data backlog.

Use a centralized platform when the bottleneck is repeated infrastructure work.
The same applies when governance or reliability is the bottleneck. Lars
Albertsson's DataOps discussion places storage, compute, workflow engines, and
self-service analytics in the platform layer. He also connects that layer to
lineage and versioning
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
30:34 and 1:04:18). Central ownership of those capabilities can reduce
duplication and make operating practices easier to enforce.

The practical rule is hybrid: decentralize accountability for data products
when domains are ready to own them. Centralize or federate the capabilities
that every domain would otherwise rebuild. Zhamak's self-serve platform and
federated governance sections support that hybrid boundary
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
41:58-53:02). Mehdi OUAZZA's platform episode shows the same boundary through
Airflow conventions and data contracts
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
17:22 and 23:26).

## Guest Differences

Guests differ on where ownership should sit.

[Zhamak Dehghani]({{ '/people/zhamakdehghani/' | relative_url }}) puts the center
of gravity in domain ownership. Her argument is that data products should have
owners close to the producing domains. Those owners provide consumer-facing
guarantees and metadata. Quality signals, service levels, and support
expectations belong to the same product interface
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
31:05-39:36).

She still keeps a strong shared layer through self-serve platforms and platform
federation. The design also keeps automated governance.

[Lars Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) is more
cautious about splitting responsibilities. His DataOps discussion asks when
decentralization creates ownership and governance risk. Reproducibility is part
of the same concern
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
57:46-1:04:18). In his framing, a team shouldn't decentralize faster than its
workflow discipline can support. Lineage, versioning, and quality practices
matter before ownership splits.

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) starts from platform
enablement during scale-up growth. His episode treats self-service as a way to
onboard more contributors. That only works with conventions, playbooks, senior
engineering judgment and Kafka schema practice. Data contracts belong in that
path too
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26). That view supports domain autonomy only after the platform gives
teams a reliable path.

[Bart Vandekerckhove]({{ '/people/bartvandekerckhove/' | relative_url }}) shifts
the comparison toward access governance. His episode separates catalogs and
dictionaries from lineage and access controls. It also covers ownership models
plus approval, review, and revocation
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
8:58-32:08). A mesh can distribute ownership, but sensitive data still needs
shared controls such as masking and review.

[Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }}) adds the
adoption test. Whether a product is built by a central team or a domain team,
users still need to discover and understand it. They also need to trust it and
connect it to a decision
([Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}),
8:48-34:00). This keeps the comparison from becoming a team-chart debate.

## Ownership Boundary

In Data Mesh, the domain owns the product meaning. Zhamak Dehghani ties domain
ownership to business-aligned teams at 16:34 in
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}).
That ownership includes what the data means and what guarantees consumers can
rely on. It also covers known quality limits and product questions
([Data Products]({{ '/wiki/data-products/' | relative_url }})).

In a centralized platform, the shared team often owns more of the pipeline and
modeling path. Lars Albertsson's platform discussion includes storage, compute,
workflow engines, and self-service SQL. It also includes reproducibility,
lineage, and versioning
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
28:22-35:57 and 1:04:18). That ownership can be useful when the organization
still needs common definitions and stable ingestion. It can also help to have
one place to fix pipeline failures.

The risky middle is unclear ownership. A domain may publish raw events without
support expectations, or a central team may publish tables without enough
domain context. Zhamak's data-product sections and Caitlin Moorman's adoption
discussion both reject that state. Useful data needs discoverability and trust.
It also needs interpretation and a named owner
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
31:05-39:36,
[Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }}),
24:13-34:00).

## Platform Boundary

Data Mesh doesn't remove the platform. Zhamak Dehghani makes self-serve data
platforms a pillar of the model and then adds platform federation with shared
standards
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
41:58 and 47:35). The platform should make it easy for domains to publish
products without rebuilding identity and authorization. Metadata, validation,
and deployment patterns should also come from the shared path.

Central platforms can also provide self-service. Lars Albertsson describes
self-service analytics through platform primitives and embedded support
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
28:22 and 50:13). Mehdi OUAZZA gives the scale-up version: onboarding and
conventions turn tools such as Airflow and Kafka into a platform surface.
Playbooks and best practices keep that surface usable
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26).

Draw the boundary around repeatability. Keep shared capabilities where every
team needs the same safe path, including orchestration templates and schema
registry practice. Access controls and monitoring belong there too. Lineage and
deployment conventions also fit that shared layer
([Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})).
Move product ownership to domains when the hard part is semantic context,
consumer commitments, and prioritization.

## Governance Boundary

Data Mesh uses federated governance instead of absent governance. Zhamak Dehghani's
governance section covers shared policies and automation across domain-owned
products. It also covers the control layer around retention and validation
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
49:25-53:02). That's why the comparison belongs near
[Data Governance]({{ '/wiki/data-governance/' | relative_url }}) and
[Governance]({{ '/wiki/governance/' | relative_url }}).

Central platforms can enforce governance more directly because fewer teams
control the release path. Bart Vandekerckhove's governance episode shows the
controls that remain necessary in either model. Catalogs and lineage are part
of that set.

Data ownership and access requests belong in the same control set. Approvals,
reviews, and revocation do too
([Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}),
8:58-42:20). Rahul Jain's platform-leadership episode adds GDPR and role-based
access control. Quality metrics and lineage are also platform responsibilities
([Data Engineering Leadership and Modern Data Platforms]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})).

The decision isn't whether governance exists. It's where policy is defined,
where policy is enforced, and who owns exceptions.

A mesh needs federated policy automation because domains publish independently.
A central platform can start with central review. It still needs ownership
metadata and access processes so data consumers know whom to ask
([Data Governance]({{ '/wiki/data-governance/' | relative_url }})).

## Practical Adoption Path

Don't start with a full reorganization. Zhamak Dehghani's adoption section
emphasizes assessment, pilots, and executive buy-in
([Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}),
57:27). Data Mesh is a maturity move. It isn't a catalog rollout or a new
warehouse label.

Start from one painful product boundary. The central platform may block a
domain that has strong ownership. In that case, pilot a domain-owned data
product.

Give the pilot a clear product interface before expanding ownership. Zhamak's
schema discussion supports that sequence. Her data-product section does too.
See 13:20 and 39:36 in
[Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}).

The domain may not be ready to own those commitments yet. In that case, borrow
the Data Mesh vocabulary but keep implementation support closer to the central
platform
([DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}),
57:46-1:03:02).

Build the paved road before widening ownership. Mehdi OUAZZA's episode shows
that self-service requires onboarding, conventions, playbooks, and schema
registry practice. Data contracts belong there as well
([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
12:30-23:26). Rahul Jain's episode adds stakeholder prioritization, quality
measurement, access control, and lineage to the platform scope
([Data Engineering Leadership and Modern Data Platforms]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})).

## Review Prompts

Use these prompts during architecture or operating-model review.

- Name the owner of product meaning, quality, freshness, and consumer support.
  This comes from Zhamak Dehghani's data-product agreement discussion in
  [Data Mesh Implementation]({{ '/podcasts/data-mesh-architecture-decentralized-data-products/' | relative_url }}).
- Separate semantic ownership from platform ownership. Lars Albertsson's
  platform discussion keeps storage, compute, workflows, and lineage visible in
  [DataOps 101 for Scaling Data Platforms]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
- Check whether each domain can operate data contracts and metadata. Support
  and quality commitments need owners too. If they don't, use the central
  platform or a pilot before declaring a mesh
  ([Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})).
- Keep identity, authorization, access review, and revocation in the design.
  Masking, filtering, and lineage belong there too. Bart Vandekerckhove covers
  these controls in
  [Data Governance and Data Access Management]({{ '/podcasts/data-governance-data-access-management/' | relative_url }}).
- Treat self-service as a product surface with onboarding and examples.
  Conventions and support matter too, and Mehdi OUAZZA and Rahul Jain ground that
  point in platform episodes
  ([Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}),
  [Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})).
- Validate adoption with real consumers. Caitlin Moorman's last-mile discussion
  asks whether users can discover and trust the data. Users also need to
  interpret and use it in decisions
  ([Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

## Related Pages

Continue with these adjacent pages.

- [Data Mesh]({{ '/wiki/data-mesh/' | relative_url }})
- [Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
- [Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [Data Governance]({{ '/wiki/data-governance/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
- [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }})
- [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
- [Modern Data Stack]({{ '/wiki/modern-data-stack/' | relative_url }})
