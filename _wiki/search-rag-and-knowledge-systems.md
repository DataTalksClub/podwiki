---
layout: wiki
title: "Search, RAG, and Knowledge Systems"
summary: "How DataTalks.Club podcast guests connect retrieval, RAG, knowledge graphs, and production knowledge systems."
related:
  - Retrieval-Augmented Generation
  - Search
  - Information Retrieval
  - Vector Databases
  - Embeddings
  - Graph RAG vs Vector RAG
  - Knowledge Graph vs Vector Search
  - LLM Production Patterns
  - LLM Evaluation Workflows
  - Agent Engineering
---

Search, RAG, and knowledge systems are the retrieval layer behind many useful
AI and data products. In the DataTalks.Club podcast discussions, this layer
starts with [search]({{ '/wiki/search/' | relative_url }}) and
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
The system finds a small set of relevant items from a large collection. Then it
ranks or filters them before exposing them to a user, application, or model.

The same retrieval discipline now appears in
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and [vector databases]({{ '/wiki/vector-databases/' | relative_url }}). It also
appears in [embeddings]({{ '/wiki/embeddings/' | relative_url }}), graph
retrieval, and
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the clearest
bridge in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}):
at 30:38 she defines RAG as retrieval plus generation. At 38:24 she turns
podcast transcripts into chunks, embeddings, and vectorized context. At 48:09
she brings evaluation and human review back into the system.

A knowledge system is broader than a vector index or chatbot. The podcast
guests treat it as the product surface and retrieval pipeline. It also includes
metadata plus source provenance. Ranking logic and evaluation loops decide
which knowledge is usable.

The central podcast discussions cover search and RAG. They also cover vector
retrieval, graph retrieval, production boundaries, and
[agent engineering]({{ '/wiki/agent-engineering/' | relative_url }}).

## Retrieval, Ranking, and Context

Across these episodes, search and RAG systems are built around one common
mechanism. They retrieve candidate information, decide what belongs in front of
the user or model, and evaluate whether the downstream task improved.
[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) frames this as
a relevance decision in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
at 6:20, then separates candidate generation from ranking at 12:45.
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) applies the same
retrieval discipline to RAG in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 30:38-42:49.

RAG adds model context and generation, but it doesn't replace search. Atita's
transcript example starts with prepared documents and chunks. The system then
creates embeddings and retrieves relevant passages. It wraps them in prompt
context and returns citations
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
35:49-42:49). That makes RAG a product design built on
[search]({{ '/wiki/search/' | relative_url }}) and
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}),
not model memory.

These episodes also don't treat vector search as the whole system. Daniel
separates vector compute from vector storage at 29:00 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
and adds filters, recency, business rules, and ranking at 34:00-45:11. These
constraints connect vector databases to
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). Embedding models, indexes,
ranking weights, and user behavior all change over time.

## Search, Graph, and Agent Boundaries

Atita starts from the search stack. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
her 17:01 and 20:27 chapters compare standalone vector databases with adding
vectors to existing search infrastructure. Her RAG guidance emphasizes
chunking, prompt context, citations, and human-in-the-loop evaluation at
38:24-48:09.

Daniel starts from production retrieval and ranking. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he ties search to relevance at 6:20 and candidate generation to ranking at
12:45. He adds hybrid retrieval at 34:00-45:11 and business metrics at
1:01:25. His view fits products where search, recommendations, ecommerce, or
matching are the main surface. It isn't limited to chatbots.

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) starts from
domain relationships. Her
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
episode contrasts text chunks and vector databases with graph semantics at
38:10. At 39:56, she discusses Cypher-driven retrieval. Her view fits domains
where an answer depends on entities, paths, reports, or simulations. It also
fits cases where verification matters more than similar text.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
starts from practical LLM engineering. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
he puts representative gold tests around the RAG application at 23:00. He
separates failure categories at 26:43. He uses logs and traces at 27:38, then
compares chunking choices at 48:20.

His practical escalation point is to use RAG for knowledge lookup. Add tools or
agents when the workflow must take action.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) starts
from agent engineering. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she pushes back on "RAG is dead" at 29:30. Long context and agents still face
latency, cost, and noisy context. They also still face metadata quality and
source-quality constraints. At 36:11-37:39, she places retrieval as one tool
inside an agentic system rather than the whole system.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) starts from LLM
deployment. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she draws the boundary between retrieval for changing knowledge and
fine-tuning for behavior, style, or task adaptation at 40:46-46:42. That
boundary anchors
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}).

## Search-First Architecture

A search-first knowledge system makes retrieval visible before generation. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel separates the user-facing relevance problem at 6:20 from candidate
generation and ranking at 12:45. He then adds vector compute, vector storage,
hybrid search, and metrics across 27:21-45:11 and 1:01:25-1:03:50. A generated
answer can't compensate for missing or badly ranked evidence. The
retrieval unit, index, filters, and ranking logic matter before the LLM sees
anything.

For product search, teams may retrieve product or document records. They may
also retrieve images, sessions, or recommendation candidates. For RAG, they may
retrieve passages or chunks. They may also retrieve sections, entities, graph
paths, or source records. Both cases need metadata for filters and permissions.

They also need citations, freshness, and evaluation. Atita covers RAG
provenance at 38:24-48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
while Daniel covers filters, recency, and business constraints at 34:00-45:11
in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).

## RAG as Context Packaging

RAG turns retrieval results into model context. Atita's podcast-transcript
chatbot in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
shows the sequence at 35:49-42:49. The system ingests transcripts, chooses
chunks and overlap, then computes embeddings. It retrieves passages, places
them into a prompt, and returns citations. Chunk design is therefore part of
the user experience, not only a preprocessing detail.

Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
discussion adds the debugging loop. At 23:00 he emphasizes representative gold
tests. At 26:43 he separates failure categories. At 27:38 he brings in logs
and traces. At 48:20 he compares chunking and context-window strategies.

Those practices connect RAG to
[LLM evaluation workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
instead of leaving it as a demo.

Meryem gives the deployment reason for the same workflow in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46-46:42, she describes retrieval as the better fit when knowledge
changes and responses need grounding. That's why RAG belongs near
[LLM production patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
as well as near search.

## Vector Retrieval and Hybrid Search

Vector retrieval helps when exact words are brittle, when users ask
semantically similar questions in different language, or when the product needs
multimodal matching. Daniel's
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
episode covers dense representations at 11:29, vector databases at 27:21, and
CLIP-style text-to-image retrieval at 32:43. Those examples connect
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) to search,
recommendations, personalization, and RAG.

Hybrid search is the production default in these search discussions. Daniel
adds filters, recency, and popularity around vector similarity. He also adds
business rules and query-time weights at 34:00-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).

[Reem Mahmoud]({{ '/people/reemmahmoud/' | relative_url }}) covers the same
family of production concerns in
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}).
That episode moves from inverted indexes at 11:29 to embeddings at 21:55. It
then moves to vector compute at 29:00, hybrid search at 34:00, and operational
search metrics at 1:01:25.

This is why
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
is an architecture decision. It isn't a slogan about newer tools replacing
older search engines. A vector database can retrieve nearest neighbors. The
knowledge system still decides which metadata is mandatory, which signals are
soft ranking features, and how to evaluate the result.

## Knowledge Graphs and Structured Retrieval

Knowledge graphs become useful when the question is about relationships, not
only similarity. Anahita's
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
episode connects graph databases to changing automotive relationships at
16:31 and semantic reporting at 10:28. It also covers graph-backed RAG at
33:43-39:56 and verification at 42:42. The graph can preserve entities,
containment, and typed links. It can also preserve order, paths, and domain
semantics that plain chunks may lose.

Graph retrieval doesn't remove grounding work. Anahita's hallucination and
verification discussion at 42:42 in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
shows why graph facts still need validation, traceability, and review. Use
[Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
and
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
when deciding whether the context should be similar text, graph paths, or both.

## Evaluation and Operations

Evaluation has to separate retrieval quality from generation quality. Atita
discusses multi-level RAG evaluation and human-in-the-loop review at 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Hugo turns that into a workflow in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

Gold questions at 23:00 help teams test real cases. Failure categories at
26:43 help them decide whether the next fix belongs in retrieval, prompt
design, or data preparation. The fix may also belong in formatting or product
constraints. Logs and traces at 27:38 make those failures inspectable.

Production search also needs business measurement. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel ties search quality to revenue, A/B tests, and operational metrics at
1:01:25-1:03:50. That makes
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
the operational counterpart to RAG evaluation. A retriever can look good
offline and still fail on latency, cost, or conversion. It can also fail on
support resolution or user trust.

Ranjitha expands the evaluation problem when retrieval becomes part of an
agent. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she argues at 51:17-54:19 that teams need their own representative datasets,
integration tests, and mocked tools. They also need outcome checks. That
connects retrieval systems to
[AI agents]({{ '/wiki/ai-agents/' | relative_url }}) when the system does more
than answer from a document set.

## Production Boundaries

Use RAG when the system mostly answers from a changing knowledge base and needs
sources, citations, or reviewable evidence. Meryem's
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
discussion at 40:46-46:42 supports retrieval for changing knowledge, while
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}) captures
the boundary with model adaptation.

Use agents for planning and tool calls when the workflow needs API queries,
state lookup, or multi-step action. Ranjitha places retrieval as one tool
inside a larger workflow at 36:11-37:39 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
That adds latency, cost, integration, and evaluation burden.
[Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }}) covers in
more detail.

Use graph retrieval when relationship structure is part of the answer.
Anahita's 38:10-39:56 discussion in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
supports graph context for domains where entity links, typed paths, and
constraints matter. Use vector retrieval when semantic similarity over chunks,
images, or sessions is the main retrieval problem. Daniel shows that vector
case at 21:55-34:00 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).

## Practical Design Questions

Define the retrieval unit first. Atita's transcript example uses chunks in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 38:24. Anahita's automotive R&D example uses graph units in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
at 38:10.

Teams may retrieve products, documents, chunks, or images. They may also
retrieve sessions, entities, graph paths, database rows and API results.

Preserve the metadata that survives retrieval. Atita's citation flow depends
on source context at 42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Daniel's hybrid-search discussion at 34:00-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
shows why filters and recency need to be designed alongside vector similarity.
Weights and business rules need the same treatment. Anahita's graph retrieval
discussion shows why
relationships and paths may also be retrieval metadata, not only background
schema.

Choose the retrieval mode by failure mode. Keyword search helps when exact
terms and controlled filters matter. Vector search helps when semantic
similarity or multimodal matching matters. Hybrid retrieval helps when both
similarity and constraints matter.

Graph retrieval helps when relationship structure changes the answer, and this
routing rule comes from three anchors. Daniel's 11:29-45:11 search architecture
discussion in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
covers retrieval and hybrid ranking. Atita's 30:38-48:09 RAG pipeline in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
covers context packaging and evaluation. Anahita's 33:43-42:42 graph RAG
discussion in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
covers relationship-aware retrieval.

Retrieval shifts when source documents, permissions or embedding models change.
Chunking strategies or graph schemas can trigger similar work too. Prompts,
ranking weights, and user behavior can do the same. Daniel covers
embedding recomputation and model versioning at 29:00-33:13 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Meryem covers changing knowledge as a reason to prefer retrieval at
40:46-46:42 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).

## Related Pages

These pages cover the neighboring retrieval, search, and LLM topics.

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
- [Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
