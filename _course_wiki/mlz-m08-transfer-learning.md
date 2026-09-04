---
title: "Transfer learning — Machine Learning Zoomcamp Module 8"
summary: "Add notes from the video (PRs are welcome)"
related_course:
  - mlz-module-08
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 8: Neural Networks and Deep Learning](/course-wiki/mlz-module-08/) › Transfer learning

## Notes

Add notes from the video (PRs are welcome)

* convolutional layers convert an image into a vector representation
* dense layers use vector representations to make predictions
* using a pretrained neural network
* imagenet has 1000 different classes
* a dense layer may be specific to a certain number of classes whereas the vector representation can be applied to another dataset
* reusing the vector representation from convolutional layers means transferring knowledge and the idea behind transfer learning
* train faster on smaller size images
* the batch size
* base model vs custom model
* bottom layers vs top layers in keras
* keras optimizers
* using the adam optimizer
* weights, learning rates
* eta in xgboost
* model loss
* categorical cross entropy
* changing accuracy during several training epochs
* overfitting

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/11/21/ml-zoomcamp-2023-deep-learning-part-6/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/11/22/ml-zoomcamp-2023-deep-learning-part-7/)

## Key concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Neural Networks](/course-wiki/neural-networks/)
- [Transfer Learning](/course-wiki/transfer-learning/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-adding-more-layers](/course-wiki/mlz-m08-adding-more-layers/)
- [mlz-m08-adjusting-the-learning-rate](/course-wiki/mlz-m08-adjusting-the-learning-rate/)
- [mlz-m08-checkpointing](/course-wiki/mlz-m08-checkpointing/)
- [mlz-m08-convolutional-neural-networks](/course-wiki/mlz-m08-convolutional-neural-networks/)
- [mlz-m08-data-augmentation](/course-wiki/mlz-m08-data-augmentation/)
- [mlz-m08-explore-more](/course-wiki/mlz-m08-explore-more/)
- [mlz-m08-fashion-classification](/course-wiki/mlz-m08-fashion-classification/)
- [mlz-m08-installation-of-tensorflow](/course-wiki/mlz-m08-installation-of-tensorflow/)
- [mlz-m08-pre-trained-convolutional-neural-networks](/course-wiki/mlz-m08-pre-trained-convolutional-neural-networks/)
- [mlz-m08-regularization-and-dropout](/course-wiki/mlz-m08-regularization-and-dropout/)
- [mlz-m08-summary](/course-wiki/mlz-m08-summary/)
- [mlz-m08-tensorflow-and-keras](/course-wiki/mlz-m08-tensorflow-and-keras/)
- [mlz-m08-training-a-larger-model](/course-wiki/mlz-m08-training-a-larger-model/)
- [mlz-m08-using-the-model](/course-wiki/mlz-m08-using-the-model/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)

## Sources

- [Video](https://www.youtube.com/watch?v=WKHylqfNmq4&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/08-deep-learning/05-transfer-learning.md)
