---
title: "ROC AUC — Machine Learning Zoomcamp Module 4"
summary: "The Area under the ROC curves can tell us how good is our model with a single value. The AUROC of a random model is 0.5, while for an ideal one is 1. "
related_course:
  - mlz-module-04
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 4: Evaluation Metrics for Classification](/course-wiki/mlz-module-04/) › ROC AUC

## Notes

The Area under the ROC curves can tell us how good is our model with a single value. The AUROC of a random model is 0.5, while for an ideal one is 1. 

In other words, AUC can be interpreted as the probability that a randomly selected positive example has a greater score than a randomly selected negative example.

**Classes and methods:** 

* `auc(x, y)` - sklearn.metrics class for calculating area under the curve of the x and y datasets. For ROC curves x would be false positive rate, and y true positive rate. 
* `roc_auc_score(x, y)` - sklearn.metrics class for calculating area under the ROC curves of the x false positive rate and y true positive rate datasets.
* `randint(x, y, size=z)` - np.random class for generating random integers from the “discrete uniform” distribution; from `x` (inclusive) to `y` (exclusive) of size `z`. 

The entire code of this project is available in [this jupyter notebook](notebook.ipynb).  

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/07/ml-zoomcamp-2023-evaluation-metrics-for-classification-part-6/)

## Key concepts

- [Classification Metrics](/course-wiki/classification-metrics/)

## Related notes

- [mlz-m02-car-price-prediction-project](/course-wiki/mlz-m02-car-price-prediction-project/)
- [mlz-m02-computing-rmse-on-validation-data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
- [mlz-m02-feature-engineering](/course-wiki/mlz-m02-feature-engineering/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)
- [mlz-m04-accuracy-and-dummy-model](/course-wiki/mlz-m04-accuracy-and-dummy-model/)
- [mlz-m04-confusion-table](/course-wiki/mlz-m04-confusion-table/)
- [mlz-m04-cross-validation](/course-wiki/mlz-m04-cross-validation/)
- [mlz-m04-evaluation-metrics-session-overview](/course-wiki/mlz-m04-evaluation-metrics-session-overview/)
- [mlz-m04-explore-more](/course-wiki/mlz-m04-explore-more/)
- [mlz-m04-precision-and-recall](/course-wiki/mlz-m04-precision-and-recall/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m04-summary](/course-wiki/mlz-m04-summary/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)

## Sources

- [Video](https://www.youtube.com/watch?v=hvIQPAwkVZo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/04-evaluation/06-auc.md)
