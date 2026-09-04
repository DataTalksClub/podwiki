---
title: "Deploying TensorFlow models to Kubernetes — Machine Learning Zoomcamp Module 10"
summary: "Add notes from the video (PRs are welcome)"
related_course:
  - mlz-module-10
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/) › Deploying TensorFlow models to Kubernetes

## Notes

Add notes from the video (PRs are welcome)

* tensorflow serving in C++, gateway service as flask app
* gateway service: image preprocessing (i.e. resizing), prepare matrix, numpy arr, convert to protobuf, gRPC to communicate with tensorflow serving; postprocessing
* using telnet to check kubernetes pod

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

## Key concepts

- [Kubernetes](/course-wiki/kubernetes/)
- [TensorFlow](/course-wiki/tensorflow/)
- [Flask](/course-wiki/flask/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-web-services-introduction-to-flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)
- [mlz-m08-checkpointing](/course-wiki/mlz-m08-checkpointing/)
- [mlz-m08-explore-more](/course-wiki/mlz-m08-explore-more/)
- [mlz-m08-fashion-classification](/course-wiki/mlz-m08-fashion-classification/)
- [mlz-m08-installation-of-tensorflow](/course-wiki/mlz-m08-installation-of-tensorflow/)
- [mlz-m08-tensorflow-and-keras](/course-wiki/mlz-m08-tensorflow-and-keras/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
- [mlz-m09-tensorflow-lite](/course-wiki/mlz-m09-tensorflow-lite/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-deploying-a-simple-service-to-kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
- [mlz-m10-deploying-to-eks](/course-wiki/mlz-m10-deploying-to-eks/)
- [mlz-m10-explore-more](/course-wiki/mlz-m10-explore-more/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)
- [mlz-m10-running-everything-locally-with-docker-compose](/course-wiki/mlz-m10-running-everything-locally-with-docker-compose/)
- [mlz-m10-summary](/course-wiki/mlz-m10-summary/)
- [mlz-m10-tensorflow-serving](/course-wiki/mlz-m10-tensorflow-serving/)

## Sources

- [Video](https://www.youtube.com/watch?v=6vHLMdnjO2w&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/10-kubernetes/07-kubernetes-tf-serving.md)
