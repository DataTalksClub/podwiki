---
title: "Decision Trees"
summary: "The if-else style model behind random forests: learning split rules from data."
related_course:
  - Gradient Boosting
  - Logistic Regression
  - Classification Metrics
  - Neural Networks
---

Module 6 opens ensemble learning with decision trees: models that partition the feature space with learned split rules, choosing splits that best separate the target. A single tree overfits easily — it can memorize the training set — so the module treats it mainly as a building block.

The practical work trains trees with scikit-learn, reads feature importance from the fitted model, and then combines many trees two ways: bagging into random forests, and boosting with XGBoost. Hyperparameter tuning (max depth, min samples per leaf) against a validation set decides how deep the trees grow.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) — Module 6: Decision Trees and Ensemble Learning

## Related concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Logistic Regression](/course-wiki/logistic-regression/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Neural Networks](/course-wiki/neural-networks/)
