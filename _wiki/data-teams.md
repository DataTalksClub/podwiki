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
[[analytics engineering]],
[[data engineering platforms]],
[[data product management]].
It also reaches [[communication]] and
[[leadership]].

The recurring design question is where authority should sit. Leaders can
centralize data work or embed it in product and business domains. They can also
use a hybrid model with shared standards.

Jesse Anderson's [[book:20210201-data-teams|Data Teams]] Book of the Week expands on these organizational models, covering data science, data engineering, and analytics team structures and how they scale.

[[person:lisacohen|Lisa Cohen]] frames that choice in
[[podcast:data-science-team-structure-and-org-design|Designing a Data Science Organization]].
She compares centralized teams, decentralized teams, and hybrid models.
[[person:zhamakdehghani|Zhamak Dehghani]]
makes the same question architectural in
[[podcast:data-mesh-architecture-decentralized-data-products|Data Mesh 101]].
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
[[podcast:building-and-scaling-data-team|Building and Leading Data Teams]],
where she starts with business health dashboards. As the team matures, she adds
a warehouse and forecasting. She also adds quality checks and adoption work.

Teams embed data people when a domain needs daily data support. That domain may
be product, marketing, operations, or finance. Cohen describes the tradeoff at
25:48. They gain domain context and faster decision paths. They may lose peer
learning and career structure if the organization doesn't protect data craft.

[[person:katiebauer|Katie Bauer]] makes this concrete in
[[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|How to Hire, Manage, and Grow a Data Science Team in B2B SaaS]].
Data science managers work in matrix organizations, and data scientists partner
with PMs and senior leaders. The manager still has to preserve maintainable
analytics and documentation. They also need peer review, mentorship, and growth
paths.

Hybrid models show up as the practical compromise. Cohen describes hybrid
structures around 10:41 and Twitter's division-level setup around 24:53. The
company can keep data people close to product areas while still preserving a
data leadership chain and shared planning cadence.

[[person:andreyshtylenko|Andrey Shtylenko]]
gives an industrial AI version in
[[podcast:building-and-scaling-data-science-practice-industrial-ai-mlops|Building Data Science Practice]].
Central teams standardize tooling and MLOps. Teams embedded in business units
earn trust locally. A hub-and-spoke model balances autonomy with shared services
for experiment tracking, annotation, and procurement.

## Roles and Interfaces

Data teams work when people make the interfaces explicit.
[[podcast:data-team-roles|Data Team Roles Explained]]
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
[[data products]] and
[[team building]]. The team succeeds
when someone owns the user, the data interface, the quality bar, and the
decision the output supports.

[[person:caitlinmoorman|Caitlin Moorman]] pushes this
interface view hardest in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Conquering the Last Mile in Data]].
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

[[person:mehdiouazza|Mehdi OUAZZA]] describes this in
[[podcast:scaling-data-engineering-teams-self-service-platforms|Growing a Data Engineering Team in a Scale-Up]].
Self-service platforms help teams onboard, follow conventions, reuse Airflow
practices, and adopt playbooks without waiting on a central bottleneck. Around
52:55, he describes a work split of roughly half platform engineering and half
use-case pipelines.

Data product ownership asks who's accountable for a data asset once other
people depend on it. Dehghani's data mesh discussion grounds that answer in
[[data mesh]],
[[self-service-data-platforms|self-service data platforms]],
and [[data engineering platforms]].

Around 16:34, she ties ownership to domains. Around 34:36 and 39:36, she
describes data products through consumer-first guarantees, quality, and service
levels. She also names clear ownership decisions. Around 49:25, she adds
federated governance so domain teams can move independently without breaking
shared standards.

Rahul Jain's data engineering leadership episode takes the platform view from a
manager's seat. In
[[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership and Modern Data Platforms]],
[[person:16rahuljain|Rahul Jain]] links management to
stakeholder prioritization, technical credibility, and quality standards. He
also covers data culture and data reconciliation. The same discussion includes
access controls, lineage, and the move from ETL to ELT.

A [[data-team-lead-role|data team lead]] is
responsible for more than delivery tickets. They protect the platform and the
people who rely on it.

## Scaling Risks

Small data teams usually start with generalists. In
[[podcast:building-data-team|Building a Data Science Team]],
[[person:dattran|Dat Tran]] argues for T-shaped
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
[[person:lisacohen|Cohen]] and
[[person:katiebauer|Bauer]] focus on reporting lines
and careers in data science teams. Cohen weighs centralization against
embedded domain context in
[[podcast:data-science-team-structure-and-org-design|Designing a Data Science Organization]].

Bauer focuses on manager expectations and craft quality. She also emphasizes
mentorship and cross-functional work in
[[podcast:hiring-and-managing-data-science-teams-in-b2b-saas|B2B SaaS]].
Their shared concern is that data people shouldn't become isolated ticket
takers, whether they sit in a central team or a matrixed product organization.

Dehghani and Mehdi put more weight on architecture and platform interfaces.
[[person:zhamakdehghani|Dehghani]] gives domain teams
ownership of interoperable [[data products]]
with federated governance and self-serve platforms around them in
[[podcast:data-mesh-architecture-decentralized-data-products|Data Mesh 101]].

[[person:mehdiouazza|Mehdi OUAZZA]] keeps the scale-up
platform team in view in
[[podcast:scaling-data-engineering-teams-self-service-platforms|Growing a Data Engineering Team in a Scale-Up]].
He names conventions and playbooks. He also names senior hiring, Kafka schemas,
and schema guarantees. His work split separates shared platform work from
use-case delivery.

Moorman and Liang both center adoption, but they start from different problems.
[[person:caitlinmoorman|Moorman]] starts from last-mile
decisions, personas, prototypes, and measurable wins in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Conquering the Last Mile in Data]].

[[person:tammyliang|Liang]] starts from business
operations and trust repair in
[[podcast:building-and-scaling-data-team|Building and Leading Data Teams]].
She uses dashboards and a warehouse as examples. She also adds forecasting,
quality checks, and team workshops. A data team isn't healthy just because its
stack works. People have to use its outputs in real decisions.

## Neighboring Work

Data team design overlaps with
[[data product management]]
when teams need roadmaps, discovery, adoption metrics, and product owners for
internal data assets. It overlaps with
[[analytics engineering]]
when the organization needs tested models, governed metrics, documentation, and
BI-ready datasets. Liang's
[[podcast:building-and-scaling-data-team|data team buildout]]
shows both: dashboards and forecasting need analytical modeling, while adoption
work needs the product habits Moorman describes in
[[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]].

[[Data Team Lead Role]] covers
hiring order, trust repair, adoption, and head-of-data scope. It also covers
manager-versus-expert boundaries. [[Data Architect Role]]
covers end-to-end model structure, reusable templates, governance, and
consumer-facing architecture. [[Leadership]]
and [[communication]] become part of
data team design when managers translate stakeholder demand into priorities.
They also help managers handle career growth and operating standards, as Rahul
Jain describes in
[[podcast:data-engineering-leadership-and-modern-data-platforms|Data Engineering Leadership and Modern Data Platforms]].
