---
layout: wiki
tags: ["transition"]
title: "Marketing to Analytics Engineering"
summary: "How marketers can move into analytics engineering through SQL, BI, dbt, product analytics, dashboards, and metric ownership."
related:
  - Career Transitions in Data
  - Analytics Engineering
  - Analytics Engineering Roadmap
  - Product Analytics
  - dbt
  - Business Intelligence
  - Dashboard and Metric Layer Project Checklist
  - Data Analyst Role
  - A/B Testing
  - Data Warehouse
---

Marketing to analytics engineering is the move from using campaign and funnel
metrics to owning reusable analytical data products. The marketer already knows
why acquisition, conversion, retention, and experiments matter. The
[[analytics engineering]]
side adds SQL models, tested transformations, metric definitions, and BI-ready
tables.

[[person:nikolamaksimovic|Nikola Maksimovic]] gives the
clearest example. At Ecosia, performance marketing led into marketing reporting
during a Tableau-to-Looker migration
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's performance-marketing and Looker migration discussion at 2:53-7:18]]).
That work then led into SQL learning and BI projects
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's BI transition and required skills discussion at 8:45-14:14]]).
Later it included dbt modeling, LookML reporting, product analytics, and A/B
testing support
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's product analytics and funnel-knowledge discussion at 38:27-41:50]]).

The transition isn't just a move from "business" to "technical" work.
Marketing knowledge stays valuable because it supplies acquisition-funnel
context, user-journey context, and campaign pressure. Analytics engineering
changes the output. A repeated campaign report becomes a maintained model.
Funnel intuition becomes
[[product analytics]] or
[[data-led-growth|data-led growth]] work
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's dbt migration and modeling discussion at 18:34-33:46]],
[[podcast:data-led-growth-event-tracking-and-reverse-etl|Choudhury's tracking-plan and growth-stack discussion at 13:34-30:03]]).

## Turn Marketing Questions Into Shared Data Products

Marketing to analytics engineering means using marketing domain knowledge as an
entry point into governed analytical data. The person moving roles learns to
turn marketing questions into reusable tables, documented metrics, tests, and
dashboards that other teams can trust.

Maksimovic's route started with marketing reporting during the Looker move,
then shifted toward a marketing-analyst bridge with the BI team. SQL was the
main gap. Pipeline understanding, Python basics, and practice with larger data
models followed
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's marketing-to-BI pivot discussion at 7:18-12:50]]).

[[person:victoriaperezmola|Victoria Perez Mola]]
defines the target role through SQL transformations and [[dbt]]
tests. She also names documentation, DAGs, Looker, and Snowflake. The role
works with analysts, data scientists, and backend teams
([[podcast:analytics-engineer-skills-tools|Perez Mola's role and dbt workflow discussion at 4:05-11:48]],
[[podcast:analytics-engineer-skills-tools|Perez Mola's collaboration discussion at 33:02-36:44]]).

This puts the transition next to
[[Data Analyst vs Analytics Engineer]],
the [[Analytics Engineering Roadmap]],
and the broader [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]].
Marketing gives the person questions and metric meaning. Analytics engineering
adds model ownership, quality checks, and shared analytical assets.

## Navigate Role Boundaries and Tool Choices

The role boundary is often negotiated through the work before it appears as a
clean job title. Maksimovic's team didn't start with a clean
analytics-engineer title. The work overlapped BI analyst, data analyst, and
analytics-engineer responsibilities because the team was small
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's analyst-versus-analytics-engineer discussion at 25:06-28:40]]).

[[person:juanmanuelperafan|Juan Manuel Perafan]]
pushes against defining analytics engineering only as a role between analyst
and engineer. He starts from messy business reality, then connects that work to
safer data systems and software engineering practice
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Perafan's business-reality and clean-data discussion at 7:56-16:25]]).
He also treats team-role splits as an organizational choice, not a universal
rule
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Perafan's team-role split discussion at 26:53-30:35]]).

Tool choice is part of that boundary, but it shouldn't define the transition.
Maksimovic says dbt strongly shaped the analytics-engineering title, but she
still separates the role from the tool. Data modeling theory matters more than
simply using dbt
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's dbt influence and modeling-theory discussion at 28:40-33:46]]).

[[person:nataliekwong|Natalie Kwong]] places dbt inside
a broader [[modern data stack]]
with ingestion and warehouse storage. Orchestration, CDC, and reverse flows
remain part of the same system
([[podcast:data-engineering-tools-modern-data-stack|Kwong's data-marts and ingestion discussion at 15:30-18:47]]).
She later connects Airbyte and dbt to orchestration
([[podcast:data-engineering-tools-modern-data-stack|Kwong's Airbyte, dbt, and orchestration discussion at 31:31-33:45]]).
CDC and schema evolution belong to the same system
([[podcast:data-engineering-tools-modern-data-stack|Kwong's CDC and schema-evolution discussion at 45:59-49:32]]).

[[person:arpitchoudhury|Arpit Choudhury]] adds a
growth-data boundary. In his data-led-growth episode, marketing-adjacent data
work extends beyond dashboards. It includes
[[event tracking]] and
[[tracking plans]]. It also includes
BI and warehouse transformations. Customer data platforms and
[[reverse ETL]] extend that work
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Choudhury's tracking-plan and warehouse-flow discussion at 13:34-30:03]]).

He treats reverse ETL and CDPs as separate tradeoff choices for activating that
data
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Choudhury's reverse-ETL and CDP tradeoff discussion at 37:25-44:24]]).

That makes the transition useful for people who want to specialize in
[[data activation]] as well as BI.

## Start With Marketing Reporting

The bridge usually begins with reporting that's already close to marketing
work. Maksimovic valued performance marketing because campaign metrics gave
fast feedback on whether work was effective. When Ecosia moved to Looker,
Maksimovic helped build marketing-team reporting and already understood the
questions
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's campaign-metric discussion at 2:53-7:04]]).

The first reporting project turns domain knowledge into visible data work. A
marketer can clean up a campaign report or clarify funnel definitions. They can
also turn repeated dashboard logic into a shared query.

In Maksimovic's case, BI-team conversations and BI projects happened alongside
marketing work
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's internal BI-pathway discussion at 9:53-14:14]]).
Looker and LookML reporting became more proof that she could move into a data
role
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's Looker and LookML reporting discussion at 23:12-24:51]]).

Her first reusable data work was marketing reporting during the
Tableau-to-Looker migration. It also included brand-campaign measurement and
dashboard work while she was still close to marketing. The transition grew
through [[Business Intelligence]]
and the
[[Dashboard and Metric Layer Project Checklist]],
not only to analytics-engineering titles.

## Build SQL, BI, and Modeling Skill

Because Maksimovic names SQL as the main skill gap, the technical path starts
there. Pipeline understanding and Python basics follow. Maksimovic also
describes more advanced practice: reading and writing complex SQL over larger
models, not only beginner queries
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's SQL and pipeline-skills discussion at 8:45-12:50]]).

BI work turns those queries into user-facing evidence. Maksimovic recommends
moving from Excel and pivot tables into SQL datasets, then building dashboards
in tools such as Looker or Tableau. That order lets a learner see how modeled
data becomes stakeholder reporting
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's Excel-to-SQL-to-dashboard playbook at 41:50-45:09]]).
She also warns that generic SQL exercises leave a gap. Reading real BI-team SQL
that builds main tables is stronger practice when a company can share it.

Maksimovic's [[dbt]] migration made model
ownership the next step. It covered transformations, model organization,
wide-versus-narrow tables, and incrementalization tradeoffs
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's dbt migration and modeling tradeoffs discussion at 18:34-33:46]]).

Perez Mola ties the role to Looker and Snowflake. She also names dbt tests and
DAGs
([[podcast:analytics-engineer-skills-tools|Perez Mola's toolstack discussion at 10:04-11:48]]).
Kwong explains why these skills sit inside an ELT system with ingestion and
warehouse transformations
([[podcast:data-engineering-tools-modern-data-stack|Kwong's ELT and analytics-engineer discussion at 7:57-15:30]]).
She also connects that system to reverse flows
([[podcast:data-engineering-tools-modern-data-stack|Kwong's operational reverse-flow discussion at 35:42-39:06]]).

## Transfer Funnel Knowledge Into Product Analytics

Marketing context transfers best when the person knows what a funnel means
before writing the model. Maksimovic names marketing funnels, conversion
funnels, and web acquisition funnels as useful prior knowledge. She also names
user journeys, touch points, optimization, and growth. That background helped
her support product managers and keep the user journey visible while building
analytical outputs
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's funnel and user-journey discussion at 39:36-41:50]]).

Her analytics-engineering work then extended into growth, retention, and RFM
analysis. It also included NLP experiments and dashboards. A/B testing support
was part of the same work
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's product-support and A/B testing discussion at 14:14-18:34]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's growth, retention, and RFM discussion at 38:27-39:36]]).

That makes [[a-b-testing|A/B Testing]] and
[[Experiment Tracking]]
direct adjacent topics for this transition. Choudhury's growth-stack episode
shows why this work needs reliable event
names and properties. It also needs source context and owners. Warehouse
storage, BI, and activation tools matter too, not only a campaign dashboard
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Choudhury's tracking-plan and data-flow discussion at 13:34-30:03]]).

That's the practical connection to [[Product Analytics]],
[[Event Tracking]],
[[Tracking Plans]], and
[[Metrics]]. The marketer's advantage is
knowing the business question. The analytics-engineering requirement is making
the answer reusable and trustworthy.

## Prove the Transition With Internal Work or Portfolio Projects

Maksimovic used internal proof instead of jumping directly from marketing into
an external analytics-engineering role. Marketing reporting and the Looker
migration showed the transition in the same organization. BI-team
conversations, BI projects, and product analytics work also mattered
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's BI pathway and side-project discussion at 7:18-14:14]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's Looker reporting discussion at 23:12-24:51]]).

An external [[analytics-engineering-portfolio-projects|analytics-engineering portfolio]]
should make the same evidence visible, especially for readers following a
[[career-transitions-in-data|career transition]] path.

Project examples include:

- a campaign reporting mart
- a web acquisition funnel model
- a retention or RFM model
- an A/B testing readout
- a [[dbt]] migration from duplicated dashboard SQL
- a reverse-ETL segment project

These projects fit the transition when they define the grain and document
metric logic
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's dbt-modeling and funnel-knowledge discussion at 18:34-33:46 and 38:27-41:50]]).
They also need dbt-style tests and BI outputs from shared models
([[podcast:analytics-engineer-skills-tools|Perez Mola's dbt-tests and collaboration discussion at 4:05-11:48 and 33:02-36:44]]).
Reverse-ETL projects should make the activation tradeoff explicit
([[podcast:data-led-growth-event-tracking-and-reverse-etl|Choudhury's reverse-ETL and CDP tradeoff discussion at 37:25-44:24]]).

The strongest project artifact shows the before-and-after. Show the duplicated
campaign or brand-dashboard SQL, then show the modeled table or dbt layer that
replaced it. Include the metric grain and the BI surface that consumes it.

## Find Sponsorship and Team Structure

The transition is easier when an existing BI or data team can sponsor practical
work. Maksimovic describes conversations with a BI colleague and a BI analyst
who helped her learn Looker. Later teammates served as mentors once she joined
the BI team
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's BI-team conversations discussion at 9:53-11:02]],
[[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's mentorship and sponsorship discussion at 45:09-50:23]]).
That makes dashboard migration, dbt adoption, and product analytics support
useful openings for marketers already inside companies with reporting needs.

Small teams can blur role boundaries. Maksimovic's BI team was small enough
that people did both analysis and analytics-engineering work
([[podcast:from-marketing-to-analytics-engineering-sql-dbt-career-switch|Maksimovic's small-team role-boundary discussion at 25:06-28:40]]).

[[person:tammyliang|Tammy Liang]] gives a related team
growth example for marketers already near business reporting. Dashboards and
business-health monitoring grew into warehouse and dbt work. Data Studio and
Notion documentation came next. Testing and monitoring followed
([[podcast:building-and-scaling-data-team|Liang's dashboards-to-warehouse discussion at 7:22-18:41]],
[[podcast:building-and-scaling-data-team|Liang's dbt, documentation, and monitoring discussion at 22:32-41:42]]).

## Related Pages

Continue through the role, stack, and transition pages that this path depends
on:

- [[Analytics Engineering]]
- [[Analytics Engineering Roadmap]]
- [[data-analyst-to-analytics-engineer|Data Analyst to Analytics Engineer Roadmap]]
- [[Analytics Engineering Portfolio Projects]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[Data Analyst vs Analytics Engineer]]
- [[Business Intelligence]]
- [[Product Analytics]]
- [[a-b-testing|A/B Testing]]
- [[data-led-growth|Data-Led Growth]]
- [[Event Tracking]]
- [[Metrics]]
- [[Modern Data Stack]]
- [[Data Quality and Observability]]
- [[career-transitions-in-data|Career Transition]]
