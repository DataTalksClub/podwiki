---
title: "MLflow"
summary: "The open-source ML lifecycle toolkit MLOps Zoomcamp standardizes on: tracking, model logging, and a registry."
related_course:
  - Experiment Tracking
  - MLOps Maturity Model
  - Model Deployment
  - Model Registry
  - OpenAPI Contract
  - Workflow Orchestration
---

MLflow is the course's tool for the experiment-tracking module: mlflow.start_run() wraps a training run, autologging or explicit calls capture parameters and metrics, and mlflow.log_artifact stores the trained model in a standard format. A tracking server (local in the course, remote in production) keeps everything browsable.

The module also covers the practical operations: loading a logged model back for scoring, switching the artifact store to S3, and standing up a remote tracking server so runs from training jobs and deployments land in the same place. Deployment later pulls models from MLflow by run id and stage.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 2: Experiment Tracking and Model Management

## Related concepts

- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [Model Registry](/course-wiki/model-registry/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
- [Model Deployment](/course-wiki/model-deployment/)
