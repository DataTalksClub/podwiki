---
layout: wiki
title: "Practices"
summary: "How DataTalks.Club episodes discuss repeatable engineering habits for technical delivery."
related:
  - MLOps
  - DataOps
  - Software Engineering
  - Production
---

Practices are the repeatable engineering habits that keep technical work usable
after the first demo. DataTalks.Club guests use the term most often in
[[DataOps]] and
[[MLOps]]. They also use it around
[[software engineering]],
[[experimentation]], and
[[open source]]. A practice must make
work repeatable and visible to others. It must change how a team ships,
reviews, or recovers.

[[person:christopherbergh|Christopher Bergh]] gives
the DataOps version in
[[podcast:dataops-automation-and-reliable-data-pipelines|6:42|Mastering DataOps]].
Teams reduce errors, shorten deployment cycle time, and improve productivity.
[[person:mariavechtomova|Maria Vechtomova]] gives the
MLOps version in
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps at 11:10 and 12:42]].
Teams enable reproducible model delivery with shared infrastructure, reusable
CI/CD, and standard repositories. Registries and monitoring complete that
baseline.
Nikolay Smorchkov's
[[book:20251006-software-development-at-rocket-speed|Software Development at Rocket Speed]]
addresses the same delivery-speed question from the software side: how
requirements decomposition, estimation, and incremental delivery keep teams
shipping rather than stuck in analysis.

## Adoption and Scope

Guests disagree less about the value of practices than about where to start.
Bergh argues from an automation-first DataOps view. Version control, tests, and
CI/CD cover the path from data to model to visualization. Runbooks,
observability, and environment management support the same path
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps at 33:47 / 34:37 / 56:32]]).

Vechtomova starts with the infrastructure a company already has. In
[[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps at 16:27 and 18:41]],
she names Git, Kubernetes, and CI/CD before more specialized platform work. She
also includes registries, object storage, and model registry options.

[[person:raphaelhoogvliets|Raphaël Hoogvliets]] puts
developer experience and trust first. His MLOps team collects pain points and
delivers quick wins. It watches deployment frequency and standardizes only
after teams see value
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale at 27:56 / 32:46 / 36:55]]).
[[person:nadianahar|Nadia Nahar]] puts shared
vocabulary and requirements alignment near the center. Documentation matters
for her because ML systems fail through organizational ambiguity as well as code
defects
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML at 13:52 and 39:05]]).

## Versioning and Reproducibility

Version control is the baseline practice for [[DataOps]]
and [[MLOps]]. Bergh includes version
control, tests, and CI/CD in his seven practical steps for healthier pipelines.
He then widens versioning beyond code to models, visualizations, and governance
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps at 33:47 and 51:21]]).
That wider scope matters for [[production]]
because a team can't recover or audit a data product if only the application
repository has history.

In the MLOps episodes, Vechtomova discusses model registries, artifact storage,
and service principals. She also covers standard repositories and moving
notebook logic into packages
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps at 20:49 / 29:55 / 33:24]]).

Hoogvliets ties reproducibility to data versioning, traceability, and
experiment capture. Dependency management, package registries, containers, and
deployment records belong in the same operating model
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale at 42:31 / 53:08 / 56:50]]).
Those concerns overlap with [[ci-cd|CI/CD]],
[[MLOps tools]], and
[[data governance]].

## Testing and Quality Gates

Testing changes by domain because data pipelines need data quality checks plus
snapshot, SQL, Spark, and integration coverage. In
[[podcast:production-ready-ai-engineering|Production AI Engineering at 9:05 / 11:47 / 13:14]],
[[person:bartoszmikulski|Bartosz Mikulski]] compares
tools such as Great Expectations and Soda with SQL-based and Spark-based tests.
He treats testing as a way to stop the familiar "this number doesn't look
correct" failure before it reaches users.

The same episode extends quality gates into AI applications through prompt
evaluation. Prompt compression tradeoffs and caching decisions also sit in that
quality discussion
([[podcast:production-ready-ai-engineering|Production AI Engineering at 28:16 / 30:00 / 31:45]]).

Product experiments need different gates. In
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing at 8:13 and 24:44]],
[[person:jakobgraff|Jakob Graff]] focuses on
randomization, traffic assignment, and assignment tracking. Monitoring belongs
with the same experimental gate. He also links reliable experiments to A/A
tests and metric stability. Power analysis, statistical tests, and distribution
checks round out the practice
([[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing at 27:52 / 33:23 / 37:44 / 40:23 / 44:39]]).

Those practices belong with [[a-b-testing|A/B Testing]],
[[a-a-testing|A/A Testing]], and
[[Causal Inference]] rather than
generic software unit testing.

Open source projects expose the social side of testing. In
[[podcast:open-source-ml-contributions|Contribute to Open Source ML at 25:50 and 27:40]],
[[person:vincentwarmerdam|Vincent Warmerdam]] connects
good issues and pull requests to reproducible examples, tests, and CI.
Packaging and pre-commit hooks help maintainers review faster because the
failure is easy to reproduce. That makes testing part of
[[open source portfolio evidence]]
as well as part of [[software engineering]].

## CI/CD and Release Paths

CI/CD reduces release risk across DataOps, MLOps, and open source. Bergh links
CI/CD to deployment cycle time and production reliability in the DataOps
episode. He also covers end-to-end testing and test data
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps at 6:42 / 33:47 / 43:06 / 44:12]]).

Vechtomova describes reusable CI/CD templates and standardized repositories as
central MLOps team responsibilities
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps at 12:42 and 29:55]]).
Hoogvliets lists CI, repository structure, parameterization, and testing as
core MLOps habits. Package registries and deployment frequency show whether the
release path works
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale at 39:06 / 48:41 / 53:08]]).

CI/CD is more than a pipeline runner in these discussions. Teams use it to
encode quality gates and packaging rules. They also encode environment
assumptions and handoff expectations.

For model systems, this work belongs to
[[MLOps Engineer]] practice.

For data pipelines, it sits next to
[[Data Quality and Observability]]
and [[DataOps tools]].

For open source, Warmerdam shows the same habit through contribution guides and
tests. Packaging checks and pre-commit hooks help too
([[podcast:open-source-ml-contributions|Contribute to Open Source ML at 22:20 / 24:10 / 27:40]]).

## Documentation and Handoffs

Documentation counts as a practice when it changes how people hand off work.
Nahar connects documentation to shared vocabulary, expectation setting,
requirements, and data assumptions. Model Cards, Datasheets, factsheets, and
checklists belong in the same documentation family. Responsible AI
accountability does too
([[podcast:software-engineering-for-machine-learning|Software Engineering for ML at 13:52 / 39:05 / 42:47 / 54:16]]).
Useful documentation keeps model behavior, stakeholder expectations, and team
responsibilities visible while the system changes.

Bergh makes the operational version of the same argument. Runbooks become a
bridge from manual checklists to automated playbooks. Documentation reduces
fragile handoffs and on-call load
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps at 34:37 and 38:01]]).

Warmerdam gives the open source version. README files, guides, API references,
and examples help people use a project. Contribution guides and polite
interaction help people maintain it
([[podcast:open-source-ml-contributions|Contribute to Open Source ML at 22:20 and 24:10]]).

Those patterns belong with [[Documentation]],
[[Developer Experience]],
and [[Open Source and Developer Relations]].

## Monitoring, Feedback, and Ownership

Practices need feedback loops or they turn into ceremony. Bergh separates
customer validation from data and model validity, then links observability to
data quality and production errors
([[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps at 7:22 and 24:59]]).
Hoogvliets uses feedback loops inside MLOps adoption. His team collects pain
points, delivers quick wins, and measures deployment frequency. Platform work
stays tied to product-team needs
([[podcast:mlops-at-scale-reproducibility-adoption|MLOps at Scale at 27:56 / 32:46 / 36:55]]).

Vechtomova makes the organizational version when she discusses buy-in and DevOps
cooperation. Monitoring standardization and centralized support for smaller
brands sit in the same adoption work
([[podcast:pragmatic-and-standardized-mlops|Pragmatic MLOps at 34:29 / 35:21 / 42:53 / 51:24]]).

Ownership changes with the domain because DataOps spans pipelines,
environments, quality, and recovery. MLOps covers model release, monitoring,
reproducibility, and support for product teams. Experimentation ownership stays
close to metric design and assignment tracking. Power analysis and
interpretation stay with the same owner, as Graff explains in
[[podcast:ab-testing-and-product-experimentation|Product Analytics and A/B Testing at 14:27 / 24:44 / 37:44 / 47:44]].

Those differences matter for role pages such as
[[MLOps Engineer]] and for
[[MLOps vs DataOps]].
