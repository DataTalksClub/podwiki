---
layout: wiki
title: "RAG Portfolio Projects"
summary: "RAG portfolio project ideas organized around retrieval quality, citations, evaluation, and production tradeoffs."
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
retrieval-backed LLM work. Choose the RAG project type, name the role signal it
sends, and ground the project story in retrieval quality and citations. The
writeup should also make evaluation and production tradeoffs visible.

Use the [[Search and RAG Project Checklist]] after choosing one project idea.
After that, review the finished README, notebook, or project page against its
criteria.

The strongest portfolio ideas make the source evidence inspectable instead of
showing only a polished chat UI. Atita Arora's transcript example starts with
RAG, chunking, and vectorization. It then adds prompt context, citations, and
multi-level evaluation
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Hugo Bowne-Anderson's practical RAG discussion adds representative gold tests,
failure analysis, and logs or traces
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Read these RAG project ideas with
[[ai-engineering-portfolio-projects=>AI engineering portfolio projects]],
[[Portfolio Projects]], and the broader
[[Machine Learning Portfolio Projects]]
standard. [[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
defines the base concept,
[[rag-evaluation-workflow=>RAG Evaluation Workflow]]
defines the evaluation procedure. The
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]]
adds a staged path from scoped assistant to retrieval, evaluation, serving, and
operations controls.

## Choosing the Project Type

A RAG portfolio project should make the retrieval problem visible. A transcript
assistant and a support-docs assistant show source-grounded answering. A
search-first benchmark, graph RAG comparison, or production-minded demo proves a
different skill.

Podcast transcripts are a concrete example because long transcripts need
chunking and overlap before vectorization. The answer path then needs retrieval
and augmentation before generation. Citations come after that
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@35:49=>Podcast Transcript Chatbot]],
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Transcript Chunking and Vectors]]).

If the source audio starts outside the text corpus, add a transcript step such as
Whisper before chunking and evaluation. That story makes the project more
specific than a generic chat wrapper. The builder can explain the
audio-to-transcript path and chunk metadata. They can also explain retrieval
choices, prompt context, and citations.

Retrieval is preferable when a company's knowledge base changes, because the
system can re-index documents instead of repeatedly retraining the model. This
makes grounding part of the project definition, not an optional README flourish
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

Representative gold tests and failure categories can be the portfolio hook.
They show debugging judgment rather than only a working chatbot
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Use the [[Search and RAG Project Checklist]] for the field-by-field review.

## Portfolio Signals by Project Type

Project ideas require different proof. A search-engineering project puts weight
on
[[information retrieval]],
chunking, and metadata. It also covers vector search choices, prompt context,
citations, and multi-level evaluation
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

The same portfolio idea can be framed against fine-tuning and serving choices.
Changing knowledge belongs in retrieval, while style and domain adaptation fit
fine-tuning. Production readiness depends on model drift and hosting choices. It
also depends on latency, cost, and privacy
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

RAG portfolio work should therefore cover
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
and
[[LLM Production Patterns]].

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

The portfolio version should use example questions, retrieved passages, and
answer citations as visible proof. Add unsupported-question refusals and missed
evidence too.
Each layer of the RAG pipeline warrants evaluation
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Failures should be labeled as retrieval, generation, formatting, or source
preparation problems
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
The [[Search and RAG Project Checklist]] turns those signals into a concrete
review rubric.

## Search-First RAG System

A search-first RAG project proves retrieval quality first, before generation
makes the demo look fluent. Candidate retrieval is separate from ranking, and
existing search engines are preferable to custom indexes. Vector databases,
ingestion encoding, query-time encoding, and hybrid search all connect to
retrieval design
([[cite:building-production-search-systems=>Building Search Systems]]).

A search-first project is strongest when the README compares retrieval
approaches on the same questions. Search quality ties to business metrics and
A/B tests, as well as to offline evaluation and fast iteration
([[cite:building-production-search-systems=>Building Search Systems]]).

A portfolio project can use keyword baselines and vector retrieval as the main
story. It can compare hybrid search, filters, ranks, and failure cases before
generated answers. This is especially relevant for
[[embeddings]],
[[information retrieval]],
and
[[Production Search Evaluation]]
work.

## Evaluation and Failure Analysis Project

An evaluation-focused RAG project can start from an ordinary demo and make it
measurable. Representative gold tests give this structure. So do failure
categories that route the next fix to retrieval or prompting, with formatting
and data preparation as separate classes. Logs and traces make the MVP debuggable
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

The portfolio version can center the writeup on a compact evaluation report
rather than on another chat interface. Make a few representative failures
visible, then show whether the next fix belongs in retrieval or prompting. Link
the work to [[LLM Evaluation Workflows]] instead of claiming evaluation in the
abstract.

## Agentic RAG Boundary

A RAG portfolio project gets stronger when it states whether the system is only
answering from retrieved documents or also taking actions. Tool calls, memory,
and agents sit beyond basic RAG when a workflow needs multiple steps
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Retrieval is one tool an agent can choose, and dynamic planning and multiple
integrations push the project into
[[Agent Engineering]]
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

For a portfolio, this boundary should be visible in the design. A support-docs
assistant can stay as RAG when it only answers with citations. An operations
assistant that searches logs and calls monitoring APIs needs more evidence. If
it proposes remediation steps, it needs mocked tools, integration tests, and
outcome assertions
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

## Graph or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. Knowledge graphs connect to LLM grounding and
RAG. They contrast text chunking and embeddings with graph semantics, vector
databases, and Cypher-driven retrieval
([[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]).

Trust, hallucination, and verification limits matter here too. So do paper
parsing, graph visualization, PageRank, and references
([[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]).

A strong
[[Graph RAG vs Vector RAG]]
portfolio project can test both retrieval paths against the same questions. It
can show text similarity for passages. It can show graph traversal for
relationships.
It should also show when the evidence is insufficient.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
AI engineering practice. A career-break example builds prototypes with
AI developer tools. The interview task centers on a PDF Q&A assistant
([[cite:s23e04-how-to-become-ai-engineer-after-career-break=>How to Become an AI Engineer After a Career Break]]).

That path connects portfolio work to visible project evidence during a restart.
The project story should explain why the builder's previous domain makes the
corpus, users, and failure cases more credible. Pair this project type with
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

A production-minded demo should name the constraints a real team would face,
even without production scale. That checklist includes hidden API changes and
model drift. It compares hosted APIs with open-source serving across latency,
cost, and hardware. It also places changing knowledge in retrieval and grounding
rather than repeated retraining
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).

For portfolio evidence, frame the demo around re-indexing and version choices.
Name latency, cost, privacy limits, and hosted API risk too. These constraints
connect the project to
[[LLM Production Patterns]],
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]],
and the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].

Long context, agents, and vector databases mark another production boundary.
They don't remove the need to manage source quality and noisy context. Teams
still need to manage chunk metadata, latency, and cost
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

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
