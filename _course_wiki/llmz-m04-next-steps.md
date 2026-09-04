---
title: "Next Steps — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=TlKPBjItUw8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Next Steps"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Next Steps

## Notes

---
video_url: "https://www.youtube.com/watch?v=TlKPBjItUw8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Next Steps

In this module, we covered evaluation at three levels:

1. Search evaluation: Hit Rate and MRR to measure retrieval quality
2. RAG evaluation: LLM-as-a-judge for answer quality
3. Agent evaluation: final answers plus tool-call trajectories

Evaluation is not a one-time activity. As you tune search parameters,
switch models, or modify prompts, re-run evaluation. Make sure the
system is getting better, not worse.

Evaluation is the most important part of building AI systems. It is also
the most time-consuming. Only after evaluation can you be confident
that your system works. Validate every change against your evaluation
framework before going to production. This applies to prompt updates,
model swaps, and agent modifications.

## From synthetic data to real data

The evaluation workflow in practice:

1. Start with synthetic data. Use an LLM to generate questions from
   your FAQ or documentation. This gives you a baseline without needing
   real users.
2. Tune the data generation. If the metrics look suspiciously good,
   the synthetic questions may be too close to the source text. Adjust
   the generation prompt to produce more realistic questions.
3. Deploy and collect real data. Once the system is in production, start
   collecting actual user queries and feedback.
4. Label real data. Have humans label whether the retrieved documents
   and generated answers are correct. This produces the most reliable
   ground truth.
5. Tune synthetic generation to match real data. Use the patterns from
   real queries to improve your synthetic data generator. The closer
   your synthetic data is to real data, the more useful the metrics
   become.

Nothing beats manual evaluation. Try the system yourself, think about
edge cases, and collect examples of where it fails. This is especially
important in the early stages when you don't have automated evaluation
set up yet.

## Evaluation frameworks

For production systems, consider using evaluation frameworks that make
it easier to manage test datasets, run evaluations, and track results:

- Ragas: a framework for evaluating RAG systems with metrics like
  faithfulness, answer relevance, and context precision
- DeepEval: provides built-in metrics for RAG evaluation including
  hallucination detection and answer relevance
- TruLens: instruments your LLM app and tracks quality metrics

These frameworks implement many of the concepts we covered here and
add visualizations and experiment tracking.

## Monitoring

Online evaluation (monitoring) is what you do after deploying your
system.

Key approaches:

- User feedback: thumbs up/down buttons to collect signal
- Logging: record queries, retrieved documents, and answers
- Dashboards: track metrics over time to spot degradation
- Alerts: get notified when metrics drop below a threshold

Monitoring is covered in more detail in module 05.

## To learn more

See also:

- Cohorts and materials:
  - 2024 cohort evaluation module (uses Elasticsearch):
    [2024/04-monitoring](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/cohorts/2024/04-monitoring)
  - 2025 cohort evaluation module:
    [2025/03-evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/cohorts/2025/03-evaluation)

## Key concepts

- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Model Deployment](/course-wiki/model-deployment/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m02-using-onnx-runtime-instead-of-pytorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
- [llmz-m02-vector-search-with-sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
- [llmz-m03-best-practices](/course-wiki/llmz-m03-best-practices/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
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

- [Video](https://www.youtube.com/watch?v=TlKPBjItUw8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/15-next-steps.md)
