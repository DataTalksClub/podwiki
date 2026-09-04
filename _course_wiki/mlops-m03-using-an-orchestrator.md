---
title: "Using an Orchestrator — MLOps Zoomcamp Module 3"
summary: "Now that we converted the notebook into a python script, we can use an orchestrator to turn the script into a production pipeline."
related_course:
  - mlops-module-03
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/) › Using an Orchestrator

## Notes

Now that we converted the notebook into a python script, we 
can use an orchestrator to turn the script into a production
pipeline.

There's no video for this unit, but you can use ChatGPT to help you with this.

### Step 1: Choosing the Tool

For that you first need to choose an orchestrator. For example:

- Airflow
- Prefect
- Dagster
- Kestra
- Mage
- or some other tool

### Step 2: Running the Tool

* Configure the tool to run locally 
* Run the simplest "hello world" workflow 

### Step 3: Orchestrating the Workflow

* Get the code from the previous unit (see code)
* Use the tool to orchestrate the steps in the pipeline

### Step 4: Parametrizing the Workflow

* Schedule the workflow to run monthly
* The train data should be from two months ago
* The validation data - one month ago

### Step 5: Backfilling

* Learn to run the workflow for some of the past months

### Step 6: Deployment (optional)

* Learn to deploy the tool to the cloud 

### Resources 

For guidance, you can refer to past cohorts of the course:

- Prefect - 2022 and 2023
- Mage - 2024

You can also rely on ChatGPT or similar tools. They are very helpful.

## Key concepts

- [OpenAI API](/course-wiki/openai-api/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Deployment Automation](/course-wiki/deployment-automation/)
- [Kestra](/course-wiki/kestra/)
- [Model Deployment](/course-wiki/model-deployment/)
- [Jupyter Notebooks](/course-wiki/jupyter-notebooks/)

## Related notes

- [mlops-m01-homework](/course-wiki/mlops-m01-homework/)
- [mlops-m01-optional-training-a-ride-duration-prediction-mod](/course-wiki/mlops-m01-optional-training-a-ride-duration-prediction-mod/)
- [mlops-m02-getting-started-with-mlflow](/course-wiki/mlops-m02-getting-started-with-mlflow/)
- [mlops-m02-homework](/course-wiki/mlops-m02-homework/)
- [mlops-m03-homework](/course-wiki/mlops-m03-homework/)
- [mlops-m03-introduction-to-ml-pipelines](/course-wiki/mlops-m03-introduction-to-ml-pipelines/)
- [mlops-m03-turning-the-notebook-into-a-python-script](/course-wiki/mlops-m03-turning-the-notebook-into-a-python-script/)
- [mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
- [mlops-m04-optional-streaming-deploying-models-with-kinesis](/course-wiki/mlops-m04-optional-streaming-deploying-models-with-kinesis/)
- [mlops-m04-three-ways-of-deploying-a-model](/course-wiki/mlops-m04-three-ways-of-deploying-a-model/)
- [mlops-m04-web-services-deploying-models-with-flask-and-doc](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
- [mlops-m05-debugging-with-test-suites-and-reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
- [mlops-m06-homework](/course-wiki/mlops-m06-homework/)
- [mlops-m07-course-project](/course-wiki/mlops-m07-course-project/)

## Sources

- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/03-orchestration/README.md)
