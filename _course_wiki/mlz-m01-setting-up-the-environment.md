---
title: "Setting up the Environment — Machine Learning Zoomcamp Module 1"
summary: "In this section, we'll prepare the environment"
related_course:
  - mlz-module-01
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/) › Setting up the Environment

## Notes

# Setting up the Environment

In this section, we'll prepare the environment

You need:

* Python 3.11 (note that videos use 3.8)
* NumPy, Pandas and Scikit-Learn (latest available versions) 
* Matplotlib and Seaborn
* Jupyter notebooks

## Github Codespaces

Video: https://www.youtube.com/watch?v=pqQFlV3f9Bo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR

This is the recommended approach for the course

## Ubuntu 22.04 on AWS

* [This video](https://www.youtube.com/watch?v=IXSiYkP23zo) shows a complete end-to-end environment configuration for an AWS EC2 instance
* This video was created for another course (MLOps Zoomcamp), so you'll need to adjust it slightly: clone this repo instead of the mlops one
* You can use these instructions for setting up your local Ubuntu

Note for WSL 

* Most of the instructions from the previous video apply to WSL too
* For setting up Docker, install Docker Desktop on Windows and it'll be automatically used in WSL. You don't need to install docker.io

## Anaconda and Conda

The easiest way to set up the environment is to use [Anaconda](https://www.anaconda.com/products/individual) or
[Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Anaconda comes with everything we need (and much more). 
Miniconda is a smaller version of Anaconda that contains only Python. 

Follow the instructions on page for installing the correct package for your system.
The site will automatically detect your operating system and suggest the correct package.

* [Anaconda](https://www.anaconda.com/products/individual)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links)

If you are using Windows, you can use WSL, but the plain Windows version should work too.

Anaconda is recommended.

### (Optional) Create environment for course

It is a good idea to set up a dedicated environment for the course 

In your terminal, run this command to create the environment

```bash
conda create -n ml-zoomcamp python=3.11
```

Activate it:

```bash
conda activate ml-zoomcamp
```

Installing libraries

```bash
conda install numpy pandas scikit-learn seaborn jupyter
```

Later in the course you will also need to install XGBoost and Tensorflow,
but we can skip this part for now.

## Cloud

Instead of running things locally, you can use online services or rent a server 

### AWS 

You can rent an instance on AWS:

* [Creating an AWS account](https://mlbookcamp.com/article/aws)
* [Renting an ec2 instance](https://mlbookcamp.com/article/aws-ec2)

### GCP

Google cloud platform offers $300 in free credits when you sign up.
You can use this for taking the course.

## Notebook services

There are services that allow you to host and run notebooks.
Note that notebooks alone are not sufficient for the course and for the deployment modules
you will need to have access to the command line interface with Docker, Python and other libraries installed.

### Kaggle

To use Kaggle to open and run the Jupyter notebooks provided as part of this course do the following:

*Pre-requisites - You need to have an account in Kaggle (it's free) and be logged into Kaggle*

1. Find the URL of the notebook. 
   
   
   
2. To open the notebook in Kaggle, in your web browser launch paste the URL as shown in below example. (*note the additional https://kaggle.com/kernels/welcome?src= before the URL of the notebook*)

   https://kaggle.com/kernels/welcome?src=https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb
  
3. Check if the notebook uses any datafile to read data from it. If yes, note the datafile name from the code.- *look for pd.read_csv("somefilename.csv")*. 
   
   
   
4. You need to download the file into Kaggle. For this:

   a. Find the URL of the datafile in github. 
   
   
   
   b. Suppose the URL is https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/data.csv , you need use the URL to raw file, which will look something like https://r

## Key concepts

- [Gradient Boosting](/course-wiki/gradient-boosting/)
- [Model Deployment](/course-wiki/model-deployment/)

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-introduction-to-machine-learning](/course-wiki/mlz-m01-introduction-to-machine-learning/)
- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-linear-algebra-refresher](/course-wiki/mlz-m01-linear-algebra-refresher/)
- [mlz-m01-ml-vs-rule-based-systems](/course-wiki/mlz-m01-ml-vs-rule-based-systems/)
- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m01-supervised-machine-learning](/course-wiki/mlz-m01-supervised-machine-learning/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m06-gradient-boosting-and-xgboost](/course-wiki/mlz-m06-gradient-boosting-and-xgboost/)
- [mlz-m06-selecting-the-best-model](/course-wiki/mlz-m06-selecting-the-best-model/)
- [mlz-m06-summary](/course-wiki/mlz-m06-summary/)
- [mlz-m06-xgboost-parameter-tuning](/course-wiki/mlz-m06-xgboost-parameter-tuning/)
- [mlz-m08-transfer-learning](/course-wiki/mlz-m08-transfer-learning/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m10-deploying-a-simple-service-to-kubernetes](/course-wiki/mlz-m10-deploying-a-simple-service-to-kubernetes/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [mlz-m10-deploying-to-eks](/course-wiki/mlz-m10-deploying-to-eks/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)
- [sma-m05-deployment-and-automation](/course-wiki/sma-m05-deployment-and-automation/)

## Sources

- [Video](https://www.youtube.com/watch?v=pqQFlV3f9Bo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/01-intro/06-environment.md)
