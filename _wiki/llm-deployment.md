---
layout: wiki
title: "LLM Deployment"
summary: "Deploying LLMs in production: open-source vs API models, serving challenges, model compression, inference optimization, model drift, and API risk."
related:
  - AI Infrastructure
  - LLM Production Patterns
  - Caching
  - LLMs
  - Generative AI
  - RAG vs Fine-Tuning
---

LLM deployment covers the engineering decisions required to move a language
model from prototype to a reliable production system. It includes choosing
between API-based and open-source models, managing serving infrastructure,
optimizing inference performance, and handling the risks that come with
model changes over time.

API models are useful for fast prototypes. Teams use self-hosted open-source
models when production needs stronger control over data, cost, latency, and
model changes
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

This topic connects to [[AI Infrastructure]] and
[[LLM Production Patterns]]. It also links to the
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] comparison and supports
[[llm-system-design-interview=>LLM system design interview]] answers. Deployment
choices have to explain latency and cost. They also need to cover provider
drift and fallback behavior.
Teams sequencing production LLM and RAG work can use the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] to place
retrieval, evaluation, serving, and monitoring.

## Open-Source vs API Models

The open-source versus API decision is the first deployment fork. API models
reduce setup work and help teams prove the business case. Open-source models
give the team more control over privacy and provider drift. They also give more
control over cost and serving performance once the system becomes durable
product infrastructure
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Alternative model products have also become practical choices for many
workflows. The deployment decision is no longer only "hosted API or research
project." Teams can choose among hosted assistants, open-source
models, search-enabled products, and self-hosted inference depending on the
task and operating constraints
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

The product tradeoff includes cost, latency, intellectual property, and data
risk. Enterprise systems with sensitive data often need open-source or
self-hosted options, while fast product discovery can justify proprietary APIs
([[cite:practical-llm-use-cases-and-product-patterns=>Practical LLM Use Cases]]).

## Serving Challenges, Compression, and Inference Optimization

Serving LLMs in production requires managing model size, compute resources, and
latency. Compression, inference optimization, and serving software reduce the
cost of running models without treating quality as separate from infrastructure
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
For repeated request prefixes and stable context blocks, [[Caching]] is another
serving-path optimization. The team still needs to know which prompt or
retrieval context should be reused.

Teams can run competitive self-hosted models on smaller GPUs or CPUs when the
serving path is optimized. That matters because many businesses deploy on ordinary
hardware rather than on the newest accelerators
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

For the broader set of techniques that make models smaller, faster, and
cheaper to serve, see
[[Model Optimization]] and
[[llm-cost-optimization=>LLM cost optimization]].

## Model Drift and API Risk

Model drift is a production risk for API-based models because providers can
change model behavior without the application team controlling the release. A
self-hosted model gives the team a fixed artifact to evaluate, monitor, and
roll forward deliberately
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

AI engineering inherits monitoring ideas from [[MLOps]], including data drift,
concept drift, and performance monitoring for agent behavior
([[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).

## Local Models and Model Specialization

Local deployment becomes more attractive when hosted model and bandwidth costs
dominate the product economics. Affordable GPUs, open-source models, and
low-latency inference providers make local or near-local serving part of the
deployment spectrum
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]).
That deployment choice belongs with
[[llm-cost-optimization=>LLM cost optimization]]
when the team compares hosted API calls, bandwidth, local hardware, and smaller
specialized models.

Teams use task-focused models when a known workflow needs faster serving than a
general model can provide. Latency constraints can rule out agent-style
execution. Some LLM prototypes may then become classic machine-learning systems
([[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]],
[[cite:s23e07-understanding-ai-engineer-role=>Understanding the AI Engineer Role]]).

## Fine-Tuning Purpose: Specialization and Domain Adaptation

Fine-tuning is for specialization, domain adaptation, format, and tone. It's
not a substitute for [[Retrieval-Augmented Generation]] when knowledge changes.
Retrieval is the better fit for current facts and documents
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Dataset expansion can support fine-tuning when a team starts with a small set
of high-quality labeled examples and uses an LLM to generate more candidates.
The result still needs evaluation against the intended task
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Generation tasks remain harder to evaluate than classification. Human review
stays important, even when the team experiments with an LLM as a judge
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
That evaluation constraint is part of
[[llm-system-design-interview=>LLM system design interview]] practice.
Candidates have to explain how the team will test generated answers.

## Related Pages


- [[AI Infrastructure]]
- [[LLM Production Patterns]]
- [[Caching]]
- [[LLMs]]
- [[Generative AI]]
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[Production]]
- [[MLOps]]
- [[llm-system-design-interview=>LLM system design interview]]
