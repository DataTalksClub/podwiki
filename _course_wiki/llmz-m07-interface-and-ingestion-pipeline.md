---
title: "Interface and Ingestion Pipeline — LLM Zoomcamp Module 7"
summary: "<a href='https://www.youtube.com/watch?v=vMHve2EyA5M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R'>"
related_course:
  - llmz-module-07
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 7: End-to-End Project](/course-wiki/llmz-module-07/) › Interface and Ingestion Pipeline

## Notes

# Interface and Ingestion Pipeline

<a href="https://www.youtube.com/watch?v=vMHve2EyA5M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  
</a>

So far we've been working in notebooks. Now we turn the notebook
into a proper application with an ingestion pipeline and a web API.

## From notebook to scripts

Convert the notebook to Python:

```bash
jupyter nbconvert --to=script rag-test.ipynb
```

Then organize the code into a package structure:

```text
fitness_assistant/
    __init__.py
    rag.py          # RAG flow + search + LLM
    ingest.py       # Load data into search index
    minsearch.py    # (installed via uv add minsearch instead)
app.py              # Flask API
db.py               # Database functions (added later)
```

Since we're using `minsearch` as a package (installed with
`uv add minsearch`), we don't need to copy `minsearch.py`.

## Ingestion

The ingestion script loads the CSV and builds the search index.

Since minsearch is in-memory, ingestion happens when the app
starts:

```python
import os
import pandas as pd
from minsearch import Index

DATA_PATH = os.getenv("DATA_PATH", "data/data.csv")

def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    documents = df.to_dict(orient="records")

    index = Index(
        text_fields=[
            "exercise_name",
            "type_of_activity",
            "type_of_equipment",
            "body_part",
            "type",
            "muscle_groups_activated",
            "instructions",
        ],
        keyword_fields=["id"],
    )

    index.fit(documents)
    return index
```

If you use a real database like Elasticsearch, ingestion would be
a separate step that indexes documents into the database.

## RAG module

The RAG module imports the index and provides the `rag` function:

```python
import json
from time import time
from openai import OpenAI
import ingest

openai_client = OpenAI()
index = ingest.load_index()

def search(query):
    boost = {
        "exercise_name": 2.11,
        "type_of_activity": 1.46,
        "type_of_equipment": 0.65,
        "body_part": 2.65,
        "type": 1.31,
        "muscle_groups_activated": 2.54,
        "instructions": 0.74
    }

    results = index.search(
        query=query, filter_dict={}, boost_dict=boost, num_results=10
    )
    return results
```

Define the prompt templates and the prompt builder:

```python
prompt_template = """
You're a fitness instructor. Answer the QUESTION based on the CONTEXT from our exercises database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

entry_template = """
exercise_name: {exercise_name}
type_of_activity: {type_of_activity}
type_of_equipment: {type_of_equipment}
body_part: {body_part}
type: {type}
muscle_groups_activated: {muscle_groups_activated}
instructions: {instructions}
""".strip()

def build_prompt(query, search_results):
    context = ""
    for doc in search_results:
        context = context + entry_template.format(**doc) + "\n\n"
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt
```

Add the LLM call and the full RAG function:

```python
def llm(prompt, model="gpt-5.4-mini"):
    response = openai_client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}]
    )
    answer = response.output_text
    token_stats = {
        "prompt_tokens": response.usage.input_tokens,
        "completion_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    return answer, token_stats

def rag(query, model="gpt-5.4-mini"):
    t0 = time()
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer, token_stats = llm(prompt, model=model)
    took = time() - t0

    return {
        "answer": answer,
        "model_used": model,
        "response_time": took,
        "prompt_tokens": token_stats["prompt_tokens"],
        "completion_

## Key concepts

- [RAG](/course-wiki/rag/)
- [Vector Search](/course-wiki/vector-search/)
- [Pandas](/course-wiki/pandas/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-introduction](/course-wiki/llmz-m01-introduction/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-course-faq-dataset](/course-wiki/llmz-m01-the-course-faq-dataset/)
- [llmz-m01-the-llm](/course-wiki/llmz-m01-the-llm/)
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
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
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
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-hybrid-search](/course-wiki/llmz-m06-hybrid-search/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=vMHve2EyA5M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/07-project-example/04-interface.md)
