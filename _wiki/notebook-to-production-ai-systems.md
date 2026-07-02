---
layout: wiki
title: "Notebook to Production AI Systems"
summary: "How DataTalks.Club guests frame the path from notebooks and experiments to end-to-end AI systems in production."
related:
  - Production
  - Machine Learning System Design
  - MLOps
  - Data Products
  - AI Engineering
---

Notebook-to-production AI systems turn exploratory work into behavior people
can rely on. The starting point may be a notebook, model experiment, prompt, or
research prototype. DataTalks.Club guests usually describe the transition as a
change in ownership. Someone has to define the product decision, run the code
again, evaluate output quality, and monitor behavior after launch. The team
also has to change the system without breaking users.

The topic sits between [[Production]],
[[Machine Learning System Design]],
[[MLOps]], and
[[Data Products]]. It also belongs
with [[AI Engineering]]. Classic ML
work adds experiment tracking, feature pipelines, and serving paths. LLM and
agent work adds prompts, retrieval, guardrails, and
[[LLM evaluation workflows]].
Tool calls create another production boundary.

A notebook is a useful exploration surface, but it isn't the production system.

## From Experiment to Owned System

[[person:marianosemelman|Mariano Semelman]] gives the
current DataTalks.Club framing in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]].
Around 17:27-21:12, he maps modern AI work back to CRISP-DM. Business
understanding and data understanding still matter. So do preparation, modeling,
evaluation, and deployment. The AI-specific parts change, but the team still
has to understand the decision before it models anything.

[[person:andreaskretz|Andreas Kretz]] makes the older
production-ML version concrete in
[[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production]].
His 9:47-25:36 discussion moves from notebooks into ingestion and buffering.
He then covers batch or streaming jobs, storage, Docker, and Flask or FastAPI
services.
[[person:benwilson|Ben Wilson]] adds the maintainable
code boundary in
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]].
Around 6:50-13:19, he ties production readiness to modular components,
testability, and stakeholder buy-in rather than clever model work alone.

These episodes define the transition as end-to-end ownership of the decision a
model or AI application supports. The team has to know which data and code
produced an output. It also has to know which assumptions are still valid and
which signals will show that the system has stopped helping. That's why the topic
overlaps with [[software engineering]],
[[testing]],
[[reproducibility]], and
[[model monitoring]].

## Product Decision Before Modeling

Notebook-to-production work can fail before the notebook if the team translates
a business need into the wrong ML task. Mariano's mortgage-risk example in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]
shows the difference. A request to predict house price may be a loan
decision about whether the property value supports the risk. The better framing
changes the target, labels, and evaluation metric. It also changes the
interface and fallback behavior.

Around 31:42-37:39 in the same episode, Mariano argues that teams sometimes
need a decision, rule, or workflow rather than a prediction or LLM call. That
boundary keeps [[machine learning system design]]
close to product design. The team asks what outcome matters and what data
exists. It also asks who uses the result and what happens when the system is
wrong.

[[person:linaweichbrodt|Lina Weichbrodt]] makes that
intake explicit in
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps]].
Around 4:50-10:26, she starts with the business case and KPIs, then checks
alternative solutions and problem specificity before modeling. Her framing
keeps [[KPIs]] and
[[data product adoption]]
inside the production discussion instead of treating deployment as the first
hard step.

## Operable Code and Data Paths

A notebook can explore data, compare ideas, and document a hypothesis. A
production version needs a repeatable path from input data to output behavior.
Andreas's pipeline episode links that path to
[[data pipelines]],
[[data engineering platforms]],
[[orchestration]], and
[[batch-vs-streaming|batch versus streaming]].
His examples use queues, cloud jobs, and Dockerized services. He also compares
streaming and batch architecture
([[podcast:production-ml-pipelines-with-aws-and-kafka|From Notebooks to Production, 9:47-25:36]]).

Ben Wilson gives the warning against shipping notebook-shaped code. In
[[podcast:machine-learning-engineering-production-best-practices|Practical Machine Learning Engineering for Production]],
his 6:50-13:19 discussion connects maintainability with modular code,
testable components, and business buy-in. He also emphasizes simpler solutions.
Another person must be able to rerun, debug, or change the system without
reconstructing the original experiment from memory.

[[person:mihaileric|Mihail Eric]] gives the
research-to-production version in
[[podcast:research-to-production-ml-systems-roadmap|From Research to Production]].
Around 10:52-23:32, he contrasts hypothesis-driven research tooling with the
ML engineer's full lifecycle. Engineers use PyTorch, Docker, cloud
infrastructure, and web frameworks. They also need engineering rigor and
reproducibility.

His discussion fits the
[[Data Scientist to Machine Learning Engineer]]
transition. The role shift is partly a shift from isolated experiments to
systems other people operate.

## Evaluation as Regression Protection

Once users depend on the output, evaluation is no longer a one-time model
selection step. It protects the team against regressions whenever someone
changes a prompt, model, retrieval index, or serving path. In
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]],
Mariano links complex AI systems to gold-standard datasets and systematic
evaluation around 26:32-28:04. In the OLX video-generation example, he also
describes prompt engineering and LLM-as-judge checks for factuality against the
input listing around 47:22-49:55 and 57:33-58:45.

[[person:pauliusztin|Paul Iusztin]] puts the same
discipline inside the AI engineering stack in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].
Around 38:41-41:39, he argues that evaluation matters more as AI generates
more code and product behavior. Around 42:28-54:05, he pairs AI assistants,
RAG, and agents with durable workflows. Queues, retries, and traces help teams
debug what happened.

[[person:bartoszmikulski|Bartosz Mikulski]] adds the
data-pipeline and prompt layer in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His episode treats testing and prompt evaluation as production concerns. Prompt
compression, caching, and response-time tradeoffs belong there too. For
[[evaluation]] in AI systems, the team
has to measure correctness, cost, and latency before the system can be trusted
at product scale.

## Feedback, Monitoring, and Incidents

Production AI improves when teams turn real behavior into labels, evaluation
cases, bug reports, or retraining decisions. Around 39:28-41:28 in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]],
Mariano separates explicit feedback from implicit feedback. Users may mark an
answer wrong directly, or their behavior may reveal whether a recommendation or
generated output helped.

MLOps discussions broaden feedback into operations. In
[[podcast:human-centered-mlops-and-model-monitoring|Human-Centered MLOps]],
Lina covers service levels, incident response, and postmortems around
24:34-32:11. She also covers live test sets, small A/B tests, and root-cause
debugging. Those practices connect notebook-to-production work to
[[a-b-testing|A/B testing]],
[[metrics]], and
[[model monitoring]].

[[person:dannyleybzon|Danny Leybzon]] links the same
production burden to upstream data in
[[podcast:mlops-model-monitoring-data-observability|MLOps Architect Guide]].
Model monitoring depends on ETL, data pipelines, and observability. Failures
may start before the model sees the input. That's why
[[data quality and observability]]
belongs in the production transition rather than later cleanup.

## Control Boundaries for LLMs and Agents

Guests don't treat "more agentic" as the default direction for production AI.
Mariano argues in
[[podcast:s24e03-from-notebook-to-production-building-end-to-end-ai-systems|From Notebook to Production]]
that teams can take back control when structured code or rules are better than
an LLM. Around 31:42-37:39 and 1:00:04-1:00:11, he uses AI where uncertainty or
generation is valuable and keeps deterministic parts outside the model.

Paul reaches the same boundary from infrastructure in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]].
His 42:28-54:05 discussion puts AI assistants, RAG, and agents inside durable
workflows. Queues, retries, and traces make those systems debuggable. Retrieval
and monitoring add more control. The model
can generate or reason, but [[agent engineering]],
[[agent-engineering|AI agents]], and
[[LLM production patterns]]
still need explicit control points.

## Validation Scales With Failure Cost

The release path depends on what happens when the system fails.
[[person:aishwaryajadhav|Aishwarya Jadhav]] gives the
most safety-critical example in
[[podcast:from-computer-vision-research-to-autonomous-driving-ai|Applying Computer Vision Research to Building Production-Ready AI Systems]].
Around 29:45-32:43, she describes validation through simulation and closed
tracks before on-road testing with large-scale sensor data and labeling. Around
51:28-52:53, sensitive pedestrian and gesture cases become inherited tests that
new models must pass.

A generated ad description or support chatbot shouldn't use the same release
path as an autonomous-driving perception stack. Fraud models and recommenders
sit between those extremes.

Lower-risk systems may use baselines, shadow mode, manual review, and canaries.
They may also use A/B tests, rollback plans, and monitoring alerts. Higher-risk systems need
staged validation and inherited safety tests. The shared rule is still stable:
the deployment environment exposes failures the notebook can't.


## Adjacent Production Topics

Readers usually need this page together with the broader
[[Production]] and
[[MLOps]] pages. For architecture choices,
use [[Machine Learning System Design]]
and [[Production ML Project Checklist]].
[[Data Products]] covers the product
side. For AI application work, use
[[AI Engineering]],
[[LLM Evaluation Workflows]],
and [[Model Monitoring]].
[[LLM Production Patterns]]
goes deeper on prompts, caching, retrieval, and serving.
