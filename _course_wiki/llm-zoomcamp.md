---
schema_type: Course
title: "LLM Zoomcamp"
summary: "DataTalks.Club's free ten-week course on building production LLM applications: agentic RAG, vector search, evaluation, monitoring, hybrid search, and reranking."
related_course:
  - Zoomcamps
  - AI Dev Tools Zoomcamp
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
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
and a [course FAQ](https://datatalks.club/faq/llm-zoomcamp.html).

## Curriculum

All modules, each with its lesson-level notes:

- [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
- [Module 2: Vector Search](/course-wiki/llmz-module-02/)
- [Module 3: Orchestration](/course-wiki/llmz-module-03/)
- [Module 4: Evaluation](/course-wiki/llmz-module-04/)
- [Module 5: Monitoring](/course-wiki/llmz-module-05/)
- [Module 6: Best Practices](/course-wiki/llmz-module-06/)
- [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)

- [**Module 1: Agentic RAG**](/course-wiki/llmz-module-01/) — build a RAG pipeline with keyword search, add
  [embeddings](/course-wiki/embeddings/) and
  [vector search](/course-wiki/vector-search/), then make it agentic with
  [function calling](/course-wiki/function-calling/)
  ([RAG](/course-wiki/rag/), [agentic RAG](/course-wiki/agentic-rag/)).
- [**Module 2: Vector Search**](/course-wiki/llmz-module-02/) — semantic search with
  [embeddings](/course-wiki/embeddings/) across minsearch, sqlitesearch, and
  PGVector.
- **Module 3: AI Orchestration** — LLM workflows as
  [Kestra](/course-wiki/kestra/) orchestrations
  ([workflow orchestration](/course-wiki/workflow-orchestration/)).
- **Workshop: Data Ingestion** — [dlt](/course-wiki/dlt/) pipelines for
  ingesting and analyzing LLM traces, with filesystem and REST API sources,
  DuckDB, and marimo dashboards.
- [**Module 4: Evaluation**](/course-wiki/llmz-module-04/) — measuring retrieval and answer quality, offline
  and online ([LLM evaluation](/course-wiki/llm-evaluation/)).
- [**Module 5: Monitoring**](/course-wiki/llmz-module-05/) — user feedback, system health, and live dashboards
  ([LLM monitoring](/course-wiki/llm-monitoring/)).
- [**Module 6: Best Practices**](/course-wiki/llmz-module-06/) — [LangChain](/course-wiki/langchain/),
  [hybrid search](/course-wiki/hybrid-search/) combining vector and keyword
  retrieval, and [reranking](/course-wiki/reranking/) for precision.
- **Module 7: End-to-End Project Example** — a complete fitness assistant
  built with LLMs.
- **Capstone** — a searchable knowledge base, retrieval pipeline, evaluation
  process, user-facing interface, and monitoring loop, all learner-owned.

## Who it is for

The course targets software engineers adding LLM and search capabilities to
real products, data engineers wiring retrieval pipelines into production
systems, and ML practitioners who want a structured way to evaluate and
monitor LLM-based applications. AI Dev Tools Zoomcamp is the complement for
the software-development workflow around such projects rather than the
application itself.

## Projects and certificate

The capstone requirements mirror what production RAG work actually needs:
ingest and store a chosen dataset, implement the full retrieve-assemble-call
flow, measure retrieval and answer quality with search metrics or
LLM-as-a-judge, expose a UI or API, and track queries and feedback over time.
Past cohort projects include fitness and nutrition assistants, study
companions, medical FAQ assistants, codebase Q&A bots, and news summarization
tools. Certificates require the capstone plus peer reviews of three peers'
projects during a live cohort.
