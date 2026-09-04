---
title: "Regularization — Machine Learning Zoomcamp Module 2"
summary: "If the feature matrix has duplicate columns (or columns that can be expressed as a linear combination of other columns), it will not have an inverse matrix. But, sometimes this error could be passed if certain values are slightly different
between du"
related_course:
  - mlz-module-02
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 2: Machine Learning for Regression](/course-wiki/mlz-module-02/) › Regularization

## Notes

If the feature matrix has duplicate columns (or columns that can be expressed as a linear combination of other columns), it will not have an inverse matrix. But, sometimes this error could be passed if certain values are slightly different
between duplicated columns. 

So, if we apply the normal equation with this feature matrix, the values associated with duplicated columns are very large, which decreases
the model performance. To solve this issue, one alternative is adding a small number to the diagonal of the feature matrix, which corresponds to regularization. 

This technique 
works because the addition of small values to the diagonal makes it less likely to have duplicated columns. The regularization value is a hyperparameter of the model. After applying 
regularization the model performance improved. 

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/23/ml-zoomcamp-2023-machine-learning-for-regression-part-11/)

## Comments
### Linear combination

I mentioned the term *linear combination* in the video, but didn't explain what it means. 
So if you're interested what it means, you can read here

* One column is a linear combination of others when you can express one column of a matrix as a sum of others columns
* The simplest example is when a column is an exact duplicate of another column
* Another example. Let's say we have 3 columns: `a`, `b`, `c`. If `c = 0.2 * a + 0.5 * b`, then `c` is a linear combination of `a` and `b`
* More formal definition: https://en.wikipedia.org/wiki/Linear_combination

### Ridge Regression
The regularization technique used (adding a factor to the diagonals of Gram Matrix) in this lesson is Ridge Regression. Further explanations are available in this [DataTalks.Club article](https://datatalks.club/blog/regularization-in-regression.html).

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

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
- [mlz-m02-linear-regression-vector-form](/course-wiki/mlz-m02-linear-regression-vector-form/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-setting-up-the-validation-framework](/course-wiki/mlz-m02-setting-up-the-validation-framework/)
- [mlz-m02-training-linear-regression-normal-equation](/course-wiki/mlz-m02-training-linear-regression-normal-equation/)
- [mlz-m02-tuning-the-model](/course-wiki/mlz-m02-tuning-the-model/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)

## Sources

- [Video](https://www.youtube.com/watch?v=91ve3EJlHBc&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=24)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/02-regression/13-regularization.md)
