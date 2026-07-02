---
layout: wiki
title: "LLM Cost Optimization"
summary: "Token optimization, prompt compression, prompt caching, model size tradeoffs, and cost-aware engineering for production LLM systems."
related:
  - AI Infrastructure Cost and Ownership
  - LLM Production Patterns
  - LLM Deployment
  - Prompt Engineering
  - AI Engineering
---

LLM cost optimization covers the engineering techniques that reduce the expense
of running language models in production. It includes token optimization, prompt
compression, prompt caching, model size selection, and the broader discipline of
cost-aware platform design. As LLM usage scales, cost becomes a competitive
differentiator rather than just a budget concern.

[[person:bartoszmikulski|Bartosz Mikulski]] provides
the most direct treatment of these techniques in
[[podcast:production-ready-ai-engineering|Production AI Engineering]].
His 28:16 section covers prompt evaluation and cost tradeoffs, followed by
prompt compression and prompt caching as model-efficiency tools.

This topic connects to
[AI Infrastructure Cost and
Ownership]({{ '/wiki/ai-infrastructure-cost-and-ownership/' | relative_url }}),
[[LLM Production Patterns]],
and [[LLM Deployment]].

## Prompt Compression: Token Optimization

Bartosz's 30:00 section covers prompt compression techniques. The goal is to
reduce the number of tokens sent to the model without losing the instruction's
meaning. Fewer tokens mean lower cost and faster response times. He treats this
as a standard part of production AI engineering, alongside prompt evaluation and
testing.

The connection to
[[Context Engineering]] is
direct: both disciplines focus on reducing noise in the prompt. Context
engineering frames this as improving model accuracy by removing irrelevant
information. Cost optimization frames the same reduction as cutting token
expense. The techniques overlap.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] makes
a related point in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
His 46:39 discussion of context rot notes that giving too much context reduces
precision and relevance. The same principle applies to cost: excess context
wastes tokens and money while degrading output quality.

## Prompt Caching and Model Efficiency

Bartosz's 31:45 section covers prompt caching and model efficiency. He
discusses attention caching, referencing Claude's caching mechanism. Prompt
caching lets the model reuse previously computed attention states for repeated
prompt prefixes, reducing both latency and cost. This is especially valuable for
agents and multi-turn systems where the same system prompt or context is sent
repeatedly.

[[Caching]] as a concept appears across
the podcast, but LLM prompt caching is more specific: it caches the model's
internal computation, not just the final output. This makes it relevant for
systems that send long, stable prompts with varying user queries appended.

## Latency and Cost Tradeoffs

[[person:meryemarik|Meryem Arik]] covers latency and
cost tradeoffs in
[Deploying LLMs in
Production](https://datatalks.club/podcast/deploying-llms-in-production-fine-tuning-retrieval-open-source-api.html).
Her 51:35 section explains that self-hosted open-source models on smaller GPUs
or CPUs can be much faster than API calls. API models are fast because they run
on expensive hardware, but self-hosted models on comparable hardware can match or
exceed that speed at lower cost.

She frames this as a prototyping-versus-production decision. During prototyping,
API speed and ease of use win. Once the business case is proven, migrating to
open-source models reduces both cost and latency. The migration requires more
engineering effort, but tools like TitanML's Takeoff server and other inference
servers make it easier.

[[person:micheallanham|Micheal Lanham]] adds the
latency perspective in
[From Game AI to LLM
Agents](https://datatalks.club/podcast/from-game-ai-to-modern-ai-agents.html).
At 46:14, he describes using Groq as a low-latency provider offering 1-2 second
response times compared to 4-5 seconds for GPT-4. Latency directly affects cost
because longer inference times consume more compute resources and limit
throughput.

## The Competitive Advantage of Cost-Aware Engineering

[[person:slawomirtulski|Slawomir Tulski]] makes cost
awareness a competitive advantage in
[Data Engineer Career in
2026](https://datatalks.club/podcast/s23e06-data-engineer-career-in-2026-roles-specializations-and-what-companies-look-for.html).
His 25:24 section says being cost aware gives engineers "a big competitive
advantage." At 25:33, he explains that cloud bills skyrocketing is a common
industry problem because "people are not cost aware. We have this thing that our
cloud is cheap and storage is cheap but then we quickly realize it is not that
cheap as you think."

He also warns against overengineering. His 26:22 section describes companies
building "behemoth platforms" before they need them: "we are now ready for real
time and batch and we have this lakehouse thing. Now what are we going to do
with that? We are going to ingest CSVs." The lesson applies directly to LLM
cost optimization: match the model and infrastructure to the actual need, not
the aspirational one.

At 20:52 in the same episode, he connects cost awareness to hiring. He values
candidates who proactively built something to reduce cost. Cost-awareness is
not just a technical skill but a signal of engineering judgment.

## Cost Considerations in Product Patterns

[[person:sandrakublik|Sandra Kublik]] touches on cost
as a product decision in
[Practical LLM Use
Cases](https://datatalks.club/podcast/practical-llm-use-cases-and-product-patterns.html).
Her 35:28 section on proprietary versus open-source models lists cost alongside
latency, IP, and data risk as the key trade-offs. For enterprise deployment,
cost compounds at scale, making model choice and optimization a product-level
concern rather than only an engineering detail.

## Related Pages

- [[AI Infrastructure Cost and Ownership]]
- [[LLM Production Patterns]]
- [[LLM Deployment]]
- [[Prompt Engineering]]
- [[Context Engineering]]
- [[Caching]]
- [[AI Engineering]]
