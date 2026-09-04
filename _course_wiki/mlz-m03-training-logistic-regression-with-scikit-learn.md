---
title: "Training logistic regression with Scikit-Learn — Machine Learning Zoomcamp Module 3"
summary: "This video was about training a logistic regression model with Scikit-Learn, applying it to the validation dataset, and calculating its accuracy. "
related_course:
  - mlz-module-03
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 3: Machine Learning for Classification](/course-wiki/mlz-module-03/) › Training logistic regression with Scikit-Learn

## Notes

This video was about training a logistic regression model with Scikit-Learn, applying it to the validation dataset, and calculating its accuracy. 

**Classes, functions, and methods:** 

* `LogisticRegression().fit(x)` - Scikit-Learn class for training the logistic regression model. 
* `LogisticRegression().coef_[0]` - return the coefficients or weights of the LR model
* `LogisticRegression().intercept_[0]` - return the bias or intercept of the LR model
* `LogisticRegression().predict[x]` - make predictions on the x dataset 
* `LogisticRegression().predict_proba[x]` - make predictions on the x dataset by returning two columns with their probabilities for the two categories - soft predictions 

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/30/ml-zoomcamp-2023-machine-learning-for-classification-part-10/)

## Key concepts

- [Logistic Regression](/course-wiki/logistic-regression/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
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
- [mlz-m03-setting-up-the-validation-framework](/course-wiki/mlz-m03-setting-up-the-validation-framework/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-using-the-model](/course-wiki/mlz-m03-using-the-model/)

## Sources

- [Video](https://www.youtube.com/watch?v=hae_jXe2fN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/03-classification/10-training-log-reg.md)
