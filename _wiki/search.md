---
layout: wiki
title: "Search"
summary: "How the podcast archive frames search as retrieval, ranking, evaluation, semantic matching, and product relevance."
related:
  - Search, RAG, and Knowledge Systems
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - NLP
  - A/B Testing
---

Search is the part of a product or knowledge system that retrieves and ranks
relevant information for a query or task. In the DataTalks.Club archive, search
covers lexical retrieval and semantic retrieval. It also covers vector search,
hybrid search, personalization, and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).

The archive doesn't treat search as a single database feature. It treats search
as an application system. The system needs indexes, candidate generation, and
ranking. It also needs filters, freshness rules, evaluation, and product
metrics. Search may need
[embeddings]({{ '/wiki/embeddings/' | relative_url }}),
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}), and LLM
context construction when it supports RAG.

## Common Definition

The search episodes converge on a practical definition. Search retrieves
candidate items, ranks them, and measures whether the result helped the person
or downstream system.

[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) gives the
clearest production-search definition in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Around 6:20, he frames search as an information-retrieval decision problem.
Around 12:45, he separates candidate generation from ranking. That split
matters because a system can retrieve plausible results and still rank them
badly.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the archive's
clearest bridge from classical search to LLM-era retrieval in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 4:42 and 9:18, she starts with Solr, Lucene, and NLP-based query matching.
At 17:01 and 20:27, she moves to vector databases and migration choices. At
30:38, she connects search to RAG.

This makes search a foundation for
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
RAG adds generation, citations, and answer evaluation, but the first failure
mode is still retrieval: the system may not find the right evidence.

## Guest Differences

Daniel's episode emphasizes production relevance. In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he moves from inverted indexes and Lucene around 11:29-17:40 to dense
representations and hybrid search. He then adds recency, business rules, and
[A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}). His view treats
search as a product-ranking system where latency, business metrics, and
operational iteration matter.

Atita's episode emphasizes search architecture and retrieval quality. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she starts from information retrieval practice, then compares vectors inside an
existing search stack with standalone vector databases at 20:27. Her RAG
discussion at 35:49-48:09 keeps chunking, prompts, citations, and human review
connected to search quality.

The two views agree on the core point. Vector search and LLMs extend search,
but they don't remove relevance engineering. Teams still need indexing, ranking,
filters, and evaluation. Daniel stresses product relevance and iteration. Atita
stresses the architecture choices that connect classical search, vector search,
and RAG.

## Lexical, Vector, and Hybrid Search

Lexical search matches query terms against indexed text. It remains useful when
people need exact terms, filters, auditability, and predictable matching. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
Atita's discussion of Solr and Lucene around 4:42 anchors modern search in that
older retrieval stack.

Vector search compares learned representations instead of only matching words.
In
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel explains the move from bag-of-words to dense vector representations
around 11:29. Around 27:21, he describes vector databases as infrastructure for
embeddings and nearest-neighbor search. That connects search directly to
[Embeddings]({{ '/wiki/embeddings/' | relative_url }}).

Hybrid search combines keyword and vector retrieval. Around 34:00 in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
Daniel discusses combining vector similarity with filters and recency. Around
39:53-45:11, he adds constraints and time encoding. He also discusses
normalization and query-time weights.

Those details matter because production search rarely optimizes only semantic
similarity. It also has to handle inventory and permissions. Freshness,
popularity, and business rules become ranking inputs too.

Use
[Vector Database vs Search Engine]({{ '/wiki/vector-database-vs-search-engine/' | relative_url }})
for the architecture comparison. Use
[Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
when the retrieval problem depends on explicit relationships rather than only
text or embedding distance.

## RAG

RAG uses search to retrieve context before an LLM generates an answer. It's not
a replacement for search. It adds another stage after retrieval.

Atita makes this concrete in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38, she introduces retrieval plus generation as a way to reduce
unsupported LLM answers. At 35:49, she applies the idea to a chatbot over
podcast transcripts.

At 38:24, she describes chunking, overlap, and embedding model choices before
vectorization. At 42:49, she connects retrieval to prompt design and citations.

RAG fails at retrieval time when chunks are wrong, missing, too broad, or
missing source metadata. It fails at generation time when the model ignores the
retrieved evidence, invents unsupported claims, or drops citations. That's why
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
and [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
need to be read together.

## Vector Databases

Vector databases store embeddings and support nearest-neighbor retrieval, but
the search episodes treat them as one component in a larger system.

In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
Atita introduces vector databases such as Qdrant at 17:01. At 20:27, she
compares adding vectors to an existing search stack with introducing a
standalone vector database. Teams make that architecture decision against their
current retrieval system and migration risk.

Daniel adds the production version of the same distinction in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
Around 29:00-33:13, he separates embedding computation and ingestion. He also
covers model versioning and multimodal retrieval. Around 52:35-54:56, he
discusses vendor selection and when teams might use Lucene or Elasticsearch
instead of a dedicated vector database.

This is why search pages should link to
[Vector Databases]({{ '/wiki/vector-databases/' | relative_url }}) without
treating a vector database as the whole search system. A team still has to
choose indexes and filters. It also has to choose ranking signals, evaluation
metrics, and reindexing jobs.

## Evaluation

Search evaluation has to measure more than whether a result was retrieved.
Teams need to test retrieval quality, ranking quality, latency, and product
impact.

Daniel ties search quality to business metrics in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
At 1:01:25, he discusses business KPIs, A/B tests, and revenue attribution. At
1:03:50, he adds offline evaluation and engineering iteration. That connects
search to [Metrics]({{ '/wiki/metrics/' | relative_url }}) and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

Atita adds RAG-specific evaluation in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
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
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}),
he discusses keyword-search brittleness, synonyms, and configuration debt.
Around 30:22-33:13, he covers recomputing embeddings and keeping pipelines
flexible when models change. Around 58:17, he uses e-commerce personalization
and CLIP-style embeddings as an example of moving from prototype to production.

Atita's episode shows the migration side. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
the 20:27 discussion warns against assuming that standalone vector storage is
always the right move. Existing Solr, Lucene, or Elasticsearch systems may
already handle lexical relevance and filters. They may already meet operational
needs too. A new vector component helps only if it improves the actual
retrieval and ranking problem.

Search therefore sits across
[Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }}),
[LLM production work]({{ '/wiki/llm-production-patterns/' | relative_url }}),
and [MLOps]({{ '/wiki/mlops/' | relative_url }}). The core question isn't
which retrieval technology is newest. The question is which search design gives
the product relevant, explainable, and measurable results.

## Related Pages

Use these pages for the surrounding architecture and evaluation details.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Embeddings]({{ '/wiki/embeddings/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
