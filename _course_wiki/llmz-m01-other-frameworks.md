---
title: "Other Frameworks — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=4yiCbKX9RhI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Other Frameworks"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Other Frameworks

## Notes

---
video_url: "https://www.youtube.com/watch?v=4yiCbKX9RhI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Other Frameworks

The concepts you learned in Part 2 are the same across frameworks.
Function calling, the agent loop, and tool definitions all wrap the
same pattern. Send messages, run any function calls, and repeat until
the model is done.

You now understand how the loop works. So you can pick up any
production framework and know what it's doing under the hood. I kept
this module framework agnostic on purpose, so you can explore and pick
the one you like.

Here are some frameworks worth a look:

## OpenAI Agents SDK

The official SDK from OpenAI for building agents. It uses the same
Responses API we used throughout this module. It supports tool
definition, multi-turn conversations, and handoffs between agents.

```bash
uv add openai-agents
```

Good choice if you're already using OpenAI and want something
official and well-maintained.

## PydanticAI

A type-safe agent framework that supports multiple LLM providers.
Tools are plain Python functions with type hints, no wrappers needed.
Switching providers is as simple as changing the model string.

```bash
uv add pydantic-ai
```

This is my personal favorite. The reason isn't the type safety, since
the other frameworks have that too. It's how it feels to use, and the
team behind Pydantic. Good choice if you want type safety and
multi-provider support.

## LangChain / LangGraph

A popular framework with lots of integrations. LangChain handles the
basics, and LangGraph adds graph-based workflows for more complex
agent patterns.

Good choice if you need lots of integrations (vector stores, document
loaders, etc.) and a large community.

## Google ADK

The Agent Development Kit from Google. If you plan to use Gemini
models, this is the one I'd reach for. It exposes the same building
blocks we've seen, like tools, instructions, and sessions. It also
integrates with Google Cloud.

Good choice if your stack is on Google Cloud or you specifically want
Gemini.

## Others

Other frameworks worth knowing:

- CrewAI - multi-agent orchestration
- AutoGen - multi-agent conversations from Microsoft
- Semantic Kernel - from Microsoft, supports C# and Python
- Smolagents - lightweight agent framework from HuggingFace
- Anthropic Tool Use - Anthropic's native tool use API

Pick one that fits your stack and your needs. The hard part is
designing good tools and prompts - the loop is always the same.

## Avoiding agents when you can

One closing thought. You don't always need an agent, and that's fine.
You might assume your app needs one, but often it doesn't.

Adding an agent is a real cost:

- More API calls per request, since the loop can fire many tool calls
  before the model is satisfied.
- Higher latency, since each round-trip waits on the model.
- More money spent, since every iteration is another billed call and
  the full message history is re-sent each turn.
- More moving parts, since you now monitor cost, iteration count, and
  whether the agent is going in circles.
- Less predictable behavior, since the LLM decides what to do and two
  runs of the same prompt can take different paths.

Before reaching for an agent, ask whether the problem needs one. A lot
of tasks are well served by simpler approaches.

Reach for one of these first:

- plain RAG, with one search and one answer
- parsing or templating a document into another form
- a single LLM call with no tools

Try the simpler approach first, and if it works, ship it. Reach for
the agent loop only when you've tried the simpler solution and it
genuinely can't handle the problem. By then you'll know the extra
complexity is worth it, and you'll be ready to take it on.

## Key concepts

- [Function Calling](/course-wiki/function-calling/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)

## Sources

- [Video](https://www.youtube.com/watch?v=4yiCbKX9RhI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/16-other-frameworks.md)
