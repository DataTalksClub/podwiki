---
layout: wiki
title: "Information Retrieval"
summary: "Information retrieval across candidate generation, indexes, prefilters, chunking, ranking boundaries, and RAG context retrieval."
related:
  - Search
  - Search Relevance
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - Vector Search vs Keyword Search
  - Production Search Evaluation
---

Information retrieval finds the right pieces of information from a larger
collection. It defines the retrieval unit, index, query representation, and
prefilters. It also defines the candidate set before [[search]] ranking or an
LLM answer takes over. Retrieval shapes
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]],
recommendations, and agent tools.

Information retrieval covers retrieval modeling. [[Search]] covers the
product-system hub, [[search-relevance=>search relevance]] covers ranking
quality and product fit, and [[Production Search Evaluation]] covers
measurement. Infrastructure and representation choices belong to their own
comparison pages.

## Retrieval Scope

Search is fundamentally a relevance decision problem: isolating relevant data
from a larger pile. Information retrieval is the common field behind both search
and personalized search, and it borders recommender systems and RAG
([[cite:building-production-search-systems=>Building Search Systems]]).

[[Search]] covers product search systems and user-facing relevance.
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] covers
generation, citations, and answer quality after retrieval.
[[Vector Search vs Keyword Search]] covers lexical-versus-semantic matching
choices.

Atita Arora keeps the classical learning path in view before vector databases
and RAG tooling. She names Introduction to Information Retrieval and Relevant
Search as useful starting points
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@57:50=>IR Learning Resources]]).
Those resources fit this page because they teach retrieval and ranking before a
team chooses a particular database, framework, or LLM wrapper. They also teach
evaluation.

The tooling changes, but the retrieval decision stays the same. The system has
to surface the evidence or candidate item that fits the query.

## Candidate Generation and Ranking

Information retrieval is two connected jobs: retrieve candidate items quickly,
then rank the smaller candidate set with richer signals
([[cite:building-production-search-systems=>Building Search Systems]]).
Candidate generation narrows the haystack to plausible results. Ranking then
estimates whether each query-result pair actually matches the task, which can
mean relevance or click probability. It can also mean purchase probability or
another product signal.

The practical search-quality question is matching the right content with the
right query
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
The same retrieval discipline applies to RAG inside LLM systems: the model can
only answer from the context the retriever finds.

## Indexes and Prefilters

Retrieval stays distinct from storage. It spans query rewriting, synonyms,
ingestion, and indexes
([[cite:building-production-search-systems=>Building Search Systems]]).

A search system prepares the query and corpus before matching. Latency is why
retrieval rarely means scanning every document. Teams need an index or another
data structure for user-facing latency.

Bloom filters answer a narrower retrieval question. Marcello La Rocca describes
them as probabilistic containment checks
[[cite:algorithms-data-structures-for-engineers@30:09=>Algorithms and Data Structures]].
They can say absence or possible presence, so false positives come with the design.
That makes them useful as a memory-saving prefilter, not as a final relevance
decision.

Common retrieval-adjacent uses include crawler URL deduplication
[[cite:algorithms-data-structures-for-engineers@34:43=>Bloom Filter Applications]].
Routing-table containment checks are another retrieval-adjacent use. Adtech
systems can screen device IDs or returning users before ranking or personalization
[[cite:algorithms-data-structures-for-engineers@35:59=>Adtech Bloom Filter Example]].

In lexical search, an inverted index links terms to the documents or positions
where they appear. This makes exact-word lookup efficient. Manual dictionaries
are brittle. Query rewrites, synonym rules, and normalization
choices add more brittleness.

Candidate generation sets the upper bound for later ranking. If the
retriever misses the relevant item, a reranker can't recover it. In a
podcast-transcript RAG system, teams chunk transcripts and embed the chunks.
The retriever returns a small number of relevant pieces before the LLM answers
from that context
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Chunk size, overlap, embedding model, and the number of retrieved chunks all
affect what the generator can see.

## Retrieval Boundaries Across Systems

The retrieval boundary shifts depending on the system being built. Search
systems center on lexical indexes, ranking,
business metrics, and product constraints
([[cite:building-production-search-systems=>Building Search Systems]]).
RAG discussions focus on chunking, [[context-engineering=>context engineering]],
and answer evaluation
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).
Agent discussions treat retrieval as one tool among table queries, APIs,
MongoDB, and other live systems
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

## Lexical and Semantic Retrieval

Lexical retrieval matches query terms against indexed text. It's still valuable
for exact words and filters, and it also helps with domain terminology or
predictable matching behavior. Solr and Lucene sat at the center of practical
search work before the current vector wave. Full-text search and NLP-based
query-content matching belonged to that same practical search work
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@4:42=>Solr and Lucene Search]]).

Sadat Anwar's OLX search story shows why teams often separate retrieval
infrastructure from the application that uses it. His team inherited Solr
firefighting and traced CPU-load spikes. They then decoupled search from the
monolith so they could change search independently
[[cite:from-software-engineering-to-leading-data-science-teams@6:31=>Search Engineering at OLX]]
[[cite:from-software-engineering-to-leading-data-science-teams@8:42=>Solr Autoscaling]]
[[cite:from-software-engineering-to-leading-data-science-teams@10:37=>Decoupling Search from Monolith]].
The ranking and product-quality consequences belong in [[search-relevance=>Search
Relevance]].

Semantic retrieval compares representations rather than only matching terms,
connecting bag-of-words search to dense vectors
([[cite:building-production-search-systems=>Building Search Systems]]).
Embedding models can turn documents and queries into vectors, and can also
encode images and user behavior. The system can then match items by proximity in
a shared representation space.

Semantic retrieval belongs with [[Embeddings]]. Storage and service ownership
belong with [[Vector Databases]] and [[Vector Database vs Search Engine]].

When teams add semantic retrieval, they don't always need to replace the
existing search stack
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@20:27=>Vectors in Existing Search]]).
The infrastructure decision belongs in [[Vector Database vs Search Engine]].

## Hybrid Retrieval Signals

Hybrid retrieval combines semantic similarity with filters, recency, and
popularity. It can also include personalization and business rules. A news
search result for "car" may need to be both relevant and fresh
([[cite:building-production-search-systems=>Building Search Systems]]).

A hard one-month filter can remove a highly relevant article older than 30 days.
Pure vector similarity may ignore freshness. The retrieval system has to balance
signals instead of treating every condition as an all-or-nothing filter.

That balancing act is where retrieval and ranking meet. Lucene-style `must` and
`should` constraints contrast with vector-query approaches that encode or weight
recency and popularity, along with user behavior and semantic relevance. The
retrieval-theory question is which signals narrow the candidate set before a
ranker sees it.

Signal weights are best postponed until query time when possible. A landing page
and a category page may need different weights over the same indexed data. A
personalized page may need different weights again.

Infrastructure pages own the service boundary. The information-retrieval design
still has to choose mandatory filters, soft retrieval features, and the handoff
to ranking. [[Vector Search vs Keyword Search]] covers the matching-method
comparison.

## RAG and Context Boundaries

RAG is retrieval plus context packaging plus generation, built from two core
pieces, retrieval and generation
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

In the retrieval step, the system converts the query to a vector query and
retrieves a chosen number of chunks. It can also return references so the
response is explainable. [[Vector Database vs Search Engine]] covers the
infrastructure choice for storing or searching those vectors.

The same design has a deployment rationale: indexing a changing knowledge base
and retrieving relevant sections
([[cite:deploying-llms-in-production-fine-tuning-retrieval-open-source-api=>Deploying LLMs in Production]]).
Teams inject those sections into a prompt and may use a summarizer for sensitive
tasks.

Retrieval doesn't make the model smarter in general. It grounds the answer in
the current documentation, which is different from fine-tuning the model to
imitate a style or task format. That retrieval boundary is central to
[[rag-vs-fine-tuning=>RAG vs Fine-Tuning]].

Large context windows don't remove retrieval work, because latency, cost, and
noisy context still matter
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Older retrieval backends were built for people clicking "blue links", not for
feeding LLM context. This is why RAG systems often need chunk metadata, source
provenance, and context wrappers, not only top-k vector search. Those choices
belong to [[context-engineering=>context engineering]] once the retrieved
material becomes model input.

Retrieval is one tool inside agentic systems: RAG or search-style information
retrieval is a tool to use when needed
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).
Agents may also query tables, MongoDB, APIs, or other systems. RAG can
reduce a large search space to useful context, while agents fit work that needs
multiple data sources, dynamic planning, and tool use.

## Retrieval Evaluation

Evaluate information retrieval by checking whether the right unit entered the
candidate set. In a search engine, that unit may be a document or product. It
may also be an image or session. In RAG, it may be a transcript chunk or
passage. It may also be a graph neighborhood or source-backed context block.

If the retriever misses that unit, later ranking or generation can't recover it
([[cite:building-production-search-systems=>Building Search Systems]]).

IR evaluation checks candidate recall, filters, index freshness, and ranking
handoff. RAG retrieval evaluation checks chunk size, overlap, and embedding
model choice. It also checks retrieval count, source metadata, and whether the
retrieved passages contain enough evidence for the answer
([[cite:modern-search-systems-vector-databases-llms-semantic-retrieval=>Modern Search Systems]]).

Prefilters deserve their own checks. A Bloom filter can cheaply say that an
item is absent or possibly present. False positives mean it can't make the
final relevance decision
[[cite:algorithms-data-structures-for-engineers@30:09=>Algorithms and Data Structures]].
The same boundary applies to hard metadata filters, permissions, and date
constraints. They reduce the search space before ranking, but they can also
exclude the result the downstream task needed.

When retrieval becomes one tool inside [[Agent Engineering]] or
[[agent-engineering=>AI Agents]], evaluate the retriever against the local
system boundary, not only a public model benchmark. Representative datasets and
integration tests help catch failures before an agent reasons over missing or
wrong context. Teams can use mocked tools and assertions over retrieved objects
too
([[cite:building-agentic-ai-engineering-tooling-retrieval-evaluation=>Building Agentic AI Systems]]).

[[Production Search Evaluation]] owns the measurement workflow across ranking
metrics, A/B tests, monitoring, and business outcomes. [[Search Relevance]]
covers the question of which candidates deserve top positions.

## System Boundaries

Design retrieval around the object being found and the decision that follows.
In product search, teams may retrieve products or recommendation candidates.
In RAG, teams may retrieve chunks or graph paths. An agent may retrieve logs,
metrics, database rows, or API responses.

Search and recommendations are neighboring brackets around the same information
retrieval field, as are personalized search and RAG
([[cite:building-production-search-systems=>Building Search Systems]]).

Information retrieval is narrower than the whole [[Search]] product and broader
than any one indexing technology. Retrieval design choices include lexical
indexes, vector indexes, and chunking strategies. Metadata filters and
evaluation datasets are retrieval design choices too. Teams use those choices to
decide what to retrieve and how to narrow the search space before ranking or
generation.
