---
layout: wiki
title: "Context Engineering"
summary: "Designing effective LLM inputs with chunking strategies, metadata, wrappers, context windows, and context rot."
related:
  - Agent Engineering
  - Retrieval-Augmented Generation
  - LLM Production Patterns
  - Prompt Engineering
  - Embeddings
  - Long-Context LLM Evaluation
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

Hugo Bowne-Anderson connects context rot to chunking strategy. Fixed-length
chunks are a fast starting point, while sliding windows can preserve continuity
across boundaries. Neither choice is complete until the team reviews the
failures. The chunking rule should change when retrieval misses the useful
passage or when the model receives too much distracting context
[[cite:practical-llm-engineering-and-rag@48:20=>Chunking and Context Rot]].

## Long-Context Boundaries

Financial LLM benchmarking adds evaluation evidence for the same boundary.
Long-context tests split below and above 32k tokens showed a clear dip around
that boundary. The same specialized-domain tests exposed pitfalls that public
benchmarks can hide.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research & Career Growth]]

At the bank, the practical response was still to chunk large inputs before
downstream processing. The team kept doing this even when they used models
advertised with much larger windows.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research & Career Growth]]

Long-context models can help while teams still use retrieval or preprocessing
for large material. Summarization can help when the material is specialized or
hard to verify.
Lavanya explicitly names chunking, retrieval, and summarization as fallbacks
instead of sending the whole document blindly. The team needs evidence for when
each path is reliable. That puts long-context work next to
[[long-context-llm-evaluation=>long-context LLM evaluation]] and
[[LLM Evaluation Workflows]]
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Large-Document LLM Strategy]].

## Chunking and Source Structure

Chunking is visible in context engineering. Teams choose units that match the
data structure.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Podcast transcripts can use question-and-answer pairs or speaker turns, while
multi-person conversations may work better with topic-based chunks. Look at the
raw source before choosing one split rule
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

Start with fixed-length chunks, then refine based on observed failures
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Chunk overlap belongs in the same decision because references can cross chunk
boundaries. If a retrieved chunk says "they" or "that result" without its
neighboring context, the model may receive a similar but unusable passage
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript Chunking]].

A chunk is lossy when it drops surrounding context.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Useful chunks keep source context, target questions, and current findings.
That connects chunking to [[Embeddings]] and [[retrieval-augmented-generation=>RAG]]:
retrieval quality depends not only on vector similarity. It also depends on
whether the retrieved unit is self-contained enough for the model to use.

## Metadata, Wrappers, and Tools

Context engineering also includes the wrapper around retrieved information.
Wrappers present chunks in a form the LLM can use. Tool lists and prior
problem-solving examples are also context that influences the output.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Repository files become context in [[ai-coding-tools=>AI coding tools]]. Error
messages and nearby tests do too. Better context selection changes the quality
of the generated diff
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

For [[Agent Engineering]], context can include tools, API affordances and memory
alongside source metadata, user state and similar-problem history.

Search isn't always the whole answer. Search and information retrieval are tools
an agent may use when needed, not a flow to apply everywhere.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Memory adds another context boundary. Retrieval memory stores facts or
documents the system can look up later. Conversation memory decides
what from the interaction history should remain active. Many single-turn
systems don't need either one. Add memory only when the task requires durable
user, document, or workflow state
[[cite:practical-llm-engineering-and-rag@57:41=>Agent Memory Design]].

Use [[ai-tools-for-personal-productivity=>AI tools for personal productivity]]
when personal assistants move from one-off drafting to remembered workflows.

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

Knowledge management is the hard part of many AI engineering systems. The team
has to model knowledge so an agent or RAG system can access it. Chunks,
metadata, a knowledge graph, or another retrieval layer can provide that context
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@29:12=>AI Engineering Skill Stack]].

Tool calls fit when the simpler RAG path can't answer the user's question.
Tools increase both power and system complexity.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Hugo's sequence is conservative. Get a useful RAG path first. Add tools only
when the question requires current state, an external API, or an action. That
keeps [[Agent Engineering]] from becoming the default answer for every retrieval
problem
[[cite:practical-llm-engineering-and-rag@50:19=>From RAG to Tool Calls]].

## Related Pages

These pages cover the surrounding LLM engineering topics.

- [[Agent Engineering]]
- [[retrieval-augmented-generation=>RAG]]
- [[LLM Production Patterns]]
- [[Prompt Engineering]]
- [[Embeddings]]
- [[long-context-llm-evaluation=>long-context LLM evaluation]]
