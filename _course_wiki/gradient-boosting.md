---
title: "Gradient Boosting"
summary: "Training trees sequentially on errors — the XGBoost technique ML Zoomcamp teaches for tabular prediction."
related_course:
  - Decision Trees
  - Classification Metrics
  - Regularization
  - Linear Regression
---

Gradient boosting trains an ensemble one tree at a time, with each new tree predicting what the ensemble so far gets wrong. Module 6 uses XGBoost for the practical work: monitoring training and validation error during boosting, tuning the learning rate, tree depth, and number of estimators, and reading feature importance from the final ensemble.

The module positions boosted trees as the strongest general-purpose model for tabular data in the course, and the capstone projects commonly use them. The evaluation discipline is the same as the rest of the course: tune against validation, report once on test.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 6: Decision Trees and Ensemble Learning

## Related concepts

- [Decision Trees](/course-wiki/decision-trees/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Regularization](/course-wiki/regularization/)
- [Linear Regression](/course-wiki/linear-regression/)
