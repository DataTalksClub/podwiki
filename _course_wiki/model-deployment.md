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

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [CRISP-DM](/course-wiki/mlz-m01-crisp-dm/)
    - [Setting up the Environment](/course-wiki/mlz-m01-setting-up-the-environment/)
    - [Summary](/course-wiki/mlz-m01-summary/)
  - [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/)
    - [Intro / Session overview](/course-wiki/mlz-m05-intro-session-overview/)
    - [Deployment to the cloud: AWS Elastic Beanstalk (optional)](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
    - [Explore more](/course-wiki/mlz-m05-explore-more/)
  - [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/)
    - [Introduction to Serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
  - [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/)
    - [Overview](/course-wiki/mlz-m10-overview/)
    - [Introduction to Kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
    - [Deploying a simple service to Kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
    - [Deploying TensorFlow models to Kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
    - [Deploying to EKS](/course-wiki/mlz-m10-deploying-to-eks/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Using ONNX Runtime instead of PyTorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Best Practices](/course-wiki/llmz-m03-best-practices/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Evaluation](/course-wiki/llmz-m04-evaluation/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 2: Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-module-02/)
    - [Build and Ship an AI-Assisted Full-Stack App](/course-wiki/aidt-m02-build-and-ship-an-ai-assisted-full-stack-app/)
  - [Module 3: Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-module-03/)
    - [Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-m03-test-containerize-and-deploy-an-ai-assisted-app/)
  - [Module 4: DevOps and Observability for AI-Built Apps](/course-wiki/aidt-module-04/)
    - [DevOps and Observability for AI-Built Apps](/course-wiki/aidt-m04-devops-and-observability-for-ai-built-apps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Using an Orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
  - [Module 4: Model Deployment](/course-wiki/mlops-module-04/)
    - [Three ways of deploying a model](/course-wiki/mlops-m04-three-ways-of-deploying-a-model/)
    - [Web-services: Deploying models with Flask and Docker](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
    - [(Optional) Streaming: Deploying models with Kinesis and Lambda](/course-wiki/mlops-m04-optional-streaming-deploying-models-with-kinesis/)
    - [MLOps Zoomcamp 4.6 - Batch scoring with Mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
  - [Module 5: Model Monitoring](/course-wiki/mlops-module-05/)
    - [Debugging with test suites and reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
  - [Module 6: Best Practices](/course-wiki/mlops-module-06/)
    - [Homework](/course-wiki/mlops-m06-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 1: Containerization and Infrastructure as Code](/course-wiki/dez-module-01/)
    - [Terraform Basics: Simple one file Terraform Deployment](/course-wiki/dez-m01-terraform-basics-simple-one-file-terraform-deplo/)
    - [Deployment with a Variables File](/course-wiki/dez-m01-deployment-with-a-variables-file/)
  - [Module 3: Data Warehousing](/course-wiki/dez-module-03/)
    - [Deploying Machine Learning model from BigQuery](/course-wiki/dez-m03-deploying-machine-learning-model-from-bigquery/)
  - [Module 5: Data Platforms](/course-wiki/dez-module-05/)
    - [Deploying to Bruin Cloud](/course-wiki/dez-m05-deploying-to-bruin-cloud/)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
  - [Module 5: Deployment and Automation](/course-wiki/sma-module-05/)
    - [Deployment and Automation](/course-wiki/sma-m05-deployment-and-automation/)
## Related concepts

- [Model Registry](/course-wiki/model-registry/)
- [Docker](/course-wiki/docker/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)
