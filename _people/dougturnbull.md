---
layout: "person"
title: "Doug Turnbull"
summary: "Search relevance practitioner connected to DataTalks.Club discussions of search quality, ranking, and retrieval evaluation."
source_url: "https://datatalks.club/people/dougturnbull.html"
podcast_episodes: []
expertise: ["search relevance", "information retrieval", "learning to rank", "Elasticsearch", "product search"]
curated: "true"
github: "softwaredoug"
twitter: "softwaredoug"
linkedin: "softwaredoug"
web: "https://softwaredoug.com/"
---

# Doug Turnbull

Doug Turnbull is a search relevance practitioner known for Relevant Search and
his public writing as `softwaredoug`. DataTalks.Club hasn't published a local
podcast interview with Doug. The strongest podcast connection is that
[Atita Arora]({{ '/people/atitaarora/' | relative_url }}) recommends Relevant
Search in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
at 58:01. The same exchange notes Doug's prior DataTalks.Club talk at 58:51.

The surrounding podcast treatment runs through
[Search]({{ '/wiki/search/' | relative_url }}),
[Search Relevance]({{ '/wiki/search-relevance/' | relative_url }}), and
[Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }}).

## Search Relevance As Product Judgment

Atita's episode explains why Doug's relevance work belongs in the search
curriculum. Around 11:29-13:33 in
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }}),
she describes work at Lucidworks and OpenSource Connections. That work taught
her that good search needs a measurable definition tied to business KPIs. At
58:01, she recommends Relevant Search because it teaches the thought process behind
relevance, not only a tool recipe.

That podcast thread matches the working model in
[Search Relevance]({{ '/wiki/search-relevance/' | relative_url }}). Relevance
isn't just semantic similarity or keyword overlap. It's the product judgment
that decides which candidates should be retrieved and ranked. It also decides
which result quality can be defended with
[metrics]({{ '/wiki/metrics/' | relative_url }}). That measurement layer leads
to [A/B testing]({{ '/wiki/a-b-testing/' | relative_url }}) and
[production search evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }}).

## Classical Search Still Matters In Vector Systems

The same
[Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
discussion starts from Solr and Lucene before moving into vector databases. It
also covers Elasticsearch and OpenSearch. At 17:01-20:27, Atita frames vector
adoption as a use-case decision. Teams can add vector retrieval to an existing
search stack. They can also use a standalone vector database or combine the two.

Doug's relevance context is useful here because classical search work doesn't
disappear when teams adopt embeddings. Mature search systems still own query
analysis and filters. They also own exact-match behavior, ranking signals, and
operational debugging. Use
[Vector Search vs Keyword Search]({{ '/comparisons/vector-search-vs-keyword-search/' | relative_url }})
for the retrieval-method tradeoff and
[Vector Database vs Search Engine]({{ '/comparisons/vector-database-vs-search-engine/' | relative_url }})
for the infrastructure boundary.

## Evaluation Makes Search Defensible

Atita's RAG section at 30:38-48:09 keeps returning to evaluation. In a real
system, teams need separate checks for retrieval quality and generated-answer
quality. They also need citation checks, offline tests, human review, and
business KPIs
([Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})).
That's the same reason Doug's search-relevance work remains relevant to LLM
and RAG products. A search product needs judgments, test cases, and product
metrics before a team can say whether results improved.

For implementation-oriented follow-up, use
[RAG Evaluation Workflow]({{ '/how-tos/rag-evaluation-workflow/' | relative_url }})
for measurement steps. Use
[Search, RAG, and Knowledge Systems]({{ '/wiki/search-rag-and-knowledge-systems/' | relative_url }})
and [Search and RAG Project Checklist]({{ '/wiki/search-and-rag-project-checklist/' | relative_url }})
for architecture and build sequencing.
For a production-search companion to Atita's episode,
[Daniel Svonava]({{ '/people/danielsvonava/' | relative_url }}) covers
candidate generation and ranking in
[Building Search Systems]({{ '/podcasts/building-production-search-systems/' | relative_url }}).
He also covers hybrid search, vector infrastructure, and business metrics.

## Search Product Design

Doug's DataTalks.Club-facing role fits a broader search product design path:

- [Modern Search Systems]({{ '/podcasts/modern-search-systems-vector-databases-llms-semantic-retrieval/' | relative_url }})
  references Relevant Search as a learning resource after discussing Lucene,
  vector databases, RAG, and evaluation.
- [Search Relevance]({{ '/wiki/search-relevance/' | relative_url }}) turns that
  resource recommendation into a product question. The team has to define good
  results for the product it's building.
- [Production Search Evaluation]({{ '/wiki/production-search-evaluation/' | relative_url }})
  gives the measurement layer for relevance labels and offline tests. It also
  covers online experiments, monitoring, and feedback loops.
- [Search]({{ '/wiki/search/' | relative_url }}) and
  [Information Retrieval]({{ '/wiki/information-retrieval/' | relative_url }})
  provide the broader retrieval and ranking vocabulary.
