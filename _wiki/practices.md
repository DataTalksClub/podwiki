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
[DataOps]({{ '/wiki/dataops/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}). They also use it around
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[experimentation]({{ '/wiki/experimentation/' | relative_url }}), and
[open source]({{ '/wiki/open-source/' | relative_url }}). A practice must make
work repeatable and visible to others. It must change how a team ships,
reviews, or recovers.

[Christopher Bergh](https://datatalks.club/people/christopherbergh.html) gives
the DataOps version in
[Mastering DataOps at 6:42](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html).
Teams reduce errors, shorten deployment cycle time, and improve productivity.
[Maria Vechtomova](https://datatalks.club/people/mariavechtomova.html) gives the
MLOps version in
[Pragmatic MLOps at 11:10 and 12:42](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html).
Teams enable reproducible model delivery with shared infrastructure, reusable
CI/CD, and standard repositories. Registries and monitoring complete that
baseline.
Nikolay Smorchkov's
[Software Development at Rocket Speed](https://datatalks.club/books/20251006-software-development-at-rocket-speed.html)
addresses the same delivery-speed question from the software side: how
requirements decomposition, estimation, and incremental delivery keep teams
shipping rather than stuck in analysis.

## Adoption and Scope

Guests disagree less about the value of practices than about where to start.
Bergh argues from an automation-first DataOps view. Version control, tests, and
CI/CD cover the path from data to model to visualization. Runbooks,
observability, and environment management support the same path
([Mastering DataOps at 33:47 / 34:37 / 56:32](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).

Vechtomova starts with the infrastructure a company already has. In
[Pragmatic MLOps at 16:27 and 18:41](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html),
she names Git, Kubernetes, and CI/CD before more specialized platform work. She
also includes registries, object storage, and model registry options.

[Raphaël Hoogvliets](https://datatalks.club/people/raphaelhoogvliets.html) puts
developer experience and trust first. His MLOps team collects pain points and
delivers quick wins. It watches deployment frequency and standardizes only
after teams see value
([MLOps at Scale at 27:56 / 32:46 / 36:55](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html)).
[Nadia Nahar](https://datatalks.club/people/nadianahar.html) puts shared
vocabulary and requirements alignment near the center. Documentation matters
for her because ML systems fail through organizational ambiguity as well as code
defects
([Software Engineering for ML at 13:52 and 39:05](https://datatalks.club/podcast/software-engineering-for-machine-learning.html)).

## Versioning and Reproducibility

Version control is the baseline practice for [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). Bergh includes version
control, tests, and CI/CD in his seven practical steps for healthier pipelines.
He then widens versioning beyond code to models, visualizations, and governance
([Mastering DataOps at 33:47 and 51:21](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).
That wider scope matters for [production]({{ '/wiki/production/' | relative_url }})
because a team can't recover or audit a data product if only the application
repository has history.

In the MLOps episodes, Vechtomova discusses model registries, artifact storage,
and service principals. She also covers standard repositories and moving
notebook logic into packages
([Pragmatic MLOps at 20:49 / 29:55 / 33:24](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)).

Hoogvliets ties reproducibility to data versioning, traceability, and
experiment capture. Dependency management, package registries, containers, and
deployment records belong in the same operating model
([MLOps at Scale at 42:31 / 53:08 / 56:50](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html)).
Those concerns overlap with [CI/CD]({{ '/wiki/ci-cd/' | relative_url }}),
[MLOps tools]({{ '/wiki/mlops-tools/' | relative_url }}), and
[data governance]({{ '/wiki/data-governance/' | relative_url }}).

## Testing and Quality Gates

Testing changes by domain because data pipelines need data quality checks plus
snapshot, SQL, Spark, and integration coverage. In
[Production AI Engineering at 9:05 / 11:47 / 13:14](https://datatalks.club/podcast/production-ready-ai-engineering.html),
[Bartosz Mikulski](https://datatalks.club/people/bartoszmikulski.html) compares
tools such as Great Expectations and Soda with SQL-based and Spark-based tests.
He treats testing as a way to stop the familiar "this number doesn't look
correct" failure before it reaches users.

The same episode extends quality gates into AI applications through prompt
evaluation. Prompt compression tradeoffs and caching decisions also sit in that
quality discussion
([Production AI Engineering at 28:16 / 30:00 / 31:45](https://datatalks.club/podcast/production-ready-ai-engineering.html)).

Product experiments need different gates. In
[Product Analytics and A/B Testing at 8:13 and 24:44](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html),
[Jakob Graff](https://datatalks.club/people/jakobgraff.html) focuses on
randomization, traffic assignment, and assignment tracking. Monitoring belongs
with the same experimental gate. He also links reliable experiments to A/A
tests and metric stability. Power analysis, statistical tests, and distribution
checks round out the practice
([Product Analytics and A/B Testing at 27:52 / 33:23 / 37:44 / 40:23 / 44:39](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html)).

Those practices belong with [A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[A/A Testing]({{ '/wiki/a-a-testing/' | relative_url }}), and
[Causal Inference]({{ '/wiki/causal-inference/' | relative_url }}) rather than
generic software unit testing.

Open source projects expose the social side of testing. In
[Contribute to Open Source ML at 25:50 and 27:40](https://datatalks.club/podcast/open-source-ml-contributions.html),
[Vincent Warmerdam](https://datatalks.club/people/vincentwarmerdam.html) connects
good issues and pull requests to reproducible examples, tests, and CI.
Packaging and pre-commit hooks help maintainers review faster because the
failure is easy to reproduce. That makes testing part of
[open source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
as well as part of [software engineering]({{ '/wiki/software-engineering/' | relative_url }}).

## CI/CD and Release Paths

CI/CD reduces release risk across DataOps, MLOps, and open source. Bergh links
CI/CD to deployment cycle time and production reliability in the DataOps
episode. He also covers end-to-end testing and test data
([Mastering DataOps at 6:42 / 33:47 / 43:06 / 44:12](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).

Vechtomova describes reusable CI/CD templates and standardized repositories as
central MLOps team responsibilities
([Pragmatic MLOps at 12:42 and 29:55](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)).
Hoogvliets lists CI, repository structure, parameterization, and testing as
core MLOps habits. Package registries and deployment frequency show whether the
release path works
([MLOps at Scale at 39:06 / 48:41 / 53:08](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html)).

CI/CD is more than a pipeline runner in these discussions. Teams use it to
encode quality gates and packaging rules. They also encode environment
assumptions and handoff expectations.

For model systems, this work belongs to
[MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) practice.

For data pipelines, it sits next to
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
and [DataOps tools]({{ '/wiki/dataops-tools/' | relative_url }}).

For open source, Warmerdam shows the same habit through contribution guides and
tests. Packaging checks and pre-commit hooks help too
([Contribute to Open Source ML at 22:20 / 24:10 / 27:40](https://datatalks.club/podcast/open-source-ml-contributions.html)).

## Documentation and Handoffs

Documentation counts as a practice when it changes how people hand off work.
Nahar connects documentation to shared vocabulary, expectation setting,
requirements, and data assumptions. Model Cards, Datasheets, factsheets, and
checklists belong in the same documentation family. Responsible AI
accountability does too
([Software Engineering for ML at 13:52 / 39:05 / 42:47 / 54:16](https://datatalks.club/podcast/software-engineering-for-machine-learning.html)).
Useful documentation keeps model behavior, stakeholder expectations, and team
responsibilities visible while the system changes.

Bergh makes the operational version of the same argument. Runbooks become a
bridge from manual checklists to automated playbooks. Documentation reduces
fragile handoffs and on-call load
([Mastering DataOps at 34:37 and 38:01](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).

Warmerdam gives the open source version. README files, guides, API references,
and examples help people use a project. Contribution guides and polite
interaction help people maintain it
([Contribute to Open Source ML at 22:20 and 24:10](https://datatalks.club/podcast/open-source-ml-contributions.html)).

Those patterns belong with [Documentation]({{ '/wiki/documentation/' | relative_url }}),
[Developer Experience]({{ '/wiki/developer-experience/' | relative_url }}),
and [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }}).

## Monitoring, Feedback, and Ownership

Practices need feedback loops or they turn into ceremony. Bergh separates
customer validation from data and model validity, then links observability to
data quality and production errors
([Mastering DataOps at 7:22 and 24:59](https://datatalks.club/podcast/dataops-automation-and-reliable-data-pipelines.html)).
Hoogvliets uses feedback loops inside MLOps adoption. His team collects pain
points, delivers quick wins, and measures deployment frequency. Platform work
stays tied to product-team needs
([MLOps at Scale at 27:56 / 32:46 / 36:55](https://datatalks.club/podcast/mlops-at-scale-reproducibility-adoption.html)).

Vechtomova makes the organizational version when she discusses buy-in and DevOps
cooperation. Monitoring standardization and centralized support for smaller
brands sit in the same adoption work
([Pragmatic MLOps at 34:29 / 35:21 / 42:53 / 51:24](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)).

Ownership changes with the domain because DataOps spans pipelines,
environments, quality, and recovery. MLOps covers model release, monitoring,
reproducibility, and support for product teams. Experimentation ownership stays
close to metric design and assignment tracking. Power analysis and
interpretation stay with the same owner, as Graff explains in
[Product Analytics and A/B Testing at 14:27 / 24:44 / 37:44 / 47:44](https://datatalks.club/podcast/ab-testing-and-product-experimentation.html).

Those differences matter for role pages such as
[MLOps Engineer]({{ '/wiki/mlops-engineer/' | relative_url }}) and for
[MLOps vs DataOps]({{ '/wiki/mlops-vs-dataops/' | relative_url }}).
