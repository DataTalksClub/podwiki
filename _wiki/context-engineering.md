---
layout: wiki
title: "Context Engineering"
summary: "Designing effective LLM inputs: chunking strategies, metadata, wrappers, context windows, and context rot, grounded in DataTalks.Club podcast discussions."
related:
  - Agent Engineering
  - Retrieval-Augmented Generation
  - LLM Production Patterns
  - Prompt Engineering
  - Embeddings
  - AI Engineering
  - LLMs
---

Context engineering is the deliberate design of what information goes into an
LLM prompt. It extends [[Prompt Engineering]] beyond instruction phrasing.
Engineers choose and package the data the model sees.
Context engineering means being deliberate about which information reaches the
model instead of "stuffing everything in."[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

The topic connects [[retrieval-augmented-generation=>RAG]], [[Embeddings]],
[[Agent Engineering]], and [[LLM Production Patterns]]. Retrieval pipelines
engineer context by selecting passages. Agents engineer context by exposing
tools, memory, examples, and state only when the task needs them.

## Reducing Noise

Recent LLM episodes keep returning to the same constraint: larger context
windows don't remove the need for selection. Noisy prompts increase latency and
cost. They also create a garbage-in/garbage-out failure mode. Even with
32k-token windows, preprocessing and sending a smaller context can matter for
reliability.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Context rot describes how long prompts can reduce precision and relevance.
Important instructions may need prominent placement at both ends of the
prompt.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
For context engineering, "more context" isn't automatically safer. Engineers
still decide what deserves attention.

## Long-Context Boundaries

Financial LLM benchmarking adds evaluation evidence for the same boundary.
Long-context tests split below and above 32k tokens showed a clear dip around
that boundary. The same specialized-domain tests exposed pitfalls that public
benchmarks can hide.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research & Career Growth]]

At the bank, the practical response was still to chunk large inputs before
downstream processing. The team kept doing this even when they used models
advertised with much larger windows.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research & Career Growth]]

Long-context models can help, but teams still need retrieval or preprocessing
when the material is large. Summarization can help when the material is
specialized or hard to verify.

## Chunking and Source Structure

Chunking is visible in context engineering. Teams choose units that match the
data structure.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Podcast transcripts can use question-and-answer pairs or speaker turns, while
multi-person conversations may work better with topic-based chunks. For
unfamiliar material, look at the raw source before choosing a universal
split.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

A pragmatic starting point is fixed-length chunks, then refinement based on
observed failures.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

A chunk is lossy when it drops surrounding context.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Useful chunks keep source context, target questions, and current findings.
That connects chunking to [[Embeddings]] and [[retrieval-augmented-generation=>RAG]]:
retrieval quality depends not only on vector similarity. It also depends on
whether the retrieved unit is self-contained enough for the model to use.

## Metadata, Wrappers, and Tools

Context engineering also includes the wrapper around retrieved information.
Wrappers present chunks in a form the LLM can use. Tool lists and prior
problem-solving examples are also context that influences the output.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

For [[Agent Engineering]], context can include tools, API affordances and memory
alongside source metadata, user state and similar-problem history.

Search isn't always the whole answer. Search and information retrieval are tools
an agent may use when needed, not a flow to apply everywhere.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## RAG, Agents, and Scope

The boundary between RAG and agents is a context decision. A restrained edtech
RAG use case doesn't need to become an all-purpose tutor. A team could use a
simple RAG bot with good chunking and embeddings.

That bot could answer common support questions and solve a meaningful share of
tickets quickly. One example was "which class contained a lesson."[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

RAG fits large search spaces and simple question answering over many documents.
When the task depends on current state or dynamic planning, context engineering
becomes part of agent orchestration. The same shift happens when the system
needs multiple data sources or API integrations.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Tool calls fit when the simpler RAG path can't answer the user's question.
Tools increase both power and system complexity.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

## Related Pages

These pages cover the surrounding LLM engineering topics.

- [[Agent Engineering]]
- [[retrieval-augmented-generation=>RAG]]
- [[LLM Production Patterns]]
- [[Prompt Engineering]]
- [[Embeddings]]
- [[long-context-llm-evaluation=>Long-Context LLM Evaluation]]
