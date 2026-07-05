---
layout: wiki
title: "RAG Portfolio Projects"
summary: "RAG portfolio project categories and the hiring signals each category can show."
related:
  - Portfolio Projects
  - Retrieval-Augmented Generation
  - Search and RAG Project Checklist
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - AI Engineering
  - Machine Learning Portfolio Projects
---

RAG portfolio projects prove that a candidate can turn a real corpus into
retrieval-backed LLM evidence. Choose projects by category and hiring signal.
The [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] hub
covers architecture. [[Search and RAG Project Checklist]] covers review fields
on a built project, while [[rag-evaluation-workflow=>RAG Evaluation Workflow]]
covers measurement procedure.

Strong portfolio ideas make source evidence inspectable instead of showing only
a polished chat UI. Useful proof includes chunking choices, retrieved passages,
prompt context, and citations. Representative gold tests, failure analysis, and
traces add debugging evidence.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Read these ideas with
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]],
[[Portfolio Projects]], and the broader
[[Machine Learning Portfolio Projects]] standard.

## Choosing the Project Type

A RAG portfolio project should make one retrieval problem visible.

Pick the category by the signal the project should send:

- a source-cited transcript or support-docs assistant
- a search-first benchmark that compares retrieval methods
- an evaluation and failure-analysis report
- a graph or domain RAG comparison
- a career-transition project tied to the builder's previous domain
- a production-minded demo that names real operating constraints

Podcast transcript projects can show these artifacts.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@35:49=>Podcast Transcript Chatbot]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript Chunking and Vectors]]

- chunk boundaries and overlap choices
- retrieved passages and cited answers
- missing evidence

If source audio starts outside the text corpus, the audio-to-transcript path
becomes part of the proof instead of hidden setup.

For changing knowledge, a portfolio project can show re-indexing instead of
model retraining. Put that boundary in the project story as a corpus-update
choice. Leave the deeper comparison to
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

Evaluation can also be the main portfolio hook. A compact report can show
representative failures and tested fixes. Traces can say more than another chat
interface.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]
Keep the detailed scoring workflow on
[[rag-evaluation-workflow=>RAG Evaluation Workflow]].

## Source-Cited Knowledge Assistant

A source-cited knowledge assistant is the most direct first RAG portfolio
project. Transcript and knowledge-base examples both show a real corpus and
retrievable chunks. They also show grounded answers, citations, and
unsupported-question refusals.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

The portfolio proof should show a few example questions with retrieved passages
and cited answers.

It should also show failure cases:

- missing evidence
- stale source material
- weak chunk boundaries
- plausible answers that the sources don't support

Use the
[[Search and RAG Project Checklist]] for the concrete review fields.

## Search-First RAG System

A search-first RAG project proves retrieval quality before fluent generation
can hide weak evidence. It signals [[information retrieval]] judgment when the
README compares retrieval approaches on the same questions. Compare keyword
search and vector search. Add filters, reranking, or hybrid search when the
project uses them.[[cite:building-production-search-systems=>Building Search Systems]]

It remains a RAG portfolio project when retrieved evidence feeds generated,
cited answers. If the project stops at candidate retrieval, ranking, or
search-quality metrics, route it to [[Information Retrieval]] or
[[Production Search Evaluation]].

## Evaluation and Failure Analysis Project

An evaluation-focused RAG project can start from an ordinary demo and make the
measuring work the main story. Representative gold tests, ranked failure
categories, and traces show debugging judgment.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

The portfolio version can center the writeup on a compact evaluation report.
Make a few representative failures visible, then show the tested fix. Keep the
workflow on [[rag-evaluation-workflow=>RAG Evaluation Workflow]] and link the
project to [[LLM Evaluation Workflows]].

## Agentic RAG Boundary

State the answer-only boundary and whether the system takes actions.

Tool calls and memory sit beyond basic RAG when the workflow needs multiple
steps.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

Retrieval becomes one tool inside an agent when the problem needs dynamic
planning or multiple integrations.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

A support-docs assistant can stay as RAG when it only answers with citations.
An operations assistant that searches logs, calls monitoring APIs, or proposes
remediation steps needs agent evidence instead. Put that proof on
[[Agent Engineering]] and [[LLM Evaluation Workflows]].

## Graph or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. Knowledge graphs add explicit entities,
relationships, provenance paths, and Cypher-driven retrieval to LLM grounding.[[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]

A [[Graph RAG vs Vector RAG]] portfolio project signals domain-modeling judgment
when it tests both retrieval paths against the same questions. It should show
which answers need passages, which need relationships, and which require an
insufficient-evidence refusal.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
AI engineering practice. A PDF Q&A assistant can turn domain documents into
visible project evidence during a restart.[[cite:s23e04-how-to-become-ai-engineer-after-career-break=>How to Become an AI Engineer After a Career Break]]

The builder's previous domain should make the corpus easier to define. The
project story should make users specific and name failure cases. RAG with
knowledge management sits inside the [[AI Engineering]] skill stack. That
supports personal knowledge-assistant projects. They should show software
quality and evaluation judgment.[[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]
Pair this project type with [[career-transitions-in-data=>Career Transition]]
and [[Job Search]] for hiring preparation.

## Production-Minded RAG Demo

A production-minded demo should name the constraints a real team would face
even without production scale.

Useful constraints include:

- source quality and chunk metadata
- re-indexing
- latency and cost
- privacy
- hosted API risk and model drift

[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]

The portfolio signal isn't scale. The candidate should explain which constraints
matter for the chosen corpus and user task. Keep the maturity sequence on
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]], and connect the
project to [[LLM Production Patterns]] and
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

## Related Pages

These pages cover the concepts and project standards around RAG portfolio work.

- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the core RAG architecture.
- [[ai-engineering-portfolio-projects=>AI engineering portfolio projects]] for the broader AI product evidence standard.
- [[Search and RAG Project Checklist]] for execution fields once the project type is chosen.
- [[rag-evaluation-workflow=>RAG Evaluation Workflow]] for retrieval checks, answer checks, traces, and feedback.
- [[LLM Evaluation Workflows]] for broader LLM gold sets, traces, and failure analysis.
- [[LLM Production Patterns]] for deployment, latency, cost, observability, and model-risk context.
- [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] for a build sequence from bounded workflows to production controls.
- [[LLM System Design Interview]] for explaining retrieval, evaluation, and production tradeoffs in interviews.
- [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] for deciding whether changing knowledge belongs in retrieval or model adaptation.
- [[Vector Databases]] and [[Embeddings]] for retrieval infrastructure choices.
- [[Agent Engineering]] for projects where retrieval becomes one tool inside a multi-step system.
- [[Graph RAG vs Vector RAG]] for projects where relationships matter as much as text similarity.
- [[Machine Learning Portfolio Projects]] for the broader project-evidence standard.
- [[career-transitions-in-data=>Career Transition]] and [[Job Search]] for turning the project into hiring evidence.
