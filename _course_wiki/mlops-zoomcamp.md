---
title: "MLOps Zoomcamp"
summary: "DataTalks.Club's free MLOps course: experiment tracking, orchestration, deployment, monitoring, and engineering best practices around one NY Taxi use case."
related_course:
  - Zoomcamps
  - Machine Learning Zoomcamp
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
and a [course FAQ](https://datatalks.club/faq/mlops-zoomcamp.html). The course
is currently self-paced only — no live cohort is scheduled for 2026, so
certificates are paused until one runs again.

## Curriculum

- **Module 1: Introduction** — what MLOps is and the
  [MLOps maturity model](/course-wiki/mlops-maturity-model/).
- **Module 2: Experiment Tracking and Model Management** —
  [experiment tracking](/course-wiki/experiment-tracking/) with
  [MLflow](/course-wiki/mlflow/), model saving and loading, and the
  [model registry](/course-wiki/model-registry/).
- **Module 3: Orchestration and ML Pipelines** — turning the training notebook
  into a script and wrapping it in an orchestrator
  ([workflow orchestration](/course-wiki/workflow-orchestration/), e.g.
  Prefect or Airflow).
- **Module 4: Model Deployment** — the three deployment shapes:
  web services with Flask and [Docker](/course-wiki/docker/), streaming with
  AWS Kinesis and Lambda, and batch scoring
  ([model deployment](/course-wiki/model-deployment/)), pulling models from
  the [model registry](/course-wiki/model-registry/).
- **Module 5: Model Monitoring** — reference datasets and
  [Evidently](/course-wiki/evidently/) metrics and dashboards, web service
  monitoring with [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/),
  and batch job monitoring with Prefect, MongoDB, and Evidently
  ([model monitoring](/course-wiki/model-monitoring/)).
- **Module 6: Best Practices** — testing Python code with pytest, integration
  tests with docker-compose and LocalStack, linting and formatting, Git
  pre-commit hooks, [CI/CD](/course-wiki/ci-cd/) with GitHub Actions, and
  infrastructure as code with Terraform.
- **Final project** — an end-to-end MLOps pipeline integrating every module:
  tracked experiments, a training pipeline, a deployed model, monitoring, and
  best practices.

## Who it is for

The course targets data scientists, ML engineers, and software engineers who
need to put models into production and operate them reliably. Prerequisites
are real: Python, Docker basics, command-line comfort, prior machine learning
experience (for example through ML Zoomcamp), and about a year of
programming.
