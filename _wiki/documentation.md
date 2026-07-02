---
layout: wiki
title: "Documentation"
summary: "How documentation supports adoption, team memory, operations, onboarding, portfolio evidence, and open-source maintenance in data and ML work."
related:
  - Technical Writing
  - Developer Relations
  - Contributing
  - Practices
  - Open Source and Developer Relations
---

## Documentation in Data and ML Work

Documentation is the written or recorded material that helps another person use
technical work. It also helps them maintain, evaluate, or extend that work.

DataTalks.Club guests discuss README files and quickstarts, along with
tutorials, API references, and examples. They also discuss contribution guides,
design docs, and decision logs. Model cards and datasheets belong in the same
family as runbooks, onboarding notes, and portfolio repo tours.

The most practical open-source definition comes from
[[person:vincentwarmerdam|Vincent Warmerdam]] in
[[podcast:open-source-ml-contributions|Contribute to Open Source ML]].
At 22:20, he lists README material, guides, and API reference as project
essentials. Examples matter too. At 24:10, he connects contribution guides with
community etiquette. At 25:50, he treats reproducible issues and small
documentation fixes as real contributions.

This topic covers documentation as a project and team practice. Use
[[Technical Writing]] for the
writing workflow, [[Developer Relations]]
for demos and tool adoption, and [[Contributing]]
for contribution paths that include docs.

## Documentation as Coordination Infrastructure

Across these episodes, documentation is useful when it lowers coordination cost. It
helps a user run a tool. It helps a teammate understand a decision, an operator
recover from failure, or a hiring manager look at a project.

[[person:eugeneyan|Eugene Yan]] expands the definition
in
[[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]].
At 51:00, he discusses working-backwards documents, press releases, and design
docs. At 54:00, he adds decision logs, rationales, and team memory. At 56:30,
he recommends portfolio READMEs, quickstarts, and repo tours so another person
can understand the work without private context.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] explains
the adoption role in
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]].
At 18:03, he defines DevRel through education, documentation, and a "wisdom
layer" around tools. At 25:17, he connects documentation feedback with
dogfooding and developer collaboration. Documentation isn't only text after
the product ships. Teams also use it to find where the product is hard to use.

## Readers and Use Cases

Guests agree that documentation makes technical work easier to use, but they
focus on different readers.

Vincent focuses on open-source users and maintainers. In
[[podcast:open-source-ml-contributions|Contribute to Open Source ML]],
docs explain the project and set contribution expectations. They also reduce
maintainer load. Around 27:40, he links first code pull requests to tests, CI,
and packaging. He also names pre-commit, which makes documentation part of the
review system.

Eugene focuses on future teammates and future readers. In
[[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]],
the 14:00 chapter starts from audience choice. The 25:00 chapter uses an
outline-first method, and the 54:00 chapter treats decision records as a way to
keep reasoning available after the meeting ends.

Hugo and [[person:willrussell|Will Russell]] focus on
developers trying to adopt tools. Hugo's 43:14 chapter says tutorials should
start from audience and goals. In
[[podcast:practical-devrel-demofirst-education-and-open-source|Developer Advocacy Through Community Impact]],
Will describes developer advocacy through documentation, demos, and outreach at
49:14. At 51:49, he describes a content workflow based on bullet points, demos,
and collaboration with writers.

[[person:nadianahar|Nadia Nahar]] adds a software
engineering and accountability lens in
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]].
At 13:52, documentation appears with shared vocabulary and expectation setting.
At 42:47, model cards and datasheets become documentation for ML products.
Factsheets and checklists belong there too. They aren't just communication
material.

## Docs for Data and ML Systems

Data and ML systems need documentation because their behavior depends on data
and requirements. Ownership and operating context matter too. Code alone rarely
shows those assumptions.

Nadia's
[[podcast:software-engineering-for-machine-learning|Software Engineering for ML]]
episode is the strongest ML-system reference. At 10:12, she frames ML products
through hidden technical debt. At 29:42, she discusses failure modes such as
unmet requirements, poor data, and deployment issues. Her 39:05 chapter puts
documentation next to workshops and shared vocabularies. She treats docs as
part of engineering remediation.

For ML systems, documentation supports [[software engineering]],
[[MLOps]], and
[[machine learning system design]].

For analytics and data products, teams document the models they expect others
to trust. The
[[Analytics Engineering]]
page links dbt-style modeling to tests, docs, lineage, and business
definitions. Those docs help users understand metrics and model dependencies.
They also help teams review changes before dashboards and forecasts break.

System design docs have a different job: they expose assumptions before a team
builds. Use
[[ML System Design Documents]]
for design-doc structure and
[[Machine Learning System Design]]
for the surrounding design choices. Those choices include data, baselines, and
evaluation. They also include serving, monitoring, fallbacks, and ownership.

## Runbooks and Operational Memory

Runbooks make documentation part of operations. They explain what to check, who
owns the system, how to recover, and when to escalate.

[[person:christopherbergh|Christopher Bergh]] gives the
clearest operational version in
[[podcast:dataops-automation-and-reliable-data-pipelines|Mastering DataOps]].
At 33:47, he lists version control, tests, and CI/CD as practical steps for
healthier data pipelines. At 34:37, he moves from runbooks to automated
playbooks. At 38:01, he connects handoffs and documentation to replaceability.
He also connects them to reduced on-call load.

That makes runbooks part of [[DataOps]]
and [[data-quality-and-observability|data observability]], not
just a support artifact. A runbook is weak when it only documents the happy
path. It becomes useful when it captures failure signals, recovery steps,
and owners. Rollback options and tradeoffs matter too.

## Technical Writing and Team Memory

Technical writing becomes documentation when it preserves a decision or makes a
workflow reproducible. Eugene's
[[podcast:technical-writing-for-data-scientists|Technical Writing for Data Scientists]]
episode links public writing and workplace writing. At 20:00, he describes a
repeatable writing cadence. At 25:00, he starts from an outline. At 51:00 and
54:00, the same habits apply to design docs, rationales, and decision logs.

Good team documentation says what changed and why. It also says what the team
decided not to do. That matters for [[practices]]
such as versioning, tests, CI/CD, and monitoring. Ownership and feedback loops
need the same context.
Without the rationale, a future teammate may repeat an old debate or undo a
constraint that still matters.

Portfolio documentation uses the same reader-focused logic. Eugene's 56:30
chapter recommends a clear README, quickstart, and repo tour. Those artifacts
also show up in
[[data engineering portfolio projects]],
[[machine learning portfolio projects]],
and [[open-source-portfolio-evidence|open-source portfolio evidence]].
The repo should let another person look at the problem, setup, tradeoffs, and
verification path.

## Onboarding and Developer Experience

Documentation is part of [[developer experience]]
because first use is often where adoption fails. Hugo's
[[podcast:devrel-open-source-machine-learning|DevRel Role for Machine Learning]]
episode makes that explicit. At 36:27, he connects teaching reproducibility to
dogfooding and simplified workflows. At 43:14, he discusses tutorial structure
through audience and goals.

Will's
[[podcast:practical-devrel-demofirst-education-and-open-source|Developer Advocacy Through Community Impact]]
episode adds the demo side. At 53:40, he recommends videos with a clear goal,
useful pace, and full walkthroughs. At 57:22, his "Learn with Kestra" examples
include adjacent tools such as Docker, Postgres, and Git. That matters because
onboarding rarely depends on one product only. Users need the surrounding setup
too.

These examples connect documentation to
[[developer relations]],
[[community building]], and
[[technical writing]]. Docs and
demos help users move from curiosity to a first successful result. Workshops,
office hours, and examples can do the same.

## Open-Source Contribution Paths

Open-source documentation has two audiences: users trying to solve a problem
and contributors trying to help the project. Vincent's open-source ML episode
keeps both in view. At 22:20, he names README files, guides, and API
references. Examples matter too.

At 24:10, he covers contribution guides and polite interaction. At 25:50, he
treats reproducible issues and docs fixes as contribution paths.

Will gives the mentorship side in
[[podcast:practical-devrel-demofirst-education-and-open-source|Developer Advocacy Through Community Impact]]
episode. Around 35:43 and 39:02, he discusses mentorship and pull request
quality. He also covers Git skills and onboarding into large repositories.
Around 41:16, he adds environment setup and maintainer collaboration.

Good open-source docs include setup steps, contribution expectations, and
examples. They give newcomers enough context to avoid wasting maintainer time.

This is why documentation belongs with
[[open source]],
[[contributing]], and
[[open source and developer relations]].
Docs work isn't a lesser form of contribution. It can be the change that makes
the next code contribution possible.

## Related Pages

Use these pages for adjacent documentation topics:

- [[Technical Writing]]
- [[Developer Relations]]
- [[Developer Experience]]
- [[Contributing]]
- [[Practices]]
- [[Open Source and Developer Relations]]
- [[Open Source Portfolio Evidence]]
- [[ML System Design Documents]]
- [[DataOps]]
- [[data-quality-and-observability|Data Observability]]
