---
title: "RAG and Agent Evaluation — LLM Zoomcamp Module 4"
summary: "---
video_url: "https://www.youtube.com/watch?v=VKHBP0QSCFo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# RAG and Agent Evaluation"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › RAG and Agent Evaluation

## Notes

---
video_url: "https://www.youtube.com/watch?v=VKHBP0QSCFo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# RAG and Agent Evaluation

So far, we evaluated retrieval. We checked whether search returns the
document that should answer the question.

That is only the first step. A complete application still needs to
produce a final answer. For RAG, this means checking the generated
answer. For agents, it also means looking at the tool calls the model
made before producing the answer.

RAG evaluation checks the whole flow together.

This includes:

- search
- prompt
- LLM

If the final answer is bad, the problem can come from any of these
steps. The search might retrieve the wrong document, the prompt might
omit important context, or the LLM might ignore the context.

In this part, we'll evaluate:

- RAG answers with an LLM judge
- Agent answers and tool-call trajectories

We won't go deep into agent evaluation frameworks here. We'll use the
agent from module 01, save the final answer, and also save the tool
calls. Then we can look at whether the answer is good and whether the
trajectory looks reasonable.

## LLM as a judge

For RAG and agent evaluation, we compare the generated answer with the
original answer. The generated answer won't use the same words as the
original. It's a generative model, so the phrasing will be different
even when the meaning is the same.

This is why we use another LLM to do the comparison. We show the judge
the question, the original answer, and the generated answer. Then we ask
it to decide if they are semantically equivalent.

This approach is called LLM-as-a-judge. The evaluating LLM is the
judge. It classifies each answer as good or bad and explains its
reasoning. Asking the judge to explain why it made a decision generally
produces better classifications than asking for just the verdict.

Next, we'll start with the RAG case and generate answers for the ground
truth questions.

## Key concepts

- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
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

- [Video](https://www.youtube.com/watch?v=VKHBP0QSCFo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/11-evaluation-intro.md)
