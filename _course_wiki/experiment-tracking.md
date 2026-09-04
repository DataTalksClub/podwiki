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

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Generating Ground Truth Data](/course-wiki/llmz-m04-generating-ground-truth-data/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 2: Experiment Tracking & Model Management](/course-wiki/mlops-module-02/)
    - [Experiment tracking intro](/course-wiki/mlops-m02-experiment-tracking-intro/)
    - [Experiment tracking with MLflow](/course-wiki/mlops-m02-experiment-tracking-with-mlflow/)
    - [Homework](/course-wiki/mlops-m02-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [MLflow](/course-wiki/mlflow/)
- [Model Registry](/course-wiki/model-registry/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Model Monitoring](/course-wiki/model-monitoring/)
