---
layout: wiki
title: "LLM Zoomcamp"
summary: "DataTalks.Club's free ten-week course on building production LLM applications: agentic RAG, vector search, evaluation, monitoring, hybrid search, and reranking."
related_course:
  - Zoomcamps
  - AI Dev Tools Zoomcamp
related:
  - LLMs
  - LLM RAG Production Roadmap
  - Retrieval-Augmented Generation
  - Vector Databases
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - RAG Portfolio Projects
---

LLM Zoomcamp is DataTalks.Club's free ten-week course on building practical,
production-ready LLM applications. It covers Retrieval-Augmented Generation,
vector search, embeddings, AI agents, function calling, evaluation,
monitoring, hybrid search, and reranking, and ends with a capstone: a
complete RAG application the learner designs, builds, evaluates, and ships.
No ML background, GPU, or expensive setup is required — confident Python,
command-line comfort, basic Docker familiarity, and a few dollars of API
credits cover it.

All materials are open source in the
[course repository](https://github.com/DataTalksClub/llm-zoomcamp), with
videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv),
a [course FAQ](https://datatalks.club/faq/llm-zoomcamp.html), and a
[course overview article](https://datatalks.club/blog/llm-zoomcamp.html). It
is part of the [Zoomcamps](/course-wiki/zoomcamps/) family.

## Curriculum

The [repository syllabus](https://github.com/DataTalksClub/llm-zoomcamp)
maps the modules:

- **Agentic RAG** — build a RAG pipeline with keyword search, then make it
  agentic with function calling ([Retrieval-Augmented Generation](/wiki/retrieval-augmented-generation/),
  [Agent Engineering](/wiki/agent-engineering/)).
- **Vector search** — semantic search with embeddings across minsearch,
  sqlitesearch, and PGVector ([Embeddings](/wiki/embeddings/), [Vector Databases](/wiki/vector-databases/),
  [Vector Search vs Keyword Search](/wiki/vector-search-vs-keyword-search/)).
- **Orchestration** — AI orchestration with Kestra ([Orchestration](/wiki/orchestration/)).
- **Workshop: data ingestion** — dlt pipelines for ingesting and analyzing
  LLM traces, with filesystem and REST API sources, DuckDB, and marimo
  dashboards.
- **Evaluation** — measuring retrieval and answer quality, offline and online
  ([Evaluation](/wiki/evaluation/), [LLM Evaluation Workflows](/wiki/llm-evaluation-workflows/)).
- **Monitoring** — user feedback, system health, and live dashboards
  ([Agent Ops](/wiki/agent-ops/) for the operations boundary).
- **Best practices** — LangChain, hybrid search combining vector and keyword
  retrieval, and reranking for precision.
- **End-to-end project example** — a complete fitness assistant built with
  LLMs.
- **Capstone** — a searchable knowledge base, retrieval pipeline, evaluation
  process, user-facing interface, and monitoring loop, all learner-owned.

## Who it is for

The course targets software engineers adding LLM and search capabilities to
real products, data engineers wiring retrieval pipelines into production
systems, and ML practitioners who want a structured way to evaluate and
monitor LLM-based applications. [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) is the complement
for the software-development workflow around such projects rather than the
application itself.

## Projects, portfolio, and certificate

The capstone requirements mirror what production RAG work actually needs:
ingest and store a chosen dataset, implement the full retrieve-assemble-call
flow, measure retrieval and answer quality with search metrics or
LLM-as-a-judge, expose a UI or API, and track queries and feedback over time.
Past cohort projects include fitness and nutrition assistants, study
companions, medical FAQ assistants, codebase Q&A bots, and news
summarization tools, browsable from the
[2025 cohort gallery](https://courses.datatalks.club/llm-zoomcamp-2025/projects).

Certificates require the capstone plus peer reviews of three peers' projects
during a live cohort. [RAG Portfolio Projects](/wiki/rag-portfolio-projects/) treats these capstones as
strong application-layer evidence, and the
[2024 competition winners](https://datatalks.club/blog/winning-solutions-from-llm-zoomcamp-2024-competition.html)
show the upper range of what learners ship.

## What the podcast adds

The course grew out of the LLM engineering practice the podcast covers week
to week: retrieval-first architectures, evaluation loops, and cost-aware
deployment. The course portfolio that added LLMs alongside ML, data
engineering, and MLOps is described in the DataTalks.Club scaling discussion.
[Inside Scaling DataTalks.Club](https://datatalks.club/podcast/datatalksclub-scaling-and-free-courses.html)
Learners returning after career breaks use LLM Zoomcamp-style projects —
such as a PDF Q&A assistant built for interviews — as concrete, discussable
evidence of shipped AI systems.
[How to Become an AI Engineer After a Career Break](https://datatalks.club/podcast/s23e04-how-to-become-ai-engineer-after-career-break.html)

For the full production sequence, the [LLM and RAG Production Roadmap](/wiki/llm-rag-production-roadmap/)
orders these same concerns from prototype to operated system, and
[LLM Production Patterns](/wiki/llm-production-patterns/) collects the recurring architecture decisions.

## Related Pages

- [Zoomcamps](/course-wiki/zoomcamps/)
- [LLMs](/wiki/llms/)
- [LLM and RAG Production Roadmap](/wiki/llm-rag-production-roadmap/)
- [Retrieval-Augmented Generation](/wiki/retrieval-augmented-generation/)
- [Vector Databases](/wiki/vector-databases/)
- [LLM Evaluation Workflows](/wiki/llm-evaluation-workflows/)
- [RAG Portfolio Projects](/wiki/rag-portfolio-projects/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
