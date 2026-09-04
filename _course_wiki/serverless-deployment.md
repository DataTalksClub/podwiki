---
title: "Serverless Deployment"
summary: "Serving models from AWS Lambda functions instead of a persistent server, exposed through API Gateway."
related_course:
  - Kubernetes
  - FastAPI
  - Docker
  - Neural Networks
  - Transfer Learning
---

Module 9 deploys models with AWS Lambda: the model and its dependencies are packaged into a Lambda-compatible container or layer, the function loads the model on invocation, and API Gateway exposes it over HTTP. The pay-per-request model fits spiky or low-traffic prediction loads without a server to maintain.

The engineering work is packaging: TensorFlow and PyTorch dependencies exceed Lambda size limits, so the course builds Lambda containers with the model baked in, and shows TensorFlow Serving as the alternative path. Learners leave with a prediction endpoint that scales to zero.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 9: Serverless Deep Learning

## Related concepts

- [Kubernetes](/course-wiki/kubernetes/)
- [FastAPI](/course-wiki/fastapi/)
- [Docker](/course-wiki/docker/)
- [Neural Networks](/course-wiki/neural-networks/)
- [Transfer Learning](/course-wiki/transfer-learning/)
