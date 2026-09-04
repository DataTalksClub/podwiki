---
title: "Debugging with test suites and reports — MLOps Zoomcamp Module 5"
summary: "<a href='https://www.youtube.com/watch?v=sNSk3ojISh8&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK'>"
related_course:
  - mlops-module-05
---

[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) › [Module 5: Model Monitoring](/course-wiki/mlops-module-05/) › Debugging with test suites and reports

## Notes

<a href="https://www.youtube.com/watch?v=sNSk3ojISh8&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK">
  
</a>

## Homework

More information here

## Notes

Did you take notes? Add them here:

* [Week 5 notes by M. Ayoub C.](https://gist.github.com/Qfl3x/aa6b1bec35fb645ded0371c46e8aafd1)
* [week 5: Monitoring notes Ayoub.B](https://github.com/ayoub-berdeddouch/mlops-journey/blob/main/monitoring-05.md)
* [Week 5: 2023](https://github.com/dimzachar/mlops-zoomcamp/tree/master/notes/Week_5)
* [Week5: Why we need to monitor models after deployment? by Hongfan (Amber)](https://github.com/Muhongfan/MLops/blob/main/05-monitoring/README.md)
* [week-5: Detailed Notes about Monitoring, codes and homework by Muhammad Shifa](https://github.com/MuhammadShifa/mlops-zoomcamp2025/blob/main/05-monitoring/README.md)
* Send a PR, add your notes above this line

# Monitoring example

## Notes
There were a massive update for Evidently since 0.7.0 version.

To check working example with Evidently >= 0.7.0 go to `post-evidently-0.7` folder.

## Prerequisites

You need following tools installed:
- `docker`
- `docker-compose` (included to Docker Desktop for Mac and Docker Desktop for Windows )

## Preparation

Note: all actions expected to be executed in repo folder.

- Create virtual environment and activate it (eg. `python -m venv venv && source ./venv/bin/activate` or `conda create -n venv python=3.11 && conda activate venv`)
- Install required packages `pip install -r requirements.txt`
- Run `baseline_model_nyc_taxi_data.ipynb` for downloading datasets, training model and creating reference dataset 

## Monitoring Example

### Starting services

To start all required services, execute:
```bash
docker-compose up
```

It will start following services:
- `db` - PostgreSQL, for storing metrics data
- `adminer` - database management tool
- `grafana` - Visual dashboarding tool 

### Sending data

To calculate evidently metrics with prefect and send them to database, execute:
```bash
python evidently_metrics_calculation.py
```

This script will simulate batch monitoring. Every 10 seconds it will collect data for a daily batch, calculate metrics and insert them into database. This metrics will be available in Grafana in preconfigured dashboard. 

### Accsess dashboard

- In your browser go to a `localhost:3000`
The default username and password are `admin`

- Then navigate to `General/Home` menu and click on `Home`.

- In the folder `General` you will see `New Dashboard`. Click on it to access preconfigured dashboard.

### Ad-hoc debugging

Run `debugging_nyc_taxi_data.ipynb` to see how you can perform a debugging with help of Evidently `TestSuites` and `Reports`

### Stopping services

To stop all services, execute:
```bash
docker-compose down
```

## Key concepts

- [Docker](/course-wiki/docker/)
- [Evidently](/course-wiki/evidently/)
- [Model Monitoring](/course-wiki/model-monitoring/)
- [Prometheus and Grafana](/course-wiki/prometheus-and-grafana/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlops-m01-2-vm-in-aws](/course-wiki/mlops-m01-2-vm-in-aws/)
- [mlops-m01-homework](/course-wiki/mlops-m01-homework/)
- [mlops-m02-homework](/course-wiki/mlops-m02-homework/)
- [mlops-m03-homework](/course-wiki/mlops-m03-homework/)
- [mlops-m03-using-an-orchestrator](/course-wiki/mlops-m03-using-an-orchestrator/)
- [mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage](/course-wiki/mlops-m04-mlops-zoomcamp-4-6-batch-scoring-with-mage/)
- [mlops-m04-optional-streaming-deploying-models-with-kinesis](/course-wiki/mlops-m04-optional-streaming-deploying-models-with-kinesis/)
- [mlops-m04-three-ways-of-deploying-a-model](/course-wiki/mlops-m04-three-ways-of-deploying-a-model/)
- [mlops-m04-web-services-deploying-models-with-flask-and-doc](/course-wiki/mlops-m04-web-services-deploying-models-with-flask-and-doc/)
- [mlops-m05-data-quality-monitoring](/course-wiki/mlops-m05-data-quality-monitoring/)
- [mlops-m05-dummy-monitoring](/course-wiki/mlops-m05-dummy-monitoring/)
- [mlops-m05-environment-setup](/course-wiki/mlops-m05-environment-setup/)
- [mlops-m05-evidently-metrics-calculation](/course-wiki/mlops-m05-evidently-metrics-calculation/)
- [mlops-m05-evidently-monitoring-dashboard](/course-wiki/mlops-m05-evidently-monitoring-dashboard/)
- [mlops-m05-intro-to-ml-monitoring](/course-wiki/mlops-m05-intro-to-ml-monitoring/)
- [mlops-m05-prepare-reference-and-model](/course-wiki/mlops-m05-prepare-reference-and-model/)
- [mlops-m05-save-grafana-dashboard](/course-wiki/mlops-m05-save-grafana-dashboard/)
- [mlops-m06-homework](/course-wiki/mlops-m06-homework/)
- [mlops-m07-course-project](/course-wiki/mlops-m07-course-project/)

## Sources

- [Video](https://www.youtube.com/watch?v=sNSk3ojISh8&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK)
- [Lesson file](https://github.com/mlops-zoomcamp/blob/main/05-monitoring/README.md)
