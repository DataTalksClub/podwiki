---
layout: wiki
title: "Search, RAG, and Knowledge Systems"
summary: "How DataTalks.Club podcast guests connect retrieval, RAG, knowledge graphs, and production knowledge systems."
related:
  - Retrieval-Augmented Generation
  - Search
  - Vector Databases
  - Knowledge Graph vs Vector Search
  - LLM Production Patterns
---

Search/RAG/knowledge systems form the retrieval layer behind useful AI and data
products. In the DataTalks.Club archive, the topic starts with
[search]({{ '/wiki/search/' | relative_url }}) and
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
It then extends into embedding-based retrieval, RAG, graph retrieval, and
[LLM evaluation]({{ '/wiki/llm-evaluation-workflows/' | relative_url }}).

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the bridge in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}):
search practice still matters when teams add vectors and LLMs. At 30:38 she
defines RAG as retrieval plus generation. At 38:24 she turns podcast
transcripts into chunks, embeddings, and vectorized context. At 48:09 she
brings evaluation and human review back into the system.

This topic maps the retrieval stack. Start with
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
for the core RAG design. Use [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
for vector storage and indexing. Use
[Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
for structured retrieval choices. Use
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
for measuring retrieval and business outcomes.

## Link Map

Core concepts:

- [Search]({{ '/wiki/search/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})

Podcast anchors:

- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
  with [Atita Arora]({{ '/people/atitaarora/' | relative_url }}) links
  classical search to vector databases, transcript RAG, citations, and RAG
  review.
- [Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
  with [Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }})
  separates retrieval and ranking. It also covers vector compute, vector
  storage, hybrid search, and business metrics.
- [Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
  covers inverted indexes, embeddings, and vector compute. It also covers
  hybrid search with filters, recency, and operational evaluation.
- [Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
  with [Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }})
  shows when graph semantics and Cypher-style retrieval matter more than
  nearest-neighbor chunks alone.
- [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
  with [Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }})
  turns RAG into engineering work with gold tests and failure categories. It
  also covers logs, traces, chunking, and tool escalation.
- [Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }})
  with [Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }})
  treats retrieval as one tool inside agent systems, not a reason to ignore
  latency and cost. It also keeps context noise and evaluation in scope.
- [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
  with [Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) draws the
  boundary between retrieval for changing knowledge and fine-tuning for
  behavior, style, or task adaptation.

## Common Definition

Across the archive, a knowledge system is the part of a product that finds and
ranks information before a user or model uses it. It also represents and
verifies that information. Search retrieves candidates, and ranking orders them.
RAG adds selected context to an LLM prompt, while knowledge graphs expose
explicit relationships.

The production system still needs provenance and permissions, which Atita covers
in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Daniel adds latency and product metrics in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
and Anahita adds verification for graph-backed systems in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).

The archive doesn't treat RAG as magic memory. Atita's transcript example works
because the system prepares documents, chunks them, and embeds them. It then
retrieves them, wraps them with context, and cites them
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
35:49-42:49). That makes RAG a product design built on
[search]({{ '/wiki/search/' | relative_url }}), not a replacement for search.

The archive also doesn't treat vector search as the whole system. The
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
discussion separates vector compute from vector storage at 29:00 and adds
filters, recency, business rules, and ranking at 34:00-45:11. This connects
vector databases to [production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
and [MLOps]({{ '/wiki/mlops/' | relative_url }}), because embedding models,
indexes, and ranking logic all change over time.

## Guest Differences

Atita starts from the search stack. Her 17:01 and 20:27 chapters in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
compare standalone vector databases with adding vectors to existing search
infrastructure. Her RAG guidance then emphasizes chunking, prompt context,
citations, and human-in-the-loop evaluation.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) starts from
production retrieval and ranking. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he frames search as a relevance decision at 6:20, separates retrieval from
ranking at 12:45. He also ties search impact to A/B tests and revenue at
1:01:25. His view is useful when the product is search, recommendations,
ecommerce, or
matching rather than a chatbot alone.

[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) starts from
domain relationships. Her
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
episode contrasts text chunks and vector databases with graph semantics at
38:10. She discusses Cypher-driven retrieval at 39:56. Her view fits domains where the
answer depends on entity relationships and report structure. It also fits
simulation-heavy domains where verification matters more than similar text.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) starts
from practical LLM engineering. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
he places gold tests and failure analysis around the RAG application. He also
uses logs, traces, and chunking choices. His escalation point is pragmatic. Use
RAG for knowledge lookup, then add tools or agents when the workflow must take
action.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) starts
from agent engineering. In
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she pushes back on "RAG is dead" at 29:30 because long context and agents still
face latency and cost. They also still face noisy context, metadata, and
source-quality constraints.
Her view keeps retrieval inside [agent engineering]({{ '/wiki/agent-engineering/' | relative_url }})
without turning every lookup problem into an agent workflow.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) starts from LLM
deployment. Her
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
episode treats retrieval as the better fit for changing knowledge at
40:46-46:42. Fine-tuning fits behavior, style, and task adaptation. That
boundary anchors [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}).

## Search-First Architecture

A search-first knowledge system makes retrieval visible before generation. The
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
episode separates inverted-index search at 11:29, candidate generation and
ranking at 12:45, embeddings at 21:55, and hybrid search at 34:00. That order
is useful for RAG because a generated answer can't compensate for missing or
badly ranked evidence.

For product search, the retrieved object may be a product or session. It may
also be an image, document, or support article.

For RAG, it may be a chunk or section. It may also be an entity, graph path, or
source record.

Both cases need metadata for filters and citations, plus freshness and
evaluation. Daniel covers those search
constraints at 29:00-45:11 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Atita covers RAG provenance at 38:24-48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).

## RAG as Context Packaging

RAG turns retrieval results into model context. Atita's transcript chatbot in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
shows the sequence. The system ingests transcripts, chooses chunks and overlap,
computes embeddings, and retrieves passages. It then places them into a prompt
and returns citations. That makes chunk design part of the user experience, not just
a preprocessing detail.

Hugo's
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
discussion adds the debugging work. At 23:00 he emphasizes representative gold
tests. At 26:43 he separates failure categories. At 27:38 he brings in logs
and traces. At 48:20 he compares chunking and context-window strategies.

Those practices connect RAG to
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
instead of leaving it as a demo.

## Vector Retrieval and Hybrid Search

Vector retrieval helps when exact words are brittle, when users ask semantically
similar questions in different language, or when the product needs multimodal
matching. The [Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }})
episode covers dense representations at 11:29, vector databases at 27:21, and
CLIP-style text-to-image retrieval at 32:43. Those examples connect
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) to search,
recommendations, personalization, and RAG.

Hybrid search is the archive's production default for search products. The same
search discussion adds filters and recency around vector similarity. It also
adds popularity and business rules. Query-time weights and ranking matter too
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
34:00-45:11). That's why
[Vector Database vs Search Engine]({{ '/wiki/vector-database-vs-search-engine/' | relative_url }})
is an architecture decision, not a slogan about newer tools replacing older
search engines.

## Knowledge Graphs and Structured Retrieval

Knowledge graphs become useful when the question is about relationships, not
only similarity. Anahita's
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
episode connects graph databases to changing automotive relationships at 16:31.
It also covers semantic reporting at 10:28 and graph-based RAG at 33:43-39:56.
The graph can preserve entities, containment, and order. It can also preserve paths and domain
semantics that plain chunks may lose.

Graph retrieval doesn't remove grounding work. Anahita's 42:42 discussion of
hallucination and verification shows why graph facts still need validation,
traceability, and review
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})).
Use [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
when deciding whether the context should be similar text, graph paths, or both.

## Evaluation and Operations

Hugo adds tests in
[the episode]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
Failure labels show whether the next fix belongs in data preparation or
retrieval. Some fixes belong in prompting, formatting, or product constraints
instead.

Production search also needs business measurement. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel ties search quality to revenue, A/B tests, and operational metrics at
1:01:25-1:03:50. That makes [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
the operational counterpart to RAG evaluation. A retriever can look good
offline and still fail on latency, cost, conversion, or support resolution. It
can also fail user trust.

## Production Boundaries

Use RAG when the system mostly answers from a changing knowledge base and needs
sources, citations, or reviewable evidence. Meryem's
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }})
discussion at 40:46-46:42 supports retrieval for changing knowledge, while
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}) captures
the boundary with model adaptation.

Use agents for planning and tool calls when action needs API queries or state
lookup. Ranjitha places retrieval as one tool inside a larger workflow at
36:11-37:39.
([episode]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}))
That adds production complexity,
while [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
covers the added evaluation and tool-integration burden.

Use graph retrieval when the relationship structure is part of the answer.
Anahita's
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
discussion at 38:10-39:56 supports graph context for domains where entity
links, paths, and constraints matter. Use vector retrieval when semantic
similarity over chunks, images, or sessions is the main retrieval problem
([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
21:55-34:00).

## Practical Design Questions

Use these checks when routing a search, RAG, or knowledge-graph design.

1. Define the retrieval unit. Atita's transcript example uses chunks, while
   Anahita's graph example uses graph units.
   ([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
   38:24 and
   [Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
   38:10).
2. Preserve the metadata that survives retrieval. Source and timestamp matter
   in Atita's citation flow, while permissions and recency may matter too.
   Graph relations can affect retrieval.
   ([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
   34:00-45:11 and
   [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
   42:49).
3. Choose the retrieval mode by failure mode. Keyword and vector search address
   text matching, while hybrid search and graph retrieval address other
   failures.
   ([Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
   11:29-45:11 and
   [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})).
4. Evaluate retrieval and generation separately. Atita uses relevance and
   citations in
   [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
   Hugo adds gold questions in
   [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
   Daniel adds business metrics in
   [Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
5. Track what changes over time. Source documents, permissions, and embedding
   models can force retrieval changes. Chunking and graph schemas can do the
   same, as can prompts and ranking weights. User behavior can also force
   changes
   ([Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
   29:00-33:13 and
   [Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
   40:46-46:42).

## Related Pages

These pages cover the neighboring concepts and decision boundaries:

- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [RAG Portfolio Projects]({{ '/wiki/rag-portfolio-projects/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Vector Database vs Search Engine]({{ '/wiki/vector-database-vs-search-engine/' | relative_url }})
- [Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
- [Graph RAG vs Vector RAG]({{ '/wiki/graph-rag-vs-vector-rag/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
- [LLM Production Patterns]({{ '/wiki/llm-production-patterns/' | relative_url }})
- [Agent Engineering]({{ '/wiki/agent-engineering/' | relative_url }})
