---
title: "Evaluating RAG — LLM Zoomcamp Module 7"
summary: "<a href='https://www.youtube.com/watch?v=lxpW2mR7dGk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R'>"
related_course:
  - llmz-module-07
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 7: End-to-End Project](/course-wiki/llmz-module-07/) › Evaluating RAG

## Notes

# Evaluating RAG

<a href="https://www.youtube.com/watch?v=lxpW2mR7dGk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  
</a>

Retrieval evaluation tells us if we're finding the right documents.
RAG evaluation tells us if the generated answers are actually good.
We use the LLM-as-a-judge approach from module 04.

## LLM-as-a-Judge for RAG

Since we don't have reference answers for every question, we use
the LLM to evaluate the relevance of generated answers:

```python
prompt2_template = """
You are an expert evaluator for a RAG system.
Your task is to analyze the relevance of the generated answer to the given question.
Based on the relevance of the generated answer, you will classify it
as 'NON_RELEVANT', 'PARTLY_RELEVANT', or 'RELEVANT'.

Here is the data for evaluation:

Question: {question}
Generated Answer: {answer_llm}

Please analyze the content and context of the generated answer in relation to the question
and provide your evaluation in parsable JSON without using code blocks:

{{
  'Relevance': 'NON_RELEVANT' | 'PARTLY_RELEVANT' | 'RELEVANT',
  'Explanation': '[Provide a brief explanation for your evaluation]'
}}
""".strip()
```

Take a sample of ground truth questions, generate answers, and
evaluate:

```python
import json
from tqdm.auto import tqdm

df_sample = df_question.sample(n=200, random_state=1)
sample = df_sample.to_dict(orient="records")

evaluations = []

for record in tqdm(sample):
    question = record["question"]
    answer_llm = rag(question)

    prompt = prompt2_template.format(
        question=question,
        answer_llm=answer_llm
    )

    evaluation = llm(prompt)
    evaluation = json.loads(evaluation)

    evaluations.append((record, answer_llm, evaluation))
```

Analyze the results:

```python
df_eval = pd.DataFrame(evaluations, columns=["record", "answer", "evaluation"])

df_eval["id"] = df_eval.record.apply(lambda d: d["id"])
df_eval["question"] = df_eval.record.apply(lambda d: d["question"])
df_eval["relevance"] = df_eval.evaluation.apply(lambda d: d["Relevance"])
df_eval["explanation"] = df_eval.evaluation.apply(lambda d: d["Explanation"])

df_eval.relevance.value_counts(normalize=True)
```

You'll see something like:

```text
RELEVANT          0.85
PARTLY_RELEVANT   0.12
NON_RELEVANT      0.03
```

Save the results:

```python
df_eval.to_csv("data/rag-eval-gpt-5.4-mini.csv", index=False)
```

## Comparing models

You can also use evaluation to compare different LLMs.

For example,
compare gpt-5.4-mini with gpt-4o:

```python
evaluations_gpt4o = []

for record in tqdm(sample):
    question = record["question"]
    answer_llm = rag(question, model="gpt-4o")

    prompt = prompt2_template.format(
        question=question,
        answer_llm=answer_llm
    )

    evaluation = llm(prompt)
    evaluation = json.loads(evaluation)

    evaluations_gpt4o.append((record, answer_llm, evaluation))

df_eval = pd.DataFrame(evaluations_gpt4o, columns=["record", "answer", "evaluation"])
df_eval["relevance"] = df_eval.evaluation.apply(lambda d: d["Relevance"])
df_eval.relevance.value_counts(normalize=True)

df_eval.to_csv("data/rag-eval-gpt-4o.csv", index=False)
```

This gives you a concrete way to decide if a more expensive model
is worth the cost. Typically, the cheaper model gives similar
results for most questions.

## Key concepts

- [RAG](/course-wiki/rag/)
- [Pandas](/course-wiki/pandas/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
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
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m02-vector-search-with-minsearch](/course-wiki/llmz-m02-vector-search-with-minsearch/)
- [llmz-m02-vector-search-with-pgvector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-next-steps](/course-wiki/llmz-m03-next-steps/)
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
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m06-next-steps](/course-wiki/llmz-m06-next-steps/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=lxpW2mR7dGk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/07-project-example/03-evaluating-rag.md)
