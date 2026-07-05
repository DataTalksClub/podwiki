---
layout: article
tags: ["roadmap"]
title: "Data Engineer Roadmap"
keyword: "data engineer roadmap"
summary: "A practical data engineer roadmap from SQL and Python fundamentals to pipelines, orchestration, DataOps, reviewable work, and interviews."
related_wiki:
 - Modern Data Engineering Trends
 - Data Engineer Role
 - How to Become a Data Engineer With No Experience
 - Data Engineering Portfolio Projects
 - Data Engineering Certification
 - Data Engineering
 - Data Pipelines
 - Data Quality and Observability
 - DataOps
 - Modern Data Stack
 - Job Search
 - Career Transitions in Data
 - FinOps for Data Engineers
 - Data Analyst to Data Engineer
 - Data Scientist to Data Engineer
 - QA to ML and Data Engineering
 - DevOps to Data Engineering
 - Hire Data Engineers
 - Teaching
---

A useful data engineer roadmap starts with the work a data engineer owns. Data
engineers move source data into trusted datasets that other people can use. Use
this roadmap to learn the sequence.

Start with SQL and Python, then learn ingestion, storage, and modeling. After
that, add orchestration and quality before documentation, cloud basics, and
interview-ready projects.

Use this roadmap when you want to decide what to learn next and how the pieces
fit together. The same sequence can support analytics and software backgrounds.
It also supports operations, QA, or a first technical role.

If you need to turn an existing background into hiring evidence, use the
relevant transition page after this sequence:

- [[data-analyst-to-data-engineer=>Data Analyst to Data Engineer]] for analysts
- [[data-scientist-to-data-engineer=>Data Scientist to Data Engineer]] for data
  scientists
- [[QA to ML and Data Engineering]] for QA backgrounds
- [[DevOps to Data Engineering]] for DevOps, SRE, and platform backgrounds
  moving toward data-platform automation
  [[cite:from-devops-to-data-engineering-automation-open-source-volunteering=>From DevOps to Data Engineering]]
- [[how-to-become-a-data-engineer-with-no-experience=>becoming a data engineer with no experience]]
  when you need first-role evidence

The guidance is consistent across two episodes. [[person:jeffkatz=>Jeff Katz]]
names the junior core as Python and SQL, plus cloud fundamentals and
orchestration. He frames the beginner path as mostly Python and SQL. Tools get
a smaller share. Junior training can postpone Spark, Kafka, and Kubernetes
([[cite:data-engineering-career-path-and-skills@38:05=>Build a Data Engineering Career]],
[[cite:data-engineering-career-path-and-skills@56:46=>Build a Data Engineering Career]]).

Brudaru puts SQL/Python before vendor checklists. [[modern-data-engineering-trends=>Modern Data Engineering Trends]]
connects that roadmap advice to current tool caution
([[cite:trends-in-modern-data-engineering=>DE]]).

His beginner path adds one detail that tool lists often miss. Learners need to
capture business requirements. The learning sequence should therefore put the
early project around a real consumer problem before it adds more tools
([[cite:trends-in-modern-data-engineering@41:06=>Modern Data Engineering Trends]]).
That project requirement applies to every learner. Analysts who already have
consumer and metric context should use
[[data-analyst-to-data-engineer=>Data Analyst to Data Engineer]] to translate
that context into transition evidence.

[[person:rahuljain=>Rahul Jain]] gives the hiring-side rule: candidates still
need DBMS and SQL fundamentals. Data platforms change structure, but the
reasoning stays useful
([[cite:data-engineering-leadership-and-modern-data-platforms=>DE Leadership]]).
The manager-side expectations behind that filter live in the
[[data-engineering-manager-role=>data engineering manager]]
role.

This roadmap gives the practical learning sequence. For the role scope, start
with [[Data Engineer Role]] and [[Data Engineering]]. For credential choices,
use [[Data Engineering Certification]].

## Start With The Role

Before choosing tools, decide which slice of data engineering you're trying to
prove.

A junior roadmap should show four abilities:

- ingest data and preserve raw records
- transform and model data with SQL
- run the workflow repeatedly
- explain how consumers can trust the output

That role boundary matters because "data engineer" can mean different things.
[[person:slawomirtulski=>Slawomir Tulski]] separates platform data engineering
from product-facing data work. He also describes a tougher market for junior
roles. He recommends reusing existing domain experience rather than applying
blindly to every data title
([[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]]).

That role split gives the roadmap a practical target. It also lets the same
skill order support different starting points. For background-specific framing,
use the transition pages above. The QA route shows how checks and reports can
turn into reviewable data-engineering proof
([[cite:how-to-transition-into-ml-and-data-engineering-from-qa=>QA to ML and Data Engineering]]).
[[Career Transitions in Data]] and [[Job Search]] connect the roadmap to
applications.

## Stage 1: SQL, Python, And Modeling

Start with SQL, Python, and basic data modeling. These skills make you useful
before you own a warehouse, lakehouse, streaming system, or platform.

For SQL, practice:

- joins and aggregations
- common table expressions
- window functions
- table grain and primary keys
- slowly changing attributes
- validation queries

SQL depth should go beyond joins and aggregates. Add window functions, with
medium SQL interview problems as a practical benchmark
([[cite:data-engineering-career-path-and-skills@44:21=>Build a Data Engineering Career]]).
Data modeling practice such as OLTP versus OLAP matters too. Use
[[Data Warehouse]] to connect that interview topic to analytical modeling work
([[cite:data-engineering-career-path-and-skills@45:14=>Build a Data Engineering Career]]).

Rahul Jain recommends learning databases and SQL first, then learning how data
moves. Treat ETL/ELT choices, lake designs, lineage, and governance tools as
follow-up details
([[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]).

For Python, practice:

- reading files and calling APIs
- handling pagination and configuration
- retrying failed requests
- isolating bad records
- writing data into storage

[[software-engineering=>Software foundations]] matter before advanced platform
tools, so start with programming fundamentals. Small data projects then make
data movement, ETL, and pipeline choices concrete
([[cite:remote-data-engineering-work-and-building-iot-platforms@48:36=>Remote Data Engineering]],
[[cite:remote-data-engineering-work-and-building-iot-platforms@50:25=>Small data projects]]).

Readable code matters because many projects list tools while showing too little
Python and SQL. Aim for small functions, useful names, targeted classes, and
tests
([[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]).

The modeling layer turns data movement into data engineering. Name the grain of
each table, separate raw and modeled layers, and write a data dictionary for
final tables. For deeper context, use
[[Data Pipelines]],
[[Data Warehouse]], and
[[Analytics Engineering]].

## Stage 2: Build One End-To-End Batch Pipeline

After the fundamentals, build one small pipeline that moves data from a source
to a trusted output. This is the center of the data engineer roadmap because it
turns study into evidence.

The first pipeline should include:

- a source such as an API, file drop, database export, public dataset, event log,
  or simulated change-data feed
- raw storage that keeps source records before transformation
- staging tables that clean types, rename fields, deduplicate records, and keep
  load metadata
- modeled tables with joins, grain, business rules, aggregations, and windows
- a serving output for a named consumer such as a BI report, ML training job,
  product workflow, or operational alert
- a command, script, scheduler, or simple orchestrator so the pipeline doesn't
  depend on notebook clicks
- documentation for setup, tables, quality checks, failure modes, and recovery

This project should show substantial SQL and Python, not only a stack diagram.
[[person:santonatuli=>Santona Tuli]] describes an
end-to-end pipeline that moves from ingestion and orchestration into modeled
marts and dashboards in
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]].
That episode also covers production ML handoffs and shows how source modeling,
declarative transformations, and serving layers connect in one pipeline story.

Portfolio work later turns this stage into hiring evidence, but this stage has
a narrower goal. One pipeline should connect Python and SQL with orchestration.
It should also include warehouse fundamentals and either Docker or a simple run command
([[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]).
Use
[[Data Engineering Portfolio Projects]]
as the review standard, and use
[[end-to-end-data-pipeline-project=>End-to-End Data Pipeline Project]]
for a single-project blueprint.

## Stage 3: Choose Storage, ETL, And ELT Deliberately

Once the first pipeline runs, learn where data should land and why. Start with
storage and transformation patterns before memorizing product names.

[[person:nataliekwong=>Natalie Kwong]] gives the clearest introduction in
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]],
covering ETL and ELT's flexibility. She also covers transformations from type
casting to SQL joins and the distinction between data marts, warehouses, and raw
ingestion layers. She frames lake versus warehouse as an architecture choice.

Your project doesn't need a full platform, but it should explain its storage
choice:

- what stays raw and what gets transformed
- whether the final output lives in a warehouse, lake, lakehouse, local
  analytical database, or object store
- who queries the final data
- how you rerun or backfill if the source changes
- what would become expensive, slow, or hard to maintain at larger scale

For deeper reading, connect this stage to
[[ETL vs ELT]] and
[[ELT]]. Then add
[[Data Lake]],
[[data-warehouse-vs-data-lakehouse=>Data Warehouse vs Lakehouse]],
and [[Modern Data Stack]].

## Stage 4: Add Orchestration, Quality, And DataOps

A data engineer roadmap is incomplete without repeatable operations. A pipeline
has to run in the right order, rerun safely, and tell you when the data is
wrong.

For orchestration, learn:

- schedules and dependencies
- retries and failure states
- backfills and reruns
- logs and alerts
- idempotent writes
- parameters and configuration

Airflow's orchestration role appears in
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
In
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]],
[[person:larsalbertsson=>Lars Albertsson]] goes deeper. He breaks a data
platform into storage, compute, and workflow engine. He treats data quality
measurements and schema automation as part of DataOps maturity.

Follow DataTalks.Club's
[lightweight local Airflow with Docker Compose tutorial](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html)
when you need a local Airflow project a reviewer can start and rerun. They can
also break it and look at the results.

For quality checks, protect the consumer:

- freshness: the latest batch arrived when expected
- volume: row counts stay within a reasonable range
- schema: required columns and types are present
- uniqueness: keys don't duplicate unexpectedly
- nulls: required fields are populated
- accepted values: categorical fields stay within expected values
- referential integrity: facts join to dimensions as expected
- distribution: important measures don't shift without explanation

[[person:christopherbergh=>Christopher Bergh]] adds the operational standard in
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].
He ties DataOps to error reduction, deployment cycle time, and team
productivity.
Use [[how-to-build-data-pipelines=>how to build data pipelines]] for the
step-by-step version of this reliability sequence.

He names practical reliability tools:

- version control
- automated tests
- CI/CD
- dbt tests
- Great Expectations
- SQL tests

[[Data Quality and Observability]],
[[DataOps]], and
[[data-quality-and-observability=>Data Observability]] cover the deeper version.

## Stage 5: Turn Learning Into A Reviewable Project

By this point, you should have one complete pipeline and one smaller exercise
that proves a specific skill. Stop adding tools until another engineer can run
the work. They should be able to read the SQL and Python, run the tests, and
ask why each tradeoff fits the consumer.

Jeff Katz's
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]
asks for readable code, visible SQL and Python depth, and tests. Slawomir
Tulski's
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]]
pushes outcome framing and a small end-to-end platform, even when the
implementation is simple. [[person:mehdiouazza=>Mehdi OUAZZA]] recommends
writing and open-source work in
[[cite:scaling-data-engineering-teams-self-service-platforms=>Scale Data Engineering Teams]],
because public explanations can create feedback and make work visible.

At this stage, check reviewability before choosing more projects. The roadmap
only tells you when to package the work. Use
[[Data Engineering Portfolio Projects]] for project selection, repository
structure, and reviewer signals.

If your main problem is missing commercial experience, use
[[how-to-become-a-data-engineer-with-no-experience=>the no-experience guide]]
for outside review and volunteer work. Use
[[data-analyst-to-data-engineer=>Data Analyst to Data Engineer]] when the
project must explain how reporting, metric, or stakeholder work transfers.
[[volunteer-data-engineering-projects=>Volunteer data engineering projects]]
cover the nonprofit or open-source version. For documentation and screening
context, use [[Documentation]] and [[CV Screening]].

## Stage 6: Prepare For Interviews While You Build

Interview preparation should follow the same roadmap. Don't study interviews
as a separate universe from your projects. Your projects should give you
examples for most interview questions.

Prepare for these areas:

- SQL screens: joins, windows, aggregations, deduplication, ranking, date logic,
  and validation queries
- Python screens: file parsing, API calls, data structures, small functions,
  error handling, and tests
- pipeline design: source, raw storage, transformation, orchestration, quality,
  serving, and recovery
- data modeling: table grain, fact and dimension thinking, slowly changing
  attributes, marts, and warehouse concepts
- failure scenarios: late data, duplicate records, schema changes, partial
  loads, broken dependencies, and bad joins
- cloud and tooling: storage, permissions, schedulers, Docker, warehouses, and
  cost awareness
- project walkthroughs: tradeoffs, bugs, rejected designs, and future
  improvements

Technical interviews include SQL, Python, and take-home work
([[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]).
They also include screening calls, SQL tests, and on-site expectations
([[cite:data-engineering-career-path-and-skills@48:00=>Build a Data Engineering Career]]).
Jain advises managers to ask follow-up questions that separate real platform
understanding from tool-name fluency
([[cite:data-engineering-leadership-and-modern-data-platforms=>Data Engineering Leadership]]).
Managers can use [[hire-data-engineers=>hiring data engineers]] when they turn
that roadmap into an employer-side screen.

End the roadmap with practice under constraints. Explain your pipeline out loud
and redesign one part on a whiteboard. Solve SQL without searching for every
syntax detail, then write a small extractor or validation function from
scratch.

## Stage 7: Add Advanced Tools Only When They Solve A Constraint

Add advanced tools when the project or target role needs them.

Add advanced tools only when the constraint is real:

- Add Spark for distributed processing, large-data transformations, or
  Spark-specific job experience.
- Add Kafka when delayed answers lose value and event ordering, replay, or late
  events become central, using
  [[Batch vs Streaming]]
  to decide whether the latency need justifies streaming.
- Add Kubernetes when deployment and platform ownership are part of the role.
- Add Iceberg, [[delta-lake=>Delta Lake]], or a catalog when lakehouse metadata
  and schema evolution become the problem.
- Add catalog and lineage tooling when discovery, ownership, and governance
  become the problem.

Tool-first roadmaps draw repeated warnings. Adrian Brudaru's
[[cite:trends-in-modern-data-engineering=>Modern Data Engineering]]
covers Iceberg and DuckDB, plus orchestration and streaming patterns. He keeps
returning to requirements and vendor caution.
Use [[modern-data-engineering-trends=>modern data engineering trends]] at this
stage as a filter for advanced tools. Add them for storage or latency problems,
metadata work, AI readiness, or cost control.

Jeff Katz gives the junior-curriculum version of the same warning. Spark,
Kafka, and Kubernetes appeared more often in senior job descriptions than in
junior interviews. His program kept more time on Python and SQL
([[cite:data-engineering-career-path-and-skills@38:05=>Build a Data Engineering Career]],
[[cite:data-engineering-career-path-and-skills@40:04=>Build a Data Engineering Career]]).

Slawomir Tulski makes the same point in
[[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]],
warning about over-engineered platforms and placing Kafka where real-time needs
justify it.

The practical sequence is:

1. Build the batch version.
2. Add tests and documentation.
3. Identify the bottleneck or requirement.
4. Add the advanced tool that addresses it.
5. Explain what became easier and what became harder.

This keeps the roadmap connected to
[[Data Engineering Tools]],
[[Data Engineering Platforms]],
[[self-service-data-platforms=>Self-Service Data Platforms]],
and [[Platform Engineering]].

## Use Courses As Roadmap Structure

Courses, bootcamps, and company training can give the roadmap deadlines and
feedback. They also help when they include labs and a project another engineer
can run.

They work best when they keep fundamentals and operations in the same learning
path:

- SQL
- Python
- data modeling
- ingestion
- orchestration
- testing

They work poorly when they replace the roadmap with a tool list or a credential
line.

[[person:gloriaquiceno=>Gloria Quiceno]] shows the learner side in
[[cite:get-data-analytics-and-data-engineering-job=>Get a Data Analytics and Data Engineering Job]].
Her path included a bootcamp, volunteer practice, tracked applications, and a
custom Twitter data pipeline capstone with Docker containers and a Slack bot.
Jeff Katz adds that cloud certificates may help with recruiter filters. Hiring
managers still check whether the candidate knows the topics and can code
[[cite:get-data-engineering-job-prep-and-interview@37:49=>Data Engineering Job Prep and Interview Guide]].

[[Data Engineering Certification]] compares course, bootcamp, cloud, and vendor
credentials. The same project rule applies to course catalogs such as
[Data Engineering Zoomcamp](https://datatalks.club/blog/data-engineering-zoomcamp.html),
which the DataTalks.Club podcast frames as free project-based learning
([[cite:datatalksclub-scaling-and-free-courses=>Inside Scaling DataTalks.Club]]).
Finish with a pipeline you can explain, not only a completed syllabus.

## Entry, Mid-Level, and Senior Signals

Entry-level readiness means you can write SQL and Python. You can explain table
grain, model basic entities, and run one orchestrated job with tests. Jeff
Katz's two episodes map this level to coding, orchestration, and interviews
([[cite:data-engineering-career-path-and-skills=>Build a Data Engineering Career]],
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]).

Mid-level readiness means you can own a production pipeline. You can talk with
downstream users about freshness and quality, handle backfills, and review
transformation code. Natalie Kwong covers stack tradeoffs and Santona Tuli
covers pipeline architecture at this level
([[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]],
[[cite:modern-data-pipelines-orchestration-ingestion-modeling=>Modern Data Pipeline Architecture]]).

Senior readiness means you can set platform conventions and define ownership
boundaries. You can decide whether governance or self-service work is worth the
operational burden. Slawomir Tulski links senior value to cost-aware
engineering and outcome framing
([[cite:s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for=>Data Engineer Career in 2026]]).

Adrian Brudaru adds that senior backend engineers can move into senior data
engineering when they bring engineering judgment and learn the business case.
They still need requirements, ingestion, and modeling practice. Highly
specialized paths such as deep Spark expertise take separate practice
([[cite:trends-in-modern-data-engineering@45:56=>Modern Data Engineering Trends]]).
At that level,
[[FinOps for Data Engineers]]
begins to matter because cloud spend becomes a shared responsibility.
The same senior filter connects cost awareness back to
[[modern-data-engineering-trends=>modern data engineering trends]] rather than
to tool collection.

## A Practical 12-Week Roadmap

Use this as a pacing guide, not a promise. Move faster if you already know SQL,
Python, or backend engineering, and move slower if you're learning programming
from scratch. The sequence follows the podcast evidence above. Fundamentals
come before tool breadth, one finished pipeline comes before specialization,
and reviewable proof comes before tool collecting.

Weeks 1-2 cover SQL and modeling through joins, windows, aggregations, and
CTEs. Then add table grain, OLTP versus OLAP, and validation queries. Jeff
Katz's SQL and modeling advice in
[[cite:data-engineering-career-path-and-skills@44:21=>Build a Data Engineering Career]]
is the benchmark for this stage.

Weeks 3-4 cover Python ingestion through scripts that call an API or read files.
Handle bad records, configuration, retries, and raw data preservation. Use
Jeff's code-quality guidance from
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]]
as the review bar.

Weeks 5-6 cover storage in a warehouse, lake, or local analytical database.
Create raw, staging, modeled, and serving layers. Add a data dictionary and
document table grain. Natalie Kwong's
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT episode]]
is the stack vocabulary for this stage.

Weeks 7-8 cover orchestration through a command or scheduler with dependencies,
retries, logs, and rerun behavior. Connect the work to
[[Orchestration]] and [[Apache Airflow]]
and Lars Albertsson's DataOps discussion of workflow engines in
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101]].

Weeks 9-10 cover quality and failures through freshness, volume, schema, and
null checks. They should also cover uniqueness, accepted values, and business
rules. Then break the pipeline on purpose and write recovery notes.
Christopher Bergh's
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]]
is the reliability model for this stage.

During weeks 11-12, clean the README and document setup. Add a project
walkthrough, then practice SQL, Python, and take-home scenarios.
Link your project story to the
[[Data Engineer Role]] you're
targeting, then use [[Job Search]] to
turn the project into applications.

If you add a certificate to the same period, use
[[Data Engineering Certification]] to keep the credential tied to project
evidence.

After that, choose one specialization based on your target role:

- analytics-heavy modeling
- platform engineering
- streaming
- lakehouse formats
- data governance
- product data engineering
- AI-ready data pipelines

## Roadmap Exit Criteria

You're ready to apply for junior data engineering roles when you can follow the
sequence without tutorial steps:

- Write SQL and Python.
- Build raw-to-modeled pipelines.
- Add orchestration and quality checks.
- Explain one practical tradeoff.

Jeff Katz uses Python, SQL, readable code, and tests as the junior bar
[[cite:data-engineering-career-path-and-skills=>Build a Data Engineering Career]]
[[cite:get-data-engineering-job-prep-and-interview=>Data Engineering Job Prep and Interview Guide]].
Natalie Kwong anchors the raw-to-modeled structure
[[cite:data-engineering-tools-modern-data-stack=>ETL vs ELT and Modern Data Engineering]].
Lars Albertsson and Christopher Bergh add workflow engines, tests, and
repeatable operations
[[cite:dataops-principles-and-scalable-data-platforms=>DataOps 101 for Scaling Data Platforms]]
[[cite:dataops-automation-and-reliable-data-pipelines=>Mastering DataOps]].

Turn the learning path into reviewable proof through
[[Data Engineering Portfolio Projects]], then use [[Job Search]] for
applications. If you come from another role, keep this sequence as the
technical path. Use the analyst, data-science, QA, and DevOps transition pages
for role-specific evidence.
