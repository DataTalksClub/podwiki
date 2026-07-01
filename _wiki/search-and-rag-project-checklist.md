---
layout: wiki
title: "Search and RAG Project Checklist"
summary: "Archive-backed checklist for a search or RAG portfolio project that proves retrieval quality, context design, citations, evaluation, tracing, and production tradeoffs."
related:
  - RAG Portfolio Projects
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - LLM Evaluation Workflows
  - LLM Production Patterns
  - Vector Databases
  - Graph RAG vs Vector RAG
---

## Definition

A search or RAG project proves that retrieval works before generation tries to
answer. The project should show the corpus, chunking, and metadata. It should
also show retrieval strategy and prompt context. Citations, evaluation, and
failure analysis complete the proof.

Use this checklist with
[RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }}),
then use
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
for the base concept. Use
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for adjacent concepts.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the backbone in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38, she defines retrieval-augmented generation as retrieval plus
generation. At 35:49, she applies it to podcast transcript question answering.
At 38:24, she discusses chunking and overlap. She also covers embeddings and
vectorization.

At 42:49, she connects retrieval and context while also covering prompt design
and citations.

## Common Definition

Guests describe a strong RAG project as the full retrieval loop. It should show
the user's query, retrieved chunks, and source metadata. It should also show
the context given to the model and the answer with citations.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) adds
the evaluation standard in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 23:00-25:25, he argues for representative gold test sets. At 26:43, he
recommends ranking and categorizing failures. At 27:38, he connects a
debuggable MVP to logs and traces.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) explains why RAG is
often better than retraining when knowledge changes. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she favors information retrieval for changing knowledge at 40:46. She explains
document indexing and grounding at 42:02.

## Guest Differences

Atita starts from search architecture. She treats chunking and metadata as core
work, and embedding, retrieval, and citations are core too.

Hugo starts from product debugging. His checklist begins with gold examples and
failure categories before logs and traces come next.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) starts
from agent engineering. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she keeps RAG in scope when latency, cost, and source quality are the main
constraints. Metadata is also part of the constraint set. At 37:39, she separates cases where RAG is enough from
workflows that need actions and planning.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) starts from
production search. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he separates candidate retrieval from ranking at 12:45 and explains embeddings
at 21:55. At 34:00, he covers hybrid search with filters and recency.

## Corpus And Chunking

Choose a corpus where source grounding matters. Podcast transcripts and support
docs work well, while policy documents and research papers also work. Product
manuals or internal wiki exports are useful too.

Chunking is a design choice. Podcast data may chunk by speaker turn or
question, and it may also chunk by chapter or time window. Documents may chunk
by heading or section.

Large context windows don't remove this work. [Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }}) discusses
long-context evaluation and degradation in
[Applied LLM Research and Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }})
at 10:15-14:54. Teams still chunk because models can become less reliable as
context grows.

## Retrieval Baselines

Build retrieval before generation by starting with keyword search or another
simple baseline. Then compare vector retrieval and filters. Add hybrid search
or reranking when the corpus needs them.

Daniel's production-search discussion supports that order. He separates
candidate retrieval from ranking at 12:45, then explains embeddings at 21:55
and hybrid search at 34:00.

Use [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}),
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}),
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }}), and
[Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
Use [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
when the project needs deeper search context.

## Evaluation And Traces

Create a small gold set. For each question, store expected evidence and
acceptable answers, then add failure labels and notes about retrieval quality.

Log the query and retrieved chunks.

Store these trace fields:

- scores
- prompt version
- model version
- answer
- latency
- cost
- feedback

Ranjitha extends the same idea to tool and agent workflows at 51:17-57:23 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
She covers custom datasets, mocked tools, integration tests, and outcome
assertions.

Separate retrieval failures from generation failures before adding agents,
fine-tuning, or prompt complexity.

## Graph Or Structured Retrieval

Some projects need more than nearest-neighbor text retrieval. In
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) connects
knowledge graphs with LLM grounding at 33:43. At 38:10, she contrasts text
chunking and embeddings with graph semantics.

Use [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
or
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
when questions depend on explicit relationships, provenance paths, entities, or
domain semantics.

## Related Pages

Use these pages to follow the retrieval and evaluation concepts.

- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
