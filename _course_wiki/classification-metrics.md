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

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 2: Machine Learning for Regression](/course-wiki/mlz-module-02/)
    - [Car price prediction project](/course-wiki/mlz-m02-car-price-prediction-project/)
    - [Root Mean Squared Error (RMSE)](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
    - [Computing RMSE on validation data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
    - [Feature engineering](/course-wiki/mlz-m02-feature-engineering/)
    - [Using the model](/course-wiki/mlz-m02-using-the-model/)
  - [Module 4: Evaluation Metrics for Classification](/course-wiki/mlz-module-04/)
    - [Evaluation metrics: session overview](/course-wiki/mlz-m04-evaluation-metrics-session-overview/)
    - [Precision and Recall](/course-wiki/mlz-m04-precision-and-recall/)
    - [ROC Curves](/course-wiki/mlz-m04-roc-curves/)
    - [ROC AUC](/course-wiki/mlz-m04-roc-auc/)
    - [Summary](/course-wiki/mlz-m04-summary/)
    - [Explore more](/course-wiki/mlz-m04-explore-more/)
  - [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/)
    - [Decision trees parameter tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
    - [XGBoost parameter tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
    - [Selecting the best model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 2: Vector Search](/course-wiki/llmz-module-02/)
    - [Vector Search with sqlitesearch](/course-wiki/llmz-m02-vector-search-with-sqlitesearch/)
  - [Module 4: Evaluation](/course-wiki/llmz-module-04/)
    - [Search Evaluation Metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
    - [Next Steps](/course-wiki/llmz-m04-next-steps/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 1: Introduction](/course-wiki/mlops-module-01/)
    - [Homework](/course-wiki/mlops-m01-homework/)
## Related concepts

- [Logistic Regression](/course-wiki/logistic-regression/)
- [Regularization](/course-wiki/regularization/)
- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)
- [Neural Networks](/course-wiki/neural-networks/)
