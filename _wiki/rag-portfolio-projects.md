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

A clear project structure moves from retrieval-augmented generation to
transcript chunking and vectorization, then adds prompt context, citations, and
multi-level RAG evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

The portfolio review standard pairs representative gold tests with failure
analysis and ties the review to logs or traces
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

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

A strong RAG portfolio project is the full retrieval loop. The project ingests
source documents and splits them into useful chunks. It keeps metadata,
retrieves evidence for a question, passes that evidence to the model, and cites
sources a reviewer can open.

Podcast transcripts are a concrete example: long transcripts need chunking and
overlap, each chunk needs vectorization, and the answer path needs retrieval,
augmentation, generation, and citations
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
The project should test embedding choices, chunking strategy, retrieval quality,
and final answer quality.

Retrieval is preferable when a company's knowledge base changes, because the
system can re-index documents instead of repeatedly retraining the model. This
makes grounding part of the project definition, not an optional README flourish
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

Representative gold tests and failure categories turn a RAG demo into a
debuggable system, and logs and traces make that review practical
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
A portfolio reviewer should be able to see which questions failed because of
retrieval or chunking. Other failures may come from prompting, formatting, or
source preparation.

## Review Signals

Approaches differ on which part of the project needs the strongest proof. A
search-engineering standard emphasizes
[[information retrieval]],
chunking, and metadata, along with vector search choices, prompt context,
citations, and multi-level evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
That view treats a
[[vector-databases|vector database]] as one
retrieval component, not the whole project.

A practical-shipping standard treats RAG as a quick business win when the
knowledge base and chunking strategy fit the task, adding tools or
[[agent-engineering|agents]] only when lookup is
not enough; the examples move from RAG into tool calls, memory, and agentic
workflows when the system must coordinate steps
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A similar boundary comes from agent engineering: long context windows don't make
RAG obsolete, because latency, cost, noisy context, chunk metadata, and source
quality still matter. Retrieval becomes one tool inside an agent when the problem
needs dynamic planning, multiple data sources, or API integrations
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

The same project can be framed against fine-tuning and serving choices: changing
knowledge belongs in retrieval, while style and domain adaptation fit
fine-tuning, and production readiness depends on model drift, latency, cost,
privacy, and hosting choices
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

RAG portfolio work should therefore cover
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]]
and
[[LLM Production Patterns]].

A domain-modeling boundary applies too: relationship-heavy domains can need
knowledge-graph retrieval and Cypher queries, and graph semantics in addition to
nearest-neighbor text chunks
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]).
That's the project boundary covered by
[[Graph RAG vs Vector RAG]].

## Source-Cited Knowledge Assistant

A source-cited knowledge assistant is the most direct first RAG portfolio
project. Transcript and knowledge-base examples both illustrate practical RAG: a
path that moves from podcast transcripts to chunking and overlap, then adds
embeddings, retrieval, and augmentation, and continues through generation,
prompt design, and citations
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Simple RAG bots with good chunking and embeddings are practical wins
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

The portfolio artifact should therefore show example questions, retrieved
passages, answer citations, and refusals when the corpus doesn't support an
answer. It should also expose missed evidence. Each layer of the RAG pipeline
warrants evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]),
and failures should be labeled as retrieval, generation, formatting, or source
preparation problems
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

## Search-First RAG System

A search-first RAG project proves retrieval quality first, before generation
makes the demo look fluent. Candidate retrieval is separate from ranking, and
existing search engines are preferable to hand-rolled indexes; vector databases,
ingestion encoding, query-time encoding, and hybrid search all connect to
retrieval design
([[podcast:building-production-search-systems|Building Search Systems]]).

This project is strongest when the README compares retrieval approaches on the
same questions. Search quality ties to business metrics and A/B tests, as well
as to offline evaluation and fast iteration
([[podcast:building-production-search-systems|Building Search Systems]]).

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
measurable. Representative gold tests, categorizing failures so the next fix
goes to retrieval or prompting (with formatting and data preparation as separate
classes), and logs and traces for a debuggable MVP give this structure
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

A portfolio version can show a small evaluation table with the question and
expected evidence. Add retrieved chunks and scores. Record prompt version,
model version, and answer. Include latency and cost.
Feedback, failure class, and next fix turn
[[LLM Evaluation Workflows]]
into visible project evidence rather than a claim in the README.

The same idea extends when retrieval becomes one tool inside a larger
[[agent-engineering|AI agent]] workflow, where agent
evaluation uses custom datasets, mocked tools, integration tests, and outcome
assertions
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
A portfolio project can show this with a compact evaluation report that includes
the query and expected evidence. It should also include retrieved evidence, the
answer, a failure class, and the next retrieval fix.

## Agentic RAG Boundary

A RAG portfolio project gets stronger when it states whether the system is only
answering from retrieved documents or also taking actions. Tool calls, memory,
and agents sit beyond basic RAG when a workflow needs multiple steps
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Retrieval is one tool an agent can choose, and dynamic planning and multiple
integrations push the project into
[[Agent Engineering]]
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

For a portfolio, this boundary should be visible in the design. A support-docs
assistant can stay as RAG when it only answers with citations. An operations
assistant that searches logs and calls monitoring APIs needs more evidence. If
it proposes remediation steps, it needs mocked tools, integration tests, and
outcome assertions
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

## Graph or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. Knowledge graphs connect to LLM grounding and
RAG, contrasting text chunking and embeddings with graph semantics, vector
databases, and Cypher-driven retrieval
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]).

Trust, hallucination, and verification limits matter here too, alongside paper
parsing, graph visualization, PageRank, and references
([[podcast:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]).

A strong
[[Graph RAG vs Vector RAG]]
portfolio project can test both retrieval paths against the same questions. It
can show text similarity for passages. It can show graph traversal for
relationships.
It should also show when the evidence is insufficient.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
current AI engineering practice. A career-break example builds prototypes with
AI developer tools and uses an interview task built around a PDF Q&A assistant
([[podcast:s23e04-how-to-become-ai-engineer-after-career-break|How to Become an AI Engineer After a Career Break]]).

That path connects portfolio work to visible project evidence during a restart.
The RAG project still needs the same evidence bar as the search and LLM
engineering material. Show corpus choice, chunking plan, retrieval baselines,
and citations. Show tests, logs, and deployment boundaries too. Pair this
project type with
[[career-transitions-in-data|Career Transition]] and
[[Job Search]] when the page is used
for hiring preparation.

RAG and knowledge management sit inside the
[[AI Engineering]] skill stack, and portfolio
work connects to a "second brain" project
([[podcast:s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products|AI Engineering Skill Stack]]).
That supports a personal knowledge assistant when the project also shows
software quality, evaluation, and knowledge-management judgment.

## Production-Minded RAG Demo

A production-minded demo doesn't need production scale, but it should name the
constraints a real team would face. Hidden API changes and model drift, the
comparison between hosted APIs and open-source serving (latency, cost, and
hardware), and placing changing knowledge in retrieval and grounding rather than
repeated retraining all belong on that checklist
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).

For portfolio evidence, document how the system re-indexes sources, which
embedding and model versions it uses, and how latency and cost would be
handled. Name privacy limits and hosted API risks too. These constraints connect
the project to
[[LLM Production Patterns]],
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]],
and the
[[llm-rag-production-roadmap|LLM and RAG Production Roadmap]].

Another production boundary: long context, agents, and vector databases do not
remove the need to manage source quality and noisy context, and teams still need
to manage chunk metadata, latency, and cost
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).

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
