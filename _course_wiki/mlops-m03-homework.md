---
title: "Homework — MLOps Zoomcamp Module 3"
summary: "If you want to run MLFlow with Docker, you can do this:"
related_course:
  - mlops-module-03
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 3: Orchestration & ML Pipelines](/course-wiki/mlops-module-03/) › Homework

## Notes

More information here.

## Resources

### Mlflow

If you want to run MLFlow with Docker, you can do this:

Create a dockerfile for mlflow, e.g. `mlflow.dockerfile`:

```dockerfile
FROM python:3.10-slim

RUN pip install mlflow==2.12.1

EXPOSE 5000

CMD [ \
    "mlflow", "server", \
    "--backend-store-uri", "sqlite:///home/mlflow_data/mlflow.db", \
    "--host", "0.0.0.0", \
    "--port", "5000" \
]
```

Add it to the docker-compose.yaml:

```yaml
  mlflow:
    build:
      context: .
      dockerfile: mlflow.dockerfile
    ports:
      - "5000:5000"
    volumes:
      - "${PWD}/mlflow_data:/home/mlflow_data/"
```

In your code, make sure you use the same version of mlflow (`mlflow==2.12.1`).

When you run it, mlflow should be accessible at `http://mlflow:5000`.

## Notes

### Notes previous editions

- 2022 Prefect notes
- 2023 Prefect notes
- 2024 Mage notes

### Notes 2025

Did you take notes? Add them here:

* [2025 Cohort | Running Airflow + MLflow using Docker by André Calatré](https://github.com/calatre/mlops-zoomcamp/tree/main/03-orchestration)
* [Week 3 - workflow orchestration & Prefect by hannarud](https://github.com/hannarud/mlops-zoomcamp-2025/blob/main/week3_notes.md)
* [Orchestration with Prefect Notes and Code by Muhammad Shifa](https://github.com/MuhammadShifa/mlops-zoomcamp2025/blob/main/03-orchestration/README.md)
* Send a PR, add your notes above this line

## Key concepts

- [Docker](/course-wiki/docker/)
- [MLflow](/course-wiki/mlflow/)
- [Workflow Orchestration](/course-wiki/workflow-orchestration/)
- [Deployment Automation](/course-wiki/deployment-automation/)

## Related notes

- [mlops-m01-2-vm-in-aws](/course-wiki/mlops-m01-2-vm-in-aws/)
- [mlops-m01-homework](/course-wiki/mlops-m01-homework/)
- [mlops-m02-experiment-tracking-with-mlflow](/course-wiki/mlops-m02-experiment-tracking-with-mlflow/)
- [mlops-m02-getting-started-with-mlflow](/course-wiki/mlops-m02-getting-started-with-mlflow/)
- [mlops-m02-homework](/course-wiki/mlops-m02-homework/)
- [mlops-m02-mlflow-benefits-limitations-and-alternatives](/course-wiki/mlops-m02-mlflow-benefits-limitations-and-alternatives/)
- [mlops-m02-mlflow-in-practice](/course-wiki/mlops-m02-mlflow-in-practice/)
- [mlops-m02-model-registry](/course-wiki/mlops-m02-model-registry/)
- [mlops-m03-introduction-to-ml-pipelines](/course-wiki/mlops-m03-introduction-to-ml-pipelines/)
- [mlops-m03-turning-the-notebook-into-a-python-script](/course-wiki/mlops-m03-turning-the-notebook-into-a-python-script/)
- [mlops-m03-using-an-orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
- [mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
- [mlops-m04-web-services-deploying-models-with-flask-and-doc](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
- [mlops-m04-web-services-getting-the-models-from-the-model-r](/course-wiki/mlops-m04-web-services-getting-the-models-from-the-model-r/)
- [mlops-m05-debugging-with-test-suites-and-reports](/course-wiki/mlops-m05-debugging-with-test-suites-and-reports/)
- [mlops-m06-homework](/course-wiki/mlops-m06-homework/)
- [mlops-m06-integration-tests-with-docker-compose](/course-wiki/mlops-m06-integration-tests-with-docker-compose/)
- [mlops-m07-course-project](/course-wiki/mlops-m07-course-project/)

## Sources

- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/03-orchestration/README.md)
