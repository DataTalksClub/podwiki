---
layout: wiki
title: "LLMOps"
summary: "LLMOps covers operating LLM systems in production, from deployment and tracing to evaluation, guardrails, cost control, and feedback loops."
related:
  - MLOps
  - LLM Production Patterns
  - AI Engineering
  - Model Monitoring
  - Agent Engineering
  - Evaluation
  - LLM Deployment
  - DataOps
  - GitOps for Data Teams
  - MLOps vs DevOps
---

LLMOps is the operational discipline for production LLM-based systems and their
deployment, monitoring, evaluation, and ongoing maintenance. DataTalks.Club
guests discuss LLMOps as the LLM-specific analogue of [[MLOps]], with concerns
around prompt caching and trace observability. It also covers LLM-as-judge
evaluation and human-in-the-loop quality control.

The topic sits at the intersection of
[[LLM Production Patterns]],
[[AI Engineering]], and
[[Agent Engineering]].

## Technical Pillars for Shipping AI Products

[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]
includes [[person:pauliusztin=>Paul Iusztin]]'s framing of LLMOps as core AI
engineering work. At 42:28 he names creating and evaluating agents as one skill.
He also names building data pipelines for RAG ingestion and making data
available to agents.

At 46:31 he recommends Arize Phoenix for monitoring code and storing traces. He
also mentions LangSmith, BrainTrust, and LangFuse. At 49:08 he explains that a
trace captures everything that happens between a request and response. A thread
is a collection of user inputs and outputs.

Paul also recommends durable workflows like Prefect or Dagster for orchestrating
agent pipelines at 45:49. These provide queues and retries, making code
resilient during ingestion and retrieval. This bridges
[[MLOps]] and LLMOps: instead of separate
orchestrators for data and agents, one tool can handle both.

## Agent MLOps: Guardrails and Data Lineage

In
[[podcast:s23e03-future-of-ai-agents=>The Future of AI Agents]],
[[person:adityagautam=>Aditya Gautam]] connects agent
governance directly to MLOps. At 30:26 he links guardrails and data lineage to
what he calls Agent MLOps. He explains that companies need to understand what
each agent is doing and how user data is processed. You need to ensure retention
and data lineage.

At 35:58 he emphasizes that cost isn't the only concern. Teams also need to
understand where user data has gone. One entry point agent may send it to
another agent, put it into a database, or pass it to an external offline
workflow. Lineage and visibility are essential for regulated environments.

Aditya also covers infrastructure and deployment risks at 56:40. He notes that
agents are microservices with non-deterministic LLMs, so they should be
replicable on Kubernetes clusters. At 57:47 he says there's no reason agent
deployment can't be done on Kubernetes, which handles managing services and
machines.

## Monitoring and Debuggable MVPs

In
[[podcast:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]],
[[person:hugobowneanderson=>Hugo Bowne-Anderson]] covers
monitoring practices that make LLM systems debuggable. At 13:56 he introduces
the generator-evaluator loop for automated quality control, where one model
generates output and another evaluates it with pass/fail scoring. At 23:00 he
discusses gold test sets, cost, and representativeness for evaluation. At 26:43
he uses failure analysis to decide whether retrieval needs to change.

Hugo recommends Braintrust, Arize, and Logfire for evaluation at 51:10. He also
describes building debuggable MVPs with logging and traces. When something goes
wrong, teams can look at the steps rather than guessing from the final output.
At 52:06 he suggests vibe coding some things first to see what's happening
before adding complexity.

## Evaluation Strategy and Testing Agents

In
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]],
[[person:ranjithakulkarni=>Ranjitha Kulkarni]] treats
evaluation as a core LLMOps practice. At 51:17 she recommends custom datasets and
system benchmarks over public benchmarks like SQuAD, which evaluate model
capability rather than your specific system. At 53:20 she discusses mocking tools,
integration tests, and regression tests for agents. She frames the agentic system
as a software system: input gives predictable output, and you test it accordingly.

At 56:02 Ranjitha emphasizes outcome assertions rather than exact paths. LLMs
can reach a goal through different paths. Evaluation should focus on the outcome
rather than the exact tool-call sequence.
This connects to [[Evaluation]] and
[[LLM Evaluation Workflows]].

## Prompt Caching, Compression, and Cost Optimization

In
[[podcast:production-ready-ai-engineering=>Production AI Engineering]],
[[person:bartoszmikulski=>Bartosz Mikulski]] discusses
prompt evaluation and cost tradeoffs at 28:16. He recommends gathering data from
tests: prepare an evaluation dataset with inputs and expected outputs, then
measure how well the model performs. At some point, adding more examples stops
improving results.

At 30:00 Bartosz introduces prompt compression. The method creates a shorter
prompt by dropping parts of words or reducing token count. At 31:45
he discusses prompt caching, where providers like Anthropic cache the shared
beginning of prompts so you don't resend the entire codebase every time. This
makes coding tasks cheaper.

The
[[book:20241104-llm-engineer-s-handbook|LLM Engineer's Handbook]] by Paul
Iusztin and Maxime Labonne structures this same LLMOps stack end to end. These
techniques connect to
[[LLM Cost Optimization]] and
[[Caching]].

## Feedback Loops and Human-in-the-Loop

Aditya covers feedback collection as an LLMOps practice in
[[podcast:s23e03-future-of-ai-agents=>The Future of AI Agents]].
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

[[person:meryemarik=>Meryem Arik]] frames the deployment choice between API and
open-source models as a core LLMOps decision in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
At 49:57 she recommends using API-based models like GPT-3.5 or GPT-4 for
prototyping because you can get to demos within a day or two. In the long term,
businesses move to open-source models for control and data privacy. They also
seek lower cost and more predictable performance.

At 18:51 she discusses model drift as an API risk: when providers change models
under the hood, production behavior shifts unexpectedly. That risk pushes some
teams toward self-hosted open-source models. At 51:35 she explains that
self-hosting on smaller GPUs or even CPUs can be faster than hosted APIs because
you control the inference stack. This connects to
[[LLM Deployment]].

## Related Pages

Continue with these connected LLMOps topics:

- [[MLOps]]
- [[LLM Production Patterns]]
- [[AI Engineering]]
- [[Model Monitoring]]
- [[Agent Engineering]]
- [[Evaluation]]
- [[LLM Deployment]]
- [[LLM Cost Optimization]]
- [[Caching]]
