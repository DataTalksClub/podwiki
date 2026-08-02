---
layout: wiki
title: "LLM Deployment"
summary: "Deploying LLMs in production: open-source vs API models, serving challenges, model compression, inference optimization, model drift, and API risk."
related:
  - AI Infrastructure
  - ai-infrastructure-cost-and-ownership
  - LLM Production Patterns
  - LLMOps
  - LLM Evaluation Workflows
  - Agent Ops
  - Agent Engineering
  - AI Product Feedback Loops
  - LLM Cost Optimization
  - Context Engineering
  - Model Monitoring
  - Orchestration
  - Caching
  - LLMs
  - Generative AI
  - RAG vs Fine-Tuning
---

LLM deployment moves a language-model feature from prototype to a service the
team can release, evaluate, monitor, and operate. The work includes model
choice, serving infrastructure, prompt cost, and retrieval cost. It also
includes release control, fallback behavior, and human review for risky outputs.

API models are useful for fast prototypes because teams can test a business
case without owning inference. Teams move toward self-hosted or open-source
models when the product needs stronger privacy or cost control. Latency control
and release control can push the same decision.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@49:44=>Deploying LLMs in Production]][[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training@17:33=>AI Infrastructure Ownership]]

This topic sits between [[AI Infrastructure]],
[[ai-infrastructure-cost-and-ownership=>AI Infrastructure Ownership]],
[[LLM Production Patterns]], and [[LLMOps]]. It also links to
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] because deployment choices change
when knowledge is fetched from a retrieval system instead of baked into model
weights. Teams sequencing production LLM and RAG work can use the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] to place
retrieval and evaluation gates. The same roadmap also covers serving,
monitoring, and security gates.

## Deployment Ownership

Production ownership is broader than the model endpoint. For agent-facing
products, the AI engineer may own user interface needs and backend performance.
They may also own infrastructure tradeoffs, MLOps-style release practices,
orchestration, and evaluation feedback. The feedback then becomes part of the
next release.
[[cite:s23e07-understanding-ai-engineer-role@43:23=>Understanding the AI Engineer Role]][[cite:s23e07-understanding-ai-engineer-role@44:37=>Understanding the AI Engineer Role]][[cite:s23e07-understanding-ai-engineer-role@45:35=>Understanding the AI Engineer Role]]
That makes [[AI Engineer Role]], [[Agent Engineering]], [[Orchestration]], and
[[Model Monitoring]] part of the deployment conversation.

Teams should treat deployment as a release boundary, not only an inference
boundary. The service needs logging, traces, evaluation data, and rollout
controls. Teams also need a way to compare new behavior against old behavior.
Those practices connect LLM deployment to [[LLM Evaluation Workflows]],
[[LLMOps]], and [[AI Product Feedback Loops]].

## Open-Source vs API Models

The open-source versus API decision is the first deployment fork. API models
reduce setup work and help teams prove the business case. Open-source models
give the team more control over privacy and provider drift. They also give more
control over cost and serving performance once the system becomes durable
product infrastructure.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@16:48=>Deploying LLMs in Production]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@49:44=>Deploying LLMs in Production]]

Alternative model products have also become practical choices for many
workflows. The deployment decision is no longer only "hosted API or research
project." Teams can choose hosted assistants or open-source models. They can
also choose search-enabled products or self-hosted inference depending on the
task and operating constraints.
[[cite:production-ready-ai-engineering@33:42=>Production AI Engineering]][[cite:production-ready-ai-engineering@47:19=>Production AI Engineering]]

The product tradeoff includes cost, latency, intellectual property, and data
risk. Enterprise systems with sensitive data often need open-source or
self-hosted options, while fast product discovery can justify proprietary APIs.
[[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]

Self-hosting isn't always cheaper once the team includes staffing and
operations. High-volume workloads can justify specialization and infrastructure
investment. Small or generic workloads may be cheaper to run through hosted
APIs. The team then avoids operating the fine-tuned serving stack.
[[cite:s23e03-future-of-ai-agents@24:58=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@25:43=>The Future of AI Agents]]

## Serving Challenges, Compression, and Inference Optimization

Serving LLMs in production requires managing model size, compute resources, and
latency. Compression, inference optimization, and serving software reduce the
cost of running models without treating quality as separate from infrastructure.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@25:26=>Deploying LLMs in Production]]
For repeated request prefixes and stable context blocks, [[Caching]] is another
serving-path optimization. The team still needs to know which prompt or
retrieval context should be reused.

Teams can run competitive self-hosted models on smaller GPUs or CPUs when the
serving path is optimized. That matters because many businesses deploy on ordinary
hardware rather than on the newest accelerators.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@51:35=>Deploying LLMs in Production]]

For the broader set of techniques that make models smaller, faster, and
cheaper to serve, see
[[model-optimization=>Model Optimization]] and
[[llm-cost-optimization=>LLM cost optimization]].

Cost gates should include prompt size and example count. The model bill is only
one part of the cost. Bartosz Mikulski describes prompt evaluation as a way to
find where examples stop improving output. Teams can then use prompt
compression. They can also use caching when repeated context is stable enough
to reuse.
[[cite:production-ready-ai-engineering@28:16=>Production AI Engineering]][[cite:production-ready-ai-engineering@30:00=>Production AI Engineering]][[cite:production-ready-ai-engineering@31:45=>Production AI Engineering]]

Those choices connect deployment to [[Context Engineering]] and
[[LLM Cost Optimization]].

## Model Drift and API Risk

Model drift is a production risk for API-based models because providers can
change model behavior without the application team controlling the release. A
self-hosted model gives the team a fixed artifact to evaluate, monitor, and
roll forward deliberately.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@18:46=>Deploying LLMs in Production]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@23:37=>Deploying LLMs in Production]]

AI engineering inherits monitoring ideas from [[MLOps]], including data drift,
concept drift, and performance monitoring for agent behavior.
[[cite:s23e07-understanding-ai-engineer-role@45:50=>Understanding the AI Engineer Role]]
When the team uses a hosted API, [[LLM Evaluation Workflows]] should version
prompts and retrieved context. It should also version model identifiers and
outputs so hidden provider changes become visible during regression checks.

## Local Models and Model Specialization

Local deployment becomes more attractive when hosted model and bandwidth costs
dominate the product economics. Affordable GPUs, open-source models, and
low-latency inference providers make local or near-local serving part of the
deployment spectrum.
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]
That deployment choice belongs with
[[llm-cost-optimization=>LLM cost optimization]]
when the team compares hosted API calls, bandwidth, local hardware, and smaller
specialized models.

Teams use task-focused models when a known workflow needs faster serving than a
general model can provide. Latency constraints can rule out agent-style
execution. Some LLM prototypes may then become classic machine-learning systems.
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]][[cite:s23e07-understanding-ai-engineer-role@56:10=>Understanding the AI Engineer Role]][[cite:s23e07-understanding-ai-engineer-role@60:25=>Understanding the AI Engineer Role]]

Infrastructure ownership adds another stage gate. Cloud APIs and managed
inference buy speed, but dedicated or on-prem GPU infrastructure brings
utilization work. It also brings maintenance, updates, and orchestration
responsibilities.
[[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training@05:27=>AI Infrastructure Ownership]][[cite:ai-infrastructure-hybrid-cloud-on-prem-distributed-training@54:31=>AI Infrastructure Ownership]]
That's why [[ai-infrastructure-cost-and-ownership=>AI Infrastructure Ownership]]
belongs next to model selection, not after deployment is already failing.

## Fine-Tuning Purpose: Specialization and Domain Adaptation

Fine-tuning is for specialization, domain adaptation, format, and tone. It's
not a substitute for [[Retrieval-Augmented Generation]] when knowledge changes.
Retrieval is the better fit for current facts and documents.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@26:30=>Deploying LLMs in Production]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@40:46=>Deploying LLMs in Production]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@42:02=>Deploying LLMs in Production]]

Dataset expansion can support fine-tuning when a team starts with a small set
of high-quality labeled examples and uses an LLM to generate more candidates.
The result still needs evaluation against the intended task.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@55:32=>Deploying LLMs in Production]]

Generation tasks remain harder to evaluate than classification. Human review
stays important, even when the team experiments with an LLM as a judge.
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@53:34=>Deploying LLMs in Production]][[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api@56:39=>Deploying LLMs in Production]]
Use [[llm-system-design-interview=>LLM system design interview]] framing when
the deployment tradeoff has to include how the team will test generated answers.

## Agent Services and Evaluation Gates

Agent deployment can use familiar service infrastructure when the company
already runs it. Aditya Gautam describes agents as microservices with
nondeterministic LLM behavior. The CPU/GPU split and service boundary still
need explicit design. The orchestration layer does too.
[[cite:s23e03-future-of-ai-agents@56:40=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@58:07=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@58:25=>The Future of AI Agents]]
That connects LLM deployment to [[Agent Ops]], [[Agent Engineering]], and
[[Orchestration]].

Use tenant- or use-case-specific evaluation sets as release gates:

- routine cases may need a high pass bar
- critical actions may need a perfect pass before release
- tools or regulated workflows need red-team cases, guardrails, and human review.

[[cite:s23e03-future-of-ai-agents@43:30=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@47:16=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@48:11=>The Future of AI Agents]]

LLM judges don't remove human labels. Gautam describes checking judge behavior
against human-labeled samples before trusting automated evaluation.
[[cite:s23e03-future-of-ai-agents@50:18=>The Future of AI Agents]][[cite:s23e03-future-of-ai-agents@54:38=>The Future of AI Agents]]
Deployment is ready only when [[LLM Evaluation Workflows]] and
[[Model Monitoring]] can turn production behavior into new test cases.
[[AI Product Feedback Loops]] then connect those cases to release decisions.

## Related Pages

LLM deployment decisions connect model choice to the production system around
the model.

- [[AI Infrastructure]]
- [[ai-infrastructure-cost-and-ownership=>AI Infrastructure Ownership]]
- [[LLM Production Patterns]]
- [[LLMOps]]
- [[LLM Evaluation Workflows]]
- [[Agent Ops]]
- [[Agent Engineering]]
- [[AI Product Feedback Loops]]
- [[LLM Cost Optimization]]
- [[Context Engineering]]
- [[Model Monitoring]]
- [[Orchestration]]
- [[Caching]]
- [[LLMs]]
- [[Generative AI]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[Production]]
- [[MLOps]]
