---
layout: wiki
title: "Data Teams"
summary: "How podcast guests describe data team models, platform ownership, data products, stakeholder interfaces, and scaling risks."
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

Jesse Anderson's [[book:20210201-data-teams=>Data Teams]] Book of the Week
expands on these organizational models. It covers data science, data
engineering, analytics team structures, and scaling dynamics.

[[person:lisacohen=>Lisa Cohen]] frames that choice in
her discussion of data science organization design. She compares centralized
teams, decentralized teams, and hybrid models.
[[cite:data-science-team-structure-and-org-design=>Data Science Org Design]]
[[person:zhamakdehghani=>Zhamak Dehghani]]
makes the same question architectural in her data mesh interview. In that
model, domain teams own data products. Platform and governance work keeps those
products discoverable and interoperable.
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh 101]]

## Operating Models

Central data teams put data scientists and analysts under one data leader. Data
engineers and analytics engineers may sit there too. Cohen names knowledge
sharing, consistent practice, and a clearer professional home for data
specialists as benefits of this model. It fits early teams that still need
common definitions, data quality discipline, and shared engineering craft.
[[cite:data-science-team-structure-and-org-design=>Cohen]]

It also matches [[person:tammyliang=>Tammy Liang]]'s early buildout, where she
starts with business health dashboards. As the team matures, she adds a
warehouse and forecasting. She also adds quality checks and adoption work.
[[cite:building-and-scaling-data-team=>Liang]]

Teams embed data people when a domain needs daily data support. Product,
marketing, operations, and finance teams often need that context. Cohen
describes the tradeoff: teams gain faster decision paths but may lose peer
learning and career structure if the organization doesn't protect data craft.
[[cite:data-science-team-structure-and-org-design=>Cohen]]

[[person:katiebauer=>Katie Bauer]] makes this concrete in
her B2B SaaS data science management discussion. Data science managers work in
matrix organizations, and data scientists partner with PMs and senior leaders.
The manager still has to preserve maintainable analytics and documentation.
They also need peer review, mentorship, and growth paths.
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>B2B SaaS]]

Cohen describes hybrid models as a practical compromise, using Twitter's
division-level setup as an example. These structures keep data people close to
product areas while still preserving a data leadership chain and shared planning
cadence. [[cite:data-science-team-structure-and-org-design=>Cohen]]

[[person:andreyshtylenko=>Andrey Shtylenko]]
gives an industrial AI version, where central teams standardize tooling and
MLOps while embedded teams earn trust locally. A hub-and-spoke model balances
autonomy with shared services for experiment tracking, annotation, and
procurement.
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops=>Industrial AI]]

## Roles and Interfaces

Data teams work when people make the interfaces explicit.
The role-split discussion separates roles by the work each person owns in an ML
product. Product managers keep the team close to the user. Data scientists test
whether the problem should become a project. [[cite:data-team-roles]]

AI product discovery can use a design sprint as a shared interface before
implementation starts. Designers, data scientists, PMs, and engineers share the
problem-definition work. Data scientists can sit in user interviews and help own
the problem. A designer, product manager, or trained data scientist can
facilitate the divergent and convergent parts of the sprint. That connects
[[data product management]], [[experimentation]], and [[communication]] before a
[[machine-learning]] solution is chosen.
[[cite:ai-ml-product-design-and-experimentation=>AI/ML Product Design]]

Data engineers make usable data available, while ML engineers bring models into
software systems.

That role split matters less as a rigid org chart than as a set of handoffs.
Data engineers and platform engineers make data available. Analytics engineers
turn messy source data into modeled analytical data.

For ML products, teams may hand over model code or expose a prediction API. They
may also add an ML engineer bridge or keep data scientists and software
engineers in one small product team. The integration approach matters because
siloed [[machine-learning]] and [[software-engineering]] groups can disagree on
quality, deployment ownership, shared vocabulary, and what productionizing a
model requires. Stronger [[mlops]], [[machine-learning-system-design]], and
[[communication]] practices make those boundaries explicit instead of leaving
them to the final deployment step.
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]

Analysts and data scientists translate questions into metrics and
recommendations. They may also run experiments or build models. Product and
business partners decide what action the work should support.

The same interface logic links data teams to
[[data products]] and
[[team building]]. The team succeeds
when someone owns the user, the data interface, the quality bar, and the
decision the output supports.

[[person:caitlinmoorman=>Caitlin Moorman]] pushes this
interface view hardest in her last-mile data discussion. She recommends treating
analytics outputs as products and doing user research when adoption is poor.
She starts data work from the decision it should enable, then embeds metrics in
the meetings where people decide. For a data team, stakeholder management isn't
a soft add-on. It's part of delivery.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data]]

## Platforms and Product Ownership

Guests repeatedly separate platform ownership from product ownership. A shared
platform team should give other teams paved paths for orchestration, data
movement, and testing. It should also cover deployment, observability,
permissions, and documentation.

[[person:mehdiouazza=>Mehdi OUAZZA]] describes this in
his scale-up data engineering episode. Self-service platforms help teams
onboard, follow conventions, reuse Airflow practices, and adopt playbooks
without waiting on a central bottleneck. He describes a work split of roughly
half platform engineering and half use-case pipelines.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale-Up Data Engineering]]

Data product ownership asks who's accountable for a data asset once other
people depend on it. Dehghani's data mesh discussion grounds that answer in
[[data mesh]],
[[self-service-data-platforms=>self-service data platforms]],
and [[data engineering platforms]].

Dehghani ties ownership to domains and describes data products through
consumer-first guarantees, quality, and service levels. She also names clear
ownership decisions and federated governance so domain teams can move
independently without breaking shared standards.
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh 101]]

Rahul Jain's data engineering leadership episode takes the platform view from a
manager's seat. [[person:16rahuljain=>Rahul Jain]] links management to
stakeholder prioritization, technical credibility, and quality standards. He
also covers data culture and data reconciliation. The same discussion covers
access controls, lineage, and the move from ETL to ELT.
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]

A [[data-team-lead-role=>data team lead]] is
responsible for more than delivery tickets. They protect the platform and the
people who rely on it.

## Scaling Risks

Small data teams usually start with generalists. [[person:dattran=>Dat Tran]]
argues for T-shaped engineers in early startups, then a shift toward specialists
as maturity grows. He also ties hiring to product uncertainty. Build the
prototype, learn what the MVP needs, and then hire around the product vision
rather than fashionable titles. [[cite:building-data-team=>Building a Data Team]]

As a data team grows, the risks change. Liang describes spreadsheet culture,
dashboard distrust, production ML gaps, and governance repairs in her team
buildout. She hires for adoption and communication, not only technical skill,
and she uses workshops and Q&A sessions to help people use the work. Bauer adds
the career-system risk. Junior data people need mentorship, practice, exposure,
and clear expectations before they specialize too narrowly.
[[cite:building-and-scaling-data-team=>Liang]]
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>Bauer]]

Hypergrowth creates a different failure mode. Mehdi describes speed versus
quality pressure, hiring surges, and onboarding strain. He also talks about
event streaming schemas and the need for senior engineers who can set
conventions.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale-Up Data Engineering]]

Rahul adds the management version. Managers need empathy and situational
awareness, but they also need explicit quality standards and enough technical
credibility to guide tradeoffs. Without that mix, a team can ship more
pipelines while making the platform harder to trust.
[[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]

## Authority Placement

Podcast discussions agree that data teams need ownership, communication, and
trustworthy delivery. They differ on where authority should sit.
[[person:lisacohen=>Cohen]] and
[[person:katiebauer=>Bauer]] focus on reporting lines
and careers in data science teams. Cohen weighs centralization against
embedded domain context.
[[cite:data-science-team-structure-and-org-design=>Cohen]]

Bauer focuses on manager expectations and craft quality, with mentorship and
cross-functional work as part of the management job.
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>Bauer]]
Their shared concern is that data people shouldn't become isolated ticket
takers, whether they sit in a central team or a matrixed product organization.

Dehghani and Mehdi put more weight on architecture and platform interfaces.
[[person:zhamakdehghani=>Dehghani]] gives domain teams
ownership of interoperable [[data products]]
with federated governance and self-serve platforms around them.
[[cite:data-mesh-architecture-decentralized-data-products=>Data Mesh 101]]

[[person:mehdiouazza=>Mehdi OUAZZA]] keeps the scale-up
platform team in view by naming conventions and playbooks. He also names senior
hiring, Kafka schemas, and schema guarantees. His work split separates shared
platform work from use-case delivery.
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale-Up Data Engineering]]

Moorman and Liang both center adoption, but they start from different problems.
[[person:caitlinmoorman=>Moorman]] starts from last-mile
decisions, personas, prototypes, and measurable wins.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Moorman]]

[[person:tammyliang=>Liang]] starts from business
operations and trust repair, using dashboards and a warehouse as examples. She
also adds forecasting, quality checks, and team workshops. A data team isn't
healthy just because its stack works. People have to use its outputs in real
decisions.
[[cite:building-and-scaling-data-team=>Liang]]

## Neighboring Work

Data team design overlaps with
[[data product management]].
Teams need roadmaps, discovery, adoption metrics, and product owners for
internal data assets.

Data team design also overlaps with
[[analytics engineering]].
Organizations need tested models, governed metrics, documentation, and BI-ready
datasets. Liang's data team buildout links both concerns. Dashboards and
forecasting need analytical modeling. Adoption work needs the product habits
Moorman describes in her last-mile data discussion.
[[cite:building-and-scaling-data-team=>Liang]]
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Moorman]]

[[Data Team Lead Role]] covers
hiring order, trust repair, adoption, and head-of-data scope. It also covers
manager-versus-expert boundaries. [[Data Architect Role]]
covers end-to-end model structure, reusable templates, governance, and
consumer-facing architecture. [[Leadership]]
and [[communication]] become part of
data team design when managers translate stakeholder demand into priorities.
They also help managers handle career growth and operating standards, as Rahul
Jain describes in his data engineering leadership episode.
[[cite:data-engineering-leadership-and-modern-data-platforms=>Jain]]
