---
title: "FastAPI"
summary: "The Python web framework ML Zoomcamp uses to expose trained models as prediction services and AI Dev Tools Zoomcamp uses for API backends."
related_course:
  - Docker
  - Serverless Deployment
  - Model Deployment
  - OpenAPI Contract
  - Kubernetes
---

In Machine Learning Zoomcamp, deployment starts when a trained model becomes a web service. FastAPI wraps the pickled model in a predict endpoint: the service loads the model at startup, receives JSON feature payloads, and returns predictions. The course chose it for its automatic validation (type hints via pydantic) and built-in interactive docs.

The service then gets packaged into a Docker image and shipped to the cloud, which is the module-to-module arc of the course. AI Dev Tools Zoomcamp reuses FastAPI as the backend framework for its full-stack app, implemented from an OpenAPI contract with tests.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 5: Deploying Machine Learning Models
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — Module 2: Build and Ship an AI-Assisted Full-Stack App

## Related concepts

- [Docker](/course-wiki/docker/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)
- [Model Deployment](/course-wiki/model-deployment/)
- [OpenAPI Contract](/course-wiki/openapi-contract/)
- [Kubernetes](/course-wiki/kubernetes/)
