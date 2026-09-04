---
title: "Generating Ground Truth Data — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=YScoH28cVf8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Generating Ground Truth Data"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Generating Ground Truth Data

## Notes

---
video_url: "https://www.youtube.com/watch?v=YScoH28cVf8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Generating Ground Truth Data

To evaluate search, we need a dataset of queries where we know which
document is the correct answer. This is called ground truth (or gold
standard) data.

For each query in our ground truth dataset, we know which document in
the knowledge base is relevant. When we run a search, we check whether
the results include the correct document.

There are several ways to get ground truth data:

- Human annotators look at documents and write queries (best quality, expensive)
- Collect real user queries and label them (requires a running system)
- Generate synthetic data with an LLM (what we'll do)

We don't have a production system yet, so we'll use an LLM to generate
questions. For each FAQ document, we ask the LLM to create 5 questions
that this document would answer. Then we know that for each generated
question, the source document is the correct answer.

## Loading the documents

We'll use helper files from module 01 and this module.

If you don't have them in your notebook directory, download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/cohorts/2026/01-agentic-rag/code/ingest.py
wget ${PREFIX}/cohorts/2026/01-agentic-rag/code/rag_helper.py
wget ${PREFIX}/cohorts/2026/04-evaluation/code/evaluation_utils.py
```

Then load the FAQ data:

```python
from ingest import load_faq_data
documents = load_faq_data()
```

We'll generate questions only for the LLM Zoomcamp FAQ. The full FAQ
dataset contains documents from multiple courses. Generating five
questions for every document would take longer and cost more.

```python
documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

len(documents_llm)
```

We'll use these documents from now on so let's name them as `documents`

```python
documents = documents_llm
```

Each document already has an `id` field:

```python
doc = documents[0]
print(doc["id"])
print(doc["question"])
print(doc["answer"])
```

The ID becomes the label in our ground truth dataset. We generate
questions from a document, so we know that this document holds the
answer. Later, search evaluation checks whether search brings back the
document with this ID.

This is why every record needs a stable ID. If you can't uniquely
identify a document, you can't tell whether search retrieved the right
one. When you build your own evaluation set, assign an ID to each record
in your knowledge base first.

## Generating questions with structured output

We use an LLM to generate questions for each document.

This is the first time we're using structured output in the course.
With structured output, we ask the LLM to return data in a specific
format instead of free-form text. For example, instead of getting a
paragraph that contains questions, we can ask for a Python object with
a `questions` field.

This is useful when code will process the output. The model returns the
same structure every time. We can access the generated questions
directly instead of parsing text manually.

We want the output as a list of strings, so we define that structure
with a Pydantic model:

```python
from pydantic import BaseModel

class Questions(BaseModel):
    questions: list[str]
```

The instructions for the LLM:

```python
data_gen_instructions = """
You emulate a student who's taking our course.
Formulate 5 questions this student might ask based on a FAQ record. The record
should contain the answer to the questions, and the questions should be complete and not too short.
If possible, use as fewer words as possible from the record.

The output should resemble how people ask questions
on the internet. Not too formal, not too short, not too long.
""".strip()
```

We ask the LLM to use different wording from the original document.
This makes the evaluation more realistic - real users won't phrase
their ques

## Key concepts

- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
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
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=YScoH28cVf8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/02-ground-truth.md)
