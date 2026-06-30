---
layout: wiki
title: "Team Building"
summary: "How DataTalks.Club podcast guests describe building data, ML, AI, DataOps, and MLOps teams through hiring order, onboarding, role design, platform enablement, leadership, and cross-functional operating models."
related:
  - Data Teams
  - Hiring
  - Leadership
  - DataOps
  - MLOps
  - Platform Adoption
  - Self-Service Data Platforms
  - Data Engineering Platforms
---

Team building in data, ML, and AI starts with deciding what the team must make
possible for the business. In the DataTalks.Club podcast archive, guests rarely
describe team building as headcount growth alone. They talk about first hires
and manager-expert boundaries. They also cover onboarding, self-service
platforms, cross-functional planning, and the operating habits that let other
teams use data work.

Data teams need craft, context, and enablement. [Dat Tran]({{ '/people/dattran/' | relative_url }})
frames early ML team building around the product vision and company maturity in
[Building a Data Science Team]({{ '/podcasts/building-data-team/' | relative_url }}).
[Tammy Liang]({{ '/people/tammyliang/' | relative_url }}) shows the business
analytics version in
[Building and Leading Data Teams]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }}).
In that story, dashboards and data engineering come before forecasting and
adoption work.

[Lisa Cohen]({{ '/people/lisacohen/' | relative_url }}) adds the org
design layer in
[Designing a Data Science Organization]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }}).
She compares centralized, embedded, and hybrid teams.

## First Hires and Role Order

First hires should match the team's first real constraint. Tran argues that an
early startup needs experienced generalists because no system exists yet. His
pricing startup needed software engineers for the library and ML engineers for
modeling work. It also needed data engineers and a product manager. Designers
covered API and product experience.

At that stage, generalists matter because people need to handle several product
and infrastructure jobs before the company has stable role boundaries
([28:57-34:44]({{ '/podcasts/building-data-team/' | relative_url }})).

That guidance changes when the company already has some data foundations. Tran
uses Idealo as the middle case. The company had analysts, BI, and older data
engineering systems, so he didn't need only broad data science generalists. He
needed people who could add ML depth while still cooperating with data engineers
and putting work into production
([32:33-34:44]({{ '/podcasts/building-data-team/' | relative_url }})).
The hiring order therefore depends on company maturity, not on a universal data
team template.

Liang gives the same point from a consumer business that started with business
health dashboards. Her first hire was a data analyst because dashboard demand was
the immediate bottleneck. Historical data, forecasting, and source integration
became harder over time. At that point, a data engineer became a "game changer"
because analysts could return to analysis while the engineer built the data
foundation
([15:04-17:11]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

Looking back, Liang says she would invest in senior people earlier. Early
technical and analytical choices become the foundation for later work. If deeper
analyses or web apps need real infrastructure, she would also hire engineers. The
same applies when the team needs to combine multiple data sources
([23:11-29:18]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

This links team building to [hiring]({{ '/wiki/hiring/' | relative_url }}) and
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}).
Teams should hire for the constraint that slows useful work today and the
foundation they'll need next.

## Manager, Expert, and Senior IC Boundaries

Team building breaks when a company hires for the wrong role. [Barbara
Sobkowiak]({{ '/people/barbarasobkowiak/' | relative_url }}) explains this in
[Data Science Manager vs Expert]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }}).

She sees job descriptions that ask for a data science manager but mostly list
expert-level tools. Managers need broad technical literacy, strategy,
stakeholder communication, and team development. Experts need deep technical and
domain knowledge for hard modeling problems
([7:28-13:29 and 25:02-28:48]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }})).

The manager doesn't need to be the strongest coder on the team. Sobkowiak says a
manager should understand technologies well enough to discuss them with the team,
but expert depth belongs with the specialist. She also describes manager work as
setting learning goals and pairing people with senior teammates. Managers also
discuss progress and guide development without replacing code review systems
([12:02-24:25]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }})).

The role split changes by company size. Sobkowiak recommends a manager plus a
technical expert for larger organizations that need both coordination and deep
specialist skill. Startups may need one senior generalist with strong
communication because the budget and scope force one person to cover more ground
([30:37-34:42]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }})).
The risk is hiring a lone expert when the real need is team building, stakeholder
translation, and strategy.

[Katie Bauer]({{ '/people/katiebauer/' | relative_url }}) adds the manager hiring
bar in
[How to Hire, Manage, and Grow a Data Science Team in B2B SaaS]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }}).
Manager interviews should test team-building judgment, stakeholder management,
and career development. They should also test strategy, measurement, and
tradeoffs, not only technical fluency
([44:39-47:21]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).
That puts team building close to [leadership]({{ '/wiki/leadership/' | relative_url }}):
the manager role exists to create conditions for other people to deliver reliable
data work.

## Onboarding and Growth

Team building continues after the offer because Bauer treats junior hiring as a
build-versus-buy decision. Senior hires bring immediate impact, but junior hires
can grow into company-specific leaders when the team gives them mentorship. They
also need project-based learning, practice, and exposure.

Bauer recommends putting a senior in a domain before adding a junior. The junior
gets day-to-day support, and the senior gets a real mentoring path
([30:10-40:59]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).

Bauer also makes onboarding explicit. Junior people need to learn the technical
craft, but they also need to learn how companies work. Product managers, senior
leaders, and adjacent teams have goals and incentives that guide data work. Bauer
recommends helping juniors talk with those people and prepare questions. They
also need to ask for help when they're stuck
([32:43-38:04 and 52:43-55:44]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).

[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) gives the
manager onboarding version in
[Data Science Leadership]({{ '/podcasts/data-science-leadership-hiring-mlops/' | relative_url }}).
When he took over a team, he used the first part of his 30-60-90 plan to meet
people and listen. He learned the projects and domain before giving stronger
feedback. He also treats one-on-ones and feedback as a growth environment rather
than a manager monologue
([12:52-17:26 and 40:25-48:13]({{ '/podcasts/data-science-leadership-hiring-mlops/' | relative_url }})).

Liang adds the scaling leadership example. As her team grew, she moved away from
holding every project herself and gave ownership to the people doing the work. Her
role became direction, resource support, and troubleshooting when the team could
not unblock a project
([50:52]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).
Together, these episodes make onboarding a team design problem. People need
technical support, business context, ownership, and predictable ways to ask for
help.

## Org Design and Cross-Functional Work

Data teams can be centralized, embedded, or hybrid, and each model changes how
team building works. Cohen describes centralized teams where data scientists
report to data science managers while aligning to business partners. She also
describes decentralized teams where data scientists report directly into product
or engineering groups. A hybrid model centralizes data science at a division or
area level while keeping daily work close to product teams
([6:27-10:44 and 24:53]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).

When teams embed data scientists, those data scientists gain domain context and
faster decision paths. They can lose peer learning, mentorship, and career
clarity if the organization doesn't protect data craft. When leaders centralize
data science, teams gain knowledge sharing and consistency. They must work harder
to build product context and avoid looking academic or detached
([25:48-29:31]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).

Bauer's matrix-org discussion turns that tradeoff into a manager responsibility.
A data scientist may report to a data leader while working day to day with a
product manager, engineering manager, or marketing lead. The data manager then
protects craft quality, documentation, peer review, and career growth even when
the dotted-line stakeholder shapes daily priorities
([8:33-14:06]({{ '/podcasts/hiring-and-managing-data-science-teams-in-b2b-saas/' | relative_url }})).

Cohen also shows why cross-functional planning has to happen at multiple levels.
Data science leaders need product, engineering, design, and research partners.
Managers need their counterparts, and individual contributors need regular
alignment with the people building or using the product. Those teams use shared
OKRs and planning rhythms to move toward the same goals
([18:43-24:03]({{ '/podcasts/data-science-team-structure-and-org-design/' | relative_url }})).
This is the org-design side of [data teams]({{ '/wiki/data-teams/' | relative_url }})
and [communication]({{ '/wiki/communication/' | relative_url }}).

## Platform and DataOps Enablement

Data and ML team building eventually becomes platform work. [Lars
Albertsson]({{ '/people/larsalbertsson/' | relative_url }}) describes the shift
at Spotify in
[DataOps 101]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }}).
The core data team was swamped with internal requests, so it stopped acting only
as an implementation bottleneck. It built tooling and workflows that let other
teams deploy and fix their own data pipelines. Early success came from embedding
with early adopter teams and learning where the platform was missing pieces
([7:52-11:50]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

Albertsson defines DataOps through enablement and people alignment, with
workflows and tooling supporting that goal. He also cautions that not every
organization should push non-technical self-service all the way. Sometimes the
better team design is to embed analysts and data engineers together. When teams
mix those competencies, they remove the wall between requesters and platform
builders
([11:50-11:57 and 50:13-57:16]({{ '/podcasts/dataops-principles-and-scalable-data-platforms/' | relative_url }})).

[Mehdi OUAZZA]({{ '/people/mehdiouazza/' | relative_url }}) gives the scale-up
version in
[Scaling Data Engineering Teams]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }}).
A data platform team may serve dozens of analysts and data scientists whose
numbers and use cases are growing quickly. The platform team has to stop being a
dependency. It can do that with onboarding sessions, support channels, and
documentation. OUAZZA also names Airflow conventions, playbooks, schemas, and
data contracts
([12:30-23:26]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).

OUAZZA also ties platform team building to seniority. Scale-ups should bring in
senior people early for practices that need to survive fast growth. That matters
even more when the team needs niche technology such as streaming.

As the organization grows, general data engineering work may split into platform
and warehouse roles. Streaming and services may become separate roles too
([20:13 and 50:17-54:55]({{ '/podcasts/scaling-data-engineering-teams-self-service-platforms/' | relative_url }})).
That connects team building to [DataOps]({{ '/wiki/dataops/' | relative_url }}),
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}).

## MLOps Teams and Production AI

MLOps teams need a different skill mix because they support models after the
notebook stage. [Raphael Hoogvliets]({{ '/people/raphaelhoogvliets/' | relative_url }})
describes an MLOps team as a centralized enabling team in
[MLOps at Scale]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }}).
His team supports product teams and embedded ML engineers with infrastructure
and best practices. It also covers deployment, maintenance, monitoring, and
reusable tools
([23:01-25:20]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

Hoogvliets argues that the team needs more than tool builders. It needs an
evangelist or executive advocate and a technical translator. It also needs
experienced technical leadership, MLOps engineers, and ML engineers. Data science
skill and SRE or DevOps skill matter too. Software engineering and data
engineering also belong in the mix.

Not everyone needs the same background, but the team needs the full mix
([16:58-20:33 and 45:10-48:15]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

[Simon Stiebellehner]({{ '/people/simonstiebellehner/' | relative_url }}) adds
the platform trigger in
[Building Production ML Platforms]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }}).
Teams shouldn't build a heavy ML platform before there's repeated model work and
clear business value. When the need exists, useful platform pieces include
self-service compute, experiment tracking, and a model registry. They also
include orchestration and batch or online deployment paths. Metadata, lineage,
and monitoring complete the platform surface
([16:52-31:51 and 42:48-49:19]({{ '/podcasts/building-production-ml-platform-and-mlops-team/' | relative_url }})).

Hoogvliets and Stiebellehner both treat MLOps team building as adoption work.
The team should collect pain points, find quick wins, and keep developer
experience in view. If models are opaque in production, start with monitoring.
If releases are slow, start with CI/CD. If version control is missing, start
there
([27:56-36:55 and 48:41-49:52]({{ '/podcasts/mlops-at-scale-reproducibility-adoption/' | relative_url }})).

The team succeeds when product teams can use the platform and trust the path to
production, not when the platform catalog is long.

## Adoption, Trust, and Data Culture

Team building is incomplete when other departments don't use the outputs.
Liang says her team added a business analyst or data researcher because tools and
dashboards weren't enough. Someone had to communicate what the data team was
building, publish short updates, run workshops, and help the business side use
the work
([18:41-18:59]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

Her team changed its workshops after lecture-style demos failed. Instead of only
showing dashboard features, they used Q&A sessions where people practiced finding
answers. That improved attention and helped build data culture
([49:00]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).
This mirrors [data product management]({{ '/wiki/data-product-management/' | relative_url }}).
The output has to fit a decision, a user, and a context of use.

Trust also depends on accuracy and reliability. Liang describes rebuilding trust
after data errors by adding playbooks and dbt tests. Her team also added regular
checks
([35:38-40:09]({{ '/podcasts/building-and-scaling-data-team/' | relative_url }})).

[Rahul Jain]({{ '/people/16rahuljain/' | relative_url }}) makes a related point
from data engineering leadership in
[Data Engineering Leadership]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }}).
He ties management to stakeholder prioritization, quality standards, data
reconciliation, and access controls. He also ties it to data culture
([4:52-13:15 and 25:04-30:50]({{ '/podcasts/data-engineering-leadership-and-modern-data-platforms/' | relative_url }})).

Tran adds expectation management for AI teams. New data science teams often face
inflated leadership expectations because "AI" sounds powerful. He recommends
educating management on what the team can and can't do, so the team isn't set up
to fail
([56:40]({{ '/podcasts/building-data-team/' | relative_url }})).
For data and AI leaders, adoption work includes communication and workshops. It
also includes quality checks, business education, and stakeholder trust.

## Adjacent Topics

[Data Teams]({{ '/wiki/data-teams/' | relative_url }}) covers the broader
organizational models behind these decisions. [Hiring]({{ '/wiki/hiring/' | relative_url }})
goes deeper into role definition, interview design, and recruiter-manager
alignment. [Leadership]({{ '/wiki/leadership/' | relative_url }}) expands the
manager, senior IC, coaching, and stakeholder side of team building.

For platform-heavy teams, use [DataOps]({{ '/wiki/dataops/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }}). For the
enablement surface, use
[platform adoption]({{ '/wiki/platform-adoption/' | relative_url }}),
[self-service data platforms]({{ '/wiki/self-service-data-platforms/' | relative_url }}),
and [platform engineering]({{ '/wiki/platform-engineering/' | relative_url }}).
