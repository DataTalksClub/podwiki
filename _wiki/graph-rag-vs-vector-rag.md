---
layout: wiki
title: "Graph RAG vs Vector RAG"
summary: "How the podcast archive compares graph-driven retrieval with vector-driven retrieval for grounded LLM systems."
related:
  - Knowledge Graph vs Vector Search
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - Vector Databases
  - Embeddings
---

Teams use graph RAG and vector RAG to decide what context an LLM should see
before it answers. Vector RAG retrieves semantically similar chunks with
[embeddings]({{ '/wiki/embeddings/' | relative_url }}) and a
[vector database]({{ '/wiki/vector-databases/' | relative_url }}). Graph RAG
retrieves entities, relations, paths, and structured facts from a knowledge
graph.

The archive treats them as complementary approaches inside
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}),
not as a winner-takes-all tool choice. Use
[Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
for the broader storage and retrieval comparison. Here, the boundary is what
the LLM receives as grounding context.

## Link Map

Start with these related wiki pages:

- [Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
- [RAG]({{ '/wiki/rag/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})

The main podcast discussions are:

- [Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})
- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
- [Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})

The guest experts are:

- [Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }}) on graph semantics and LLM grounding
- [Atita Arora]({{ '/people/atitaarora/' | relative_url }}) on vector RAG for podcast transcripts
- [Reem Mahmoud]({{ '/people/reemmahmoud/' | relative_url }}) on production ML search and hybrid retrieval

## Common Definition

Vector RAG starts from a query and embeds it. It retrieves nearby chunks and
places those chunks into the prompt. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
Atita Arora uses a podcast-transcript chatbot as the example. Around
38:24-42:49, the system chunks transcripts, then chooses chunk size and overlap.
It embeds the chunks, retrieves relevant pieces and passes them to the LLM
with instructions and citations.

Graph RAG starts from modeled relationships. In
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
Anahita Pakiman argues that plain vector chunks can miss chapter order and
containment. They can also miss parent-child links and domain semantics. Around 38:10, she
contrasts "chunks in a vector database" with a graph that stores chapters and
their relationships. Around 39:56, she extends that into
prompt templates that can use Cypher-style graph queries to retrieve relevant
context.

The shared goal is grounded generation. Both approaches try to reduce unsupported
answers by retrieving evidence before the model responds. The practical
difference is whether the first retrieval unit is a semantically similar chunk
or an explicitly connected entity, relation, path, or subgraph.

## Guest Perspectives

Atita emphasizes user-facing answer quality through chunking, overlap,
retrieval count, and prompt context. She also covers references, offline
checks, and human-in-the-loop evaluation
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
40:01-48:09). That framing fits knowledge bases, transcripts, support content,
and other text-heavy systems where the hardest problem is finding the right
passage.

Anahita emphasizes semantics and trust. Her automotive R&D examples need
relationships between simulations, chapters, entities, and engineering
concepts. She also warns around 42:42 that LLM-generated graph
content is hard to trust at scale. Traditional graph-building and verification
still matter
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})).

Production-search guests add a third pressure: product relevance. The
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }})
discussion shows that a pure vector match often needs filters, recency,
popularity, and query-time weights around 34:00-45:11. That doesn't make the
system graph RAG, but it pushes teams toward hybrid retrieval instead of a
single nearest-neighbor lookup.

## Vector RAG Fits Fuzzy Text Retrieval

Vector RAG is strongest when a user may ask the same thing many ways. Podcast
transcripts are a good archive example: a question like "how do I move from
analytics to data science?" may not share exact words with the best episode
segment. Atita's transcript-chatbot example retrieves by semantic similarity
and then asks the LLM to answer from those chunks
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24-42:49).

Embeddings alone aren't enough, so the archive repeatedly ties vector RAG
quality to chunk boundaries, overlap, and source metadata. It also ties quality
to citation behavior and retrieval evaluation.

If chunks are too broad, the answer becomes vague. If chunks are too narrow,
pronouns, definitions, and context can break. If
citations are missing, the user can't check whether the answer is grounded.

## Graph RAG Fits Relationship Questions

Graph RAG is strongest when the relationship is part of the answer. In
Anahita's book example, teams can represent chapter containment and chapter
order in a graph. In the automotive setting, teams can model simulations and
parts. They can also model reports, finite-element-analysis concepts, and
engineering relationships
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}),
15:58-20:32 and 38:10-39:56).

With graph structure, teams can make prompts more precise. Instead of
retrieving five nearby paragraphs, the system can retrieve a neighborhood, a
path, or a Cypher-derived set of facts. The payoff is stronger when the LLM must answer
"how are these things connected?" rather than "which passage sounds similar?"

## Hybrid Design Is Usually the Real Choice

Across the archive, guests route by failure mode. If the system misses
semantically related passages, improve vector retrieval and reranking. Then
revisit chunking or embeddings.

If it loses entity relationships or lineage, add graph modeling or graph lookup.
Add graph modeling when it loses order or constraints, too. If it returns
plausible but irrelevant results, add filters or ranking weights. Recency and
popularity can also become product signals
([Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
34:00-45:11).

A mature RAG system can use both: vector search finds candidate documents or
chunks, and graph traversal adds related entities and validated facts. It can
also add dependency paths or provenance. The prompt can then include text
evidence and structured context.

## Evaluation Questions

Graph RAG and vector RAG should be evaluated against different mistakes. For
vector RAG, look at whether the retrieved chunks contain enough evidence and
useful overlap. Also check whether they cite the right source and answer
representative questions.
Atita's evaluation discussion around 48:09 separates model choice, ingestion,
retrieval strategy, and end-to-end user feedback
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})).

For graph RAG, look at whether the graph facts are correct, current, and
traceable. Anahita's caution around 42:42 is important. If an LLM extracted the
graph, the team still needs to validate it. Otherwise, the system may only move
hallucination from the answer layer into the retrieval layer
([Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }})).

## Related Pages

These pages cover the surrounding retrieval and search topics:

- [Knowledge Graph vs Vector Search]({{ '/wiki/knowledge-graph-vs-vector-search/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
