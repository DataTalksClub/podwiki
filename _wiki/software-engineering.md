---
layout: wiki
title: "Software Engineering"
summary: "How DataTalks.Club guests apply software engineering discipline to data, ML, and AI systems through testing, interfaces, deployment, and maintainability."
related:
  - Machine Learning vs Software Engineering
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
and trust. Data, ML, and AI work enters this territory when notebooks and
scripts become shared products. Teams then need to change, release, observe, and
repair them.[[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]][[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]][[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]

Software engineering isn't a separate cleanup phase after modeling. Data
pipelines need version control, tests, deployment paths, and monitoring. ML
systems need interfaces, model artifacts, reproducible experiments, and release
ownership. AI products add prompt evaluation, data quality checks, latency
controls, and maintainable application code.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

Use [[Machine Learning System Design]] for the architecture layer around model
behavior, data, serving, and reliability. For operating practices after release,
use [[MLOps]], [[DataOps]], and [[Production]].
Use [[Machine Learning vs Software Engineering]] for the direct comparison
between ordinary software risk and ML-specific uncertainty, data, and monitoring
risk.

## Engineering Habits

Software engineering means repeatable habits around a changing system.

The recurring habits are:

- defining requirements and modules
- using version control, tests, and documentation
- deploying and observing the system
- assigning ownership

In data and ML work, those habits cover code and data. They also cover model
behavior, prompts, business metrics, and users.[[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]][[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

Production ML discussions put maintainability ahead of novelty, so large scripts
need to become modular, testable components. SQL or statistical baselines can be
better than deep learning when they solve the business problem with less
operational burden.[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]

MLOps discussions put version control, CI/CD, and registries in one operating
model. Documentation, reproducibility, code quality, and testing belong in that
model too. The shift from notebooks into packages and CI/CD is a software
engineering change as much as an ML tooling change.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

DataOps discussions apply the same discipline to pipelines and analytics
products. Data teams use CI/CD pipelines and regression tests. They add test
data and connect version control to deployment automation.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Analytics craft needs the same maintainability bar.
Katie Bauer describes documentation and peer review as part of senior analytics
practice. Maintainable work isn't only a habit for application engineers
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas@11:58=>How to Hire, Manage, and Grow a Data Science Team]].
That connects [[Analytics Engineering]] to software engineering when modeled
data becomes shared team infrastructure.

For data teams, peer review and documentation are also succession tools. They
let another analyst or analytics engineer understand the model. That person can
change it and defend the metric after the original author moves on
[[cite:hiring-and-managing-data-science-teams-in-b2b-saas@11:58=>How to Hire, Manage, and Grow a Data Science Team]].

Marcello La Rocca adds a lower-level version of the same habit. Abstractions are
useful until performance, memory, or correctness depends on the implementation.
Engineers can trust library APIs for ordinary work. When the system's behavior
makes that boundary visible, they look at the underlying data structures,
algorithms, and serialization details
[[cite:algorithms-data-structures-for-engineers@12:17=>Abstraction and Implementation]]
[[cite:algorithms-data-structures-for-engineers@47:47=>Frameworks vs Internals]].

## Engineering Entry Points

The episodes converge on software engineering as risk reduction, but they put
the first intervention in different places.

The ML-software boundary starts with requirements and team participation. Weak
requirements and unrealistic expectations can undermine ML systems before
implementation starts. Data-access problems, vocabulary gaps, and missing
documentation create the same risk.
ML practitioners need to stay involved from requirements through testing.[[cite:software-engineering-for-machine-learning@56:55=>Software Engineering for Machine Learning]]

Nadia Nahar ties this to hidden technical debt. The model may be the visible
piece, but surrounding software and data workflow create much of the long-term
cost. Monitoring and handoff decisions add to that cost
[[cite:software-engineering-for-machine-learning@10:12=>Software Engineering for Machine Learning]].

The production-ML boundary starts with code and model complexity. Teams use
timeboxed experiments to keep research curiosity from becoming an unbounded
production commitment. Maintainability becomes a first-order constraint once a
team has to operate the result.[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]

The platform boundary starts with developer experience and shared interfaces.
ML platform work includes software engineering fundamentals and thin
abstractions. API schemas, prediction logging, and shared infrastructure preserve
developer autonomy.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
That view overlaps with [[Platform Engineering]].

End-to-end AI systems start with ownership and business translation. Teams turn
business needs into ML requirements, and notebooks become less central as systems
need concrete serving paths and observability. Product engineering around model
behavior becomes part of the work.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]
That makes [[Notebook to Production AI Systems]] a close companion topic.

## Data Systems

Data systems turn software engineering into repeatable change management. A
pipeline may run on schedule and still produce late, incomplete, or wrong data.
That risk is why data teams use tests, observability, deployment automation, and
recovery practices.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

[[DataOps]] reduces fear-driven deployment culture by combining automation,
observability, and data versioning. Productivity and immutability matter too.
Those practices make analytics and data products behave more like maintained
software systems than one-off scripts.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Production AI engineering handles data trust with snapshot and integration tests
that catch changes in data behavior. Great Expectations and Soda sit alongside
SQL tests and Spark tests.[[cite:production-ready-ai-engineering=>Production AI Engineering]]
These practices also belong on [[Testing]] and [[Production]]. Engineers use
them to make changes safer, so they're software engineering concerns too.

## ML Systems

ML systems need normal software engineering plus lifecycle controls for data and
features. Experiments, metrics, model artifacts, and serving behavior need
tracking too. Readable code, dependency management, tests, and releases still
matter. The system also needs traceability across the model lifecycle.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]][[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

MLOps standardization favors existing infrastructure such as Kubernetes, Git, and
CI/CD over adding tools for their own sake. Cookie-cutter repositories and
standard service accounts sit next to software engineering, system design, and
ML fundamentals.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

ML platforms add experiment tracking and model registries so downstream teams
can reproduce and use model work. Metadata, lineage, artifact logging, and
prediction tracking support that handoff.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The [[MLOps vs DataOps]] boundary matters here because DataOps keeps inputs
reliable. MLOps keeps experiments and artifacts traceable, along with deployment
and monitoring. Software engineering ties both sides together through code
structure, tests, interfaces, and release discipline.

## AI Systems

AI systems add an application layer around models and prompts. Teams still need
software engineering fundamentals. They also need to evaluate outputs, control
latency and cost, and choose when an LLM is the wrong tool.[[cite:production-ready-ai-engineering=>Production AI Engineering]][[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]

Production AI work includes in-context learning, examples, prompt formatting,
and prompt evaluation. Cost tradeoffs, prompt compression, and caching also
matter. These concerns also belong on [[LLM Production Patterns]].[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Product engineering still matters when an AI system uses LLMs. Application
logic such as image description may be separate from model choice. The serving
and observability stack can include FastAPI, `uv`, and Arize.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]
[[AI Engineering]] includes ordinary application engineering rather than only
model selection. [[AI Coding Tools]] bring LLMs into the development workflow.

## Production Readiness

A system is production-ready when a team can release it, observe it, explain it,
and recover from failure. Production means more than deploying something once.
It also includes business buy-in and reproducibility. Environment assumptions,
cost control, and enough engineering work keep research code maintainable.[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]

Platform design adds runtime choices to that readiness work. Batch inference,
online serving, and orchestration all affect production design. Security,
compliance, and GDPR constraints affect it too.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]
For the broader operating model, see [[Production]] and [[Platform Engineering]].

## Testing

Software engineering for data, ML, and AI systems includes more than unit tests.
Teams test code paths and pipeline outputs. They also test data assumptions,
model behavior, prompt outputs, and release configuration. Test data has to
reflect production risks.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]][[cite:production-ready-ai-engineering=>Production AI Engineering]]

Data teams use CI/CD pipelines, regression tests, and test data for analytics.
They connect version control and tests to end-to-end deployment automation.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]]

Angela Ramirez makes the data-engineering version concrete with PySpark and
Scala Spark work. Data engineers still need readable code structure and unit
tests. They also test pipeline data with null checks, type checks, schema
expectations, and other quality checks
[[cite:building-and-scaling-data-engineering-systems-for-fraud-detection@41:09=>Angela Ramirez on PySpark testing]].
That puts [[Testing]] and [[Data Quality and Observability]] in the same
engineering loop rather than separate cleanup work.

ML-system testing starts before release. Requirements, operations, open-source
ML product analysis, and practitioner involvement through testing all affect
whether the system can be trusted after handoff.[[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]]

Open-source ML maintenance uses the same practices in public projects. Testing
and CI support pull requests. Packaging and pre-commit hooks make code review
possible for internal data and ML projects too.[[cite:open-source-ml-contributions=>Open Source ML Contributions]]

## Deployment

Deployment turns engineering work into an owned running system.

The deployment surface differs by system type:

- Data teams promote pipelines, schedule jobs, and plan rollback.
- ML teams register artifacts, serve models, define schemas, and monitor predictions.
- AI teams also manage prompt and model changes.

These deployment concerns recur across data, ML, and AI discussions.[[cite:dataops-for-data-engineering=>DataOps for Data Engineering]][[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]][[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]

Standard deployment paths reuse CI/CD and central infrastructure. Registries and
CI/CD sit in the essential MLOps stack because teams need a repeatable way to
move models from development into operation.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

Platform choices define deployment boundaries. Batch inference, online serving,
and unified prediction schemas support monitoring and analytics once the model is
running.[[cite:building-production-ml-platform-and-mlops-team=>Building Production ML Platforms]]

The notebook-to-production handoff is also a product engineering problem.
Production AI work moves away from notebooks as the delivery interface. Serving
and observability tools become part of the handoff.[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]]
For more on this handoff, see [[Notebook to Production AI Systems]].

## Maintainability

Maintainability means a team can change the system without relearning the whole
project from scratch. Simple designs and modular code reduce the cost of future
changes. Documentation, shared vocabulary, and explicit ownership reduce it too.[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]][[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]]

[[book:20210906-software-mistakes-and-tradeoffs=>Software Mistakes and Tradeoffs]]
by Tomasz Lelek and Jon Skeet covers common pitfalls and architectural
tradeoffs behind maintainability decisions. [[book:20210322-street-coder=>Street Coder]]
by Sedat Kapanoglu focuses on pragmatic engineering judgment beyond textbook
rules.

Production ML maintainability includes refactoring large code blocks into
modular, testable code. Team composition also matters after release. A team needs
statistics expertise, coding skill, and ML engineering.[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]

ML system accountability depends on documentation as well as code. Workshops and
shared vocabularies help teams expose assumptions. Model cards, datasheets,
factsheets, and checklists make responsibilities visible.[[cite:software-engineering-for-machine-learning=>Software Engineering for Machine Learning]]

Open-source ML maintenance adds low-maintenance APIs and ecosystem compatibility.
README files and guides make a project easier to extend. API references,
examples, and contribution guides help internal ML libraries too.[[cite:open-source-ml-contributions=>Open Source ML Contributions]]

## Related Pages

These pages cover the adjacent operating, testing, and platform topics.

- [[Machine Learning System Design]]
- [[Machine Learning vs Software Engineering]]
- [[MLOps]]
- [[DataOps]]
- [[Production]]
- [[Testing]]
- [[Platform Engineering]]
- [[Notebook to Production AI Systems]]
- [[Open Source and Developer Relations]]
