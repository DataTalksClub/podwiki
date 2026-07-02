---
layout: wiki
tags: ["transition"]
title: "QA to ML and Data Engineering"
summary: "Transition notes for QA engineers moving into machine learning or data engineering through testing discipline, projects, cloud practice, public notes, and interview framing."
related:
  - Career Transitions in Data
  - Testing
  - Machine Learning
  - Machine Learning Engineer Role
  - Data Engineering
  - Data Engineer Role
  - Portfolio Projects
  - Production ML Project Checklist
  - End-to-End Data Pipeline Project
  - Job Search
---

QA to ML and data engineering is the transition from testing work into
model-backed systems, data pipelines, or adjacent data-quality roles. The direct
DataTalks.Club example is
[[person:alvaronavaspeire|Alvaro Navas Peire]]. He
moved from Android-phone QA and field testing into machine-learning study,
data-engineering coursework, and ML/NLP project work
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's Android QA starting point at 1:15-3:56]]).

The transition is strongest when QA experience becomes evidence, so it
shouldn't read as a title substitution. Alvaro's route combines structured
learning and role-shaped projects with cloud practice and public notes. His
interview framing connects testing discipline to the target role
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's structured learning, projects, and interview prep at 13:32-45:28]]).
That places the page inside
[[career-transitions-in-data|Career Transition]],
[[Career Transitions in Data]],
[[Testing]], and
[[Job Search]].

Choose the target role before choosing a project. QA-to-ML should route toward
[[Machine Learning]],
[[Machine Learning Engineer Role]],
the
[[Machine Learning Engineer Roadmap]],
and the
[[Production ML Project Checklist]].
QA-to-data-engineering should route toward
[[Data Engineering]],
[[Data Engineer Role]],
the [[Data Engineer Roadmap]],
and
[[end-to-end-data-pipeline-project|End-to-End Data Pipeline Project]].
Alvaro separates math-heavy ML from tooling-focused data engineering near the
end of his interview
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's target-role discussion at 47:39-59:51]]).

## Proof-Building Transition

QA-to-ML or QA-to-data-engineering work is credible when the candidate keeps
testing experience visible and proves the new role with concrete work. The
target-role evidence belongs in
[[Machine Learning Engineer Role]],
[[Data Engineer Role]],
[[Data Roles]], and
[[Portfolio Projects]].

Alvaro's QA work wasn't a vague "attention to detail" claim. He describes
phone-prototype testing, GPS field testing, and RF field testing. He also
describes Android certification checks, repeated firmware validation,
checklists, and written reports
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's Android QA work at 2:13-7:14]]).
Those examples let a QA candidate talk about acceptance criteria, edge cases,
and repeatability. They also let the candidate discuss failure reports and
communication as working habits rather than personality traits.

Alvaro then explored new roles and chose structured retraining. He first
explored front-end work and chose ML because he liked the mathematical
challenge. He used a postgraduate course and Neuromatch Academy to build
project experience. Machine Learning Zoomcamp and Data Engineering Zoomcamp
served the same purpose
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's retraining path at 8:35-17:28]]).

His work included an EDA project and a vegetable image-classification project.
He also practiced Google Cloud deployment, AWS exercises, and public GitHub
notes
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's projects and public notes at 24:57-28:42 and 35:02-42:55]]).

Hiring translation mattered because Alvaro's coaching covered hiring-manager
conversations and behavioral questions. The same coaching helped with
communication and negotiation. Technical preparation still belonged to Alvaro
when the target role involved NLP
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's interview-coaching discussion at 43:33-51:20]]).
For a QA transitioner, the bridge is credible when the CV and interviews connect
old validation work to new role evidence. The career change shouldn't read as
a title swap.

## Choosing the Target Role

The first decision is role direction. Alvaro separates math-heavy data science
or research-oriented ML from tooling-focused data engineering. Mathematical
background helps for high-level model experimentation. Data engineering depends
more on Spark, Kafka, Docker, and Kubernetes on top of programming foundations
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's target-role distinction at 47:39-59:51]]).

[[person:svpino|Santiago Valdarrama]] uses coding and
shipped projects to set the software-to-ML boundary.
[[podcast:from-software-engineer-to-machine-learning|From Software Engineering to Machine Learning]]
treats coding as a core ML skill. Santiago recommends building projects before
overpreparing on theory. His ML engineering path includes Python, Pandas, and
scikit-learn. It also includes deployment, Docker, APIs, and cloud providers
([[podcast:from-software-engineer-to-machine-learning|Santiago's project-first ML path at 17:25-29:05 and 33:10-51:21]]).

This ML route fits QA engineers who already have strong programming or test
automation experience. Relevant pages are
[[Software Engineer to Machine Learning]]
and
[[Machine Learning for Software Engineers]].

[[person:jeffkatz|Jeff Katz]] defines the
data-engineering route around fundamentals first. In
[[podcast:data-engineering-career-path-and-skills|Build a Data Engineering Career]],
he emphasizes Python and SQL. He also emphasizes cloud fundamentals, backend
engineering, ETL, and codebase navigation. He explains why junior curricula
shouldn't over-prioritize Spark, Kafka, and Kubernetes before the fundamentals
are strong
([[podcast:data-engineering-career-path-and-skills|Jeff's data-engineering fundamentals at 23:35-38:05]]).

In
[[podcast:get-data-engineering-job-prep-and-interview|Data Engineering Job Prep and Interview Guide]],
Jeff adds Python/SQL depth and warehouse fundamentals. He also adds Docker and
Airflow. Clean code, tests, portfolio projects, and technical interview formats
matter too.
This version of the transition points toward the
[[data-engineer-roadmap|Data Engineering Roadmap]]
and [[Data Engineer Roadmap]]
rather than model research
([[podcast:get-data-engineering-job-prep-and-interview|Jeff's data-engineering job-prep scope at 1:20-9:41]]).

[[person:juanmanuelperafan|Juan Manuel Perafan]] makes
testing part of the data-role boundary. In
[[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Foundations of the Analytics Engineer Role]],
he separates testing data from testing code. He shows how a manual dashboard
checklist can become dbt generic tests, singular tests, unit tests, and CI
checks
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Juan Manuel's analytics-testing discussion at 38:41-46:34]]).
His example makes
[[Data Quality and Observability]]
and [[Analytics Engineering]]
natural adjacent paths for QA people who want to stay close to validation.

[[person:benwilson|Ben Wilson]] gives the production-ML
version of the boundary. In
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]],
he frames ML work as iterative, executable, maintainable code.
His example includes feature engineering and placeholder models. It also
includes unit tests and integration tests from ingest to prediction. Monitoring
and A/B testing complete the example, along with deployment and CI/CD
([[podcast:machine-learning-engineering-production-best-practices|Ben's production-ML testing example at 52:14-59:27]]).

Wilson's version fits QA engineers aiming at
[[Machine Learning Engineer Role]]
or production data and ML operations rather than notebook-only data science.

## Transferable QA Evidence

The strongest transferable QA evidence is concrete test work, not "attention
to detail" as a personality claim. Alvaro names checklists, repeated
validation, field routes, and written reports
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's QA validation routines at 3:56-8:18]]).

For ML work, the QA habit should become evaluation and failure analysis.
[[person:svpino|Santiago Valdarrama]] presents ML as
building working systems, not only studying algorithms.
[[person:benwilson|Ben Wilson]] emphasizes
unit-tested feature engineering plus integration tests from ingest to
prediction
([[podcast:from-software-engineer-to-machine-learning|Santiago's deployed-project guidance at 33:10-51:21]],
[[podcast:machine-learning-engineering-production-best-practices|Ben's ingest-to-prediction test example at 52:14-59:27]]).

Alvaro's image-classification project and cloud deployment are useful because
they're concrete evidence. The interview story becomes stronger when the
candidate can explain the dataset, task, tools, and result without underselling
the project. The
[[Machine Learning Portfolio Projects]]
page collects the adjacent portfolio examples
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's image-classification project discussion at 24:57-30:56]]).

For data engineering work, the QA habit should become pipeline reliability.
Katz's data-engineering job-prep episode names Python, SQL, Docker, and
Airflow. Warehouses, clean code, tests, and portfolio projects are hiring
signals too
([[podcast:get-data-engineering-job-prep-and-interview|Jeff's data-engineering hiring signals at 1:20-9:41]]).

The
[[Data Engineering Portfolio Projects]]
page is the related project-design reference for ingestion and source handling.
It also covers modeling, reliability checks, deployment, and maintainability.

For analytics and data-quality work, QA experience maps most directly to
automated checks. Perafan's dashboard example starts with a growing manual
checklist. It moves toward dbt generic tests, singular tests, unit tests, and
CI checks
([[podcast:s23e02-foundations-of-analytics-engineer-role-skills-scope-and-modern-practices|Juan Manuel's dbt testing example at 38:41-46:34]]).
That makes
[[Data Quality and Observability]]
a natural adjacent topic for QA transitioners.

## Skill Gaps by Target Role

The ML route needs enough Python and data work to discuss a project as a
system. It also needs modeling, evaluation, and deployment practice.
Valdarrama's route starts from projects. It then adds Python and Pandas.
Scikit-learn, problem analysis, deployment, and cloud work round out the route
([[podcast:from-software-engineer-to-machine-learning|Santiago's ML skill sequence at 17:25-29:05 and 33:10-51:21]]).

Alvaro's route adds postgraduate ML study and Zoomcamp work. It also includes a
deployed image-classification project
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's ML study and deployment practice at 13:32-17:28 and 24:57-28:42]]).

The data-engineering route needs Python, SQL, cloud fundamentals, and ETL work.
It also needs testing and interview drills. Katz's career-path episode includes
Python, SQL, cloud, and dbt. It also includes backend and codebase practice.
Katz warns against over-prioritizing Spark and Kafka for junior curricula before
fundamentals are strong
([[podcast:data-engineering-career-path-and-skills|Jeff's junior data-engineering curriculum discussion at 23:35-38:05]]).

This data-engineering route belongs with
[[Data Engineering]] and
[[Data Engineer Roadmap]].

The production-ML route needs testing and operations beyond a notebook. Wilson
describes ML work as iterative and executable. His example includes feature
engineering and placeholder models. It also includes unit tests and integration
tests from ingest to prediction. Monitoring, A/B testing, deployments, and
CI/CD are part of the same production frame
([[podcast:machine-learning-engineering-production-best-practices|Ben's production-ML workflow at 52:14-59:27]]).

A QA engineer can use that as a bridge into
[[MLOps]] or
[[DataOps]] work when their portfolio
proves system ownership rather than only model training. The
[[MLOps vs DataOps]]
comparison helps separate those two paths.

## Portfolio and Public Notes

Alvaro shows portfolio evidence through an EDA project and an
image-classification project. He also practiced Google Cloud deployment and AWS
exercises during the course
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's Zoomcamp project examples at 24:57-28:42]]).

His notes show learning evidence through Markdown notes and GitHub gists. He
also used screenshots, indexes, and outside links. Writing helped him remember
and explain the material
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's public-notes workflow at 35:02-42:55]]).

For QA-to-ML candidates, a useful portfolio project should show the model and
the checks around it. The project should explain the dataset and target. It
should name the baseline and evaluation metric. It should also cover error
cases, deployment path, and failure modes
([[podcast:machine-learning-engineering-production-best-practices|Ben's production-ML testing example at 52:14-59:27]],
[[Machine Learning Portfolio Projects]]).

Use [[Portfolio Projects]] for
the cross-role standard and
[[Production ML Project Checklist]]
for reproducible training, deployment, monitoring, and rollback criteria. The
[[Machine Learning Engineer Roadmap]]
turns the same evidence into a learning sequence. QA discipline becomes a
visible ML asset when the project explains what can fail and how the candidate
checked it.

For QA-to-data-engineering candidates, a useful portfolio project should show
ingestion and transformation. It should also show SQL depth, data quality
tests, and orchestration. Recovery behavior belongs in the project too
([[Data Engineering Portfolio Projects]],
[[podcast:get-data-engineering-job-prep-and-interview|Jeff's data-engineering job-prep scope at 1:20-9:41]]).

[[person:santonatuli|Santona Tuli]] and
[[person:nataliekwong|Natalie Kwong]] show the pipeline
version through ingestion and transformation. They also cover marts,
orchestration, and consumer-facing outputs
([[podcast:modern-data-pipelines-orchestration-ingestion-modeling|Santona pipeline structure at 37:10-43:05]],
[[podcast:data-engineering-tools-modern-data-stack|Natalie modern stack details at 15:30-30:59]]).
Use
[[end-to-end-data-pipeline-project|End-to-End Data Pipeline Project]]
when the transition project needs one concrete data-engineering blueprint.
A QA background strengthens the story when the README explains what can break,
which tests catch it, and how to rerun the pipeline.

## Interview and CV Framing

A specific interview lesson for QA transitioners is to describe projects
objectively. Alvaro says he tended to undersell his projects. The host points
out that a better answer states the dataset, problem, tools, and task. The
interviewer can then evaluate the work
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's project-framing lesson at 28:52-30:56]]).
That advice is especially relevant for QA transitioners because they may
compare themselves unfavorably with candidates who already held ML or data
titles.

Alvaro's interview preparation had technical and behavioral sides. His coach
helped with hiring-manager framing and behavioral questions, plus communication
and negotiation. Alvaro still handled the technical model questions
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's coach and behavioral-prep discussion at 43:33-47:29]]).

Katz's data-engineering job-prep episode adds the role-specific hiring format.
It covers SQL and Python, plus take-home projects, resumes, and interview
stages
([[podcast:get-data-engineering-job-prep-and-interview|Jeff's data-engineering interview overview at 1:20-9:41]]).

The CV should make the bridge obvious. Alvaro's episode includes CV and
portfolio tips near the end
([[podcast:how-to-transition-into-ml-and-data-engineering-from-qa|Alvaro's CV and portfolio tips at 1:00:26-1:02:11]]).

[[person:alvaronavaspeire|Alvaro Navas Peire]] gives
the episode context for Android QA and ML/data-engineering courses. The
candidate should present QA work as evidence of validation and communication.
They can then present ML or data engineering projects as evidence of the target
role. Use [[Job Search]] for hiring
context and [[Data Roles]] for role
selection.
