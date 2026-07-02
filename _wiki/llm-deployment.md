---
layout: wiki
title: "LLM Deployment"
summary: "Deploying LLMs in production: open-source vs API models, serving challenges, model compression, inference optimization, model drift, and API risk."
related:
  - AI Infrastructure
  - LLM Production Patterns
  - LLMs
  - Generative AI
  - RAG vs Fine-Tuning
---

LLM deployment covers the engineering decisions required to move a language
model from prototype to a reliable production system. It includes choosing
between API-based and open-source models, managing serving infrastructure,
optimizing inference performance, and handling the risks that come with
model changes over time.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}), co-founder of
TitanML, frames the core tradeoff in
Deploying LLMs in
Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 49:44, she says that API models like GPT-3.5 or GPT-4 are best for
prototyping because they let you get to demos quickly. In the long term,
businesses tend to want open-source models for control, data privacy, cost, and
performance reasons.

This topic connects to
[AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}),
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and the [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
comparison.

## Open-Source vs API Models

The open-source versus API decision is the first deployment fork. Meryem's
49:57 section lays out the reasoning. API models let teams move fast during
prototyping. Once a business case is proven, open-source models provide
stability: "you actually know that the model is not changing under the hood."
Other advantages include data privacy, lower cost, and comparable or better
speed on available hardware.

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) adds a
production AI perspective in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
His 33:45 section discusses open-source models and tools like DeepSeek and
Perplexity. He uses Perplexity more than ChatGPT and notes that you can switch
off the search feature and use it like a standard chatbot. His experience shows
that open-source and alternative models have reached production quality for many
use cases.

[Sandra Kublik]({{ '/people/sandrakublik/' | relative_url }}) covers the
trade-off from the product side in
[Practical LLM Use Cases]({{ '/podcasts/practical-llm-use-cases-and-product-patterns/' | relative_url }}).
Her 35:28 section on proprietary versus open source models covers cost, latency,
intellectual property, and data risk. She explains that the choice depends on
the use case: for enterprise deployment with sensitive data, open-source or
self-hosted models reduce risk. For rapid prototyping, proprietary APIs are
faster.

## Serving Challenges, Compression, and Inference Optimization

Serving LLMs in production requires managing model size, compute resources, and
latency. Meryem's 25:26 section covers model size, compression, and inference
optimization. She explains that TitanML's approach involves training,
optimization, and a Takeoff server for fast inference. The goal is to make
models smaller and cheaper to run without losing quality.

Her 51:35 section on latency and cost tradeoffs adds that self-hosted models on
smaller GPUs or CPUs can be much faster than API calls on the same hardware.
Most businesses deploy on smaller GPUs or CPUs, not state-of-the-art hardware.
With good inference techniques, self-hosted models achieve comparable speeds for
much lower prices.

For the broader set of techniques that make models smaller, faster, and
cheaper to serve, see
[Model Optimization]({{ '/wiki/model-optimization/' | relative_url }}).

## Model Drift and API Risk

Model drift is a production risk specific to API-based models. Meryem's 18:46
section explains the problem: API providers can change the model under the hood
without notice. This creates hidden model changes that affect production output.
She describes this as a key reason businesses move to open-source models: with a
self-hosted model, "you actually know that the model is not changing under the
hood."

[Nasser Qadri]({{ '/people/nasserqadri/' | relative_url }}) connects this to
evaluation in
Understanding the AI Engineer
Role]({{ '/podcasts/s23e07-understanding-ai-engineer-role/' | relative_url }}).
His 53:22 section discusses monitoring agent performance using concepts like
data drift and concept drift from [MLOps]({{ '/wiki/mlops/' | relative_url }}).
He expects AI engineering to adopt these monitoring practices as the field
matures.

## Local Models and Model Specialization

[Micheal Lanham]({{ '/people/micheallanham/' | relative_url }}) describes the
local model trend in
[From Game AI to LLM
Agents]({{ '/podcasts/from-game-ai-to-modern-ai-agents/' | relative_url }}).
At 45:40, he says people will want models running locally because paying for
hosted models and bandwidth gets expensive. GPUs are becoming affordable enough
for self-hosting. At 46:14, he describes working with open-source large models
and low-latency providers like Groq, which offers 1-2 second latency compared to
4-5 seconds for GPT-4.

His 48:40 section on model specialization adds that smaller, task-focused models
are emerging. Most current models are general-purpose, but future models will be
more efficient and specialized. This trend directly affects deployment
architecture: specialized models can run on smaller hardware and serve specific
tasks faster.

Nasser's 56:10 section makes a related point about latency. He notes that
autonomous cars cannot run on agents due to latency constraints, and that some
patterns discovered through LLM prototyping may eventually be converted to
traditional machine learning models for speed. This suggests a deployment
spectrum from general LLMs to specialized small models to classic ML.

## Fine-Tuning Purpose: Specialization and Domain Adaptation

Meryem's 26:30 section covers fine-tuning purpose. Fine-tuning is for
specialization, domain adaptation, and tone control. It is not a substitute for
[retrieval]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) when
the knowledge changes. She explains that dealing with changing knowledge should
use retrieval over continuous retraining. Fine-tuning adapts the model to a
domain or style; retrieval grounds it in current, accurate information.

Her 33:32 section adds dataset expansion as a fine-tuning technique. Starting
with a small set of gold-standard, high-quality labeled data, teams can use an
LLM to generate more examples. This approach yielded good results in TitanML's
GPTeacher benchmark, where LLM-augmented data performed comparably to
hand-labeled data at much lower cost.

For evaluation of deployed models, Meryem's 56:39 section notes that generation
tasks are harder to evaluate than classification. Her team measures output
quality by hand, which is the most reliable method they found. They recommend
hand-evaluating at least some outputs and potentially using an LLM as a judge,
though a human in the loop remains essential for production systems.

## Related Pages

- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [MLOps]({{ '/wiki/mlops/' | relative_url }})
