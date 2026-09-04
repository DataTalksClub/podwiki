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

- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
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
