---
title: "Experiment Tracking"
summary: "Recording every training run's parameters, metrics, and artifacts so results can be compared and reproduced."
related_course:
  - Evidently
  - MLOps Maturity Model
  - MLflow
  - Model Monitoring
  - Model Registry
  - Workflow Orchestration
---

Experiment tracking solves the 'which of the fifty training runs produced this model?' problem. Module 2 instruments the NY Taxi training code with MLflow: every run records its parameters (features, hyperparameters), metrics (RMSE on validation), and artifacts (the pickled model), all browsable in the tracking UI.

With runs logged, model selection becomes a query instead of memory: sort runs by metric, compare parameter sets side by side, and promote the winner. The module treats this as the first non-negotiable MLOps practice — before pipelines, before deployment, you need to know what you trained and how it performed.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 2: Experiment Tracking and Model Management

## Related concepts

- [MLflow](/course-wiki/mlflow/)
- [Model Registry](/course-wiki/model-registry/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Model Monitoring](/course-wiki/model-monitoring/)
