---
title: "Embeddings — LLM Zoomcamp Module 2"
summary: "--- video_url: 'https://www.youtube.com/watch?v=kJOlW1HeMp4&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Embeddings"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Embeddings

## Notes

---
video_url: "https://www.youtube.com/watch?v=kJOlW1HeMp4&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Embeddings

Before we can do vector search, we need to turn our text into vectors.
We call this process embedding: we embed text into a vector space. The
vectors we get back are also called "embeddings."

## Word embeddings and sentence embeddings

This idea comes from
[word2vec](https://en.wikipedia.org/wiki/Word2vec). The model learns to
place words as points in a multi-dimensional space. Words with similar
meanings land close to each other.

Imagine a 2D space where "enroll" and "join" are near each other and
"Docker" is far away:

```text
        · enroll
       · join
                   · Docker
```

The same idea works for entire sentences:

```text
Q1: "I just discovered the course. Can I still join it?"
Q2: "I just found out about the program. Can I still enroll?"

These two are close - they mean the same thing.

Q3: "How do I run Docker on Windows?"

This one is far away from Q1 and Q2.
```

Now imagine all 1200 documents in our FAQ dataset. Each one becomes a
point in this space. When a user asks a question, we embed it into the
same space and find the closest documents. Those nearest neighbors are
our search results.

The model encodes the whole sentence, not the words in isolation. So it
can tell apart the same word in different contexts.

Take the word "judge." In "the judge ruled out the possibility of crime"
(legal) it gets one vector. In "LLM-as-a-judge approach to evaluate
LLMs" (ML evaluation) it gets a different one. The surrounding context
changes the embedding.

So an embedding model takes text in and returns a fixed-length array of
numbers. We train it so that texts with similar meanings get similar
vectors.

We'll use [sentence-transformers](https://www.sbert.net/), a popular
open-source library for embeddings. It runs locally on your machine, so
there are no API costs.

## Install sentence-transformers

Recent versions of sentence-transformers install the GPU-enabled PyTorch package, which pulls large NVIDIA CUDA libraries.
It takes a few gigabytes of disk space, even if you don't have a GPU.

To avoid this, you need to explicitly tell uv to install the CPU-only PyTorch wheels.

Add a CPU-only PyTorch index to `pyproject.toml`:

```toml
[tool.uv.sources]
torch = { index = "pytorch-cpu" }

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
```

Install the library:

```bash
uv add sentence-transformers
```

If your pyproject.toml already specifies the requests package, make sure it is pinned to requests>=2.28.1, because pytorch-cpu requires this version to install correctly.

In this way, uv will automatically resolve PyTorch using the CPU-only index.

We will also see how to trim it down even more for using in production in the ONNX Embedder lesson later.

## Choosing a model

Sentence-transformers supports many models. The right one depends on
your task, your language, and the resources you have. Larger models are
usually slower, so for our FAQ dataset of short English texts a small
model is enough. Try a few on your own data and keep the one that works
best.

We'll use `all-MiniLM-L6-v2`:

- 384-dimensional vectors (compact)
- Fast on CPU
- Good quality for general English text
- Uses cosine similarity (we'll explain this below)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
```

The first time you run this, it downloads the model (~80 MB) and the
tokenizer from HuggingFace. The tokenizer turns text into something the
model can read. After that, both load from a local cache.

## Trying it with simple examples

Let's see how embeddings work on a few examples.

We'll start with a query:

```python
q1 = "Can I still join the course after the start date?"
v1 = model.encode(q1)
```

`v1` is a vector, an array of 384 numbers. Each number stands for some
concept the model learned. We can't read off what a

## Key concepts

- [Docker](/course-wiki/docker/)
- [PyTorch](/course-wiki/pytorch/)
- [Vector Search](/course-wiki/vector-search/)
- [Embeddings](/course-wiki/embeddings/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
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
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
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

- [Video](https://www.youtube.com/watch?v=kJOlW1HeMp4&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/02-embeddings.md)
