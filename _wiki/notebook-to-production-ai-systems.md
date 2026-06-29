---
layout: wiki
title: "Notebook to Production AI Systems"
summary: "How the podcast archive frames the path from notebooks and experiments to end-to-end AI systems in production."
related:
  - Production
  - Machine Learning System Design
  - MLOps
  - Data Products
  - AI Engineering
---

Notebook to production AI systems is the transition from exploratory modeling,
prompting, or notebooks into owned product behavior. Teams handle requirements,
data, and evaluation. They also handle deployment, monitoring, user feedback,
and operational fixes. In the podcast archive, production AI is less about
moving a notebook into a service. The harder work is owning the full decision
cycle around the system.

Here, [Production]({{ '/wiki/production/' | relative_url }}) meets
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}), while recent-season discussions
also connect this topic to [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}).
Guests explain why AI products still need the older habits of data science and
software engineering. Those habits include requirements, evaluation, and
feedback. They also include monitoring and knowing when not to use AI.

## Link Map

The related wiki pages are:

- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})

The podcast discussions are:

- [From Notebook to Production: Building End-to-End AI Systems]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}) with [Mariano Semelman]({{ '/people/marianosemelman/' | relative_url }})
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}) with [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})
- [Applying Computer Vision Research to Building Production-Ready AI Systems]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}) with [Aishwarya Jadhav]({{ '/people/aishwaryajadhav/' | relative_url }})

## Common Definition

The archive defines notebook-to-production work as end-to-end system ownership
rather than deployment alone. In
[Mariano Semelman's notebook-to-production episode]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
Mariano Semelman says this at 18:40. Successful projects need the data scientist
or AI builder to help define requirements with product. The same person or team
then collects data and creates the model or application. They deploy it as a
service or batch job, operate it, monitor it, and learn from production
behavior.

That view matches the broader [MLOps]({{ '/wiki/mlops/' | relative_url }})
archive. The mechanics may change because teams now call model endpoints,
compose LLMs, or build agents. The workflow still includes requirements, data,
evaluation, and deployment. It also includes operation and monitoring. Mariano
explicitly connects modern AI work back to CRISP-DM at 18:40-21:12.

Even when teams train fewer models themselves, the steps required to make a
working product haven't disappeared.

## Delegation Boundaries

Guests differ on how much of the system should be delegated to AI tools. In
[Paul Iusztin's AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
he encourages AI engineers to use assistants broadly. He also warns that serious
projects need custom logic, durable workflows, and queues. Retries, traces, and
monitoring matter more than opaque framework abstractions at 43:49-46:31.

Mariano draws a similar boundary from the product side. In
[his notebook-to-production episode]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
he says at 36:00-37:39 that teams often wanted a decision instead of a
prediction. Sometimes they don't need AI at all.

Aishwarya Jadhav's
autonomous-driving discussion adds the safety-critical version of the same point.
Production deployment requires simulation, closed tracks, and on-road testing.
It also requires a labeling strategy and staged releases before changes reach
driverless operation
([Applying Computer Vision Research to Building Production-Ready AI Systems]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}),
29:45-32:43).

## Requirements Before Models

The first production step is translating the business or user problem into the
right machine learning or AI problem. Mariano gives a mortgage-risk example at
34:29-36:00. A request to predict house price may actually be a decision about
whether a property is valuable enough for a loan. That distinction changes the
target, data, and model. It also changes evaluation and product behavior
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).

This is why the topic belongs with [Data Products]({{ '/wiki/data-products/' | relative_url }}).
The same production framing connects it to
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
Teams start before the notebook by asking what user decision the system supports
and what context they have that the model lacks.
Teams also ask what data is available. They check whether the business
requirement makes sense and whether a simple rule or dummy model is a better
first version.

## Evaluation as Regression Protection

When experiments become products, evaluation becomes regression protection.
Mariano says that once systems become complex, teams need to make sure they
don't break existing behavior. That risk shows up when they add a feature, solve
an error, or change the model. At 26:32-28:04 in
[From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
the discussion connects this directly to gold-standard datasets and systematic
evaluation.

The same approach appears in [Paul Iusztin's AI engineering discussion]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
At 38:41-41:39, Paul says evaluation will keep growing as a skill. Builders need
measurement strategies even when code is generated by AI. That connects
notebook-to-production work to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [Testing]({{ '/wiki/testing/' | relative_url }}).

## Feedback Loops After Launch

Production AI systems improve through product feedback, not offline metrics
alone. Mariano explains at 39:28-41:28 that some systems can use user behavior
as labels. Other use cases still need human labeling and a deliberate labeling
strategy. He distinguishes explicit feedback from implicit feedback. A user can
say an answer is wrong, or their behavior can show which recommendation was useful
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).

In the OLX video-generation example, Mariano describes the same feedback cycle
in product form. He worked closely with car dealers and showed early generated
videos. The team learned what dealers did and didn't want mentioned. They used
prompt engineering and LLM-as-judge checks for factuality against the ad input.

They also used seller requirements such as avoiding marketing slang. Monitoring
tools, including Arize and MLflow, helped trace and evaluate outputs
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }}),
47:22-49:55 and 57:33-58:45).

## Knowing When Not to Use LLMs or Agents

The recent archive repeatedly pushes back against making every production AI
system fully agentic. Mariano says at 1:00:04-1:00:11 that too much agentic
behavior isn't always useful. Teams can take back control when code or rules can
solve a structured part of the problem. They can solve that part outside the LLM
([From Notebook to Production]({{ '/podcasts/s24e03-from-notebook-to-production-building-end-to-end-ai-systems/' | relative_url }})).

Paul makes the engineering version of that argument in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
He recommends owning planning and execution in serious projects rather than
delegating too much to generic abstractions. At 43:49-46:31, he references
durable workflows, data ingestion, and retrieval. He also references queues,
retries, monitoring, and traces as the infrastructure that makes AI product code
resilient.

## Production Validation in Physical Systems

The autonomous-driving episode shows the most conservative version of
notebook-to-production work. Aishwarya Jadhav describes validation through
simulation, closed tracks, and on-road testing with safety drivers before
driverless deployment. She also describes large-scale sensor data management,
human and automated labeling, safety checks, and staged rollouts. Before wider
release, teams rerun models on sensitive pedestrian and gesture cases
([Applying Computer Vision Research to Building Production-Ready AI Systems]({{ '/podcasts/from-computer-vision-research-to-autonomous-driving-ai/' | relative_url }}),
29:45-32:43 and 51:28-52:16).

Less safety-critical AI teams can still use that example because it makes the
archive's general production lesson concrete. The deployment environment creates
failure modes the notebook doesn't show. Production ownership therefore means
collecting the right evidence and testing the right edge cases. Teams roll
changes out at a pace that matches the risk of the product.

## Related Pages

Continue with these related pages:

- [Production]({{ '/wiki/production/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [Data Products]({{ '/wiki/data-products/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
