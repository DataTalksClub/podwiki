---
layout: wiki
title: "Software Engineering"
summary: "How DataTalks.Club guests apply software engineering discipline to data, ML, and AI systems through requirements, interfaces, testing, deployment, documentation, and maintainability."
related:
  - Machine Learning System Design
  - MLOps
  - DataOps
  - Production
  - Testing
  - Platform Engineering
  - Notebook to Production AI Systems
  - Open Source and Developer Relations
---

Software engineering turns code into systems that other people can understand
and trust. It also makes those systems easier to change and run. In the
DataTalks.Club podcast discussions, the topic usually appears when data, ML, or
AI work has to move beyond a notebook or one-person script.

Guests treat software engineering as part of data, ML, and AI work rather than
as a separate craft borrowed at the end. Data pipelines need version control,
tests, deployment paths, and monitoring. ML systems need interfaces, model
artifacts, reproducible experiments, and release ownership. AI products need
prompt evaluation, data quality checks, latency controls, and maintainable
application code.

Use
[[Machine Learning System Design]]
for the architecture layer around model behavior, data, serving, and
reliability.
For operating practices after release, use
[[MLOps]],
[[DataOps]], and
[[Production]].

The clearest starting point is
[[person:nadianahar|Nadia Nahar]]'s
[[podcast:software-engineering-for-machine-learning|Software Engineering for Machine Learning]]
episode. At 6:58 and 7:42, she distinguishes ML systems from traditional
software through uncertainty, data workflows, and monitoring needs. At 10:12,
she ties the discussion to hidden technical debt.
Engin Yoyen's
[[book:20250922-how-software-fails|How Software Fails]]
collects the same failure patterns from the software side: technical debt,
communication breakdowns, deadline pressure, and the human and organizational
factors that undermine even well-architected systems.

## Engineering Habits for Changing Systems

Across these podcast discussions, software engineering means repeatable
engineering habits around a changing system. Teams define requirements and
structure code into modules. They use version control, tests, documentation,
and deployment. They also need observability and clear ownership.

In data and ML work, code changes alongside data and model behavior. Prompts,
business metrics, and users also change.

[[person:benwilson|Ben Wilson]] gives the production ML
version of this definition in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
At 6:50 and 8:49, he argues for maintainability over novelty and for refactoring
large scripts into modular, testable components. At 44:23, he recommends trying
SQL or statistical baselines before deep learning when the simpler system can
solve the problem.

[[person:mariavechtomova|Maria Vechtomova]] gives the
MLOps version in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]].
Her 18:41 and 22:23 chapters put version control, CI/CD, and registries in the
same operating model. Documentation and reproducibility belong there too. So do
code quality and testing. At 33:24, she recommends moving production logic from
notebooks into packages and CI/CD.

For data teams, [[person:christopherbergh|Christopher Bergh]]
connects the same discipline to pipeline work in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
At 30:55 and 42:39, he discusses CI/CD pipelines, regression tests, and test
data. He also covers version control and end-to-end deployment automation. Those
are software engineering practices applied to data products and analytics
systems.

## Engineering Entry Points

Guests agree that software engineering lowers operational risk, but they differ
on where teams should apply it first.

[[person:nadianahar|Nadia Nahar]] starts with the
requirements and team boundary. In
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]],
the 10:54 and 13:52 chapters connect failure to weak requirements, unrealistic
expectations, and data access. Vocabulary gaps and missing documentation also
show up as failure causes. Her 36:28 and 56:55 chapters put ML practitioners
into the full delivery path, from requirements through testing.

[[person:benwilson|Ben Wilson]] starts with code and
model complexity. In
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]],
he frames maintainability as a first-order engineering constraint. His 32:03 and
55:41 chapters also use timeboxed experiments to prevent teams from turning
research curiosity into an unbounded production commitment.

[[person:simonstiebellehner|Simon Stiebellehner]]
starts from the platform boundary in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
At 13:25, he names software engineering fundamentals as part of ML platform
work. Later, the 38:40 chapter connects developer experience and thin
abstractions to platform design. The 54:15 chapter adds API schemas and
prediction logging. His platform view overlaps with
[[Platform Engineering]]
because shared infrastructure has to preserve developer autonomy and reliable
interfaces.

[[person:marianosemelman|Mariano Semelman]] brings the
same question to end-to-end AI systems in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
His 17:27 and 37:39 chapters focus on ownership and translating business needs
into ML requirements. The 55:28 chapter discusses the declining role of
notebooks in production AI systems, which makes
[[Notebook to Production AI Systems]]
a close companion topic.

## Practices for Data Systems

Data systems turn software engineering into repeatable change management. A
pipeline may run as scheduled and still produce data that's late, incomplete, or
wrong. That's why guests connect data engineering to tests, observability,
deployment automation, and recovery.

[[person:christopherbergh|Christopher Bergh]] frames
[[DataOps]] as a way to reduce fear-driven
deployment culture in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
The 13:27 and 15:52 chapters discuss deployment fear, automation,
observability, and productivity. The 54:05 chapter adds data versioning and
immutability to the engineering discussion.

[[person:bartoszmikulski|Bartosz Mikulski]] connects
data engineering to AI reliability in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
At 9:05, he explains why data trust matters. At 11:47 and 13:14, he discusses
snapshot tests and integration tests. He also compares Great Expectations, Soda,
SQL tests, and Spark tests. These practices belong on
[[Testing]] and
[[Production]] pages too, but they're
software engineering concerns because engineers use them to make changes safer.

## Practices for ML Systems

ML systems need normal software engineering and additional lifecycle controls.
Teams still need readable code, dependency management, tests, and releases. They
also need to track data, features, experiments, and metrics. Model artifacts and
serving behavior need tracking too.

[[person:mariavechtomova|Maria Vechtomova]] connects
those controls to standardized MLOps in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]].
The 16:27 chapter recommends using existing infrastructure such as Kubernetes,
Git, and CI/CD instead of adding tools for their own sake. The 29:55 chapter
adds cookie-cutter repositories and standard service accounts. The 56:08
chapter places software engineering and system design next to ML fundamentals.

[[person:simonstiebellehner|Simon Stiebellehner]]
adds the platform view in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
At 29:41 and 30:32, he presents experiment tracking and model registries as
practical ways to persist work for downstream use. At 42:48, he links metadata
and lineage to reproducibility. Artifact logging and tracking also matter.

This is where the
[[MLOps vs DataOps]]
boundary matters. DataOps keeps inputs reliable, while MLOps keeps experiments
and artifacts traceable. It also tracks deployment and monitoring. Software
engineering ties both sides together through code structure, tests, interfaces,
and release discipline.

## Practices for AI Systems

AI systems add an application layer around models and prompts. Teams still need
software engineering fundamentals. They also need to evaluate outputs, control
latency and cost, and choose when an LLM is the wrong tool.

[[person:bartoszmikulski|Bartosz Mikulski]] discusses
that practical layer in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His 25:13 and 28:16 chapters cover in-context learning, examples, and prompt
formatting. They also cover prompt evaluation and cost tradeoffs. At 30:00 and
31:45, he connects prompt compression and prompt caching to model efficiency.
Those concerns also belong on
[[LLM Production Patterns]].

[[person:marianosemelman|Mariano Semelman]] adds the
product engineering side in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
At 31:42, he explains why LLMs aren't always the best solution. At 48:26, he
walks through application architecture for image-description logic. At 1:02:53,
he discusses a modern stack with FastAPI, `uv`, and Arize.
[[AI Engineering]] includes ordinary
application engineering rather than only model selection. AI engineers also
build with [[AI Coding Tools]]
that integrate LLMs into the development workflow.

## Production Readiness

A system is production-ready when a team can release it, observe it, explain
it, and recover from failure. Guests repeatedly push against the idea that
production means only "deployed somewhere."

[[person:benwilson|Ben Wilson]] warns against building
systems that nobody can maintain in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
His 10:35 chapter ties failure to missing business buy-in and overcomplicated
solutions. His 46:22 chapter adds reproducibility, environment assumptions, and
cloud cost when teams borrow research code without enough engineering work.

[[person:simonstiebellehner|Simon Stiebellehner]]
connects production readiness to platform design in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
The 31:15 and 31:51 chapters distinguish batch inference, online serving, and
orchestration. The 39:54 and 45:50 chapters add security, compliance, and GDPR
constraints. For the broader operating model, see
[[Production]] and
[[Platform Engineering]].

## Testing

Guests cover more than unit tests in these episodes. Teams test code paths and
pipeline outputs, plus data assumptions and model behavior. They also test
prompt outputs and release configuration. Test data has to reflect production
risks.

[[person:christopherbergh|Christopher Bergh]] makes the
data-team case in
[[podcast:dataops-for-data-engineering|DataOps for Data Engineering]].
At 30:55, he discusses CI/CD pipelines, regression tests, and test data for
analytics. At 42:39, he links version control and tests to end-to-end deployment
automation.

[[person:nadianahar|Nadia Nahar]] makes the ML-system
case in
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]].
The 24:03 chapter lists testing and operations among the questions her research
uses to analyze open-source ML products. The 56:55 chapter argues for involving
ML practitioners from requirements through testing.

[[person:vincentwarmerdam|Vincent Warmerdam]] gives a
software-maintenance example in
[[podcast:open-source-ml-contributions|Open Source ML Contributions]].
At 27:40, he covers testing and CI for pull requests. He also covers packaging
and pre-commit hooks. That advice comes from open source, but it maps directly
to internal data and ML projects: tests and packaging make code review possible.

## Deployment

Deployment turns engineering work into an owned running system. For data teams,
deployment includes pipeline promotion, job scheduling, and rollback. For ML
teams, it includes artifact registration and batch or online serving. It also
includes prediction schemas and monitoring. For AI systems, deployment includes
prompt and model changes.

[[person:mariavechtomova|Maria Vechtomova]] describes
standardized deployment paths in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]],
where the 12:42 chapter covers reusable CI/CD and central infrastructure. Her
18:41 chapter puts registries and CI/CD into the essential MLOps stack.

[[person:simonstiebellehner|Simon Stiebellehner]]
connects deployment to platform choices in
[[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]].
The 31:15 chapter separates batch inference from online serving. The 54:15
chapter uses unified prediction schemas for monitoring and analytics.

[[person:marianosemelman|Mariano Semelman]] shows why
deployment is also a product engineering question in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
His 55:28 chapter moves away from notebooks as the production interface. The
1:02:53 chapter discusses concrete serving and observability tools. For more on
this handoff, see
[[Notebook to Production AI Systems]].

## Maintainability

Maintainability means a team can change the system without relearning the whole
project from scratch. Guests connect that to simple designs, modular code, and
documentation. Teams also need shared vocabulary and explicit
ownership.

[[book:20210906-software-mistakes-and-tradeoffs|Software Mistakes and Tradeoffs]] by Tomasz Lelek and Jon Skeet covers the common pitfalls and architectural tradeoffs that underpin these maintainability decisions. For pragmatic coding habits, [[book:20210322-street-coder|Street Coder]] by Sedat Kapanoglu distills real-world engineering judgment that goes beyond textbook rules.

[[person:benwilson|Ben Wilson]] is the strongest
maintainability reference. In
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]],
the 8:49 chapter discusses refactoring large code blocks into modular,
testable code. The 36:13 chapter warns that teams can become attached to
complex systems because they invested so much work in them. The 49:54 chapter
ties maintainability to team composition. Teams need statistics expertise,
coding skill, and ML engineering.

[[person:nadianahar|Nadia Nahar]] adds documentation
and accountability in
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]].
The 39:05 chapter covers workshops, shared vocabularies, documentation, and
engineering remedies. The 42:47 chapter discusses model cards, datasheets,
factsheets, and checklists. The 54:16 chapter connects responsible AI to team
accountability, which makes maintainability include more than code cleanup.

[[person:vincentwarmerdam|Vincent Warmerdam]] gives the
open-source version in
[[podcast:open-source-ml-contributions|Open Source ML Contributions]].
At 19:00, he discusses low-maintenance APIs and ecosystem compatibility. At
22:20 and 24:10, he covers README files and guides. He also covers API
references, examples, and contribution guides. Those practices make a project
easier to extend, whether the project is public open source or an internal ML
library.
