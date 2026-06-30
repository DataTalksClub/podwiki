---
layout: wiki
title: "RAG Portfolio Projects"
summary: "Archive-backed guidance for RAG portfolio projects that prove retrieval quality, context design, citations, evaluation, failure analysis, and production-minded AI engineering."
related:
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - AI Engineering
  - Machine Learning Portfolio Projects
---

## Definition and Scope

A RAG portfolio project is a public artifact. It proves that the builder can
turn a document corpus into a retrieval-backed LLM system with grounded answers.
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the core path
in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 30:38-42:49. She connects retrieval and context packaging. She also covers
generation, prompt design, and citations.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
adds evaluation sets and failure categories. He also covers logs, traces, and
chunking choices in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 23:00-48:20.

This topic covers RAG projects aimed at
[AI engineering]({{ '/wiki/ai-engineering/' | relative_url }}),
[LLM production]({{ '/wiki/llm-production-patterns/' | relative_url }}),
search engineering, or career-transition proof. For the concept page, start
with
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
For general project evidence, compare
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
and
[Open Source Portfolio Evidence]({{ '/wiki/open-source-portfolio-evidence/' | relative_url }}).

## Link Map

Core wiki routes:

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})

Podcast anchors:

- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}) with [Atita Arora]({{ '/people/atitaarora/' | relative_url }})
- [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}) with [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}) with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }})
- [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}) with [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
- [Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
- [Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}) with [Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }})
- [AI Engineering: Skill Stack, Agents, LLMOps, and How to Ship AI Products]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}) with [Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }})

## Common Definition

Across the archive, a strong RAG project proves the full retrieval loop. It
covers source ingestion, chunking, and metadata. It also covers retrieval,
answer generation, and citations. Evaluation and iteration are part of the same
loop.

Atita's transcript-chatbot example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 35:49-42:49 is the clearest portfolio model. The corpus is long, the chunks
need provenance, and the answer has to point back to the source.

Hugo adds the review standard in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 23:00-27:38. Build representative gold tests. Categorize failures. Log
traces. Change chunking or retrieval before polishing the UI when retrieval is
the larger failure class.

The portfolio signal is strongest when readers can look at the system's work. A
README should show example questions, retrieved chunks, and citations. It
should also show wrong answers, latency or cost notes, and the next retrieval
fix. This follows Atita's multi-level RAG evaluation discussion at 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
and Hugo's debugging workflow at 27:38 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

## Guest Differences

Atita starts from search engineering. Her useful portfolio standard is to
compare existing search infrastructure with standalone
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}). The project
should preserve metadata and evaluate retrieval quality before the LLM answer
becomes the product
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
17:01-48:09).

Hugo starts from practical LLM shipping. He presents RAG as a quick business win
when the corpus, chunking, and embeddings fit the task. He also says teams
should add tools or agents only when the workflow needs actions beyond lookup
([Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
44:26-56:21).

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) draws the
same boundary from agent engineering. RAG remains useful when retrieval controls
latency, cost, noisy context, and chunk metadata. Source quality and wrappers
also decide whether retrieval helps
([Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
29:30-37:39).

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) frames RAG against
fine-tuning and deployment constraints. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she treats retrieval as a better fit for changing knowledge at 40:46-46:42. She
also covers API risk and model drift at 18:46. Later, she covers latency, cost,
and self-hosting at 49:44-51:35.

## Source-Cited Knowledge Assistant

Start with a source-cited assistant over a real corpus. Good archive-backed
choices include podcast transcripts, internal docs, and policies. Tickets,
research papers, and course notes can also work.

Atita's podcast-transcript RAG example at 35:49-42:49
in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
shows the essential proof. Parse long source documents and chunk them. Attach
source metadata, retrieve relevant passages, and return citations users can
open.

For a portfolio README, include questions where the assistant answers with
citations. Include questions where it refuses because evidence is missing. That
matches the grounding work in
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and the human-review layer Atita describes at 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).

## Search-First RAG Project

A search-first project proves that generation isn't hiding weak retrieval.
Build keyword search or vector search first. Add filters or hybrid search when
the corpus needs them. Then add the answer-generation layer.

This follows
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
where the discussion separates candidate generation from ML ranking at
12:45-17:40. The same episode covers embeddings and vector compute at
21:55-29:00. It also covers vector storage, filters, recency, and business
constraints at 29:00-45:11.

This project is useful for candidates targeting search,
[embeddings]({{ '/wiki/embeddings/' | relative_url }}), or
[vector database]({{ '/wiki/vector-databases/' | relative_url }}) roles. It can
show retrieval metrics before and after changes. Compare one simple baseline
with one semantic or hybrid path. That reflects Atita's migration discussion at
20:27 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
and the hybrid-search discussion at 34:00 in
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}).

## Evaluation and Failure Analysis

An evaluation-focused project can start from an existing demo and make it
measurable. Hugo's workflow in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 23:00-27:38 gives the structure. Create a representative gold set, run the
system, label failures, and separate retrieval failures from generation
failures. Then log enough traces to debug the next change. This connects to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

Ranjitha's agent-evaluation guidance extends the same idea. It applies when
retrieval is one tool in a larger workflow. At 51:17-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she argues for custom datasets and mocked tools. She also covers integration
tests and outcome assertions.

A portfolio project can show this with a small report. Include the query,
retrieved evidence, and generated answer. Add the
expected evidence, failure class, and proposed fix.

## Domain Knowledge or Graph RAG

Some RAG projects shouldn't be only nearest-neighbor text search. In
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) contrasts
text chunking, embeddings, and vector databases at 33:43-38:10. She also
compares that with graph semantics. Then she covers Cypher-driven retrieval and
verification limits at 39:56-42:42.

That supports RAG projects for domains where relationships matter. Examples
include papers and citations, parts and simulations, regulations and clauses,
or incident reports and linked systems. A useful
[Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
portfolio example can retrieve text snippets and relationship paths. It should
show where each method fails or succeeds against the same gold questions
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
38:10-47:10).

## Career-Transition RAG Project

A career-switcher RAG project should connect old domain knowledge to current AI
engineering.
[How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }})
shows [Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }}) in
her restart path. She uses current project evidence and GitHub work. She also
uses a deployed project and a PDF Q&A assistant at 22:15-33:45.

The
[Career Transition]({{ '/wiki/career-transition/' | relative_url }}) page
connects that story to a broader archive lesson. Visible artifacts make prior
experience legible to a target role.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) adds the
AI-engineering version in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
His 29:12 chapter puts RAG and knowledge management inside the AI engineer
skill set. His 54:05 chapter connects portfolio work with a "second brain"
artifact. A personal knowledge assistant is credible when it shows software
quality, evaluation, and knowledge-management judgment.

## Practical Review Criteria

Use these criteria as the project review standard because each one maps to a
recurring archive discussion.

1. Define the corpus and user questions. Atita's transcript-chatbot example in
   [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
   works because the corpus and question type are clear at 35:49.
2. Preserve source provenance. Chunk metadata and wrappers matter because Atita
   and Ranjitha connect retrieval quality to context design and metadata. Useful
   provenance can include titles, timestamps, and sections. Authors or
   permissions can matter too
   ([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
   38:24-42:49 and
   [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
   32:48).
3. Compare retrieval approaches. A portfolio project shouldn't assume vector
   search is the whole answer because
   [Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
   separates keyword search from vector search. It also covers filters,
   recency, and ranking at 11:29-45:11.
4. Require grounded answers. The generation step should cite retrieved evidence
   and expose missing-evidence cases, following
   [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
   at 42:49 and
   [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
   at 42:02-46:42.
5. Build a small gold set. Hugo's test-set discussion at 23:00-25:25 in
   [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
   supports a compact evaluation file with questions, expected evidence,
   acceptable answers, and failure labels.
6. Log the debugging path. Retrieved chunks and scores are portfolio evidence.
   Prompts and model versions matter too. Log outputs, latency, cost, and
   feedback because Hugo ties logs and traces to debuggable MVPs at 27:38 in
   [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
7. State production boundaries. Meryem's production discussion at 18:46 and
   49:44-51:35 in
   [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
   supports documenting API risk, model drift, and privacy. It also supports
   latency, cost, serving, and reindexing notes.

## Weak Signals to Avoid

A RAG portfolio is weak when it only shows "chat with PDF" behavior. That misses
retrieval evaluation and source citations. It also misses visible chunks and
failure analysis.

The project then misses Atita's retrieval-plus-generation path in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 30:38-48:09. It also misses the gold-set workflow Hugo describes in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
at 23:00-27:38.

It's also weak to use agents or long context as a way to skip retrieval design.
A vector database doesn't remove that work either.

Ranjitha's RAG reality check
at 29:30-37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
keeps latency and cost in scope. It also keeps noisy context, chunk metadata,
and tool boundaries in scope. The
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion keeps filters and recency in scope. It also covers ranking and
offline tests at 34:00-63:50.

## Related Pages

Use these pages for adjacent concepts and project standards:

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) for the core RAG architecture.
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) for retrieval architecture and knowledge-system tradeoffs.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for gold sets, failure analysis, and agent tests.
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}) for deployment, latency, cost, observability, and model-risk context.
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) for deciding whether changing knowledge belongs in retrieval or model adaptation.
- [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }}) for projects where relationships matter as much as text similarity.
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}) for the broader project-evidence standard.
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }}) and [Job Search]({{ '/wiki/job-search/' | relative_url }}) for turning the project into hiring evidence.
