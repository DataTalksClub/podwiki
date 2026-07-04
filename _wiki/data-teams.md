---
layout: wiki
title: "Data Teams"
summary: "How podcast guests describe data team models, platform ownership, data products, stakeholder interfaces, and scaling risks."
related:
  - Data Mesh
  - Data Products
  - Data Strategy
  - Data Engineering Platforms
  - Self-Service Data Platforms
  - Data Product Management
  - Data Product Adoption
  - Data Translator Role
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
The hiring path moves from analyst capacity to engineering foundations and then
to business-facing adoption work as the bottleneck changes.
[[cite:building-and-scaling-data-team@15:04=>Liang]]

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
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas@8:33=>B2B SaaS]]
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas@11:58=>B2B SaaS]]

Cohen describes hybrid models as a practical compromise, using Twitter's
division-level setup as an example. These structures keep data people close to
product areas while still preserving a data leadership chain and shared planning
cadence. [[cite:data-science-team-structure-and-org-design=>Cohen]]

Industrial AI teams face a harder coordination problem. Plants, business units,
and central technology teams may all own part of the delivery path.

Shtylenko describes a staged path. Teams start with one end-to-end POC, then
centralize data people long enough to define roles and MLOps standards.
After that, they move people near the product or engineering teams that own
daily delivery.
Central teams can set standards and build reusable MLOps capability, but they
can also become resource pools with queues and weaker product trust.

Domain-facing teams learn local operational constraints faster, but a fully
decentralized model can lose common standards. A hub-and-spoke model keeps
shared services such as experiment tracking, annotation, and procurement near
the center while domain-facing teams own the local adoption work.
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops@32:00=>Industrial AI POC wedge]]
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops@43:39=>Industrial AI org design]]
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops@48:13=>Hub-and-spoke model]]

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
[[cite:ai-ml-product-design-and-experimentation@25:00=>AI/ML Product Design]]

Data engineers make usable data available, while ML engineers bring models into
software systems.

That role split matters less as a rigid org chart than as a set of handoffs.
Data engineers and platform engineers make data available. Analytics engineers
turn messy source data into modeled analytical data.

Analytics engineers also decide where business logic should live.

Victoria Perez Mola describes the role as modeling data and maintaining
quality. The role also exposes usable data to Looker. Analysts and data
scientists then avoid repeated cleanup
[[cite:analytics-engineer-skills-tools@4:05=>Analytics engineer responsibilities]]
[[cite:analytics-engineer-skills-tools@31:09=>Cleaner data for analysts]].

Juan Manuel Perafan frames the same interface as turning business reality into
tables. Stakeholder mediation helps teams reconcile conflicting source systems
and definitions
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices@11:03=>Business reality into data]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices@25:52=>Stakeholder mediation]].

For ML products, teams may hand over model code or expose a prediction API. They
may also add an ML engineer bridge or keep data scientists and software
engineers in one small product team. The integration approach matters because
siloed [[machine-learning]] and [[software-engineering]] groups can disagree on
quality, deployment ownership, shared vocabulary, and what productionizing a
model requires. Stronger [[mlops]], [[machine-learning-system-design]], and
[[communication]] practices make those boundaries explicit instead of leaving
them to the final deployment step.
[[cite:software-engineering-for-machine-learning@36:28=>Software Engineering for ML]]

Analysts and data scientists translate questions into metrics and
recommendations. They may also run experiments or build models. Product and
business partners decide what action the work should support.

The same interface logic links data teams to
[[data products]] and
[[team building]]. The team succeeds
when someone owns the user, the data interface, the quality bar, and the
decision the output supports.

Teams should scale role vocabulary with team size instead of forcing every
specialty into the first org chart. Early teams may combine product, data
science, engineering, and ML engineering responsibilities. They can split those
responsibilities as handoffs become bottlenecks.
[[cite:data-team-roles=>Data Team Roles]]

[[person:caitlinmoorman=>Caitlin Moorman]] pushes this
interface view hardest in her last-mile data discussion. She recommends treating
analytics outputs as products and doing user research when adoption is poor.
She starts data work from the decision it should enable, then embeds metrics in
the meetings where people decide. For a data team, stakeholder management isn't
a soft add-on. It's part of delivery.
[[cite:last-mile-data-delivery-and-data-product-adoption-modern-data-stack=>Last-Mile Data]]

A team can formalize translation as an interface, not just an individual soft
skill. A data strategist can sit between data engineering, data science, and
business teams. The role aligns definitions, explains dashboard reliability, and
turns business pressure into usable technical priorities. That role sits close to the
[[data-translator-role=>Data Translator Role]], [[communication]], and
[[data-product-adoption=>Data Product Adoption]].
[[cite:data-translator-role-and-data-strategy=>Data Translator Role]]

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

Cloud governance adds a more operational role map. Data stewards, producers,
and decision makers all participate in governance. Ownership isn't just a label
on a dataset. It's a set of review and access responsibilities inside the team
model.[[cite:cloud-data-governance@33:03=>Cloud Data Governance]]

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

Industrial AI shared services put part of that ownership in the center. The
central group doesn't need to force every product team onto the same framework.
It can own vendor relationships and help teams choose common MLOps, experiment
tracking, and annotation services. That keeps procurement and platform decisions
from splintering while embedded teams stay accountable for product outcomes.
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops@50:14=>Industrial AI shared services]]

## Scaling Risks

Small data teams usually start with generalists. [[person:dattran=>Dat Tran]]
argues for T-shaped engineers in early startups, then a shift toward specialists
as maturity grows. He also ties hiring to product uncertainty. Build the
prototype, learn what the MVP needs, and then hire around the product vision
rather than fashionable titles. [[cite:building-data-team=>Building a Data Team]]

Organizations with limited resources may keep a small core data team and extend
capacity through a research network. The organization keeps ownership inside
the core team while using external researchers for specialized modeling,
evaluation, or domain work.
[[cite:data-science-and-analytics-for-nonprofits-tech-for-good@54:07=>Nonprofit data science]]

As a data team grows, the risks change. Liang describes spreadsheet culture,
dashboard distrust, production ML gaps, and governance repairs in her team
buildout. She hires for adoption and communication, not only technical skill,
and she uses workshops and Q&A sessions to help people use the work. Bauer adds
the career-system risk. Junior data people need mentorship, practice, exposure,
and clear expectations before they specialize too narrowly.
[[cite:building-and-scaling-data-team@10:06=>Liang]]
[[cite:building-and-scaling-data-team@49:00=>Liang]]
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas=>Bauer]]

Role order should change when the bottleneck changes, so a dashboard-heavy team
can start with an analyst. Source integration, historical data, forecasting, and
multiple data sources make a data engineer foundational. Stakeholder-heavy
businesses may need a business analyst or data researcher alongside engineering.
That gives adoption work an owner.
[[cite:building-and-scaling-data-team@23:11=>Liang]]

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

Industrial AI leaders have to treat the reporting line as part of the design,
not just a title choice. A data science or AI practice may report through a
CTO, CIO, CMO, or CEO.

A CTO line usually points the team toward product
capabilities. A CIO line points toward internal efficiency. A CMO line points
toward marketing, sales, and customer interaction. A CEO line gives the data
group a broader cross-company mandate.

For the team, the useful test is whether that line gives it enough authority to
coordinate platforms, business adoption, and operational change.
[[cite:building-and-scaling-data-science-practice-industrial-ai-mlops@19:06=>Industrial AI reporting line]]

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

Analytics engineers can sit in a platform team or inside domain analytics teams.
Victoria describes a platform setup that later decentralizes analytics engineers
into operations or commercial analytics. Business-facing teams then get modeled
data closer to their stakeholders
[[cite:analytics-engineer-skills-tools@33:02=>Analytics engineer collaboration]]
[[cite:analytics-engineer-skills-tools@48:36=>Platform and embedded analytics engineers]].
That placement decision connects [[Analytics Engineering Roadmap]] to
[[Team Building]] because the same skillset can support shared standards,
domain ownership, or both.

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
