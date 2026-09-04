---
title: "Evaluation — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=eC_IcxfxoiQ&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Evaluation"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Evaluation

## Notes

---
video_url: "https://www.youtube.com/watch?v=eC_IcxfxoiQ&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Evaluation

In the previous modules, we built search engines and RAG pipelines.
We tried different approaches: keyword search with minsearch, vector
search, agents with function calling. But we never answered the obvious
question of which one is actually better.

We could try a few queries by hand and see what looks good. That's fine
for a quick sanity check, but it doesn't scale, and it doesn't give us a
number to compare. We need a systematic way to tell whether one approach
beats another.

That's what evaluation is for. And it's worth saying up front: of
everything in this course, evaluation is the part that matters most. It's
also the most tedious. But it's the only way to be sure your system
works. And it's how you keep it working as you change prompts and swap
models.

## The evaluation setup

For search evaluation, we need a dataset of questions where we know
which document is the correct answer. We'll use an LLM to generate
these questions from our FAQ data.

The approach works like this:

- A = the original answer in the FAQ
- Q* = a question generated from that answer by an LLM
- We send Q* through our search and check if the original document
  appears in the results

For RAG evaluation, we go one step further:

- A = the original answer in the FAQ
- Q* = a question generated from that answer by an LLM
- A' = the answer produced by our RAG system when given Q*
- We compare A' with A to see if the system produced the right answer

This is the A → Q* → A' pattern. We know the answer for each generated
question because we created the question from that answer.

With evaluation, we can:

- Compare different search methods (minsearch vs vector search vs hybrid)
- Tune parameters (boost values, number of results, prompt templates)
- Compare different LLMs (gpt-5.4-mini vs others)
- Track improvements over time

There are two types of evaluation:

- Offline evaluation: run the system on a test dataset and compute metrics
- Online evaluation: collect feedback from real users in production

Offline evaluation is what we do before putting changes in front of
users. It lets us compare search settings, prompts, or models on the
same dataset. Online evaluation happens after deployment. It uses real
traffic, feedback, logs, and dashboards to monitor quality.

In this module, we focus on offline evaluation. We'll generate a test
dataset, run our search and RAG systems on it, and measure how well they
perform.

Synthetic data is a good starting point when you don't have real user
data. But generated questions can be too similar to the original FAQ
text, which inflates the metrics. As soon as you can, start collecting
real user queries and use them to validate your evaluation framework.

We'll cover three levels of evaluation:

1. Search evaluation: does the search return the right documents?
2. RAG evaluation: does the LLM generate good answers?
3. Agent evaluation: does the agent use tools efficiently?

Most of our time goes to search, and that's on purpose. Everything else
depends on it: if retrieval brings back the wrong documents, no prompt or
model can rescue the answer. So we test search on its own first, then
evaluate the full pipeline on top of it.

For search, we'll use two metrics: Hit Rate and MRR (Mean Reciprocal
Rank). For RAG quality, we'll use LLM-as-a-judge. For agents, we'll
look at the final answer and the tool-call trajectory.

Let's start with generating the test data we need.

## Key concepts

- [Function Calling](/course-wiki/function-calling/)
- [Keyword Search](/course-wiki/keyword-search/)
- [Vector Search](/course-wiki/vector-search/)
- [Model Deployment](/course-wiki/model-deployment/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-agents](/course-wiki/llmz-m01-agents/)
- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m01-data-ingestion](/course-wiki/llmz-m01-data-ingestion/)
- [llmz-m01-environment](/course-wiki/llmz-m01-environment/)
- [llmz-m01-function-calling](/course-wiki/llmz-m01-function-calling/)
- [llmz-m01-other-frameworks](/course-wiki/llmz-m01-other-frameworks/)
- [llmz-m01-quick-rag-revision-optional](/course-wiki/llmz-m01-quick-rag-revision-optional/)
- [llmz-m01-rag](/course-wiki/llmz-m01-rag/)
- [llmz-m01-rag-helper](/course-wiki/llmz-m01-rag-helper/)
- [llmz-m01-search](/course-wiki/llmz-m01-search/)
- [llmz-m01-the-agentic-loop](/course-wiki/llmz-m01-the-agentic-loop/)
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
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m03-retrieval-augmented-generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
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
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
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

- [Video](https://www.youtube.com/watch?v=eC_IcxfxoiQ&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/01-intro.md)
