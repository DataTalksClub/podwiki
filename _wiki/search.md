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
relevant information for a query or task. DataTalks.Club guests discuss search
through [[information retrieval]]
and lexical matching. They then add semantic retrieval and vector search.
Hybrid search, personalization, and
[[retrieval-augmented-generation|retrieval-augmented generation]]
appear as product patterns.

The search discussions treat search as an application system rather than a
single database feature. The system needs indexes, candidate generation,
ranking, and filters. Freshness rules, evaluation, and product metrics
determine quality.

Search may need
[[embeddings]],
[[vector databases]], and LLM
context construction. In
[[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]],
the same retrieval layer becomes the evidence layer for answers and citations.
It also supports knowledge workflows.

## Retrieval and Ranking

Search starts by retrieving candidate items, ranking them, and measuring
whether the result helped the person or downstream system. [[book:20210712-relevant-search|Relevant Search]] by Doug Turnbull and John Berryman covers the relevance engineering discipline of scoring, ranking, and tuning from the Solr/Elasticsearch era, while [[book:20211101-ai-powered-search|AI-Powered Search]] by Trey Grainger, Doug Turnbull, and Max Irwin extends the same discipline into learning-to-rank, vector, and LLM-era retrieval. In
[[podcast:building-production-search-systems|Building Search Systems]],
[[person:danielsvonava|Daniel Svonava]] frames search
as an information-retrieval decision problem around 6:20. Around 12:45, he
separates candidate generation from ranking. A system can retrieve plausible
results and still rank them badly, so
[[production search evaluation]]
has to evaluate both stages.

[[person:atitaarora|Atita Arora]] bridges classical
search and LLM-era retrieval in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 4:42 and 9:18, she starts with Solr, Lucene, and NLP-based query matching.
At 17:01 and 20:27, she moves to vector databases and migration choices. At
30:38, she makes search the retrieval side of RAG. RAG adds generation,
citations, and answer evaluation, but the first failure mode is still
retrieval because the system may not find the right evidence.

Daniel emphasizes product relevance in
[[podcast:building-production-search-systems|Building Search Systems]].
Around 11:29-17:40, he moves from inverted indexes and Lucene to dense
representations and hybrid search. He then adds recency, business rules, and
[[a-b-testing|A/B testing]].

Atita emphasizes architecture choices at 20:27 in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
where she compares vectors inside an existing search stack with a standalone
vector database. Vector search and LLMs extend search, but they don't remove
relevance engineering. Teams still need indexing, ranking, filters, and
evaluation.

## Lexical, Vector, and Hybrid Search

Lexical search matches query terms against indexed text. It remains useful when
people need exact terms, filters, auditability, and predictable matching. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
[[person:atitaarora|Atita]] anchors modern search in
Solr and Lucene around 4:42, then adds NLP-based query matching at 9:18.
[[NLP]] matters here because query parsing,
synonyms, normalization, and semantic matching decide which candidates enter
the ranking stage.

Vector search compares learned representations instead of only matching words.
In
[[podcast:building-production-search-systems|Building Search Systems]],
[[person:danielsvonava|Daniel]] explains the move from
bag-of-words to dense vector representations around 11:29. Around 27:21, he
describes vector databases as infrastructure for embeddings and
nearest-neighbor search, making search a practical use case for
[[embeddings]].

Hybrid search combines keyword and vector retrieval. Around 34:00 in
[[podcast:building-production-search-systems|Building Search Systems]],
Daniel discusses combining vector similarity with filters and recency. Around
39:53-45:11, he adds constraints and time encoding. He also discusses
normalization and query-time weights.

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

Atita makes this concrete in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 30:38, she introduces retrieval plus generation as a way to reduce
unsupported LLM answers. At 35:49, she applies the idea to a chatbot over
podcast transcripts. At 38:24, she describes chunking, overlap, and embedding
model choices before vectorization. At 42:49, she links retrieval to prompt
design and citations.

RAG fails at retrieval time when chunks are wrong, missing, too broad, or
missing source metadata. It fails at generation time when the model ignores the
retrieved evidence, invents unsupported claims, or drops citations. That's why
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
and [[LLM Evaluation Workflows]]
need to be read together. The practical build path in
[[Search and RAG Project Checklist]]
starts with searchable source material before adding answer generation.

## Vector Databases

Vector databases store embeddings and support nearest-neighbor retrieval, but
the search episodes treat them as one component in a larger system.

In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
Atita introduces vector databases such as Qdrant at 17:01. At 20:27, she
compares adding vectors to an existing search stack with introducing a
standalone vector database. Teams make that architecture decision against their
current retrieval system and migration risk.

Daniel adds the production version of the same distinction in
[[podcast:building-production-search-systems|Building Search Systems]].
Around 29:00-33:13, he separates embedding computation and ingestion. He also
covers model versioning and multimodal retrieval. Around 52:35-54:56, he
discusses vendor selection and when teams might use Lucene or Elasticsearch
instead of a dedicated vector database.

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

Daniel ties search quality to business metrics in
[[podcast:building-production-search-systems|Building Search Systems]].
At 1:01:25, he discusses business KPIs, A/B tests, and revenue attribution. At
1:03:50, he adds offline evaluation and engineering iteration. Search
evaluation belongs with [[Metrics]] and
[[Production Search Evaluation]].

Atita adds RAG-specific evaluation in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 48:09, she discusses multi-level metrics, offline tests, and
human-in-the-loop review. For RAG, teams need to evaluate the retrieved
passages and the generated answer. They also need to evaluate citation quality
and whether the answer solves the user's task.

## Production Tradeoffs

Production search work starts after a prototype retrieves a few plausible
results. Teams have to keep indexes fresh and manage embedding model versions.
They also have to handle latency, support filters, monitor relevance drift, and
decide when to re-rank.

Daniel's episode shows how these tradeoffs appear in everyday search systems.
Around 20:02 in
[[podcast:building-production-search-systems|Building Search Systems]],
he discusses keyword-search brittleness, synonyms, and configuration debt.
Around 30:22-33:13, he covers recomputing embeddings and keeping pipelines
flexible when models change. Around 58:17, he uses e-commerce personalization
and CLIP-style embeddings as an example of moving from prototype to production.

Atita's episode shows the migration side. In
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]],
the 20:27 discussion warns against assuming that standalone vector storage is
always the right move. Existing Solr, Lucene, or Elasticsearch systems may
already handle lexical relevance and filters. They may already meet operational
needs too. A new vector component helps only if it improves the actual
retrieval and ranking problem.

Search therefore sits across
[[Machine Learning System Design]],
[[llm-production-patterns|LLM production work]],
and [[MLOps]]. The core question isn't
which retrieval technology is newest. The question is which search design gives
the product relevant, explainable, and measurable results.
