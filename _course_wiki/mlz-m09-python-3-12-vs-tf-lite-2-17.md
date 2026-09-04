---
title: "Python 3.12 vs TF Lite 2.17 — Machine Learning Zoomcamp Module 9"
summary: "The latest versions of TF Lite don't support Python 3.12 yet."
related_course:
  - mlz-module-09
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/) › Python 3.12 vs TF Lite 2.17

## Notes

# Python 3.12 vs TF Lite 2.17

The latest versions of TF Lite don't support Python 3.12 yet. 

As a workaround, we can use the previous version of TF Lite 
to serve the models created by TensorFlow 2.17. We tested 
it with TF Lite 2.14 and the deep learning models we use
in the course work successfully with this setup.

Here's how you do it

First, use Python 3.10. It means that you will need to use
`public.ecr.aws/lambda/python:3.10` as the base image:

```docker 
FROM public.ecr.aws/lambda/python:3.10
```

Second, use numpy 1.23.1:

```docker
RUN pip install numpy==1.23.1
```

When installing tf lite interpreter for AWS lambda, 
make sure you don't install dependencies with `--no-deps` flag:

```docker
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

If you don't do it, pip will try to upgdate the version of numpy
and your code won't work (as the tflite runtime was compiled 
with numpy 1, not numpy 2).

## Key concepts

- [Docker](/course-wiki/docker/)
- [Neural Networks](/course-wiki/neural-networks/)
- [Serverless Deployment](/course-wiki/serverless-deployment/)

## Related notes

- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m08-convolutional-neural-networks](/course-wiki/mlz-m08-convolutional-neural-networks/)
- [mlz-m08-fashion-classification](/course-wiki/mlz-m08-fashion-classification/)
- [mlz-m08-pre-trained-convolutional-neural-networks](/course-wiki/mlz-m08-pre-trained-convolutional-neural-networks/)
- [mlz-m08-regularization-and-dropout](/course-wiki/mlz-m08-regularization-and-dropout/)
- [mlz-m08-tensorflow-and-keras](/course-wiki/mlz-m08-tensorflow-and-keras/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-api-gateway-exposing-the-lambda-function](/course-wiki/mlz-m09-api-gateway-exposing-the-lambda-function/)
- [mlz-m09-aws-lambda](/course-wiki/mlz-m09-aws-lambda/)
- [mlz-m09-creating-the-lambda-function](/course-wiki/mlz-m09-creating-the-lambda-function/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-preparing-a-docker-image](/course-wiki/mlz-m09-preparing-a-docker-image/)
- [mlz-m09-preparing-the-code-for-lambda](/course-wiki/mlz-m09-preparing-the-code-for-lambda/)
- [mlz-m09-summary](/course-wiki/mlz-m09-summary/)
- [mlz-m09-tensorflow-lite](/course-wiki/mlz-m09-tensorflow-lite/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)

## Sources

- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/09-serverless/updates.md)
