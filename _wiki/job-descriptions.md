---
layout: wiki
title: "Job Descriptions"
summary: "Podcast-backed guidance for reading and writing data job descriptions: role clarity, problem framing, requirements, red flags, and candidate fit."
related:
  - Hiring
  - Job Search
  - Data Science Careers
  - Data Analyst Careers
  - CV Screening
  - Data Teams
---

## Definition and Scope

A job description is the shared role spec between a hiring team and a candidate.
It names the business problem and team context. It also names the level,
responsibilities, required evidence, and interview path. In data work, the
description also separates noisy titles such as
[[data-scientist-role=>Data Scientist]],
[[data-engineer-role=>Data Engineer]], and
[[data-analyst-role=>Data Analyst]] from the actual
work.

DataTalks.Club guests treat the posting as both a hiring artifact and a reading
artifact. [[person:alicjanotowska|Alicja Notowska]]
describes recruiters building the role spec with hiring managers, then using
market reality to adjust requirements [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
[[person:terezaiofciu=>Tereza Iofciu]] gives the
candidate-side diagnostic [[cite:data-science-job-red-flags-and-mismatched-roles|Data Science Jobs]].
When the title and responsibilities disagree with the team context, the company
may not know which data problem it's hiring for.

## Role Clarity

A useful data job description names the team, the business problem, the level,
and the must-have work before it lists tools. Alicja's recruiting episode makes
that practical. Recruiters and hiring managers define what the role needs, then
check whether the market can supply those requirements [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].

Her guidance is to focus the posting on problems over perks [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
That places job descriptions inside
[[Hiring]] and
[[CV Screening]].

Candidates use the same artifact from the other side.
[[person:lukewhipps=>Luke Whipps]] advises candidates to research the company
problem, map their evidence to it, and send fewer targeted applications [[cite:get-data-scientist-job|Land Data Scientist Roles]].
[[person:olegnovikov=>Oleg Novikov]] gives the interview
version [[cite:data-science-interview-and-cv-guide|Data Science Interview Guide]].

The posting helps candidates infer whether a company wants product data science
or machine learning engineering. It can also reveal analytics work or another
role structure [[cite:data-science-interview-and-cv-guide|Data Science Interview Guide]].

## Requirements and Level

Requirements should describe the work before the technology stack. For data
scientists, the posting should distinguish experiments and modeling from product
decision support and deployed ML systems. For analysts, it should separate BI
reporting and product analytics from stakeholder analysis and
[[Analytics Engineering]].

For [[Data Engineering]], it should
name the operating surface, such as pipelines and platform infrastructure. It may
also include data models, governance controls, or production ownership.

Level matters as much as title. [[person:nicolasrassam|Nicolas Rassam]]
discusses junior-to-senior expectations in data engineering [[cite:hiring-for-data-engineering-jobs-in-europe|Hiring Data Engineers in Europe]].
Junior descriptions should leave room for training and mentorship. Senior
descriptions can ask for system ownership, architecture judgment, and cross-team
communication.

He treats titles as noisy while checking for SQL knowledge and Python ability [[cite:hiring-for-data-engineering-jobs-in-europe|Hiring Data Engineers in Europe]].
He also looks for problems, outcomes, projects, and level-appropriate
responsibility.

A posting that asks for junior compensation with senior scope damages both sides
of the market. Candidates reading
[[Job Search]] signals may self-select
out or tailor the wrong evidence. Recruiters applying
[[CV Screening]] criteria may also
reject people against a role that was never clearly defined.

## Candidate Evidence

A strong description tells candidates which evidence matters. Alicja describes
screening experience, education, responsibility clarity, and CV readability [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
Those signals work best when the posting says what the person will actually do.

For experimentation roles, the description should name experiment design and
metrics. It should also name product decision work. For engineering roles, it
should name pipeline work and data quality. It should also state ownership
boundaries and orchestration expectations.

Tools such as SQL and Python can then act as evidence for a concrete job.
Airflow, dbt, cloud platforms, or vector databases can do the same when the
posting explains the work behind them. They shouldn't appear as a loose keyword
list.

Luke's candidate advice points in the same direction. In [[cite:get-data-scientist-job|Land Data Scientist Roles]],
he looks for industry fit and use-case alignment. He also emphasizes concrete
projects and business impact. Oleg adds that candidates should treat the CV like
a landing page [[cite:data-science-interview-and-cv-guide|Data Science Interview Guide]].
The job description gives enough signal to put relevant achievements first and
remove unrelated detail.

## Role-Mismatch Signals

A misleading title can hide a different role, as Tereza explains in [[cite:data-science-job-red-flags-and-mismatched-roles|Data Science Jobs]].
A "data scientist" posting full of ETL, Airflow, and data platform work may be
[[Data Engineering]]. A "data
analyst" posting that owns instrumentation, dbt models, and semantic layers may
be closer to [[Analytics Engineering]].
The same ambiguity appears in broader [[Data Teams]]
questions when the posting omits whether analysts, engineers, ML engineers, and
product stakeholders already exist.

Long technology lists are another warning sign. Tereza discusses overloaded tech
lists and vague responsibilities [[cite:data-science-job-red-flags-and-mismatched-roles|Data Science Jobs]].

Tools matter, but the description should explain why they matter. Airflow often
means batch pipelines. dbt often means analytics engineering. Vector databases
may mean search or retrieval-augmented generation. Without that context, the tool
list becomes keyword noise.

Language can also reveal role design. Alicja discusses inclusive
job-description wording [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
Tereza flags words such as "rockstar" and "ninja" [[cite:data-science-job-red-flags-and-mismatched-roles|Data Science Jobs]].
The issue isn't style alone. Such wording can signal unclear expectations, hero
culture, or a narrow view of who belongs in the role.

## Compensation and Interview Context

Missing salary context and unclear interview steps weaken a description because
they hide basic fit information until recruiter calls. Tereza discusses salary
transparency [[cite:data-science-job-red-flags-and-mismatched-roles|Data Science Jobs]],
while Alicja covers salary bands and negotiation [[cite:hiring-data-scientists-and-analysts|Hiring Data Scientists and Analysts]].
Those discussions place salary ranges, leveling, and role scope inside the same
[[Salary Negotiation]] problem.

Interview structure is also part of the role signal. Oleg describes recruiter
screening, take-home work, and interview rounds, then warns candidates to weigh
take-home time investment [[cite:data-science-interview-and-cv-guide|Data Science Interview Guide]].
Nicolas adds the data-engineering version, where assessments should vary by
level [[cite:hiring-for-data-engineering-jobs-in-europe|Hiring Data Engineers in Europe]].
A good posting tells candidates enough about the interview path to judge whether
the requested work is proportionate to the role.

## Portfolio Fit

Portfolio evidence should answer the job description rather than display
unrelated work. Luke tells candidates to connect projects to concrete use cases
and business impact [[cite:get-data-scientist-job|Land Data Scientist Roles]].
Oleg recommends cold-start projects, synthetic data, and blogging for candidates
without direct industry experience [[cite:data-science-interview-and-cv-guide|Data Science Interview Guide]].

Nicolas gives the data-engineering version [[cite:hiring-for-data-engineering-jobs-in-europe|Hiring Data Engineers in Europe]].
Shareable projects and GitHub work can show pipeline thinking, privacy
awareness, and clear storytelling.

For [[Data Engineering Portfolio Projects]],
strong evidence includes ingestion and orchestration. Tests, data quality checks,
and a runbook make the project easier to evaluate.

For [[Machine Learning Portfolio Projects]],
the evidence should show model framing and evaluation. Deployment, monitoring,
and tradeoffs make the work closer to a real role.

For
[[Analytics Engineering Portfolio Projects]],
the strongest evidence is clean models and metric definitions. Stakeholder-facing
documentation and decision support show how the work would be used.
