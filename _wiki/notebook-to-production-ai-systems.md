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

The topic sits between [Production]({{ '/wiki/production/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}), and
[Data Products]({{ '/wiki/data-products/' | relative_url }}). It also belongs
with [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}). Classic ML
work adds experiment tracking, feature pipelines, and serving paths. LLM and
agent work adds prompts, retrieval, guardrails, and
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).
Tool calls create another production boundary.

A notebook is a useful exploration surface, but it isn't the production system.

## From Experiment to Owned System

[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) gives the
current DataTalks.Club framing in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}).
Around 17:27-21:12, he maps modern AI work back to CRISP-DM. Business
understanding and data understanding still matter. So do preparation, modeling,
evaluation, and deployment. The AI-specific parts change, but the team still
has to understand the decision before it models anything.

[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) makes the older
production-ML version concrete in
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}).
His 9:47-25:36 discussion moves from notebooks into ingestion and buffering.
He then covers batch or streaming jobs, storage, Docker, and Flask or FastAPI
services.
[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) adds the maintainable
code boundary in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}).
Around 6:50-13:19, he ties production readiness to modular components,
testability, and stakeholder buy-in rather than clever model work alone.

These episodes define the transition as end-to-end ownership of the decision a
model or AI application supports. The team has to know which data and code
produced an output. It also has to know which assumptions are still valid and
which signals will show that the system has stopped helping. That's why the topic
overlaps with [software engineering]({{ '/wiki/software-engineering/' | relative_url }}),
[testing]({{ '/wiki/testing/' | relative_url }}),
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}), and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

## Product Decision Before Modeling

Notebook-to-production work can fail before the notebook if the team translates
a business need into the wrong ML task. Mariano's mortgage-risk example in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
shows the difference. A request to predict house price may be a loan
decision about whether the property value supports the risk. The better framing
changes the target, labels, and evaluation metric. It also changes the
interface and fallback behavior.

Around 31:42-37:39 in the same episode, Mariano argues that teams sometimes
need a decision, rule, or workflow rather than a prediction or LLM call. That
boundary keeps [machine learning system design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
close to product design. The team asks what outcome matters and what data
exists. It also asks who uses the result and what happens when the system is
wrong.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) makes that
intake explicit in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Around 4:50-10:26, she starts with the business case and KPIs, then checks
alternative solutions and problem specificity before modeling. Her framing
keeps [KPIs]({{ '/wiki/kpis/' | relative_url }}) and
[data product adoption]({{ '/wiki/data-product-adoption/' | relative_url }})
inside the production discussion instead of treating deployment as the first
hard step.

## Operable Code and Data Paths

A notebook can explore data, compare ideas, and document a hypothesis. A
production version needs a repeatable path from input data to output behavior.
Andreas's pipeline episode links that path to
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
[orchestration]({{ '/wiki/orchestration/' | relative_url }}), and
[batch versus streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}).
His examples use queues, cloud jobs, and Dockerized services. He also compares
streaming and batch architecture
([From Notebooks to Production, 9:47-25:36]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }})).

Ben Wilson gives the warning against shipping notebook-shaped code. In
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
his 6:50-13:19 discussion connects maintainability with modular code,
testable components, and business buy-in. He also emphasizes simpler solutions.
Another person must be able to rerun, debug, or change the system without
reconstructing the original experiment from memory.

[Mihail Eric]({{ '/people/mihaileric/' | relative_url }}) gives the
research-to-production version in
[From Research to Production]({{ '/podcasts/research-to-production-ml-systems-roadmap/' | relative_url }}).
Around 10:52-23:32, he contrasts hypothesis-driven research tooling with the
ML engineer's full lifecycle. Engineers use PyTorch, Docker, cloud
infrastructure, and web frameworks. They also need engineering rigor and
reproducibility.

His discussion fits the
[Data Scientist to Machine Learning Engineer]({{ '/wiki/data-scientist-to-machine-learning-engineer/' | relative_url }})
transition. The role shift is partly a shift from isolated experiments to
systems other people operate.

## Evaluation as Regression Protection

Once users depend on the output, evaluation is no longer a one-time model
selection step. It protects the team against regressions whenever someone
changes a prompt, model, retrieval index, or serving path. In
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano links complex AI systems to gold-standard datasets and systematic
evaluation around 26:32-28:04. In the OLX video-generation example, he also
describes prompt engineering and LLM-as-judge checks for factuality against the
input listing around 47:22-49:55 and 57:33-58:45.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts the same
discipline inside the AI engineering stack in
[AI Engineering Skill Stack]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
Around 38:41-41:39, he argues that evaluation matters more as AI generates
more code and product behavior. Around 42:28-54:05, he pairs AI assistants,
RAG, and agents with durable workflows. Queues, retries, and traces help teams
debug what happened.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) adds the
data-pipeline and prompt layer in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His episode treats testing and prompt evaluation as production concerns. Prompt
compression, caching, and response-time tradeoffs belong there too. For
[evaluation]({{ '/wiki/evaluation/' | relative_url }}) in AI systems, the team
has to measure correctness, cost, and latency before the system can be trusted
at product scale.

## Feedback, Monitoring, and Incidents

Production AI improves when teams turn real behavior into labels, evaluation
cases, bug reports, or retraining decisions. Around 39:28-41:28 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano separates explicit feedback from implicit feedback. Users may mark an
answer wrong directly, or their behavior may reveal whether a recommendation or
generated output helped.

MLOps discussions broaden feedback into operations. In
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
Lina covers service levels, incident response, and postmortems around
24:34-32:11. She also covers live test sets, small A/B tests, and root-cause
debugging. Those practices connect notebook-to-production work to
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}),
[metrics]({{ '/wiki/metrics/' | relative_url }}), and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).

[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) links the same
production burden to upstream data in
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}).
Model monitoring depends on ETL, data pipelines, and observability. Failures
may start before the model sees the input. That's why
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }})
belongs in the production transition rather than later cleanup.

## Control Boundaries for LLMs and Agents

Guests don't treat "more agentic" as the default direction for production AI.
Mariano argues in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
that teams can take back control when structured code or rules are better than
an LLM. Around 31:42-37:39 and 1:00:04-1:00:11, he uses AI where uncertainty or
generation is valuable and keeps deterministic parts outside the model.

Paul reaches the same boundary from infrastructure in
[AI Engineering Skill Stack]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
His 42:28-54:05 discussion puts AI assistants, RAG, and agents inside durable
workflows. Queues, retries, and traces make those systems debuggable. Retrieval
and monitoring add more control. The model
can generate or reason, but [agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
still need explicit control points.

## Validation Scales With Failure Cost

The release path depends on what happens when the system fails.
[Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }}) gives the
most safety-critical example in
[Applying Computer Vision Research to Building Production-Ready AI Systems]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}).
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
[Production]({{ '/wiki/production/' | relative_url }}) and
[MLOps]({{ '/wiki/mlops/' | relative_url }}) pages. For architecture choices,
use [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }}).
[Data Products]({{ '/wiki/data-products/' | relative_url }}) covers the product
side. For AI application work, use
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}),
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}),
and [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }}).
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
goes deeper on prompts, caching, retrieval, and serving.
