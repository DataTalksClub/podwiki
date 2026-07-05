---
layout: wiki
title: "Embeddings"
summary: "How DataTalks.Club guests explain embeddings as representations for semantic search, RAG, recommendations, multimodal retrieval, and language systems."
related:
  - Vector Databases
  - Search
  - Retrieval-Augmented Generation
  - Multimodal LLMs
  - NLP
---

Embeddings are numerical representations of text and images, users and products,
or other objects. They let a system compare meaning or behavior by distance in a
shared vector space instead of comparing only exact words or hand-written rules.

Embeddings sit behind
[[search]] and
[[vector databases]], and they also
appear in
[[retrieval-augmented-generation=>retrieval-augmented generation]]
systems. Recommendation systems and multimodal retrieval use them too.

In
weak-supervision workflows and production
[[machine-learning-system-design=>ML systems]],
they're a representation layer, not the whole product. Embedding generation
stays separate from storage and ranking, and from evaluation, citations, and
business logic.

## Representation Space

A search system can map queries and searchable items into the same
representation space. Retrieval can then find items with similar meaning even
when the words differ
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
Vector compute stays separate from vector storage: the embedding model is
distinct from the database that stores and searches vectors.

A transcript-chatbot example uses the same representation idea in a retrieval
system. Chunks with overlap are embedded and stored as vectors for retrieval
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
The embedding model creates the representation and the
[[vector-databases=>vector database]] retrieves nearby vectors. The application
still needs prompts, references, and evaluation.

Marcello La Rocca connects this representation layer to the underlying
nearest-neighbor problem. Once items, users, or images become vectors, search
finds nearby points in multi-dimensional space. Exact search can become too
costly as dimensionality grows. Approximate nearest-neighbor structures and
libraries such as Faiss trade a small amount of optimality for faster candidate
retrieval
([[cite:algorithms-data-structures-for-engineers@44:46=>Vector Similarity and Faiss]]).

In production LLM systems, vector databases work through embeddings, indexing,
and semantic search
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
Retrieval fits changing knowledge, while fine-tuning changes model behavior or
style, a boundary expanded in
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

## Semantic Search

Keyword matching can be too brittle when users express the same intent with
different language
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
Vector search matches queries and documents through shared representations,
which keeps embeddings inside the larger
[[information retrieval]]
system. Vector search changes candidate generation, but it doesn't replace
[[search-relevance=>search relevance]] work or ranking.

Candidate generation is separate from ML ranking
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
A vector match finds plausible candidates, but the product still decides which
result belongs first and trades semantic similarity against freshness and
popularity.

Metadata, behavior, query-time weights, and business rules also matter. Filters
and recency make embeddings one signal inside
[[production search evaluation]],
not a substitute for product ranking
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).

The architecture choice is explicit: plug-and-play vector search versus vector
support inside existing search systems
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
That decision is the same boundary covered in
[[Vector Database vs Search Engine]].
Teams can choose the embedding model, vector storage, and search application
behavior as separate design decisions.

## RAG Systems

In [[retrieval-augmented-generation=>RAG]], embeddings retrieve context for a
language model. A transcript-chatbot example chunks transcripts with overlap,
embeds them, retrieves relevant passages, and generates an answer with
references
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Evaluation then extends beyond nearest-neighbor retrieval into generated answer
quality, citation quality, and human review.

The update path favors retrieval over retraining for systems that need current
or proprietary knowledge
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
A team can re-ingest, re-embed, and re-index documents instead of fine-tuning the
model every time facts change.

Chunking and embeddings are a practical first step for useful LLM systems
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).
Fixed-size chunks, sliding windows, and context quality determine what the
embedding model can retrieve. Embeddings help only when the chunks preserve the
information an answer needs. The broader
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]]
page treats retrieval as search with generation attached.

## Recommendations and Multimodal Retrieval

Embeddings aren't limited to text, and multimodal embeddings include image-text
matching and CLIP-style representations. The vector can also extend beyond raw
text or image content by adding metadata, behavior, and popularity, as in
e-commerce personalization
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
That shared image-text space helps
[[multimodal-llms=>multimodal LLMs]] retrieve across modalities.

Vector databases also serve session-based recommendations and re-ranking outside
RAG
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Embeddings retrieve candidates for the next stage. Ranking, constraints, and
product goals decide what users actually see. This boundary is central to
[[machine-learning-personalization=>machine learning personalization]]. A nearby
vector match is only useful if the product can rank it for the current user or
session.

In the OLX recommender example, users and items are fixed-length vectors. The
system can search for item vectors close to a user's vector. Similar-image
retrieval uses the same vector-search structure because the embedding narrows
the candidate set. The recommender or search system then decides which nearby
items are useful enough to show.
Marcello La Rocca makes the same general connection between vector similarity,
embeddings, recommender systems, and Faiss
[[cite:algorithms-data-structures-for-engineers@44:46=>Vector Similarity and Recommendations]].

## NLP Data Work

From an [[NLP]] tooling perspective, embeddings connect to weak supervision and
labeling workflows. They also connect to Hugging Face and data management
([[cite:building-open-source-nlp-tool=>Build Open-Source NLP Tools]]).
They help teams look at text, cluster similar examples, build heuristics, and
manage messy labels before a production search system exists.

This data-work framing makes embedding versioning part of model governance. If
labels, source documents, or model versions change, the stored vectors and
downstream checks may need to change too. Public search, RAG, and labeling use
embeddings differently. They share the same representation risk: a vector only
helps if it preserves the distinction the downstream task needs.

## Production Evaluation

Vector search has multiple moving parts, so embeddings create operational work.
Teams have to manage model versioning, query-vector compatibility, and batch
reindexing. They also have to manage latency and rollback
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
A vector database can store and retrieve vectors, but it can't repair stale
embeddings or a mismatch between document and query encoders.

Evaluation has to match the product. Search quality ties to business KPIs and
A/B tests
([[cite:production-ml-search-vector-search-embeddings-hybrid-search=>Production ML Search]]).
RAG adds answer quality, citation quality, and human review
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
LLM workflows add gold evaluation sets, failure analysis, logs, and traces
([[cite:practical-llm-engineering-and-rag=>Practical LLM Engineering and RAG]]).

Nearest-neighbor matches are candidate evidence, not proof. A retrieved passage
can be wrong, stale, incomplete, or irrelevant to the user's real task. The
production system needs provenance, citations, feedback loops, and regression
tests. [[LLM Evaluation Workflows]]
covers LLM-specific checks, while
[[Production Search Evaluation]]
covers retrieval and ranking checks.
