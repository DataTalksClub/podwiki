---
layout: wiki
title: "Portfolio Projects"
summary: "Guidance for choosing data, analytics, ML, AI, and open-source portfolio projects with reviewable evidence and role fit."
related:
  - Career Development
  - Job Search
  - CV Screening
  - Data Engineering Portfolio Projects
  - Analytics Engineering Portfolio Projects
  - Machine Learning Portfolio Projects
  - RAG Portfolio Projects
  - Open Source Portfolio Evidence
  - End-to-End Data Pipeline Project
  - Dashboard and Metric Layer Project Checklist
  - Production ML Project Checklist
  - Search and RAG Project Checklist
---

A portfolio project is public evidence of judgment, not a tool demo. It
connects a real problem to data, code, and evaluation. It also shows operation
and a defensible interview story.

Choose a project by evidence type. A strong project is reviewable, grounded in a
decision, and easy to discuss.

[[Data Engineering Portfolio Projects]] covers pipeline and platform proof.
That evidence should show source behavior and table modeling, with orchestration
and recovery visible in the same project.
[[Analytics Engineering Portfolio Projects]] covers modeled metrics, business
definitions, and BI-ready marts.

[[Machine Learning Portfolio Projects]] covers model proof because those
projects show problem framing, baselines, and labels. They also show
validation, evaluation, serving boundaries, and production awareness.

[[RAG Portfolio Projects]] covers retrieval-backed LLM proof because those
projects show corpus choice, chunking, and retrieval evidence. They also show
citations and evaluation.
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]] covers
the broader artifact that combines product software and agents with evaluation
and deployment.

[[person:jeffkatz=>Jeff Katz]] and
[[person:ellenkonig=>Ellen König]] ground the data
engineering version. In
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep]]
and
[[cite:from-software-engineering-data-science-to-data-engineering-leadership=>How to Become a Data Engineer]],
they connect project evidence to fundamentals and clean code. They also connect
it to domain work and reviewable pipelines.

[[person:victoriaperezmola=>Victoria Perez Mola]] and
[[person:juanmanuelperafan=>Juan Manuel Perafan]] ground
the analytics engineering version. Their episodes connect portfolio evidence to
SQL modeling, data quality, and documentation. They also connect it to business
reality and BI consumption
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].

[[person:valeriybabushkin=>Valeriy Babushkin]] grounds
the machine learning version through baselines, validation, and production
robustness. [[person:benwilson=>Ben Wilson]] and
[[person:nadianahar=>Nadia Nahar]] add maintainable code
and tests. They also add serving boundaries, monitoring, and software
integration
[[cite:machine-learning-system-design-interview=>Machine Learning System Design Interview]]
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]].

[[person:atitaarora=>Atita Arora]] and
[[person:hugobowneanderson=>Hugo Bowne-Anderson]] ground
the RAG version. Their episodes make chunking, retrieval evidence, citations,
and gold tests part of the project. Failure labels and traces aren't optional
polish
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Reviewable Project Standard

A strong portfolio project makes the work reviewable by naming the consumer or
decision. It shows the input data and the transformation or modeling path. It
includes quality checks, evaluation, or both. It also has a README or writeup
that lets another person run, review, or question the work.

The project should answer these review questions:

- What decision or workflow changes if the project works?
- Which data enters the system, and what assumptions come with it?
- Which baseline or simpler version does the project improve on?
- Which checks catch bad data, bad logic, weak retrieval, or model failure?
- How can a reviewer run the project or look at the result?

[[person:dannyma=>Danny Ma]] adds a learning-order test:
start by building, then learn the theory when the project exposes a real gap
[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]].
That makes the project more reviewable. The writeup can show where a method,
metric, model, or tool became necessary instead of presenting theory as
decoration.

[[person:sarahmestiri=>Sarah Mestiri]] makes the job-search version of the same
point. Courses can help someone explore a direction. A project tests whether
the person can use the skill and still wants that role. A portfolio should turn
course learning into role-shaped practical work before the next course becomes
the default step
[[cite:job-search-strategy-in-tech-projects-skills-cv-networking@26:28=>Tech Job Search Strategy]].

[[person:marijnmarkus=>Marijn Markus]] adds a differentiation test. A project
can stand out when it grows from a real curiosity or domain problem. It doesn't
have to be another leaderboard clone. His examples include home automation,
plant sensors, and coffee-machine time series.

Those projects show data collection and time series reasoning. They also show
storytelling in a way a generic Kaggle notebook may not
[[cite:how-to-stand-out-in-data-science@36:21=>Data Science Career Playbook]]
[[cite:how-to-stand-out-in-data-science@37:49=>Data Science Career Playbook]].
Use Kaggle when it fits the target role, but don't let it be the only proof of
judgment.

Pauline Clavelloux's indie projects show the same learning sequence outside a
course. Cryptopy and UnrealMe forced work across GCP, data engineering, and web
development. They also exposed launch channels, pricing, and marketing. A
portfolio writeup should name those acquired skills and connect them to the
project evidence. That matters when the role crosses [[machine learning]],
product, and operations
[[cite:data-scientist-and-indie-hacker-bootstrapping-side-projects@35:47=>Indie Hacking Side Projects]].

[[person:eugeneyan=>Eugene Yan]] adds the writeup
standard in
[[cite:technical-writing-for-data-scientists=>Technical Writing for Data Scientists]].
He describes outlines and section headers. He also covers topic sentences and
supporting evidence. That structure works for portfolio case studies because the
project has to explain its assumptions and evidence.

## Portfolio Signals Across Roles

Start with reviewable fundamentals instead of tool lists.
[[person:jeffkatz=>Jeff Katz]] says portfolios should
show Python, SQL, code structure, and tests. They should also show public or
personal projects in
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep]].
That advice applies to
[[data engineering]],
[[analytics engineering]],
[[machine learning]], and
[[AI engineering]] portfolios.

Every project needs a consumer, a decision, or a business question.
[[person:lukewhipps=>Luke Whipps]] frames projects as
resume evidence in
[[cite:get-data-scientist-job=>Land Data Scientist Roles]].
[[person:nicksingh=>Nick Singh]] treats project
walkthroughs as interview evidence in
[[cite:data-interview-behavioral-and-portfolio-prep-guide=>Ace Data Interviews]].

Portfolio work becomes part of [[job search]]
and [[CV screening]] when it gives
hiring teams concrete evidence to review.

End-to-end proof beats notebook-only proof. [[person:santonatuli=>Santona Tuli]]
shows how a pipeline moves from ingestion to transformation, modeled outputs,
and consumers in
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
[[person:nataliekwong=>Natalie Kwong]] adds modern-stack
boundaries in
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and the Modern Data Stack]].
Santona covers pipeline stages. Natalie covers ingestion, transformation, marts,
and warehouse boundaries.

Those episodes support
[[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]]
as the concrete data-pipeline blueprint.

## Choosing a Project Type

Choose [[data engineering]] when
the project should prove ingestion, modeling, orchestration, and recovery. The
best project has a real source behavior, a modeled output, and a rerun path.
[[person:santonatuli=>Santona Tuli]] grounds that choice in
pipeline stages, orchestration, and consumers
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
[[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]]
is the concrete data-pipeline blueprint.

Choose [[analytics engineering]]
when the project should prove business definitions and reusable SQL models. The
best project has source assumptions and table grain. It also has tests,
documentation, and a BI or query surface.

[[person:victoriaperezmola=>Victoria Perez Mola]] and
[[person:juanmanuelperafan=>Juan Manuel Perafan]] connect
those signals to dbt and data quality. They also connect them to business
definitions and BI consumption
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].
[[Dashboard and Metric Layer Project Checklist]]
covers metric-centered portfolio evidence.

Choose [[machine learning]] when
the project should prove problem framing and data strategy. It also needs
baselines, evaluation, and software boundaries.
[[person:valeriybabushkin=>Valeriy Babushkin]] anchors this
in baselines and validation. He also covers features, labels, and production
robustness
[[cite:machine-learning-system-design-interview=>Machine Learning System Design Interview]].
[[Production ML Project Checklist]]
fits target roles in [[MLOps]], ML platforms,
or machine learning engineering.

Choose [[retrieval-augmented-generation=>RAG]] when
the project should prove retrieval quality and grounded generation. The best
project shows the corpus and chunks. It also shows metadata, retrieved evidence,
citations, and failure analysis.

[[person:atitaarora=>Atita Arora]] ties this to chunking
and embeddings. She also ties it to citations and evaluation
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
[[Search and RAG Project Checklist]]
is the practical review checklist.

Choose [[open source]] when public
collaboration is the strongest evidence. A smaller issue or docs fix can be
more credible than a large unfinished app. A reproducible bug, test, or example
can work too.

[[person:vincentwarmerdam=>Vincent Warmerdam]] grounds that
path in reproducible issues and small fixes. He also covers tests and CI.
Packaging and maintainer discussion matter too
[[cite:open-source-ml-contributions=>Contribute to Open Source ML]].
[[Open Source Portfolio Evidence]]
and the
[[Open Source Contributor Roadmap]]
cover that path.

## Project Boundaries

A project becomes credible when the repository and writeup expose the tradeoffs.
Data projects should show source behavior and table grain. They should also
show orchestration, quality checks, and recovery. [[Data Engineering Portfolio
Projects]] gives the detailed pipeline checklist.

Analytics projects should show metric ownership and a consumption surface.
[[Analytics Engineering Portfolio Projects]] gives those proof patterns.

ML projects should show a baseline, validation, serving boundary, and monitoring
plan. [[Machine Learning Portfolio Projects]] gives the detailed model-proof
standard. RAG projects should show retrieval examples, citations, and failure
labels. [[RAG Portfolio Projects]] and
[[Search and RAG Project Checklist]] give retrieval-specific review points.

Role fit matters here because an analyst-style project should make exploration,
visualization, and the final decision clear. A builder-style project should add
packaging, deployment, and operational failure modes. A consultant-style project
should show stakeholder framing and the recommendation a decision maker could
act on
[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]].

Don't add tools before the project needs them. [[person:adrianbrudaru=>Adrian Brudaru]]
ties modern tool choices to requirements in
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering Trends]].
[[person:slawomirtulski=>Slawomir Tulski]] warns against
over-engineered platforms in
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]].

The same rule applies to AI projects. Start with a reliable retrieval or model
baseline before adding agents, long-context tricks, or fine-tuning.
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
and
[[Graph RAG vs Vector RAG]]
cover those design choices.

Production awareness is stronger than model novelty, and [[Machine Learning
Portfolio Projects]] covers that evidence.
[[person:benwilson=>Ben Wilson]] connects maintainable code, tests, and
production engineering in
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]].
[[person:marianosemelman=>Mariano Semelman]] shows the notebook-to-production path in
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].
[[Production ML Project Checklist]] covers project claims about production
readiness.

## Public Proof and Open Source

Open-source work is portfolio evidence when review pressure is visible. Issues,
docs, tests, and demos can be stronger than a private tutorial repository. Pull
requests, CI, and maintainer discussion strengthen the proof.

[[person:vincentwarmerdam=>Vincent Warmerdam]] treats
open-source contribution as practical work in
[[cite:open-source-ml-contributions=>Contribute to Open Source ML]].
[[person:mervenoyan=>Merve Noyan]] shows how public
Hugging Face work, model cards, demos, and community contributions create NLP
portfolio evidence in
[[cite:hugging-face-contributions-and-nlp-portfolio=>Hugging Face Contributions and NLP Portfolio]].

AI-for-Good adds a first-experience route when the work has real users, domain
constraints, and a project team. A geospatial AI-for-Good project gave
[[person:isabellabicalho=>Isabella Bicalho]] enough applied experience for her
first freelance client. Open-source ML projects filled the practical
[[machine learning]] gap before paid work arrived
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers@23:39=>From Biology to ML]].
That makes [[open source]] and [[computer vision]] useful portfolio routes for
early contributors when the repository shows data, model choices, and a
concrete result.

Project work becomes job-ready when it resembles a team project for an external
problem. It's weaker when it reads like a solo toy app. A green-space
segmentation project used open satellite imagery and [[computer vision]]. It
compared CNN and transformer benchmarks. The design also tested whether other
cities could replicate the workflow
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers@42:24=>From Biology to ML]].

Collaboration and repeatable implementation create the portfolio signal. A few
hours a week can still support [[job search]] evidence when the work is public
and reviewable.

Kaggle and competitions count when they're repackaged as engineering evidence.
[[person:andradaolteanu=>Andrada Olteanu]] connects
Kaggle work to an analytics-to-data-science transition in
[[cite:analytics-to-data-science-with-kaggle-portfolio=>Analytics to Data Science with Kaggle]].
[[person:tatianagabruseva=>Tatiana Gabruseva]] pushes
competition work beyond leaderboard chasing in
[[cite:s24e01-competitions-beyond-kaggle-leaderboard=>Competitions Beyond the Kaggle Leaderboard]].

[[competitions-beyond-kaggle=>Competitions Beyond Kaggle]] covers portfolio
items that start from a leaderboard or hosted challenge. Decomposition and
reproducible code create the public proof, while README quality and domain
explanation matter too.

## Portfolio Interview Discussion

A portfolio project should be easy to discuss under interview pressure. The
candidate should explain why the project matters and which simpler baseline
came first. They should also explain which parts failed and what they would
change with more time. For data scientist candidates, the
[[data-scientist-interview=>data scientist interview]] path turns that project
story into case practice. It also connects it to SQL, coding, and behavioral
preparation.

The hiring context connects to [[Job Search]]
and the longer arc connects to [[Career Development]].
[[Machine Learning System Design]]
covers projects discussed as system design examples.

## Role-Specific Review Signals

Guests differ on which proof matters most because each role values a different
signal. [[person:jeffkatz=>Jeff Katz]] asks for Python
and SQL. He also asks for clean code, tests, and open-source review pressure
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep]].
[[person:ellenkonig=>Ellen König]]
adds professional software habits and domain-specific pipeline projects
[[cite:from-software-engineering-data-science-to-data-engineering-leadership=>How to Become a Data Engineer]].

[[person:dannyma=>Danny Ma]] frames role fit as Analyst, Builder, and
Consultant profiles. In that model, a portfolio should reveal the candidate's
strongest mode of work. The evidence might come from analysis and storytelling,
production-oriented building, or stakeholder-facing problem shaping
[[cite:data-science-career-abc-framework=>Data Science Career ABC Framework]].

[[person:victoriaperezmola=>Victoria Perez Mola]] and
[[person:juanmanuelperafan=>Juan Manuel Perafan]] connect
reusable models to metric definitions and data quality. They also connect those
models to business reality
[[cite:analytics-engineer-skills-tools=>Master Analytics Engineering]]
[[cite:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices=>Foundations of the Analytics Engineer Role]].

[[person:valeriybabushkin=>Valeriy Babushkin]] asks for
baselines and validation. [[person:benwilson=>Ben Wilson]]
and [[person:nadianahar=>Nadia Nahar]] add production
and software boundaries
[[cite:machine-learning-system-design-interview=>Machine Learning System Design Interview]]
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]]
[[cite:software-engineering-for-machine-learning=>Software Engineering for ML]].

[[person:atitaarora=>Atita Arora]] and
[[person:hugobowneanderson=>Hugo Bowne-Anderson]] focus on
retrieval evidence and citations. They also focus on failure analysis and gold
tests
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
[[person:vincentwarmerdam=>Vincent Warmerdam]]
and [[person:mervenoyan=>Merve Noyan]] focus on public
review, docs, and community-visible work
[[cite:open-source-ml-contributions=>Contribute to Open Source ML]]
[[cite:hugging-face-contributions-and-nlp-portfolio=>Hugging Face Contributions and NLP Portfolio]].

The common thread is reviewability. A project can be small if another person can
understand the decision, run the work, look at the evidence, and challenge the
tradeoffs.

## Related Pages

These pages cover project types and role-specific checklists.

- [[Data Engineering Portfolio Projects]]
- [[Analytics Engineering Portfolio Projects]]
- [[Machine Learning Portfolio Projects]]
- [[RAG Portfolio Projects]]
- [[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]]
- [[Dashboard and Metric Layer Project Checklist]]
- [[Production ML Project Checklist]]
- [[Search and RAG Project Checklist]]
- [[Open Source Portfolio Evidence]]
- [[Job Search]]
