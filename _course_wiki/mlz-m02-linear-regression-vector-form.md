---
title: "Linear regression: vector form — Machine Learning Zoomcamp Module 2"
summary: "The formula of linear regression can be synthesized with the dot product between features and weights. The feature vector includes the bias term with an x value of one, such as ."
related_course:
  - mlz-module-02
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 2: Machine Learning for Regression](/course-wiki/mlz-module-02/) › Linear regression: vector form

## Notes

The formula of linear regression can be synthesized with the dot product between features and weights. The feature vector includes the *bias* term with an *x* value of one, such as $w_{0}^{x_{i0}},\ where\ x_{i0} = 1\ for\ w_0$.

When all the records are included, the linear regression can be calculated with the dot product between ***feature matrix*** and ***vector of weights***, obtaining the `y` vector of predictions. 

The entire code of this project is available in [this jupyter notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb).  

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.wordpress.com/2023/09/20/ml-zoomcamp-2023-machine-learning-for-regression-part-5/)

## Key concepts

- [Linear Regression](/course-wiki/linear-regression/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

## Related notes

- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-linear-algebra-refresher](/course-wiki/mlz-m01-linear-algebra-refresher/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m02-baseline-model-for-car-price-prediction-project](/course-wiki/mlz-m02-baseline-model-for-car-price-prediction-project/)
- [mlz-m02-car-price-prediction-project](/course-wiki/mlz-m02-car-price-prediction-project/)
- [mlz-m02-car-price-prediction-project-summary](/course-wiki/mlz-m02-car-price-prediction-project-summary/)
- [mlz-m02-categorical-variables](/course-wiki/mlz-m02-categorical-variables/)
- [mlz-m02-computing-rmse-on-validation-data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
- [mlz-m02-data-preparation](/course-wiki/mlz-m02-data-preparation/)
- [mlz-m02-exploratory-data-analysis](/course-wiki/mlz-m02-exploratory-data-analysis/)
- [mlz-m02-explore-more](/course-wiki/mlz-m02-explore-more/)
- [mlz-m02-feature-engineering](/course-wiki/mlz-m02-feature-engineering/)
- [mlz-m02-linear-regression](/course-wiki/mlz-m02-linear-regression/)
- [mlz-m02-regularization](/course-wiki/mlz-m02-regularization/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-setting-up-the-validation-framework](/course-wiki/mlz-m02-setting-up-the-validation-framework/)
- [mlz-m02-training-linear-regression-normal-equation](/course-wiki/mlz-m02-training-linear-regression-normal-equation/)
- [mlz-m02-tuning-the-model](/course-wiki/mlz-m02-tuning-the-model/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)
- [mlz-m03-data-preparation](/course-wiki/mlz-m03-data-preparation/)
- [mlz-m03-eda](/course-wiki/mlz-m03-eda/)
- [mlz-m03-explore-more](/course-wiki/mlz-m03-explore-more/)
- [mlz-m03-feature-importance-churn-rate-and-risk-ratio](/course-wiki/mlz-m03-feature-importance-churn-rate-and-risk-ratio/)
- [mlz-m03-feature-importance-correlation](/course-wiki/mlz-m03-feature-importance-correlation/)
- [mlz-m03-feature-importance-mutual-information](/course-wiki/mlz-m03-feature-importance-mutual-information/)
- [mlz-m03-logistic-regression](/course-wiki/mlz-m03-logistic-regression/)
- [mlz-m03-model-interpretation](/course-wiki/mlz-m03-model-interpretation/)
- [mlz-m03-one-hot-encoding](/course-wiki/mlz-m03-one-hot-encoding/)
- [mlz-m03-setting-up-the-validation-framework](/course-wiki/mlz-m03-setting-up-the-validation-framework/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m04-accuracy-and-dummy-model](/course-wiki/mlz-m04-accuracy-and-dummy-model/)
- [mlz-m04-confusion-table](/course-wiki/mlz-m04-confusion-table/)
- [mlz-m04-cross-validation](/course-wiki/mlz-m04-cross-validation/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m04-summary](/course-wiki/mlz-m04-summary/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-installation-of-tensorflow](/course-wiki/mlz-m08-installation-of-tensorflow/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)

## Sources

- [Video](https://www.youtube.com/watch?v=YkyevnYyAww&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=17)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/02-regression/06-linear-regression-vector.md)
