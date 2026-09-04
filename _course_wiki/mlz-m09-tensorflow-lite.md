---
title: "TensorFlow Lite — Machine Learning Zoomcamp Module 9"
summary: "bash wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5"
related_course:
  - mlz-module-09
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/) › TensorFlow Lite

## Notes

New URL for downloading the model:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5
```

Add notes from the video (PRs are welcome)

* tensorflow has a size of approximately 1.7 GB
* there are size limits of cloud services and docker container
* tensorflow lite is small in size and limited to using a model to make predictions (inference)
* convert tensorflow keras model to a tensorflow lite model

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/01/ml-zoomcamp-2023-serverless-part-2/)
* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/02/ml-zoomcamp-2023-serverless-part-3/)

## Key concepts

- [Docker](/course-wiki/docker/)

## Related notes

- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m09-api-gateway-exposing-the-lambda-function](/course-wiki/mlz-m09-api-gateway-exposing-the-lambda-function/)
- [mlz-m09-aws-lambda](/course-wiki/mlz-m09-aws-lambda/)
- [mlz-m09-creating-the-lambda-function](/course-wiki/mlz-m09-creating-the-lambda-function/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-preparing-a-docker-image](/course-wiki/mlz-m09-preparing-a-docker-image/)
- [mlz-m09-preparing-the-code-for-lambda](/course-wiki/mlz-m09-preparing-the-code-for-lambda/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
- [mlz-m09-summary](/course-wiki/mlz-m09-summary/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)

## Sources

- [Video](https://www.youtube.com/watch?v=OzZA4mSBE0Q&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/09-serverless/03-tensorflow-lite.md)
