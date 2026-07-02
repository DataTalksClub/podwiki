---
layout: wiki
title: "Information Retrieval"
summary: "How DataTalks.Club podcast guests discuss retrieval discipline across candidate generation, ranking, RAG, and evaluation."
related:
  - Search
  - Retrieval-Augmented Generation
  - Vector Databases
  - Embeddings
  - Production Search Evaluation
---

Information retrieval finds the right pieces of information from a larger
collection. It has to satisfy time, quality, and system constraints. In
DataTalks.Club podcast discussions, retrieval sits behind
[[search]] and
[[vector databases]]. It also
shapes
[[retrieval-augmented-generation|Retrieval-Augmented Generation]],
recommendations, and agent tools.

Search is fundamentally a relevance decision problem: isolating relevant data
from a larger pile. Information retrieval is the common field behind both search
and personalized search, and it borders recommender systems and RAG
([[podcast:building-production-search-systems|Building Search Systems]]).

For product search systems and user-facing relevance, start with
[[Search]]. For generation, citations, and
answer quality after retrieval, use
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].
For the broader map across retrieval systems and LLM applications, use
[[retrieval-augmented-generation|Retrieval-Augmented Generation]].

## Candidate Generation and Ranking

Information retrieval is two connected jobs: retrieve candidate items quickly,
then rank the smaller candidate set with richer signals
([[podcast:building-production-search-systems|Building Search Systems]]).
Candidate generation narrows the haystack to plausible results. Ranking then
estimates whether each query-result pair actually matches the task, which can
mean relevance or click probability. It can also mean purchase probability or
another product signal.

The practical search-quality question is matching the right content with the
right query, and teams need to measure search quality against business goals
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
The same retrieval discipline carries into RAG inside LLM systems: the model can
only answer from the context the retriever finds.

## Candidate Generation and Indexing

Retrieval stays distinct from storage, spanning query rewriting, synonyms,
ingestion, and indexes
([[podcast:building-production-search-systems|Building Search Systems]]).

A search system prepares the query and corpus before matching. Latency is why
retrieval rarely means scanning every document. Teams need an index or another
data structure for user-facing latency.

In lexical search, an inverted index links terms to the documents or positions
where they appear. This makes exact-word lookup efficient, but handcrafted
dictionaries are brittle, and query rewrites, synonym rules, and normalization
choices add more brittleness.

Candidate generation sets the upper bound for later ranking. If the
retriever misses the relevant item, a reranker can't recover it. A
podcast-transcript RAG example makes this concrete: teams chunk transcripts and
embed the chunks, and the retriever returns a small number of relevant pieces
before the LLM answers from that context
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Chunk size, overlap, embedding model, and the number of retrieved chunks all
affect what the generator can see.

## Lexical and Semantic Retrieval

Lexical retrieval matches query terms against indexed text. It's still valuable
when the task depends on exact words, filters, domain terminology, or
predictable matching behavior. Solr and Lucene sat at the center of practical
search work before the current vector wave, alongside full-text search and
NLP-based query-content matching
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

Semantic retrieval compares representations rather than only matching terms,
connecting bag-of-words search to dense vectors
([[podcast:building-production-search-systems|Building Search Systems]]).
Embedding models can turn documents and queries into vectors, and can also
encode images and user behavior. The system can then match items by proximity in
a shared representation space.

Semantic retrieval belongs with
[[Embeddings]] as much as with
[[Vector Databases]].
Vector storage and vector compute are separate concerns. Teams compute vectors
during ingestion and at query time, and both paths must land in the same vector
space. When documents change or embedding models change, teams may need to
recompute vectors or rebuild indexes.

The architecture choice comes next: teams don't always need to dump an existing
Solr, Elasticsearch, or OpenSearch stack when they add vectors
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
A standalone vector database can sit beside the current search system when
reindexing the production stack is risky.

## Hybrid Retrieval and Ranking

Hybrid retrieval combines semantic similarity with filters, recency, and
popularity. It can also include personalization and business rules. A news
search result for "car" may need to be both relevant and fresh
([[podcast:building-production-search-systems|Building Search Systems]]):
a hard one-month filter can remove a highly relevant article older than 30 days,
while pure vector similarity may ignore freshness. The retrieval system has to
balance signals instead of treating every condition as an all-or-nothing filter.

That balancing act is where retrieval and ranking meet. Lucene-style `must` and
`should` constraints contrast with vector-query approaches that encode or weight
recency and popularity, along with user behavior and semantic relevance.

Signal weights are best postponed until query time when possible. A landing page
and a category page may need different weights over the same indexed data. A
personalized page may need different weights again.

The comparison with
[[Vector Database vs Search Engine]]
comes from the same boundary. A vector database can return nearest neighbors,
but an information retrieval system still has to choose mandatory filters and
soft ranking features. Teams also choose which reranker to run and how to keep
the index fresh. A vector database is retrieval infrastructure, not the whole
retrieval discipline.

## RAG and Context Boundaries

RAG is retrieval plus context packaging plus generation, built from two core
pieces, retrieval and generation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).

In the retrieval step, the system converts the query to a vector query and sends
it to a vector search engine. It retrieves a chosen number of chunks and places
those chunks in the prompt, and it can also return references so the response is
explainable.

The same design has a deployment rationale: indexing a changing knowledge base
and retrieving relevant sections
([[podcast:deploying-llms-in-production-fine-tuning-retrieval-open-source-api|Deploying LLMs in Production]]).
Teams inject those sections into a prompt and may use a summarizer for sensitive
tasks.

Retrieval doesn't make the model smarter in general. It grounds the answer in
the current documentation, which is different from fine-tuning the model to
imitate a style or task format. That retrieval boundary is central to
[[rag-vs-fine-tuning|RAG vs Fine-Tuning]].

Large context windows don't remove retrieval work, because latency, cost, and
noisy context still matter
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Older retrieval backends were built for people clicking "blue links", not for
feeding LLM context. This is why RAG systems often need chunk metadata, source
provenance, and context wrappers, not only top-k vector search.

Retrieval is one tool inside agentic systems: RAG or search-style information
retrieval is a tool to use when needed
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Agents may also query tables, MongoDB, APIs, or other systems. RAG can
reduce a large search space to useful context, while agents fit work that needs
multiple data sources, dynamic planning, and tool use.

## Evaluation

Retrieval evaluation has to cover both the result set and the downstream task.
Search relevance ties to business outcomes: teams should connect retrieval and
ranking changes to business metrics
([[podcast:building-production-search-systems|Building Search Systems]]).
They should run careful A/B tests when possible and use offline evaluation or
operational metrics that engineers can iterate on. Information retrieval
shares that evaluation discipline with
[[Production Search Evaluation]]
and [[MLOps]].

Classic search evaluation differs from RAG evaluation
([[podcast:modern-search-systems-vector-databases-llms-semantic-retrieval|Modern Search Systems]]).
Ecommerce search has a clearer query-response setup with precision and recall
concepts. RAG evaluation needs multiple layers: teams evaluate the embedding
model and the chunking strategy, and also the retrieval strategy and the
end-to-end answer.

This distinction matters because a RAG answer can fail even when the vector
database returns similar chunks. A generated answer can also look fluent while
the retrieved evidence is incomplete.

For agents, there's a system-benchmark version
([[podcast:building-agentic-ai-engineering-tooling-retrieval-evaluation|Building Agentic AI Systems]]).
Public benchmarks such as SQuAD evaluate model capability, not the team's
retrieval or agent system. Teams need their own representative datasets,
integration tests, mocked tools, and assertions over outcomes. That applies
when retrieval is one step inside
[[Agent Engineering]] or
[[agent-engineering|AI Agents]], not a standalone search
endpoint.

## System Boundaries

Design retrieval around the object being found and the decision that follows.
In product search, teams may retrieve products or recommendation candidates.
In RAG, teams may retrieve chunks or graph paths. An agent may retrieve logs,
metrics, database rows, or API responses.

Search and recommendations are neighboring brackets around the same information
retrieval field, as are personalized search and RAG
([[podcast:building-production-search-systems|Building Search Systems]]).

Information retrieval is narrower than the whole
[[Search]] product and broader than any one
indexing technology. Retrieval design choices include lexical indexes, vector
indexes, rerankers, and chunking strategies. Metadata filters and evaluation
datasets are retrieval design choices too. Teams use those choices to decide
what to retrieve and how to narrow the search space. They also use them to rank
candidates and prove that the retrieved information helped the person or system
that needed it.
