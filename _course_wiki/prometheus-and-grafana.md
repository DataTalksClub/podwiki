---
title: "Prometheus and Grafana"
summary: "The metrics-scraping and dashboarding pair behind MLOps Zoomcamp's live model monitoring."
related_course:
  - CI/CD
  - Evidently
  - Kestra
  - Model Deployment
  - Model Monitoring
  - OpenTelemetry
---

Prometheus scrapes numerical metrics from running services on a schedule and stores them as time series; Grafana queries those series and draws the operational picture. MLOps Zoomcamp connects them to ML monitoring: the prediction service exposes Evidently-derived metrics (drift scores, prediction counts, interquartile distances) on a /metrics endpoint, Prometheus collects them every 15 seconds, and Grafana dashboards show drift and traffic over time with alert rules on top.

The module's Docker Compose stack runs the whole loop locally — service, Prometheus, Grafana, and an Evidently metrics service — so learners see alerts fire when they send drifted data through the service.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Monitoring](/course-wiki/llmz-m05-monitoring/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [Streamlit Dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
    - [Feedback Dashboard](/course-wiki/llmz-m05-feedback-dashboard/)
    - [Synthetic Data Generation](/course-wiki/llmz-m05-synthetic-data-generation/)
    - [Grafana Dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
    - [Docker Compose](/course-wiki/llmz-m05-docker-compose/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 5: Model Monitoring](/course-wiki/mlops-module-05/)
    - [Save Grafana Dashboard](/course-wiki/mlops-m05-save-grafana-dashboard/)
    - [Debugging with test suites and reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
## Related concepts

- [Evidently](/course-wiki/evidently/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Model Deployment](/course-wiki/model-deployment/)
- [OpenTelemetry](/course-wiki/opentelemetry/)
- [CI/CD](/course-wiki/ci-cd/)
