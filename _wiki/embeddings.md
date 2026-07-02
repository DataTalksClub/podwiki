---
layout: wiki
title: "Embeddings"
summary: "How DataTalks.Club guests explain embeddings as representations for semantic search, RAG, recommendations, multimodal retrieval, and language systems."
related:
  - Vector Databases
  - Search
  - Retrieval-Augmented Generation
  - NLP
---

Embeddings are numerical representations of text and images, users and products,
or other objects. They let a system compare meaning or behavior by distance in a
shared vector space instead of comparing only exact words or hand-written rules.

Embeddings sit behind
[[search]] and
[[vector databases]], and they also
appear in
[[retrieval-augmented-generation|retrieval-augmented generation]]
systems. Recommendation systems and multimodal retrieval use them too.

In
weak-supervision workflows and production
[[machine-learning-system-design|ML systems]],
they're a representation layer, not the whole product. Embedding generation
stays separate from storage and ranking, and from evaluation, citations, and
business logic.

## Representation Space

Queries and searchable items can be mapped into the same representation space,
so retrieval finds items with similar meaning even when the words differ
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
Vector compute stays separate from vector storage: the embedding model is
distinct from the database that stores and searches vectors.

The same representation idea takes a retrieval-system frame in a
transcript-chatbot example, where chunks with overlap are embedded and stored as
vectors for retrieval
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
The embedding model creates the representation and the
[[vector-databases|vector database]] retrieves nearby vectors, while the
application still needs prompts, references, and evaluation.

In production LLM systems, vector databases work through embeddings, indexing,
and semantic search
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Retrieval fits changing knowledge, while fine-tuning changes model behavior or
style, a boundary expanded in
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]].

## Semantic Search

Keyword matching can be too brittle when users express the same intent with
different language
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
Vector search matches queries and documents through shared representations,
which keeps embeddings inside the larger
[[information retrieval]]
system. Vector search changes candidate generation, but it doesn't replace
ranking.

Candidate generation is separate from ML ranking
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
A vector match finds plausible candidates, but the product still decides which
result belongs first and trades semantic similarity against freshness and
popularity.

Metadata, behavior, query-time weights, and business rules also matter. Filters
and recency make embeddings one signal inside
[[production search evaluation]],
not a substitute for product ranking
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).

The architecture choice is explicit: plug-and-play vector search versus vector
support inside existing search systems
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
That decision is the same boundary covered in
[[Vector Database vs Search Engine]].
Teams can choose the embedding model, vector storage, and search application
behavior as separate design decisions.

## RAG Systems

In [[retrieval-augmented-generation|RAG]], embeddings retrieve context for a
language model. A transcript-chatbot example chunks transcripts with overlap,
embeds them, retrieves relevant passages, and generates an answer with
references
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Evaluation then extends beyond nearest-neighbor retrieval into generated answer
quality, citation quality, and human review.

The update path favors retrieval over retraining for systems that need current
or proprietary knowledge
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
A team can re-ingest, re-embed, and re-index documents instead of fine-tuning the
model every time facts change.

Chunking and embeddings are a practical first step for useful LLM systems
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).
Fixed-size chunks, sliding windows, and context quality determine what the
embedding model can retrieve, so embeddings help only when the chunks preserve
the information an answer needs. The broader
[[retrieval-augmented-generation|Retrieval-Augmented Generation]]
page treats retrieval as search with generation attached.

## Recommendations and Multimodal Retrieval

Embeddings aren't limited to text. Multimodal embeddings include image-text
matching and CLIP-style representations, and the vector can extend beyond raw
text or image content by adding metadata, behavior, and popularity, as in
e-commerce personalization
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).

Vector databases serve ML systems beyond RAG, including session-based
recommendations and re-ranking
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
The same separation holds: embeddings retrieve candidates, while ranking,
constraints, and product goals decide what users actually see.

## NLP Data Work

From an [[NLP]] tooling perspective, embeddings connect to weak supervision,
labeling workflows, Hugging Face, and data management
([[podcast:building-open-source-nlp-tool|Build Open-Source NLP Tools]]).
They help teams look at text, cluster similar examples, build heuristics, and
manage messy labels before a production search system exists.

This data-work framing makes embedding versioning part of model governance. If
labels, source documents, or model versions change, the stored vectors and
downstream checks may need to change too. Public search, RAG, and labeling use
embeddings differently. They share the same representation risk: a vector only
helps if it preserves the distinction the downstream task needs.

## Production Evaluation

Embeddings create operational work because vector search has multiple moving
parts. The split between embedding generation and vector storage affects model
versioning, query-vector compatibility, batch reindexing, latency, and rollback
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
A vector database can store and retrieve vectors, but it can't repair stale
embeddings or a mismatch between document and query encoders.

Evaluation has to match the product. Search quality ties to business KPIs and
A/B tests
([[podcast:production-ml-search-vector-search-embeddings-hybrid-search|Production ML Search]]).
RAG adds answer quality, citation quality, and human review
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
LLM workflows add gold evaluation sets, failure analysis, logs, and traces
([[podcast:practical-llm-engineering-and-rag|Practical LLM Engineering and RAG]]).

Nearest-neighbor matches are candidate evidence, not proof. A retrieved passage
can be wrong, stale, incomplete, or irrelevant to the user's real task. The
production system needs provenance, citations, feedback loops, and regression
tests. [[LLM Evaluation Workflows]]
covers LLM-specific checks, while
[[Production Search Evaluation]]
covers retrieval and ranking checks.
