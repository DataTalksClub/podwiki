---
layout: wiki
title: "Data Science Project Management"
summary: "How DataTalks.Club guests manage data science, analytics, and ML projects through problem framing, scope, stakeholders, baselines, metrics, evaluation, adoption, and production handoff."
related:
  - Data Science
  - Business Skills for Data Professionals
  - Data Product Management
  - Machine Learning System Design
  - Evaluation
  - Metrics
  - Leadership
  - Data Teams
  - Production ML Project Checklist
---

Data science project management is the operating discipline that turns an
ambiguous business, analytics, or machine learning request into useful shipped
work. It covers problem framing and stakeholder alignment. It also covers data
access, baselines, and metrics. Delivery cadence, evaluation, adoption, and
production handoff belong in the same management work.

It sits between [Data Science]({{ '/wiki/data-science/' | relative_url }}),
[Business Skills for Data Professionals]({{ '/wiki/business-skills-for-data-professionals/' | relative_url }}),
[Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}), and
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
It also depends on [Leadership]({{ '/wiki/leadership/' | relative_url }}).

DataTalks.Club guests treat data science project management as technical work
and organizational work. In [CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}),
teams start by understanding the business and preparing data. They model and
evaluate next. They deploy when the result is ready to leave analysis.

In [From Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}),
[Ksenia Legostay]({{ '/people/ksenialegostay/' | relative_url }}) treats planning
and stakeholder communication as useful after the work moves into analytics and
machine learning. KPI work stays useful too.

## Decision, Evidence, and Delivery

Across the podcast episodes, managing a data science project means keeping the
decision, evidence, and delivery path aligned. The manager or lead asks what
business objective the work serves. They also ask whether the problem is
measurable, what data exists, which baseline is good enough, and how the result
will be used.
In [CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}), the 13:25 section
frames the problem as important, measurable, and connected to a way to measure
success. The 17:05 and 18:23 sections keep baselines, evaluation, and business
objectives together rather than treating modeling as an isolated phase.

That definition also appears in data product work. In [Building Data Products
at Scale]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }}),
[Ioannis Mesionis]({{ '/people/ioannismesionis/' | relative_url }}) describes an
operating model with intake, prioritization, and Definition of Done. KPIs and
feasibility checks come before pilots. Later work includes A/B tests and
rollout. Monitoring, demos, and stakeholder feedback also stay in the lifecycle
([14:00-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

That project structure links data science management to [Data Products]({{ '/wiki/data-products/' | relative_url }}),
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }}),
[Evaluation]({{ '/wiki/evaluation/' | relative_url }}), and [Metrics]({{ '/wiki/metrics/' | relative_url }}).

## Different Management Risks

The guests don't disagree that data science projects need structure. They focus
on different risks.

Ksenia Legostay focuses on transferable project-management craft. Around 22:32
in [From Project Manager to Data Scientist]({{ '/podcasts/project-manager-to-data-scientist/' | relative_url }}),
she treats planning, stakeholder communication, and business KPIs as strengths
that transfer into data work. Around 30:20, she names CRISP-DM as a useful
project framework. Around 41:07, she adds Git and testing. She also adds Docker,
deployment, and clean code because a project that affects other people can't remain only a
notebook.

Ioannis Mesionis focuses on lifecycle control. His lead data scientist role is
embedded with marketing stakeholders. The work still goes through a single
front door, Definition of Done, and feasibility checks. It then moves through
sprint or Kanban delivery, pilots, A/B testing, and production rollout
([7:23-27:25]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

That view is close to [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }}).
The project isn't complete until the product can be used, measured, and
operated.

[Shir Meir Lador]({{ '/people/shirmeirlador/' | relative_url }}) focuses on
uncertainty management in [Data Science Management and Agile Machine Learning]({{ '/podcasts/data-science-management-and-agile-machine-learning/' | relative_url }}).
Her management discussion covers roadmaps, debrief culture, and business
impact. It also covers cross-functional partnerships, exploration sprints,
design stories, and incremental movement from POC to production
([9:18-17:23 and 41:06-54:59]({{ '/podcasts/data-science-management-and-agile-machine-learning/' | relative_url }})).
That focus belongs with [Data Teams]({{ '/wiki/data-teams/' | relative_url }})
and [Data Team Lead Role]({{ '/wiki/data-team-lead-role/' | relative_url }}).
The project manager protects learning speed and delivery discipline at the same
time.

## Framing and Scope

The first management task is to turn a request into a decision. A request for a
forecast, dashboard, model, or segmentation usually hides several questions.
The manager has to ask who will act, what will change, what cost matters, and
what answer would be good enough. In [CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}), the 7:55,
10:58, and 13:25 sections move from an online classified-site example to
measurable problem size and success criteria. That's the project-management
moment before modeling starts.

Project managers should include non-goals and a smallest useful path. [Valeriy
Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}) makes that explicit
for [ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
in [ML System Design Playbook]({{ '/podcasts/ml-system-design/' | relative_url }}).
At 7:06 and 14:36, design documents help teams fail early and align
stakeholders. At 19:01, the document remains alive as the system changes.

For project managers, this means scope isn't a fixed wish list. It's a written
agreement about the decision, assumptions, risks, and next review point.

The team also decides whether the answer should be analysis, analytics
engineering, a model, or a productized ML system. [Anna Hannemann]({{ '/people/annahannemann/' | relative_url }})
gives that product-owner judgment in [Product Owners in Data Science]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }}).
The right next step may be manual cleanup, an MVP, or staged investment rather
than a model
([44:48-53:09]({{ '/podcasts/building-data-products-product-owner-vs-product-manager/' | relative_url }})).
Use [Data Product Owner vs Data Product Manager]({{ '/comparisons/data-product-owner-vs-data-product-manager/' | relative_url }})
when the scope question is about who owns the delivery and product
decision.

## Stakeholders and Decision Rights

Data science projects fail when stakeholders agree to a title but not to a
decision path. [Loris Marini]({{ '/people/lorismarini/' | relative_url }})
starts [Business Skills for Data Professionals in SaaS]({{ '/podcasts/data-professionals-business-skills-in-saas/' | relative_url }})
with shared meaning for words such as customer, usage, and churn. Around 25:53
and 35:20, he ties trust to active listening, stakeholder mapping, and recording
roles and context. That's project infrastructure, not presentation polish.

Mesionis gives the delivery version. His marketing data science team uses
weekly embedded meetings and stakeholder observation before formal intake
([7:23-15:23]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).
Later, the team invites stakeholders to demos rather than daily stand-ups. They
also simplify technical results for non-technical audiences
([35:38-41:33]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).
This keeps stakeholders close to direction and feedback while the delivery team
keeps space for exploration and technical work.

For managers, decision rights are part of team design. [Barbara
Sobkowiak]({{ '/people/barbarasobkowiak/' | relative_url }}) separates data
science managers from experts in [Data Science Manager vs Expert]({{ '/podcasts/data-science-manager-vs-expert-hiring-guide/' | relative_url }}).
Around 8:22 and 15:49, the manager needs enough technical literacy and strategy
to redirect work when good enough is enough. Around 31:56 and 34:04, she warns
that companies sometimes hire deep experts when the real gap is coordination,
translation, and team development. That distinction links project management to
[Data Scientist Role]({{ '/wiki/data-scientist-role/' | relative_url }}) and
[Leadership]({{ '/wiki/leadership/' | relative_url }}).

## Baselines, Metrics, and Definition of Done

Baselines make progress visible before the final model exists. In [CRISP-DM]({{ '/podcasts/crisp-dm/' | relative_url }}),
the 17:05 section treats a sufficient baseline as a reason to move to
evaluation. In [Machine Learning System Design Interviews]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
Valeriy connects baselines and metrics to system design around 24:28. Around
46:02, he adds A/B testing, monitoring, and fallbacks. Project managers should
therefore ask for a baseline early, not after a complex model has consumed the
budget.

Metrics need a decision owner and a unit of action. [Adam Sroka]({{ '/people/adamsroka/' | relative_url }})
frames KPI design as top-down alignment with executive decisions in [KPI Design
& Metrics Strategy]({{ '/podcasts/ml-engineering-kpis-and-metrics-strategy/' | relative_url }})
around 22:41. He then warns about vanity metrics and KPI gaming around 26:07
and 28:04. For managed projects, [Metrics]({{ '/wiki/metrics/' | relative_url }})
aren't only dashboard numbers. They're acceptance criteria, guardrails, and
review triggers.

Mesionis makes that concrete with Definition of Done. His team defines KPIs and
success criteria before deep delivery work. It also defines fail-fast checks
([17:37-25:17]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).
The same project can need an offline metric, an A/B test, and stakeholder
feedback. It may also need monitoring and a production support plan.

The [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
is the closer checklist when the project changes a live system.

## Delivery Under Uncertainty

Data science work is hard to estimate because data access, labels, model
behavior, and stakeholder needs can change the plan. Shir Meir Lador's agile ML
discussion names that uncertainty directly. Around 41:06, she discusses data
risks and unknowns. Around 44:18 and 45:36, she uses exploration tasks and
design stories to manage ML work. Grooming practices and iterative milestones
also keep the work from pretending it behaves like ordinary feature delivery
([Data Science Management and Agile Machine Learning]({{ '/podcasts/data-science-management-and-agile-machine-learning/' | relative_url }})).

Mesionis uses Kanban to plan sprints and estimate work, while demos keep
stakeholder feedback in the lifecycle. His team also keeps feasibility
assessment, MVPs, and fail-fast checks
([20:54-40:49]({{ '/podcasts/building-data-products-lead-data-scientist/' | relative_url }})).

That matches the [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
habit of writing goals, non-goals, assumptions, and data paths before the work
becomes expensive. Serving constraints and monitoring belong in the same design.

Project managers should keep the delivery unit small enough to learn.

A useful increment might be a small validation or delivery milestone:

- a validated dataset
- a baseline notebook
- a dashboard with agreed metric definitions
- a design document
- a pilot
- a shadow-mode model
- a monitored batch job

For product-facing experiments, [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }})
and [Product Analytics]({{ '/wiki/product-analytics/' | relative_url }}) help
separate a real rollout decision from a promising internal score.

## Evaluation, Adoption, and Handoff

Evaluation is where project management checks whether the work should continue,
change, ship, or stop. In [From Analytics to Production ML]({{ '/podcasts/production-ml-mlops-and-data-team-building/' | relative_url }}),
[Rishabh Bhargava]({{ '/people/rishabhbhargava/' | relative_url }}) describes
production ML as experimental. Around 28:42, offline experiments, shadow mode,
and A/B tests bridge model work to product impact. Around 31:19, segment
analysis and root-cause work explain live results. That's why [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
belongs in the project plan, not only in the modeling phase.

Adoption is also part of completion. [Caitlin Moorman]({{ '/people/caitlinmoorman/' | relative_url }})
argues in [Last-Mile Data Delivery]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})
that data products can fail when users don't know they exist. They can also
fail when users don't understand or trust them. Sometimes they don't see how the
product fits the decision
([24:13-40:53]({{ '/podcasts/last-mile-data-delivery-and-data-product-adoption-modern-data-stack/' | relative_url }})).

For project management, adoption work includes discoverability,
interpretability, and workflow placement. Documentation and feedback loops
belong there too.

Production handoff should name the owner of data quality and model behavior.
It should also name owners for alerts, rollback, and stakeholder communication.
[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }})
connects project intake, KPIs, stakeholder fears, and service levels in
[Human-Centered MLOps and Model Monitoring]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
She also connects post-mortems, drift, and user feedback to the same operating
model
([4:50-29:23 and 46:28-50:30]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})).

That handoff links [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), and
[Production]({{ '/wiki/production/' | relative_url }}). A project is unfinished
if nobody knows what happens when the metric moves, the input data changes, or
the model stops helping the user.

## Related Pages

These pages cover the neighboring practices and role boundaries.

- [Data Science]({{ '/wiki/data-science/' | relative_url }})
- [Business Skills for Data Professionals]({{ '/wiki/business-skills-for-data-professionals/' | relative_url }})
- [Data Product Management]({{ '/wiki/data-product-management/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [Metrics]({{ '/wiki/metrics/' | relative_url }})
- [Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
- [Data Product Owner vs Data Product Manager]({{ '/comparisons/data-product-owner-vs-data-product-manager/' | relative_url }})
- [Machine Learning Engineer Roadmap]({{ '/roadmaps/machine-learning-engineer-roadmap/' | relative_url }})
