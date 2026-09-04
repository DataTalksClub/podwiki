---
title: "Using ONNX Runtime instead of PyTorch — LLM Zoomcamp Module 2"
summary: "---
video_url: "https://www.youtube.com/watch?v=BMqa4OsCk58&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Using ONNX Runtime instead of PyTorch"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › Using ONNX Runtime instead of PyTorch

## Notes

---
video_url: "https://www.youtube.com/watch?v=BMqa4OsCk58&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Using ONNX Runtime instead of PyTorch

When you move to production, you want to cut overhead, both the
dependencies and the size of your deployment. sentence-transformers
drags in PyTorch plus a pile of Nvidia libraries, which is a lot. ONNX
Runtime serves the same model without that weight.

To put a number on it, I created two empty projects. In one I ran `uv
add sentence-transformers`, in the other I set up ONNX Runtime.

Then I measured the virtual environment sizes:

- sentence-transformers: 4.8 GB, 58 packages
- ONNX Runtime: 147 MB, 27 packages

That's 33x smaller for the same embeddings and the same results. Often
we don't even convert the model ourselves. Someone has usually published
an ONNX version we can download.

For development and experiments, sentence-transformers is fine. For
production you want the lighter option.

Let's create a separate project for this lesson:

```bash
mkdir llm-zoomcamp-onnx && cd llm-zoomcamp-onnx
uv init --no-workspace
uv add onnxruntime tokenizers numpy tqdm minsearch
uv add --dev huggingface-hub jupyter
```

`huggingface-hub` is only needed to download the model. At runtime we'll need `onnxruntime`, `tokenizers`, and `numpy`.

Then register a kernel for this project:

```bash
uv run python -m ipykernel install --user --name llm-zoomcamp-onnx --display-name "llm-zoomcamp-onnx"
```

## Downloading the model

We'll use the [download.py](embed/download.py) script from the
`embed/` directory to fetch the ONNX model from HuggingFace.

Copy it to your project, then run:

```bash
uv run python download.py
```

This creates:

```text
models/
  Xenova/
    all-MiniLM-L6-v2/
      tokenizer.json
      model.onnx
```

You only run this once. After that, the model files are local.

Add the models directory to `.gitignore`:

```text
models/
```

## The Embedder class

We'll use the [embedder.py](embed/embedder.py) script from the
`embed/` directory for generating embeddings.

Copy it to your project as well.

Under the hood, it does four things:

1. Tokenize - convert text into integer IDs and attention masks
2. Run ONNX model - execute the model graph on CPU
3. Mean pooling - average the token embeddings, weighted by the
   attention mask
4. Normalize - divide by L2 norm so vectors can be compared with
   dot product

You don't need to follow every step inside `embedder.py`. It gives us
the same `encode` interface as before, with none of the PyTorch weight.

## Same pipeline, no PyTorch

Let's repeat the examples from earlier and confirm the numbers match.

First, comparing two queries against a document:

```python
from embedder import Embedder

embed = Embedder()

q1 = "Can I still join the course after the start date?"
q2 = "How to install Docker on Windows?"
d  = "You don't need to register. You're accepted. You can also just start learning and submitting homework without registering."

v1 = embed.encode(q1)
v2 = embed.encode(q2)
dv = embed.encode(d)
```

Compute similarities:

```python
v1.dot(dv)
```

And the second similarity:

```python
v2.dot(dv)
```

We get the same result as before. The first score is higher because
the query about joining the course is more similar to the document
about registration.

Next, we embed the FAQ dataset.

If you didn't fetch `ingest.py` earlier, grab it now:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/01-agentic-rag/code/ingest.py
```

Load the documents:

```python
from ingest import load_faq_data

documents = load_faq_data()
```

Combine question and answer for each document:

```python
texts = [doc["question"] + " " + doc["answer"] for doc in documents]
```

Embed in batches:

```python
from tqdm.auto import tqdm
import numpy as np

batch_size = 50
X = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = embed.encode_batch(batch)
    X.extend(ba

## Key concepts

- [Vector Search](/course-wiki/vector-search/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
- [llmz-m01-wrap-up-of-part-1](/course-wiki/llmz-m01-wrap-up-of-part-1/)
- [llmz-m02-embedding-our-dataset](/course-wiki/llmz-m02-embedding-our-dataset/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-rag-with-vector-search](/course-wiki/llmz-m02-rag-with-vector-search/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=BMqa4OsCk58&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/09-onnx-embedder.md)
