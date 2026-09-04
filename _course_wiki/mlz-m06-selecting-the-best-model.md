---
title: "Selecting the best model — Machine Learning Zoomcamp Module 6"
summary: "We select the final model from decision tree, random forest, or xgboost based on the best auc scores. After that we prepare the `df_full_train` and `df_test` to train and evaluate the final model. If there is not much difference between model auc sco"
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › Selecting the best model

## Notes

We select the final model from decision tree, random forest, or xgboost based on the best auc scores. After that we prepare the `df_full_train` and `df_test` to train and evaluate the final model. If there is not much difference between model auc scores on the train as well as test data then the model has generalized the patterns well enough.

Generally, XGBoost models perform better on tabular data than other machine learning models but the downside is that these model are easy to overfit cause of the high number of hyperparameter. Therefore, XGBoost models require a lot more attention for parameters tuning to optimize them.

Add notes from the video (PRs are welcome)

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/29/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-14/)

## Key concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Classification Metrics](/course-wiki/classification-metrics/)
- [Decision Trees](/course-wiki/decision-trees/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m02-car-price-prediction-project](/course-wiki/mlz-m02-car-price-prediction-project/)
- [mlz-m02-computing-rmse-on-validation-data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
- [mlz-m02-feature-engineering](/course-wiki/mlz-m02-feature-engineering/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)
- [mlz-m04-evaluation-metrics-session-overview](/course-wiki/mlz-m04-evaluation-metrics-session-overview/)
- [mlz-m04-explore-more](/course-wiki/mlz-m04-explore-more/)
- [mlz-m04-precision-and-recall](/course-wiki/mlz-m04-precision-and-recall/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m04-summary](/course-wiki/mlz-m04-summary/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-data-cleaning-and-preparation](/course-wiki/mlz-m06-data-cleaning-and-preparation/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-explore-more](/course-wiki/mlz-m06-explore-more/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)

## Sources

- [Video](https://www.youtube.com/watch?v=lqdnyIVQq-M&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/09-final-model.md)
