---
title: "Generating Ground Truth for All Documents — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=eM6xmdZDT6k&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Generating Ground Truth for All Documents"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Generating Ground Truth for All Documents

## Notes

---
video_url: "https://www.youtube.com/watch?v=eM6xmdZDT6k&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Generating Ground Truth for All Documents

In the previous lesson, we generated questions for one document and
converted them into ground truth records.

We want to do the same thing for every document in the FAQ dataset.
For each document, we generate questions and save them as ground truth
records.

For this part, we'll use `tqdm` for progress bars and `pandas` for
saving the final CSV.

If you don't have them installed yet, add them first:

```bash
uv add tqdm pandas
```

The processing function takes one document and turns it into ground
truth records.

For each document, we:

- convert the document to JSON so we can send it to the LLM
- ask the LLM to return a `Questions` object
- create one ground truth record for each generated question

Each record contains the generated question and the ID of the document
that should answer the question.

When we send many requests, one of them might fail. We don't want the
entire batch to fail because of one temporary error.

Import the retry helper from `evaluation_utils.py`:

```python
from evaluation_utils import llm_structured_retry
```

`llm_structured` makes one structured-output call. `llm_structured_retry`
wraps the same call in a retry loop. If one request fails because of a
temporary API or network issue, it waits briefly and tries again.

Use it in the processing function:

```python
def generate_ground_truth(doc):
    user_prompt = json.dumps(doc)

    out, usage = llm_structured_retry(
        openai_client,
        data_gen_instructions,
        user_prompt,
        Questions
    )

    results = []

    for q in out.questions:
        results.append({
            "question": q,
            "document": doc["id"]
        })

    return results, usage
```

Try it for the first 5 documents.

Import `tqdm` and run the loop:

```python
from tqdm.auto import tqdm

ground_truth = []
usages = []

for doc in tqdm(documents[:5]):
    records, usage = generate_ground_truth(doc)
    ground_truth.extend(records)
    usages.append(usage)
```

This works, but it runs one LLM call after another. Running it for all
documents this way would take too long.

## Parallel processing

Running the calls one after another wastes most of the time waiting on
the network. Each request just sits there until OpenAI responds, so we
can fire several at once and wait on them together. We process the
documents in parallel and track progress while the requests run.

One caution: don't open too many connections at once, or you'll hit the
provider's rate limits. Five or six workers is a safe default here.

Import `ThreadPoolExecutor`:

```python
from concurrent.futures import ThreadPoolExecutor
from evaluation_utils import map_progress
```

This submits one job per document, updates the progress bar when a job
finishes, and collects the results. If you want a more detailed
explanation of `ThreadPoolExecutor` and futures, ask ChatGPT to walk
through this helper line by line.

Then replace the loop with the parallel version:

```python
with ThreadPoolExecutor(max_workers=6) as pool:
    results = map_progress(pool, documents, generate_ground_truth)
```

`generate_ground_truth` returns two things for each document: the
generated records and the token usage.

Split those into separate lists:

```python
ground_truth = []
usages = []

for records, usage in results:
    ground_truth.extend(records)
    usages.append(usage)

len(ground_truth)
```

With 5 questions per document, you should get roughly 5x the number of
documents.

Calculate the total cost:

```python
from evaluation_utils import calc_price

total_cost = 0.0

for usage in usages:
    cost = calc_price(usage)
    total_cost = total_cost + cost["total_cost"]

total_cost
```

We'll calculate total cost several times in this module, so the utility
file has a helper for it:

```python
from evaluation_utils import calc_total_price

calc_total_price(us

## Key concepts

- [Pandas](/course-wiki/pandas/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-vector-search](/course-wiki/llmz-m02-vector-search/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
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
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=eM6xmdZDT6k&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/03-ground-truth-batch.md)
