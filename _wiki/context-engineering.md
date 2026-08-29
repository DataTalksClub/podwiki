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
tools, memory, examples, and state only when the task needs them. Use
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] when those
context choices become rollout milestones.

## Reducing Noise

Recent LLM episodes keep returning to one constraint: larger context windows
don't remove the need for selection. Noisy prompts increase latency and cost,
and they create garbage-in/garbage-out failures. Preprocessing still matters
even with 32k-token windows because a smaller context can improve reliability.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Teams sometimes keep a stable prompt prefix or retrieved block after selection.
In those cases [[caching]] can reduce repeated LLM work without changing what
the model receives. The cost and latency tradeoff is also a
[[llm-deployment=>LLM Deployment]] concern.
[[cite:production-ready-ai-engineering=>Production AI Engineering]]

Context rot describes how long prompts can reduce precision and relevance.
Important instructions may need prominent placement at both ends of the
prompt.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
For context engineering, "more context" isn't automatically safer. Engineers
still decide what deserves attention.

[[person:pauliusztin=>Paul Iusztin]] describes a personal second brain as the context layer that makes
an assistant useful. The durable advantage is not a particular model; it is the
selection, source quality, and maintenance boundary around the material the
model receives. His practical constraint is to let that layer grow organically
without turning curation into a second full-time task.[[cite:s24e09-engineering-your-own-ai-assistant@15:17=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@16:15=>Engineering Your Own AI Assistant]]

For a writing or coding task, he starts with a Markdown brain dump, retrieves
and reranks relevant resources, then builds a small project wiki rather than
passing the entire corpus to the agent. The wiki is a progressive-disclosure
boundary: it keeps source relationships available while exposing only the
subset needed for the current question. Resource counts and graph size in this
example are personal heuristics, not context-window requirements.[[cite:s24e09-engineering-your-own-ai-assistant@26:34=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@28:19=>Engineering Your Own AI Assistant]][[cite:s24e09-engineering-your-own-ai-assistant@35:24=>Engineering Your Own AI Assistant]]

Hugo Bowne-Anderson connects context rot to chunking strategy. Fixed-length
chunks are a fast starting point, while sliding windows can preserve continuity
across boundaries. Neither choice is complete until the team reviews the
failures. The chunking rule should change when retrieval misses the useful
passage or when the model receives too much distracting context.
[[cite:practical-llm-engineering-and-rag@48:20=>Chunking and Context Rot]]

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
[[LLM Evaluation Workflows]].
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Large-Document LLM Strategy]]

## Chunking and Source Structure

Chunking is visible in context engineering. Teams choose units that match the
data structure.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Podcast transcripts can use question-and-answer pairs or speaker turns, while
multi-person conversations may work better with topic-based chunks. Look at the
raw source before choosing one split rule.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Start with fixed-length chunks, then refine based on observed failures.
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Chunk overlap belongs in the same decision because references can cross chunk
boundaries. If a retrieved chunk says "they" or "that result" without its
neighboring context, the model may receive a similar but unusable passage.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript Chunking]]

A chunk is lossy when it drops surrounding context.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
Useful chunks keep source context, target questions, and current findings.
That connects chunking to [[Embeddings]] and [[retrieval-augmented-generation=>RAG]]:
retrieval quality depends not only on vector similarity. It also depends on
whether the retrieved unit is self-contained enough for the model to use.

## Metadata, Wrappers, and Tools

Context engineering also includes the wrapper around retrieved information.
Wrappers present chunks in a form the LLM can use. Tool lists and prior
problem-solving examples are also context that influences the output.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Repository files, error messages, and nearby tests become context in
[[ai-coding-tools=>AI coding tools]]. Better context selection changes the
quality of the generated diff.
[[cite:production-ready-ai-engineering=>Production AI Engineering]]
In [[ai-engineering-portfolio-projects=>AI Engineering Portfolios]], those
artifacts show which context the system selected and why.

For [[Agent Engineering]], context can include tools and API affordances. It can
also include memory, source metadata, user state, and similar-problem history. The
[[game-ai-to-llm-agents=>Game AI to LLM Agents]] bridge is useful here because
game AI makes state and actions explicit. It also treats feedback and
environments as part of the design. Those ideas reappear as tool lists,
scratchpads, and task state in LLM agents.
[[cite:from-game-ai-to-modern-ai-agents=>From Game AI to LLM Agents]]

Search isn't always the whole answer. Search and information retrieval are tools
an agent may use when needed, not a flow to apply everywhere.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Memory adds another context boundary. Retrieval memory stores facts or
documents the system can look up later. Conversation memory decides
what from the interaction history should remain active. Many single-turn
systems don't need either one. Add memory only when the task requires durable
user, document, or workflow state.
[[cite:practical-llm-engineering-and-rag@57:41=>Agent Memory Design]]

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
needs multiple data sources, API integrations, or
[[multi-agent-systems=>Multi-Agent Systems]].[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Knowledge management is the hard part of many AI engineering systems. The team
has to model knowledge so an agent or RAG system can access it. Chunks,
metadata, a knowledge graph, or another retrieval layer can provide that context.
[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products@29:12=>AI Engineering Skill Stack]]

Tool calls fit when the simpler RAG path can't answer the user's question.
Tools increase both power and system complexity.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Hugo recommends starting with a useful RAG path before adding tools for current
state, external APIs, or actions. That keeps [[Agent Engineering]] from becoming
the default answer for every retrieval problem.
[[cite:practical-llm-engineering-and-rag@50:19=>From RAG to Tool Calls]]
The same RAG-to-tools ordering appears in
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].

## Related Pages

Adjacent context decisions affect agents and retrieval. They also affect
production paths, prompts, embeddings, and long-context evaluation.

- [[Agent Engineering]]
- [[retrieval-augmented-generation=>RAG]]
- [[LLM Production Patterns]]
- [[Prompt Engineering]]
- [[Embeddings]]
- [[long-context-llm-evaluation=>long-context LLM evaluation]]
