---
title: "LLM Monitoring"
summary: "Watching a live LLM application: user feedback, system health, and drift in what users ask."
related_course:
  - CRISP-DM
  - LLM Evaluation
  - Model Monitoring
  - RAG
  - Terraform
  - dlt
---

Module 5 keeps watch after deployment. The signals are different from classic ML: explicit user feedback (thumbs up/down on answers), implicit signals (users rephrasing questions, abandoning conversations), system health (latency, errors, token spend), and the distribution of incoming questions drifting toward topics the knowledge base does not cover.

The course builds the monitoring loop with the dlt workshop's trace pipelines feeding dashboards — queries, retrieved documents, generated answers, and feedback all land in DuckDB for analysis. Monitoring closes the loop that evaluation opened: what you measure in production becomes the next round of test cases and improvements.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [User Feedback](/course-wiki/llmz-m05-user-feedback/)
    - [Feedback Dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
    - [Grafana Dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
## Related concepts

- [LLM Evaluation](/course-wiki/llm-evaluation/)
- [dlt](/course-wiki/dlt/)
- [RAG](/course-wiki/rag/)
- [Model Monitoring](/course-wiki/model-monitoring/)
