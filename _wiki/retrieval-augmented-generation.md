---
layout: wiki
title: "Retrieval-Augmented Generation"
summary: "How DataTalks.Club podcast guests describe RAG as retrieval quality, context design, generation, citation, evaluation, and production tradeoffs."
related:
  - LLM Production Patterns
  - Search
  - Vector Databases
  - Embeddings
  - Multimodal LLMs
  - LLM Evaluation Workflows
  - RAG Evaluation Workflow
  - Search and RAG Project Checklist
  - RAG Portfolio Projects
  - Text-to-SQL
---

RAG, short for retrieval-augmented generation, is an LLM application design
where the system searches external knowledge before asking the model to answer.
It starts with [[search=>Search]] and
[[information-retrieval=>information retrieval]]. It also needs
[[context-engineering=>context engineering]], generation, citation, and
[[llm-evaluation-workflows=>LLM evaluation]] to turn retrieved material into a
verifiable answer.

Across DataTalks.Club discussions, RAG is more than one tool: search quality
and chunk design affect answer quality. Embeddings, prompt construction,
citations, and review affect whether an answer can be trusted.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

RAG mechanics and boundaries sit upstream of several practical pages.
[[RAG Portfolio Projects]] helps choose a project type, and the
[[Search and RAG Project Checklist]] helps review a scoped implementation.
[[rag-evaluation-workflow=>RAG Evaluation Workflow]]
checks retrieval and answers, while
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
orders the production sequence.
For structured analytics questions, [[text-to-sql=>Text-to-SQL]] is the
adjacent design where retrieval supplies schema or metric context before SQL
generation.

## RAG Mechanics

A RAG system prepares source material before a question arrives. Documents are
split into retrieval units and enriched with metadata. The system embeds or
indexes those units before they reach the query path. When a question arrives,
the system retrieves candidates, filters or reranks them, and adds the selected
passages to the model input. The model then answers from that
context.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

This reduces hallucination risk by forcing the generator to work from retrieved
evidence instead of only parametric memory. It still needs prompt design and
citations. Retrieval alone doesn't guarantee that the answer uses the
evidence correctly
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]].

Retrieval is useful when knowledge changes too often for repeated fine-tuning.
Teams index documents and retrieve relevant passages. They ground the generated
answer with those passages instead of retraining every time the facts
change.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

That boundary is central to [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] because
retrieval fits changing knowledge, source review, and citation needs.
Fine-tuning fits behavior changes, domain style, or task performance that
retrieval and prompting don't fix.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## Approach Differences

Approaches differ on how much engineering should surround retrieval. A
search-centered approach, represented by [[person:atitaarora=>Atita Arora]],
treats RAG as an extension of production search. Retrieval quality and context
design matter, and so do citations and human review.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

A practical LLM engineering approach treats RAG as an early business win when
the knowledge base and chunking strategy fit the task. Embedding setup has to
fit too. Applications move toward
[[agent-engineering=>agent engineering]] when they need actions, API calls, or
multi-step coordination beyond
lookup.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

RAG still has latency, cost, and context-noise limits. That's why
[[person:ranjithakulkarni=>Ranjitha Kulkarni]] is cautious about treating it as
solved. Retrieval can become one tool inside a larger agentic system.

[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@36:11=>Agentic RAG]]

RAG is enough when the main job is shrinking a large search space. Agents become
more relevant when the workflow needs dynamic planning, multiple data sources,
or API integrations.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@37:39=>Building Agentic AI Systems]]

Large context windows can still degrade on specialized documents. In
financial-domain tests, Lavanya Gupta's team split prompts at 32k tokens. The
team still saw failures around 64k on models with larger advertised windows.
The team still uses large-document fallbacks such as chunking, retrieval, and
summarization. Those fallbacks route large documents through reliable
subproblems instead of trusting the whole window.[[cite:applied-llm-research-and-career-growth-in-practice@12:36=>Applied LLM Research]]
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Applied LLM Research]]

## Retrieval and Context Design

Chunking is part of answer quality, not just storage. In transcript and document
RAG, chunk size and overlap affect what the model receives. Embedding choice,
vectorization, prompt design, and citations affect whether the reader can look
at the evidence.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]

Chunking can use fixed-length chunks, sliding windows, or context rotation.
In Atita Arora's podcast-transcript example, overlap matters because pronouns
and references can cross chunk boundaries. The ingestion strategy has to
preserve enough nearby context before the model generates an answer
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript RAG Chunking]].

Hugo Bowne-Anderson makes the same boundary practical. Start with fixed chunks,
then use transcript structure, speaker turns, and context rot to decide whether
the chunking rule should change
[[cite:practical-llm-engineering-and-rag@48:20=>Chunking and Context Rot]].

Failure analysis should separate retrieval failures from prompt or formatting
failures. Teams can then fix missing or noisy context before polishing the
prompt.[[cite:practical-llm-engineering-and-rag=>Practical RAG]]

Long-document systems should add another separation. First test whether raw
long context still works for the domain. Then decide whether chunking,
retrieval, or summarization gives a more reliable path. That keeps RAG
connected to [[long-context-llm-evaluation=>long-context evaluation]] instead
of treating retrieval as only a workaround for small context windows
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Applied LLM Research]].

RAG also belongs to the broader [[llm-production-patterns=>LLM production]]
skill stack. Engineers have to choose what knowledge to capture and how to
organize it for retrieval. They also have to preserve provenance as retrieved
context reaches the model.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

## Embeddings, Search, and Knowledge Graphs

RAG often uses vector search, but it isn't the same thing as a
[[vector-databases=>vector database]]. Vector databases such as Qdrant provide
plug-and-play vector search infrastructure. Teams can also put vectors into an
existing search stack. That choice fits when migration risk matters. Filters,
ranking requirements, or operations can also favor the current system.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Vector search uses [[embeddings=>embeddings]] to map queries and content into
comparable vectors. Hybrid search can then add filters, recency, popularity, and
business constraints to similarity. Those choices connect RAG retrieval to the
broader tradeoffs in
[[vector-search-vs-keyword-search=>Vector Search vs Keyword Search]].[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

When those representations include both images and text, retrieval becomes an
input layer for [[multimodal-llms=>multimodal LLMs]] rather than only a
text-document pipeline.

Knowledge graphs can ground answers through explicit
relationships.[[cite:knowledge-graphs-and-llms-for-automotive-rnd=>KG and LLMs]]
Cypher-driven retrieval can complement or replace nearest-neighbor chunks in
domains that need graph semantics.
Those tradeoffs belong with [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]]
and [[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]].

## Evaluation and Failure Analysis

RAG evaluation has at least two layers: retrieval quality and answer quality.
The system can fail because retrieved chunks are wrong, stale, too broad, or
missing source metadata. It can also fail because the prompt uses the evidence
badly or because the answer overstates what the sources support.

Multi-level RAG evaluation includes retrieval checks and answer
checks.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]]
Offline tests and human review are part of the same evaluation work. Gold tests
and failure categories show whether to fix retrieval, prompting, formatting, or
data preparation.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Agentic RAG needs custom datasets and system benchmarks because public model
benchmarks don't test tool use or integration behavior. They also don't test
the outcome of a retrieval step inside a larger agent workflow.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Production Constraints

Production RAG adds latency, cost, reliability, and maintenance work. Retrieval
requires indexing jobs, embedding computation, metadata schemas, and query-time
latency. Reranking and reindexing may be needed when sources, ranking rules, or
embedding models change.

These choices sit inside broader LLM deployment tradeoffs. For prototypes, teams
can use hosted APIs, while production cases may need open-source models for
control.
Latency and cost then move into serving, hardware, and model
optimization decisions.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Long context and agents don't remove retrieval's production constraints. They
still leave latency, cost, source-quality, and context-noise problems to solve.
Agentic systems add tool integration and evaluation work on top of
retrieval. Use the agentic path when retrieval alone can't complete the task.
In those cases, the system must choose tools, act on changing state, or
coordinate multiple sources.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@37:39=>Building Agentic AI Systems]]

## Related Pages

These pages cover the main design boundaries around RAG:

- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[context-engineering=>Context Engineering]]
- [[multimodal-llms=>Multimodal LLMs]]
- [[vector-databases=>Vector Databases]]
- [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]]
- [[llm-evaluation-workflows=>LLM Evaluation Workflows]]
- [[rag-evaluation-workflow=>RAG Evaluation Workflow]]
- [[Search and RAG Project Checklist]]
- [[RAG Portfolio Projects]]
- [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
