---
title: "Generating RAG Answers — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=utkcclfpj0g&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Generating RAG Answers"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Generating RAG Answers

## Notes

---
video_url: "https://www.youtube.com/watch?v=utkcclfpj0g&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Generating RAG Answers

In the first part of this module, we evaluated search quality. We
checked whether the right document appeared in the search results.

Now we evaluate the full RAG pipeline. For each generated question, we
run RAG and save the answer produced by the LLM. Later, we'll compare
this answer with the original FAQ answer.

This is the A->Q->A' setup:

- A = original answer in the FAQ
- Q = generated question from this answer
- A' = answer produced by our RAG system

If A' is close to A, the RAG system is doing a good job.

This is still offline evaluation. We can compare A and A' because our
questions came from FAQ records. For each question, we know which
original answer it came from.

## Loading the data

Create a new notebook for RAG evaluation.

Load the ground truth questions:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground_truth-new.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Load the FAQ documents and the search index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()

documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

documents = documents_llm
index = build_index(documents)
```

Create a lookup table for the original FAQ documents:

```python
doc_idx = {}

for doc in documents:
    doc_idx[doc["id"]] = doc
```

We'll use this lookup table to find the original answer for each
ground truth question.

## Running RAG

Import the usual things first:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

For this lesson, use `RAGWithUsage` from the evaluation utilities. It
subclasses `RAGBase` from module 01, so it has the same `rag` method.

It stores token usage after each LLM call. Then we can calculate the
total cost later.

It also uses the search boosts we selected in the search tuning lesson:
`question=1.0`, `answer=2.0`, and `section=0.1`.

```python
from evaluation_utils import RAGWithUsage

assistant = RAGWithUsage(
    index=index,
    llm_client=openai_client,
)
```

For each question, `RAGBase` searches the FAQ, builds a prompt with the
retrieved context, and asks the LLM to answer. We save the answer so the
next lesson can judge it.

Run RAG for one question:

```python
rec = ground_truth[0]
question = rec["question"]

answer_llm = assistant.rag(question)
answer_llm
```

Check the cost of this call:

```python
assistant.total_cost()
```

Get the original answer from the document ID:

```python
doc_id = rec["document"]
original_doc = doc_idx[doc_id]
answer_orig = original_doc["answer"]

answer_orig
```

Now save both answers in one record:

```python
rag_result = {
    "question": question,
    "answer_llm": answer_llm,
    "answer_orig": answer_orig,
    "document": doc_id,
}

rag_result
```

## Processing all questions

Create a function that processes one ground truth record:

```python
def generate_rag_answer(rec):
    question = rec["question"]
    doc_id = rec["document"]
    original_doc = doc_idx[doc_id]

    answer_llm = assistant.rag(question)
    answer_orig = original_doc["answer"]

    result = {
        "question": question,
        "answer_llm": answer_llm,
        "answer_orig": answer_orig,
        "document": doc_id,
    }

    return result
```

Test it on one record:

```python
answer_record = generate_rag_answer(ground_truth[0])
answer_record
```

Before running the full batch, reset the usage we collected while
testing:

```python
assistant.reset_usage()
```

This calls the LLM once per ground truth question, so it can take some
time. Let's process the questions in parallel and track progress.

Import the parallel processing helper from the same utility file:

```python
from concurrent.futures import ThreadPoolExecutor
from evaluation_utils import map_progress
`

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
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=utkcclfpj0g&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/12-rag-answers.md)
