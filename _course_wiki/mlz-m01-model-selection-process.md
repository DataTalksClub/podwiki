---
title: "Model Selection Process — Machine Learning Zoomcamp Module 1"
summary: "- Logistic regression
- Decision tree
- Neural Network
- Or many others"
related_course:
  - mlz-module-01
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/) › Model Selection Process

## Notes

### Which model to choose?

- Logistic regression
- Decision tree
- Neural Network
- Or many others

The validation dataset is not used in training. There are feature matrices and y vectors
for both training and validation datasets. 
The model is fitted with training data, and it is used to predict the y values of the validation
feature matrix. Then, the predicted y values (probabilities)
are compared with the actual y values. 

**Multiple comparisons problem (MCP):** just by chance one model can be lucky and obtain
good predictions because all of them are probabilistic. 

The test set can help to avoid the MCP. Obtaining the best model is done with the training and validation datasets, while the test dataset is used for assuring that the proposed best model is the best. 

1. Split datasets in training, validation, and test. E.g. 60%, 20% and 20% respectively 
2. Train the models
3. Evaluate the models
4. Select the best model 
5. Apply the best model to the test dataset 
6. Compare the performance metrics of validation and test

<u>NB:</u> Note that it is possible to reuse the validation data. After selecting the best model (step 4), the validation and training datasets can be combined to form a single training dataset for the chosen model before testing it on the test set.

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/09/13/ml-zoomcamp-2023-introduction-to-machine-learning-part-5/)

## Key concepts

- [Neural Networks](/course-wiki/neural-networks/)
- [Logistic Regression](/course-wiki/logistic-regression/)
- [Decision Trees](/course-wiki/decision-trees/)

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-introduction-to-machine-learning](/course-wiki/mlz-m01-introduction-to-machine-learning/)
- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-linear-algebra-refresher](/course-wiki/mlz-m01-linear-algebra-refresher/)
- [mlz-m01-ml-vs-rule-based-systems](/course-wiki/mlz-m01-ml-vs-rule-based-systems/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m01-supervised-machine-learning](/course-wiki/mlz-m01-supervised-machine-learning/)
- [mlz-m03-logistic-regression](/course-wiki/mlz-m03-logistic-regression/)
- [mlz-m03-model-interpretation](/course-wiki/mlz-m03-model-interpretation/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m03-using-the-model](/course-wiki/mlz-m03-using-the-model/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-credit-risk-scoring-project](/course-wiki/mlz-m06-credit-risk-scoring-project/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-decision-trees-parameter-tuning](/course-wiki/mlz-m06-decision-trees-parameter-tuning/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-convolutional-neural-networks](/course-wiki/mlz-m08-convolutional-neural-networks/)
- [mlz-m08-fashion-classification](/course-wiki/mlz-m08-fashion-classification/)
- [mlz-m08-pre-trained-convolutional-neural-networks](/course-wiki/mlz-m08-pre-trained-convolutional-neural-networks/)
- [mlz-m08-regularization-and-dropout](/course-wiki/mlz-m08-regularization-and-dropout/)
- [mlz-m08-tensorflow-and-keras](/course-wiki/mlz-m08-tensorflow-and-keras/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)

## Sources

- [Video](https://www.youtube.com/watch?v=OH_R0Sl9neM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=6)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/01-intro/05-model-selection.md)
