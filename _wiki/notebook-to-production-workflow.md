---
layout: article
tags: ["how-to"]
title: "Notebook to Production"
keyword: "notebook to production AI systems"
secondary_keywords:
  - "AI notebook to production"
  - "ML notebook to production"
  - "Jupyter notebook to production"
  - "productionize machine learning notebook"
  - "notebook to production workflow"
summary: "A workflow for turning AI or ML notebooks into production systems with decisions, reusable code, evaluation, serving, and monitoring."
related_wiki:
  - Notebook to Production AI Systems
  - Production
  - Machine Learning System Design
  - MLOps
  - Data Pipelines
  - Model Monitoring
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - AI Engineering
  - Data Products
  - Data Translator Role
---

When you take an AI or ML notebook to production, don't start by copying cells
into a service. Start with the decision the system supports. Then make the data
path explicit and extract the code people need to reuse. Add evaluation gates,
choose the serving path, and close the release with monitoring and feedback.

Use this sequence with
[[Notebook to Production AI Systems]],
[[Production]],
[[Machine Learning System Design]],
and [[MLOps]]. For LLM and RAG systems, use
the [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
alongside this sequence.

Modern AI work still fits a CRISP-DM-style lifecycle. Teams first understand the
business and data, then prepare data and model, then evaluate and deploy. They
can use the notebook during exploration, but they shouldn't ship it as the
product
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

## Define the decision before the model

Name the business decision before you name the model. A notebook can make a
prediction look useful while the real workflow needs a rule or ranking. It may
need a review queue, retrieval answer, or product action instead.

Business-to-ML translation draws that boundary. Teams sometimes need a decision
or workflow rather than a model call
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].
Keep [[AI Engineering]] and [[Data Products]] close to the problem framing.
Don't treat deployment as a packaging step.

Start the intake with the business case and KPIs, then check alternative
solutions and problem specificity before modeling. Add stakeholder pairing,
buy-in, and concern handling before the team commits to production work
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].
Use those conversations to define success and failure before any production
code exists.

Start simple and fail fast when the team is still testing product value. Product
feedback and fast learning should come before heavier model or platform
complexity
([[cite:data-science-leadership-hiring-mlops@30:06=>From Model to Product]]
[[cite:data-science-leadership-hiring-mlops@33:36=>Start Simple and Fail Fast]]).
The first production version should be the smallest baseline that can touch the
workflow. It should show whether users and KPIs move before the team adds
complexity.

For translator-led prototypes, the handoff is part of the workflow. A rough
script, spreadsheet, or dashboard can validate demand. Treat it as proof of
value rather than the production design. Once the use case is clear, name the
owner who can rewrite and operate the useful part. That owner also explains and
supports the system
[[cite:data-translator-role-and-data-strategy=>Data Translator Role and Data Strategy]].

That owner may keep some code, rebuild from scratch, or automate the manual
version. Ownership should move from "the person who proved it" to the team that
can maintain the system.

Write a one-page production brief before you extract code:

1. Who uses the output?
2. What decision, workflow, or product action changes because of it?
3. Which metric or KPI should improve?
4. What simpler rule, SQL query, or workflow would be good enough?
5. What happens when the system is wrong, late, unavailable, or uncertain?
6. Who can approve launch, rollback, and future changes?

Keep that brief next to
[[KPIs]],
[[Metrics]], and
[[Data Product Adoption]]
while you scope the work.

## Extract notebook code into a reproducible project

Move the notebook into a project that another person can run without your
memory. Keep the notebook if it helps exploration, but move reusable code into
modules and tests. Add configuration plus scheduled or callable entry points.

Production readiness depends on maintainable, modular, testable code. It also
requires stakeholder buy-in and restraint against overcomplicated solutions.
Refactor notebook-shaped "walls of text" into smaller pieces that someone can
test and change
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]].

Research work uses notebooks and experiment tooling to run benchmarks for
hypothesis-driven work. Production ML engineering adds lifecycle ownership,
engineering rigor, and reproducibility. It also requires PyTorch and Docker
practice. Cloud infrastructure and web frameworks matter too
[[cite:research-to-production-ml-systems-roadmap=>From Research to Production]].

CJ Jenkins describes the career-transition version of the same gap. An academic
researcher may understand statistics and modeling. They may still need Python
and API practice before the work can become a production artifact. Docker and
deployment practice matter too, especially when a notebook result has to become
a service another team can run
[[cite:postdoc-to-data-science-lead-career-transition@6:10=>Postdoc to Data Science Lead]].

The learner-to-practitioner version is practical. Learners move from exploratory
analysis toward reusable code, project structure, and production habits
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@26:58=>Reusable Code and Production Practices]].
In Daniel Egbo's account, that move included virtual environments and cloud
computing as much as code refactoring. The production step also makes the run
context explicit enough for another machine or teammate.

Use a small project structure before you add platform complexity:

```text
project/
  notebooks/
  src/
  tests/
  configs/
  pipelines/
  app/
  evals/
  README.md
```

Put exploration in `notebooks/` and reusable code in `src/`, then use `src/`
for transformations and feature builders. Add prompts, retrieval code, and
model wrappers there too.

Put API or worker entry points in `app/`. Put training, batch scoring, index
refreshes, or other repeatable jobs in `pipelines/`. Put evaluation cases and
expected behavior in `evals/`.

This structure connects the notebook to
[[Software Engineering]],
[[Testing]], and
[[Reproducibility]]. Rerun the
system from known inputs and check the output, test result, or failure.

Extract code in this order:

1. Move constants, credentials, paths, thresholds, and model names into
   configuration, and keep secrets out of the notebook and the repository.
2. Turn cleaning, feature, prompt, retrieval, and post-processing cells into
   functions with typed inputs and outputs.
3. Add tests for the transformations before you change their behavior.
4. Add a command, scheduled job, worker, or API endpoint that calls the same
   functions the tests call.
5. Keep the notebook as an example or experiment log only after the production
   path runs without notebook state.

## Build the data and feature path

Production notebooks fail when the data path lives only in ad hoc cells. Build
the path from ingestion to training, retrieval, batch scoring, or online
inference as a pipeline people can look at.

The classic production ML path moves from notebooks into ingestion and buffers,
then processing, storage, and Docker jobs. Cloud storage such as Parquet on S3
can sit on that path, along with SQL or dataframe transformations
[[cite:production-ml-pipelines-with-aws-and-kafka@34:16=>Dockerized Training and Model Storage]].

Event ingestion with queues such as Kafka or Kinesis solves a different problem
from batch processing
[[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].

Use the simpler path until a harder requirement forces a more complex one:

1. Read from a stable source or fixture.
2. Save raw inputs before transformation.
3. Build deterministic cleaning and feature steps.
4. Version the data, features, prompts, retrieval index, or model inputs that
   change behavior.
5. Run the same path in training, evaluation, and serving where possible.
6. Add batch, streaming, or message queues only when freshness and scale need
   them.

For the broader pipeline sequence, use
[[How to Build Data Pipelines]]
and [[Data Pipelines]]. Use
[[Batch vs Streaming]]
when freshness changes the architecture. Use
[[Apache Airflow]]
only after your workflow needs scheduling, dependencies, retries,
or backfills.

Compare Airflow with simpler schedulers, CloudWatch, and Lambda before adding a
workflow orchestrator. Queues and Kubernetes may be useful later, but start
simple and iterate when the workflow needs more control
[[cite:production-ml-pipelines-with-aws-and-kafka=>From Notebooks to Production]].

## Turn research into evaluation gates

Treat evaluation as the bridge between notebook experiments and production
changes. A metric in a notebook helps select a candidate. A production
evaluation suite protects the system when someone changes a feature or prompt.
It should also catch regressions from model, retrieval, serving-code, and data
source changes.

Complex AI systems need gold-standard datasets and systematic evaluation. The
OLX content-generation example combines prompt engineering with LLM-as-judge
checks for factuality against the input listing
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

For classic ML, add testing alongside timeboxed bake-offs and cost-benefit
tradeoffs. Start with simpler baselines and iterative MVPs, and use feature
engineering plus tests before investing in harder-to-maintain approaches
[[cite:machine-learning-engineering-production-best-practices=>Practical Machine Learning Engineering for Production]].

Build evaluation gates before launch:

1. A baseline that a model, prompt, or retrieval system must beat.
2. A representative validation set or gold-standard cases.
3. Tests for data schema, feature ranges, missing values, and duplicate keys.
4. Task metrics tied to the production brief, not only offline model scores.
5. Latency and cost checks for serving paths.
6. Regression tests for known failures and sensitive examples.
7. Human review criteria when the output affects people or business risk.

For LLM systems, pair this page with
[[LLM Evaluation Workflows]],
[[LLM Production Patterns]],
and the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].
If the system uses retrieval, test retrieval quality separately from answer
generation so failures don't hide behind one aggregate score.

Production AI readiness also depends on data trust, integration tests, prompt
evaluation, and cost checks
[[cite:production-ready-ai-engineering=>Production AI Engineering]].
Use that episode when the notebook contains prompts, agents, or model calls
that need tests beyond offline accuracy.

## Package serving around the product boundary

Choose serving after you know who needs the output and how quickly they need it.
Some systems can precompute predictions or embeddings. Others need an API,
worker, queue, or batch job. Some need a dashboard or human review interface.

Compare live API calls with precomputed predictions before choosing a serving
path. Include Dockerized training, model storage, managed endpoints, and cost
tradeoffs in that decision. Message queues can sequence jobs instead of turning
everything into a single synchronous request
[[cite:production-ml-pipelines-with-aws-and-kafka@31:33=>From Notebooks to Production]]
[[cite:production-ml-pipelines-with-aws-and-kafka@34:16=>From Notebooks to Production]].

Modern AI systems often move away from notebooks toward services and
observability tools. FastAPI, `uv`, and Arize are one example stack for that
shift
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

High-stakes systems need a production surface that frontline users can work with
as decision support. That surface includes UI, training, and trust-building. It
also needs explicit operational limits, not only scoring code
([[cite:building-domestic-risk-assessment-tool@32:10=>Frontline Workflow Deployment]]
[[cite:building-domestic-risk-assessment-tool@35:50=>Decision Support UI]]).

Keep control boundaries explicit:

1. Put deterministic transformations, business rules, validation, and routing
   in code.
2. Use models or LLMs where uncertainty, ranking, generation, or perception
   creates value.
3. Store the model version, prompt version, retrieval index version, and config
   version with each production output.
4. Add timeouts, retries, and fallbacks before the first user-facing launch.
5. Decide whether users see confidence, citations, explanations, or manual
   review states.

For LLM serving, compare fine-tuning and retrieval with hosted APIs and
open-source models. Include latency, cost, and drift in that decision
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
Use that framing when the notebook result can ship as retrieval, a prompt
chain, a tuned model, or an external API call.

If structured code or a rule solves the problem, don't hide that logic inside a
model call
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].
That advice is useful when you work with
[[Agent Engineering]],
[[agent-engineering=>AI Agents]], and
[[LLM Production Patterns]].
Don't make them default answers to every product problem.

## Release with monitoring and feedback

Launch only after someone owns service levels, monitoring, incident response,
and feedback intake. A notebook ends when the analysis is convincing. A
production system keeps changing after users see it.

Release work starts with service levels and impact assessment before incident
response and postmortems. It can also include live test sets, small A/B tests,
and root-cause debugging
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].

User bug reports and postmortem action items turn production failures into
backlog work. Track input distribution changes and feature drift. Add logging,
feature stores, and reproducibility when the system needs them
[[cite:human-centered-mlops-and-model-monitoring=>Human-Centered MLOps]].

AI products can collect explicit user feedback and behavioral feedback. Capture
both when they're available
[[cite:s24e03-from-notebook-to-production-building-end-to-end-ai-systems=>From Notebook to Production]].

Monitor at four levels:

1. Data: freshness, schema, volume, distributions, and missing values.
2. Model or LLM behavior: accuracy, hallucination rate, calibration, refusal
   rate, drift, and task-specific quality.
3. Service: latency, errors, timeouts, cost, queue depth, and availability.
4. Product: adoption, override rate, user feedback, business KPI movement, and
   incidents.

Tie those signals to
[[Model Monitoring]],
[[Data Quality and Observability]],
[[a-b-testing=>A/B Testing]], and
[[Metrics]]. Use monitoring to decide when
to rollback, retrain, or re-index. It should also tell the team when to change
a prompt, update a rule, or ask for more labels.

## Production sequence

Use this sequence when you turn a notebook into a system:

1. Write the production brief: user, decision, KPI, failure modes, approval
   owner, and rollback owner.
2. Decide whether the first production version needs ML, an LLM, retrieval,
   rules, SQL, or a human workflow.
3. Build a repeatable data path from raw inputs to features, prompts,
   embeddings, training rows, or serving inputs.
4. Move reusable notebook code into modules with tests and configuration.
5. Add a baseline and evaluation cases before changing model or prompt
   complexity.
6. Choose batch, API, queue, or scheduled serving based on freshness, latency,
   cost, and user workflow.
7. Package the runtime with pinned dependencies, environment configuration, and
   a documented run command.
8. Log enough input, output, version, and trace data to reproduce failures.
9. Release behind a small audience, shadow mode, manual review, or A/B test
   when risk requires it.
10. Monitor data, model behavior, service health, cost, and product outcomes.
11. Convert user feedback, incident reviews, and failed evaluation cases into
   new tests before the next release.

This sequence keeps the notebook useful without pretending it's the system.
It connects the production work to decisions and reusable code. It also covers
data paths, evaluation gates, serving boundaries, and monitoring.
