---
title: "Model Registry"
summary: "The promotion path between training and serving: registered versions, stages, and a single source of the production model."
related_course:
  - CRISP-DM
  - Experiment Tracking
  - MLOps Maturity Model
  - MLflow
  - Model Deployment
  - Model Monitoring
---

The model registry sits between experiment tracking and deployment. Trained models are registered as named models with versioned versions; a version moves through stages — staging, then production — and the deployment code loads from the registry by name and stage instead of by hard-coded run id.

Module 4 completes the loop: the web service queries the registry for the production version of the NY Taxi model and downloads it at startup. Moving a new model to production becomes a registry operation (promote the version), not a redeploy — the serving code always pulls whatever production points to.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 2: Experiment Tracking & Model Management](/course-wiki/mlops-module-02/)
    - [Model registry](/course-wiki/mlops-m02-model-registry/)
  - [Module 4: Model Deployment](/course-wiki/mlops-module-04/)
    - [Web-services: Getting the models from the model registry (MLflow)](/course-wiki/mlops-m04-web-services-getting-the-models-from-the-model-r/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [MLflow](/course-wiki/mlflow/)
- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [MLOps Maturity Model](/course-wiki/mlops-maturity-model/)
