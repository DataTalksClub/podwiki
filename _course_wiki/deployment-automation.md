---
title: "Deployment Automation"
summary: "From Colab notebooks to scheduled Python: files, SQLite storage, cron, and Airflow."
related_course:
  - Avro Schema Management
  - Backtesting
  - Market Data APIs
  - Pandas
  - Trading Strategy
  - Workflow Orchestration
---

Module 5 closes the loop from analysis to operation. Notebooks become Python files; prediction outputs get persistent storage (files or a simple SQLite database, with an SQL introduction); and the whole prediction pipeline runs on a schedule — cron for a series of scripts, with Apache Airflow introduced as the workflow-level alternative.

The automation target is the full cycle: download fresh data, compute indicators, generate predictions, execute or log the trades the strategy calls for — systematically, on schedule, without a human opening a notebook. An optional track adds email notifications with predictions and profit/loss updates.

## Taught in

- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 3: Orchestration](/course-wiki/llmz-module-03/)
    - [AI Orchestration](/course-wiki/llmz-m03-ai-orchestration/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/)
    - [Using an Orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
    - [Homework](/course-wiki/mlops-m03-homework/)
  - [Module 6: Best Practices](/course-wiki/mlops-module-06/)
    - [Homework](/course-wiki/mlops-m06-homework/)
  - [Module 07: Course Project](/course-wiki/mlops-module-07/)
    - [Course Project](/course-wiki/mlops-m07-course-project/)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
  - [Module 5: Deployment and Automation](/course-wiki/sma-module-05/)
    - [Deployment and Automation](/course-wiki/sma-m05-deployment-and-automation/)
## Related concepts

- [Backtesting](/course-wiki/backtesting/)
- [Trading Strategy](/course-wiki/trading-strategy/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Pandas](/course-wiki/pandas/)
- [Market Data APIs](/course-wiki/market-data-apis/)
