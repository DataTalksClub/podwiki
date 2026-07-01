---
layout: wiki
title: "LLMOps"
summary: "The operational discipline for deploying, monitoring, evaluating, and maintaining LLM-based systems in production: model serving, prompt versioning, evaluation pipelines, drift detection, guardrails, and feedback loops."
related:
  - MLOps
  - LLM Production Patterns
  - AI Engineering
  - Model Monitoring
  - Agent Engineering
  - Evaluation
  - LLM Deployment
---

LLMOps is the operational discipline for deploying, monitoring, evaluating, and
maintaining LLM-based systems in production. It covers model serving, prompt
versioning, evaluation pipelines, drift detection, guardrails, and feedback
loops. DataTalks.Club guests discuss LLMOps as the LLM-specific analogue of
[MLOps]({{ '/wiki/mlops/' | relative_url }}), with new concerns around prompt
caching, trace observability, LLM-as-judge evaluation, and human-in-the-loop
quality control.

The topic sits at the intersection of
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}), and
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}).

## Technical Pillars for Shipping AI Products

In
[AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}),
[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) frames LLMOps as part
of the core skills for AI engineers. At 42:28 he names creating and evaluating
agents, building data pipelines for RAG ingestion, and knowing how to make data
available to agents. At 46:31 he recommends LLMOps tools like Arize Phoenix for
monitoring code and storing traces, along with LangSmith, BrainTrust, and
LangFuse. He explains that a trace captures everything that happens between a
request and response, while a thread is a collection of user inputs and outputs
at 49:08.

Paul also recommends durable workflows like Prefect or Dagster for orchestrating
agent pipelines at 45:49. These provide queues and retries, making code
resilient during ingestion and retrieval. This bridges
[MLOps]({{ '/wiki/mlops/' | relative_url }}) and LLMOps: instead of separate
orchestrators for data and agents, one tool can handle both.

## Agent MLOps: Guardrails and Data Lineage

In
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}),
[Aditya Gautam]({{ '/people/adityagautam/' | relative_url }}) connects agent
governance directly to MLOps. At 30:26 he links guardrails and data lineage to
what he calls Agent MLOps. He explains that companies need to understand what
each agent is doing and how user data is processed. You need to ensure retention
and data lineage. At 35:58 he emphasizes that more than cost, you need to
understand where your data has gone: one entry point agent sends it to another,
which may put it into a database, and an external offline workflow may process
user data. Lineage and visibility are crucial for regulated environments.

Aditya also covers infrastructure and deployment risks at 56:40. He notes that
agents are basically microservices with non-deterministic LLMs, so they should
be replicable on Kubernetes clusters. At 57:47 he says there is no reason agent
deployment cannot be done on Kubernetes, which handles managing services and
machines.

## Monitoring and Debuggable MVPs

In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) covers
monitoring practices that make LLM systems debuggable. At 13:56 he introduces
the generator-evaluator loop for automated quality control, where one model
generates output and another evaluates it with pass/fail scoring. At 23:00 he
discusses gold test sets, cost, and representativeness for evaluation. At 26:43
he uses failure analysis to decide whether retrieval needs to change.

Hugo recommends evaluation tools like Braintrust, Arize, and Logfire at 51:10.
He also describes building debuggable MVPs with logging and traces, so that when
something goes wrong, you can inspect what happened rather than guessing from
the final output. At 52:06 he suggests vibe coding some things first to see what
is really happening before adding complexity.

## Evaluation Strategy and Testing Agents

In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) treats
evaluation as a core LLMOps practice. At 51:17 she recommends custom datasets and
system benchmarks over public benchmarks like SQuAD, which evaluate model
capability rather than your specific system. At 53:20 she discusses mocking tools,
integration tests, and regression tests for agents. She frames the agentic system
as a software system: input gives predictable output, and you test it accordingly.

At 56:02 Ranjitha emphasizes goal-based evaluation with outcome assertions over
exact paths. LLMs can accomplish the same goal differently, so evaluation should
focus on whether the goal was achieved rather than the exact tool-call sequence.
This connects to [Evaluation]({{ '/wiki/evaluation/' | relative_url }}) and
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

## Prompt Caching, Compression, and Cost Optimization

In
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) discusses
prompt evaluation and cost tradeoffs at 28:16. He recommends gathering data from
tests: prepare an evaluation dataset with inputs and expected outputs, then
measure how well the model performs. At some point, adding more examples stops
improving results.

At 30:00 Bartosz introduces prompt compression, creating a shorter prompt that
does the same thing by dropping parts of words or reducing token count. At 31:45
he discusses prompt caching, where providers like Anthropic cache the shared
beginning of prompts so you do not resend the entire codebase every time. This
makes coding tasks cheaper. These techniques connect to
[LLM Cost Optimization]({{ '/wiki/llm-cost-optimization/' | relative_url }}) and
[Caching]({{ '/wiki/caching/' | relative_url }}).

## Feedback Loops and Human-in-the-Loop

Aditya covers feedback collection as an LLMOps practice in
[The Future of AI Agents]({{ '/podcasts/s23e03-future-of-ai-agents/' | relative_url }}).
At 36:55 he discusses user feedback loops, where implicit signals like repeated
queries or reframed questions indicate frustration. Companies collect these gaps
from bad user feedback, generate synthetic data or use human labeling teams, and
fine-tune the LLM to address edge cases. Over time, this iterative process
improves the evaluation dataset and the model.

At 50:18 Aditya emphasizes aligning LLM judges with human labels. The judge is
trained on human-annotated data, and you need the judge to correlate above 90%
or 95% with human ideology. Even ten years down the line, he says, you still want
humans in the loop as a confidence check. At 59:37 he warns that relying only on
LLMs is a scary scenario: if any bias is replicated in production, you lose your
ground truth.

## Open-Source Models and Production Deployment

In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) frames the deployment
choice between API and open-source models as a core LLMOps decision. At 49:57 she
recommends using API-based models like GPT-3.5 or GPT-4 for prototyping because
you can get to demos within a day or two. In the long term, businesses move to
open-source models for control, data privacy, lower cost, and predictable
performance.

At 18:51 she discusses model drift as an API risk: when providers change models
under the hood, production behavior shifts unexpectedly. This is a key reason
teams transition to self-hosted open-source models. At 51:35 she explains that
self-hosting on smaller GPUs or even CPUs can be faster than hosted APIs because
you control the inference stack. This connects to
[LLM Deployment]({{ '/wiki/llm-deployment/' | relative_url }}).

## Related Pages

- [MLOps]({{ '/wiki/mlops/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [Model Monitoring]({{ '/wiki/model-monitoring/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [Evaluation]({{ '/wiki/evaluation/' | relative_url }})
- [LLM Deployment]({{ '/wiki/llm-deployment/' | relative_url }})
- [LLM Cost Optimization]({{ '/wiki/llm-cost-optimization/' | relative_url }})
- [Caching]({{ '/wiki/caching/' | relative_url }})
