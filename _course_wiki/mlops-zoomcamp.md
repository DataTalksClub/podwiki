---
layout: wiki
title: "MLOps Zoomcamp"
summary: "DataTalks.Club's free MLOps course: experiment tracking, orchestration, deployment, monitoring, and engineering best practices around one NY Taxi use case."
related_course:
  - Zoomcamps
  - Machine Learning Zoomcamp
related:
  - MLOps
  - MLOps Roadmap
  - Experiment Tracking
  - Model Registry
  - Model Monitoring
  - Orchestration
  - CI/CD
  - MLOps Tools
---

MLOps Zoomcamp is DataTalks.Club's free course on productionizing machine
learning services. It teaches the fundamentals of MLOps — experiment
tracking, orchestration, deployment, and monitoring — through structured
modules, hands-on workshops, and a final project that wires everything into
one end-to-end pipeline. The running example is the NY Taxi dataset.

All materials are open source in the
[course repository](https://github.com/DataTalksClub/mlops-zoomcamp), with
videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK)
and a [course FAQ](https://datatalks.club/faq/mlops-zoomcamp.html). It is part
of the [Zoomcamps](/course-wiki/zoomcamps/) family and builds directly on
[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/).

## Curriculum

The [repository syllabus](https://github.com/DataTalksClub/mlops-zoomcamp)
maps the modules:

- **Introduction** — what MLOps is, the MLOps maturity model, and why it is
  essential ([MLOps](/wiki/mlops/)).
- **Experiment tracking and model management** — MLflow basics, model saving
  and loading, and the model registry ([Experiment Tracking](/wiki/experiment-tracking/),
  [Model Registry](/wiki/model-registry/)).
- **Orchestration and ML pipelines** — workflow orchestration
  ([Orchestration](/wiki/orchestration/)).
- **Model deployment** — online versus offline strategies: web services with
  Flask, streaming with AWS Kinesis and Lambda, and batch scoring
  ([LLM Deployment](/wiki/llm-deployment/) covers the LLM analog of the same serving decisions).
- **Model monitoring** — web service monitoring with Prometheus, Evidently,
  and Grafana; batch job monitoring with Prefect, MongoDB, and Evidently
  ([Model Monitoring](/wiki/model-monitoring/)).
- **Best practices** — unit and integration testing, linting and pre-commit
  hooks, CI/CD with GitHub Actions, and infrastructure as code with Terraform
  ([CI/CD](/wiki/ci-cd/)).
- **Final project** — an end-to-end MLOps pipeline integrating every module.

## Who it is for

The course targets data scientists, ML engineers, and software engineers who
need to put models into production and operate them reliably. Prerequisites
are real: Python, Docker basics, command-line comfort, prior machine learning
experience (for example through ML Zoomcamp), and about a year of
programming. The course is currently self-paced only — no live cohort is
scheduled for 2026, so certificates are paused until one runs again.

## What the podcast adds

MLOps Zoomcamp appears in expert learning advice on the podcast. In a
discussion of pragmatic, standardized MLOps practice, hands-on projects plus
the MLOps Zoomcamp come up as the recommended path into the discipline,
paired with the skill balance of ML fundamentals plus software engineering
and system design.
[Pragmatic MLOps](https://datatalks.club/podcast/pragmatic-and-standardized-mlops.html)
The same discussion covers how central MLOps support operates across brands,
which mirrors the course's platform-first framing.

For how the pieces fit on the job, the [MLOps Roadmap](/wiki/mlops-roadmap/) sequences the
maturity steps the course's module 1 introduces, and [MLOps Tools](/wiki/mlops-tools/) maps the
tool categories MLflow, Prometheus, Evidently, and Terraform belong to.
[Production ML Checklist](/wiki/production-ml-project-checklist/) turns the final project's requirements into a
review gate for production readiness.

## Related Pages

- [Zoomcamps](/course-wiki/zoomcamps/)
- [MLOps](/wiki/mlops/)
- [MLOps Roadmap](/wiki/mlops-roadmap/)
- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
- [Experiment Tracking](/wiki/experiment-tracking/)
- [Model Registry](/wiki/model-registry/)
- [Model Monitoring](/wiki/model-monitoring/)
- [CI/CD](/wiki/ci-cd/)
