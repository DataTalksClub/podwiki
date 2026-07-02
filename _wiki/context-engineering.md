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
LLM prompt. It is a reframing of
[Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }}) that shifts
attention from instruction phrasing to the selection, structure, and packaging of
the data the model sees. Where prompt engineering asks how to write instructions,
context engineering asks what context to provide and how to shape it so the model
can use it well.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) introduces
the term in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 27:59, she calls it "more of a rephrasing or rewording of the whole thing so
that you look at it from a different perspective." At 28:52, she frames context
engineering as a subfield of prompt engineering focused on being "more deliberate
about what information you give the LLM rather than stuffing everything in."

The topic sits at the intersection of
[RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}). Every
retrieval pipeline, agent memory design, and production prompt strategy touches
it.

## The Noise Problem and Garbage-In, Garbage-Out

The core motivation for context engineering is that LLMs degrade when given too
much irrelevant information. Ranjitha's 29:30 section makes this explicit: "it
is latency, it is cost, and it is also garbage in, garbage out. If you put a lot
of noise in, then your model only has so much to work with." She notes that
models have become more capable and can fill a 32k context window, but "beyond
that, many models don't do very well." Reducing the context window so the LLM
isn't burdened with runtime processing is the starting point.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) makes
the same point through the concept of context rot in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 46:39, he references Jeff Huber and the Chroma team's essay on context rot:
"giving too much context can reduce precision and relevance." He illustrates it
with a concrete observation: when processing a long transcript, the model
reformats things nicely at the start but "by the end it gets sloppy." His advice
at 47:26 is practical: "if something is really important, say it at the start of
your prompt and repeat it at the end."

## Context Window Limits and the 32k-64k Performance Drop

[Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }}) provides empirical
evidence on context window performance in
[Applied LLM Research & Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}).
Her team at JP Morgan benchmarked long-context LLMs on financial concepts. At
12:36, she reports "a clear dip" around the 32k token boundary. They split
evaluations into less than 32k tokens and greater than 32k tokens. She adds that
public benchmarks tend to use artificially simplified tasks, but real-world
specialized domains like finance and healthcare expose the pitfalls of longer
contexts more sharply.

This finding aligns with Ranjitha's practical observation that many production
use cases stay within 32k tokens and that pushing the boundary to 128k degrades
reliability. Lavanya's published work at EMNLP, "Long Context LLMs on Financial
Concepts," documents this systematically.

## Chunking Strategies

Chunking is the most direct context engineering technique: breaking documents
into pieces that fit the model's attention and the retrieval pipeline.

Hugo's 45:01 section in his episode gives a data-driven approach. He says
chunking "depends entirely on the structure of the content." For a podcast
transcript, chunking by question-and-answer pairs or speaker turns makes sense.
For five-person conversations, chunking by topic might be better. He advises
studying the raw data: Zoom provides closed captions without names and a full
transcript with speaker names, and the richer version is more useful for
chunking. His practical starting point at 48:57 is "fixed character-length
chunks" refined from there, noting that "more complex methods often
overcomplicate things."

Ranjitha's 32:48 section adds the metadata layer. She explains that breaking a
document into 200-line chunks is "almost always lossy." The engineering work is
embedding context into each chunk: which document it comes from, what question
it tries to answer, and what has been learned so far. She also describes
wrappers that present information in a way that is "more conducive for the LLM to
understand." At 34:02, she adds that agents can be influenced by showing
available tools and past problem-solving examples, all of which shape the output
through context rather than instructions.

## Metadata, Wrappers, and Context Shaping

Beyond chunking, context engineering includes the structures that frame the
retrieved information for the model. Ranjitha's 32:48 section names three
elements: the chunk itself, metadata about the chunk, and a wrapper that
presents the information. The wrapper might format retrieved passages with
headers, indicate source documents, or add task-specific context.

This connects to [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
because agents use context engineering not only for retrieval results but also
for tool descriptions, past examples, and reasoning traces. Ranjitha at 35:09
frames search and information retrieval as tools themselves, used when needed
rather than applied everywhere.

## When to Retrieve and When to Avoid It

A key context engineering decision is whether to retrieve at all. Hugo's 44:26
section gives a practical example. An edtech company wanted an all-purpose AI
tutor, but their support tickets revealed that 20% were simple questions like
"which class is this lesson in?" A simple
[RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) bot with good chunking and embeddings
could solve one in five support tickets immediately. That is less flashy than a
moonshot tutor but delivers real business value. The lesson is that context
engineering should match the actual information need, not the aspirational one.

Ranjitha's 38:13 section adds the boundary between RAG and agents. RAG works
well when the search space is large and the task is simple, like finding an
answer in millions of documents. It is less good when context matters
dynamically, like time of day or current state. When problems involve multiple
data sources, dynamic planning, or multiple API integrations, the system moves
toward agents, and context engineering becomes part of tool selection and
orchestration.

## Related Pages

- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
- [RAG]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Prompt Engineering]({{ '/wiki/prompt-engineering/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Long-Context LLM Evaluation]({{ '/wiki/long-context-llm-evaluation/' | relative_url }})
