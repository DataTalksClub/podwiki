---
layout: wiki
title: "RAG Portfolio Projects"
summary: "Archive-backed guidance for RAG portfolio projects that prove retrieval quality, context design, citations, evaluation, failure analysis, and production-minded AI engineering."
related:
  - Portfolio Projects
  - Retrieval-Augmented Generation
  - Search and RAG Project Checklist
  - Search, RAG, and Knowledge Systems
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - AI Engineering
  - Machine Learning Portfolio Projects
---

In a RAG portfolio project, the builder turns a document corpus into a
retrieval-backed LLM system. A reviewer can look at the evidence behind each
answer. In the README, the builder names the corpus and chunking plan. In the
demo, the reviewer sees metadata, retrieved context, and citations. The builder
uses evaluation notes to explain failures.

This topic is one branch of the broader
[Portfolio Projects]({{ '/wiki/portfolio-projects/' | relative_url }}) hub. It
starts with
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
Use [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for gold sets and failure analysis. Use
[AI Engineering]({{ '/wiki/ai-engineering/' | relative_url }}) for the wider
product-engineering context. For project review, pair this page with the
[Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
and the broader
[Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }})
standard.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the clearest
archive-backed structure in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38-42:49, she connects retrieval and chunking to context packaging. She
then brings in vectorization, prompt design, and citations.
[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) adds
the review standard in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}):
at 23:00-27:38, he ties gold tests and failure categories to traceable logs.

## Common Definition

Across the podcast archive, guests treat a strong RAG portfolio project as the
full retrieval loop, not only a chat UI over files. The project ingests source
documents and splits them into useful chunks. It keeps source metadata, retrieves
evidence for a question, and gives that evidence to the model. The answer cites
the sources a reader can open.

At 35:49-42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
Atita gives the most direct project model. Long transcripts need chunking and
overlap. Each retrieved passage needs provenance before the answer can cite it.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the production
reason in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46-46:42, she frames retrieval as a better fit than repeated retraining
when knowledge changes. The answer still has to stay grounded in indexed
documents.

The same project should make evaluation visible. Hugo's discussion at
23:00-27:38 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
supports a small gold set with expected evidence, acceptable answers, and
failure labels. [Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }})
adds the search-system view in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}):
at 12:45-17:40, he separates candidate retrieval from ranking. At 34:00-45:11,
he discusses hybrid search with filters, recency, and query-time weights.

## Guest Differences

Guests mostly differ on which part of the project needs the strongest proof.
Atita starts from search engineering. Her RAG standard emphasizes chunking,
metadata, and vector search choices. It also covers prompt context, citations,
and multi-level retrieval evaluation
([Modern Search Systems, 17:01-48:09]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})).
That view treats a
[vector database]({{ '/wiki/vector-databases/' | relative_url }}) as one
possible retrieval component, not as the whole project.

Hugo starts from practical LLM shipping. For him, RAG is a quick business win
when the knowledge base fits the task. Chunking and embeddings also need to fit.
Teams should add tools or
[agents]({{ '/wiki/agent-engineering/' | relative_url }}) only when the system
needs more than lookup. The system may need to take actions, call APIs, or
coordinate multiple steps
([Practical LLM Engineering and RAG, 44:26-56:21]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})).

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) draws a
similar boundary from agent engineering. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she argues at 29:30-37:39 that RAG still matters when latency and cost constrain
the system. Noisy context, chunk metadata, and source quality matter too.

At 51:17-57:23, she extends evaluation to custom datasets, mocked tools, and
integration tests. Outcome assertions matter for agentic RAG too.

Meryem frames the project against fine-tuning and deployment choices, and her
production episode supports RAG when knowledge changes. It asks the project to
name API risk, model drift, latency, and cost. Privacy and serving tradeoffs
also matter
([Deploying LLMs in Production, 18:46 and 49:44-51:35]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})).

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) adds a domain
modeling boundary. When relationships matter, a graph-backed retrieval design
can be more useful than nearest-neighbor text chunks
([Knowledge Graphs and LLMs for Automotive R&D, 33:43-42:42]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})).

## Source-Cited Knowledge Assistant

A source-cited knowledge assistant is the safest first RAG portfolio project.
Use a corpus where grounding matters. Podcast transcripts and policy documents
work well. Course notes and product manuals also work. Support tickets and
research papers are useful when the project can cite exact passages.

The project should show example questions and retrieved passages. It should also
show answer citations and refusals when the corpus lacks evidence.

Atita's transcript-chatbot discussion at 35:49-42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
supports this structure directly. She moves from long podcast transcripts to
chunking and overlap. She then covers embeddings, retrieval, augmentation,
and generation. Prompt design and citations complete that path. For this kind
of portfolio, a useful README should show the retrieved transcript sections and
the citation linked by the answer.

The assistant should expose missed evidence, not hide it. Atita discusses
multi-level RAG evaluation at 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Hugo gives a failure-analysis workflow at 26:43 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
that supports labeling failures as retrieval, generation, formatting, or source
preparation problems.

## Search-First RAG System

A search-first RAG project proves retrieval quality before generation makes the
demo look fluent. Start with keyword search or another simple baseline. Then
compare vector retrieval with filters or recency. Add hybrid search or reranking
when the corpus needs them.

In Daniel's
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
episode, he separates candidate generation from ranking at 12:45. At 17:40, he
recommends existing search engines instead of hand-rolled indexes.

At 27:21-34:00, he covers vector databases and vector compute. He also covers
ingestion encoding, query-time encoding, and hybrid search. At 1:01:25-1:03:50,
he ties search quality to business metrics and A/B tests, then connects it to
offline evaluation and fast iteration.

This project is strongest when the README compares retrieval approaches on the
same questions. A candidate for search roles can show precision-oriented
examples before generated answers. A candidate for
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) or
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
roles can add retrieved chunk ranks, filters, and failure cases.

## Evaluation And Failure Analysis Project

An evaluation-focused RAG project can start from an ordinary demo and make it
measurable. Build a small gold set. Each row should include a question, expected
evidence, and an acceptable answer. Add failure labels.

Store retrieved chunks and scores for each run, plus the prompt and model
versions. The run log should also include the answer, latency, cost, and
feedback.

Hugo gives this structure in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 23:00-25:25, he argues for representative gold tests. At 26:43, he
recommends categorizing failures so the next fix goes to retrieval or prompting.
Formatting and data preparation can be separate failure classes. At 27:38, he
connects logs and traces to a debuggable MVP.

Ranjitha extends the same idea when retrieval becomes one tool inside a larger
[AI agent]({{ '/wiki/ai-agents/' | relative_url }}) workflow. Her agent
evaluation discussion at 51:17-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
supports custom datasets, mocked tools, integration tests, and outcome
assertions. A portfolio project can show this with a compact evaluation report.
Include the query, expected evidence, and retrieved evidence. Include the
answer, failure class, and next retrieval fix too.

## Graph Or Domain RAG Project

Some RAG portfolio projects should model relationships instead of relying only
on nearest-neighbor text chunks. Paper citations and regulatory clauses can need
explicit entities, edges, and paths. Simulation parts, service incidents, and
customer tickets can need the same structure.

Anahita's
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
episode supports this project type. At 33:43, she connects knowledge graphs with
LLM grounding and RAG. At 38:10-39:56, she contrasts text chunking and
embeddings with graph semantics. She also discusses vector databases and
Cypher-driven retrieval.

At 42:42-47:10, she discusses trust and hallucination, plus verification limits
and paper parsing. She also covers graph visualization, PageRank, and references.

A strong [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
portfolio project tests both retrieval paths against the same questions. It can
show text similarity for passages and graph traversal for relationships. It
should also show when the answer needs to say the evidence is insufficient.

## Career-Transition RAG Project

A career-transition RAG project should connect the builder's previous domain to
current AI engineering practice. The project works best when it uses domain
documents the builder understands. It should then prove modern engineering
choices through chunking, retrieval baselines, and citations. Tests, logs, and
deployment boundaries matter too.

[Revathy Ramalingam]({{ '/people/revathyramalingam/' | relative_url }}) gives a
career-break example in
[How to Become an AI Engineer After a Career Break]({{ '/podcasts/s23e04-how-to-become-ai-engineer-after-career-break/' | relative_url }}).
Her 22:15 chapter covers building prototypes with AI developer tools, and her
33:45 chapter covers an interview task that uses a PDF Q&A assistant. Her
episode connects portfolio work to visible project evidence during a restart.

[Paul Iusztin]({{ '/people/pauliusztin/' | relative_url }}) adds the AI
engineering framing in
[his AI engineering episode]({{ '/podcasts/s23e01-ai-engineering-skill-stack-agents-llmops-and-how-to-ship-ai-products/' | relative_url }}).
At 29:12, he places RAG and knowledge management inside the AI engineer skill
stack. At 54:05, he connects portfolio work with a "second brain" project. That
supports a personal knowledge assistant when the project also shows software
quality, evaluation, and knowledge-management judgment.

## Production-Minded RAG Demo

A production-minded demo doesn't need production scale, but it should name the
constraints a real team would face. Document how the system reindexes sources
and which model versions it uses. Add embedding versions and latency. Include
cost, privacy limits, and hosted API risks.

Meryem's
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
episode supports that checklist. At 18:46, she discusses hidden API changes and
model drift. At 49:44-51:35, she compares hosted APIs with open-source serving
and covers latency, cost, and hardware. Deployment tradeoffs belong in the same
review. These constraints connect the project to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}).

Ranjitha's RAG reality check at 29:30-37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
adds another production boundary. Long context, agents, and vector databases do
not remove the need to manage source quality and noisy context. Teams still need
to manage chunk metadata, latency, and cost.

## Related Pages

These pages cover the concepts and project standards around RAG portfolio work.

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}) for the core RAG architecture.
- [Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }}) for a practical review checklist.
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}) for retrieval architecture and knowledge-system tradeoffs.
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}) for gold sets, traces, and failure analysis.
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}) for deployment, latency, cost, observability, and model-risk context.
- [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}) for deciding whether changing knowledge belongs in retrieval or model adaptation.
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) and [Embeddings]({{ '/wiki/embeddings/' | relative_url }}) for retrieval infrastructure choices.
- [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }}) for projects where relationships matter as much as text similarity.
- [Machine Learning Portfolio Projects]({{ '/wiki/machine-learning-portfolio-projects/' | relative_url }}) for the broader project-evidence standard.
- [Career Transition]({{ '/wiki/career-transition/' | relative_url }}) and [Job Search]({{ '/wiki/job-search/' | relative_url }}) for turning the project into hiring evidence.
