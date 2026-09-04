---
title: "Gradient boosting and XGBoost — Machine Learning Zoomcamp Module 6"
summary: "Unlike Random Forest where each decision tree trains independently, in the Gradient Boosting Trees, the models are combined sequentially, where each model takes the prediction errors made by the previous model and then tries to improve the prediction"
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › Gradient boosting and XGBoost

## Notes

**Gradient Boosting**

Unlike Random Forest where each decision tree trains independently, in the Gradient Boosting Trees, the models are combined sequentially, where each model takes the prediction errors made by the previous model and then tries to improve the prediction. This process continues to `n` number of iterations, and in the end, all the predictions get combined to make the final prediction.

XGBoost is one of the libraries which implements the gradient boosting technique. To make use of the library, we need to install with `pip install xgboost`. To train and evaluate the model, we need to wrap our train and validation data into a special data structure from XGBoost which is called `DMatrix`. This data structure is optimized to train XGBoost models faster.

**XGBoost Training Parameters**

*   `eta`: learning rate, which indicates how fast the model learns.
*   `max_depth`: to control the size of the trees.
*   `min_child_weight`: to control the minimum size of a child node.
*   `objective`: To specify which problem we are trying to solve, either regression, or classification (binary: `'binary:logistic'`, or other).
*   `nthread`: 8, used for parallelized training.
*   `seed`: 1, for reproducibility.
*   `verbosity`: 1 (`True`) to show warnings, if any, during model training.

**Classes, functions, and methods**:

- `xgb.train()`: method to train xgboost model.
- `xgb_params`: key-value pairs of hyperparameters to train xgboost model.
- `watchlist`: list to store training and validation data to evaluate the performance of the model after each training iteration. The list takes tuple of train and validation set from DMatrix wrapper, for example, `watchlist = [(dtrain, 'train'), (dval, 'val')]`.
- `%%capture output`: IPython magic command which captures the standard output and standard error of a cell.

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

- [Notes from Peter Ernicke](https://knowmledge.com/2023/10/25/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-10/)
- [Notes from Peter Ernicke](https://knowmledge.com/2023/10/26/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-11/)

### Extracting results from `xgb.train(..)`

In the video we use jupyter magic command `%%capture output` to extract the output of `xgb.train(..)` method.

Alternatively you can use the `evals_result` parameter of the `xgb.train(..)`. You can pass an empty dictionary in for this parameter and the train() method will populate it with the results. The result will be of type `OrderedDict` so we have to transform it to a dataframe. For this, `zip()` can help. Here's an example code snippet:

```python
evals_result = {}

model = xgb.train(params=xgb_params,
                  dtrain=dm_train,
                  num_boost_round=200,
                  verbose_eval=5,
                  evals=watchlist,
                  evals_result=evals_result)

columns = ['iter', 'train_auc', 'val_auc']
train_aucs = list(evals_result['train'].values())[0]
val_aucs = list(evals_result['val'].values())[0]

df_scores = pd.DataFrame(
    list(zip(
        range(1, len(train_aucs) + 1),
        train_aucs,
        val_aucs
    )), columns=columns)

plt.plot(df_scores.iter, df_scores.train_auc, label='train')
plt.plot(df_scores.iter, df_scores.val_auc, label='val')
plt.legend()
```

## Installing XGBoost on Mac

Some students reported problems with installing XGBoost on Mac.

When you run `pip install xgboost` and when you try to `import xgboost` in a script you might get an warning or error stating that libomp has not been installed and to run `brew install libomp` in the terminal.

Be careful: this will install a version of libomp that does not work with `xgboost`!

This shows in one of two ways after attempting to run `xgb.DMatrix(X_train, label=y_train, featu

## Key concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Decision Trees](/course-wiki/decision-trees/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-data-cleaning-and-preparation](/course-wiki/mlz-m06-data-cleaning-and-preparation/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-explore-more](/course-wiki/mlz-m06-explore-more/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)

## Sources

- [Video](https://www.youtube.com/watch?v=xFarGClszEM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/07-boosting.md)
