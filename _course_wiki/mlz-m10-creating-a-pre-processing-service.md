---
title: "Creating a pre-processing service — Machine Learning Zoomcamp Module 10"
summary: "Add notes from the video (PRs are welcome)"
related_course:
  - mlz-module-10
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/) › Creating a pre-processing service

## Notes

Add notes from the video (PRs are welcome)

* turn jupyter notebook into flask app
* the notebook communicates with the model deployed with tensorflow
* the notebook fetches an image, pre-processes it, turns it into protobuf, sends it to tensorflow-serving, does post-processing and finally gives a human-readable answer
* convert notebook into python script and call the script gateway
* prepare request, send request, prepare response
* you can reuse the flask app code from session 5
* two components: docker container with tensorflow serving and flask application with the gateway
* be aware of the library sizes: tensorflow 1.7 GB, tensorflow CPU ~400 MB, tensorflow serving
* turn numpy array into protobuf format
* tensorflow protobuf

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

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m10-deploying-a-simple-service-to-kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [mlz-m10-deploying-to-eks](/course-wiki/mlz-m10-deploying-to-eks/)
- [mlz-m10-explore-more](/course-wiki/mlz-m10-explore-more/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)
- [mlz-m10-running-everything-locally-with-docker-compose](/course-wiki/mlz-m10-running-everything-locally-with-docker-compose/)
- [mlz-m10-summary](/course-wiki/mlz-m10-summary/)
- [mlz-m10-tensorflow-serving](/course-wiki/mlz-m10-tensorflow-serving/)

## Sources

- [Video](https://www.youtube.com/watch?v=OIlrS14Zi0o&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/10-kubernetes/03-preprocessing.md)
