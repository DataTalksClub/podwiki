---
title: "Kubernetes"
summary: "Orchestrating containerized model services: pods, services, scaling, and TensorFlow Serving."
related_course:
  - Docker
  - FastAPI
  - Function Calling
  - Loop and Graph Engineering
  - Model Deployment
  - Serverless Deployment
---

The final ML Zoomcamp module serves models with Kubernetes. A trained TensorFlow model runs behind TensorFlow Serving; Kubernetes wraps it in a deployment, exposes it through a service, and distributes traffic across replicas. The course teaches the core object model — pods, deployments, services, ingress — at the depth needed to run model serving, not to administer clusters.

Scaling and load distribution are the operational payoff: when prediction traffic grows, Kubernetes adds replicas behind the same endpoint. The module completes the course arc — from a notebook model in module 2 to a horizontally scaled prediction service.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/)
    - [Overview](/course-wiki/mlz-m10-overview/)
    - [Introduction to Kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
    - [Deploying a simple service to Kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
    - [Deploying TensorFlow models to Kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
## Related concepts

- [Serverless Deployment](/course-wiki/serverless-deployment/)
- [Docker](/course-wiki/docker/)
- [FastAPI](/course-wiki/fastapi/)
- [Model Deployment](/course-wiki/model-deployment/)
