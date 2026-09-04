---
title: "XGBoost parameter tuning — Machine Learning Zoomcamp Module 6"
summary: "XGBoost has various tunable parameters but the three most important ones are:"
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › XGBoost parameter tuning

## Notes

XGBoost has various tunable parameters but the three most important ones are:

- `eta` (default=0.3)
  - It is also called `learning_rate` and is used to prevent overfitting by regularizing the weights of new features in each boosting step. range: [0, 1]
- `max_depth` (default=6)
  - Maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit. range: [0, inf]
- `min_child_weight` (default=1)
  - Minimum number of samples in leaf node. range: [0, inf]

For XGBoost models, there are other ways of finding the best parameters as well but the one we implement in the notebook follows the sequence of:

- First find the best value for `eta`
- Second, find the best value for `max_depth`
- Third, find the best value for `min_child_weight`

Other useful parameter are:

- `subsample` (default=1)
  - Subsample ratio of the training instances. Setting it to 0.5 means that model would randomly sample half of the training data prior to growing trees. range: (0, 1]
- `colsample_bytree` (default=1)
  - This is similar to random forest, where each tree is made with the subset of randomly choosen features.
- `lambda` (default=1)
  - Also called `reg_lambda`. L2 regularization term on weights. Increasing this value will make model more conservative.
- `alpha` (default=0)
  - Also called `reg_alpha`. L1 regularization term on weights. Increasing this value will make model more conservative.

### Alternative: Tuning XGBoost using a loop

Instead of repeating the training process manually for each `eta` value, you can use a loop to automate it (and other parameters to be tuned):
```python
# Train XGBoost models for each eta and store AUC results
scores = {} # dictionary to store results for each eta
etas = [0.01, 0.05, 0.1, 0.3, 1.0] # list of parameter values. in this case it is 'eta'.

for eta in etas:
    evals_result = {}

    xgb_params = {
        'eta': eta,
        'max_depth': 6,
        'min_child_weight': 1,

        'objective': 'binary:logistic',
        'eval_metric': 'auc',

        'nthread': 8,
        'seed': 1,
        'verbosity': 1
    }

    model = xgb.train(
        xgb_params,
        dtrain,
        evals=watchlist,
        verbose_eval=0,
        num_boost_round=200,
        evals_result=evals_result
    )

    columns = ['iter', 'train_auc', 'val_auc']
    train_aucs = list(evals_result['train'].values())[0]
    val_aucs = list(evals_result['val'].values())[0]

    df_results = pd.DataFrame(
        list(zip(range(1, len(train_aucs) + 1), train_aucs, val_aucs)),
        columns=columns
    )

    key = f'eta={eta}'
    scores[key] = df_results
```

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/27/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-12/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/28/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-13/)

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
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)

## Sources

- [Video](https://www.youtube.com/watch?v=VX6ftRzYROM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/08-xgb-tuning.md)
