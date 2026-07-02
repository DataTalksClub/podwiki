---
layout: "person"
title: "Zhamak Dehghani"
source_person: "../datatalksclub.github.io/_people/zhamakdehghani.md"
person_id: "zhamakdehghani"
summary: "Founder of data mesh contributing decentralized data architecture, data products, contracts, and federated governance."
expertise: ["data mesh", "data engineering", "data products", "data governance"]
podcast_episodes: ["data-mesh-architecture-decentralized-data-products"]
curated: "true"
source_url: "https://datatalks.club/people/zhamakdehghani.html"
---

Zhamak Dehghani's DataTalks.Club contribution is the reference interview for
[Data Mesh]({{ '/wiki/data-mesh/' | relative_url }}). She explains why
centralized data pipelines become bottlenecks. She also shows how domain teams
can own analytical data while shared platform and governance capabilities keep
decentralization usable.
In the
[Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html),
she explains the idea as a socio-technical architecture, not a tool category.

## From Distributed Systems to Data Mesh

Zhamak introduces herself as a former ThoughtWorks consultant. She spent more
than a decade working with complex enterprises and had just left to start a
company focused on peer-to-peer analytical data sharing
([2:39-6:19](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).
Her short biography matters because the interview frames data mesh through
[distributed systems]({{ '/wiki/data-engineering-platforms/' | relative_url }})
and large-scale software architecture. It also draws on the friction she saw in
companies trying to turn data into reports, dashboards, and ML products.

At 6:42, she describes building data infrastructure and data platforms together
with [data products]({{ '/wiki/data-products/' | relative_url }}) and ML/AI use
cases. She doesn't treat the platform as a separate back-office project. At
7:51, she says enterprise data strategies often left data
scientists and business users waiting for access or unable to deploy what they
built. That diagnosis sets up the rest of the episode: data mesh is her answer
to long, fragile paths from data to value.

## Data Mesh Starts with Decoupling

At 9:56, Zhamak defines data mesh as a decentralized way to manage and share
analytical data across teams. The model still needs quality, integrity, and
interoperability
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).
She challenges the "pipeline thinking" that moves data into one place and adds
processing and metadata later. That approach makes the time from data to value
too long.

Her architectural move decouples pipelines into smaller units. Each unit
includes data and metadata, plus computation and sharing APIs. At 13:20, she
contrasts that with a warehouse or lake full of tables, where producer and
consumer are tied by a fragile interface. This is why her interview anchors
[Data Mesh vs Centralized Data Platform]({{ '/wiki/data-mesh-vs-centralized-data-platform/' | relative_url }}):
the difference isn't whether a warehouse exists. It's whether ownership,
interfaces, and change are arranged around domain-owned products or a central
team.

## Domain Ownership Is a Scaling Model

Zhamak's first principle is domain ownership. At 17:10, she says data
generation and data consumption should align with autonomous groups of people.
Those groups are usually business domains with their own vocabulary and outcomes
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).

Her streaming-company example uses teams for listener onboarding and playlist
generation. It also includes artist management, artist payments, and partners.
The example shows why a mesh grows with the business instead of routing every
dependency through one shared data team.

She also gives a maturity warning. At 22:51, putting each team in its own
warehouse schema can be a start, but it doesn't deliver the loose coupling she
wants. A playlist team, player team, or onboarding team should be able to change
its data product without breaking consumers. That thread connects her
episode to [data strategy]({{ '/wiki/data-strategy/' | relative_url }}),
[data teams]({{ '/wiki/data-teams/' | relative_url }}), and
[data architect role]({{ '/wiki/data-architect-role/' | relative_url }}).

## Data Products Need Consumer-Facing Guarantees

The second principle is data as a product. At 34:59, Zhamak says domain
ownership can collapse into new silos. To prevent that, teams need to measure
shared data from the consumer's point of view
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).

For her, a data product isn't just a dataset. It includes the information a
consumer needs to discover it and assess trust. The consumer also needs to
understand quality and decide whether it's fit for a use case.

At 39:36, she makes the role concrete through a player-clickstream example. A
data product owner or data product manager talks with consumers, learns whether
they need low-latency events or higher-integrity aggregates. The owner then
decides whether the producer team, a middle team, or the consumer should build
the next product version. That makes her episode useful for
[Data Product Owner vs Data Product Manager]({{ '/wiki/data-product-owner-vs-data-product-manager/' | relative_url }}),
[Product Owner vs Product Manager]({{ '/wiki/product-owner-vs-product-manager/' | relative_url }}),
and the
[Data Product Manager Roadmap]({{ '/wiki/data-product-manager-roadmap/' | relative_url }}).

## Platforms Should Hide Undifferentiated Complexity

Zhamak treats the self-serve data platform as the third principle. Domain teams
can't own data products if every product requires deep expertise across the
whole platform stack. At 42:11, she says the platform should make data
producers and consumers' work easier. It does that by raising the abstraction
level
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).

She's careful not to equate self-service with untestable no-code tooling. At
45:47, she argues that engineering practices still matter, but a data product
developer shouldn't have to stitch together every vertical concern manually.
This is the clearest bridge from her interview to
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
[developer experience]({{ '/wiki/developer-experience/' | relative_url }}), and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

At 47:35, she rejects the idea that one giant platform should serve every need
in a complex organization. Teams may use different processing tools or cloud
services. Common platform responsibilities let data products be discovered and
understood. They also support sharing, use, and connection.

## Governance Is Federated and Computational

Zhamak's fourth principle is federated computational governance. At 49:25, she
frames governance as shared policies and cross-cutting concerns that must work
across independent data products
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).
Governance shouldn't slow teams down with manual control gates. It should embed
privacy, security, and access control into automated platform capabilities. It
also needs standard language and interoperability.

At 53:02, she uses retention policy as an example. Every data product should
declare retention, but each domain can set the value that fits its data. The
platform then automates configuration, enforcement, validation, and discovery.
That explanation grounds related pages on
[data governance]({{ '/wiki/data-governance/' | relative_url }}),
[governance]({{ '/wiki/governance/' | relative_url }}), and
[security]({{ '/wiki/security/' | relative_url }}). It also complements
[Bart Vandekerckhove](https://datatalks.club/people/bartvandekerckhove.html),
whose data access episode discusses ownership models and access management in
data mesh setups from the governance side.

## Adoption Starts with Readiness, Not a Reorg

Near the end of the interview, Zhamak warns against adopting data mesh as a
small side project. At 54:48, she says teams should first understand why data
mesh exists and what first principles define it. Implementation spans
technology, architecture, and organizational change
([Data Mesh Implementation](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html)).

At 57:27, her practical adoption advice is to assess readiness and confirm
executive support. Teams should also check DevOps and DataOps maturity. They
should find allies and start with use cases that touch one or two domains. She
warns against starting with a broad marketing use case. That kind of work
depends on many domains before the interoperability layer and ways of working
exist.

Her caution makes her a useful counterpoint to
[Lars Albertsson](https://datatalks.club/people/larsalbertsson.html). Lars
discusses [DataOps]({{ '/wiki/dataops/' | relative_url }}) and the risk of
splitting ownership before the organization can support the operating model.
