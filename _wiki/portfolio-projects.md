---
layout: wiki
title: "Portfolio Projects"
summary: "Archive-backed guidance for choosing data, analytics, ML, AI, and open-source portfolio projects that prove role fit, practical judgment, public proof, and interview-ready ownership."
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

A portfolio project is public evidence of judgment. In the DataTalks.Club
archive, the useful project isn't a tool demo. It connects a real problem to
data, code, and evaluation. It also shows operation and a defensible interview
story.

Use this page as the hub for project choices. Use
[Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
for pipelines and platform data work. Use
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
for modeled metrics and BI-ready marts. Use
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
for modeling, baselines, evaluation, and production awareness. Use
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
for retrieval-backed LLM systems with citations and evaluation.

[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) and
[Ellen König]({{ '/people/ellenkonig/' | relative_url }}) ground the data
engineering version. In
[Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }})
and
[How to Become a Data Engineer]({{ '/podcasts/from-software-engineering-data-science-to-data-engineering-leadership/' | relative_url }}),
they connect project evidence to fundamentals and clean code. They also connect
it to domain work and reviewable pipelines.

[Victoria Perez Mola]({{ '/people/victoriaperezmola/' | relative_url }}) and
[Juan Manuel Perafan]({{ '/people/juanmanuelperafan/' | relative_url }}) ground
the analytics engineering version. Their episodes connect portfolio evidence to
SQL modeling, data quality, and documentation. They also connect it to business
reality and BI consumption
([Master Analytics Engineering]({{ '/podcasts/analytics-engineer-skills-tools/' | relative_url }})
and
[Foundations of the Analytics Engineer Role]({{ '/podcasts/s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices/' | relative_url }})).

[Valerii Babushkin]({{ '/people/valeriybabushkin/' | relative_url }}),
[Ben Wilson]({{ '/people/benwilson/' | relative_url }}), and
[Nadia Nahar]({{ '/people/nadianahar/' | relative_url }}) ground the machine
learning version. Their discussions move a project beyond a notebook by asking
for baselines, validation, serving boundaries, and tests. They also ask for
monitoring and software integration
([Machine Learning System Design Interview]({{ '/podcasts/machine-learning-system-design-interview/' | relative_url }}),
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
and
[Software Engineering for ML]({{ '/podcasts/software-engineering-for-machine-learning/' | relative_url }})).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) and
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) ground
the RAG version. Their episodes make chunking, retrieval evidence, citations,
and gold tests part of the project. Failure labels and traces aren't optional
polish
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
and
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})).

## Common Definition

Across the archive, a strong portfolio project makes the work reviewable. It
names the consumer or decision. It shows the input data and the transformation
or modeling path. It includes quality checks, evaluation, or both. It also has
a README or writeup that lets another person run, review, or question the work.

The project should answer these review questions:

- What decision or workflow changes if the project works?
- Which data enters the system, and what assumptions come with it?
- Which baseline or simpler version does the project improve on?
- Which checks catch bad data, bad logic, weak retrieval, or model failure?
- How can a reviewer run the project or look at the result?

[Eugene Yan]({{ '/people/eugeneyan/' | relative_url }}) adds the writeup
standard in
[Technical Writing for Data Scientists]({{ '/podcasts/technical-writing-for-data-scientists/' | relative_url }}).
Around 20:18, he describes outlines, section headers, and topic sentences. He
also describes supporting evidence. That structure works for portfolio case
studies because the project has to explain its assumptions and evidence.

## Portfolio Signals Across Roles

Start with reviewable fundamentals instead of tool lists.
[Jeff Katz]({{ '/people/jeffkatz/' | relative_url }}) says portfolios should
show Python, SQL, code structure, and tests. They should also show public or
personal projects in
[Data Engineering Job Prep]({{ '/podcasts/get-data-engineering-job-prep-and-interview/' | relative_url }}).
That advice applies to
[data engineering]({{ '/wiki/data-engineering/' | relative_url }}),
[analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }}),
[machine learning]({{ '/wiki/machine-learning/' | relative_url }}), and
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) portfolios.

Every project needs a consumer, decision, or business question.
[Luke Whipps]({{ '/people/lukewhipps/' | relative_url }}) frames projects as
resume evidence in
[Land Data Scientist Roles]({{ '/podcasts/get-data-scientist-job/' | relative_url }}).
[Nick Singh]({{ '/people/nicksingh/' | relative_url }}) treats project
walkthroughs as interview evidence in
[Ace Data Interviews]({{ '/podcasts/data-interview-behavioral-and-portfolio-prep-guide/' | relative_url }}).
This connects portfolio work to [job search]({{ '/wiki/job-search/' | relative_url }})
and [CV screening]({{ '/wiki/cv-screening/' | relative_url }}).

End-to-end proof beats notebook-only proof. [Santona Tuli]({{ '/people/santonatuli/' | relative_url }})
shows how a pipeline moves from ingestion to transformation, modeled outputs,
and consumers in
[Modern Data Pipeline Architecture]({{ '/podcasts/modern-data-pipelines-orchestration-ingestion-modeling/' | relative_url }}).
[Natalie Kwong]({{ '/people/nataliekwong/' | relative_url }}) adds modern-stack
boundaries in
[ETL vs ELT and the Modern Data Stack]({{ '/podcasts/data-engineering-tools-modern-data-stack/' | relative_url }}).
Those episodes support
[End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
as the concrete data-pipeline blueprint.

## Choosing A Project Type

Choose [data engineering]({{ '/wiki/data-engineering/' | relative_url }}) when
the project should prove ingestion, modeling, orchestration, and recovery. The
best project has a real source behavior, a modeled output, and a rerun path.
Use
[End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
when you need one concrete data-pipeline blueprint.

Choose [analytics engineering]({{ '/wiki/analytics-engineering/' | relative_url }})
when the project should prove business definitions and reusable SQL models. The
best project has source assumptions, table grain, and tests. It also has
documentation and a BI or query surface. Use
[Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
when the project centers on metrics.

Choose [machine learning]({{ '/wiki/machine-learning/' | relative_url }}) when
the project should prove problem framing, baselines, and data strategy. It also
needs evaluation and software boundaries. Use
[Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
when the target role is [MLOps]({{ '/wiki/mlops/' | relative_url }}), ML
platforms, or machine learning engineering.

Choose [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) when
the project should prove retrieval quality and grounded generation. The best
project shows the corpus, chunks, metadata, and retrieved evidence. It also
shows answer citations and failure analysis. Use
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
when the project needs a practical review checklist.

Choose [open source]({{ '/wiki/open-source/' | relative_url }}) when public
collaboration is the strongest evidence. A smaller issue, test, example, or
docs fix can be more credible than a large unfinished app. A reproducible bug
can work too. Use
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
and the
[Open Source Contributor Roadmap]({{ '/roadmaps/open-source-contributor-roadmap/' | relative_url }})
for that path.

## Role-Specific Project Evidence

A project becomes credible when the repository and writeup expose the tradeoffs.
Data projects should show source behavior, table grain, and orchestration. They
should also show quality checks and recovery. Analytics projects should show
metric ownership and a consumption surface.

ML projects should show a baseline, validation, serving boundary, and monitoring
plan. RAG projects should show retrieval examples, citations, and failure
labels.

Don't add tools before the project needs them because the archive repeatedly
warns against tool-first portfolios. [Adrian Brudaru]({{ '/people/adrianbrudaru/' | relative_url }})
ties modern tool choices to requirements in
[Modern Data Engineering Trends]({{ '/podcasts/trends-in-modern-data-engineering/' | relative_url }}).
[Slawomir Tulski]({{ '/people/slawomirtulski/' | relative_url }}) warns against
over-engineered platforms in
[Data Engineer Career in 2026]({{ '/podcasts/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for/' | relative_url }}).

The same rule applies to AI projects. Start with a reliable retrieval or model
baseline before adding agents, long-context tricks, or fine-tuning. Use
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
and
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
when the project needs that decision.

Production awareness is stronger than model novelty. [Ben Wilson]({{ '/people/benwilson/' | relative_url }})
connects maintainable code, tests, and production engineering in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) shows the
notebook-to-production path in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
That's why ML projects should use
[Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
when they claim production readiness.

RAG and AI projects need evidence, not only a chat UI. Strong RAG portfolios
expose corpus choice, chunking, metadata, and retrieval baselines. They also
show citations, logs, and failure analysis. Use
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }}).

## Public Proof And Open Source

Open-source work is portfolio evidence when review pressure is visible. Issues,
docs, tests, and demos can be stronger than a private tutorial repository. Pull
requests, CI, and maintainer discussion strengthen the proof.

[Vincent Warmerdam]({{ '/people/vincentwarmerdam/' | relative_url }}) treats
open-source contribution as practical work in
[Contribute to Open Source ML]({{ '/podcasts/open-source-ml-contributions/' | relative_url }}).
[Merve Noyan]({{ '/people/mervenoyan/' | relative_url }}) shows how public
Hugging Face work, model cards, demos, and community contributions create NLP
portfolio evidence in
[Hugging Face Contributions and NLP Portfolio]({{ '/podcasts/hugging-face-contributions-and-nlp-portfolio/' | relative_url }}).

Kaggle and competitions count when they're repackaged as engineering evidence.
[Andrada Olteanu]({{ '/people/andradaolteanu/' | relative_url }}) connects
Kaggle work to an analytics-to-data-science transition in
[Analytics to Data Science with Kaggle]({{ '/podcasts/analytics-to-data-science-with-kaggle-portfolio/' | relative_url }}).
[Tatiana Gabruseva]({{ '/people/tatianagabruseva/' | relative_url }}) pushes
competition work beyond leaderboard chasing in
[Competitions Beyond the Kaggle Leaderboard]({{ '/podcasts/s24e01-competitions-beyond-kaggle-leaderboard/' | relative_url }}).
Decomposition, reproducible code, README quality, and domain explanation create
the public proof.

## Interview Readiness

A portfolio project should be easy to discuss under interview pressure. The
candidate should explain why the project matters and which simpler baseline
came first. They should also explain which parts failed and what they would
change with more time.

Use [Job Search]({{ '/wiki/job-search/' | relative_url }}) for the hiring
context and [Career Development]({{ '/wiki/career-development/' | relative_url }})
for the longer arc. Use
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
when the project will be discussed as a system design example.

## Guest Differences

Guests differ on which proof matters most because each role values a different
signal. Jeff Katz asks for fundamentals, and Ellen König adds professional
habits. Victoria and Juan connect reusable models to metric definitions and
business reality. Valerii asks for baselines and validation, while Ben and
Nadia add software boundaries.

Atita and Hugo focus on retrieval evidence, citations, and failure analysis.
Vincent and Merve focus on public review, docs, and community-visible work.

The common thread is reviewability. A project can be small if another person can
understand the decision, run the work, look at the evidence, and challenge the
tradeoffs.

## Related Pages

Use these pages to choose the right project type and checklist.

- [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }})
- [Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }})
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [End-to-End Data Pipeline Project]({{ '/wiki/end-to-end-data-pipeline-project/' | relative_url }})
- [Dashboard and Metric Layer Project Checklist]({{ '/wiki/dashboard-and-metric-layer-project-checklist/' | relative_url }})
- [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
- [Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
- [Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }})
- [Job Search]({{ '/wiki/job-search/' | relative_url }})
