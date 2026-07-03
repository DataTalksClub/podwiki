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
LLM prompt. It extends [[Prompt Engineering]] beyond instruction phrasing. The
work is choosing and packaging the data the model sees.
[[person:ranjithakulkarni=>Ranjitha Kulkarni]] defines the shift in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Context engineering means being deliberate about which information reaches the
model instead of "stuffing everything in" [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|28:52]].

The topic connects [[retrieval-augmented-generation=>RAG]], [[Embeddings]],
[[Agent Engineering]], and [[LLM Production Patterns]]. Retrieval pipelines
engineer context by selecting passages. Agents engineer context by exposing
tools, memory, examples, and state only when the task needs them.

## Reducing Noise

Recent LLM episodes keep returning to the same constraint: larger context
windows don't remove the need for selection. Ranjitha argues that noisy prompts
increase latency and cost. They also create a garbage-in/garbage-out failure
mode. Even with 32k-token windows, she recommends preprocessing and sending a
smaller context when reliability matters [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|30:27]].

[[person:hugobowneanderson=>Hugo Bowne-Anderson]] makes a similar point in
[[podcast:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
through context rot. Long prompts can reduce precision and relevance. Important
instructions may need prominent placement at both the beginning and end of the
prompt [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG|46:39]].
For context engineering, "more context" isn't automatically safer. The useful
work is deciding what deserves attention.

## Long-Context Boundaries

[[person:lavanyagupta=>Lavanya Gupta]] adds evaluation evidence from financial
LLM benchmarking. In
[[podcast:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research & Career Growth]],
she says her team split long-context tests below and above 32k tokens. They saw
a clear dip around that boundary. Those specialized domains also exposed
pitfalls that public benchmarks can hide [[cite:applied-llm-research-and-career-growth-in-practice|Applied LLM Research & Career Growth|12:36]].

At the bank, the practical response was still to chunk large inputs before
downstream processing. The team kept doing this even when they used models
advertised with much larger windows [[cite:applied-llm-research-and-career-growth-in-practice|Applied LLM Research & Career Growth|14:54]].

This supports the same production instinct as Ranjitha's RAG discussion.
Long-context models can help, but teams still need retrieval or preprocessing
when the material is large. Summarization can help when the material is
specialized or hard to verify.

## Chunking and Source Structure

Chunking is the most visible context engineering technique, but Hugo stresses
that it depends on the data structure. For podcast transcripts, he suggests
question-and-answer pairs or speaker turns. For multi-person conversations,
topic-based chunks may work better. For unfamiliar material, the first step is
to look at the raw source rather than assume one universal split [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG|45:01]].
His pragmatic starting point is fixed-length chunks, then refinement based on
observed failures [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG|48:57]].

Ranjitha adds that length-based chunking is often lossy unless each chunk has
the surrounding context. The model needs the source document, the question the
chunk helps answer, and what the system has already learned [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|32:48]].
That connects chunking to [[Embeddings]] and [[retrieval-augmented-generation=>RAG]]:
retrieval quality depends not only on vector similarity. It also depends on
whether the retrieved unit is self-contained enough for the model to use.

## Metadata, Wrappers, and Tools

Context engineering also includes the wrapper around retrieved information.
Ranjitha describes wrappers as structures that present chunks in a form the LLM
can use. She also treats tool lists and prior problem-solving examples as
context that influences the output [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|34:02]].

For [[Agent Engineering]], context can include tools, API affordances and memory
alongside source metadata, user state and similar-problem history.

That framing also explains why search isn't always the whole answer. Ranjitha
describes search and information retrieval as tools an agent may use when needed,
not a flow to apply everywhere [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|35:09]].

## RAG, Agents, and Scope

The boundary between RAG and agents is a context decision. Hugo's edtech example
shows a restrained RAG use case. Instead of building an all-purpose tutor, a
team could use a simple RAG bot with good chunking and embeddings.

That bot could answer common support questions and solve a meaningful share of
tickets quickly. One example was "which class contained a lesson" [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG|44:26]].

Ranjitha draws the line similarly. RAG fits large search spaces and simple
question answering over many documents. When the task depends on current state
or dynamic planning, context engineering becomes part of agent orchestration.
The same shift happens when the system needs multiple data sources or API
integrations [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems|38:13]].

Hugo's advice is to add tool calls only when the simpler RAG path can't answer
the user's question. Tools increase both power and system complexity [[cite:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG|51:10]].

## Related Pages

These pages cover the surrounding LLM engineering topics.

- [[Agent Engineering]]
- [[retrieval-augmented-generation=>RAG]]
- [[LLM Production Patterns]]
- [[Prompt Engineering]]
- [[Embeddings]]
- [[long-context-llm-evaluation=>Long-Context LLM Evaluation]]
