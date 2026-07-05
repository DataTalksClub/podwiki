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

After choosing a search or RAG project idea, this checklist turns one specific
system into a reviewable README, notebook, or project page. [[RAG Portfolio Projects]]
covers project categories and role signals, while
[[rag-evaluation-workflow=>RAG Evaluation Workflow]] covers the evaluation
procedure.

For the chosen project, prove retrieval before generation. A reviewer should see
the inputs, retrieval behavior, answer behavior, and evaluation trace. Those
fields make the work reviewable as a retrieval system, not only as a chat UI.

Show these parts on the project page:

- corpus choice and chunking
- retrieval baselines and citations
- evaluation, traces, and production tradeoffs

Use [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the
base concept and [[rag-evaluation-workflow=>RAG Evaluation Workflow]] for the
detailed eval workflow.
For sequencing retrieval work inside a larger product plan, use the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].

[[person:atitaarora=>Atita Arora]] starts from retrieval plus generation for
RAG projects
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
She applies that design to transcript question answering and chunking. The same
discussion covers prompt context, citations, and evaluation criteria.

[[person:hugobowneanderson=>Hugo Bowne-Anderson]] adds
the debugging standard. He recommends representative gold test sets, ranked
failure categories, and MVP logs and traces
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].

## Corpus Evidence and Chunking

Choose the corpus named by the project idea, such as podcast transcripts or
support docs. Policy documents, research papers, product manuals, and wiki
exports can also work. The corpus only works when the answer needs source
grounding and the project can cite those sources.

Show why that corpus needs retrieval and what a citation references. For
transcript data, cite the episode and guest. For documents, cite the title and
section. Add the version and source owner when that metadata exists.

Chunking is a design choice, not a cleanup detail. Podcast data can be chunked
by speaker turn or question. It can also be chunked by chapter or time window.
Documents can be chunked by heading, section, or a sliding token window.

Atita's transcript example uses chunking and overlap with embeddings and
retrieval. The answer path then includes prompt design and citations
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@35:49=>Transcript RAG Chatbot]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Chunking, Overlap, and Embeddings]].
The same project evidence belongs with
[[Embeddings]] and
[[Vector Databases]].

Large context windows don't remove chunking decisions.
[[person:lavanyagupta=>Lavanya Gupta]] discusses
long-context evaluation and degradation
[[cite:applied-llm-research-and-career-growth-in-practice=>Applied LLM Research and Career Growth]].
A project can cite that evidence when it tests chunk size, overlap, and
retrieval count instead of stuffing every source into one prompt.

## Retrieval Baselines

Build retrieval before generation by starting with keyword search or another
simple baseline. Compare vector retrieval, filters, reranking, and hybrid
search on the same questions before asking the LLM to write final answers. A
search-first project can show where keyword search wins, where embeddings win,
and where metadata filters are required.

[[person:danielsvonava=>Daniel Svonava]] supports that
order by separating candidate retrieval from ranking, explaining embeddings,
and covering hybrid search with filters and recency
[[cite:building-production-search-systems=>Building Search Systems]].

Link to [[Vector Database vs Search Engine]] when the project compares a
standalone vector store with an existing search stack. Link to
[[Production Search Evaluation]] and [[search-relevance=>search relevance]]
when relevance metrics or business outcomes matter.

[[person:meryemarik=>Meryem Arik]] gives the RAG reason
for this baseline work. Retrieval fits knowledge that changes too often for
repeated fine-tuning. Document indexing and retrieved sections support grounded
summarization
[[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]].
That boundary belongs with
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]]
and
[[LLM Production Patterns]].

## Context, Citations, and System Boundary

The generated answer should be inspectable. Show the query and retrieved
chunks, then include scores and source metadata. The trace should also include
prompt context, answer, and citations. If the system refuses to answer, show
which missing evidence caused the refusal. If it answers, link each claim to a
source chunk a reviewer can open.

Atita's RAG discussion places prompt design and citations after retrieval
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]].
In the review, first prove the retriever found useful context. Then prove the
prompt used it correctly.

[[person:ranjithakulkarni=>Ranjitha Kulkarni]] draws the
boundary between RAG and agents
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
She separates cases where retrieval is enough from cases that need planning,
actions, or tool use.
A project should stay with RAG when the main task is source lookup and grounded
answering. Move toward
[[agent-engineering=>AI Agents]] or
[[Agent Engineering]] only when
the task requires API calls, multi-step coordination, or external actions.

## Evaluation Artifacts

Show enough evaluation evidence for a reviewer to trust the project. Keep the
full procedure on [[rag-evaluation-workflow=>RAG Evaluation Workflow]]. In this
checklist, verify that reviewers can see the tests, traces, and failure labels
that support the project claim.

At minimum, link each eval run to:

- the question and expected evidence
- retrieved sources and scores
- prompt version
- model version
- answer
- citations
- latency, cost, and review labels

[[person:hugobowneanderson=>Hugo Bowne-Anderson]] gives
the core evaluation structure
[[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]].
Use [[rag-evaluation-workflow=>RAG Evaluation Workflow]] for gold examples,
retrieved-context checks, and answer scoring. It also covers human review and
production feedback.

Ranjitha extends the same idea to tool and agent workflows with custom datasets,
mocked tools, integration tests, and outcome assertions
[[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]].
That agent-evaluation evidence belongs with [[LLM Evaluation Workflows]] and
[[Testing]].

## Graph or Structured Retrieval

Some projects need more than nearest-neighbor text retrieval.
[[person:anahitapakiman=>Anahita Pakiman]] connects
knowledge graphs with LLM grounding
[[cite:knowledge-graphs-and-llms-for-automotive-rnd=>Knowledge Graphs and LLMs for Automotive R&D]].
She contrasts text chunking and embeddings with graph semantics. She also
discusses prompt templates that use Cypher-style graph queries for retrieval
context.

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
shows the corpus and chunking strategy. It should also show the metadata schema
and retrieval baseline. Reviewers should see retrieval comparisons, prompt
context, and citation behavior. They should also see the evaluation set,
failure labels, and traces.

The strongest projects include negative examples such as missing evidence and
stale chunks. They also show wrong citations, weak filters, high latency, or
plausible answers that aren't grounded.

A source-cited assistant belongs with
[[RAG Portfolio Projects]].
A search-first system belongs with
[[Information Retrieval]]
and
[[Production Search Evaluation]].
A focused evaluation pass belongs with
[[rag-evaluation-workflow=>RAG Evaluation Workflow]].
A production-minded LLM project should connect retrieval decisions to
[[LLM Production Patterns]]
and the
[[llm-rag-production-roadmap=>LLM and RAG Production Roadmap]].
