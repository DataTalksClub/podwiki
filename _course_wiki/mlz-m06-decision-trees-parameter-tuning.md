---
title: "Decision trees parameter tuning — Machine Learning Zoomcamp Module 6"
summary: "In this lesson, we will discuss about different parameters used to control a Decision Tree (DT). Two of them, `max_depth` and `min_samples_leaf` have a greater importance than the others. We will further see how we first tune `max_depth` parameter an"
related_course:
  - mlz-module-06
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 6: Decision Trees and Ensemble Learning](/course-wiki/mlz-module-06/) › Decision trees parameter tuning

## Notes

In this lesson, we will discuss about different parameters used to control a Decision Tree (DT). Two of them, `max_depth` and `min_samples_leaf` have a greater importance than the others. We will further see how we first tune `max_depth` parameter and then move to tuning other parameters will help. After that, a dataframe will be created with all possible combinations of `max_depth`, `min_sample_leaf` and the auc score corresponding to them. These results will be visualized using a heatmap by pivoting the dataframe to easily determine the best possible `max_depth` and `min_samples_leaf` combination. Finally, the DT will be retrained using the identified parameter combination. The DT so trained will be viewed as a tree diagram, for visualizing decision rules.     

### Steps
* **Fine-Tuning Process:** iterate to find optimal parameter settings.
    *   Start by tuning `max_depth` with various values to determine a subset of optimal
depths.
    *   Then, using this subset, fine-tune the model further by exploring different
`min_samples_leaf` values.

    This method is computationally efficient for **large datasets**, though it may not be optimal for smaller ones.

* **Heatmaps for Visualization:** Store the scores (e.g., AUC) obtained during tuning in a pivot table, and create a heatmap with `seaborn` to easily identify high score areas, which helps pinpoint the optimal `max_depth` and `min_samples_leaf` combination.

**NB:** Choose parameter values that effectively control the tree's size and avoid values like 'nan' (Not a Number), even if they seem to lead to better scores.

### Importance of  `max_depth` and `min_samples_leaf`

*   **Controlling Overfitting:** these parameters play a critical role in preventing overfitting.
    *   `max_depth` limits the tree's complexity, preventing it from growing too deep and memorizing the training data.
    *   `min_samples_leaf` ensures that leaf nodes have a sufficient number of samples,
reducing the chance of creating nodes that are too specific to the training data.

*   **Impact on Bias and Variance:** They also affect the model's bias and variance.
    *   Increasing `max_depth` and decreasing `min_samples_leaf` can lead to a more complex model with lower bias but higher variance.
    *   Decreasing `max_depth` and increasing `min_samples_leaf` results in a simpler model with higher bias but lower variance.
      
It's then important to find the right balance between `max_depth` and `min_samples_leaf` to achieve optimal model performance.
This involves a trade-off between bias and variance, and the best values depend on the specific dataset and problem.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/23/ml-zoomcamp-2023-decision-trees-and-ensemble-learning-part-8/)

## Key concepts

- [Classification Metrics](/course-wiki/classification-metrics/)
- [Decision Trees](/course-wiki/decision-trees/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m02-car-price-prediction-project](/course-wiki/mlz-m02-car-price-prediction-project/)
- [mlz-m02-computing-rmse-on-validation-data](/course-wiki/mlz-m02-computing-rmse-on-validation-data/)
- [mlz-m02-feature-engineering](/course-wiki/mlz-m02-feature-engineering/)
- [mlz-m02-root-mean-squared-error-rmse](/course-wiki/mlz-m02-root-mean-squared-error-rmse/)
- [mlz-m02-using-the-model](/course-wiki/mlz-m02-using-the-model/)
- [mlz-m04-evaluation-metrics-session-overview](/course-wiki/mlz-m04-evaluation-metrics-session-overview/)
- [mlz-m04-explore-more](/course-wiki/mlz-m04-explore-more/)
- [mlz-m04-precision-and-recall](/course-wiki/mlz-m04-precision-and-recall/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m04-summary](/course-wiki/mlz-m04-summary/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-data-cleaning-and-preparation](/course-wiki/mlz-m06-data-cleaning-and-preparation/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-explore-more](/course-wiki/mlz-m06-explore-more/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)

## Sources

- [Video](https://www.youtube.com/watch?v=XJaxwH50Qok&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/06-trees/05-decision-tree-tuning.md)
