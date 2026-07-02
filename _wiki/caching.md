---
layout: wiki
title: "Caching"
summary: "How DataTalks.Club guests discuss caching, prompt caching, context reuse, and model efficiency in production AI systems."
related:
  - AI Engineering
  - AI Infrastructure
  - LLM Production Patterns
  - AI Tooling
  - Production
---

Caching is the reuse of already computed work so an AI or data system can avoid
doing the same expensive step on every request. In the DataTalks.Club podcast
discussions, the clearest example is prompt caching for LLM systems. When many
calls share the same prompt prefix or model computation, teams can reduce
per-request cost and latency. Guests discuss caching alongside
[prompt engineering]({{ '/wiki/prompt-engineering/' | relative_url }}),
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and [AI infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}).

[Bartosz Mikulski]({{ '/people/bartoszmikulski/' | relative_url }}) gives the
main podcast discussion in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
At 28:16-31:45, he moves from examples and prompt evaluation to prompt
compression and prompt caching. He treats caching as a later efficiency tactic,
not a magic quality fix. Teams can use it after they understand which prompt content helps.
They also need to know which examples justify their token cost and what the
expected output should look like.

## Reusing Stable Computation

DataTalks.Club guests use caching as an efficiency tactic, not as a separate AI
discipline. Teams cache when the same stable input appears across requests. The
reused input may be a retrieval result, model state, or prompt prefix. Teams do
this to reduce repeated computation while preserving the behavior that tests and
evaluation already approved.

The LLM version appears at 29:33 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
where bigger prompts cost more because each extra example adds tokens. At
30:00, Bartosz recommends collecting evaluation data and stopping when more
examples no longer improve results. At 31:04, prompt compression and prompt
caching split into different tactics. Compression creates a shorter prompt with
the same intended behavior, while caching reuses work for repeated prompt parts.

At 31:45-33:29, the example is provider-side prompt caching that avoids sending
or paying for the same large codebase context on every coding request. Bartosz
recalls attention-value caching as a possible implementation detail. He then
says readers should check provider documentation rather than rely on their
memory.

Bartosz supports the product-level technique, but he doesn't claim one universal
provider implementation.

Two adjacent podcast discussions place caching inside broader production
decisions. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) discusses model
compression and serving efficiency at 25:26. At 51:35-52:57, she turns to
hardware, latency, and cost.

In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) explains
context engineering and RAG preprocessing at 28:17-36:41. Her 30:27 chapter
names latency and cost as reasons to reduce context before an LLM call. Together,
these episodes connect caching to [AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}),
[AI tooling]({{ '/wiki/ai-tooling/' | relative_url }}), and
[production]({{ '/wiki/production/' | relative_url }}) work rather than to a
standalone cache layer.

## Prompt Caching and Model Efficiency

Prompt caching matters when many requests share a long prefix. Coding assistants
are the example in the Bartosz discussion: the same project context may appear
again and again, while the final instruction changes. If the provider or serving
layer can reuse the stable prefix, the request may need less processing. It may
also cost less
([Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
31:45-33:29).

Prompt caching connects directly to
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}) because the
engineer chooses prompt structure, examples, and context boundaries.
At 25:13-28:16 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
Bartosz explains in-context learning through examples and JSON formatting. At
28:16-30:00, he ties those examples to evaluation and cost. A cache-friendly
prompt still has to be a good prompt: repeated wrong context only makes wrong
behavior cheaper to repeat.

Prompt compression is a neighboring tactic, but Bartosz treats it as different
from caching. Compression changes the prompt so it uses fewer tokens. Caching
keeps the useful shared part stable enough to reuse. Both belong in the same
cost-control conversation, but they create different engineering constraints.

Compression needs evaluation to prove that the shorter prompt still works.
Caching needs a prompt or context layout that creates reusable prefixes.

## System Placement

Caching belongs in the application and serving path around the model.

Teams use it in three layers:

- [AI tooling]({{ '/wiki/ai-tooling/' | relative_url }}) when a team uses
  provider prompt caching or prompt templates.
- [AI infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }}) when a
  team owns serving, batching, hardware, or model runtime optimization.
- [Production]({{ '/wiki/production/' | relative_url }}) when cached results
  affect reliability, freshness, rollback, or user-facing latency.

Meryem Arik's deployment episode supports that placement even though it isn't
primarily a caching episode. At 25:26 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she describes serving large models as difficult and connects model compression
to needing fewer GPUs. At 51:35-52:57, she compares API speed with self-hosted
models. She also compares hardware choices, cost, privacy, and long-term
performance.

Caching is one request-level tool in that serving-efficiency problem.
Compression, faster inference servers, and hardware choices sit beside it.

Caching also belongs near [RAG]({{ '/wiki/rag/' | relative_url }}) and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
because retrieved context can dominate prompt size and latency. Ranjitha
Kulkarni doesn't frame her 29:30-32:48 discussion as caching. Her context
engineering section gives the architectural reason caching often appears in RAG
systems.

Stuffing too much context into the model increases latency, cost, and noise
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})).
Teams first reduce and structure context with retrieval, chunking, metadata,
and wrappers. They can then cache stable retrieval results or stable context
blocks when the product can tolerate their freshness rules.

For data systems, Bartosz's testing sequence implies a guardrail: cache only
after correctness is visible. He starts the same production AI episode with data
trust, snapshot tests, integration tests, and testing tools at 9:05-13:14. Teams
that test first are less likely to let caching hide bad inputs.

If a data pipeline or AI feature caches intermediate results, teams still need
tests around the source data. They also need monitoring for the cached value and
the decision that consumes it.

## Optimization Tradeoffs Across Layers

Guests agree that efficiency work must serve the product rather than the
benchmark. Bartosz starts from prompt behavior and evaluation. Meryem starts
from serving and deployment control. Ranjitha starts from context quality and
workflow architecture. They all connect efficiency to latency, cost, and
reliability, but they optimize different layers.

Bartosz's tradeoff is prompt quality versus repeated token spend. At 30:00 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}),
he says teams should gather evaluation data and stop adding examples when
quality stops improving. Caching helps after that point because the team has
identified reusable prompt content that improves the result.

Meryem's tradeoff is speed of adoption versus long-term control. Teams can move
quickly with hosted APIs, but open-source or self-hosted models become
important when cost and privacy matter. They also matter when teams need
different performance or hardware choices
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
51:35-52:57). In that framing, caching isn't the first decision. It's one
optimization among several once a team knows where the model runs.

Ranjitha's tradeoff is context quantity versus context usefulness. At 30:27 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she names latency, cost, and garbage-in/garbage-out as reasons not to overload
the LLM context. Caching and retrieval meet here. Caching a large noisy context
is less useful than preprocessing and caching the smaller context the model can
reliably use.

## Latency, Cost, and Reliability

Caching can lower latency when a system reuses work instead of recomputing it.
It can lower cost because repeated LLM context and repeated model processing
can dominate per-request spend. It can improve reliability when a cache
stabilizes common paths. Without a freshness rule, the same cache can serve
stale or wrong context.

Bartosz, Ranjitha, and Meryem support a practical rule: make cost and latency
visible before optimizing. Bartosz ties prompt examples to cost at 29:33 and
evaluation at 30:00 in
[Production AI Engineering]({{ '/podcasts/production-ready-ai-engineering/' | relative_url }}).
Ranjitha ties long context to latency, cost, and noisy outputs at 30:27 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
Meryem ties deployment choices to hardware, cost, and performance at 51:35 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).

Together, these discussions treat caching as a production control rather than a
shortcut. A useful cache has a clear unit of reuse, a freshness boundary, and
evaluation that shows the cached path still produces acceptable results. Without
those, caching can make a bad AI system cheaper and faster without making it
more dependable.

## Related Pages

These pages extend the caching discussion into production LLM systems, tooling,
and infrastructure:

- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }})
- [AI Infrastructure]({{ '/wiki/ai-infrastructure/' | relative_url }})
- [AI Tooling]({{ '/wiki/ai-tooling/' | relative_url }})
- [Production]({{ '/wiki/production/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [LLM Tools]({{ '/wiki/llm-tools/' | relative_url }})
