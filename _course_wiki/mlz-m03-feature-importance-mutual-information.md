---
title: "Feature importance: Mutual information — Machine Learning Zoomcamp Module 3"
summary: "Mutual information is a concept from information theory, which measures how much we can learn about one variable if we know the value of another. In this project, we can think of this as how much do we learn about churn if we have the information fro"
related_course:
  - mlz-module-03
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 3: Machine Learning for Classification](/course-wiki/mlz-module-03/) › Feature importance: Mutual information

## Notes

Mutual information is a concept from information theory, which measures how much we can learn about one variable if we know the value of another. In this project, we can think of this as how much do we learn about churn if we have the information from a particular feature. So, it is a measure of the importance of a categorical variable. 

**Classes, functions, and methods:** 

* `mutual_info_score(x, y)` - Scikit-Learn class for calculating the mutual information between the x target variable and y feature. 
* `df[x].apply(y)` - apply a y function to the x series of the df dataframe. 
* ` df.sort_values(ascending=False).to_frame(name='x')` - sort values in an ascending order and called the column as x. 

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/28/ml-zoomcamp-2023-machine-learning-for-classification-part-6/)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m03-churn-prediction-project](/course-wiki/mlz-m03-churn-prediction-project/)
- [mlz-m03-data-preparation](/course-wiki/mlz-m03-data-preparation/)
- [mlz-m03-eda](/course-wiki/mlz-m03-eda/)
- [mlz-m03-explore-more](/course-wiki/mlz-m03-explore-more/)
- [mlz-m03-feature-importance-churn-rate-and-risk-ratio](/course-wiki/mlz-m03-feature-importance-churn-rate-and-risk-ratio/)
- [mlz-m03-feature-importance-correlation](/course-wiki/mlz-m03-feature-importance-correlation/)
- [mlz-m03-logistic-regression](/course-wiki/mlz-m03-logistic-regression/)
- [mlz-m03-model-interpretation](/course-wiki/mlz-m03-model-interpretation/)
- [mlz-m03-one-hot-encoding](/course-wiki/mlz-m03-one-hot-encoding/)
- [mlz-m03-setting-up-the-validation-framework](/course-wiki/mlz-m03-setting-up-the-validation-framework/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m03-using-the-model](/course-wiki/mlz-m03-using-the-model/)

## Sources

- [Video](https://www.youtube.com/watch?v=_u2YaGT6RN0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/03-classification/06-mutual-info.md)
