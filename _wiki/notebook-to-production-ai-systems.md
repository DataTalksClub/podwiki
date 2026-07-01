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

Notebook-to-production AI systems turn exploratory work into reliable
user-facing behavior. The starting point may be a notebook, model experiment,
prompt or research prototype. In DataTalks.Club discussions, this transition
isn't just deployment. It's the move from a promising experiment to a system
with owners and evaluation. The system also needs monitoring, feedback loops,
and a way to change safely.

The topic connects [Production]({{ '/wiki/production/' | relative_url }}),
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}). Classic ML
projects bring experiment tracking plus feature pipelines. LLM and agent
projects add prompts, retrieval, tool calls and guardrails. A notebook is a
useful exploration surface, but it isn't the production system.

## Common Definition

Across these episodes, notebook-to-production means end-to-end ownership of the
decision a model or AI application supports. In
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
[Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }}) frames the
work around requirements and data. Modeling, deployment, monitoring, and
learning from production behavior follow. Around 17:27-21:12, he connects the
modern AI workflow back to CRISP-DM.

Business understanding still comes before modeling, and deployment still needs
evaluation after launch.

Earlier production-ML episodes make the same point with different tooling. In
[From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
[Andreas Kretz]({{ '/people/andreaskretz/' | relative_url }}) describes the move
from notebooks into data pipelines and Dockerized services. He also covers
message queues, batch and streaming processing, and cloud jobs. In
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
[Ben Wilson]({{ '/people/benwilson/' | relative_url }}) emphasizes maintainable
code and modular components. He also emphasizes stakeholder buy-in and avoiding
needless complexity.

The common definition is practical. Define the product decision, make the
experiment reproducible enough for others to operate, and build the surrounding
system so the team can measure it. That's why the production
transition overlaps with
[data products]({{ '/wiki/data-products/' | relative_url }}) and
[software engineering]({{ '/wiki/software-engineering/' | relative_url }}). It
also overlaps with [testing]({{ '/wiki/testing/' | relative_url }}) and
[model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}), not only
model training.

## Guest Differences

Guests mostly agree on the lifecycle, but they differ on where the hardest
boundary sits. Mariano starts from product ownership. The first mistake is often
translating a business need into the wrong ML task. Around 31:42-37:39 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
he argues that teams sometimes need a decision, rule, or workflow rather than a
prediction or LLM call.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) puts more emphasis
on the AI engineering stack. In
[Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
he treats AI assistants, RAG, and agents as part of the practical skill stack.
He pairs them with durable workflows, queues, retries, and traces. Around
42:28-54:05, he moves from experimentation to debuggable infrastructure.

[Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }}) gives the
safety-critical version of the same transition. In
[Aishwarya's production computer vision episode]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}),
production validation depends on simulation and closed-track testing. It also
depends on on-road testing, labeling strategy, release cadence and inherited
safety tests. Around 29:45-32:43 and 51:28-52:53, her examples show that the
right production path
depends on failure cost. A marketing-content generator doesn't need the same
release process as an autonomous-driving perception stack.

## Start With the Product Decision

The first production step is to turn an ambiguous request into a decision the
system can support. Mariano's mortgage-risk example in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
shows why this matters. A request to predict house price may be a loan
decision about whether the property value supports the risk. The better framing
changes the target, labels, evaluation metric, user interface and fallback
behavior.

This is the same design discipline described in
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
The production path starts before the notebook by asking what outcome matters
and what data exists. Teams also ask how the system will be used and what
happens when it's wrong.

[Lina Weichbrodt]({{ '/people/linaweichbrodt/' | relative_url }}) makes that
intake explicit in
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}).
Around 4:50-10:26, she starts with the business case and KPIs. She also checks
alternative solutions and problem specificity before modeling.

## Turn Experiments Into Operable Code

A notebook can be the right place to explore data and compare ideas, but the
production artifact needs a repeatable execution path. Andreas's pipeline
episode moves from notebooks into ingestion, buffering, processing, and storage.
It then adds visualization, Docker, and Flask or FastAPI. Cloud jobs and
streaming or batch architecture follow
([From Notebooks to Production]({{ '/podcasts/production-ml-pipelines-with-aws-and-kafka/' | relative_url }}),
9:47-25:36). That framing links notebook-to-production work to
[data pipelines]({{ '/wiki/data-pipelines/' | relative_url }}),
[data engineering platforms]({{ '/wiki/data-engineering-platforms/' | relative_url }}),
and [batch versus streaming]({{ '/comparisons/batch-vs-streaming/' | relative_url }}).

Ben Wilson gives the clearest warning in these discussions
against shipping notebook-shaped code. Around 6:50-13:19 in
[Practical Machine Learning Engineering for Production]({{ '/podcasts/machine-learning-engineering-production-best-practices/' | relative_url }}),
he connects maintainability to modular code and testable components. He also
connects it to business buy-in and simpler solutions. His argument complements
[reproducibility]({{ '/wiki/reproducibility/' | relative_url }}).

A production team needs to know which code and data produced an output. It also
needs the parameters and dependencies. Another person must be able to rerun or
change the system.

[Mihail Eric]({{ '/people/mihaileric/' | relative_url }}) gives the
research-to-production version of this point in
[From Research to Production]({{ '/podcasts/research-to-production-ml-systems-roadmap/' | relative_url }}).
Around 10:52-23:32, he contrasts hypothesis-driven research tooling with the ML
engineer's full lifecycle. Engineers use PyTorch, Docker and cloud
infrastructure. They also need web frameworks, engineering rigor and
reproducibility. See
[Data Scientist to Machine Learning Engineer]({{ '/wiki/data-scientist-to-machine-learning-engineer/' | relative_url }})
for that role transition.

## Evaluation Becomes Regression Protection

Once an experiment affects users, evaluation is no longer a one-time model
selection activity. It becomes protection against regressions whenever the team
changes a prompt, model, retrieval index or serving path. In
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano connects complex AI systems to gold-standard datasets and systematic
evaluation around 26:32-28:04. In the OLX video-generation example, he also
describes prompt engineering and LLM-as-judge checks for factuality against the
input listing around 47:22-49:55 and 57:33-58:45.

This connects the production transition to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [evaluation]({{ '/wiki/evaluation/' | relative_url }}). Paul makes the same
future-facing claim in his AI engineering episode. Around 38:41-41:39, he
argues that evaluation grows in importance as AI generates more code and
product behavior. [Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }})
adds the data-pipeline side in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
where testing and prompt evaluation appear as production concerns. He also
covers prompt compression, caching, and response-time tradeoffs.

## Build Feedback and Monitoring Into the Product

Production AI improves through feedback loops, not offline metrics alone. Around
39:28-41:28 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano separates explicit feedback from implicit feedback. Users may directly
mark an answer wrong. Their behavior may also reveal whether a recommendation or
generated output helped. The useful production question is how those signals
become labels, evaluations, bug reports, or retraining decisions.

MLOps episodes broaden that into operations. In
[Human-Centered MLOps]({{ '/podcasts/human-centered-mlops-and-model-monitoring/' | relative_url }}),
Lina covers service levels, incident response, and postmortems around
24:34-32:11. She also covers live test sets, small A/B tests, and root-cause
debugging. In
[MLOps Architect Guide]({{ '/podcasts/mlops-model-monitoring-data-observability/' | relative_url }}),
[Danny Leybzon]({{ '/people/dannyleybzon/' | relative_url }}) connects model
monitoring to upstream ETL, data pipelines, and observability. Those discussions
explain why [MLOps]({{ '/wiki/mlops/' | relative_url }}),
[data quality and observability]({{ '/wiki/data-quality-and-observability/' | relative_url }}),
and [model monitoring]({{ '/wiki/model-monitoring/' | relative_url }}) are part
of the production transition rather than later cleanup.

## Keep Control Where Determinism Helps

Guests don't treat "more agentic" as the default production direction.
Mariano argues in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})
that teams can take back control when structured code or rules are better than
an LLM. Around 31:42-37:39 and 1:00:04-1:00:11, he uses AI where uncertainty or
generation is valuable and keeps deterministic parts outside the model.

Paul's AI engineering episode reaches the same boundary from infrastructure.
Around 42:28-54:05 in
[Paul's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
durable workflows and queues make AI applications operable. Retries, traces,
retrieval and monitoring make them debuggable. That connects notebook-to-production
systems to
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}),
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}), and
[LLM production practices]({{ '/wiki/llm-production-patterns/' | relative_url }}).
The model can be powerful, but the system still needs explicit control points.

## Match Validation to Failure Cost

The final production path depends on what happens when the system fails.
Among these episodes, Aishwarya gives the most conservative example. Around
29:45-32:43 in
[Aishwarya's production computer vision episode]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}),
she describes validation through simulation and closed tracks. Teams then move
to on-road testing, large-scale sensor data and labeling. Safety checks plus
staged rollouts come before wider release.

Around 51:28-52:53, sensitive
pedestrian and gesture cases become inherited tests that new models must pass.

Less safety-critical teams can still use the same structure. A recommender or
ranking system should have a release path proportional to its business and user
risk. The same is true for a generated ad description, fraud model or support
chatbot. The path may include a baseline, shadow mode and manual review. It may
also include a canary release, A/B test, rollback plan or monitoring alerts.

The exact controls differ, but the shared production rule is stable.
The deployment environment exposes failures the notebook can't.

## Related Pages

These pages expand the adjacent production decisions:

- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Production ML Project Checklist]({{ '/wiki/production-ml-project-checklist/' | relative_url }})
- [Data Scientist to Machine Learning Engineer]({{ '/wiki/data-scientist-to-machine-learning-engineer/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
