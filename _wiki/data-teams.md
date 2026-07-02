---
layout: wiki
title: "Data Teams"
summary: "How DataTalks.Club podcast guests describe data teams as organizational design around data work, including team models, platform ownership, data products, stakeholder interfaces, and scaling risks."
related:
  - Data Mesh
  - Data Products
  - Data Engineering Platforms
  - Self-Service Data Platforms
  - Data Product Management
  - Analytics Engineering
  - Communication
  - Leadership
  - Team Building
---

Data teams are the organizational design around data work. They decide who owns
pipelines and analytical models, who maintains ML systems and metrics, and
who's accountable for stakeholder and quality commitments.

DataTalks.Club guests don't treat a data team as one job family. They describe
a coordination model that spans
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[data product management]({{ '/wiki/data-product-management/' | relative_url }}).
It also reaches [communication]({{ '/wiki/communication/' | relative_url }}) and
[leadership]({{ '/wiki/leadership/' | relative_url }}).

The recurring design question is where authority should sit. Leaders can
centralize data work or embed it in product and business domains. They can also
use a hybrid model with shared standards.

Jesse Anderson's [Data Teams](https://datatalks.club/books/20210201-data-teams.html) Book of the Week expands on these organizational models, covering data science, data engineering, and analytics team structures and how they scale.

[Lisa Cohen](https://datatalks.club/people/lisacohen.html) frames that choice in
[Designing a Data Science Organization](https://datatalks.club/podcast/data-science-team-structure-and-org-design.html).
She compares centralized teams, decentralized teams, and hybrid models.
[Zhamak Dehghani](https://datatalks.club/people/zhamakdehghani.html)
makes the same question architectural in
[Data Mesh 101](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html).
In that model, domain teams own data products. Platform and governance work
keeps those products discoverable and interoperable.

## Operating Models

Central data teams put data scientists and analysts under one data leader. Data
engineers and analytics engineers may sit there too. Around 29:25 in her
org-design episode, Cohen names knowledge sharing and consistent practice. She
also names a clearer professional home for data specialists. This model fits
early teams that still need common definitions, data quality discipline, and
shared engineering craft.

It also matches Tammy Liang's early buildout in
[Building and Leading Data Teams](https://datatalks.club/podcast/building-and-scaling-data-team.html),
where she starts with business health dashboards. As the team matures, she adds
a warehouse and forecasting. She also adds quality checks and adoption work.

Teams embed data people when a domain needs daily data support. That domain may
be product, marketing, operations, or finance. Cohen describes the tradeoff at
25:48. They gain domain context and faster decision paths. They may lose peer
learning and career structure if the organization doesn't protect data craft.

[Katie Bauer](https://datatalks.club/people/katiebauer.html) makes this concrete in
[How to Hire, Manage, and Grow a Data Science Team in B2B SaaS](https://datatalks.club/podcast/hiring-and-managing-data-science-teams-in-b2b-saas.html).
Data science managers work in matrix organizations, and data scientists partner
with PMs and senior leaders. The manager still has to preserve maintainable
analytics and documentation. They also need peer review, mentorship, and growth
paths.

Hybrid models show up as the practical compromise. Cohen describes hybrid
structures around 10:41 and Twitter's division-level setup around 24:53. The
company can keep data people close to product areas while still preserving a
data leadership chain and shared planning cadence.

[Andrey Shtylenko](https://datatalks.club/people/andreyshtylenko.html)
gives an industrial AI version in
[Building Data Science Practice](https://datatalks.club/podcast/building-and-scaling-data-science-practice-industrial-ai-mlops.html).
Central teams standardize tooling and MLOps. Teams embedded in business units
earn trust locally. A hub-and-spoke model balances autonomy with shared services
for experiment tracking, annotation, and procurement.

## Roles and Interfaces

Data teams work when people make the interfaces explicit.
[Data Team Roles Explained](https://datatalks.club/podcast/data-team-roles.html)
separates roles by the work each person owns in an ML product. Product managers
keep the team close to the user. Data scientists test whether the problem
should become a project.

Data engineers make usable data available, while ML engineers bring models into
software systems.

That role split matters less as a rigid org chart than as a set of handoffs.
Data engineers and platform engineers make data available. Analytics engineers
turn messy source data into modeled analytical data.

Analysts and data scientists translate questions into metrics and
recommendations. They may also run experiments or build models. Product and
business partners decide what action the work should support.

The same interface logic links data teams to
[data products]({{ '/wiki/data-products/' | relative_url }}) and
[team building]({{ '/wiki/team-building/' | relative_url }}). The team succeeds
when someone owns the user, the data interface, the quality bar, and the
decision the output supports.

[Caitlin Moorman](https://datatalks.club/people/caitlinmoorman.html) pushes this
interface view hardest in
[Conquering the Last Mile in Data](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html).
Around 26:21, she recommends treating analytics outputs as products and doing
user research when adoption is poor. Around 34:00 and 38:15, she starts data
work from the decision it should enable, then embeds metrics in the meetings
where people decide. For a data team, stakeholder management isn't a soft
add-on. It's part of delivery.

## Platforms and Product Ownership

Guests repeatedly separate platform ownership from product ownership. A shared
platform team should give other teams paved paths for orchestration, data
movement, and testing. It should also cover deployment, observability,
permissions, and documentation.

[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) describes this in
[Growing a Data Engineering Team in a Scale-Up](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html).
Self-service platforms help teams onboard, follow conventions, reuse Airflow
practices, and adopt playbooks without waiting on a central bottleneck. Around
52:55, he describes a work split of roughly half platform engineering and half
use-case pipelines.

Data product ownership asks who's accountable for a data asset once other
people depend on it. Dehghani's data mesh discussion grounds that answer in
[data mesh]({{ '/wiki/data-mesh/' | relative_url }}),
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).

Around 16:34, she ties ownership to domains. Around 34:36 and 39:36, she
describes data products through consumer-first guarantees, quality, and service
levels. She also names clear ownership decisions. Around 49:25, she adds
federated governance so domain teams can move independently without breaking
shared standards.

Rahul Jain's data engineering leadership episode takes the platform view from a
manager's seat. In
[Data Engineering Leadership and Modern Data Platforms](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html),
[Rahul Jain](https://datatalks.club/people/16rahuljain.html) links management to
stakeholder prioritization, technical credibility, and quality standards. He
also covers data culture and data reconciliation. The same discussion includes
access controls, lineage, and the move from ETL to ELT.

A [data team lead]({{ '/wiki/data-team-lead-role/' | relative_url }}) is
responsible for more than delivery tickets. They protect the platform and the
people who rely on it.

## Scaling Risks

Small data teams usually start with generalists. In
[Building a Data Science Team](https://datatalks.club/podcast/building-data-team.html),
[Dat Tran](https://datatalks.club/people/dattran.html) argues for T-shaped
engineers in early startups, then a shift toward specialists as maturity grows.
He also ties hiring to product uncertainty. Build the prototype, learn what the
MVP needs, and then hire around the product vision rather than fashionable
titles.

As a data team grows, the risks change. Liang describes spreadsheet culture,
dashboard distrust, production ML gaps, and governance repairs in her team
buildout. She hires for adoption and communication, not only technical skill,
and she uses workshops and Q&A sessions to help people use the work. Bauer adds
the career-system risk. Junior data people need mentorship, practice, exposure,
and clear expectations before they specialize too narrowly.

Hypergrowth creates a different failure mode. Mehdi describes speed versus
quality pressure, hiring surges, and onboarding strain. He also talks about
event streaming schemas and the need for senior engineers who can set
conventions.

Rahul adds the management version. Managers need empathy and situational
awareness, but they also need explicit quality standards and enough technical
credibility to guide tradeoffs. Without that mix, a team can ship more
pipelines while making the platform harder to trust.

## Authority Placement

Podcast discussions agree that data teams need ownership, communication, and
trustworthy delivery. They differ on where authority should sit.
[Cohen](https://datatalks.club/people/lisacohen.html) and
[Bauer](https://datatalks.club/people/katiebauer.html) focus on reporting lines
and careers in data science teams. Cohen weighs centralization against
embedded domain context in
[Designing a Data Science Organization](https://datatalks.club/podcast/data-science-team-structure-and-org-design.html).

Bauer focuses on manager expectations and craft quality. She also emphasizes
mentorship and cross-functional work in
[B2B SaaS](https://datatalks.club/podcast/hiring-and-managing-data-science-teams-in-b2b-saas.html).
Their shared concern is that data people shouldn't become isolated ticket
takers, whether they sit in a central team or a matrixed product organization.

Dehghani and Mehdi put more weight on architecture and platform interfaces.
[Dehghani](https://datatalks.club/people/zhamakdehghani.html) gives domain teams
ownership of interoperable [data products]({{ '/wiki/data-products/' | relative_url }})
with federated governance and self-serve platforms around them in
[Data Mesh 101](https://datatalks.club/podcast/data-mesh-architecture-decentralized-data-products.html).

[Mehdi OUAZZA](https://datatalks.club/people/mehdiouazza.html) keeps the scale-up
platform team in view in
[Growing a Data Engineering Team in a Scale-Up](https://datatalks.club/podcast/scaling-data-engineering-teams-self-service-platforms.html).
He names conventions and playbooks. He also names senior hiring, Kafka schemas,
and schema guarantees. His work split separates shared platform work from
use-case delivery.

Moorman and Liang both center adoption, but they start from different problems.
[Moorman](https://datatalks.club/people/caitlinmoorman.html) starts from last-mile
decisions, personas, prototypes, and measurable wins in
[Conquering the Last Mile in Data](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html).

[Liang](https://datatalks.club/people/tammyliang.html) starts from business
operations and trust repair in
[Building and Leading Data Teams](https://datatalks.club/podcast/building-and-scaling-data-team.html).
She uses dashboards and a warehouse as examples. She also adds forecasting,
quality checks, and team workshops. A data team isn't healthy just because its
stack works. People have to use its outputs in real decisions.

## Neighboring Work

Data team design overlaps with
[data product management]({{ '/wiki/data-product-management/' | relative_url }})
when teams need roadmaps, discovery, adoption metrics, and product owners for
internal data assets. It overlaps with
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
when the organization needs tested models, governed metrics, documentation, and
BI-ready datasets. Liang's
[data team buildout](https://datatalks.club/podcast/building-and-scaling-data-team.html)
shows both: dashboards and forecasting need analytical modeling, while adoption
work needs the product habits Moorman describes in
[Last-Mile Data Delivery](https://datatalks.club/podcast/last-mile-data-delivery-and-data-product-adoption-modern-data-stack.html).

[Data Team Lead Role]({{ '/wiki/data-team-lead-role/' | relative_url }}) covers
hiring order, trust repair, adoption, and head-of-data scope. It also covers
manager-versus-expert boundaries. [Data Architect Role]({{ '/wiki/data-architect-role/' | relative_url }})
covers end-to-end model structure, reusable templates, governance, and
consumer-facing architecture. [Leadership]({{ '/wiki/leadership/' | relative_url }})
and [communication]({{ '/wiki/communication/' | relative_url }}) become part of
data team design when managers translate stakeholder demand into priorities.
They also help managers handle career growth and operating standards, as Rahul
Jain describes in
[Data Engineering Leadership and Modern Data Platforms](https://datatalks.club/podcast/data-engineering-leadership-and-modern-data-platforms.html).
