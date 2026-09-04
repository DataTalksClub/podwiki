---
title: "Model Monitoring"
summary: "Detecting when a deployed model degrades: data drift, target drift, and score health over time."
related_course:
  - Evidently
  - Experiment Tracking
  - LLM Monitoring
  - MLOps Maturity Model
  - Model Deployment
  - Model Registry
  - OpenTelemetry
  - Prometheus and Grafana
  - Stream Processing
  - Docker
  - LLM Evaluation
---

Module 5 starts from the uncomfortable fact that a deployed model decays: the world shifts away from the training data. Monitoring compares production traffic against a reference dataset (the training data or a known-good period) and flags drift in feature distributions, in prediction distributions, and — where ground truth arrives later — in actual performance metrics.

The course builds two monitoring pipelines: a web service path where Prometheus scrapes Evidently metrics and Grafana dashboards them with alerts, and a batch path where Prefect jobs dump predictions to MongoDB and Evidently reports run over them. The output is actionable: dashboards and alerts that say when to retrain, not just that something changed.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [Chat App](/course-wiki/llmz-m05-chat-app/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [Grafana Dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 6: Best Practices](/course-wiki/llmz-module-06/)
    - [Best Practices for RAG](/course-wiki/llmz-m06-best-practices-for-rag/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 5: Model Monitoring](/course-wiki/mlops-module-05/)
    - [Intro to ML monitoring](/course-wiki/mlops-m05-intro-to-ml-monitoring/)
    - [Evidently Monitoring Dashboard](/course-wiki/mlops-m05-evidently-monitoring-dashboard/)
    - [Dummy monitoring](/course-wiki/mlops-m05-dummy-monitoring/)
    - [Data quality monitoring](/course-wiki/mlops-m05-data-quality-monitoring/)
    - [Debugging with test suites and reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [Evidently](/course-wiki/evidently/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
