---
layout: wiki
title: "Retrieval-Augmented Generation"
summary: "How DataTalks.Club podcast guests describe RAG as retrieval quality, context design, generation, citation, evaluation, and production tradeoffs."
related:
  - LLM Production Patterns
  - Search
  - Vector Databases
  - Embeddings
  - LLM Evaluation Workflows
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

## RAG Mechanics

A RAG system prepares source material before a question arrives. Documents are
split into retrieval units and enriched with metadata. The system embeds or
indexes those units before they reach the query path. When a question arrives,
the system retrieves candidates, filters or reranks them, and adds the selected
passages to the model input. The model then answers from that
context.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

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

An agent engineering approach, represented by
[[person:ranjithakulkarni=>Ranjitha Kulkarni]], is more cautious about treating
RAG as solved. Latency and cost still matter. Noisy context and
garbage-in-garbage-out problems still matter too. Retrieval can become one tool
inside a larger agentic system.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@36:11=>Building Agentic AI Systems]]

Long-context research adds another boundary because large context windows can
still degrade on specialized documents. Chunking, retrieval, and summarization
remain useful even when a model advertises a large context
window.[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Applied LLM Research]]

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

Failure analysis should separate retrieval failures from prompt or formatting
failures. Teams can then fix missing or noisy context before polishing the
prompt.[[cite:practical-llm-engineering-and-rag=>Practical RAG]]

RAG also belongs to the broader [[llm-production-patterns=>LLM production]]
skill stack. Engineers have to choose what knowledge to capture and how to
organize it for retrieval. They also have to preserve provenance as retrieved
context reaches the model.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

## Embeddings, Search, and Knowledge Graphs

RAG often uses vector search, but it isn't the same thing as a
[[vector-databases=>vector database]]. Vector databases such as Qdrant provide
plug-and-play vector search infrastructure. Teams can also put vectors into an
existing search stack. That choice fits when migration risk, filters, ranking
requirements, or operations favor the current system.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

[[embeddings=>Embeddings]] give vector search a shared representation for
queries and content. Hybrid search adds filters and recency to similarity. It
can also encode popularity and business constraints, which connects RAG
retrieval to the broader tradeoffs in
[[vector-search-vs-keyword-search=>Vector Search vs Keyword Search]].[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]

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
- [[vector-databases=>Vector Databases]]
- [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]]
- [[llm-evaluation-workflows=>LLM Evaluation Workflows]]
