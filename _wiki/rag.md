---
layout: wiki
title: "RAG"
summary: "A practical DataTalks.Club guide to RAG implementation choices and boundaries."
related:
  - Retrieval-Augmented Generation
  - Search, RAG, and Knowledge Systems
  - RAG vs Fine-Tuning
  - Vector Databases
  - LLM Evaluation Workflows
  - Agent Engineering
---

RAG is the short name for retrieval-augmented generation. DataTalks.Club guests
use it to answer from external sources instead of asking an
[LLM]({{ '/wiki/llms/' | relative_url }}) to rely only on model weights. For a
deeper concept page, use
[Retrieval-Augmented Generation]({{ '/wiki/retrieval-augmented-generation/' | relative_url }}).

Use this common-name page for practical RAG implementation choices around
retrieval chunks, [embeddings]({{ '/wiki/embeddings/' | relative_url }}), and
[vector databases]({{ '/wiki/vector-databases/' | relative_url }}). It also
covers citation and evaluation choices, plus security and graph variants. For
the boundary with [fine-tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }})
and [agents]({{ '/wiki/agent-engineering/' | relative_url }}), continue to the
final section.

[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) gives the archive's
clearest RAG definition in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 30:38, she describes RAG as retrieval plus generation. The system retrieves
client or product context and gives it to the model so the answer has a basis
outside the model's training data.

She then turns that definition into a podcast
transcript example at 35:49-42:49. The example moves from transcript chunking
to embeddings and vector search. It then covers prompt context, answers, and
references.

## Retrieval Before Generation

The archive's RAG advice starts with [search]({{ '/wiki/search/' | relative_url }})
and [information retrieval]({{ '/wiki/information-retrieval/' | relative_url }}),
not with generation. Atita's transcript chatbot starts by asking how to find the
right part of many podcast transcripts for a user's question
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
38:24). The LLM only answers after the system has retrieved useful context.

That order matters because a fluent answer can still be unsupported. Atita ties
RAG to hallucination reduction at 30:38 and to source references at 42:49. In
the same episode, she also explains why teams have to test the retrieval
strategy. They can vary the embedding model, chunk size, overlap, and number of
retrieved chunks. Then they can compare whether the final answer improves.

[Meryem Arik]({{ '/people/meryemarik/' | relative_url }}) gives the production
reason for retrieval in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}).
At 40:46-46:42, she describes customer-support knowledge bases where the correct
answer changes over time. Instead of retraining the model for every update, the
team can index the documentation, retrieve relevant sections, and let the model
answer from those sections.

## Chunking And Context

Chunking isn't a formatting detail in the podcast discussions because it decides
what the model can see and cite. Atita explains at 40:01 that chunking should
follow the answer experience the product wants. If the user needs a specific
answer, the system needs chunks that preserve enough surrounding text and
speaker context. It also needs overlap for pronouns and references to make sense
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})).

[Hugo Bowne-Anderson]({{ '/people/hugobowneanderson/' | relative_url }}) makes
the same point from a builder's perspective in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}).
At 44:26-49:21, he treats a focused RAG bot with good chunking, embeddings, and
an interface as a practical business win. He also says chunking depends on the
data. Transcripts can be split by question-answer pairs, speaker turns, or topic
shifts. Videos or books may need different boundaries.

[Ranjitha Kulkarni]({{ '/people/ranjithakulkarni/' | relative_url }}) connects
RAG to context engineering in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}).
At 29:30-32:48, she argues that long context doesn't remove the need to reduce
noise. A length-only split is lossy, so the retrieved context should include
the source document, the question it answers, and what the system has already
learned.

## Embeddings And Vector Stores

Many RAG systems use vector retrieval, but the archive doesn't equate RAG with a
vector database. Atita introduces Qdrant and other vector stores at 17:01 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
At 20:27, she compares standalone vector databases with adding vectors to
existing search stacks such as Solr and Elasticsearch. She also mentions
OpenSearch and Postgres. Teams should start from the use case, then decide
whether specialized vector search is needed.

Meryem gives the LLM version at 48:01 in
[Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}):
the system embeds documents and indexes them. At query time, it embeds the
question and looks up similar vectors before generation. That retrieval layer
helps the model answer from documentation, but the application still owns source
selection and permissions. It also owns citations and evaluation.

For the storage choice, use
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
and [Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }}).
Those pages connect RAG to indexing, ranking, filters, and metadata. They also
keep freshness and product metrics in view.

## Citations And Evaluation

RAG is useful when people can look at why the answer was produced. Atita
explicitly connects references to explainability and user trust at 42:49 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}).
For this wiki, that translates into local episode links, guest links, and
timestamps near claims instead of unsupported summary text.

Evaluation has to separate retrieval failures from generation failures. Atita's
48:09 discussion breaks RAG evaluation into the embedding model and chunking
strategy. It also covers retrieval strategy and end-to-end answer quality.
Hugo's [Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }})
episode adds the day-to-day work. At 23:00, he recommends representative gold
tests.

At 26:43, Hugo recommends failure analysis so teams know whether to fix
retrieval or prompting. Formatting and data preparation can be separate failure
sources too.

Ranjitha extends the same evaluation idea when retrieval becomes part of an
agent. At 51:17-53:20 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
she argues for custom datasets and system benchmarks. She also argues for
mocked tools, integration tests, and regression tests. Use
[LLM Evaluation Workflows]({{ '/wiki/llm-evaluation-workflows/' | relative_url }})
when the question is how to test the RAG system rather than how to build the
index.

## Security And Access

RAG security starts before the model answers. The system shouldn't retrieve
documents the user isn't allowed to see. The answer shouldn't leak restricted
content through summaries or citations. The archive's clearest
LLM-security discussion comes from
[Maria Sukhareva]({{ '/people/mariasukhareva/' | relative_url }}) in
[Hardening Generative AI Chatbots]({{ '/podcasts/generative-ai-chatbots-in-production-security/' | relative_url }}).
At 13:20, she describes data exfiltration from a knowledge database through
prompt attacks.

At 16:15-17:00, she recommends layered defenses such as query
analysis and output validation. She also recommends sensitive-content
classifiers, including non-LLM classifiers where generative models are too easy
to manipulate.

Those controls apply directly to RAG because retrieved documents become model
context. The retrieval layer needs access checks, tenant filters, source
allowlists, and logging. The generation layer still needs output checks and
human review for high-risk use cases. Use
[Security]({{ '/wiki/security/' | relative_url }}) and
[Responsible AI and Governance]({{ '/wiki/responsible-ai-and-governance/' | relative_url }})
for the wider controls around data access, review, and accountability.

## Graph And Vector Variants

Vector RAG retrieves similar chunks, while graph RAG retrieves entities and
relationships. It can also retrieve paths or structured facts.
[Anahita Pakiman]({{ '/people/anahitapakiman/' | relative_url }})
draws this boundary in
[Knowledge Graphs and LLMs for Automotive R&D]({{ '/podcasts/knowledge-graphs-and-llms-for-automotive-rnd/' | relative_url }}).
At 38:10, she contrasts chunks in a vector database with knowledge graph
semantics. At 39:56, she discusses prompt templates and Cypher-style retrieval.

This distinction matters when the relationship is part of the answer. Similar
text chunks can help with fuzzy recall. Graph retrieval can preserve chapter
order, parent-child links, simulation relationships, and domain semantics.
Anahita also warns at 42:42 that LLM-extracted graph knowledge still needs
verification, so teams still have to construct and validate the graph.

Use [Graph RAG vs Vector RAG]({{ '/comparisons/graph-rag-vs-vector-rag/' | relative_url }})
and [Knowledge Graph vs Vector Search]({{ '/comparisons/knowledge-graph-vs-vector-search/' | relative_url }})
when the model may need similar passages or structured relationships. Those
pages also cover designs that use both.

## Boundaries With Other Patterns

RAG isn't the answer to every LLM problem, and Meryem's production episode draws
the boundary with fine-tuning. Retrieval fits changing knowledge and grounded
answers, while fine-tuning fits style and tone. It also fits domain adaptation
and repeated task behavior
([Deploying LLMs in Production]({{ '/podcasts/deploying-llms-in-production-fine-tuning-retrieval-open-source-api/' | relative_url }}),
26:30-31:38 and 40:46-46:42). Use
[RAG vs Fine-Tuning]({{ '/comparisons/rag-vs-fine-tuning/' | relative_url }}) for that
comparison.

Long context also doesn't make RAG disappear. [Lavanya Gupta]({{ '/people/lavanyagupta/' | relative_url }})
discusses long-context model evaluation in
[Applied LLM Research and Career Growth]({{ '/podcasts/applied-llm-research-and-career-growth-in-practice/' | relative_url }}).
At 12:36-14:54, she describes performance drops in long financial contexts and
keeps chunking, retrieval, and summarization in the practical toolkit. Ranjitha
adds the production reason at 29:30-30:27 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}),
where large prompts still add latency, cost, and noise.

Agents are the next design choice when retrieval isn't enough.

At 49:21-50:19 in
[Practical LLM Engineering and RAG]({{ '/podcasts/practical-llm-engineering-and-rag/' | relative_url }}),
Hugo says that broad corpus summaries may need a summarization tool. Ordinary
RAG looks for individual chunks.

Ranjitha makes the stronger agent boundary at
36:11-38:59 in
[Building Agentic AI Systems]({{ '/podcasts/building-agentic-ai-engineering-tooling-retrieval-evaluation/' | relative_url }}):
RAG fits a simple question over a large search space. Agents fit dynamic
planning and multiple data sources. They also fit tool calls and API
integrations.

For interview-style system design, the same tradeoffs appear in
[LLM System Design Interview]({{ '/guides/llm-system-design-interview/' | relative_url }}):
first name the user task and source of truth. Then choose the repair path based
on the system failure. That may be retrieval or fine-tuning. It may also be long
context, tools, or agents.
