---
title: "Homework — MLOps Zoomcamp Module 6"
summary: "### Infrastructure-as-Code with Terraform"
related_course:
  - mlops-module-06
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 6: Best Practices](/course-wiki/mlops-module-06/) › Homework

## Notes

More information here.

<br>

## Part B

### Infrastructure-as-Code
with Terraform 

!image

#### Summary
* Setting up a stream-based pipeline infrastructure in AWS, using Terraform
* Project infrastructure modules (AWS): Kinesis Streams (Producer & Consumer), Lambda (Serving API), S3 Bucket (Model artifacts), ECR (Image Registry)

Further info here:
* Concepts of IaC and Terraform
* [Setup and Execution](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/06-best-practices/code#iac)

#### 6B.1: Terraform - Introduction

https://www.youtube.com/watch?v=zRcLgT7Qnio&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=48

* Introduction
* Setup & Pre-Reqs
* Concepts of Terraform and IaC (reference material from previous courses)

#### 6B.2: Terraform - Modules and Outputs variables

https://www.youtube.com/watch?v=-6scXrFcPNk&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=49

* What are they?
* Creating a Kinesis module

#### 6B.3: Build an e2e workflow for Ride Predictions

https://www.youtube.com/watch?v=JVydd1K6R7M&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=50

* TF resources for ECR, Lambda, S3

#### 6B.4: Test the pipeline e2e

https://www.youtube.com/watch?v=YWao0rnqVoI&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=51

* Demo: apply TF to our use-case, manually deploy data dependencies & test
* Recap: IaC, Terraform, next steps

Additional material on understanding Terraform concepts here: Reference Material

<br>

### CI/CD
with GitHub Actions

!image

#### Summary

* Automate a complete CI/CD pipeline using GitHub Actions to automatically trigger jobs 
to build, test, and deploy our service to Lambda for every new commit/code change to our repository.
* The goal of our CI/CD pipeline is to execute tests, build and push container image to a registry,
and update our lambda service for every commit to the GitHub repository.

Further info here: Concepts of CI/CD and GitHub Actions

#### 6B.5: CI/CD - Introduction

https://www.youtube.com/watch?v=OMwwZ0Z_cdk&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=52

* Architecture (Ride Predictions)
* What are GitHub Workflows?

#### 6B.6: Continuous Integration

https://www.youtube.com/watch?v=xkTWF9c33mU&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=53

* `ci-tests.yml`
    * Automate sections from tests: Env setup, Unit test, Integration test, Terraform plan
    * Create a CI workflow to trigger on `pull-request` to `develop` branch
    * Execute demo

#### 6B.7: Continuous Delivery

https://www.youtube.com/watch?v=jCNxqXCKh2s&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=54

* `cd-deploy.yml`
    * Automate sections from tests: Terraform plan, Terraform apply, Docker build & ECR push, Update Lambda config
    * Create a CD workflow to trigger on `push` to `develop` branch
    * Execute demo

#### Alternative CICD Solutions

* Using args and env variables in docker image, and leveraging makefile commands in cicd
    * Check the repo [README](https://github.com/Nakulbajaj101/mlops-zoomcamp/blob/main/06-best-practices/code-practice/README.md)
    * Using the args [Dockerfile](https://github.com/Nakulbajaj101/mlops-zoomcamp/blob/main/06-best-practices/code-practice/Dockerfile)
    * Using build args [ECR terraform](https://github.com/Nakulbajaj101/mlops-zoomcamp/blob/main/06-best-practices/code-practice/deploy/modules/ecr/main.tf)
    * Updating lambda env variables [Post deploy](https://github.com/Nakulbajaj101/mlops-zoomcamp/blob/main/06-best-practices/code-practice/deploy/run_apply_local.sh

## Key concepts

- [Docker](/course-wiki/docker/)
- [Terraform](/course-wiki/terraform/)
- [CI/CD](/course-wiki/ci-cd/)
- [Deployment Automation](/course-wiki/deployment-automation/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlops-m01-2-vm-in-aws](/course-wiki/mlops-m01-2-vm-in-aws/)
- [mlops-m01-homework](/course-wiki/mlops-m01-homework/)
- [mlops-m02-homework](/course-wiki/mlops-m02-homework/)
- [mlops-m03-homework](/course-wiki/mlops-m03-homework/)
- [mlops-m03-using-an-orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
- [mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
- [mlops-m04-optional-streaming-deploying-models-with-kinesis](/course-wiki/mlops-m04-optional-streaming-deploying-models-with-kinesis/)
- [mlops-m04-three-ways-of-deploying-a-model](/course-wiki/mlops-m04-three-ways-of-deploying-a-model/)
- [mlops-m04-web-services-deploying-models-with-flask-and-doc](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
- [mlops-m05-debugging-with-test-suites-and-reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
- [mlops-m06-code-quality-linting-and-formatting](/course-wiki/mlops-m06-code-quality-linting-and-formatting/)
- [mlops-m06-git-pre-commit-hooks](/course-wiki/mlops-m06-git-pre-commit-hooks/)
- [mlops-m06-integration-tests-with-docker-compose](/course-wiki/mlops-m06-integration-tests-with-docker-compose/)
- [mlops-m06-makefiles-and-make](/course-wiki/mlops-m06-makefiles-and-make/)
- [mlops-m06-testing-cloud-services-with-localstack](/course-wiki/mlops-m06-testing-cloud-services-with-localstack/)
- [mlops-m06-testing-python-code-with-pytest](/course-wiki/mlops-m06-testing-python-code-with-pytest/)
- [mlops-m07-course-project](/course-wiki/mlops-m07-course-project/)

## Sources

- [Video](https://www.youtube.com/watch?v=zRcLgT7Qnio&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=48)
- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/06-best-practices/README.md)
