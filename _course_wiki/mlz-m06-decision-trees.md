---
title: "Decision trees — Machine Learning Zoomcamp Module 6"
summary: "Decision Trees are powerful algorithms, capable of fitting complex datasets. The decision trees make predictions based on the bunch of if/else statements by splitting a node into two or more sub-nodes."
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › Decision trees

## Notes

Decision Trees are powerful algorithms, capable of fitting complex datasets. The decision trees make predictions based on the bunch of *if/else* statements by splitting a node into two or more sub-nodes.

With versatility, the decision tree is also prone to overfitting. One of the reasons why this algorithm often overfits is its depth. It tends to memorize all the patterns in the train data but struggles to perform well on the unseen data (validation or test set).

To overcome the overfitting problem, we can reduce the complexity of the algorithm by reducing the depth size.

A decision tree with a depth of 1 is called `decision stump` and has only one split from the root.

**Classes, functions, and methods**:

- `DecisionTreeClassifier`: classification model from `sklearn.tree` class.
- `max_depth`: hyperparameter to control the maximum depth of decision tree algorithm.
- `export_text`: method from `sklearn.tree` class to display the text report showing the rules of a decision tree.

*Note*: we have already covered `DictVectorizer` in session 3 and `roc_auc_score` in session 4 respectively.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/19/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-4/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/20/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-5/)

## Key concepts

- [scikit-learn](/course-wiki/scikit-learn/)
- [Decision Trees](/course-wiki/decision-trees/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m02-explore-more](/course-wiki/mlz-m02-explore-more/)
- [mlz-m03-explore-more](/course-wiki/mlz-m03-explore-more/)
- [mlz-m03-feature-importance-mutual-information](/course-wiki/mlz-m03-feature-importance-mutual-information/)
- [mlz-m03-one-hot-encoding](/course-wiki/mlz-m03-one-hot-encoding/)
- [mlz-m03-setting-up-the-validation-framework](/course-wiki/mlz-m03-setting-up-the-validation-framework/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m04-accuracy-and-dummy-model](/course-wiki/mlz-m04-accuracy-and-dummy-model/)
- [mlz-m04-cross-validation](/course-wiki/mlz-m04-cross-validation/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-data-cleaning-and-preparation](/course-wiki/mlz-m06-data-cleaning-and-preparation/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-explore-more](/course-wiki/mlz-m06-explore-more/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)

## Sources

- [Video](https://www.youtube.com/watch?v=YGiQvFbSIg8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/03-decision-trees.md)
