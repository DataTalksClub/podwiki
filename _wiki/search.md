---
layout: wiki
title: "Search"
summary: "How DataTalks.Club guests frame search as retrieval, ranking, evaluation, semantic matching, and product relevance."
related:
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - NLP
  - A/B Testing
---

Search is the part of a product or knowledge system that retrieves and ranks
relevant information for a query or task. Search work starts with
[[information retrieval]]
and lexical matching, then adds semantic retrieval and vector search.
Hybrid search, [[machine-learning-personalization=>personalization]], and
[[retrieval-augmented-generation=>retrieval-augmented generation]]
appear as product patterns.

Search is the broad product-system layer. The useful framing treats search as
an application system rather than a single database feature.
The system needs indexes and candidate generation. It also needs ranking and
filters. Freshness rules, evaluation, and product metrics determine quality.

[[Information Retrieval]] covers the underlying retrieval discipline, and
[[Search Relevance]] covers ordering and product-fit quality.
[[Vector Search vs Keyword Search]] covers matching methods, while
[[Vector Database vs Search Engine]] covers vector infrastructure placement.

Search may need
[[embeddings]],
[[vector databases]], and LLM
context construction. In
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
the same retrieval layer becomes the evidence layer for answers and citations.
It also supports knowledge workflows.

## Retrieval and Ranking

Search starts by retrieving candidate items, ranking them, and measuring
whether the result helped the person or downstream system. [[book:20210712-relevant-search=>Relevant Search]] by Doug Turnbull and John Berryman covers the Solr and Elasticsearch-era discipline of scoring, ranking, and tuning. [[book:20211101-ai-powered-search=>AI-Powered Search]] by Trey Grainger and coauthors extends the same discipline into learning-to-rank, vector retrieval, and LLM-era retrieval.

Search is an information-retrieval decision problem. Candidate generation is separate from ranking, so a system can retrieve plausible results and still rank them badly. That means
[[production search evaluation]]
has to evaluate both stages
([[cite:building-production-search-systems=>Building Search Systems]]).

Classical search and LLM-era retrieval connect through a common path. Search
systems start with Solr, Lucene, and NLP-based query matching, then add vector
databases and migration choices. The same retrieval layer then becomes part of
RAG
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
RAG adds generation, citations, and answer evaluation, but the first failure
mode is still retrieval because the system may not find the right evidence.
The same arc includes
[[machine-learning-personalization=>personalization]]
and learning-to-rank, so LLM-era search still inherits ranking and evaluation
work from earlier information-retrieval systems
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

Each generation adds a layer rather than replacing the previous one. Solr and
Lucene keep inverted-index discipline. Learning-to-rank adds model-based
ordering. LLMs add generation and citation checks on top of retrieved evidence.

Product relevance moves from inverted indexes and Lucene to dense
representations and hybrid search, then adds recency, business rules, and
[[a-b-testing=>A/B testing]]
([[cite:building-production-search-systems=>Building Search Systems]]).

Architecture choices compare vectors inside an existing search stack with a
standalone vector database
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Vector search and LLMs extend search, but they don't remove relevance
engineering. Teams still need indexing, ranking, filters, and evaluation.

## Lexical, Vector, and Hybrid Search

Lexical search matches query terms against indexed text. It remains useful when
people need exact terms, filters, auditability, and predictable matching. Modern
search anchors in Solr and Lucene, then adds NLP-based query matching
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
[[NLP]] matters here because query parsing,
synonyms, normalization, and semantic matching decide which candidates enter
the ranking stage.

Vector search compares learned representations instead of only matching words,
moving from bag-of-words to dense vector representations. Vector databases are
infrastructure for embeddings and nearest-neighbor search, making search a
practical use case for
[[embeddings]]
([[cite:building-production-search-systems=>Building Search Systems]]).

Hybrid search combines keyword and vector retrieval by joining vector similarity
with filters and recency. It also adds constraints, time encoding, normalization,
and query-time weights
([[cite:building-production-search-systems=>Building Search Systems]]).

Production search rarely optimizes only semantic similarity, because it also
ranks against inventory, permissions, and freshness. Popularity and business
rules may become ranking inputs too.

[[Vector Database vs Search Engine]]
compares where vector retrieval belongs in a search stack.
[[Knowledge Graph vs Vector Search]]
is the sharper comparison when retrieval depends on explicit relationships
rather than only text or embedding distance.

## RAG

RAG uses search to retrieve context before an LLM generates an answer. It's not
a replacement for search. It adds another stage after retrieval.

Retrieval plus generation reduces unsupported LLM answers. In a chatbot over
podcast transcripts, the build starts with chunking, overlap, and embedding
model choices before vectorization. It then links retrieval to prompt design and
citations
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

RAG fails at retrieval time when chunks are wrong, missing, too broad, or
missing source metadata. It fails at generation time when the model ignores the
retrieved evidence, invents unsupported claims, or drops citations. That's why
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
and [[LLM Evaluation Workflows]]
need to be read together. The practical build path in
[[Search and RAG Project Checklist]]
starts with searchable source material before adding answer generation.

## Vector Databases

Vector databases store embeddings and support nearest-neighbor retrieval, but
they're one component in a larger search system.

Vector databases such as Qdrant store embeddings. Adding vectors to an existing
search stack differs from introducing a standalone vector database. Teams make
that decision against their current retrieval system and migration risk
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

The production version of the same distinction separates embedding computation
from ingestion. It also covers model versioning, multimodal retrieval, and
vendor selection against Lucene or Elasticsearch instead of a dedicated vector
database
([[cite:building-production-search-systems=>Building Search Systems]]).

[[Vector Databases]] covers
storage and nearest-neighbor retrieval, but a vector database isn't the whole
search system. A team still has to choose indexes and filters. It also needs
ranking signals, evaluation metrics, and reindexing jobs.

When retrieval feeds an LLM,
[[Graph RAG vs Vector RAG]]
marks another boundary. Dense chunks help semantic similarity, while graph
retrieval helps when relationships define the answer.

## Evaluation

Search evaluation has to measure more than whether a result was retrieved.
Teams need to test retrieval quality, ranking quality, latency, and product
impact.

Search quality ties to business metrics through business KPIs, A/B tests, and
revenue attribution. Offline evaluation and engineering iteration complete the
loop
([[cite:building-production-search-systems=>Building Search Systems]]). Search
evaluation belongs with [[Search Relevance]], [[Metrics]], and
[[Production Search Evaluation]].

RAG-specific evaluation adds multi-level metrics, offline tests, and
human-in-the-loop review
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
For RAG, teams need to evaluate the retrieved passages and the generated answer,
along with citation quality and whether the answer solves the user's task.

## Production Tradeoffs

Production search work starts after a prototype retrieves a few plausible
results. Teams have to keep indexes fresh and manage embedding model versions.
They also have to handle latency, support filters, monitor relevance drift, and
decide when to re-rank.

These tradeoffs appear in everyday search systems. Keyword-search brittleness,
synonyms, and configuration debt show up on the lexical side. Recomputing
embeddings and keeping pipelines flexible matter when models change.
E-commerce [[machine-learning-personalization=>personalization]] with CLIP-style
embeddings is one example of moving from prototype to production
([[cite:building-production-search-systems=>Building Search Systems]]).

On the migration side, standalone vector storage isn't always the right move.
Existing search systems may already handle lexical relevance, filters, and
operational needs. That includes Solr, Lucene, or Elasticsearch systems. A new
vector component helps only if it improves the actual retrieval and ranking problem
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

Search therefore sits across
[[Machine Learning System Design]],
[[llm-production-patterns=>LLM production work]],
and [[MLOps]]. The core question isn't
which retrieval technology is newest. The question is which search design gives
the product relevant, explainable, and measurable results.
