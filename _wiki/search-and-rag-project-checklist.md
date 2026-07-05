---
layout: wiki
title: "Search/RAG Project Checklist"
summary: "Review checklist for one chosen search or RAG implementation: corpus, chunking, baselines, citations, evaluation artifacts, traces, and production constraints."
related:
  - Portfolio Projects
  - RAG Portfolio Projects
  - Retrieval-Augmented Generation
  - RAG Evaluation Workflow
  - LLM Evaluation Workflows
  - Production Search Evaluation
  - LLM Production Patterns
  - Vector Databases
  - Graph RAG vs Vector RAG
---

After a search or RAG project exists, use this checklist to test the evidence.
The README, notebook, or project page should give reviewers enough context to
judge it.
For project categories and role signals, use [[RAG Portfolio Projects]]. For architecture, use
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]].

A reviewer should see retrieval before generation:

- corpus and chunking
- retrieval behavior
- answer behavior and citations
- evaluation trace
- production constraints

Those fields make the work reviewable as a retrieval system, not only as a chat
UI.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

[[rag-evaluation-workflow=>RAG Evaluation Workflow]] covers detailed evaluation
design. [[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]] covers
sequencing retrieval work inside a larger product plan.

## Corpus Evidence and Chunking

Review the corpus the project already chose. Name the source collection, explain
why retrieval is needed, and show what a citation references.
The corpus only works when the answer needs source grounding and the project can
cite those sources.

Show why that corpus needs retrieval and what a citation references. For
transcript data, cite the episode and guest. For documents, cite the title and
section. Add the version and source owner when that metadata exists.

Chunking is a design choice, not a cleanup detail. Podcast data can be chunked
by speaker turn or question. It can also be chunked by chapter or time window.
Documents can be chunked by heading, section, or a sliding token window.

Transcript RAG review should show these fields in the implementation evidence:

- chunking and overlap before retrieval
- embeddings
- prompt design and citations

[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@35:49=>Transcript RAG Chatbot]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Chunking, Overlap, and Embeddings]]
Link the implementation to [[Embeddings]] and [[Vector Databases]] when the
project page explains embedding or vector-store choices.

Large context windows don't remove chunking decisions. Cite long-context
evidence when testing chunk size, overlap, and retrieval count instead of
stuffing every source into one prompt.[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research and Career Growth]]

## Retrieval Baselines

Review retrieval before generation by starting with keyword search or another
simple baseline. Compare vector retrieval, filters, reranking, and hybrid search
on the same questions before asking the LLM to write final answers. Review
candidate retrieval and ranking separately. Treat embeddings, filters, and
recency as separate fields too.[[cite:building-production-search-systems=>Building Search Systems]]

Link to [[Vector Database vs Search Engine]] when the project compares a
standalone vector store with an existing search stack. Link to
[[Production Search Evaluation]] and [[search-relevance=>search relevance]]
when relevance metrics or business outcomes matter.

Retrieval fits knowledge that changes too often for repeated fine-tuning.
Document indexing and retrieved sections support grounded summarization.[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]
That boundary belongs with [[rag-vs-fine-tuning=>RAG vs Fine-Tuning]] and
[[LLM Production Patterns]].

## Context, Citations, and System Boundary

The generated answer should be inspectable. Show the query and retrieved
chunks, then include scores and source metadata. The trace should also include
prompt context, answer, and citations. If the system refuses to answer, show
which missing evidence caused the refusal. If it answers, link each claim to a
source chunk a reviewer can open.

Prompt design and citations follow retrieval in the review trace.[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
First show the retriever found useful context. Then show the prompt used it
correctly. The architecture explanation lives in
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]. Use this
page for the screenshots, tables, traces, and links that make the implementation
inspectable.

A project should stay with RAG when the main task is source lookup and grounded
answering. Move toward [[agent-engineering=>AI Agents]] or
[[Agent Engineering]] only when the task requires API calls, multi-step
coordination, or external actions.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]

## Evaluation Artifacts

Show enough evaluation evidence for a reviewer to trust the project. Keep the
full procedure on [[rag-evaluation-workflow=>RAG Evaluation Workflow]]. In this
checklist, verify that the project page links to the tests, traces, and failure
labels that support the project claim.

At minimum, link each eval run to:

- the question and expected evidence
- retrieved sources and scores
- prompt version
- model version
- answer
- citations
- latency, cost, and review labels

Core evaluation evidence should include representative tests, failure labels,
and logs or traces.[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]

[[rag-evaluation-workflow=>RAG Evaluation Workflow]] covers gold examples and
retrieved-context checks. It also covers answer scoring, human review, and
production feedback.

Agent workflows need custom datasets, mocked tools, integration tests, and
outcome assertions.[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]
That evidence belongs with [[LLM Evaluation Workflows]] and [[Testing]].

## Graph or Structured Retrieval

Some projects need more than nearest-neighbor text retrieval. Knowledge graphs
can add entities, relationships, graph paths, and Cypher-style query results to
retrieval context.[[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]]

Link to [[Graph RAG vs Vector RAG]] or [[Knowledge Graph vs Vector Search]] when
questions depend on explicit relationships, provenance paths, entities, or domain
semantics.

Graph or structured retrieval changes the checklist fields too. A vector RAG
project should show chunks, embeddings, similarity scores, and citation
metadata. A graph RAG project should show entity and relationship definitions,
query results, graph paths, and provenance. Hybrid retrieval should show whether
each answer part came from semantic search, structured lookup, filters, or
reranking.

## Review-Ready Evidence

A search or RAG project is ready to review when the page, notebook, or README
shows these fields:

- corpus and chunking strategy
- metadata schema
- retrieval baseline and comparisons
- prompt context and citation behavior
- evaluation set, failure labels, and traces

Strong projects include negative examples:

- missing evidence
- stale chunks
- wrong citations
- weak filters
- high latency
- plausible answers that aren't grounded

Those fields come from review work across transcript RAG, production search, and
agent traces. A reviewer needs to see retrieval choices and failure points
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]
[[cite:building-production-search-systems=>Building Search Systems]]
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].

When the project is also hiring evidence, link the finished checklist back to
[[RAG Portfolio Projects]]. Use that page for the project story and this
checklist for review evidence. If it's mainly a search system, connect the checklist to
[[Information Retrieval]], [[Production Search Evaluation]], and
[[search-relevance=>search relevance]]. For production-minded LLM projects,
connect retrieval decisions to [[LLM Production Patterns]] and the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].
