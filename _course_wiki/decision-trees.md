---
title: "Decision Trees"
summary: "The if-else style model behind random forests: learning split rules from data."
related_course:
  - Classification Metrics
  - Gradient Boosting
  - Logistic Regression
  - Neural Networks
  - Spark
  - Spec-Driven Development
---

Module 6 opens ensemble learning with decision trees: models that partition the feature space with learned split rules, choosing splits that best separate the target. A single tree overfits easily — it can memorize the training set — so the module treats it mainly as a building block.

The practical work trains trees with scikit-learn, reads feature importance from the fitted model, and then combines many trees two ways: bagging into random forests, and boosting with XGBoost. Hyperparameter tuning (max depth, min samples per leaf) against a validation set decides how deep the trees grow.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/)
    - [Model Selection Process](/course-wiki/mlz-m01-model-selection-process/)
  - [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/)
    - [Summary](/course-wiki/mlz-m05-summary/)
  - [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/)
    - [Credit risk scoring project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
    - [Decision trees](/course-wiki/mlz-m06-decision-trees/)
    - [Decision tree learning algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
    - [Decision trees parameter tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
    - [Ensemble learning and random forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
    - [Gradient boosting and XGBoost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
    - [XGBoost parameter tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
    - [Selecting the best model](/course-wiki/mlz-m06-selecting-the-best-model/)
    - [Summary](/course-wiki/mlz-m06-summary/)
## Related concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Logistic Regression](/course-wiki/logistic-regression/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Neural Networks](/course-wiki/neural-networks/)
