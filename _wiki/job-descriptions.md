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
[Data Scientist]({{ '/wiki/data-scientist-role/' | relative_url }}),
[Data Engineer]({{ '/wiki/data-engineer-role/' | relative_url }}), and
[Data Analyst]({{ '/wiki/data-analyst-role/' | relative_url }}) from the actual
work.

DataTalks.Club guests treat the posting as both a hiring artifact and a reading
artifact. [Alicja Notowska](https://datatalks.club/people/alicjanotowska.html)
describes recruiters building the role spec with hiring managers around 7:09 in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html).
She then uses market reality to adjust requirements around 13:57 and 17:18.
[Tereza Iofciu](https://datatalks.club/people/terezaiofciu.html) gives the
candidate-side diagnostic in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html).
When the title and responsibilities disagree with the team context, the company
may not know which data problem it's hiring for.

## Role Clarity

A useful data job description names the team, the business problem, the level,
and the must-have work before it lists tools. Alicja's recruiting episode makes
that practical. Recruiters and hiring managers define what the role needs, then
check whether the market can supply those requirements. She discusses that in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html)
around 7:09, 13:57, and 17:18.

Her guidance around 18:28 is to focus the posting
on problems over perks. That places job descriptions inside
[Hiring]({{ '/wiki/hiring/' | relative_url }}) and
[CV Screening]({{ '/wiki/cv-screening/' | relative_url }}).

Candidates use the same artifact from the other side. In
[Land Data Scientist Roles](https://datatalks.club/podcast/get-data-scientist-job.html),
[Luke Whipps](https://datatalks.club/people/lukewhipps.html) advises candidates
around 37:54 to research the company problem and map their evidence to it.
Around 44:26, he argues for fewer targeted applications.
[Oleg Novikov](https://datatalks.club/people/olegnovikov.html) gives the interview
version in
[Data Science Interview Guide](https://datatalks.club/podcast/data-science-interview-and-cv-guide.html).

Around 15:29 and 17:13, the posting helps candidates infer whether a company
wants product data science or machine learning engineering. It can also reveal
analytics work or another role structure.

## Requirements and Level

Requirements should describe the work before the technology stack. For data
scientists, the posting should distinguish experiments and modeling from product
decision support and deployed ML systems. For analysts, it should separate BI
reporting and product analytics from stakeholder analysis and
[Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).

For [Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}), it should
name the operating surface, such as pipelines and platform infrastructure. It may
also include data models, governance controls, or production ownership.

Level matters as much as title. [Nicolas Rassam](https://datatalks.club/people/nicolasrassam.html)
discusses junior-to-senior expectations around 22:55 in
[Hiring Data Engineers in Europe](https://datatalks.club/podcast/hiring-for-data-engineering-jobs-in-europe.html).
Junior descriptions should leave room for training and mentorship. Senior
descriptions can ask for system ownership, architecture judgment, and cross-team
communication.

Around 18:47 and 31:16, he treats titles as noisy while checking for SQL
knowledge and Python ability.
He also looks for problems, outcomes, projects, and level-appropriate
responsibility.

A posting that asks for junior compensation with senior scope damages both sides
of the market. Candidates reading
[Job Search]({{ '/wiki/job-search/' | relative_url }}) signals may self-select
out or tailor the wrong evidence. Recruiters applying
[CV Screening]({{ '/wiki/cv-screening/' | relative_url }}) criteria may also
reject people against a role that was never clearly defined.

## Candidate Evidence

A strong description tells candidates which evidence matters. Alicja describes
screening experience and education around 21:32 and 27:10 in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html).
She then discusses responsibility clarity and CV readability around 28:41 and
32:40.
Those signals work best when the posting says what the person will actually do.

For experimentation roles, the description should name experiment design and
metrics. It should also name product decision work. For engineering roles, it
should name pipeline work and data quality. It should also state ownership
boundaries and orchestration expectations.

Tools such as SQL and Python can then act as evidence for a concrete job.
Airflow, dbt, cloud platforms, or vector databases can do the same when the
posting explains the work behind them. They shouldn't appear as a loose keyword
list.

Luke's candidate advice points in the same direction. In
[Land Data Scientist Roles](https://datatalks.club/podcast/get-data-scientist-job.html),
he looks for industry fit and use-case alignment around 16:15 and 19:50. Around
25:04, he adds concrete projects and business impact. Oleg adds that candidates
should treat the CV like a landing page around
18:28 in
[Data Science Interview Guide](https://datatalks.club/podcast/data-science-interview-and-cv-guide.html).
The job description gives enough signal to put relevant achievements first and
remove unrelated detail.

## Role-Mismatch Signals

A misleading title can hide a different role. Tereza calls this out around 20:06
and 23:01 in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html).
A "data scientist" posting full of ETL, Airflow, and data platform work may be
[Data Engineering]({{ '/wiki/data-engineering/' | relative_url }}). A "data
analyst" posting that owns instrumentation, dbt models, and semantic layers may
be closer to [Analytics Engineering]({{ '/wiki/analytics-engineering/' | relative_url }}).
The same ambiguity appears in broader [Data Teams]({{ '/wiki/data-teams/' | relative_url }})
questions when the posting omits whether analysts, engineers, ML engineers, and
product stakeholders already exist.

Long technology lists are another warning sign. Tereza discusses overloaded tech
lists and vague responsibilities around 30:20 and 33:33 in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html).

Tools matter, but the description should explain why they matter. Airflow often
means batch pipelines. dbt often means analytics engineering. Vector databases
may mean search or retrieval-augmented generation. Without that context, the tool
list becomes keyword noise.

Language can also reveal role design. Alicja discusses inclusive
job-description wording around 20:04 in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html).
Tereza flags words such as "rockstar" and "ninja" around 31:03 in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html).
The issue isn't style alone. Such wording can signal unclear expectations, hero
culture, or a narrow view of who belongs in the role.

## Compensation and Interview Context

Missing salary context and unclear interview steps weaken a description because
they hide basic fit information until recruiter calls. Tereza discusses salary
transparency around 37:08 in
[Data Science Jobs](https://datatalks.club/podcast/data-science-job-red-flags-and-mismatched-roles.html),
while Alicja covers salary bands and negotiation around 40:33 in
[Hiring Data Scientists and Analysts](https://datatalks.club/podcast/hiring-data-scientists-and-analysts.html).
Those discussions place salary ranges, leveling, and role scope inside the same
[Salary Negotiation]({{ '/wiki/salary-negotiation/' | relative_url }}) problem.

Interview structure is also part of the role signal. Oleg describes recruiter
screening, take-home work, and interview rounds around 13:24 in
[Data Science Interview Guide](https://datatalks.club/podcast/data-science-interview-and-cv-guide.html).
He then warns candidates to weigh take-home time investment around 27:51. Nicolas
adds the data-engineering version around 26:38 in
[Hiring Data Engineers in Europe](https://datatalks.club/podcast/hiring-for-data-engineering-jobs-in-europe.html),
where assessments should vary by level. A good posting tells candidates enough
about the interview path to judge whether the requested work is proportionate to
the role.

## Portfolio Fit

Portfolio evidence should answer the job description rather than display
unrelated work. Luke tells candidates to connect projects to concrete use cases
around 19:50 and business impact around 25:04 in
[Land Data Scientist Roles](https://datatalks.club/podcast/get-data-scientist-job.html).
Oleg recommends cold-start projects, synthetic data, and blogging for candidates
without direct industry experience around 45:46 in
[Data Science Interview Guide](https://datatalks.club/podcast/data-science-interview-and-cv-guide.html).

Nicolas gives the data-engineering version around 54:25 and 55:53 in
[Hiring Data Engineers in Europe](https://datatalks.club/podcast/hiring-for-data-engineering-jobs-in-europe.html).
Shareable projects and GitHub work can show pipeline thinking, privacy
awareness, and clear storytelling.

For [Data Engineering Portfolio Projects]({{ '/wiki/data-engineering-portfolio-projects/' | relative_url }}),
strong evidence includes ingestion and orchestration. Tests, data quality checks,
and a runbook make the project easier to evaluate.

For [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}),
the evidence should show model framing and evaluation. Deployment, monitoring,
and tradeoffs make the work closer to a real role.

For
[Analytics Engineering Portfolio Projects]({{ '/wiki/analytics-engineering-portfolio-projects/' | relative_url }}),
the strongest evidence is clean models and metric definitions. Stakeholder-facing
documentation and decision support show how the work would be used.
