---
title: "Intro / Session overview — Machine Learning Zoomcamp Module 5"
summary: "In this session, we talked about the earlier model we made in chapter 3 for churn prediction. <br>
This chapter contains the deployment of the model. If we want to use the model to predict new values without running the code, there's a way to do this"
related_course:
  - mlz-module-05
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/) › Intro / Session overview

## Notes

In this session, we talked about the earlier model we made in chapter 3 for churn prediction. <br>
This chapter contains the deployment of the model. If we want to use the model to predict new values without running the code, there's a way to do this. The way to use the model in different machines without running the code, is to deploy the model in a server (run the code and make the model). After deploying the code in a machine used as server we can make some endpoints (using api's) to connect from another machine to the server and predict values.

Model deployment is crucial when you need to use the model across different machines or applications without having to retrain or rerun the code. By deploying the model as a web service, external systems (like marketing services) can send requests to the server to get predictions, such as whether a customer is likely to churn. Based on the prediction, actions like sending promotional offers can be automated.

To deploy the model in a server there are some steps:
1. **Train and Save the Model**: After training the model, save it as a file, to use it for making predictions in future (session 02-pickle).
2. **Create API Endpoints**: Make the API endpoints in order to request predictions. It is possible to use the Flask framework to create web service API endpoints that other services can interact with (session 03-flask-intro and 04-flask-deployment).
3. **Some other server deployment options** (sessions 5 to 9):
   - **Pipenv**: Create isolated environments to manage the Python dependencies of the web service, ensuring they don’t interfere with other services on the machine.
   - **Docker**: Package the service in a Docker container, which includes both system and Python dependencies, making it easier to deploy consistently across different environments. 
4. **Deploy to the Cloud**: Finally, deploy the Docker container to a cloud service like AWS to make the model accessible globally, ensuring scalability and reliability.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/09/ml-zoomcamp-2023-deploying-machine-learning-models-part-1/)

## Key concepts

- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-saving-and-loading-the-model](/course-wiki/mlz-m05-saving-and-loading-the-model/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m05-web-services-introduction-to-flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m10-deploying-a-simple-service-to-kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [mlz-m10-deploying-to-eks](/course-wiki/mlz-m10-deploying-to-eks/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)

## Sources

- [Video](https://www.youtube.com/watch?v=agIFak9A3m8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/05-deployment/01-intro.md)
