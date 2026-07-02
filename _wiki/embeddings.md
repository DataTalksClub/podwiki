---
layout: wiki
title: "Embeddings"
summary: "How DataTalks.Club guests explain embeddings as representations for semantic search, RAG, recommendations, multimodal retrieval, and language systems."
related:
  - Search, RAG, and Knowledge Systems
  - Vector Databases
  - Search
  - Retrieval-Augmented Generation
  - NLP
---

Embeddings are numerical representations of text and images, users and products,
or other objects. They let a system compare meaning or behavior by distance in a
shared vector space instead of comparing only exact words or hand-written rules.

DataTalks.Club guests often place embeddings behind
[[search]] and
[[vector databases]]. They also
appear in
[[retrieval-augmented-generation|retrieval-augmented generation]]
systems. Recommendation systems and multimodal retrieval use them too.

In
weak-supervision workflows and production
[[machine-learning-system-design|ML systems]],
they're a representation layer, not the whole product. Guests separate
embedding generation from storage and ranking. They also separate evaluation,
citations, and business logic.

## Representation Space

[[person:reemmahmoud|Reem Mahmoud]] maps embeddings to
vector search in
[[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
At 21:55, she explains that queries and searchable items can be mapped into the
same representation space. Retrieval can then find items with similar meaning
even when the words differ. At 29:00, she separates vector compute from vector
storage. The embedding model stays distinct from the database that stores and
searches vectors.

[[person:atitaarora|Atita Arora]] gives the same
representation idea a retrieval-system frame in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 38:24, her transcript chatbot example creates chunks with overlap, embeds
them, and stores vectors for retrieval. The embedding model creates the
representation. The
[[vector-databases|vector database]] retrieves
nearby vectors. The application still needs prompts, references, and evaluation.

[[person:meryemarik|Meryem Arik]] connects embeddings
to production LLM systems in
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]].
At 48:01, she describes vector databases through embeddings, indexing, and
semantic search. In the surrounding discussion, retrieval fits changing
knowledge, while fine-tuning changes model behavior or style. The same boundary
is expanded in
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]].

## Semantic Search

Keyword matching can be too brittle when users express the same intent with
different language. Reem describes keyword-search challenges around 20:02 in
[[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]].
At 21:55, she introduces vector search as a way to match queries and documents
through shared representations. That keeps embeddings inside the larger
[[information retrieval]]
system. Vector search changes candidate generation, but it doesn't replace
ranking.

Reem separates candidate generation from ML ranking at 12:45 and returns to
operational search metrics at 1:01:25. A vector match can find plausible
candidates. The product still has to decide which result belongs first. It also
has to trade semantic similarity against freshness and popularity.

Metadata, behavior, query-time weights, and business rules also matter. Her 34:00-45:11
discussion of filters and recency makes embeddings one signal inside
[[production search evaluation]],
not a substitute for product ranking.

Atita makes the architecture choice explicit in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
At 17:01 and 20:27, she compares plug-and-play vector search with vector support
inside existing search systems. That decision is the same boundary covered in
[[Vector Database vs Search Engine]].
Teams can choose the embedding model, vector storage, and search application
behavior as separate design decisions.

## RAG Systems

In [[retrieval-augmented-generation|RAG]], embeddings retrieve context for a
language model. Atita's transcript-chatbot example in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]
starts at 35:49 and becomes concrete at 38:24. The system chunks transcripts
with overlap, embeds them, and retrieves relevant passages. It then generates
an answer with references. At 48:09, she extends evaluation beyond
nearest-neighbor retrieval into generated answer quality, citation quality, and
human review.

Meryem's production discussion adds the update path. In
[[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]],
she compares retrieval with retraining around 40:46-42:02. Retrieval fits
systems that need current or proprietary knowledge. A team can re-ingest,
re-embed, and re-index documents instead of fine-tuning the model every time
facts change.

[[person:hugobowneanderson|Hugo Bowne-Anderson]] gives
the builder's version in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]].
Around 44:26, he presents chunking and embeddings as a practical first step for
useful LLM systems.

Around 48:20, he focuses on chunking strategy. Fixed-size chunks, sliding
windows, and context quality determine what the embedding model can retrieve.
Embeddings help only when the chunks preserve the information an answer needs.
The broader
[[search-rag-and-knowledge-systems|Search, RAG, and Knowledge Systems]]
page treats retrieval as search with generation attached.

## Recommendations and Multimodal Retrieval

Guests don't limit embeddings to text. In
[[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]],
Reem discusses multimodal embeddings at 33:13, including image-text matching
and CLIP-style representations. At 38:50, she expands the vector beyond raw
text or image content by adding metadata, behavior, and popularity. At 58:17,
she uses e-commerce personalization as a concrete example.

Atita connects vectors to recommendation use cases in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Around 52:07, she discusses vector databases for ML systems beyond RAG,
including session-based recommendations and re-ranking. The same separation
appears again. Embeddings retrieve candidates, while ranking, constraints, and
product goals decide what users actually see.

## NLP Data Work

[[person:johanneshotter|Johannes Hötter]] uses
embeddings from an [[NLP]] tooling perspective.
In
[[podcast:building-open-source-nlp-tool|Build Open-Source NLP Tools]],
he describes weak supervision and labeling workflows before connecting Hugging
Face, embeddings, and data management at 17:34. Embeddings can help teams look
at text, cluster similar examples, build heuristics, and manage messy labels
before a production search system exists.

This data-work framing makes embedding versioning part of model governance. If
labels, source documents, or model versions change, the stored vectors and
downstream checks may need to change too. Public search, RAG, and labeling use
embeddings differently. They share the same representation risk: a vector only
helps if it preserves the distinction the downstream task needs.

## Production Evaluation

Embeddings create operational work because vector search has multiple moving
parts. Reem's 29:00 split between embedding generation and vector storage in
[[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]
affects model versioning and query-vector compatibility. It also affects batch
reindexing, latency, and rollback. A vector database can store and retrieve
vectors, but it can't repair stale embeddings or a mismatch between document
and query encoders.

Evaluation has to match the product. Reem ties search quality to business KPIs
and A/B tests around 1:01:25. Atita adds answer quality, citation quality, and
human review for RAG around 48:09 in
[[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]].
Hugo adds gold evaluation sets and failure analysis for LLM workflows. His
23:00-27:38 discussion in
[[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]
covers logs and traces.

Nearest-neighbor matches are candidate evidence, not proof. A retrieved passage
can be wrong, stale, incomplete, or irrelevant to the user's real task. The
production system needs provenance, citations, feedback loops, and regression
tests. [[LLM Evaluation Workflows]]
covers LLM-specific checks, while
[[Production Search Evaluation]]
covers retrieval and ranking checks.
