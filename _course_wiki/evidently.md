---
title: "Evidently"
summary: "The drift-and-quality evaluation tool MLOps Zoomcamp wires into both streaming and batch monitoring."
related_course:
  - Context Engineering
  - Experiment Tracking
  - Model Deployment
  - Model Monitoring
  - Prometheus and Grafana
  - Risk Management
---

Evidently computes the monitoring signals: comparing the current batch of production data against a reference dataset and producing data drift metrics, target drift reports, and data quality checks. The module generates these as JSON metrics for machines and as dashboards for humans.

In the web-service pipeline, Evidently metrics are exposed on an endpoint for Prometheus to scrape every 15 seconds. In the batch pipeline, Evidently reports run over predictions stored in MongoDB. Either way, the tool turns raw prediction logs into named, thresholdable signals — the raw material for alerting.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Built-in Judge](/course-wiki/llmz-m05-built-in-judge/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 5: Model Monitoring](/course-wiki/mlops-module-05/)
    - [Evidently metrics calculation](/course-wiki/mlops-m05-evidently-metrics-calculation/)
    - [Evidently Monitoring Dashboard](/course-wiki/mlops-m05-evidently-monitoring-dashboard/)
    - [Debugging with test suites and reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [Model Monitoring](/course-wiki/model-monitoring/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Experiment Tracking](/course-wiki/experiment-tracking/)
