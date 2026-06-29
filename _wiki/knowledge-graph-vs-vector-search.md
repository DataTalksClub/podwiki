---
layout: wiki
title: "Knowledge Graph vs Vector Search"
summary: "How the podcast archive compares explicit graph relationships with embedding-based retrieval for RAG, semantic systems, and domain knowledge."
related:
  - Search, RAG, and Knowledge Systems
  - Search
  - Vector Databases
  - Embeddings
  - Retrieval-Augmented Generation
---

## Definition and Scope

A knowledge graph represents entities and relationships explicitly. Vector
search represents text, images, users, products, or other objects as embeddings
and retrieves nearby items by similarity.

The podcast archive treats them as complementary retrieval patterns. Vector
search is strong when the question is "what is semantically similar to this?"
Knowledge graphs are strong when the question is "how are these things
connected, constrained, or explainable?"

## Contents

- [Archive-Level Takeaways](#archive-level-takeaways)
- [Comparison Structure](#comparison-structure)
- [Decision Points](#decision-points)
- [Episode Evidence](#episode-evidence)
- [Related Pages](#related-pages)
- [Maintenance Notes](#maintenance-notes)

## Archive-Level Takeaways

### Graphs make relationships first-class

Anahita Pakiman's knowledge-graphs episode is the archive's strongest source
for graph architecture. Automotive R&D work needs semantic reporting,
simulation comparison, clustering, load-path detection, and reusable analysis.
Those tasks depend on explicit relationships between simulations, parts,
reports, constraints, and results.

Vector search can retrieve semantically similar chunks, but it does not expose
relationship structure by itself. A graph can answer path, neighborhood,
dependency, and entity-relationship questions that are awkward in a flat vector
index.

### Vector search makes fuzzy retrieval practical

The search episodes explain why vectors matter: they handle paraphrases,
synonyms, language variation, multimodal similarity, recommendations, and RAG
candidate retrieval. Embeddings help when exact keywords or rigid rules miss
relevant content.

This is why vector search remains central for RAG. It can reduce a large corpus
to a smaller context set for an LLM. But the archive keeps warning that
retrieved neighbors still need provenance, ranking, and evaluation.

### Graph RAG and vector RAG solve different problems

Knowledge graphs can ground LLMs by retrieving structured facts or
Cypher-derived context. Vector RAG retrieves chunks by embedding similarity.
The two patterns can work together: vector search finds relevant documents,
while graph traversal provides relationships, constraints, or verified facts.

The distinction matters when teams evaluate hallucination risk. A vector result
may sound plausible because it is similar. A graph result may be easier to
inspect because the path, relation type, and entity IDs are explicit.

### Extraction and maintenance are the hard parts

Knowledge graphs require entity modeling, relation design, ingestion,
validation, and updates. Anahita's episode also discusses limits around
LLM-extracted knowledge and verification. Vector search requires embedding
pipelines, chunking, model versioning, and reindexing. Neither pattern removes
data engineering work.

## Comparison Structure

| Dimension | Knowledge graph | Vector search |
| --- | --- | --- |
| Representation | Entities, relationships, labels, properties, paths | Embeddings in a shared vector space |
| Best fit | Explicit relationships, lineage, constraints, dependency paths, domain semantics | Semantic similarity, paraphrase matching, recommendations, multimodal retrieval |
| Query style | Graph traversal, Cypher, SPARQL, neighborhood and path queries | Nearest-neighbor search, hybrid retrieval, ranking and re-ranking |
| Explainability | Stronger when relations and paths are curated | Weaker unless paired with metadata, citations, and ranking explanations |
| Main risk | Modeling cost, stale graph, extraction errors, schema drift | Wrong nearest neighbors, stale embeddings, missing constraints |
| RAG role | Structured grounding and relationship-aware context | Candidate chunk retrieval and semantic recall |

## Decision Points

### Use vector search when semantic recall is the bottleneck

Vector search fits FAQ retrieval, document search, transcript search,
e-commerce similarity, recommendations, and multimodal matching. It helps when
users ask in language that does not match the source text or when similarity is
more important than a named relationship.

### Use a knowledge graph when the relationship is the answer

A graph fits questions about dependencies, paths, ownership, constraints,
hierarchies, part relationships, citations, and entity neighborhoods. In the
automotive R&D episode, graph structure supports semantic reporting and
simulation analysis because the relationships themselves carry the knowledge.

### Combine them when RAG needs both recall and structure

Many LLM systems need both. A vector index can retrieve candidate passages.
A graph can supply entity context, validated relationships, and structured
facts. Prompt templates can then use graph-derived context instead of relying
only on chunks.

### Evaluate the failure mode you care about

If the failure is missing a semantically related passage, improve chunking,
embeddings, hybrid retrieval, or re-ranking. If the failure is losing the
relationship between entities, add graph modeling, relation extraction, or
graph traversal. If the failure is hallucination, require citations,
verification, and human review instead of assuming either store is enough.

## Episode Evidence

| Episode | Evidence | Source pointer |
| --- | --- | --- |
| [Knowledge Graphs and LLMs for Automotive R&D](https://datatalks.club/podcast.html) | At 15:58, explains why automotive R&D teams adopt Neo4j and knowledge graphs. At 20:32, compares graph and tabular representations for visualization, clustering, and load-path detection. | `../datatalksclub.github.io/_podcast/knowledge-graphs-and-llms-for-automotive-rnd.md` |
| [Knowledge Graphs and LLMs for Automotive R&D](https://datatalks.club/podcast.html) | At 33:43, combines knowledge graphs and LLMs for grounding and RAG. At 38:10, contrasts text chunking, embeddings, vector databases, and knowledge graph semantics. At 39:56, uses Cypher-driven prompt templates. | `../datatalksclub.github.io/_podcast/knowledge-graphs-and-llms-for-automotive-rnd.md` |
| [Knowledge Graphs and LLMs for Automotive R&D](https://datatalks.club/podcast.html) | At 42:43, discusses trust, hallucination, and verification limits when extracting or using knowledge with LLMs. | `../datatalksclub.github.io/_podcast/knowledge-graphs-and-llms-for-automotive-rnd.md` |
| [Modern Search Systems](https://datatalks.club/podcast.html) | At 38:24, uses chunking, embeddings, vectorization, and vector search for transcript RAG. At 48:09, discusses multi-level RAG evaluation and human review. | [summary]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}) |
| [Production ML Search](https://datatalks.club/podcast.html) | At 21:55, explains embeddings as shared representations. At 34:00, shows why vector retrieval often needs filters, recency, and hybrid signals. | `../datatalksclub.github.io/_podcast/production-ml-search-vector-search-embeddings-hybrid-search.md` |
| [Building Agentic AI Systems](https://datatalks.club/podcast.html) | At 36:11 and 37:39, frames retrieval as one tool within larger agent workflows and distinguishes RAG-enough use cases from cases that need more tools or state. | `../datatalksclub.github.io/_podcast/building-agentic-ai-engineering-tooling-retrieval-evaluation.md` |

## Related Pages

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [AI]({{ '/wiki/ai/' | relative_url }})

## Maintenance Notes

- Add a dedicated knowledge-graphs hub only after more archive evidence exists.
  For now, this page and
  [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
  should carry the graph-RAG synthesis.
- When adding examples, say whether the system retrieves similar text, traverses
  explicit relations, or combines both.
- Preserve the distinction between graph databases, knowledge graphs, graph ML,
  vector databases, embeddings, and RAG orchestration.
