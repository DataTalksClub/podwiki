---
title: "Python virtual environment: Pipenv — Machine Learning Zoomcamp Module 5"
summary: "In this session we're going to make virtual environments for our project. So Let's start this session by getting to know what is a virtual environment and how to make it. - Every time we're running a file from a directory we're using the..."
related_course:
  - mlz-module-05
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/) › Python virtual environment: Pipenv

## Notes

In this session we're going to make virtual environments for our project. So Let's start this session by getting to know what is a virtual environment and how to make it.
- Every time we're running a file from a directory we're using the executive files from a global directory. When we install python on our machine the executable files that are able to run our codes will go to somewhere like _/home/username/python/bin/_. The pip command, for example, may go to _/home/username/python/bin/pip_.
- Sometimes the versions of libraries conflict (the project may not run or get into massive errors). For example, we have an old project that uses sklearn library with the version of 0.24.1 and now we want to run it using sklearn version 1.0.0. We may get into errors because of the version conflict.
   - To solve the conflict we can make virtual environments. A virtual environment is an operation that can separate the libraries installed in our system and the libraries with specified version we want our project to run with. There are a lot of ways to create virtual environments. One way we are going to use is a library named pipenv.
   - pipenv is a library that can create a virutal environment. To install this library just use the classic method ```pip install pipenv```.
   - After installing pipenv we must install the libraries we want for our project in the new virtual environment. It's really easy, Just use the command pipenv instead of pip. ```pipenv install numpy scikit-learn==0.24.1 flask```. With this command we installed the libraries we want for our project.
   - Note that using the pipenv command we made two files named _Pipfile_ and _Pipfile.lock_. If we look at these files closely we can see that in Pipfile the libraries we installed are named. If we specified the library name, it's also specified in Pipfile.
   - In _Pipfile.lock_ we can see that each library with its installed version is named and a hash file is there to reproduce if we move the environment to another machine.
   - If we want to run the project in another machine, we can easily install the libraries we want with the command ```pipenv install```. This command will look into _Pipfile_ and _Pipfile.lock_ to install the libraries with specified version.
   - After installing the required libraries we can run the project in the virtual environment with ```pipenv shell``` command. This will go to the virtual environment's shell and then any command we execute will use the virtual environment's libraries. Typing `gunicorn --bind localhost:9696 predict:app` can run the web service. However, if we prefer to use only one command to run the application in our environment, we just have to type: `pipenv run gunicorn --bind localhost:9696 predict:app`.
- Installing and using the libraries such as gunicorn is the same as the last session.
- Until here we made a virtual environment for our libraries with a required specified version. To seperate this environment more, such as making gunicorn be able to run in windows machines we need another way. The other way is using Docker. Docker allows us to seperate everything more than before and make any project able to run on any machine that supports Docker smoothly.
- In the next session we'll go in detail of how Docker works and how to use it.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/13/ml-zoomcamp-2023-deploying-machine-learning-models-part-5/)

## Key concepts

- [Docker](/course-wiki/docker/)
- [scikit-learn](/course-wiki/scikit-learn/)
- [Flask](/course-wiki/flask/)

## Related notes

- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m02-explore-more](/course-wiki/mlz-m02-explore-more/)
- [mlz-m03-explore-more](/course-wiki/mlz-m03-explore-more/)
- [mlz-m03-feature-importance-mutual-information](/course-wiki/mlz-m03-feature-importance-mutual-information/)
- [mlz-m03-one-hot-encoding](/course-wiki/mlz-m03-one-hot-encoding/)
- [mlz-m03-setting-up-the-validation-framework](/course-wiki/mlz-m03-setting-up-the-validation-framework/)
- [mlz-m03-summary](/course-wiki/mlz-m03-summary/)
- [mlz-m03-training-logistic-regression-with-scikit-learn](/course-wiki/mlz-m03-training-logistic-regression-with-scikit-learn/)
- [mlz-m04-accuracy-and-dummy-model](/course-wiki/mlz-m04-accuracy-and-dummy-model/)
- [mlz-m04-cross-validation](/course-wiki/mlz-m04-cross-validation/)
- [mlz-m04-roc-auc](/course-wiki/mlz-m04-roc-auc/)
- [mlz-m04-roc-curves](/course-wiki/mlz-m04-roc-curves/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-saving-and-loading-the-model](/course-wiki/mlz-m05-saving-and-loading-the-model/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m05-web-services-introduction-to-flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)
- [mlz-m06-decision-tree-learning-algorithm](/course-wiki/mlz-m06-decision-tree-learning-algorithm/)
- [mlz-m06-decision-trees](/course-wiki/mlz-m06-decision-trees/)
- [mlz-m06-ensemble-learning-and-random-forest](/course-wiki/mlz-m06-ensemble-learning-and-random-forest/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-preparing-a-docker-image](/course-wiki/mlz-m09-preparing-a-docker-image/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
- [mlz-m09-tensorflow-lite](/course-wiki/mlz-m09-tensorflow-lite/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)
- [mlz-m10-running-everything-locally-with-docker-compose](/course-wiki/mlz-m10-running-everything-locally-with-docker-compose/)

## Sources

- [Video](https://www.youtube.com/watch?v=BMXh8JGROHM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/05-deployment/05-pipenv.md)
