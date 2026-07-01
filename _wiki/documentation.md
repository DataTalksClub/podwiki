---
layout: wiki
title: "Documentation"
summary: "Podcast-grounded reference on documentation as adoption infrastructure, team memory, operational practice, onboarding support, portfolio evidence, and open-source maintenance."
related:
  - Technical Writing
  - Developer Relations
  - Contributing
  - Practices
  - Open Source and Developer Relations
---

## Definition and Scope

Documentation is the written or recorded material that helps another person use
technical work. It also helps them maintain, evaluate, or extend that work.

DataTalks.Club guests discuss README files and quickstarts, along with
tutorials, API references, and examples. They also discuss contribution guides,
design docs, and decision logs. Model cards and datasheets belong in the same
family as runbooks, onboarding notes, and portfolio repo tours.

The most practical open-source definition comes from
[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
At 22:20, he lists README material, guides, and API reference as project
essentials. Examples matter too. At 24:10, he connects contribution guides with
community etiquette. At 25:50, he treats reproducible issues and small
documentation fixes as real contributions.

This topic covers documentation as a project and team practice. Use
[Technical Writing]({{ '/wiki/technical-writing/' | relative_url }}) for the
writing workflow, [Developer Relations]({{ '/wiki/developer-relations/' | relative_url }})
for demos and tool adoption, and [Contributing]({{ '/wiki/contributing/' | relative_url }})
for contribution paths that include docs.

## Common Definition

Across these episodes, documentation is useful when it lowers coordination cost. It
helps a user run a tool. It helps a teammate understand a decision, an operator
recover from failure, or a hiring manager look at a project.

[Eugene Yan]({{ '/people/eugeneyan/' | relative_url }}) expands the definition
in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}).
At 51:00, he discusses working-backwards documents, press releases, and design
docs. At 54:00, he adds decision logs, rationales, and team memory. At 56:30,
he recommends portfolio READMEs, quickstarts, and repo tours so another person
can understand the work without private context.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) gives
the adoption version in
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }}).
At 18:03, he defines DevRel through education, documentation, and a "wisdom
layer" around tools. At 25:17, he connects documentation feedback with
dogfooding and developer collaboration. Documentation isn't just text after
the product ships. It's one way a team discovers where the product is hard to
use.

## Guest Differences

Guests agree that documentation makes technical work easier to use, but they
focus on different readers.

Vincent focuses on open-source users and maintainers. In
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}),
docs explain the project and set contribution expectations. They also reduce
maintainer load. Around 27:40, he links first code pull requests to tests, CI,
and packaging. He also names pre-commit, which makes documentation part of the
review system.

Eugene focuses on future teammates and future readers. In
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}),
the 14:00 chapter starts from audience choice. The 25:00 chapter uses an
outline-first method, and the 54:00 chapter treats decision records as a way to
keep reasoning available after the meeting ends.

Hugo and [Will Russell]({{ '/people/willrussell/' | relative_url }}) focus on
developers trying to adopt tools. Hugo's 43:14 chapter says tutorials should
start from audience and goals. In
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }}),
Will describes developer advocacy through documentation, demos, and outreach at
49:14. At 51:49, he describes a content workflow based on bullet points, demos,
and collaboration with writers.

[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) adds a software
engineering and accountability lens in
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }}).
At 13:52, documentation appears with shared vocabulary and expectation setting.
At 42:47, model cards and datasheets become documentation for ML products.
Factsheets and checklists belong there too. They aren't just communication
material.

## Docs for Data and ML Systems

Data and ML systems need documentation because their behavior depends on data
and requirements. Ownership and operating context matter too. Code alone rarely
shows those assumptions.

Nadia's
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})
episode is the strongest ML-system reference. At 10:12, she frames ML products
through hidden technical debt. At 29:42, she discusses failure modes such as
unmet requirements, poor data, and deployment issues. Her 39:05 chapter puts
documentation next to workshops and shared vocabularies. It also connects docs
to engineering remedies.

That connects documentation to [software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).

For analytics and data products, documentation appears as part of trusted
models. The
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
page links dbt-style modeling to tests, docs, lineage, and business
definitions. Those docs help users understand metrics and model dependencies.
They also help teams review changes before dashboards and forecasts break.

System design docs have a different job: they expose assumptions before a team
builds. Use
[ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
for design-doc structure and
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
for the surrounding design choices. Those choices include data, baselines, and
evaluation. They also include serving, monitoring, fallbacks, and ownership.

## Runbooks and Operational Memory

Runbooks turn documentation into an operating practice. They explain what to
check, who owns the system, how to recover, and when to escalate.

[Christopher Bergh]({{ '/people/christopherbergh/' | relative_url }}) gives the
clearest operational version in
[Mastering DataOps]({{ '/podcasts/dataops-automation-and-reliable-data-pipelines/' | relative_url }}).
At 33:47, he lists version control, tests, and CI/CD as practical steps for
healthier data pipelines. At 34:37, he moves from runbooks to automated
playbooks. At 38:01, he connects handoffs and documentation to replaceability.
He also connects them to reduced on-call load.

That makes runbooks part of [DataOps]({{ '/wiki/dataops/' | relative_url }})
and [data observability]({{ '/wiki/data-observability/' | relative_url }}), not
just a support artifact. A runbook is weak when it only documents the happy
path. It becomes useful when it captures failure signals, recovery steps,
and owners. Rollback options and tradeoffs matter too.

## Technical Writing and Team Memory

Technical writing becomes documentation when it preserves a decision or makes a
workflow reproducible. Eugene's
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }})
episode links public writing and workplace writing. At 20:00, he describes a
repeatable writing cadence. At 25:00, he starts from an outline. At 51:00 and
54:00, the same habits apply to design docs, rationales, and decision logs.

Good team documentation says what changed and why. It also says what the team
decided not to do. That matters for [practices]({{ '/wiki/practices/' | relative_url }})
such as versioning, tests, CI/CD, and monitoring. Ownership and feedback loops
need the same context.
Without the rationale, a future teammate may repeat an old debate or undo a
constraint that still matters.

Portfolio documentation uses the same idea for a public reader. Eugene's 56:30
chapter recommends a clear README, quickstart, and repo tour. Those artifacts
also show up in
[data engineering portfolio projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
[machine learning portfolio projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
and [open-source portfolio evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).
The repo should let another person look at the problem, setup, tradeoffs, and
verification path.

## Onboarding and Developer Experience

Documentation is part of [developer experience]({{ '/wiki/developer-experience/' | relative_url }})
because first use is often where adoption fails. Hugo's
[DevRel Role for Machine Learning]({{ '/podcasts/devrel-open-source-machine-learning/' | relative_url }})
episode makes that explicit. At 36:27, he connects teaching reproducibility to
dogfooding and simplified workflows. At 43:14, he discusses tutorial structure
through audience and goals.

Will's
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }})
episode adds the demo side. At 53:40, he recommends videos with a clear goal,
useful pace, and full walkthroughs. At 57:22, his "Learn with Kestra" examples
include adjacent tools such as Docker, Postgres, and Git. That matters because
onboarding rarely depends on one product only. Users need the surrounding setup
too.

This is where documentation overlaps with
[developer relations]({{ '/wiki/developer-relations/' | relative_url }}),
[community building]({{ '/wiki/community-building/' | relative_url }}), and
[technical writing]({{ '/wiki/technical-writing/' | relative_url }}). Docs and
demos help users move from curiosity to a first successful result. Workshops,
office hours, and examples can do the same.

## Open-Source Docs

Open-source documentation has two audiences: users trying to solve a problem
and contributors trying to help the project. Vincent's open-source ML episode
keeps both in view. At 22:20, he names README files, guides, and API
references. Examples matter too.

At 24:10, he covers contribution guides and polite interaction. At 25:50, he
treats reproducible issues and docs fixes as contribution paths.

Will gives the mentorship side in
[Developer Advocacy Through Community Impact]({{ '/podcasts/practical-devrel-demofirst-education-and-open-source/' | relative_url }})
episode. Around 35:43 and 39:02, he discusses mentorship and pull request
quality. He also covers Git skills and onboarding into large repositories.
Around 41:16, he adds environment setup and maintainer collaboration.

Good open-source docs should include setup steps, contribution expectations,
and examples. They should give newcomers enough context to avoid wasting
maintainer time.

This is why documentation belongs with
[open source]({{ '/wiki/open-source/' | relative_url }}),
[contributing]({{ '/wiki/contributing/' | relative_url }}), and
[open source and developer relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }}).
Docs work isn't a lesser form of contribution. It can be the change that makes
the next code contribution possible.

## Related Pages

Use these pages for adjacent documentation topics:

- [Technical Writing]({{ '/wiki/technical-writing/' | relative_url }})
- [Developer Relations]({{ '/wiki/developer-relations/' | relative_url }})
- [Developer Experience]({{ '/wiki/developer-experience/' | relative_url }})
- [Contributing]({{ '/wiki/contributing/' | relative_url }})
- [Practices]({{ '/wiki/practices/' | relative_url }})
- [Open Source and Developer Relations]({{ '/wiki/open-source-and-developer-relations/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [ML System Design Documents]({{ '/wiki/ml-system-design-documents/' | relative_url }})
- [DataOps]({{ '/wiki/dataops/' | relative_url }})
- [Data Observability]({{ '/wiki/data-observability/' | relative_url }})
