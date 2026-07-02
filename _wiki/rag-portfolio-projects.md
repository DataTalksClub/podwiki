---
layout: wiki
title: "RAG Portfolio Projects"
summary: "DataTalks.Club guest guidance for RAG portfolio projects that prove retrieval quality, context design, citations, evaluation, failure analysis, and production-minded AI engineering."
related:
  - Portfolio Projects
  - Retrieval-Augmented Generation
  - Search and RAG Project Checklist
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - AI Engineering
  - Machine Learning Portfolio Projects
---

In a RAG portfolio project, the builder turns a real document corpus into a
retrieval-backed LLM system whose answers can be checked against source
evidence. The project is stronger when the demo shows retrieved passages and
answer citations. It should also show metadata, evaluation runs, and failure
labels instead of only a polished chat UI.

[[person:atitaarora|Atita Arora]] gives the clearest
project structure in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]:
at 30:38-48:09, she moves from retrieval-augmented generation to transcript
chunking and vectorization. She then adds prompt context, citations, and
multi-level RAG evaluation.

[[person:hugobowneanderson|Hugo Bowne-Anderson]]
adds the portfolio review standard in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]:
at 23:00-27:38, he connects representative gold tests with failure analysis. He
also ties the review to logs or traces.

Read this page with
[[Portfolio Projects]] and the
broader
[[Machine Learning Portfolio Projects]]
standard. For architecture and review criteria, use
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
with
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
and the
[[Search and RAG Project Checklist]].
Use
[[LLM Evaluation Workflows]]
and the
[[llm-rag-production-roadmap|LLM and RAG Production Roadmap]]
when the project needs evaluation, deployment, and operations evidence.

## Reviewable RAG Project

Across the RAG, search, and LLM engineering episodes, guests treat a strong RAG
portfolio project as the full retrieval loop. The project ingests source
documents and splits them into useful chunks. It keeps metadata, retrieves
evidence for a question, passes that evidence to the model, and cites sources a
reviewer can open.

At 35:49-42:49 in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
[[person:atitaarora|Atita Arora]] uses podcast
transcripts as the concrete example. Long transcripts need chunking and
overlap. Each chunk needs vectorization. The answer path needs retrieval,
augmentation, generation, and citations.

Her 48:09 evaluation discussion means
the project should test embedding choices and chunking strategy. It should also
test retrieval quality and final answer quality.

[[person:meryemarik|Meryem Arik]] gives the production
reason in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]:
at 40:46-46:42, she prefers retrieval when a company's knowledge base changes.
The system can re-index documents instead of repeatedly retraining the model.
Her framing makes grounding part of the project definition, not an optional
README flourish.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] adds
the reviewable engineering loop in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 23:00-27:38, representative gold tests and failure categories turn a RAG
demo into a debuggable system. Logs and traces make that review practical. A
portfolio reviewer should be able to see which questions failed because of
retrieval or chunking. Other failures may come from prompting, formatting, or
source preparation.

## Review Signals

Guests mostly differ on which part of the project needs the strongest proof.
Atita starts from search engineering. Her standard emphasizes
[[information retrieval]],
chunking, and metadata. It also emphasizes vector search choices, prompt
context, and citations. Multi-level evaluation matters too
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems, 17:01-48:09]]).

That view treats a
[[vector-databases|vector database]] as one
retrieval component, not the whole project.

Hugo starts from practical LLM shipping. In
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
he treats RAG as a quick business win when the knowledge base and chunking
strategy fit the task. He asks teams to add tools or
[[agent-engineering|agents]] only when lookup is
not enough. At 44:26-56:21, his examples move from RAG into tool calls, memory,
and agentic workflows when the system must coordinate steps.

[[person:ranjithakulkarni|Ranjitha Kulkarni]] draws a
similar boundary from agent engineering in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].
At 29:30-37:39, she argues that long context windows don't make RAG obsolete.
Latency and cost still matter. So do noisy context, chunk metadata, and source
quality.
At 36:11-40:30, she treats retrieval as one tool inside an agent when the
problem needs dynamic planning, multiple data sources, or API integrations.

Meryem frames the same project against fine-tuning and serving choices. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
she places changing knowledge in retrieval at 40:46. At 26:30, style and domain
adaptation fit fine-tuning. At 18:46 and 49:44-51:35, production readiness
depends on model drift, latency, and cost. Privacy and hosting choices matter
too.

RAG portfolio work should therefore cover
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
and
[[LLM Production Patterns]].

[[person:anahitapakiman|Anahita Pakiman]] adds a domain
modeling boundary. In
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]],
she argues at 33:43-42:42 that relationship-heavy domains can need
knowledge-graph retrieval and Cypher queries. They can also need graph
semantics in addition to nearest-neighbor text chunks. That's the project
boundary covered by
[[Graph RAG vs Vector RAG]].

## Source-Cited Knowledge Assistant

A source-cited knowledge assistant is the most direct first RAG portfolio
project. Atita and Hugo both use transcript or knowledge-base examples to
explain practical RAG. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]
at 35:49-42:49, [[person:atitaarora|Atita Arora]]
moves from podcast transcripts to chunking and overlap. She then adds
embeddings, retrieval, and augmentation. The path continues through generation,
prompt design, and citations.

In
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]],
[[person:hugobowneanderson|Hugo Bowne-Anderson]]
describes simple RAG bots with good chunking and embeddings as practical wins
at 44:26-50:30.

The portfolio artifact should therefore show example questions, retrieved
passages, answer citations, and refusals when the corpus doesn't support an
answer. It should also expose missed evidence. Atita's 48:09 discussion in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]
supports evaluating each layer of the RAG pipeline. Hugo's 26:43 failure
analysis in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
supports labeling failures as retrieval, generation, formatting, or source
preparation problems.

## Search-First RAG System

A search-first RAG project proves retrieval quality first. It does that before
generation makes the demo look fluent.
[[person:danielsvonava|Daniel Svonava]] grounds this
project type in
[[podcast:building-production-search-systems|Building Search Systems]].

At 12:45-17:40, he separates candidate retrieval from ranking and recommends
existing search engines instead of hand-rolled indexes. At 27:21-34:00, he
connects vector databases and ingestion encoding to retrieval design. He also
covers query-time encoding and hybrid search.

This project is strongest when the README compares retrieval approaches on the
same questions. Daniel's 1:01:25-1:03:50 discussion in
[[podcast:building-production-search-systems|Building Search Systems]]
ties search quality to business metrics and A/B tests. It also connects search
quality to offline evaluation and fast iteration.

A portfolio project can show keyword baselines and vector retrieval. It can
compare hybrid search, filters, ranks, and failure cases before generated
answers. This is especially relevant for
[[embeddings]],
[[information retrieval]],
and
[[Production Search Evaluation]]
work.

## Evaluation and Failure Analysis Project

An evaluation-focused RAG project can start from an ordinary demo and make it
measurable.
[[person:hugobowneanderson|Hugo Bowne-Anderson]] gives
this structure in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
At 23:00-25:25, he argues for representative gold tests. At 26:43, he
recommends categorizing failures so the next fix goes to retrieval or prompting.
Formatting and data preparation can be separate classes.

At 27:38, he connects logs and traces to a debuggable MVP.

A portfolio version can show a small evaluation table with the question and
expected evidence. Add retrieved chunks and scores. Record prompt version,
model version, and answer. Include latency and cost.
Feedback, failure class, and next fix turn
[[LLM Evaluation Workflows]]
into visible project evidence rather than a claim in the README.

Ranjitha extends the same idea when retrieval becomes one tool inside a larger
[[agent-engineering|AI agent]] workflow. Her agent
evaluation discussion at 51:17-57:23 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]
supports custom datasets, mocked tools, integration tests, and outcome
assertions. A portfolio project can show this with a compact evaluation report
that includes the query and expected evidence. It should also include retrieved
evidence, the answer, a failure class, and the next retrieval fix.

## Agentic RAG Boundary

A RAG portfolio project gets stronger when it states whether the system is only
answering from retrieved documents or also taking actions. Hugo's 44:26-56:21
discussion in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
places tool calls, memory, and agents beyond basic RAG when a workflow needs
multiple steps. Ranjitha makes the same boundary explicit in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]:
at 36:11-40:30, retrieval is one tool an agent can choose. Dynamic planning and
multiple integrations push the project into
[[Agent Engineering]].

For a portfolio, this boundary should be visible in the design. A support-docs
assistant can stay as RAG when it only answers with citations. An operations
assistant that searches logs and calls monitoring APIs needs more evidence. If
it proposes remediation steps, it needs mocked tools, integration tests, and
outcome assertions. Ranjitha describes that at 51:17-57:23 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]].

## Graph or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. [[person:anahitapakiman|Anahita Pakiman]]
grounds this project type in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]:
at 33:43-42:42, she connects knowledge graphs with LLM grounding and RAG. She
then contrasts text chunking and embeddings with graph semantics, vector
databases, and Cypher-driven retrieval.

The 42:42-47:10 section in
[[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]
also covers trust and hallucination. It covers verification limits too.
Anahita adds paper parsing and graph visualization. She also covers PageRank
and references.

A strong
[[Graph RAG vs Vector RAG]]
portfolio project can test both retrieval paths against the same questions. It
can show text similarity for passages. It can show graph traversal for
relationships.
It should also show when the evidence is insufficient.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
current AI engineering practice.
[[person:revathyramalingam|Revathy Ramalingam]] gives
the career-break example in
[[podcast:s23e04-how-to-become-ai-engineer-after-career-break|How to Become an AI Engineer After a Career Break]].
Her 22:15 chapter covers building prototypes with AI developer tools. Her 33:45
chapter covers an interview task that uses a PDF Q&A assistant.

That episode connects portfolio work to visible project evidence during a
restart. The RAG project still needs the same evidence bar as the search and
LLM engineering episodes. Show corpus choice, chunking plan, retrieval
baselines, and citations. Show tests, logs, and deployment boundaries too. Pair
this project type with
[[career-transitions-in-data|Career Transition]] and
[[Job Search]] when the page is used
for hiring preparation.

[[person:pauliusztin|Paul Iusztin]] adds the
[[AI Engineering]] framing in
[[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|his AI engineering episode]].
At 29:12, he places RAG and knowledge management inside the AI engineer skill
stack. At 54:05, he connects portfolio work with a "second brain" project. That
supports a personal knowledge assistant when the project also shows software
quality, evaluation, and knowledge-management judgment.

## Production-Minded RAG Demo

A production-minded demo doesn't need production scale, but it should name the
constraints a real team would face. [[person:meryemarik|Meryem Arik]]'s
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]
episode supports that checklist. At 18:46, she discusses hidden API changes and
model drift. At 49:44-51:35, she compares hosted APIs with open-source serving
and covers latency, cost, and hardware. At 40:46-46:42, she places changing
knowledge in retrieval and grounding rather than repeated retraining.

For portfolio evidence, document how the system re-indexes sources, which
embedding and model versions it uses, and how latency and cost would be
handled. Name privacy limits and hosted API risks too. These constraints connect
the project to
[[LLM Production Patterns]],
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]],
and the
[[llm-rag-production-roadmap|LLM and RAG Production Roadmap]].

Ranjitha's RAG reality check at 29:30-37:39 in
[[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]
adds another production boundary. Long context, agents, and vector databases do
not remove the need to manage source quality and noisy context. Teams still need
to manage chunk metadata, latency, and cost.

## Related Pages

These pages cover the concepts and project standards around RAG portfolio work.

- [[retrieval-augmented-generation|Retrieval-Augmented Generation]] for the core RAG architecture.
- [[Search and RAG Project Checklist]] for a practical review checklist.
- [[LLM Evaluation Workflows]] for gold sets, traces, and failure analysis.
- [[LLM Production Patterns]] for deployment, latency, cost, observability, and model-risk context.
- [[llm-rag-production-roadmap|LLM and RAG Production Roadmap]] for a build sequence from bounded workflows to production controls.
- [[LLM System Design Interview]] for explaining retrieval, evaluation, and production tradeoffs in interviews.
- [[rag-vs-fine-tuning|RAG vs Fine-Tuning]] for deciding whether changing knowledge belongs in retrieval or model adaptation.
- [[Vector Databases]] and [[Embeddings]] for retrieval infrastructure choices.
- [[Agent Engineering]] for projects where retrieval becomes one tool inside a multi-step system.
- [[Graph RAG vs Vector RAG]] for projects where relationships matter as much as text similarity.
- [[Machine Learning Portfolio Projects]] for the broader project-evidence standard.
- [[career-transitions-in-data|Career Transition]] and [[Job Search]] for turning the project into hiring evidence.
