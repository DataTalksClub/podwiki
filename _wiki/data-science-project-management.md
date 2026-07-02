---
layout: wiki
title: "Data Science Project Management"
summary: "How DataTalks.Club guests manage data science, analytics, and ML projects through problem framing, scope, stakeholders, baselines, metrics, evaluation, adoption, and production handoff."
keyword: "data science project management"
secondary_keywords:
  - "project management for data science"
  - "data science project manager"
  - "managing data science projects"
  - "data science project planning"
  - "machine learning project management"
related:
  - Data Science
  - Business Skills for Data Professionals
  - Data Product Management
  - Data Science for Managers
  - Machine Learning System Design
  - Evaluation
  - Metrics
  - Leadership
  - Data Teams
  - Production ML Project Checklist
---

Data science project management is the operating discipline that turns an
ambiguous business, analytics, or machine learning request into useful shipped
work. A data science project manager or data lead turns the decision into a
measurable target. They keep the smallest useful version explicit, plan the
shipping path, and name the handoff owner.

The practice draws from [[Data Science]],
[[Business Skills for Data Professionals]],
[[Data Product Management]], and
[[Machine Learning System Design]].
It also depends on [[Leadership]] and
[[Data Science for Managers]],
because the work combines technical uncertainty with team coordination.

DataTalks.Club guests treat data science project management as technical work
and organizational work. In [[podcast:crisp-dm|CRISP-DM]],
teams start by understanding the business and preparing data. They model and
evaluate next. They deploy when the result is ready to leave analysis.
[[book:20241118-why-data-science-projects-fail-harsh-realities-of-implementing-ai-and-analytics-without-hype-chapman-hall-crc-data-science-series|Why Data Science Projects Fail]]
by Evan Shellshear and Douglas Gray grounds the same failure modes the podcast
returns to repeatedly: misaligned business framing, over-scoped pilots, and
projects that never reach production adoption.
[[book:20221010-managing-machine-learning-projects|Managing Machine Learning Projects]]
by Simon Thompson covers the same project lifecycle from the delivery side: scoping, risk management, and stakeholder alignment for ML-specific work.

In [[podcast:project-manager-to-data-scientist|From Project Manager to Data Scientist]],
[[person:ksenialegostay|Ksenia Legostay]] treats planning
and stakeholder communication as useful after the work moves into analytics and
machine learning. KPI work stays useful too.

## Project Lifecycle

Across the podcast episodes, guests mostly agree that project management for
data science starts before modeling and ends after the first analysis or model
result. The manager or lead asks what business objective the work serves and
whether the problem is measurable. They also ask what data exists, which
baseline is good enough, how the result will be used, and what operational
owner receives the handoff.
In [[podcast:crisp-dm|CRISP-DM]], the 13:25 section
frames the problem as important, measurable, and connected to a way to measure
success. The 17:05 and 18:23 sections keep baselines, evaluation, and business
objectives together rather than treating modeling as an isolated phase.

That definition also appears in data product work. In [[podcast:building-data-products-lead-data-scientist|Building Data Products
at Scale]],
[[person:ioannismesionis|Ioannis Mesionis]] describes an
operating model with intake, prioritization, and Definition of Done. KPIs and
feasibility checks come before pilots. Later work includes A/B tests and
rollout. Monitoring, demos, and stakeholder feedback also stay in the lifecycle
([[podcast:building-data-products-lead-data-scientist|14:00-41:33]]).

That project structure links data science management to [[Data Products]],
[[Data Product Adoption]],
[[Evaluation]], and [[Metrics]].

## Risk Emphasis

The guests don't disagree that data science projects need structure. They focus
on different risks.

Ksenia Legostay focuses on transferable project-management craft. Around 22:32
in [[podcast:project-manager-to-data-scientist|From Project Manager to Data Scientist]],
she treats planning, stakeholder communication, and business KPIs as strengths
that transfer into data work. Around 30:20, she names CRISP-DM as a useful
project framework. Around 41:07, she adds Git and testing. She also adds Docker,
deployment, and clean code because a project that affects other people can't remain only a
notebook.

Ioannis Mesionis focuses on lifecycle control. His lead data scientist role is
embedded with marketing stakeholders. The work still goes through a single
front door, Definition of Done, and feasibility checks. It then moves through
sprint or Kanban delivery, pilots, A/B testing, and production rollout
([[podcast:building-data-products-lead-data-scientist|7:23-27:25]]).

That view is close to [[Data Product Management]].
The project isn't complete until the product can be used, measured, and
operated.

[[person:shirmeirlador|Shir Meir Lador]] focuses on
uncertainty management in [[podcast:data-science-management-and-agile-machine-learning|Data Science Management and Agile Machine Learning]].
Her management discussion covers roadmaps, debrief culture, and business
impact. It also covers cross-functional partnerships, exploration sprints,
design stories, and incremental movement from POC to production
([[podcast:data-science-management-and-agile-machine-learning|9:18-17:23 and 41:06-54:59]]).
That focus belongs with [[Data Teams]]
and [[Data Team Lead Role]].
The project manager protects learning speed and delivery discipline at the same
time.

[[person:yurykashnitsky|Yury Kashnitsky]] makes the
failure case concrete. After a BERT-based proofreading classifier reached only
60% precision and was prematurely advertised internally, he convened all
stakeholders and recommended dropping the project rather than burning months on
an under-resourced team. He argues that customer development and rapid
validation should precede ML work, and that interview candidates should ask
whether a company has active revenue-producing ML in production
([[podcast:data-science-failures-and-mlops-lessons|Data Science Failures and MLOps Lessons]]).

## Framing and Scope

The first management task is to turn a request into a decision. A request for a
forecast or dashboard usually hides more than one question. So does a request
for a model or segmentation. The manager has to identify who will act, what
will change, what cost matters, and what answer would be good enough.

In [[podcast:crisp-dm|CRISP-DM]], the 7:55, 10:58, and
13:25 sections move from an online classified-site example to measurable
problem size and success criteria. Project planning starts there, before anyone
chooses a model.

Project managers should include non-goals and a smallest useful path. [[person:valeriybabushkin|Valeriy
Babushkin]] makes that explicit
for [[ML System Design Documents]]
in [[podcast:ml-system-design|ML System Design Playbook]].
At 7:06 and 14:36, design documents help teams fail early and align
stakeholders. At 19:01, the document remains alive as the system changes.

For project managers, this means scope isn't a fixed wish list. It's a written
agreement about the decision, assumptions, risks, and next review point.

The team also decides whether the answer should be analysis, analytics
engineering, a model, or a productized ML system. [[person:annahannemann|Anna Hannemann]]
gives that product-owner judgment in [[podcast:building-data-products-product-owner-vs-product-manager|Product Owners in Data Science]].
The right next step may be manual cleanup, an MVP, or staged investment rather
than a model
([[podcast:building-data-products-product-owner-vs-product-manager|44:48-53:09]]).
Use [[Data Product Owner vs Data Product Manager]]
when the scope question is about who owns the delivery and product
decision. For a role-focused learning path, the
[[Machine Learning Engineer Roadmap]]
shows how this scope work connects to production ML responsibilities.

## Stakeholders and Decision Rights

Data science projects fail when stakeholders agree to a title but not to a
decision path. [[person:lorismarini|Loris Marini]]
starts [[podcast:data-professionals-business-skills-in-saas|Business Skills for Data Professionals in SaaS]]
with shared meaning for words such as customer, usage, and churn. Around 25:53
and 35:20, he ties trust to active listening, stakeholder mapping, and recording
roles and context. That's project infrastructure, not presentation polish.

Mesionis gives the delivery version. His marketing data science team uses
weekly embedded meetings and stakeholder observation before formal intake
([[podcast:building-data-products-lead-data-scientist|7:23-15:23]]).
Later, the team invites stakeholders to demos rather than daily stand-ups. They
also simplify technical results for non-technical audiences
([[podcast:building-data-products-lead-data-scientist|35:38-41:33]]).
The demos keep stakeholders close to direction and feedback while the delivery
team keeps space for exploration and technical work.

For managers, decision rights are part of team design. [[person:barbarasobkowiak|Barbara
Sobkowiak]] separates data
science managers from experts in [[podcast:data-science-manager-vs-expert-hiring-guide|Data Science Manager vs Expert]].
Around 8:22 and 15:49, the manager needs enough technical literacy and strategy
to redirect work when good enough is enough. Around 31:56 and 34:04, she warns
that companies sometimes hire deep experts when the real gap is coordination,
translation, and team development. That distinction links project management to
[[Data Scientist Role]] and
[[Leadership]].

## Baselines, Metrics, and Definition of Done

Baselines make progress visible before the final model exists. In [[podcast:crisp-dm|CRISP-DM]],
the 17:05 section treats a sufficient baseline as a reason to move to
evaluation. In [[podcast:machine-learning-system-design-interview|Machine Learning System Design Interviews]],
Valeriy connects baselines and metrics to system design around 24:28. Around
46:02, he adds A/B testing, monitoring, and fallbacks. Project managers should
therefore ask for a baseline early, not after a complex model has consumed the
budget.

Metrics need a decision owner and a unit of action. [[person:adamsroka|Adam Sroka]]
frames KPI design as top-down alignment with executive decisions in [[podcast:ml-engineering-kpis-and-metrics-strategy|KPI Design
& Metrics Strategy]]
around 22:41. He then warns about vanity metrics and KPI gaming around 26:07
and 28:04. For managed projects, [[Metrics]]
aren't only dashboard numbers. They're acceptance criteria, guardrails, and
review triggers.

Mesionis makes that concrete with Definition of Done. His team defines KPIs and
success criteria before deep delivery work. It also defines fail-fast checks
([[podcast:building-data-products-lead-data-scientist|17:37-25:17]]).
The same project can need an offline metric, an A/B test, and stakeholder
feedback. It may also need monitoring and a production support plan.

The [[Production ML Project Checklist]]
is the closer checklist when the project changes a live system.

## Delivery Under Uncertainty

Data science work is hard to estimate because data access, labels, model
behavior, and stakeholder needs can change the plan. Shir Meir Lador's agile ML
discussion names that uncertainty directly. Around 41:06, she discusses data
risks and unknowns. Around 44:18 and 45:36, she uses exploration tasks and
design stories to manage ML work. Grooming practices and iterative milestones
also keep the work from pretending it behaves like ordinary feature delivery
([[podcast:data-science-management-and-agile-machine-learning|Data Science Management and Agile Machine Learning]]).

Mesionis uses Kanban to plan sprints and estimate work, while demos keep
stakeholder feedback in the lifecycle. His team also keeps feasibility
assessment, MVPs, and fail-fast checks
([[podcast:building-data-products-lead-data-scientist|20:54-40:49]]).

That matches the [[Machine Learning System Design]]
habit of writing goals, non-goals, assumptions, and data paths before the work
becomes expensive. Serving constraints and monitoring belong in the same design.

A project manager keeps the delivery unit small enough to learn.

A useful increment might be a small validation or delivery milestone:

- a validated dataset
- a baseline notebook
- a dashboard with agreed metric definitions
- a design document
- a pilot
- a shadow-mode model
- a monitored batch job

For product-facing experiments, [[a-b-testing|A/B Testing]]
and [[Product Analytics]] help
separate a real rollout decision from a promising internal score.

## Evaluation, Adoption, and Handoff

Evaluation is where project management checks whether the work should continue,
change, ship, or stop. In [[podcast:production-ml-mlops-and-data-team-building|From Analytics to Production ML]],
[[person:rishabhbhargava|Rishabh Bhargava]] describes
production ML as experimental. Around 28:42, offline experiments, shadow mode,
and A/B tests bridge model work to product impact. Around 31:19, segment
analysis and root-cause work explain live results. That's why [[Evaluation]]
belongs in the project plan, not only in the modeling phase.

Adoption is also part of completion. [[person:caitlinmoorman|Caitlin Moorman]]
argues in [[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|Last-Mile Data Delivery]]
that data products can fail when users don't know they exist. They can also
fail when users don't understand or trust them. Sometimes they don't see how the
product fits the decision
([[podcast:last-mile-data-delivery-and-data-product-adoption-modern-data-stack|24:13-40:53]]).

For project management, adoption work includes discoverability,
interpretability, and workflow placement. Documentation and feedback loops
belong there too.

Production handoff should name the owner of data quality and model behavior.
It should also name owners for alerts, rollback, and stakeholder communication.
[[person:linaweichbrodt|Lina Weichbrodt]]
connects project intake, KPIs, stakeholder fears, and service levels in
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps and Model Monitoring]].
She also connects post-mortems, drift, and user feedback to the same operating
model
([[podcast:human-centered-mlops-and-model-monitoring|4:50-29:23 and 46:28-50:30]]).

That handoff links [[MLOps]],
[[Model Monitoring]], and
[[Production]]. A project is unfinished
if nobody knows what happens when the metric moves, the input data changes, or
the model stops helping the user.
