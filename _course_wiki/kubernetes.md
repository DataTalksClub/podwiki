---
title: "Kubernetes"
summary: "Orchestrating containerized model services: pods, services, scaling, and TensorFlow Serving."
related_course:
  - Serverless Deployment
  - Docker
  - FastAPI
  - Model Deployment
---

The final ML Zoomcamp module serves models with Kubernetes. A trained TensorFlow model runs behind TensorFlow Serving; Kubernetes wraps it in a deployment, exposes it through a service, and distributes traffic across replicas. The course teaches the core object model — pods, deployments, services, ingress — at the depth needed to run model serving, not to administer clusters.

Scaling and load distribution are the operational payoff: when prediction traffic grows, Kubernetes adds replicas behind the same endpoint. The module completes the course arc — from a notebook model in module 2 to a horizontally scaled prediction service.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 10: Kubernetes and TensorFlow Serving

## Related concepts

- [Serverless Deployment](/course-wiki/serverless-deployment/)
- [Docker](/course-wiki/docker/)
- [FastAPI](/course-wiki/fastapi/)
- [Model Deployment](/course-wiki/model-deployment/)
