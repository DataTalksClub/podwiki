---
title: "Model Deployment"
summary: "The three ways a model reaches consumers — web service, streaming, and batch — and when each fits."
related_course:
  - CI/CD
  - CRISP-DM
  - Docker
  - Evidently
  - FastAPI
  - Kubernetes
  - MLOps Maturity Model
  - MLflow
  - Model Monitoring
  - Model Registry
  - Prometheus and Grafana
  - Serverless Deployment
  - Workflow Orchestration
---

Module 4 organizes deployment into three shapes. Web services (online): a Flask/Flask-and-Docker service answers prediction requests in real time, pulling the model from the registry. Streaming: events flow through AWS Kinesis, a Lambda function scores each one, and results go to a sink — for per-event latency without a always-on server. Batch: scheduled jobs score a table of records at once, which is often the cheapest and simplest option when real-time answers are not required.

The module's decision frame is business-driven: how fast do consumers need predictions, and how do they call the model? The final project requires deploying in at least one of the three shapes with the monitoring hooks from module 5 attached.

## Taught in

- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — Module 4: Model Deployment

## Related concepts

- [Model Registry](/course-wiki/model-registry/)
- [Docker](/course-wiki/docker/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)
