---
title: "Supervised Machine Learning — Machine Learning Zoomcamp Module 1"
summary: "In Supervised Machine Learning (SML) there are always labels associated with certain features.
The model is trained, and then it can make predictions on new features. In this way, the model
is taught by certain features and targets. "
related_course:
  - mlz-module-01
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/) › Supervised Machine Learning

## Notes

In Supervised Machine Learning (SML) there are always labels associated with certain features.
The model is trained, and then it can make predictions on new features. In this way, the model
is taught by certain features and targets. 

* **Feature matrix (X):** made of observations or objects (rows) and features (columns).
* **Target variable (y):** a vector with the target information we want to predict. For each row of X there's a value in y.

The model can be represented as a function, **g**, that takes the feature matrix, **X**, as **input** and tries to predict values as close as possible to the targets, **y**. The process of **finding** this function **g** is called **training**.

### Types of SML problems 

* **Regression:** the output is a number (car's price).
* **Classification:** the output is a category (spam example). 
	* **Binary:** there are two categories. 
	* **Multiclass problems:** there are more than two categories. 
* **Ranking:** the output is the top scores associated with corresponding items. It is applied in recommender systems. 

In summary, SML is about teaching the model by showing it different examples, and the goal is to come up with a function, that takes the feature matrix as input, and makes predictions of values as close as possible to the **y** targets. 

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/11/ml-zoomcamp-2023-introduction-to-machine-learning-part-3/)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-introduction-to-machine-learning](/course-wiki/mlz-m01-introduction-to-machine-learning/)
- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-linear-algebra-refresher](/course-wiki/mlz-m01-linear-algebra-refresher/)
- [mlz-m01-ml-vs-rule-based-systems](/course-wiki/mlz-m01-ml-vs-rule-based-systems/)
- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)

## Sources

- [Video](https://www.youtube.com/watch?v=j9kcEuGcC2Y&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=4)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/01-intro/03-supervised-ml.md)
