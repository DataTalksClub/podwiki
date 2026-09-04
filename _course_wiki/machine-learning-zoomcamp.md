---
title: "Machine Learning Zoomcamp"
summary: "DataTalks.Club's free machine learning engineering course: from regression and classification to deploying models with FastAPI, Docker, Kubernetes, and AWS Lambda."
related_course:
  - Zoomcamps
  - MLOps Zoomcamp
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
[YouTube](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
and a [course FAQ](https://datatalks.club/faq/machine-learning-zoomcamp.html).
The live cohort runs once a year (September through December, capstones
concluding in January); everything is also available self-paced.

## Curriculum

The course uses Python, NumPy, pandas, scikit-learn, TensorFlow, PyTorch,
FastAPI, Docker, Kubernetes, and AWS Lambda.

- **Module 1: Introduction to Machine Learning** — rule-based systems versus
  ML, supervised learning, and structuring a project with
  [CRISP-DM](/course-wiki/crisp-dm/).
- **Module 2: Machine Learning for Regression** — a car-price prediction model
  built from exploratory analysis through
  [linear regression](/course-wiki/linear-regression/) and
  [regularization](/course-wiki/regularization/), with a validation framework.
- **Module 3: Machine Learning for Classification** — customer-churn
  prediction with [logistic regression](/course-wiki/logistic-regression/),
  categorical encoding, and feature importance.
- **Module 4: Evaluation Metrics for Classification** — accuracy, precision,
  recall, F1, confusion matrices, ROC curves and AUC, cross-validation, and
  class imbalance ([classification metrics](/course-wiki/classification-metrics/)).
- **Module 5: Deploying Machine Learning Models** — model serialization,
  serving predictions through [FastAPI](/course-wiki/fastapi/), packaging with
  [Docker](/course-wiki/docker/), and cloud deployment.
- **Module 6: Decision Trees and Ensemble Learning** —
  [decision trees](/course-wiki/decision-trees/), random forests, and
  [gradient boosting](/course-wiki/gradient-boosting/) with XGBoost, plus
  hyperparameter tuning.
- **Midterm project** — an end-to-end ML problem of the learner's choice,
  deployed as a web service.
- **Module 8: Neural Networks and Deep Learning** —
  [neural networks](/course-wiki/neural-networks/), convolutional networks and
  [transfer learning](/course-wiki/transfer-learning/) with PyTorch, TensorFlow,
  and Keras for image classification.
- **Module 9: Serverless Deep Learning** — scikit-learn, TensorFlow, and
  PyTorch models served through AWS Lambda and API Gateway
  ([serverless deployment](/course-wiki/serverless-deployment/)).
- **Module 10: Kubernetes and TensorFlow Serving** — model serving, scaling,
  and traffic distribution on [Kubernetes](/course-wiki/kubernetes/).
- **Capstone projects 1 and 2** — two larger end-to-end projects that qualify
  for the certificate.

## Who it is for

The course targets people with about a year of programming experience who
want to move into machine learning engineering — software engineers, data
analysts, data engineers, and technical students. No prior machine learning
experience is required; command-line comfort is. Cloud, Kubernetes, and GPU
experience are explicitly not prerequisites, and the deep learning modules
use cloud resources instead of a local GPU.

## Projects and certificate

Certificates require a live cohort: two qualifying projects (the midterm plus
one capstone, or both capstones) and peer reviews of three other learners'
projects. The capstone workflow — choose a dataset, define the prediction
task, train and evaluate, deploy as a web service — is the same shape hiring
managers probe for. Published learner case studies include a
[blood cell classifier for cancer prediction](https://datatalks.club/blog/how-to-build-blood-cell-classifier-for-cancer-prediction-case-study-from-ml-zoomcamp.html)
and a
[waste classifier](https://datatalks.club/blog/how-to-build-waste-classifier-case-study-from-ml-zoomcamp.html)
serving an Xception model through a Docker-packaged API.
