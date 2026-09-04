---
title: "End-to-End Project Example — LLM Zoomcamp Module 7"
summary: "<a href="https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">"
related_course:
  - llmz-module-07
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 7: End-to-End Project](/course-wiki/llmz-module-07/) › End-to-End Project Example

## Notes

# End-to-End Project Example

<a href="https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  
</a>

In this module, we build a complete RAG project from scratch. The
project is a fitness assistant that helps users with exercise questions.

The final project is at
[alexeygrigorev/fitness-assistant](https://github.com/alexeygrigorev/fitness-assistant)
on GitHub. Check the final result - it's been polished beyond what
we show in the videos.

## Project overview

A RAG application that:

- Uses a dataset of exercises with muscle groups, equipment, and
  instructions
- Answers questions about exercises, replacements, and proper form
- Has a search component, an LLM component, and evaluation
- Includes an API interface (Flask)
- Has monitoring with PostgreSQL and Grafana
- Is containerized with Docker

## Setting up the project

Create a new project with uv:

```bash
mkdir fitness-assistant
cd fitness-assistant
uv init
uv add openai minsearch requests python-dotenv jupyter pandas scikit-learn tqdm
rm main.py
```

Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=sk-...
```

Add `.env` to `.gitignore`:

```gitignore
.env
```

Start Jupyter:

```bash
uv run jupyter notebook
```

## Generating the dataset

Since we don't have a real fitness FAQ database, we generate one
with an LLM. We use structured output (from module 04) to make
sure the data comes back in the right format.

First, define a Pydantic model for a single exercise:

```python
from pydantic import BaseModel, Field
from typing import List

class Exercise(BaseModel):
    id: str = Field(description="Unique identifier, e.g. 'push-up-001'")
    exercise_name: str = Field(description="Name of the exercise")
    type_of_activity: str = Field(description="Strength, Cardio, Flexibility, etc.")
    type_of_equipment: str = Field(description="Dumbbells, Barbell, None (bodyweight), etc.")
    body_part: str = Field(description="Chest, Back, Legs, etc.")
    type: str = Field(description="Compound, Isolation, etc.")
    muscle_groups_activated: str = Field(description="Comma-separated list, e.g. 'Chest, Triceps, Shoulders'")
    instructions: str = Field(description="Detailed step-by-step instructions")

class ExerciseDataset(BaseModel):
    exercises: List[Exercise]
```

Now generate the data using `responses.parse`:

```python
from openai import OpenAI
import pandas as pd

openai_client = OpenAI()

prompt = """
Generate a dataset of 50 diverse fitness exercises.
Cover different muscle groups, equipment types, and difficulty levels.
Include bodyweight exercises, free weights, and machine exercises.
""".strip()

response = openai_client.responses.parse(
    model="gpt-5.4-mini",
    input=[{"role": "user", "content": prompt}],
    text_format=ExerciseDataset,
)

dataset = response.output_parsed
df = pd.DataFrame([ex.model_dump() for ex in dataset.exercises])
df.to_csv("data/data.csv", index=False)
print(f"Generated {len(df)} exercises")
```

You may need to run this multiple times with different prompts
to cover enough exercises. Append all results to `data/data.csv`.

## The RAG flow

Build the basic RAG flow in a notebook.

First, load the data and
create a search index:

```python
import pandas as pd
from minsearch import Index

df = pd.read_csv("data/data.csv")
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
    keyword_fields=["id"]
)

index.fit(documents)
```

Search function:

```python
def search(query):
    boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results
```

Build the prompt:

```python
prompt_template = """
You're a fitness instructor. Answer the QUESTION based on the CONTEXT from our exercises databa

## Key concepts

- [Vector Search](/course-wiki/vector-search/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
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
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
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
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
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
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/07-project-example/01-intro.md)
