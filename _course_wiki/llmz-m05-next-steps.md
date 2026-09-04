---
title: "Next Steps — LLM Zoomcamp Module 5"
summary: "---
video_url: "https://www.youtube.com/watch?v=GpQeAniVGfk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Next Steps"
related_course:
  - llmz-module-05
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 5: Monitoring](/course-wiki/llmz-module-05/) › Next Steps

## Notes

---
video_url: "https://www.youtube.com/watch?v=GpQeAniVGfk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Next Steps

Let's recap what we did. We took the RAG pipeline from the earlier
modules and wrapped it in a simple Streamlit interface. We started
recording every interaction to PostgreSQL.

On top of that data we built a dashboard, first in Streamlit and then in
Grafana. It tracks response time, cost, tokens, and which models we use.
Then we added two quality signals: an LLM judge, plus thumbs up and down
from users.

We now have two things we didn't have before. We have visibility into how
the system behaves, and we have logs to dig into when something looks
wrong.

## Build it yourself, or use a framework

Doing the instrumentation by hand gives you total flexibility. You
capture exactly what you want and store it where you want. You don't
always need that much control, though.

Several tools are built for this and take the wiring off your hands:

- [Langfuse](https://langfuse.com/) and
  [Arize Phoenix](https://phoenix.arize.com/) trace LLM apps.
- [Pydantic Logfire](https://pydantic.dev/logfire) is my favorite for
  monitoring. It instruments your code and gives you a dashboard with the
  metrics already wired up, so you write almost nothing.
- [Evidently](https://www.evidentlyai.com/) works for both monitoring and
  evaluation. I mostly reach for it on the eval side.

The automatic tools have a flip side. You get a dashboard for free, but
you don't always know what they capture. And changing something means
digging into the framework. So it's a real tradeoff: hand-rolling gives
you control, frameworks give you speed. Try a couple and see which you
like.

## Going to production

What we built is a minimal example to show the concepts, not a production
setup. Two things in particular change at scale.

The first is overhead. Each call now writes to the database, and the
judge adds another LLM call. In production you'd do this asynchronously so
it doesn't slow down the user's request. You capture into a queue and
process it separately.

The second is storage. Postgres is fine for us, but it isn't the best
place to store high-volume logs. A common pattern is to push events to
something like Kafka and let downstream systems store them.

[OpenTelemetry](https://opentelemetry.io/) is the standard worth knowing
here. It's the instrumentation layer that tools like Logfire and Langfuse
build on, and it's simple to set up. Conceptually your system will look
like what we built. The technology behind it will likely be something
else.

## Homework

We only covered RAG, so pick one of these to take it further:

- Monitor an agent. Apply the same instrumentation to an agent from the
  [agents module](../01-agentic-rag/), capturing each tool call the
  way we captured LLM calls.
- Generate synthetic data and watch the Grafana dashboard fill out, as in
  the synthetic data lesson.
- Move everything to Docker Compose so the whole stack starts with one
  command. The [Docker Compose lesson](13-docker-compose.md) has no video,
  and the compose file and the Dockerfile live only in the lesson text -
  they aren't in `code/`, which still starts Postgres with a plain
  `docker run`. So write them out yourself, then take it past what the
  lesson shows. `db_init.py` still runs by hand afterwards, so fold it in
  as an init step. Grafana's datasource and dashboards are clicked
  together in the UI in the [Grafana lesson](12-grafana.md), so provision
  them from files instead, and a fresh clone comes up with the dashboard
  already there. Add a healthcheck on Postgres so the app doesn't race the
  database on a cold start. Then `docker-compose up` really is the only
  command you need.

## Older content

The 2024 cohort used Elasticsearch instead of minsearch and ran Ollama
for local models. If that setup is useful to you, see the
[2024 monitoring module](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/cohorts/2024/04-monitoring).

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
- [llmz-m05-assistant](/course-wiki/llmz-m05-assistant/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-chat-app](/course-wiki/llmz-m05-chat-app/)
- [llmz-m05-docker-compose](/course-wiki/llmz-m05-docker-compose/)
- [llmz-m05-feedback-dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
- [llmz-m05-grafana-dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-querying-data](/course-wiki/llmz-m05-querying-data/)
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
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=GpQeAniVGfk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/05-monitoring/14-next-steps.md)
