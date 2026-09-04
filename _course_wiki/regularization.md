---
title: "Regularization"
summary: "Constraining model weights so redundant or noisy features cannot destabilize predictions."
related_course:
  - Agentic RAG
  - Classification Metrics
  - Function Calling
  - Gradient Boosting
  - Linear Regression
  - Logistic Regression
---

In Machine Learning Zoomcamp, regularization means adding a penalty on the size of the weights to the training objective. When features carry similar information (for example, duplicate car specifications), unregularized linear regression can push weights to large opposite values that cancel out — the model fits the training data but generalizes badly.

The course shows ridge-style weight control implemented by hand in the normal-equation solution, and the same idea carries into logistic regression in the classification module. The regularization parameter is tuned against the validation set, which is the module's repeated lesson: model settings are selected on held-out data, never on the test set.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 2: Machine Learning for Regression](/course-wiki/mlz-module-02/)
    - [Car price prediction project](/course-wiki/mlz-m02-car-price-prediction-project/)
    - [Regularization](/course-wiki/mlz-m02-regularization/)
    - [Tuning the model](/course-wiki/mlz-m02-tuning-the-model/)
    - [Car price prediction project summary](/course-wiki/mlz-m02-car-price-prediction-project-summary/)
  - [Module 3: Machine Learning for Classification](/course-wiki/mlz-module-03/)
    - [Explore more](/course-wiki/mlz-m03-explore-more/)
  - [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/)
    - [XGBoost parameter tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
  - [Module 8: Neural Networks and Deep Learning](/course-wiki/mlz-module-08/)
    - [Fashion classification](/course-wiki/mlz-m08-fashion-classification/)
    - [Regularization and dropout](/course-wiki/mlz-m08-regularization-and-dropout/)
## Related concepts

- [Linear Regression](/course-wiki/linear-regression/)
- [Logistic Regression](/course-wiki/logistic-regression/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
