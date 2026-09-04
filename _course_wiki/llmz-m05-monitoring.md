---
title: "Monitoring — LLM Zoomcamp Module 5"
summary: "---
video_url: "https://www.youtube.com/watch?v=lbEj3Waxs1U&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Monitoring"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Monitoring

## Notes

---
video_url: "https://www.youtube.com/watch?v=lbEj3Waxs1U&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Monitoring

In the previous module we evaluated our system offline, before anyone
used it. We measured search quality with Hit Rate and MRR, and answer
quality with cosine similarity and an LLM judge.

But once we deploy, real people start asking real questions. The offline
numbers stop telling the whole story. We don't know how long answers
take, what they cost, or whether anyone finds them useful. We need to
watch the system while it runs.

That's monitoring: online evaluation. We collect metrics from the
running system and put them on a dashboard. Then we can see how it
performs with real traffic.

For every question that comes in, there's a lot we can capture:

- The instructions, prompt, and model behind the answer
- Input and output tokens, and how much the call cost
- Response time: how long the person waited
- User feedback: a thumbs up or thumbs down on the answer
- Relevance: does the answer address the question?

Collecting and viewing all of this takes three new pieces:

- a user interface where people ask questions
- a database to store conversations and feedback
- a dashboard to visualize the metrics

We build all three on top of the RAG pipeline from the earlier modules.
We don't rebuild the RAG part. We wrap it in a Streamlit app and save
every interaction to PostgreSQL. Then we put a dashboard in front of the
data. At the end we add Grafana for a more powerful view.

We focus on RAG here. Monitoring an agent works almost the same way, so
we leave it as homework. The [agents module](../01-agentic-rag/)
already has the pieces you need to apply these same ideas there.

## Key concepts

- [Model Monitoring](/course-wiki/model-monitoring/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m03-ai-agents](/course-wiki/llmz-m03-ai-agents/)
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
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
- [llmz-m05-storing-data-in-postgresql](/course-wiki/llmz-m05-storing-data-in-postgresql/)
- [llmz-m05-streamlit-dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
- [llmz-m05-synthetic-data-generation](/course-wiki/llmz-m05-synthetic-data-generation/)
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

- [Video](https://www.youtube.com/watch?v=lbEj3Waxs1U&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/01-intro.md)
