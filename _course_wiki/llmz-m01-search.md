---
title: "Search — LLM Zoomcamp Module 1"
summary: "--- video_url: 'https://www.youtube.com/watch?v=GYgpNKiuCJU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' code: - label: 'notebook.ipynb' path: 'code/notebook.ipynb' --- # Search"
related_course:
  - llmz-module-01
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 1: Agentic RAG](/course-wiki/llmz-module-01/) › Search

## Notes

---
video_url: "https://www.youtube.com/watch?v=GYgpNKiuCJU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
code:
  - label: "notebook.ipynb"
    path: "code/notebook.ipynb"
---
# Search

## Search basics

At its core, every search engine does the same thing. It takes a query,
scores every document for similarity, and returns the top results.

Formally, there is a similarity function:

```python
score = sim(query, document)
```

For each document in the database, you compute this score. Then you
rank all documents by score and return the top N. What makes a search
engine different from another search engine is what `sim` actually
computes.

- text/lexical search (covered in this section): `sim` counts how
  many words the query and the document share. It looks at the surface
  form, the actual words, and matches them exactly.

- vector/semantic search (covered in module 2):
  `sim` compares the meaning of the query and the document. Same
  function, different similarity measure.

Consider these two questions:

- "Can I still join the course after the start date?"
- "Is it possible to enroll late?"

They mean the same thing, but share almost no keywords. "Join" is not
"enroll", "course" is absent, "start date" is not "late". A text search
engine would struggle to match them, because it only sees words.

We'll see how vector search solves this later. For now, let's build text
search with minsearch.

## Indexing with minsearch

We already have the `documents` list from the previous section. Now
let's index it.

Searching matters because we have around 1100 documents. Sending all
of them to the LLM would be expensive and slow. The model would get
confused with too much data. Search finds the most relevant documents
to send instead.

There are many search libraries you can use - Apache Lucene,
Elasticsearch, Solr, and others. But these are somewhat heavy. For
example, to run Elasticsearch, you need to start a Docker container.

[minsearch](https://github.com/alexeygrigorev/minsearch) is a simple
in-memory search engine. It's lightweight, so it runs anywhere Python
runs, including Google Colab where you can't start a Docker container.
It's a toy implementation, not production ready, but it illustrates how
search engines work and it gives good results.

I should add a disclaimer: I wrote this library and I maintain it. It
started as a single Python file in the first edition of LLM Zoomcamp. I
wanted to show that keyword search isn't magic. We wrote it together as
part of the [Build a Search Engine](https://www.youtube.com/watch?v=nMrGK5QgPVE) workshop
(see the [code](https://github.com/alexeygrigorev/build-your-own-search-engine)).

It turned out useful beyond teaching. After two years across many
projects, it's pretty reliable for small datasets.

The concepts in minsearch are the same as in Elasticsearch (which
comes from Lucene): text fields, keyword fields, boosting, filtering. I
borrowed those terms from Elasticsearch on purpose, since I wanted a
lightweight stand-in for it. So what you learn here transfers directly.

We'll index the `question`, `section`, and `answer` fields as text
(they'll be tokenized and ranked), and the `course` field as a
keyword (for filtering).

The index tokenizes text fields and treats keyword fields as exact strings.

Text fields are the fields you search through. When you type a query,
the search engine looks at these fields and tokenizes them. It splits
text into words, lowercases them, removes stop words, and ranks the
results by relevance. So `question`, `section`, and `answer` are text
fields.

Keyword fields are for exact matching. Think of a SQL query like
`SELECT * FROM index WHERE course = 'data-engineering-zoomcamp'`. The
results must come from the specified course, no matter what ranking or
boosting you do for text fields.

You use keyword fields to restrict the search space to a particular
subset. In our case, we have four courses. Say you're taking the LLM
course and ask a question. You don't w

## Key concepts

- [RAG](/course-wiki/rag/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Docker](/course-wiki/docker/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)
- [scikit-learn](/course-wiki/scikit-learn/)
- [Elasticsearch](/course-wiki/elasticsearch/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-toyaikit](/course-wiki/llmz-m01-toyaikit/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m03-setting-up-kestra](/course-wiki/llmz-m03-setting-up-kestra/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=GYgpNKiuCJU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/01-agentic-rag/05-search.md)
