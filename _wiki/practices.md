---
layout: wiki
title: "Practices"
summary: "Repeatable engineering habits for technical delivery across data, ML, AI, documentation, testing, and production ownership."
related:
  - MLOps
  - DataOps
  - Software Engineering
  - Production
---

Practices are repeatable engineering habits that keep technical work usable
after the first demo. They appear most often in
[[DataOps]] and [[MLOps]], then extend the same idea into
[[software engineering]],
[[experimentation]], and
[[open source]]. A practice must make
work repeatable and visible to others. It must change how a team ships,
reviews, or recovers.

## Delivery Habits Across Domains

In DataOps, practices reduce errors and shorten deployment cycle time. They make
pipeline work visible enough to improve productivity.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
In MLOps, practices make model delivery reproducible. The baseline combines
shared infrastructure and reusable CI/CD with standard repositories,
registries, and monitoring.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

Nikolay Smorchkov's
[[book:20251006-software-development-at-rocket-speed=>Software Development at Rocket Speed]]
addresses the same delivery-speed question from the software side. It covers
how requirements decomposition, estimation, and incremental delivery keep teams
shipping rather than stuck in analysis.

## Starting Points

The main disagreement is where teams should start, not whether repeatable
practices matter. The DataOps path starts with automation. Version control,
tests, and CI/CD cover the path from data to model to visualization. Runbooks,
observability, and environment management support that path.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

The MLOps infrastructure path starts with what a company already has. Git,
Kubernetes, and CI/CD come before more specialized platform work. Registries,
object storage, and model registry options come next.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

The adoption path starts with developer experience and trust. An MLOps team can
collect pain points and deliver quick wins.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

Deployment frequency shows when product teams see enough value to
standardize.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

The software-engineering path starts with shared vocabulary and requirements
alignment because ML systems fail through organizational ambiguity as well as
code defects.[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]

## Versioning and Reproducibility

Version control is the baseline practice for [[DataOps]]
and [[MLOps]]. Healthier pipelines combine version control, tests, and CI/CD.
Teams then widen versioning beyond code to models, visualizations, and
governance.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

This wider scope matters for [[production]]
because a team can't recover or audit a data product when only the application
repository has history.

MLOps reproducibility also depends on model registries and artifact storage.
Service principals, standard repositories, and packaged notebook logic support
the same goal.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

Reproducibility ties together data versioning, traceability, and experiment
capture. Dependency management and package registries belong with containers
and deployment records.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]
Those concerns overlap with [[ci-cd=>CI/CD]],
[[MLOps tools]], and
[[data governance]].

## Testing and Quality Gates

Testing changes by domain because data pipelines need data quality checks,
snapshot tests, SQL tests, and Spark tests. Integration coverage belongs beside
those checks.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Tools such as Great Expectations and Soda sit next to SQL-based and Spark-based
tests.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Testing catches the familiar "this number doesn't look correct" failure before
it reaches users.

AI application quality gates extend into prompt evaluation, prompt compression
tradeoffs, and caching decisions.[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Product experiments need gates for randomization, traffic assignment, and
assignment tracking. Monitoring, A/A tests, and metric stability belong with
those gates. Power analysis, statistical tests, and distribution checks round
out the practice.[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]

Those practices belong with [[a-b-testing=>A/B Testing]],
[[a-a-testing=>A/A Testing]], and
[[Causal Inference]] rather than
generic software unit testing.

In open source projects, good issues and pull requests rely on reproducible
examples and tests. CI keeps failures visible in review.[[cite:open-source-ml-contributions=>Contribute to Open Source ML]]
Packaging and pre-commit hooks help maintainers review faster. That makes
testing part of
[[open source portfolio evidence]]
as well as part of [[software engineering]].

## CI/CD and Release Paths

CI/CD reduces release risk across DataOps, MLOps, and open source. In DataOps,
CI/CD connects deployment cycle time and production reliability. It also
connects end-to-end testing and test data.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

Reusable CI/CD templates and standardized repositories are central MLOps team
responsibilities.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]
CI, repository structure, parameterization, and testing are core MLOps habits.
Package registries and deployment frequency show whether the release path
works.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

CI/CD is more than a pipeline runner in these discussions. Teams use it to
encode quality gates and packaging rules. They also encode environment
assumptions and handoff expectations.

For model systems, this work belongs to
[[MLOps Engineer]] practice.

For data pipelines, it sits next to
[[Data Quality and Observability]]
and [[DataOps tools]].

For open source, the same habit appears in contribution guides and tests.
Packaging checks and pre-commit hooks support it too.[[cite:open-source-ml-contributions=>Contribute to Open Source ML]]

## Documentation and Handoffs

Documentation counts as a practice when it changes handoffs. It connects shared
vocabulary with expectation setting.[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]

Requirements and data assumptions belong in the same work.[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]

Model Cards and Datasheets belong in this family. Factsheets, checklists, and
responsible AI accountability belong there too.[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]]

Useful documentation keeps model behavior, stakeholder expectations, and team
responsibilities visible while the system changes.

Runbooks are the operational version: they bridge manual checklists and
automated playbooks, reducing fragile handoffs and on-call load.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]

README files, guides, API references, and examples help people use an open
source project. Contribution guides and polite interaction help people maintain
it.[[cite:open-source-ml-contributions=>Contribute to Open Source ML]]

Those patterns belong with [[Documentation]],
[[Developer Experience]],
and [[Open Source and Developer Relations]].

## Monitoring, Feedback, and Ownership

Without feedback loops, practices turn into ceremony, so DataOps separates
customer validation from data and model validity. It connects observability to
data quality and production errors.[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
MLOps adoption uses feedback loops through pain-point collection, quick wins,
and deployment-frequency measurement. Platform work stays tied to product-team
needs.[[cite:mlops-at-scale-reproducibility-adoption=>MLOps at Scale]]

The organizational side includes buy-in, DevOps cooperation, monitoring
standardization, and centralized support for smaller brands.[[cite:pragmatic-and-standardized-mlops=>Pragmatic MLOps]]

Ownership changes with the domain because DataOps spans pipelines,
environments, quality, and recovery. MLOps covers model release, monitoring,
reproducibility, and support for product teams. Experimentation ownership stays
close to metric design and assignment tracking. Power analysis and
interpretation stay with the same owner.[[cite:ab-testing-and-product-experimentation=>Product Analytics and A/B Testing]]

Those differences matter for role pages such as
[[MLOps Engineer]] and for
[[MLOps vs DataOps]].

## Related Pages

These pages cover the neighboring roles, systems, and engineering habits:

- [[DataOps]]
- [[MLOps]]
- [[Software Engineering]]
- [[production]]
- [[Developer Experience]]
- [[Documentation]]
