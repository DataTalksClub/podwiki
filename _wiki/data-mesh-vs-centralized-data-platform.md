---
layout: article
tags: ["comparison"]
title: "Data Mesh vs Centralized Data Platform"
keyword: "data mesh vs centralized data platform"
secondary_keywords:
  - centralized data platform vs data mesh
  - data mesh versus centralized data platform
  - data mesh vs central data team
summary: "How DataTalks.Club podcast guests compare domain-owned data products with centralized platform ownership through architecture, governance, self-service, reliability, and organizational maturity."
related_wiki:
  - Data Mesh
  - Data Engineering Platforms
  - Self-Service Data Platforms
  - Data Products
  - Data Governance
  - DataOps
  - Platform Engineering
  - Data Quality and Observability
  - Platform Adoption
---

Data Mesh and a centralized data platform answer different parts of the same
operating decision. The decision assigns ownership for data meaning and
quality. It also assigns ownership for access, reliability, and consumer
support. In
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
[Zhamak Dehghani](https://datatalks.club/people/zhamakdehghani.html) frames
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}) as a decentralized
socio-technical model where business domains publish data as products.

In
[DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
[Lars Albertsson](https://datatalks.club/people/larsalbertsson.html) frames the
central platform around storage, compute, and workflow engines. Self-service
analytics, lineage, and versioning sit in the same platform discussion.

These episodes frame the choice as an ownership boundary, not as modern versus
old. A Data Mesh moves product accountability toward domains that understand
the data. A centralized
[Data Engineering Platform]({{ '/wiki/data-engineering-platforms/' | relative_url }})
keeps more implementation, governance, and operating discipline in a shared
team.

Both models still need [Data Products]({{ '/wiki/data-products/' | relative_url }})
and [Data Governance]({{ '/wiki/data-governance/' | relative_url }}).
They also need [DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
when many consumers depend on the same outputs.

## Model Assignment

[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}) decentralizes
data-product ownership while keeping shared standards. Zhamak Dehghani starts
from enterprise data friction: long centralized pipelines delay value because
domain context has to move through a central queue. Her Data Mesh model gives
domains responsibility for producer and consumer commitments. Self-serve
platform capabilities and federated governance keep the products interoperable
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
7:35 and 16:34, plus 41:58 and 49:25).

A centralized data platform assigns more of the common path to a shared data or
platform team. Lars Albertsson describes the platform through storage and
compute. Workflow engines and self-service SQL belong in the same platform
model. He also connects the platform to reproducible pipelines. Lineage and
versioning sit there too
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
28:22-35:57 and 1:04:18).

In that model, the shared team centralizes infrastructure mechanisms, quality
checks, and more of the governance path. The domain team may still explain
business meaning, but the central team owns more implementation work and
operating responsibility.

Both models need a reliable product interface, and Zhamak ties
[Data Products]({{ '/wiki/data-products/' | relative_url }}) to metadata and
quality expectations. She puts service levels and ownership decisions in that
same interface
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
31:05-39:36).

[Caitlin Moorman](https://datatalks.club/people/caitlinmoorman.html)
adds the adoption test because users need to discover and trust data outputs.
They also need to interpret and apply them before the platform or mesh has
created value
([Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html),
8:48-34:00).

## Boundary Movement

Zhamak Dehghani puts the center of gravity in domain ownership. Her Data Mesh
discussion argues that the teams closest to a business domain should own the
data products they publish. Those products include contracts and metadata. They
also include quality signals, service levels, and consumer support
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
13:20-39:36).

She still keeps a strong shared layer through self-serve
platforms, identity, and authorization. Platform federation and automated
governance remain shared concerns. That keeps
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }})
inside the Data Mesh decision rather than outside it
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
41:58-53:02).

Lars Albertsson is more cautious about splitting responsibility. His DataOps
episode asks when decentralization introduces ownership, governance, and
reproducibility risks. He treats lineage and versioning as operating
prerequisites. Workflow discipline and quality automation matter before teams
distribute platform responsibility
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
46:52 and 57:46-1:04:18).

[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) approaches the same
boundary from scale-up platform work. His self-service platform depends on
onboarding and Airflow conventions. Playbooks, senior engineering judgment, and
Kafka schemas belong to the same path. Schema registry practice and data
contracts make that path explicit
([Scaling Data Engineering Teams and Self-Service Platforms](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
12:30-23:26). That supports domain autonomy only when the shared platform gives
teams a reliable way to build.

[Bart Vandekerckhove](https://datatalks.club/people/bartvandekerckhove.html) shifts
the comparison toward access governance. His episode separates catalogs and
dictionaries from lineage and access controls. It then ties ownership models
to requests, approval, and review. Revocation, masking, and filtering belong
to the same control set
([Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html),
8:58-42:20). In his framing, a mesh can distribute ownership, but sensitive
data still needs shared control processes.

## Ownership: Domain Meaning or Shared Execution

The strongest case for Data Mesh appears when the bottleneck is domain meaning.
Zhamak Dehghani's domain-ownership section moves accountability toward teams
that know what the data represents. They also know how it changes and what
consumers need
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
16:34). That ownership includes the
[Data Products]({{ '/wiki/data-products/' | relative_url }}) interface.

Product meaning and quality limits belong there, along with freshness
expectations and service levels. Support belongs there too.

That ownership keeps product questions close to the teams that can answer
them.

The centralized platform case is strongest when the bottleneck is shared
execution. Lars Albertsson's platform model keeps common storage, compute,
workflow orchestration, and self-service SQL in a shared foundation. Lineage
and versioning stay visible in that same foundation
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
30:34 and 1:04:18). His decentralization caution says teams need enough
DataOps maturity, governance, and sharing culture before responsibility spreads
across domains (57:46-1:03:02).

The failure mode in both models is unclear ownership. A domain can publish raw
events without support expectations, or a central team can publish tables
without enough domain context. Zhamak's data-product sections and Caitlin
Moorman's last-mile discussion both point away from that state. Useful data
needs discoverability and trust. It also needs interpretation and a named owner
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
31:05-39:36,
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html),
24:13-34:00).

Move meaning, quality expectations, prioritization, and consumer support to
domains when those domains can maintain the
[Data Products]({{ '/wiki/data-products/' | relative_url }}) they publish.
Keep execution centralized when the main risk is duplicated platform work,
uneven [DataOps]({{ '/wiki/dataops/' | relative_url }}) practice, or missing
lineage and versioning discipline.

## Platform: Shared Capabilities or Domain Autonomy

Data Mesh doesn't remove the platform. Zhamak Dehghani makes self-serve data
platforms a pillar of the model, then adds platform federation and shared
standards. Domains don't rebuild identity and authorization. They also
shouldn't rebuild metadata, validation, and deployment paths
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
41:58 and 47:35). This is why the comparison belongs beside
[Self-Service Data Platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }})
and [Platform Engineering]({{ '/wiki/platform-engineering/' | relative_url }}).

A centralized platform can also be self-service. Lars Albertsson describes
self-service analytics through platform primitives and embedded support
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
28:22 and 50:13).

Mehdi OUAZZA gives the implementation structure through onboarding and Airflow
conventions. Playbooks and Kafka schemas
turn shared tools into a supported surface. Schema registries and data
contracts make the interface explicit
([Scaling Data Engineering Teams and Self-Service Platforms](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
12:30-23:26).

The practical boundary is repeatability. Keep shared capabilities where every
team needs the same safe path. That includes orchestration templates, schema
practices, access controls, and lineage. The shared layer also includes
monitoring and deployment conventions when those paths support many teams
([Data Engineering Leadership and Modern Data Platforms](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html),
57:29).

Move product ownership to domains when the hard part is semantic context.
Consumer commitments, prioritization, and support belong with that ownership
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
16:34 and 39:36). Use
[Data Engineering Platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and [Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) for the
shared-platform side of the same boundary.

## Governance: Federated Policy or Central Control

Data Mesh uses federated governance rather than absent governance because shared
policies and automation remain necessary. Zhamak Dehghani covers that control
layer
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
49:25-53:02). Retention and metadata apply across independently owned data
products. Validation and enforcement apply in the same layer.

It still needs explicit ownership and policy mechanisms.

Bart Vandekerckhove's governance episode shows the controls that remain
necessary in either architecture. Catalogs, dictionaries, and lineage sit in
the operating model. Access requests, approval, and review sit there too.
Revocation, masking, and filtering complete the control set
([Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html),
8:58-42:20).

[Rahul Jain](https://datatalks.club/people/16rahuljain.html) adds a
platform-leadership version through GDPR and role-based access control.
Dynamic masking and data lineage belong to that platform view. Quality metrics
and stakeholder prioritization belong there too
([Data Engineering Leadership and Modern Data Platforms](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html),
25:04-30:50 and 57:29).

The governance decision sets policy definition, enforcement, and exception
ownership. A mesh needs policy automation because domains publish
independently. A centralized platform can keep more review and access control
in one operating path. Consumers still need ownership metadata and access
processes so they know whom to ask
([Data Governance and Data Access Management](https://datatalks.club/podcast/data-governance-data-access-management.html),
8:58-42:20).

Use [Data Governance]({{ '/wiki/data-governance/' | relative_url }}) as the
boundary check. If access approvals, masking, and revocation still depend on
manual coordination, a centralized or strongly federated control path is safer.
The same applies when lineage and retention are still handled manually. If
those controls are automated and visible in the platform, domains can own more
of the product surface without creating separate policy systems.

## Reliability: Product Commitments or Operating Discipline

When reliability practices are still uneven, Lars Albertsson's caution favors
building the shared operating discipline first. He ties scalable platforms to
immutable pipelines, reproducibility, and schema automation. Quality practices,
lineage, and versioning sit in the same operating layer
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
16:42-20:12 and 46:52 plus 1:04:18). Those practices make it easier to reason
about failures before responsibility is split across many domain teams.

Data Mesh pushes reliability closer to product owners, but it doesn't remove
shared operating discipline. Zhamak Dehghani's data-product agreement section
puts quality, SLAs, and ownership decisions into the product interface
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
39:36). The shared platform still needs to expose observability, validation,
and deployment paths that domains can use consistently.

Use [Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
for the trust layer. A central team can own most of those practices, or the
organization can split them between central platform capabilities and domain
product commitments.

The reliability boundary depends on who can respond when data breaks. A mesh
works when domain owners can explain the data, maintain quality signals, and
support consumers. A centralized platform fits when incident response,
deployment conventions, and reproducible changes still need one disciplined
operating path.

## Adoption: Pilot Domains Before Reorgs

Don't start the comparison with a reorg. Zhamak Dehghani's adoption section
emphasizes assessment, pilots, and executive buy-in rather than a blanket
rollout
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
57:27). A team can pilot one domain-owned data product, define contracts and
quality expectations, and learn which shared platform capabilities are missing
before expanding the model.

When domains aren't ready to own product commitments, Lars Albertsson's
decentralization caution and Mehdi
OUAZZA's self-service platform examples both suggest building the paved road
first. Reproducible workflows and onboarding belong on that path, while
conventions and schema practices belong there too. Data contracts and support
complete the same path
([DataOps 101 for Scaling Data Platforms](https://datatalks.club/podcast/dataops-principles-and-scalable-data-platforms.html),
57:46-1:03:02,
[Scaling Data Engineering Teams and Self-Service Platforms](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html),
12:30-23:26).

The synthesis from these episodes is hybrid. Decentralize accountability where
domains can own meaning and quality expectations. Consumer support belongs
there too. Centralize or federate capabilities every domain would otherwise
rebuild.

Access and lineage often fit the shared layer, along with orchestration
patterns and schemas. Observability, deployment conventions, and governance
automation often fit there as well.

Validate the choice through actual consumer
adoption, as Caitlin Moorman argues in the last-mile data delivery episode
([Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html),
24:13-41:18).

[Platform Adoption]({{ '/wiki/platform-adoption/' | relative_url }}) is the
practical test. A Data Mesh pilot should prove that domain teams can publish and
support useful data products. A centralized platform pilot should prove that the
shared team can reduce waiting time without hiding business context from
consumers. In both cases, people need to find and trust the data before they can
interpret and use it.

## Related Pages

These adjacent pages expand the ownership, platform, governance, and adoption
threads in this comparison.

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

