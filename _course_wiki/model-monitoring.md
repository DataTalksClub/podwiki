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
---

Module 5 starts from the uncomfortable fact that a deployed model decays: the world shifts away from the training data. Monitoring compares production traffic against a reference dataset (the training data or a known-good period) and flags drift in feature distributions, in prediction distributions, and — where ground truth arrives later — in actual performance metrics.

The course builds two monitoring pipelines: a web service path where Prometheus scrapes Evidently metrics and Grafana dashboards them with alerts, and a batch path where Prefect jobs dump predictions to MongoDB and Evidently reports run over them. The output is actionable: dashboards and alerts that say when to retrain, not just that something changed.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 5: Model Monitoring

## Related concepts

- [Evidently](/course-wiki/evidently/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
