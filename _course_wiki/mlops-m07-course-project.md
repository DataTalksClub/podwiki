---
title: "Course Project — MLOps Zoomcamp Module 07"
summary: "Module overview and materials for Course Project."
related_course:
  - mlops-module-07
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 07: Course Project](/course-wiki/mlops-module-07/) › Course Project

## Notes

## Course Project

<a href="https://www.loom.com/share/8f99d25893de4fb8aaa95c0395c740b6">
  
</a>

### Objective

The goal of this project is to apply everything we have learned
in this course to build an end-to-end machine learning project.

## Problem statement

For the project, we will ask you to build an end-to-end ML project. 

For that, you will need:

* Select a dataset that you're interested in (see Datasets)
* Train a model on that dataset tracking your experiments
* Create a model training pipeline
* Deploy the model in batch, web service or streaming
* Monitor the performance of your model
* Follow the best practices 

## Datasets you cannot use

The NYC taxi dataset is used throughout the course modules and homework. It cannot be used for the project. Pick any other dataset.

## Technologies 

You don't have to limit yourself to technologies covered in the course. You can use alternatives as well:

* **Cloud**: AWS, GCP, Azure, ... 
* **Experiment tracking tools**: MLFlow, Weights & Biases, ... 
* **Workflow orchestration**: Prefect, Airflow, Flyte, Kubeflow, Argo, ...
* **Monitoring**: Evidently, WhyLabs/whylogs, ...
* **CI/CD**: Github actions, Gitlab CI/CD, ...
* **Infrastructure as code (IaC)**: Terraform, Pulumi, Cloud Formation, ...

If you use a tool that wasn't covered in the course, be sure to explain what that tool does.

If you're not certain about some tools, ask in Slack.

## Peer reviewing

> [!IMPORTANT]  
> To evaluate the projects, we'll use peer reviewing. This is a great opportunity for you to learn from each other.
> * To get points for your project, you need to evaluate 3 projects of your peers
> * You get 3 extra points for each evaluation

## Evaluation Criteria

* Problem description
    * 0 points: The problem is not described
    * 1 point: The problem is described but shortly or not clearly 
    * 2 points: The problem is well described and it's clear what the problem the project solves
* Cloud
    * 0 points: Cloud is not used, things run only locally
    * 2 points: The project is developed on the cloud OR uses localstack (or similar tool) OR the project is deployed to Kubernetes or similar container management platforms
    * 4 points: The project is developed on the cloud and IaC tools are used for provisioning the infrastructure
* Experiment tracking and model registry
    * 0 points: No experiment tracking or model registry
    * 2 points: Experiments are tracked or models are registered in the registry
    * 4 

## Key concepts

- [Model Registry](/course-wiki/model-registry/)
- [Experiment Tracking](/course-wiki/experiment-tracking/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [CI/CD](/course-wiki/ci-cd/)
- [Deployment Automation](/course-wiki/deployment-automation/)
- [Model Deployment](/course-wiki/model-deployment/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [mlops-m02-experiment-tracking-intro](/course-wiki/mlops-m02-experiment-tracking-intro/)
- [mlops-m02-experiment-tracking-with-mlflow](/course-wiki/mlops-m02-experiment-tracking-with-mlflow/)
- [mlops-m02-homework](/course-wiki/mlops-m02-homework/)
- [mlops-m02-model-registry](/course-wiki/mlops-m02-model-registry/)
- [mlops-m03-homework](/course-wiki/mlops-m03-homework/)
- [mlops-m03-using-an-orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
- [mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
- [mlops-m04-optional-streaming-deploying-models-with-kinesis](/course-wiki/mlops-m04-optional-streaming-deploying-models-with-kinesis/)
- [mlops-m04-three-ways-of-deploying-a-model](/course-wiki/mlops-m04-three-ways-of-deploying-a-model/)
- [mlops-m04-web-services-deploying-models-with-flask-and-doc](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
- [mlops-m04-web-services-getting-the-models-from-the-model-r](/course-wiki/mlops-m04-web-services-getting-the-models-from-the-model-r/)
- [mlops-m05-data-quality-monitoring](/course-wiki/mlops-m05-data-quality-monitoring/)
- [mlops-m05-debugging-with-test-suites-and-reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
- [mlops-m05-dummy-monitoring](/course-wiki/mlops-m05-dummy-monitoring/)
- [mlops-m05-evidently-monitoring-dashboard](/course-wiki/mlops-m05-evidently-monitoring-dashboard/)
- [mlops-m05-intro-to-ml-monitoring](/course-wiki/mlops-m05-intro-to-ml-monitoring/)
- [mlops-m06-homework](/course-wiki/mlops-m06-homework/)

## Sources

- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/07-project/README.md)
