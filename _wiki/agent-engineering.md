---
layout: wiki
title: "Agent Engineering"
summary: "How the podcast archive frames AI agents through tools, planning, retrieval, evaluation, workflow design, and production constraints."
related:
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - Generative AI
  - LLMs
  - MLOps and DataOps
---

## Definition and Scope

Agent engineering designs AI systems that use models to pursue goals, call
tools, maintain context, and act on behalf of a person or team. In the archive,
agents aren't only chatbots. They include on-call assistants, productivity
assistants, coding agents, multi-agent support systems, and email assistants.

Use [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
for the larger production hub. This bridge keeps the agent-specific evidence
together for linked topic slugs.


## Recurring Archive Themes

Agents need a reason to be agents. The archive distinguishes knowledge
lookup from agentic workflows. If the system mainly answers from documents, RAG
may be enough. Agents become useful when the task requires planning, tool use,
dynamic state checks, or action.

Tool design is part of the product. Agents depend on tool wrappers, APIs,
memory, knowledge stores, protocols, and integration boundaries. Poor tool
design makes the model reason over noisy or unusable context. Good tool design
gives the agent constrained actions, traceable inputs, and outputs that teams can
test.

Context engineering is a core agent skill. Agent systems need deliberate inputs
such as retrieved chunks, metadata, summaries, tool outputs, and task state. Long
context doesn't remove this work. Guests keep returning to chunk metadata,
wrappers, and retrieval as a tool that agents can call when they need external
information.

Evaluation should check outcomes, not only paths. Agent evaluation is harder
than answer evaluation because multiple tool-call paths may be valid. The
archive references custom datasets, system benchmarks, mocked tools, integration
tests, regression tests, and goal-based assertions. For enterprise agents,
guardrails, auditability, lineage, feedback loops, and human review also matter.

## Episode Evidence

These episodes provide the strongest evidence for this bridge page.

- [Building Agentic AI Systems](https://datatalks.club/podcast.html): The 11:00
  and 12:31 clips define agents through autonomy, objectives, LLMs, tools,
  memory, and knowledge stores. The 15:10 and 21:21 clips compare planning
  strategies and introduce context engineering. The 36:11, 51:17, and 56:02
  clips connect retrieval tools with custom datasets, benchmarks, and goal-based
  evaluation.
- [Practical LLM Engineering and RAG](https://datatalks.club/podcast.html): At
  33:14, covers embedded agents in workflows. At 40:12, moves beyond chat to
  actions, documents, and automation. At 50:19, discusses when to add tooling
  and agent capabilities. At 56:21, gives a four-step agent framework. At 57:41,
  compares retrieval-based memory with multi-turn memory.
- [From Game AI to Modern AI Agents](https://datatalks.club/podcast.html): At
  10:00, connects early LLM work to the rise of agents. At 20:57, emphasizes
  minimalism and task decomposition. At 23:48, compares sequential flows with
  manager-agent work. At 31:31, covers OpenAI Agent SDK and MCP integration. At
  57:39, discusses evaluation and monitoring tools.
- [The Future of AI Agents](https://datatalks.club/podcast.html): Early sections
  connect agents to LLM economics, responsible deployment, and product impact.
  Later sections support enterprise guardrails, auditability, lineage, and
  feedback-loop framing.
- [Production AI Engineering](https://datatalks.club/podcast.html): At 42:05,
  covers coding assistants. At 47:19, positions search-focused AI assistants as
  research and retrieval aids.

## Related Pages

Use these pages for deeper treatment of nearby topics.

- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Generative AI]({{ '/wiki/generative-ai/' | relative_url }})
- [LLMs]({{ '/wiki/llms/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [MLOps and DataOps]({{ '/wiki/mlops-and-dataops/' | relative_url }})
