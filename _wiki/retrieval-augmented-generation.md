---
layout: wiki
title: "Retrieval-Augmented Generation"
summary: "RAG architecture across retrieval, context design, generation, citation, and system boundaries."
related:
  - LLM Production Patterns
  - Search
  - Vector Databases
  - Embeddings
  - Graph RAG vs Vector RAG
  - Knowledge Graph vs Vector Search
  - Multimodal LLMs
  - LLM Evaluation Workflows
  - Long-Context LLM Evaluation
  - RAG Evaluation Workflow
  - Search and RAG Project Checklist
  - RAG Portfolio Projects
  - Text-to-SQL
---

RAG, short for retrieval-augmented generation, is an LLM application design
where the system searches external knowledge before asking the model to answer.
It starts with [[search=>Search]] and
[[information-retrieval=>information retrieval]]. Teams use
[[search-relevance=>search relevance]] to keep retrieved material useful. They
then use [[context-engineering=>Context engineering]], generation, citation, and
[[llm-evaluation-workflows=>LLM evaluation]] to turn that material into a
verifiable answer.

The architecture depends on search quality and chunk design. Embeddings and
prompt construction influence the answer, while citations and review affect
whether readers can trust it.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Use this hub for the concept and architecture patterns. For project examples and
hiring proof, use [[RAG Portfolio Projects]]. For review fields on one
implementation, use the [[Search and RAG Project Checklist]]. For measurement
runs, labels, and traces, use
[[rag-evaluation-workflow=>RAG Evaluation Workflow]]. For learning and rollout
sequence, use the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].

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
evidence correctly.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>RAG Prompt Design and Citations]]

Retrieval is useful when knowledge changes too often for repeated fine-tuning.
Teams index documents and retrieve relevant passages. They ground the generated
answer with those passages instead of retraining every time the facts
change.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

That boundary is central to [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] because
retrieval fits changing knowledge, source review, and citation needs.
Fine-tuning fits behavior changes, domain style, or task performance that
retrieval and prompting don't fix.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

## System Boundaries

RAG approaches differ on how much engineering should surround retrieval.
Systems centered on search treat RAG as an extension of production search.
Retrieval quality, context design, citations, and human review all matter.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]

Practical LLM systems often use RAG as an early business win when the knowledge
base, chunking strategy, and embedding setup fit the task. Applications move
toward [[agent-engineering=>agent engineering]] when they need actions, API
calls, or multi-step coordination beyond lookup.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

RAG still has latency, cost, and context-noise limits. Retrieval can become one
tool inside a larger agentic system when the workflow needs dynamic planning.
Multiple data sources or API integrations can push the system in the same
direction.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@36:11=>Agentic RAG]]
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@37:39=>Building Agentic AI Systems]]

Large context windows can still degrade on specialized documents. In
financial-domain tests, Lavanya Gupta's team split prompts at 32k tokens. The
team still saw failures around 64k on models with larger advertised windows.
The team still uses large-document fallbacks such as chunking, retrieval, and
summarization. Those fallbacks route large documents through reliable
subproblems instead of trusting the whole window.[[cite:applied-llm-research-and-career-growth-in-practice@12:36=>Applied LLM Research]]
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Applied LLM Research]]

## Retrieval and Context Design

Chunking is part of answer quality, not just storage. In transcript and document
RAG, chunk size and overlap affect what the model receives. That makes chunking
a [[context-engineering=>context engineering]] decision as much as a storage
decision. Embedding choice, vectorization, prompt design, and citations affect
whether the reader can look at the evidence.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Modern Search Systems]]

Teams can use fixed chunks or sliding windows, and context rotation is another
option. Pronouns and references can cross chunk boundaries, so overlap helps
preserve nearby context before the model generates an answer.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript RAG Chunking]]

Teams often start with fixed chunks. Transcript structure, speaker turns, and
context rot can force a different chunking rule.[[cite:practical-llm-engineering-and-rag@48:20=>Chunking and Context Rot]]

Failure analysis separates missing or noisy retrieval from prompt and formatting
problems before a team changes the generator.[[cite:practical-llm-engineering-and-rag=>Practical RAG]]

Long-document systems should add another separation. First test whether raw
long context still works for the domain. Then decide whether chunking,
retrieval, or summarization gives a more reliable path. That keeps RAG
connected to [[long-context-llm-evaluation=>long-context LLM evaluation]]
instead of treating retrieval as only a workaround for small context windows.
[[cite:applied-llm-research-and-career-growth-in-practice@14:54=>Applied LLM Research]]

RAG also belongs to the broader [[llm-production-patterns=>LLM production]]
skill stack. Engineers have to choose what knowledge to capture, organize it for
retrieval, and preserve provenance as context reaches the
model.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]

Webinar recordings cover the improvement loop end to end: five retrieval-side
techniques from an AWS Generative AI Innovation Center applied
scientist,[[event:xPYmClWk5O8=>Five Techniques for Improving RAG Chatbots]]
an ingestion-retrieval-generation walkthrough with chunking strategies and
query rewriting,[[event:RexNgpgwmkk=>Elevating RAG Systems]]
and production bots built on the DataTalks.Club FAQ corpus with Elasticsearch
field boosting.[[event:QhFLeZV-PVk=>How to Build an LLM-powered QA bot]][[event:q-p36Ak6YI8=>Chat with Your Own Data: Introduction to the LLM Zoomcamp]]

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
domains that need graph semantics. If similarity or link scoring selects graph
context upstream, the work belongs with [[Graph Data Science]]. The RAG decision
is whether those facts, paths, or Cypher results enter the prompt.
Those tradeoffs belong with [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]]
and [[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]].

## Evaluation Boundary

RAG evaluation splits the architecture into retrieval quality and answer quality.
A retriever can return chunks that are wrong, stale, too broad, or missing source
metadata. The generator can also misuse good evidence or overstate what the
sources support.
Multi-level evaluation keeps those failure sources separate.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@48:09=>Modern Search Systems]][[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Agentic RAG adds another boundary. Public model benchmarks don't test tool use
or integration behavior. They also don't test retrieval inside a larger agent
workflow.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

Use the [[llm-system-design-interview=>LLM system design interview]] frame for
that same decision. Decide whether retrieval alone is enough or whether the
system needs tools.
For the run sequence and gold examples, see
[[rag-evaluation-workflow=>RAG Evaluation Workflow]]. It also covers review
labels, traces, and production feedback.

Keep project evidence in the [[Search and RAG Project Checklist]] and
measurement design in [[rag-evaluation-workflow=>RAG Evaluation Workflow]].

## Production Constraints

Production RAG adds latency, cost, reliability, and maintenance work around
retrieval. Teams still need indexing jobs, embedding computation, and metadata
schemas. They also need query-time latency budgets and reindexing plans when
sources, ranking rules, or embedding models change.

These choices sit inside broader [[LLM Deployment]] tradeoffs. For prototypes,
teams can use hosted APIs, while production cases may need open-source models
for control.
Latency and cost then move into serving, hardware, and model
optimization decisions.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Long context and agents don't remove retrieval's production constraints. They
still leave latency, cost, source-quality, and context-noise problems to solve.
Agentic systems add tool integration and evaluation work when retrieval alone
can't complete the task. The system must choose tools, act on changing state, or
coordinate multiple sources.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation@37:39=>Building Agentic AI Systems]]

Use the [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] for the
sequence from assistant to RAG, evaluation, agents, and production readiness.

## Related Pages

Adjacent pages split retrieval choices, evaluation, and project evidence.

- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
- [[context-engineering=>Context Engineering]]
- [[multimodal-llms=>Multimodal LLMs]]
- [[vector-databases=>Vector Databases]]
- [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]]
- [[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]]
- [[llm-evaluation-workflows=>LLM Evaluation Workflows]]
- [[rag-evaluation-workflow=>RAG Evaluation Workflow]]
- [[Search and RAG Project Checklist]]
- [[RAG Portfolio Projects]]
- [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
