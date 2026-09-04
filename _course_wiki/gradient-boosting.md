---
title: "Gradient Boosting"
summary: "Training trees sequentially on errors — the XGBoost technique ML Zoomcamp teaches for tabular prediction."
related_course:
  - Classification Metrics
  - Decision Trees
  - Linear Regression
  - Logistic Regression
  - Neural Networks
  - Regularization
  - Transfer Learning
---

Gradient boosting trains an ensemble one tree at a time, with each new tree predicting what the ensemble so far gets wrong. Module 6 uses XGBoost for the practical work: monitoring training and validation error during boosting, tuning the learning rate, tree depth, and number of estimators, and reading feature importance from the final ensemble.

The module positions boosted trees as the strongest general-purpose model for tabular data in the course, and the capstone projects commonly use them. The evaluation discipline is the same as the rest of the course: tune against validation, report once on test.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [Setting up the Environment](/course-wiki/mlz-m01-setting-up-the-environment/)
  - [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/)
    - [Summary](/course-wiki/mlz-m05-summary/)
  - [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/)
    - [Gradient boosting and XGBoost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
    - [XGBoost parameter tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
    - [Selecting the best model](/course-wiki/mlz-m06-selecting-the-best-model/)
    - [Summary](/course-wiki/mlz-m06-summary/)
  - [Module 8: Neural Networks and Deep Learning](/course-wiki/mlz-module-08/)
    - [Transfer learning](/course-wiki/mlz-m08-transfer-learning/)
  - [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/)
    - [Explore more](/course-wiki/mlz-m09-explore-more/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 1: Agentic RAG](/course-wiki/llmz-module-01/)
    - [Search](/course-wiki/llmz-m01-search/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [Evaluating Retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
## Related concepts

- [Decision Trees](/course-wiki/decision-trees/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Regularization](/course-wiki/regularization/)
- [Linear Regression](/course-wiki/linear-regression/)
