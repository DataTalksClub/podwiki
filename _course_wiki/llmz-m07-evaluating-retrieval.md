---
title: "Evaluating Retrieval — LLM Zoomcamp Module 7"
summary: "<a href='https://www.youtube.com/watch?v=6ulnHtJPCWY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R'>"
related_course:
  - llmz-module-07
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 7: End-to-End Project](/course-wiki/llmz-module-07/) › Evaluating Retrieval

## Notes

# Evaluating Retrieval

<a href="https://www.youtube.com/watch?v=6ulnHtJPCWY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  
</a>

Now that we have a dataset and a basic RAG flow, we need to
evaluate how well the retrieval works. We use the same approach
from module 04: generate ground truth data and measure Hit Rate
and MRR.

## Problem description and README

First, write a clear README that describes the problem, the data,
and how to run the project.

A good README should include:

- What the project does
- The dataset used
- How to install dependencies (`uv sync`)
- How to run the application
- How to run the Jupyter notebook

You can use ChatGPT to help draft the README. Give it your project
criteria, describe your dataset, and ask it to write a problem
description. Then edit the result to make it concise.

## Generating ground truth data

We need questions with known relevant documents.

We generate these
with an LLM, asking it to create questions for each exercise:

```python
prompt1_template = """
You are a fitness expert generating evaluation questions.
For the exercise below, generate 2 questions that a user might ask.
Return the result as a JSON array with objects containing 'id' and 'question' fields.

Exercise: {exercise_name}
Activity type: {type_of_activity}
Equipment: {type_of_equipment}
Body part: {body_part}
Muscle groups: {muscle_groups_activated}
Instructions: {instructions}
""".strip()

from tqdm.auto import tqdm
import json

df = pd.read_csv("data/data.csv")

results = []

for _, row in tqdm(df.iterrows(), total=len(df)):
    prompt = prompt1_template.format(**row.to_dict())
    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=[{"role": "user", "content": prompt}]
    )
    questions = json.loads(response.output_text)
    for q in questions:
        q["id"] = row["id"]
        results.append(q)

df_questions = pd.DataFrame(results)
df_questions.to_csv("data/ground-truth-retrieval.csv", index=False)
```

Load the ground truth:

```python
df_question = pd.read_csv("data/ground-truth-retrieval.csv")
ground_truth = df_question.to_dict(orient="records")
```

## Evaluating retrieval quality

We use the same Hit Rate and MRR metrics from module 04:

```python
def hit_rate(relevance_total):
    cnt = 0
    for line in relevance_total:
        if True in line:
            cnt += 1
    return cnt / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0
    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank]:
                total_score += 1 / (rank + 1)
                break
    return total_score / len(relevance_total)

def evaluate(ground_truth, search_function):
    relevance_total = []
    for q in tqdm(ground_truth):
        doc_id = q["id"]
        results = search_function(q)
        relevance = [d["id"] == doc_id for d in results]
        relevance_total.append(relevance)
    return {
        "hit_rate": hit_rate(relevance_total),
        "mrr": mrr(relevance_total)
    }
```

Evaluate the default search (no boosting):

```python
evaluate(ground_truth, lambda q: search(q["question"]))
```

## Finding the best boost parameters

We can optimize the boost values for each field using random
search.

Split the ground truth into validation and test sets:

```python
df_validation = df_question[:100]
df_test = df_question[100:]

gt_val = df_validation.to_dict(orient="records")
gt_test = df_test.to_dict(orient="records")
```

Define the search function with configurable boost:

```python
def minsearch_search(query, boost=None):
    if boost is None:
        boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )
    return results
```

Random search over boost values:

```python
import random

def simple_optimize(param_ranges, objective_function, n_iterations=10):
    best_params = None
    best_score = float("-inf")

    for _ in range(n_itera

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [RAG](/course-wiki/rag/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Pandas](/course-wiki/pandas/)
- [Prompt Engineering](/course-wiki/prompt-engineering/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
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
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
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
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-ai-copilot](/course-wiki/llmz-m03-ai-copilot/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-context-engineering](/course-wiki/llmz-m03-context-engineering/)
- [llmz-m03-multi-agent-systems](/course-wiki/llmz-m03-multi-agent-systems/)
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
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-hybrid-search-with-langchain](/course-wiki/llmz-m06-hybrid-search-with-langchain/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=6ulnHtJPCWY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/07-project-example/02-evaluating-retrieval.md)
