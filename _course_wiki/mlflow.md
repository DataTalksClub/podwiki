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

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 2: Experiment Tracking & Model Management](/course-wiki/mlops-module-02/)
    - [Getting started with MLflow](/course-wiki/mlops-m02-getting-started-with-mlflow/)
    - [Experiment tracking with MLflow](/course-wiki/mlops-m02-experiment-tracking-with-mlflow/)
    - [Model registry](/course-wiki/mlops-m02-model-registry/)
    - [MLflow in practice](/course-wiki/mlops-m02-mlflow-in-practice/)
    - [MLflow: benefits, limitations and alternatives](/course-wiki/mlops-m02-mlflow-benefits-limitations-and-alternatives/)
    - [Homework](/course-wiki/mlops-m02-homework/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Homework](/course-wiki/mlops-m03-homework/)
  - [Module 4: Model Deployment](/course-wiki/mlops-module-04/)
    - [Web-services: Getting the models from the model registry (MLflow)](/course-wiki/mlops-m04-web-services-getting-the-models-from-the-model-r/)
    - [MLOps Zoomcamp 4.6 - Batch scoring with Mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [Model Registry](/course-wiki/model-registry/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
- [Model Deployment](/course-wiki/model-deployment/)
