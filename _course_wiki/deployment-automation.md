---
title: "Deployment Automation"
summary: "From Colab notebooks to scheduled Python: files, SQLite storage, cron, and Airflow."
related_course:
  - Backtesting
  - Trading Strategy
  - Workflow Orchestration
  - Pandas
  - Market Data APIs
---

Module 5 closes the loop from analysis to operation. Notebooks become Python files; prediction outputs get persistent storage (files or a simple SQLite database, with an SQL introduction); and the whole prediction pipeline runs on a schedule — cron for a series of scripts, with Apache Airflow introduced as the workflow-level alternative.

The automation target is the full cycle: download fresh data, compute indicators, generate predictions, execute or log the trades the strategy calls for — systematically, on schedule, without a human opening a notebook. An optional track adds email notifications with predictions and profit/loss updates.

## Taught in

- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/) — Module 5: Deployment and Automation

## Related concepts

- [Backtesting](/course-wiki/backtesting/)
- [Trading Strategy](/course-wiki/trading-strategy/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Pandas](/course-wiki/pandas/)
- [Market Data APIs](/course-wiki/market-data-apis/)
