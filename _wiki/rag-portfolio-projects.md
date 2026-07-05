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

RAG portfolio projects turn a real document corpus into hiring evidence for
retrieval-backed LLM work. Start here when choosing the project category and the
role signal it sends. The [[Search and RAG Project Checklist]] covers
implementation review fields, and
[[rag-evaluation-workflow=>RAG Evaluation Workflow]] covers the evaluation
procedure.

Strong portfolio ideas make source evidence inspectable instead of showing only
a polished chat UI. Atita Arora's transcript example starts with RAG, chunking,
and vectorization. It then adds prompt context, citations, and multi-level
evaluation
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Hugo Bowne-Anderson's practical RAG discussion adds representative gold tests,
failure analysis, and logs or traces
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Read these project ideas with
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]],
[[Portfolio Projects]], and the broader
[[Machine Learning Portfolio Projects]] standard. Use
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the base
architecture and the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] for sequencing.

## Choosing the Project Type

A RAG portfolio project should make one retrieval problem visible.

Pick the category by the signal the project should send:

- a transcript assistant
- a support-docs assistant
- a search-first benchmark
- a graph RAG comparison
- an evaluation report
- a production-minded demo

Podcast transcripts are a concrete example because long transcripts need
chunking and overlap before vectorization. The answer path then needs retrieval
and augmentation before generation. Citations come after that
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@35:49=>Podcast Transcript Chatbot]],
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript Chunking and Vectors]]).

If source audio starts outside the text corpus, add a transcript step before
chunking. That makes the project more specific than a generic chat wrapper. The
portfolio signal is the builder's ability to explain the audio-to-transcript path
and chunk metadata, plus retrieval choices, prompt context, and citations.

Retrieval is preferable when a company's knowledge base changes because the
system can re-index documents instead of repeatedly retraining the model. That
boundary makes grounding part of the project choice
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

An evaluation report can be the portfolio hook when it shows debugging judgment
rather than only a working chatbot
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
The detailed test data, retrieved-context checks, answer checks, and iteration
belong on [[rag-evaluation-workflow=>RAG Evaluation Workflow]].

## Portfolio Signals by Project Type

Project categories signal different strengths. A search-engineering project puts
weight on [[information retrieval]], chunking, metadata, and vector search choices
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
That view treats a
[[vector-databases=>vector database]] as one
retrieval component, not the whole project.

A practical-shipping project treats RAG as a quick business win when the
knowledge base and chunking strategy fit the task. It adds tools or
[[agent-engineering=>agents]] only when lookup is
not enough. The examples move from RAG into tool calls, memory, and agentic
workflows when the system must coordinate steps
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Agent engineering draws a similar boundary. Long context windows don't make RAG
obsolete because latency, cost, and noisy context still matter. Chunk metadata
and source quality still matter too. Retrieval becomes one tool inside an agent
when the problem needs dynamic planning, multiple data sources, or API
integrations
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

The same portfolio idea can signal deployment judgment when it names the
boundary between retrieval, fine-tuning, and serving. Changing knowledge belongs
in retrieval, while style and domain adaptation fit fine-tuning. Hosting choices
and model drift set the production story. So do latency, cost, and privacy
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

RAG portfolio work should therefore link to
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] and [[LLM Production Patterns]]
without restating those pages.

A domain-modeling boundary applies too when relationship-heavy domains need
knowledge-graph retrieval and Cypher queries. They may also need graph semantics
in addition to nearest-neighbor text chunks
([[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]).
That's the project boundary covered by
[[Graph RAG vs Vector RAG]].

## Source-Cited Knowledge Assistant

A source-cited knowledge assistant is the most direct first RAG portfolio
project. Transcript and knowledge-base examples both illustrate practical RAG.
They move from podcast transcripts to chunking and overlap, then add embeddings,
retrieval, and augmentation. They continue through generation, prompt design,
and citations
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Simple RAG bots with good chunking and embeddings are practical wins
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Visible source grounding is the portfolio signal. Show example questions and
retrieved passages, then include answer citations, unsupported-question refusals,
and missed evidence.
Atita's discussion treats evaluation as layered across the RAG pipeline
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
The [[Search and RAG Project Checklist]] turns those fields into a review rubric.

## Search-First RAG System

A search-first RAG project proves retrieval quality first, before generation
makes the demo look fluent. Candidate retrieval is separate from ranking, and
existing search engines are preferable to custom indexes. Vector databases,
ingestion encoding, query-time encoding, and hybrid search all connect to
retrieval design
([[cite:building-production-search-systems=>Building Search Systems]]).

A search-first project signals retrieval judgment when the README compares
retrieval approaches on the same questions. Search quality ties to business
metrics, A/B tests, offline evaluation, and fast iteration
([[cite:building-production-search-systems=>Building Search Systems]]).
It remains a RAG portfolio project when retrieval feeds generated answers with
visible source citations. If the project stops at candidate retrieval, ranking,
or search-quality metrics, route it to [[Information Retrieval]] or
[[Production Search Evaluation]].

## Evaluation and Failure Analysis Project

An evaluation-focused RAG project can start from an ordinary demo and make the
measuring work the main story. Representative gold tests, failure categories,
and traces show debugging judgment
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

The portfolio version can center the writeup on a compact evaluation report
rather than on another chat interface. Make a few representative failures
visible, then show the tested fix. Keep the workflow on
[[rag-evaluation-workflow=>RAG Evaluation Workflow]] and link the project to
[[LLM Evaluation Workflows]].

## Agentic RAG Boundary

A RAG portfolio project gets stronger when it states whether the system is only
answering from retrieved documents or also taking actions. Tool calls, memory,
and agents sit beyond basic RAG when a workflow needs multiple steps
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Retrieval is one tool an agent can choose, and dynamic planning and multiple
integrations push the project into
[[Agent Engineering]]
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

For a portfolio, make this boundary visible in the design. A support-docs
assistant can stay as RAG when it only answers with citations. An operations
assistant that searches logs, calls monitoring APIs, or proposes remediation
steps needs agent evidence instead. Put the agent details on
[[Agent Engineering]] and [[LLM Evaluation Workflows]]
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

## Graph or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. Knowledge graphs connect to LLM grounding and
RAG. They contrast text chunking and embeddings with graph semantics, vector
databases, and Cypher-driven retrieval
([[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]).

A [[Graph RAG vs Vector RAG]] portfolio project signals domain-modeling judgment
when it tests both retrieval paths against the same questions. It should show
which answers need passages, relationships, or insufficient-evidence refusals.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
AI engineering practice. A career-break example builds prototypes with
AI developer tools. The interview task centers on a PDF Q&A assistant
([[cite:s23e04-how-to-become-ai-engineer-after-career-break=>How to Become an AI Engineer After a Career Break]]).

That path connects portfolio work to visible project evidence during a restart.
The project story can explain why the builder's previous domain makes the
corpus, users, and failure cases easier to define. Pair this project type with
[[career-transitions-in-data=>Career Transition]] and
[[Job Search]] when the page is used
for hiring preparation.

RAG and knowledge management sit inside the
[[AI Engineering]] skill stack, and portfolio
work connects to a "second brain" project
([[cite:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products=>AI Engineering Skill Stack]]).
That supports a personal knowledge assistant when the project also shows
software quality, evaluation, and knowledge-management judgment.

## Production-Minded RAG Demo

A production-minded demo should name the constraints a real team would face
even without production scale. The project story should compare hosted APIs
with open-source serving. It should also name latency, cost, and hardware. Hidden
API changes and model drift belong in the same story
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Frame portfolio evidence around source quality, chunk metadata, re-indexing
choices, and version choices. Name latency, cost, privacy, and hosted API risk
too. Keep the maturity sequence on
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
