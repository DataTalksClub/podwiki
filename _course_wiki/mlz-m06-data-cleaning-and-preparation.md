---
title: "Data cleaning and preparation — Machine Learning Zoomcamp Module 6"
summary: "In this section we clean and prepare the [dataset](https://github.com/gastonstat/CreditScoring/raw/master/CreditScoring.csv) for the model which involves the following steps:"
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › Data cleaning and preparation

## Notes

In this section we clean and prepare the [dataset](https://github.com/gastonstat/CreditScoring/raw/master/CreditScoring.csv) for the model which involves the following steps:

- Download the data from the given link.
- Reformat categorical columns (`status`, `home`, `marital`, `records`, and `job`) by mapping with appropriate values.
- Replace the maximum value of `income`, `assests`, and `debt` columns with NaNs.
- Replace the NaNs in the dataframe with `0` (*will be shown in the next lesson*).
- Extract only those rows in the column `status` who are either ok or default as value.
- Split the data in a two-step process which finally leads to the distribution of 60% train, 20% validation, and 20% test sets with random seed to `11`.
- Prepare target variable `status` by converting it from categorical to binary, where 0 represents `ok` and 1 represents `default`.
- Finally delete the target variable from the train/val/test dataframe.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/17/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-2/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/18/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-3/)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-explore-more](/course-wiki/mlz-m06-explore-more/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)

## Sources

- [Video](https://www.youtube.com/watch?v=tfuQdI3YO2c&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/02-data-prep.md)
