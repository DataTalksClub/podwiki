---
layout: wiki
title: "Embeddings"
summary: "How the podcast archive explains embeddings as representations for semantic search, RAG, recommendations, multimodal retrieval, and language systems."
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

In the DataTalks.Club archive, embeddings often sit behind
[search]({{ '/wiki/search/' | relative_url }}),
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}), and
[retrieval-augmented generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).
They also support recommendation systems, multimodal retrieval,
weak-supervision workflows, and production
[ML systems]({{ '/wiki/machine-learning-system-design/' | relative_url }}).
They aren't the whole product. The archive separates embedding generation from
storage, ranking, evaluation, and business logic.

## Common Definition

The strongest archive episodes use embeddings as learned representations for
search and retrieval.

In
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
[Reem Mahmoud]({{ '/people/reemmahmoud/' | relative_url }}) maps the concept to
vector search. At 21:55, she explains that queries and searchable items can be
mapped into the same representation space. That shared space lets a system
retrieve items with similar meaning even when the words differ.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the same idea a
retrieval-system frame in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 38:24, she walks through transcript ingestion for RAG. The system splits
documents into chunks, chooses overlap, creates embeddings, and stores vectors
for retrieval.

The example separates three responsibilities. The embedding model creates the
representation, and the
[vector database]({{ '/wiki/vector-databases/' | relative_url }}) retrieves
nearby vectors. The application still needs prompts, citations, and evaluation.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) connects embeddings
to production LLM systems in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 48:01, she describes vector databases through embeddings, indexing, and
semantic search. Her surrounding discussion distinguishes retrieval from
fine-tuning. Retrieval fits changing knowledge, while fine-tuning changes model
behavior or style.

## Guest Differences

Guests agree on the representation idea, but each guest stresses another risk.
Reem's production-search discussion focuses on product ranking. Around
29:00 in
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
she separates vector compute from vector storage. Around 34:00-45:11, she adds
filters and recency. She also adds popularity, metadata, behavior, and
query-time weights.

Her view treats embeddings as one signal inside a
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
problem.

Atita's view starts from information retrieval. In
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she moves from Solr and Lucene to vector databases, LLMs, and RAG. At 20:27 she
frames the architecture choice as a migration decision: add vectors to an
existing search stack or introduce a dedicated vector database. See
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
for that architecture boundary. At 48:09, she
pushes evaluation beyond nearest-neighbor retrieval into generated answer
quality, citations, and human review.

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) starts
from practical LLM workflows. In
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
he says around 44:26 that RAG can be a quick business win. That happens when
the chunking and embedding setup fits the problem. At 48:20, he focuses on
chunking strategy.
Fixed-size chunks, sliding windows, and context quality determine what the
embedding model can retrieve.

[Johannes Hötter]({{ '/people/johanneshotter/' | relative_url }}) uses
embeddings from an NLP tooling perspective. In
[Build Open-Source NLP Tools]({{ '/podcasts/building-open-source-nlp-tool/' | relative_url }}),
the 17:34 section places Hugging Face, embeddings, and data management inside
weak-supervision and labeling workflows. That keeps embeddings connected to
[NLP]({{ '/wiki/nlp/' | relative_url }}) data work, not only chatbots.

## Search and Semantic Retrieval

Keyword matching can become too brittle for search teams.

In
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
Reem describes keyword search challenges around 20:02. At 21:55, she introduces
vector search as a way to match queries and documents through shared
representations. That doesn't remove classical
[information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).
It changes what candidate generation can do.

The search stack still needs ranking. Reem separates candidate generation from
ML ranking at 12:45 and returns to operational search metrics at 1:01:25. A
vector match can find plausible candidates. The product still has to decide
which result belongs first. It also has to trade semantic similarity against
freshness, popularity, and business rules.

Atita makes the architecture choice explicit in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 17:01 and 20:27, she compares plug-and-play vector search with vector
support inside existing search systems. That comparison supports a recurring
archive claim. Teams should choose embeddings, vector storage, and search
application behavior separately.

## RAG and Knowledge Systems

In RAG, embeddings retrieve context for a language model. The archive treats
RAG as a search problem with generation attached. It isn't only an LLM feature.

Atita's transcript-chatbot example in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
starts at 35:49 and becomes concrete at 38:24. The system chunks transcripts
and sets overlap. It embeds chunks, retrieves the relevant passages, and then
generates an answer with references.

Meryem's production discussion adds the update path. In
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
she compares retrieval with retraining around 40:46-42:02. Retrieval fits
systems that need current or proprietary knowledge. The team can re-ingest,
re-embed, and re-index documents instead of fine-tuning the model every time
facts change. That's the same distinction used on
[RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }}).

Hugo's RAG workflow gives the builder's version of the same idea. Around 44:26
in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
he presents chunking and embeddings as a practical first step for useful LLM
systems. Around 48:20, he warns that chunk boundaries and context rot determine
whether retrieval gives the model the right evidence. Embeddings help only if
the chunks preserve the information the answer needs.

## Recommendations and Multimodal Systems

The archive doesn't limit embeddings to text. In
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}),
Reem discusses multimodal embeddings at 33:13, including image-text matching
and CLIP-style representations. At 38:50, she expands the vector beyond raw
text or image content by adding metadata, behavior, and popularity. At 58:17,
she uses e-commerce personalization as a concrete example.

Atita also connects vectors to recommendation use cases in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
Around 52:07, she discusses vector databases for ML systems beyond RAG,
including session-based recommendations and re-ranking. The same split appears
again. Embeddings retrieve candidates, while ranking, constraints, and product
goals decide what users actually see.

## NLP Tooling and Labeling

Embeddings also appear in the archive as infrastructure for training-data work.
In
[Build Open-Source NLP Tools]({{ '/podcasts/building-open-source-nlp-tool/' | relative_url }}),
Johannes describes weak supervision and labeling workflows before connecting
Hugging Face, embeddings, and data management at 17:34. This work goes beyond
retrieval. Embeddings help teams look at text, cluster similar examples, build
heuristics, and manage messy labels.

That makes embeddings part of the wider [NLP]({{ '/wiki/nlp/' | relative_url }})
workflow, and a team may use them before production search exists. Common uses
include data exploration, active learning, weak supervision, and error analysis.
The representation still needs governance. If labels, source documents, or
model versions change, the embeddings and downstream checks may need to change
too.

## Evaluation and Production Tradeoffs

Embeddings create operational work because Reem separates embedding generation
from vector storage at 29:00 in
[Production ML Search]({{ '/podcasts/production-ml-search-vector-search-embeddings-hybrid-search/' | relative_url }}).
That split affects model versioning and query-vector compatibility. Teams also
have to plan batch reindexing, latency, and rollback. A vector database can
store and retrieve vectors, but it can't repair stale embeddings or a mismatch
between document and query encoders.

Because evaluation has to match the product, search teams test retrieval,
ranking, and product outcomes separately. Reem ties this to business KPIs and
A/B tests around 1:01:25. For RAG, Atita adds answer quality and citation
quality around 48:09 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
She also adds human review.

For LLM workflows, Hugo adds gold evaluation sets and failure analysis. Around
23:00-27:38, he also covers logs and traces in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).

Nearest-neighbor matches are candidate evidence, not proof. A retrieved passage
can be wrong, stale, incomplete, or irrelevant to the user's real task. The
production system needs provenance, citations, feedback loops, and regression
tests. Use
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
for LLM-specific checks and
[Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
for retrieval and ranking checks.

## Related Pages

Use these pages for the surrounding architecture and evaluation details.

- [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
- [Vector Databases]({{ '/wiki/vector-databases/' | relative_url }})
- [Search]({{ '/wiki/search/' | relative_url }})
- [Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }})
- [NLP]({{ '/wiki/nlp/' | relative_url }})
- [Machine Learning System Design]({{ '/wiki/machine-learning-system-design/' | relative_url }})
- [RAG vs Fine-Tuning]({{ '/wiki/rag-vs-fine-tuning/' | relative_url }})
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
- [LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
