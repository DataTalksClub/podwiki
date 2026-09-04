---
layout: wiki
title: "Machine Learning Zoomcamp"
summary: "DataTalks.Club's free machine learning engineering course: from regression and classification to deploying models with FastAPI, Docker, Kubernetes, and AWS Lambda."
related_course:
  - Zoomcamps
  - MLOps Zoomcamp
related:
  - Machine Learning
  - Machine Learning Engineer Roadmap
  - Machine Learning Portfolio Projects
  - Production ML Project Checklist
  - Teaching
  - Learning in Public AI Career Switch
---

Machine Learning Zoomcamp is DataTalks.Club's free, hands-on course on machine
learning engineering. It follows the complete path from a machine learning
problem to a production service: frame the problem, prepare the data, train
and evaluate the model, expose it through an API, package it, and deploy it.
The emphasis is on turning trained models into services other applications can
call, not on theory.

All materials are open source in the
[course repository](https://github.com/DataTalksClub/machine-learning-zoomcamp),
with videos on
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR),
a [course FAQ](https://datatalks.club/faq/machine-learning-zoomcamp.html), and
a [course overview article](https://datatalks.club/blog/machine-learning-zoomcamp.html).
It is part of the [Zoomcamps](/course-wiki/zoomcamps/) family; [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) is the natural
follow-up for the operational layer after deployment.

## Curriculum

The course runs four cohort months per year (September through December, with
capstones concluding in January) and uses Python, NumPy, pandas,
scikit-learn, TensorFlow, PyTorch, FastAPI, Docker, Kubernetes, and AWS
Lambda. The [repository syllabus](https://github.com/DataTalksClub/machine-learning-zoomcamp)
maps each module:

- **Introduction to Machine Learning** — rule-based systems versus ML,
  supervised learning, and structuring a project with CRISP-DM.
- **Regression** — a car-price prediction model built from exploratory
  analysis through regularization and validation.
- **Classification** — customer-churn prediction with logistic regression,
  categorical encoding, and feature importance.
- **Evaluation metrics for classification** — accuracy, precision, recall,
  F1, confusion matrices, ROC/AUC, cross-validation, and class imbalance.
- **Deployment** — model serialization, serving predictions through FastAPI,
  packaging with Docker, and cloud deployment ([Production](/wiki/production/)).
- **Decision trees and ensemble learning** — random forests, gradient
  boosting with XGBoost, and hyperparameter tuning.
- **Midterm project** — an end-to-end ML problem of the learner's choice.
- **Neural networks and deep learning** — CNNs, transfer learning, and
  PyTorch/TensorFlow/Keras for image classification ([Computer Vision](/wiki/computer-vision/)).
- **Serverless deep learning** — scikit-learn, TensorFlow, and PyTorch models
  served through AWS Lambda and API Gateway.
- **Kubernetes and TensorFlow Serving** — model serving, scaling, and traffic
  distribution on Kubernetes.
- **Capstone projects** — two larger end-to-end projects that qualify for the
  certificate.

## Who it is for

The course targets people with about a year of programming experience who
want to move into machine learning engineering — software engineers, data
analysts, data engineers, and technical students. No prior machine learning
experience is required; command-line comfort is. Cloud, Kubernetes, and GPU
experience are explicitly not prerequisites, and the deep learning modules
use cloud resources instead of a local GPU.

## Projects, portfolio, and certificate

Certificates require a live cohort: two qualifying projects (the midterm plus
one capstone, or both capstones) and peer reviews of three other learners'
projects. The capstone workflow — choose a dataset, define the prediction
task, train and evaluate, deploy as a web service — is the same shape hiring
managers probe for, which is why [ML Portfolio Projects](/wiki/machine-learning-portfolio-projects/) treats Zoomcamp
capstones as strong entry-level evidence.

Published learner case studies include a
[blood cell classifier for cancer prediction](https://datatalks.club/blog/how-to-build-blood-cell-classifier-for-cancer-prediction-case-study-from-ml-zoomcamp.html)
and a
[waste classifier](https://datatalks.club/blog/how-to-build-waste-classifier-case-study-from-ml-zoomcamp.html)
serving an Xception model through a Docker-packaged API.

## What the podcast adds

The DataTalks.Club podcast repeatedly shows this course as the structured path
into ML engineering. The teaching model behind it centers project-based,
end-to-end learning where notes, READMEs, and GitHub artifacts carry the
knowledge.
[Designing FinTech Data Analytics Curriculum](https://datatalks.club/podcast/teaching-mentoring-data-analytics-fintech.html)
A radio astronomer used it to move MEERKAT data-pipeline work from notebooks
toward reusable, production-grade ML code.
[From Radio Astronomy to Applied ML](https://datatalks.club/podcast/from-radio-astronomy-to-machine-learning-and-data-engineering.html)
A self-taught bioinformatician paired the same project-first learning style
with open-source contributions to break in without a degree.
[How to Teach Yourself Bioinformatics & ML](https://datatalks.club/podcast/learning-machine-learning-self-taught-bioinformatics.html)
Career switchers returning after a break rebuilt evidence through ML Zoomcamp
projects and shared the progress publicly, which turned into recruiter
inbound.
[How to Become an AI Engineer After a Career Break](https://datatalks.club/podcast/s23e04-how-to-become-ai-engineer-after-career-break.html)

[Public Learning for AI Careers](/wiki/learning-in-public-ai-career-switch/) documents how learners turn the course's
homework cadence into visible proof of work. For the operational layer after
deployment — tracking, orchestration, monitoring — continue with
[MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/) and the [ML Engineer Roadmap](/wiki/machine-learning-engineer-roadmap/).

## Related Pages

- [Zoomcamps](/course-wiki/zoomcamps/)
- [Machine Learning](/wiki/machine-learning/)
- [ML Engineer Roadmap](/wiki/machine-learning-engineer-roadmap/)
- [ML Portfolio Projects](/wiki/machine-learning-portfolio-projects/)
- [Production ML Checklist](/wiki/production-ml-project-checklist/)
- [MLOps Zoomcamp](/course-wiki/mlops-zoomcamp/)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
- [Teaching](/wiki/teaching/)
