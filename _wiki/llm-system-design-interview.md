---
layout: article
tags: ["guide"]
title: "LLM System Design Interview"
keyword: "llm system design interview"
summary: "Prepare for LLM system design interviews with production patterns for RAG, agents, evaluation, safety, latency, cost, and operations."
related_wiki:
  - LLM Production Patterns
  - Retrieval-Augmented Generation
  - LLM Evaluation Workflows
  - Long-Context LLM Evaluation
  - Agent Engineering
  - AI Red Teaming
---

An LLM system design interview tests whether you can turn a language model into
a bounded product system. It doesn't test whether you can name the newest
framework.
DataTalks.Club guests keep returning to that boundary: [[person:atitaarora=>Atita Arora]]
frames [[retrieval-augmented-generation=>RAG]] around retrieval, chunking,
citations, and review [[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
[[person:hugobowneanderson=>Hugo Bowne-Anderson]] turns LLM applications into
gold tests, failure analysis, logs, and traces
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
[[person:ranjithakulkarni=>Ranjitha Kulkarni]] separates ordinary
retrieval from agent flows that need tools, memory, and outcome-based
evaluation [[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Use the broader [[machine learning system design]] page for the classical
product-first discipline. [[person:valeriybabushkin=>Valerii Babushkin]] applies
that framing in the [[Machine Learning System Design Interview]] discussion
[[cite:machine-learning-system-design-interview=>ML System Design Interview]].
For LLM-specific prompts, add context design and retrieval quality. Then cover
tool boundaries and evaluation. Include red-team cases, latency, cost, and
ownership.

## Start With The Product Boundary

Begin by saying what the system is allowed to do. A policy assistant that
answers from internal documents differs from a refund agent that can change
account state. The [[Agent Engineering]] page uses this boundary to separate a
knowledge lookup system from a tool-using agent.

Ranjitha defines agents around autonomy and objectives. She keeps orchestration
and tool use inside the design boundary. Memory and knowledge stores belong
there too
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

In an interview, ask these questions before drawing boxes:

1. Who's the user?
2. What task are they trying to complete?
3. What source of truth should the answer come from?
4. What should happen when the system is uncertain?
5. Can the system only advise, or can it call tools and change state?
6. What latency, cost, privacy, and safety limits matter?

[[person:meryemarik=>Meryem Arik]] adds hosted-model risk and API drift to that
boundary. She also covers latency, cost, and self-hosting tradeoffs
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

[[person:bartoszmikulski=>Bartosz Mikulski]] keeps production AI close to
ordinary application architecture. He covers backend integration and prompt
evaluation. He also covers caching and cost controls
[[cite:production-ready-ai-engineering=>Production AI Engineering]].

Choose the smallest system that satisfies the product boundary, then add
complexity only when the boundary requires it.

## Draw The Data And Context Path

Most LLM system design prompts need an explicit context path.

For a document-backed assistant, draw the flow before the user asks a question:

1. Ingest documents.
2. Split them into useful chunks.
3. Attach source metadata.
4. Embed or index the chunks.
5. Retrieve candidates.
6. Build model context.
7. Generate an answer.
8. Return citations.

Atita's search systems discussion grounds that sequence in chunking and
embeddings. She also covers prompts, citations, and human review
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
The [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] page
keeps the same RAG design close to source provenance and permissions. It also
covers metadata, citations, and evaluation. Use
[[Vector Database vs Search Engine]] when the interviewer asks whether semantic
retrieval belongs in a dedicated vector store or an existing search stack.

For product search, [[person:danielsvonava=>Daniel Svonava]] separates retrieval
from ranking and connects search quality to A/B tests and business outcomes
[[cite:building-production-search-systems=>Building Search Systems]].
[[person:reemmahmoud=>Reem Mahmoud]] adds hybrid search, filters, recency, and
search operations
[[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]].

Make the retriever easy to debug:

1. Store document owners, timestamps, permissions, and freshness.
2. Pick chunking rules with overlap or section boundaries.
3. Use embeddings and keyword indexes where exact terms still matter.
4. Apply metadata filters before retrieval, especially for tenant or role
   access.
5. Rerank or trim results before building model context.
6. Ask the model for grounded answers and citations.
7. Log retrieved chunks, scores, prompt version, model, answer, latency, token
   count, and feedback.

That debugging path follows Atita's RAG discussion. It also follows Hugo's
logs-and-traces view of LLM engineering
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Large-document designs need
[[long-context-llm-evaluation=>long-context LLM evaluation]] as a separate test
before the team assumes a larger context window replaces retrieval
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research]].

## Choose RAG, Fine-Tuning, Tools, Or Agents

Interview prompts often hide a design choice. The system may need retrieval,
fine-tuning, tools, or an agent.

Meryem gives the clearest boundary: retrieval fits changing knowledge better
than fine-tuning
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
The [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] page keeps fine-tuning for
behavior, style, specialized task performance, or format reliability when
prompting and retrieval don't solve the problem.

Use RAG when the answer depends on documents, policies, tickets, or transcripts
that change and should remain openable by the reader. Use fine-tuning when the
repeated problem is output behavior, domain phrasing, format reliability, or task
adaptation. Use tools when the system must query an API, fetch account state,
create a ticket, or check a calendar. Use agents when the system must pick steps
and tools inside a flow.

Ranjitha covers planning and wrappers for agentic systems. She also covers tool
integration, mocked tools, and goal-based evaluation
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Hugo starts from the problem, then adds data, evaluation, and tools only when the
flow needs action
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
In an interview, justify the simplest reliable path before adding orchestration.

## Make Evaluation Part Of The Architecture

An LLM design is incomplete if it ends at "call the model." Hugo's LLM
engineering discussion makes evaluation part of the architecture through gold
tests and representative examples. He also uses failure categories, logs, and
traces
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
The [[LLM Evaluation Workflows]] page turns that into the maintained topic hub.

Split evaluation into layers:

1. Retrieval quality: the system retrieves the right evidence.
2. Grounding: the answer stays supported by the retrieved evidence.
3. Task success: the person gets the decision, summary, or action they needed.
4. Format correctness: the system returns valid JSON, citations, or fields.
5. Safety: the system refuses, escalates, or limits unsafe requests.
6. Regression: a prompt, model, index, or tool change doesn't break known cases.
7. Product impact: the system reduces support time, improves resolution, or
   meets the product metric.

Atita covers multi-level RAG evaluation and human review
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
Ranjitha argues that agent tests should assert outcomes and tool parameters
rather than one exact internal reasoning path
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
[[person:adityagautam=>Aditya Gautam]] adds enterprise agent evaluation with
human labels and LLM judges. He also covers guardrails, lineage, and
auditability
[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]].

## Treat Safety As System Design

Prompt wording isn't the security layer. The security discussions point toward
layered controls around retrieval and tools. They also cover outputs, logging,
and human review.
[[person:mariasukhareva=>Maria Sukhareva]] grounds this in a chatbot hacking
exercise where overloaded prompts and knowledge-base retrieval expose hidden
content risks
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].
The [[AI Red Teaming]] page keeps those attack patterns close to [[security]]
and [[retrieval-augmented-generation=>RAG]].

Name the threat model:

1. Prompt injection from the user or retrieved documents.
2. Data exfiltration from prompts, tools, logs, or knowledge bases.
3. Hallucinated claims that create legal, medical, financial, or brand risk.
4. Tool misuse, such as changing account state without approval.
5. Permission leaks across tenants, roles, teams, or document groups.
6. Model, prompt, or index changes that bypass expected behavior.

Then name controls outside the model. Check permissions before retrieval, not
only after generation, following the RAG security guidance in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]. Use
least-privilege tools and validate structured outputs before downstream calls,
as in [[Agent Engineering]].

Add output validators and classifiers. Add rate limits, audit logs, red-team
regression cases, and human review. Maria's discussion covers query analysis and
layered defenses. It also covers non-LLM classifiers and human-in-the-loop review
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].

## Discuss Latency, Cost, And Operations

Make latency and cost visible. Retrieval, reranking, and tool calls all affect
the user experience. Tokens, retries, and model choice affect it too. Meryem
covers hosted APIs and open-source models. She also covers model drift, latency,
cost, and serving tradeoffs
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

Bartosz adds prompt compression and caching. He also covers prompt evaluation and
model efficiency [[cite:production-ready-ai-engineering=>Production AI Engineering]].
Ranjitha keeps tool-call latency and cost inside the agent design boundary
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

Include a cost and latency plan:

1. Start with search, templates, rules, or one model call when that meets the
   user need.
2. Use a smaller model, classifier, or deterministic parser for routing when a
   strong model is unnecessary.
3. Cache repeated answers or intermediate retrieval results when freshness
   permits it.
4. Limit prompt size with better retrieval, summarization, or context
   compression instead of sending every document.
5. Stream responses only when it improves perceived latency and doesn't hide
   unsafe intermediate behavior.
6. Track token count, model calls, tool calls, retrieval latency, reranking
   latency, cache hit rate, and cost per successful task.

Track these operational fields:

1. Request IDs.
2. Prompt versions.
3. Model versions when available.
4. Retrieved document IDs, chunk IDs, and scores.
5. Tool inputs and tool outputs.
6. Schema failures.
7. Latency by stage and token counts.
8. User feedback and reviewer decisions.

This operating view connects Hugo's logs and traces to
[[LLM Production Patterns]] and [[Model Monitoring]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Practice Answer Structure

Use this structure when practicing an LLM system design interview:

1. Restate the product: user, task, risk, source of truth, and action boundary.
2. Pick the simplest baseline and say why it might be enough.
3. Draw the request path from UI and API to auth, retrieval, or tools. Then add
   the context builder and model, and finish with the validator, storage, and
   response.
4. If RAG is needed, explain ingestion, chunking, metadata, and permissions.
   Then add embeddings and search, and finish with reranking, citations, and
   reindexing.
5. If tools or agents are needed, define tool permissions, typed inputs, mocked
   tool tests, integration tests, stop conditions, and human approval.
6. Separate retrieval evaluation, answer evaluation, safety evaluation, and
   product metrics.
7. Add red-team cases for prompt injection, data leakage, unsafe output, and
   tool misuse.
8. Explain latency and cost levers such as model choice and token budgets. Add
   caching and streaming, then include batching, retries, and fallbacks.
9. Define observability, rollout, rollback, ownership, and the review path.

This structure combines retrieval and chunking from Atita
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
It adds evaluation and traces from Hugo
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
It also uses deployment and model-choice tradeoffs from Meryem
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].

Ranjitha contributes agent tooling and outcome tests
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
Maria contributes chatbot security controls
[[cite:generative-ai-chatbots-in-production-security=>Hardening Generative AI Chatbots]].
Aditya contributes enterprise agent governance
[[cite:s23e03-future-of-ai-agents=>The Future of AI Agents]].

## Related Pages

Use these pages to go deeper on specific parts of an LLM system design answer:

1. [[retrieval-augmented-generation=>Retrieval-Augmented Generation]].
2. [[LLM Evaluation Workflows]].
3. [[Agent Engineering]].
4. [[AI Red Teaming]].
5. [[LLM Production Patterns]].
