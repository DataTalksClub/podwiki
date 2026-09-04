---
schema_type: Course
title: "Zoomcamps"
summary: "The DataTalks.Club Zoomcamps: free, open-source cohort courses covering machine learning, data engineering, MLOps, LLM engineering, AI developer tools, and stock market analytics."
related_course:
  - Machine Learning Zoomcamp
  - Data Engineering Zoomcamp
  - MLOps Zoomcamp
  - LLM Zoomcamp
  - AI Dev Tools Zoomcamp
  - Stock Markets Analytics Zoomcamp
---

The Zoomcamps are the free, open-source course family run by DataTalks.Club.
Each course covers one role-shaped slice of the data and AI stack — machine
learning engineering, data engineering, MLOps, LLM engineering, AI-assisted
software development, and stock market analytics — through pre-recorded videos,
homework, and an end-to-end project. All materials live in public GitHub
repositories, and every course can be taken self-paced at any time.

The portfolio grew from the first
[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
into a family covering Machine Learning, Data Engineering, MLOps, LLMs, Stock
Analytics, and AI Dev Tools. This wiki is the course knowledge layer: each
course has a page with its module map, and the concepts taught across the
courses are extracted into their own pages and linked together.

## The shared course model

Every Zoomcamp follows the same operating model:

- Lectures are pre-recorded and free; materials and homework live in the
  course repository.
- A live cohort adds shared deadlines, scored homework, a leaderboard, peer
  review, and certificate eligibility. There are no live classes.
- Self-paced learners can start anytime and use everything for free, but
  certificates require a live cohort.
- Every course ends in a project: the midterm/capstone pattern in the longer
  courses, a final project in the rest. Projects are peer-reviewed.
- Learning in public (blogging, posting progress) earns bonus points toward
  homework and project scores.

## The courses

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — from
  regression and classification to deploying models as web services with
  FastAPI, Docker, Kubernetes, and AWS Lambda.
  [Materials](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- [Data Engineering Zoomcamp](/course-wiki/data-engineering-zoomcamp/) — an
  end-to-end pipeline built from scratch with Docker, Terraform, Kestra,
  BigQuery, dbt, Spark, and Kafka.
  [Materials](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) — experiment tracking,
  orchestration, deployment, monitoring, and best practices around one NY Taxi
  use case.
  [Materials](https://github.com/DataTalksClub/mlops-zoomcamp)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/) — building production LLM
  applications with agentic RAG, vector search, evaluation, and monitoring.
  [Materials](https://github.com/DataTalksClub/llm-zoomcamp)
- [AI Dev Tools Zoomcamp](/course-wiki/ai-dev-tools-zoomcamp/) — AI-native
  software engineering: coding agents, context engineering, MCP, tests, CI/CD,
  deployment, and observability for AI-built apps.
  [Materials](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
  — financial data analysis and trading strategy simulation with pandas,
  time-series models, and automation, run with PythonInvest.
  [Materials](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp)

## Concept glossary

Every concept taught across the courses is extracted into its own page, and
each concept page links the exact units (modules and lessons) that cover it.
Start from the [Concept Glossary](/course-wiki/concepts/) to find where a
concept is taught.

## Shared concepts across courses

The courses reuse each other's foundations, and the concept pages in this wiki
link them together:

- [Docker](/course-wiki/docker/) appears in Machine Learning (packaging model
  services), Data Engineering (pipeline components), MLOps (deployment and
  integration testing), and AI Dev Tools (containerizing apps).
- [Workflow orchestration](/course-wiki/workflow-orchestration/) is taught with
  Kestra in Data Engineering and LLM Zoomcamp, and with Prefect in MLOps
  Zoomcamp.
- [dlt](/course-wiki/dlt/) data ingestion appears in both the Data Engineering
  and LLM Zoomcamp workshops.
- [FastAPI](/course-wiki/fastapi/) serves models in Machine Learning Zoomcamp
  and backs the full-stack app in AI Dev Tools Zoomcamp.
- [CI/CD](/course-wiki/ci-cd/) with GitHub Actions closes out MLOps Zoomcamp
  best practices and the AI Dev Tools deployment pipeline.
