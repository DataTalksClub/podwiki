---
title: "Classification Metrics"
summary: "Accuracy, precision, recall, F1, confusion matrices, ROC curves and AUC — and why accuracy alone misleads on imbalanced data."
related_course:
  - CRISP-DM
  - Decision Trees
  - Gradient Boosting
  - LLM Evaluation
  - Linear Regression
  - Logistic Regression
  - Neural Networks
  - Regularization
---

Module 4 confronts the class-imbalance problem: when 3% of customers churn, a model that predicts 'no churn' for everyone is 97% accurate and useless. The course builds the confusion matrix and derives precision (how many predicted churners actually churn) and recall (how many real churners were caught), then combines them into F1.

The second half covers threshold-independent evaluation: ROC curves, the area under them (AUC), and cross-validation to compare model variants reliably. The module's outcome is an evaluation workflow that matches the metric to the business decision — for churn, that is usually a precision-recall tradeoff at a chosen threshold.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 4: Evaluation Metrics for Classification

## Related concepts

- [Logistic Regression](/course-wiki/logistic-regression/)
- [Regularization](/course-wiki/regularization/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
- [Neural Networks](/course-wiki/neural-networks/)
