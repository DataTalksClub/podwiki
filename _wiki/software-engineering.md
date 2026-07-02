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
episode. ML systems differ from traditional software through uncertainty, data
workflows, and monitoring needs, and the discussion ties to hidden technical
debt.
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

[[person:benwilson|Ben Wilson]] gives the production ML version of this
definition, arguing for maintainability over novelty and for refactoring large
scripts into modular, testable components, and recommending SQL or statistical
baselines before deep learning when the simpler system can solve the problem
([[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]).

[[person:mariavechtomova|Maria Vechtomova]] gives the MLOps version, putting
version control, CI/CD, and registries in the same operating model, along with
documentation, reproducibility, code quality, and testing, and moving production
logic from notebooks into packages and CI/CD
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

For data teams, [[person:christopherbergh|Christopher Bergh]] connects the same
discipline to pipeline work: CI/CD pipelines, regression tests, test data,
version control, and end-to-end deployment automation
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]). Those
are software engineering practices applied to data products and analytics
systems.

## Engineering Entry Points

Guests agree that software engineering lowers operational risk, but they differ
on where teams should apply it first.

[[person:nadianahar|Nadia Nahar]] starts with the requirements and team boundary.
Failure connects to weak requirements, unrealistic expectations, and data access,
and vocabulary gaps and missing documentation also show up as failure causes. ML
practitioners belong in the full delivery path, from requirements through testing
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]).

[[person:benwilson|Ben Wilson]] starts with code and model complexity, framing
maintainability as a first-order engineering constraint and using timeboxed
experiments to prevent teams from turning research curiosity into an unbounded
production commitment
([[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]).

[[person:simonstiebellehner|Simon Stiebellehner]] starts from the platform
boundary, naming software engineering fundamentals as part of ML platform work,
connecting developer experience and thin abstractions to platform design, and
adding API schemas and prediction logging
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
This platform view overlaps with
[[Platform Engineering]]
because shared infrastructure has to preserve developer autonomy and reliable
interfaces.

[[person:marianosemelman|Mariano Semelman]] brings the same question to end-to-end
AI systems, focusing on ownership, translating business needs into ML
requirements, and the declining role of notebooks in production AI systems
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
That makes [[Notebook to Production AI Systems]]
a close companion topic.

## Practices for Data Systems

Data systems turn software engineering into repeatable change management. A
pipeline may run as scheduled and still produce data that's late, incomplete, or
wrong. That's why guests connect data engineering to tests, observability,
deployment automation, and recovery.

[[person:christopherbergh|Christopher Bergh]] frames
[[DataOps]] as a way to reduce fear-driven
deployment culture, covering deployment fear, automation, observability,
productivity, data versioning, and immutability
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

[[person:bartoszmikulski|Bartosz Mikulski]] connects data engineering to AI
reliability: data trust matters, and snapshot tests and integration tests, plus
a comparison of Great Expectations, Soda, SQL tests, and Spark tests, all support
it
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). These
practices belong on
[[Testing]] and
[[Production]] pages too, but they're
software engineering concerns because engineers use them to make changes safer.

## Practices for ML Systems

ML systems need normal software engineering and additional lifecycle controls.
Teams still need readable code, dependency management, tests, and releases. They
also need to track data, features, experiments, and metrics. Model artifacts and
serving behavior need tracking too.

[[person:mariavechtomova|Maria Vechtomova]] connects those controls to
standardized MLOps: use existing infrastructure such as Kubernetes, Git, and
CI/CD instead of adding tools for their own sake, add cookie-cutter repositories
and standard service accounts, and place software engineering and system design
next to ML fundamentals
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

[[person:simonstiebellehner|Simon Stiebellehner]] adds the platform view:
experiment tracking and model registries persist work for downstream use,
metadata and lineage support reproducibility, and artifact logging and tracking
matter too
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

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

[[person:bartoszmikulski|Bartosz Mikulski]] discusses that practical layer:
in-context learning, examples, prompt formatting, prompt evaluation, cost
tradeoffs, and prompt compression and caching for model efficiency
([[podcast:production-ready-ai-engineering|Production AI Engineering]]). Those
concerns also belong on
[[LLM Production Patterns]].

[[person:marianosemelman|Mariano Semelman]] adds the product engineering side:
LLMs aren't always the best solution, application architecture matters for logic
such as image description, and a modern stack can use FastAPI, `uv`, and Arize
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
[[AI Engineering]] includes ordinary
application engineering rather than only model selection. AI engineers also
build with [[AI Coding Tools]]
that integrate LLMs into the development workflow.

## Production Readiness

A system is production-ready when a team can release it, observe it, explain
it, and recover from failure. Guests repeatedly push against the idea that
production means only "deployed somewhere."

[[person:benwilson|Ben Wilson]] warns against building systems that nobody can
maintain: failure ties to missing business buy-in and overcomplicated solutions,
and reproducibility, environment assumptions, and cloud cost become problems when
teams borrow research code without enough engineering work
([[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]).

[[person:simonstiebellehner|Simon Stiebellehner]] connects production readiness to
platform design, distinguishing batch inference, online serving, and
orchestration, and adding security, compliance, and GDPR constraints
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).
For the broader operating model, see
[[Production]] and
[[Platform Engineering]].

## Testing

Guests cover more than unit tests in these episodes. Teams test code paths and
pipeline outputs, plus data assumptions and model behavior. They also test
prompt outputs and release configuration. Test data has to reflect production
risks.

[[person:christopherbergh|Christopher Bergh]] makes the data-team case: CI/CD
pipelines, regression tests, and test data for analytics, with version control
and tests linked to end-to-end deployment automation
([[podcast:dataops-for-data-engineering|DataOps for Data Engineering]]).

[[person:nadianahar|Nadia Nahar]] makes the ML-system case: testing and
operations are among the questions used to analyze open-source ML products, and
ML practitioners should be involved from requirements through testing
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]).

[[person:vincentwarmerdam|Vincent Warmerdam]] gives a software-maintenance
example: testing and CI for pull requests, packaging, and pre-commit hooks
([[podcast:open-source-ml-contributions|Open Source ML Contributions]]). That
advice comes from open source, but it maps directly to internal data and ML
projects: tests and packaging make code review possible.

## Deployment

Deployment turns engineering work into an owned running system. For data teams,
deployment includes pipeline promotion, job scheduling, and rollback. For ML
teams, it includes artifact registration and batch or online serving. It also
includes prediction schemas and monitoring. For AI systems, deployment includes
prompt and model changes.

[[person:mariavechtomova|Maria Vechtomova]] describes standardized deployment
paths built on reusable CI/CD and central infrastructure, with registries and
CI/CD in the essential MLOps stack
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps]]).

[[person:simonstiebellehner|Simon Stiebellehner]] connects deployment to platform
choices, separating batch inference from online serving and using unified
prediction schemas for monitoring and analytics
([[podcast:building-production-ml-platform-and-mlops-team|Building Production ML Platforms]]).

[[person:marianosemelman|Mariano Semelman]] shows why deployment is also a product
engineering question, moving away from notebooks as the production interface
toward concrete serving and observability tools
([[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]).
For more on this handoff, see
[[Notebook to Production AI Systems]].

## Maintainability

Maintainability means a team can change the system without relearning the whole
project from scratch. Guests connect that to simple designs, modular code, and
documentation. Teams also need shared vocabulary and explicit
ownership.

[[book:20210906-software-mistakes-and-tradeoffs|Software Mistakes and Tradeoffs]] by Tomasz Lelek and Jon Skeet covers the common pitfalls and architectural tradeoffs that underpin these maintainability decisions. For pragmatic coding habits, [[book:20210322-street-coder|Street Coder]] by Sedat Kapanoglu distills real-world engineering judgment that goes beyond textbook rules.

[[person:benwilson|Ben Wilson]] is the strongest maintainability reference:
refactor large code blocks into modular, testable code; teams can become attached
to complex systems because they invested so much work in them; and
maintainability ties to team composition, needing statistics expertise, coding
skill, and ML engineering
([[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]]).

[[person:nadianahar|Nadia Nahar]] adds documentation and accountability:
workshops, shared vocabularies, documentation, engineering remedies, model cards,
datasheets, factsheets, and checklists, plus responsible AI tied to team
accountability
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]).
That makes maintainability include more than code cleanup.

[[person:vincentwarmerdam|Vincent Warmerdam]] gives the open-source version:
low-maintenance APIs, ecosystem compatibility, README files, guides, API
references, examples, and contribution guides
([[podcast:open-source-ml-contributions|Open Source ML Contributions]]). Those
practices make a project easier to extend, whether the project is public open
source or an internal ML library.
