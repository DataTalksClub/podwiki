---
title: "Setting up the validation framework — Machine Learning Zoomcamp Module 3"
summary: "Splitting the dataset with Scikit-Learn."
related_course:
  - mlz-module-03
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 3: Machine Learning for Classification](/course-wiki/mlz-module-03/) › Setting up the validation framework

## Notes

Splitting the dataset with **Scikit-Learn**. 

**Classes, functions, and methods:** 

* `train_test_split` - Scikit-Learn class for splitting a dataset into two parts. The `test_size` argument states how large the test set should be. The `random_state` argument sets a random seed for reproducibility purposes.  
* `df.reset_index(drop=True)` - reset the indices of a dataframe and delete the previous ones. 
* `df.x.values` - extract the values from x series
* `del df['x']` - delete x series from a dataframe 

The entire code of this project is available in [this jupyter notebook](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/03-classification/notebook.ipynb).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/27/ml-zoomcamp-2023-machine-learning-for-classification-part-3/)

## Key concepts

- [Pandas](/course-wiki/pandas/)
- [scikit-learn](/course-wiki/scikit-learn/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

## Related notes

- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-linear-algebra-refresher](/course-wiki/mlz-m01-linear-algebra-refresher/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m02-baseline-model-for-car-price-prediction-project](/course-wiki/mlz-m02-baseline-model-for-car-price-prediction-project/)
- [mlz-m02-categorical-variables](/course-wiki/mlz-m02-categorical-variables/)
- [mlz-m02-computing-rmse-on-validation-data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
- [mlz-m02-data-preparation](/course-wiki/mlz-m02-data-preparation/)
- [mlz-m02-exploratory-data-analysis](/course-wiki/mlz-m02-exploratory-data-analysis/)
- [mlz-m02-explore-more](/course-wiki/mlz-m02-explore-more/)
- [mlz-m02-feature-engineering](/course-wiki/mlz-m02-feature-engineering/)
- [mlz-m02-linear-regression](/course-wiki/mlz-m02-linear-regression/)
- [mlz-m02-linear-regression-vector-form](/course-wiki/mlz-m02-linear-regression-vector-form/)
- [mlz-m02-regularization](/course-wiki/mlz-m02-regularization/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-setting-up-the-validation-framework](/course-wiki/mlz-m02-setting-up-the-validation-framework/)
- [mlz-m02-training-linear-regression-normal-equation](/course-wiki/mlz-m02-training-linear-regression-normal-equation/)
- [mlz-m02-tuning-the-model](/course-wiki/mlz-m02-tuning-the-model/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)
- [mlz-m03-churn-prediction-project](/course-wiki/mlz-m03-churn-prediction-project/)
- [mlz-m03-data-preparation](/course-wiki/mlz-m03-data-preparation/)
- [mlz-m03-eda](/course-wiki/mlz-m03-eda/)
- [mlz-m03-explore-more](/course-wiki/mlz-m03-explore-more/)
- [mlz-m03-feature-importance-churn-rate-and-risk-ratio](/course-wiki/mlz-m03-feature-importance-churn-rate-and-risk-ratio/)
- [mlz-m03-feature-importance-correlation](/course-wiki/mlz-m03-feature-importance-correlation/)
- [mlz-m03-feature-importance-mutual-information](/course-wiki/mlz-m03-feature-importance-mutual-information/)
- [mlz-m03-logistic-regression](/course-wiki/mlz-m03-logistic-regression/)
- [mlz-m03-model-interpretation](/course-wiki/mlz-m03-model-interpretation/)
- [mlz-m03-one-hot-encoding](/course-wiki/mlz-m03-one-hot-encoding/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m03-using-the-model](/course-wiki/mlz-m03-using-the-model/)
- [mlz-m04-accuracy-and-dummy-model](/course-wiki/mlz-m04-accuracy-and-dummy-model/)
- [mlz-m04-confusion-table](/course-wiki/mlz-m04-confusion-table/)
- [mlz-m04-cross-validation](/course-wiki/mlz-m04-cross-validation/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m04-summary](/course-wiki/mlz-m04-summary/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m06-data-cleaning-and-preparation](/course-wiki/mlz-m06-data-cleaning-and-preparation/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-installation-of-tensorflow](/course-wiki/mlz-m08-installation-of-tensorflow/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)

## Sources

- [Video](https://www.youtube.com/watch?v=_lwz34sOnSE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/03-classification/03-validation.md)
