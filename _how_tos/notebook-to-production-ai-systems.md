---
layout: article
title: "How to Take an AI Notebook to Production"
keyword: "notebook to production AI systems"
secondary_keywords:
  - "AI notebook to production"
  - "ML notebook to production"
  - "Jupyter notebook to production"
  - "productionize machine learning notebook"
  - "notebook to production workflow"
summary: "A procedural guide for turning an AI or ML notebook into a production system with scoped business requirements, reproducible code, data paths, evaluation, serving, monitoring, and feedback."
search_intent: "Help readers searching for notebook to production AI systems understand the practical sequence for moving an AI or ML notebook into production, using DataTalks.Club podcast evidence."
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
---

When you take an AI or ML notebook to production, don't start by copying cells
into a service. Start with the decision the system supports. Then make the data
path explicit and extract the code people need to reuse. Add evaluation gates,
choose the serving path, and close the release with monitoring and feedback.

Use this sequence with
[Notebook to Production AI Systems]({{ '/wiki/notebook-to-production-ai-systems/' | relative_url }}),
[Production]({{ '/wiki/production/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). For LLM and RAG systems, use
the [LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }})
alongside this sequence.

[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) frames the
transition in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
as end-to-end ownership. Around 17:27-21:12, he maps modern AI work back to
CRISP-DM. Teams still need business understanding, data understanding, and
preparation. They also need modeling, evaluation, and deployment. Use the
notebook as one working surface inside that lifecycle, not as the product.

## Define The Decision Before The Model

Name the business decision before you name the model. A notebook can make a
prediction look useful while the real workflow needs a rule or ranking. It may
need a review queue, retrieval answer, or product action instead.

Mariano uses business-to-ML translation to draw that boundary.
Around 31:42-37:39 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
he argues that teams sometimes need a decision or workflow rather than a model
call. Keep [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) and
[Data Products]({{ '/wiki/data-products/' | relative_url }}) close to the
problem framing. Don't treat deployment as a packaging step.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) gives the
intake checklist in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Around 4:50-10:26, she starts with the business case and KPIs. She also checks
alternative solutions and problem specificity before modeling. Around
12:22-18:29, she adds stakeholder pairing, buy-in, and concern handling. Use
those conversations to define success and failure before any production code
exists.

Write a one-page production brief before you extract code:

1. Who uses the output?
2. What decision, workflow, or product action changes because of it?
3. Which metric or KPI should improve?
4. What simpler rule, SQL query, or workflow would be good enough?
5. What happens when the system is wrong, late, unavailable, or uncertain?
6. Who can approve launch, rollback, and future changes?

Keep that brief next to
[KPIs]({{ '/wiki/kpis/' | relative_url }}),
[Metrics]({{ '/wiki/metrics/' | relative_url }}), and
[Data Product Adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
while you scope the work.

## Extract Notebook Code Into A Reproducible Project

Move the notebook into a project that another person can run without your
memory. Keep the notebook if it helps exploration, but move reusable code into
modules and tests. Add configuration plus scheduled or callable entry points.

[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) gives the maintainable
code boundary in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
Around 6:50-13:19, he ties production readiness to maintainability, modular
components, and testability. He also ties it to stakeholder buy-in and avoiding
overcomplicated solutions. Around 8:49, he describes refactoring
notebook-shaped "walls of text" into smaller pieces that someone can test and
change.

[Mihail Eric]({{ '/people/mihaileric/' | relative_url }}) gives the
research-to-production version in
[From Research to Production]({{ '/podcasts/research-to-production-ml-systems-roadmap/' | relative_url }}).
Around 10:52-17:35, researchers use notebooks, experiment tooling, and
benchmarks for hypothesis-driven work. Around 17:35-23:32, the ML engineer owns
the full lifecycle with PyTorch and Docker. They also work with cloud
infrastructure and web frameworks. He emphasizes engineering rigor and
reproducibility too.

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
[Software Engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[Testing]({{ '/wiki/testing/' | relative_url }}), and
[Reproducibility]({{ '/wiki/reproducibility/' | relative_url }}). Rerun the
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

## Build The Data And Feature Path

Production notebooks fail when the data path lives only in ad hoc cells. Build
the path from ingestion to training, retrieval, batch scoring, or online
inference as a pipeline people can look at.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) walks through the
classic production-ML version in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 9:47-25:36, he moves from notebooks into ingestion and buffers. He also
covers processing, storage, and Docker jobs. Cloud storage such as Parquet on
S3 is part of that path. SQL or dataframe transformations sit there too.

Around 15:11-16:51, he distinguishes event ingestion with queues such as Kafka
or Kinesis from batch processing.

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
[How to Build Data Pipelines]({{ '/how-tos/how-to-build-data-pipelines/' | relative_url }})
and [Data Pipelines]({{ '/wiki/data-pipelines/' | relative_url }}). Use
[Batch vs Streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }})
when freshness changes the architecture. Use
[Airflow Docker Compose]({{ '/how-tos/airflow-docker-compose/' | relative_url }})
only after your workflow needs scheduling, dependencies, retries,
or backfills.

Andreas makes the orchestration boundary practical around 35:46-41:06 in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
He compares Airflow with simpler schedulers, CloudWatch, and Lambda. He also
discusses queues and Kubernetes. He then recommends starting simple and
iterating when the workflow needs more control.

## Turn Research Into Evaluation Gates

Treat evaluation as the bridge between notebook experiments and production
changes. A metric in a notebook helps select a candidate. A production
evaluation suite protects the system when someone changes a feature or prompt.
It should also catch regressions from model, retrieval, serving-code, and data
source changes.

Mariano connects complex AI systems to gold-standard datasets and systematic
evaluation around 26:32-28:04 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
In the OLX content-generation example, he also discusses prompt engineering and
LLM-as-judge checks for factuality against the input listing around
47:22-49:55 and 57:33-58:45.

For classic ML, Ben adds testing alongside timeboxed bake-offs and cost-benefit
tradeoffs. Around 32:03-55:41 in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
he pushes teams toward simpler baselines and iterative MVPs. He also emphasizes
feature engineering and tests before teams invest in harder-to-maintain
approaches.

Build evaluation gates before launch:

1. A baseline that a model, prompt, or retrieval system must beat.
2. A representative validation set or gold-standard cases.
3. Tests for data schema, feature ranges, missing values, and duplicate keys.
4. Task metrics tied to the production brief, not only offline model scores.
5. Latency and cost checks for serving paths.
6. Regression tests for known failures and sensitive examples.
7. Human review criteria when the output affects people or business risk.

For LLM systems, pair this page with
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and the
[LLM and RAG Production Roadmap]({{ '/roadmaps/llm-rag-production-roadmap/' | relative_url }}).
If the system uses retrieval, test retrieval quality separately from answer
generation so failures don't hide behind one aggregate score.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) adds the
AI-engineering version in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His discussion ties data trust, integration tests, prompt evaluation, and cost
checks to production AI readiness. Use that episode when the notebook contains
prompts, agents, or model calls that need tests beyond offline accuracy.

## Package Serving Around The Product Boundary

Choose serving after you know who needs the output and how quickly they need it.
Some systems can precompute predictions or embeddings. Others need an API,
worker, queue, or batch job. Some need a dashboard or human review interface.

Andreas gives the serving choices in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
Around 31:33, he compares live API calls with precomputed predictions. Around
34:16, he discusses Dockerized training and model storage. Around 37:53, he
covers managed endpoints and cost tradeoffs. Around 40:01, message queues
become a way to sequence jobs instead of turning everything into a single
synchronous request.

Mariano's later AI-system example shows a modern service stack. Around
55:28-1:02:53 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
he moves away from notebooks toward services and observability tools. In that
stack discussion, he names FastAPI, `uv`, and Arize.

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

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the LLM serving
tradeoff in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
Her discussion compares fine-tuning and retrieval with hosted APIs and
open-source models. It also covers latency, cost, and drift. Use that framing
when the notebook result can ship as retrieval, a prompt chain, a tuned model,
or an external API call.

Mariano's caution around 31:42-37:39 matters here too: if structured code or a
rule solves the problem, don't hide that logic inside a model call. That advice
is useful when you work with
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).
Don't make them default answers to every product problem.

## Release With Monitoring And Feedback

Launch only after someone owns service levels, monitoring, incident response,
and feedback intake. A notebook ends when the analysis is convincing. A
production system keeps changing after users see it.

Lina's
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }})
episode gives the release operating model. Around 24:34-32:11, she discusses
service levels and impact assessment before incident response and postmortems.
Her operating model also includes live test sets, small A/B tests, and
root-cause debugging.

Around 36:41-42:03, user bug reports and postmortem action items turn
production failures into backlog work. Around 46:28-49:28, she covers input
distribution changes and feature drift. She also covers logging, feature stores,
and reproducibility.

Mariano adds the AI-product feedback path around 39:28-41:28 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
Users may give explicit feedback, or their behavior may show whether the output
helped. Capture both paths when they're available.

Monitor at four levels:

1. Data: freshness, schema, volume, distributions, and missing values.
2. Model or LLM behavior: accuracy, hallucination rate, calibration, refusal
   rate, drift, and task-specific quality.
3. Service: latency, errors, timeouts, cost, queue depth, and availability.
4. Product: adoption, override rate, user feedback, business KPI movement, and
   incidents.

Tie those signals to
[Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}),
[Data Quality and Observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
[A/B Testing]({{ '/wiki/a-b-testing/' | relative_url }}), and
[Metrics]({{ '/wiki/metrics/' | relative_url }}). Use monitoring to decide when
to rollback, retrain, or re-index. It should also tell the team when to change
a prompt, update a rule, or ask for more labels.

## Notebook-To-Production Sequence

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
It also connects the production work to the responsibilities Mariano and
Andreas describe. Ben, Mihail, and Lina extend the same production AI and MLOps
thread.
