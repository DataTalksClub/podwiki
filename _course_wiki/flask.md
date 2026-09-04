---
title: "Flask"
summary: "The lightweight web framework MLOps Zoomcamp uses to turn a trained model into a prediction web service."
related_course:
  - Model Deployment
  - Model Registry
  - Docker
  - FastAPI
  - Model Monitoring
---

Module 4's web-service deployment is a Flask application: it loads the NY Taxi duration model from the model registry at startup, exposes a /predict endpoint that takes JSON ride features, and returns the prediction. The service is packaged with a Dockerfile and run with gunicorn inside Docker.

Flask's minimalism is the point — the deployment lessons focus on the surrounding machinery (registry access, containerization, testing with docker-compose) rather than framework features. The same pattern is what Machine Learning Zoomcamp's FastAPI module mirrors with type-safe request validation.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/)
    - [Intro / Session overview](/course-wiki/mlz-m05-intro-session-overview/)
    - [Web services: introduction to Flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)
    - [Serving the churn model with Flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
    - [Python virtual environment: Pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
    - [Environment management: Docker](/course-wiki/mlz-m05-environment-management-docker/)
    - [Deployment to the cloud: AWS Elastic Beanstalk (optional)](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
    - [Explore more](/course-wiki/mlz-m05-explore-more/)
  - [Module 10: Kubernetes and TensorFlow Serving](/course-wiki/mlz-module-10/)
    - [Creating a pre-processing service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
    - [Deploying TensorFlow models to Kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [LLM Zoomcamp](/course-wiki/llm-zoomcamp/)
  - [Module 7: End-to-End Project](/course-wiki/llmz-module-07/)
    - [End-to-End Project Example](/course-wiki/llmz-m07-end-to-end-project-example/)
    - [Interface and Ingestion Pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
    - [Monitoring and Containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
    - [Summary and Closing Remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
  - [Module 4: Model Deployment](/course-wiki/mlops-module-04/)
    - [Web-services: Deploying models with Flask and Docker](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
## Related concepts

- [Model Deployment](/course-wiki/model-deployment/)
- [Model Registry](/course-wiki/model-registry/)
- [Docker](/course-wiki/docker/)
- [FastAPI](/course-wiki/fastapi/)
- [Model Monitoring](/course-wiki/model-monitoring/)
