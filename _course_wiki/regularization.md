---
title: "Regularization"
summary: "Constraining model weights so redundant or noisy features cannot destabilize predictions."
related_course:
  - Linear Regression
  - Logistic Regression
  - Classification Metrics
  - Gradient Boosting
---

In Machine Learning Zoomcamp, regularization means adding a penalty on the size of the weights to the training objective. When features carry similar information (for example, duplicate car specifications), unregularized linear regression can push weights to large opposite values that cancel out — the model fits the training data but generalizes badly.

The course shows ridge-style weight control implemented by hand in the normal-equation solution, and the same idea carries into logistic regression in the classification module. The regularization parameter is tuned against the validation set, which is the module's repeated lesson: model settings are selected on held-out data, never on the test set.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Modules 2-3: Regression and Classification

## Related concepts

- [Linear Regression](/course-wiki/linear-regression/)
- [Logistic Regression](/course-wiki/logistic-regression/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
