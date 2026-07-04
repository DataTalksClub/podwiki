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

Caching reuses already computed work so an AI or data system can avoid doing the
same expensive step on every request. LLM systems show the clearest example:
many calls can share the same prompt prefix or model computation. That reuse can
reduce per-request cost and latency. Caching sits alongside
[[prompt engineering]],
[[LLM production patterns]],
and [[AI infrastructure]].

Prompt evaluation leads into prompt compression and prompt caching, which is a
later efficiency tactic rather than a quality fix. Teams can use it after they
understand the prompt content that helps and the examples that justify their
token cost. They also need a clear expected output
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

## Reusing Stable Computation

Caching is an efficiency tactic, not a separate AI discipline. Teams cache when
the same stable input appears across requests. That input might be a retrieval
result, model state, or prompt prefix. Teams reduce repeated computation while
preserving the behavior that tests and evaluation already approved.

Bigger prompts cost more because each extra example adds tokens. Teams collect
evaluation data and stop adding examples when results no longer improve. Prompt
compression and prompt caching are different tactics. Compression creates a
shorter prompt with the same intended behavior, while caching reuses work for
repeated prompt parts
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

Provider-side prompt caching can avoid sending or paying for the same large
codebase context on every coding request. Attention-value caching is a possible
implementation detail. Provider documentation is the authority for the exact
mechanism, and the product-level technique holds without one universal provider
implementation
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

Two adjacent discussions place caching inside broader production decisions. Model
compression and serving efficiency connect to hardware, latency, and cost
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
Context engineering for RAG names latency and cost as reasons to reduce context
before an LLM call
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Together, these connect caching to [[AI engineering]],
[[AI tooling]], and
[[production]] work rather than to a
standalone cache layer.

## Prompt Caching and Model Efficiency

Prompt caching matters when many requests share a long prefix. Coding assistants
are the example. The same project context may appear again and again while the
final instruction changes. If the provider or serving layer can reuse the stable
prefix, the request may need less processing and cost less
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

Prompt caching connects directly to
[[AI engineering]] because the
engineer chooses prompt structure, examples, and context boundaries. In-context
learning through examples and JSON formatting ties to evaluation and cost
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).
A cache-friendly prompt still has to be a good prompt: repeated wrong context
only makes wrong behavior cheaper to repeat.

Prompt compression is a neighboring but different tactic. Compression changes the
prompt so it uses fewer tokens, while caching keeps the useful shared part stable
enough to reuse. Both belong in the same cost-control conversation but create
different engineering constraints. Compression needs evaluation to prove the
shorter prompt still works, while caching needs a prompt or context layout that
creates reusable prefixes.

## System Placement

Caching belongs in the application and serving path around the model, across
three layers:

- [[AI tooling]] when a team uses
  provider prompt caching or prompt templates.
- [[AI infrastructure]] when a
  team owns serving, batching, hardware, or model runtime optimization.
- [[Production]] when cached results
  affect reliability, freshness, rollback, or user-facing latency.

The deployment discussion supports that placement. Serving large models is
difficult, and model compression connects to needing fewer GPUs. Teams also weigh
hosted API speed against self-hosted models on hardware choices, cost,
privacy, and long-term performance
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
Caching is one request-level tool in that serving-efficiency problem, beside
compression, faster inference servers, and hardware choices.

Caching also belongs near [[retrieval-augmented-generation=>RAG]]
because retrieved context can dominate prompt size and latency. Context
engineering gives the architectural reason caching often appears in RAG systems.
Stuffing too much context into the model increases latency, cost, and noise
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Teams first reduce and structure context with retrieval, chunking, metadata, and
wrappers. Then they cache stable retrieval results or stable context blocks when
the product can tolerate their freshness rules.

For data systems, the testing sequence implies a guardrail: cache only after
correctness is visible. Production AI starts with data trust, snapshot tests,
integration tests, and testing tools
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).
Teams that test first are less likely to let caching hide bad inputs. If a data
pipeline or AI feature caches intermediate results, teams still need tests around
the source data. They also need monitoring for the cached value and the decision
that consumes it.

## Optimization Tradeoffs Across Layers

Efficiency work must serve the product rather than the benchmark. The podcast
discussions start from prompt behavior and evaluation, serving and deployment
control, and context quality and workflow architecture. All connect efficiency
to latency, cost, and reliability, but they optimize different layers.

The first tradeoff is prompt quality versus repeated token spend: gather
evaluation data and stop adding examples when quality stops improving. Caching
helps after that point, once reusable prompt content that improves the result is
identified
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).

The second tradeoff is speed of adoption versus long-term control. Teams can move
quickly with hosted APIs. Open-source or self-hosted models become important when
cost, privacy, performance, or hardware choices matter
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
In that framing, caching isn't the first decision. It's one optimization among
several once a team knows where the model runs.

Teams decide how much context to send by looking at usefulness first.
Overloading the LLM raises latency and cost while creating garbage-in/garbage-out
failures
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Caching and retrieval meet here because a large noisy context is less useful
than a smaller context the model can reliably use.

## Latency, Cost, and Reliability

Caching can lower latency when a system reuses work instead of recomputing it. It
can lower cost because repeated LLM context and repeated model processing can
dominate per-request spend. It can improve reliability when a cache stabilizes
common paths, but without a freshness rule the same cache can serve stale or
wrong context.

The practical rule is to make cost and latency visible before optimizing. Prompt
examples tie to cost and evaluation
([[cite:production-ready-ai-engineering=>Production AI Engineering]]).
Long context ties to latency, cost, and noisy outputs
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Deployment choices tie to hardware, cost, and performance
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Together these treat caching as a production control rather than a shortcut. A
useful cache has a clear unit of reuse, a freshness boundary, and evaluation that
shows the cached path still produces acceptable results. Without those, caching
can make a bad AI system cheaper and faster without making it more dependable.

## Related Pages

These pages extend the caching discussion into production LLM systems, tooling,
and infrastructure:

- [[LLM Production Patterns]]
- [[AI Engineering]]
- [[AI Infrastructure]]
- [[AI Tooling]]
- [[Production]]
- [[Prompt Engineering]]
- [[LLM Tools]]
