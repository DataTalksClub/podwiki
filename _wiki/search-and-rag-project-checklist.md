---
layout: wiki
title: "Search and RAG Project Checklist"
summary: "Archive-backed checklist for a search or RAG portfolio project that proves retrieval quality, context design, citations, evaluation, tracing, and production tradeoffs."
related:
  - Portfolio Projects
  - RAG Portfolio Projects
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - Vector Databases
  - Graph RAG vs Vector RAG
---

A search or RAG project proves retrieval before generation. A reviewer should
see the corpus, chunking plan, metadata, and retrieved chunks. The same review
should show prompt context, citations, evaluation results, and failure labels.
Those review signals make the project a retrieval system, not only a chat UI.

Pair this checklist with
[Portfolio Projects]({{ '/wiki/portfolio-projects/' | relative_url }}),
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }}),
and the base concept in
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).
For the surrounding topic map, start with
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
Use [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
and
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the core structure
in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38, she defines RAG as retrieval plus generation. At 35:49, she applies
that design to podcast transcript question answering. At 38:24, she discusses
chunking and overlap. At 42:49, she moves from retrieval into prompt context
and citations.

Her 48:09 evaluation discussion turns those implementation choices into review
criteria.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) adds
the debugging standard in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}):
at 23:00-25:25, he argues for representative gold test sets. At 26:43, he
recommends ranking and categorizing failures. At 27:38, he ties a debuggable
MVP to logs and traces.

## Corpus and Chunking

Choose a corpus where grounding matters. Podcast transcripts, support docs,
policy documents, and research papers work well. Product manuals and internal
wiki exports also work.

The project should show why the corpus needs retrieval and what a citation
references. For transcript data, cite the episode and guest plus the timestamp
and nearby speaker context. For documents, cite the title and section plus the
version and source owner when that metadata exists.

Chunking is a design choice, not a cleanup detail. Podcast data can be chunked
by speaker turn or question. It can also be chunked by chapter or time window.
Documents can be chunked by heading, section, or a sliding token window.

Atita's transcript example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
uses chunking and overlap at 35:49-42:49. It also uses embeddings, retrieval,
prompt design, and citations. The same project evidence belongs with
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}) and
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}).

Large context windows don't remove chunking decisions.
[Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }}) discusses
long-context evaluation and degradation at 10:15-14:54 in
[Applied LLM Research and Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}).
A project can use that evidence to justify testing chunk size, overlap, and
retrieval count instead of stuffing every source into one prompt.

## Retrieval Baselines

Build retrieval before generation by starting with keyword search or another
simple baseline. Compare vector retrieval, filters, reranking, and hybrid
search on the same questions before asking the LLM to write final answers. A
search-first README can show where keyword search wins, where embeddings win,
and where metadata filters are required.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) supports that
order in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
He separates candidate retrieval from ranking at 12:45 and explains embeddings
at 21:55. At 34:00, he covers hybrid search with filters and recency.

Use
[Vector Database vs Search Engine]({{ '/wiki/vector-database-vs-search-engine/' | relative_url }})
when the project compares a standalone vector store with an existing search
stack. Use
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
when relevance metrics or business outcomes matter.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the RAG reason
for this baseline work in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46, she favors retrieval when knowledge changes too often for repeated
fine-tuning. At 42:02 and 46:42, she describes document indexing, retrieved
sections, and summarization for grounding. That boundary belongs with
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
and
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }}).

## Context, Citations, and Boundaries

The generated answer should be inspectable. Show the query and retrieved
chunks, then include scores and source metadata. The trace should also include
prompt context, answer, and citations. If the system refuses to answer, show
which missing evidence caused the refusal. If it answers, link each claim to a
source chunk a reviewer can open.

Atita's RAG discussion at 42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
places prompt design and citations after retrieval. The project should preserve
that order: first prove the retriever found useful context, then prove the
prompt used it correctly.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) draws the
boundary between RAG and agents in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 37:39, she separates cases where retrieval is enough from cases that need
planning, actions, or tool use. A project should stay with RAG when the main
task is source lookup and grounded answering. Move toward
[AI Agents]({{ '/wiki/ai-agents/' | relative_url }}) or
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) only when
the task requires API calls, multi-step coordination, or external actions.

## Evaluation and Traces

Create a small gold set. For each question, store expected evidence and
acceptable answers, then add failure labels and notes about retrieval quality.
The trace should make it possible to separate retrieval failures from generation
failures before adding agents, fine-tuning, or prompt complexity.

Store these trace fields with each run:

- scores
- prompt version
- model version
- answer
- latency
- cost
- feedback

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) gives
the core evaluation structure at 23:00-27:38 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
Representative gold tests make the system measurable. Failure categories tell
the team whether the next fix belongs in retrieval, prompting, formatting, or
data preparation. Logs and traces make those decisions reviewable.

Ranjitha extends the same idea to tool and agent workflows at 51:17-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
She covers custom datasets, mocked tools, integration tests, and outcome
assertions.
That agent-evaluation evidence belongs with
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
and [Testing]({{ '/wiki/testing/' | relative_url }}).

## Graph or Structured Retrieval

Some projects need more than nearest-neighbor text retrieval. In
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) connects
knowledge graphs with LLM grounding at 33:43. At 38:10, she contrasts text
chunking and embeddings with graph semantics. At 39:56, she discusses prompt
templates that use Cypher-style graph queries for retrieval context.

Use [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
or
[Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
when questions depend on explicit relationships, provenance paths, entities, or
domain semantics.

Graph or structured retrieval changes the portfolio evidence too. A vector RAG
project should show chunks, embeddings, similarity scores, and citation metadata. A
graph RAG project should show entity and relationship definitions, query
results, graph paths, and provenance. Hybrid retrieval should show whether each
answer part came from semantic search, structured lookup, filters, or reranking.

## Portfolio Review Checklist

A search or RAG project is ready to review when the page, notebook, or README
shows the corpus and chunking strategy. It should also show the metadata schema
and retrieval baseline. Reviewers should see retrieval comparisons, prompt
context, and citation behavior. They should also see the evaluation set,
failure labels, and traces.

The strongest projects include negative examples such as missing evidence and
stale chunks. They also show wrong citations, weak filters, high latency, or
plausible answers that aren't grounded.

A source-cited assistant belongs with
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }}).
A search-first system belongs with
[Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).
A production-minded LLM project should connect retrieval decisions to
[LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
and the
[LLM and RAG Production Roadmap]({{ '/wiki/llm-rag-production-roadmap/' | relative_url }}).
