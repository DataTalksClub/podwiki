---
title: "RAG with Vector Search — LLM Zoomcamp Module 2"
summary: "--- video_url: 'https://www.youtube.com/watch?v=-GBW3g3PVTM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # RAG with Vector Search"
related_course:
  - llmz-module-02
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 2: Vector Search](/course-wiki/llmz-module-02/) › RAG with Vector Search

## Notes

---
video_url: "https://www.youtube.com/watch?v=-GBW3g3PVTM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# RAG with Vector Search

In module 1, we built a RAG pipeline with three steps:

```python
def rag(question):
    search_results = search(question)
    user_prompt = build_prompt(question, search_results)
    return llm(user_prompt)
```

The search step used keyword search. Now we swap in vector search.
Because RAG is modular, search is the only step we touch. Build prompt
and the LLM call stay exactly as they were.

## Using RAGBase

In module 1 we put all the RAG logic into a
`RAGBase` helper class. It
has `search`, `build_prompt`, and `llm` methods, so we only need to
override `search`.

Download `rag_helper.py` (and `ingest.py` if you didn't get it earlier)
into your project:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/01-agentic-rag/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/01-agentic-rag/code/ingest.py
```

First, create the OpenAI client:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Next, download and index the data:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Then use the `RAGBase` class:

```python
from rag_helper import RAGBase

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)
```

Ask it a question:

```python
query = "I just found out about the program, can I still sign up?"
assistant.rag(query)
```

This still uses keyword search. Text search isn't bad here, so the
answer may already look right. Next we replace search with vector
search.

We already have:

- All the indexed documents `documents`
- The embeddings matrix `X` with all these documents
- The vector search engine `vindex`

We can't pass `vindex` to RAG as-is. Text search takes the query string
directly, but vector search needs the query as a vector first. So we
subclass `RAGBase` and override `search` to encode the query before
searching.

The subclass overrides `search`:

```python

class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        super().__init__(**kwargs)
        self.embedder = embedder

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        filter_dict = {"course": self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )
```

The `__init__` method adds one extra argument, `embedder`, for the
sentence transformer. Inside `search` we use it to turn the query into a
vector. Then we query `vindex` with that vector instead of the raw text.
Everything else is inherited from `RAGBase`.

## Using it

Let's init it:

```python
vector_assistant = RAGVector(
    embedder=model,
    index=vindex,
    llm_client=openai_client,
)
```

Try it with different queries:

```python
vector_assistant.rag("the program has already begun, can I still sign up?")
```

The answers should be close to what we got with keyword search, but
vector search handles rephrased questions better. The swap was trivial
because RAG has three clear steps. The same trick lets us change the LLM
provider later by overriding just the `llm` step.

## Key concepts

- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)

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
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-2](/course-wiki/llmz-m02-vector-search-2/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
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

- [Video](https://www.youtube.com/watch?v=-GBW3g3PVTM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/02-vector-search/06-rag-vector.md)
