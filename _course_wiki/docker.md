---
title: "Docker"
summary: "Container packaging for model services, pipeline components, and app deployments across four Zoomcamps."
related_course:
  - BigQuery
  - Bruin
  - CI/CD
  - FastAPI
  - Kestra
  - Kubernetes
  - Model Deployment
  - Playwright
  - Serverless Deployment
  - Terraform
  - Transfer Learning
---

Docker turns an application plus its dependencies into a portable image. Data Engineering Zoomcamp introduces it first: Postgres, pgAdmin, and later pipeline components all run as containers defined in docker-compose files, so a local environment mirrors production.

Machine Learning Zoomcamp uses the same skill to package a FastAPI model service into an image that runs identically on a laptop and in the cloud. MLOps Zoomcamp deploys Flask web services in containers and runs integration tests with docker-compose; AI Dev Tools Zoomcamp containerizes the full-stack app with Docker Compose and Postgres before deploying it to AWS. The throughline: if it runs in the container, it runs anywhere.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [Setting up the Environment](/course-wiki/mlz-m01-setting-up-the-environment/)
  - [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/)
    - [Intro / Session overview](/course-wiki/mlz-m05-intro-session-overview/)
    - [Python virtual environment: Pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
    - [Environment management: Docker](/course-wiki/mlz-m05-environment-management-docker/)
    - [Deployment to the cloud: AWS Elastic Beanstalk (optional)](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
  - [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/)
    - [TensorFlow Lite](/course-wiki/mlz-m09-tensorflow-lite/)
    - [Preparing a Docker image](/course-wiki/mlz-m09-preparing-a-docker-image/)
    - [Python 3.12 vs TF Lite 2.17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
  - [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/)
    - [Overview](/course-wiki/mlz-m10-overview/)
    - [Creating a pre-processing service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
    - [Introduction to Kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Environment](/course-wiki/llmz-m01-environment/)
    - [Search](/course-wiki/llmz-m01-search/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search](/course-wiki/llmz-m02-vector-search/)
    - [Embeddings](/course-wiki/llmz-m02-embeddings/)
    - [Vector Search with PGVector](/course-wiki/llmz-m02-vector-search-with-pgvector/)
    - [Using ONNX Runtime instead of PyTorch](/course-wiki/llmz-m02-using-onnx-runtime-instead-of-pytorch/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [Setting up Kestra](/course-wiki/llmz-m03-setting-up-kestra/)
    - [Retrieval Augmented Generation](/course-wiki/llmz-m03-retrieval-augmented-generation/)
    - [AI Agents](/course-wiki/llmz-m03-ai-agents/)
  - [Module 5: Monitoring](/course-wiki/llmz-module-05/)
    - [Storing Data in PostgreSQL](/course-wiki/llmz-m05-storing-data-in-postgresql/)
    - [Streamlit Dashboard](/course-wiki/llmz-m05-streamlit-dashboard/)
    - [Synthetic Data Generation](/course-wiki/llmz-m05-synthetic-data-generation/)
    - [Grafana Dashboards](/course-wiki/llmz-m05-grafana-dashboards/)
    - [Docker Compose](/course-wiki/llmz-m05-docker-compose/)
    - [Next Steps](/course-wiki/llmz-m05-next-steps/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/)
  - [Module 3: Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-module-03/)
    - [Test, Containerize, and Deploy an AI-Assisted App](/course-wiki/aidt-m03-test-containerize-and-deploy-an-ai-assisted-app/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 1: Introduction](/course-wiki/mlops-module-01/)
    - [2 VM in AWS](/course-wiki/mlops-m01-2-vm-in-aws/)
    - [Homework](/course-wiki/mlops-m01-homework/)
  - [Module 2: Experiment Tracking & Model Management](/course-wiki/mlops-module-02/)
    - [Homework](/course-wiki/mlops-m02-homework/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Homework](/course-wiki/mlops-m03-homework/)
  - [Module 4: Model Deployment](/course-wiki/mlops-module-04/)
    - [Web-services: Deploying models with Flask and Docker](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
  - [Module 5: Model Monitoring](/course-wiki/mlops-module-05/)
    - [Debugging with test suites and reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
  - [Module 6: Best Practices](/course-wiki/mlops-module-06/)
    - [Homework](/course-wiki/mlops-m06-homework/)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/)
  - [Module 3: Data Warehousing](/course-wiki/dez-module-03/)
    - [Deploying Machine Learning model from BigQuery](/course-wiki/dez-m03-deploying-machine-learning-model-from-bigquery/)
  - [Module 4: Analytics Engineering](/course-wiki/dez-module-04/)
    - [Analytics Engineering](/course-wiki/dez-m04-analytics-engineering/)
## Related concepts

- [FastAPI](/course-wiki/fastapi/)
- [CI/CD](/course-wiki/ci-cd/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Terraform](/course-wiki/terraform/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)
