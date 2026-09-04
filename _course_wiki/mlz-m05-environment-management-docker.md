---
title: "Environment management: Docker — Machine Learning Zoomcamp Module 5"
summary: "- Once our project was packed in a Docker container, we're able to run our project on any machine. - First we have to make a Docker image. In Docker image file there are settings and dependecies we have in our project. To find Docker..."
related_course:
  - mlz-module-05
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/) › Environment management: Docker

## Notes

- Once our project was packed in a Docker container, we're able to run our project on any machine.
- First we have to make a Docker image. In Docker image file there are settings and dependecies we have in our project. To find Docker images that you need you can simply search the [Docker](https://hub.docker.com/search?type=image) website.

Here a Dockerfile (There should be no comments in Dockerfile, so remove the comments when you copy)

```docker
# First install the python 3.8, the slim version uses less space
FROM python:3.8.12-slim

# Install pipenv library in Docker 
RUN pip install pipenv

# create a directory in Docker named app and we're using it as work directory 
WORKDIR /app                                                                

# Copy the Pip files into our working derectory 
COPY ["Pipfile", "Pipfile.lock", "./"]

# install the pipenv dependencies for the project and deploy them.
RUN pipenv install --deploy --system

# Copy any python files and the model we had to the working directory of Docker 
COPY ["*.py", "churn-model.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "churn_serving:app"]
```

The flags `--deploy` and `--system` make sure that we install the dependencies directly inside the Docker container without creating an additional virtual environment (which `pipenv` does by default). 

If we don't put the last line `ENTRYPOINT`, we will be in a python shell.
Note that for the entrypoint, we put our commands in double quotes.

After creating the Dockerfile, we need to build it:

```bash
docker build -t churn-prediction .
```

To run it,  execute the command below:

```bash
docker run -it -p 9696:9696 churn-prediction:latest
```

Flag explanations: 

- `-t`: is used for specifying the tag name "churn-prediction".
- `-it`: in order for Docker to allow us access to the terminal.
- `--rm`: allows us to remove the image from the system after we're done.  
- `-p`: to map the 9696 port of the Docker to 9696 port of our machine. (first 9696 is the port number of our machine and the last one is Docker container port.)
- `--entrypoint=bash`: After running Docker, we will now be able to communicate with the container using bash (as you would normally do with the Terminal). Default is `python`.

At last you've deployed your prediction app inside a Docker container. Congratulations 🥳

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/14/ml-zoomcamp-2023-deploying-machine-learning-models-part-6/)

## Key concepts

- [Docker](/course-wiki/docker/)
- [Flask](/course-wiki/flask/)

## Related notes

- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-saving-and-loading-the-model](/course-wiki/mlz-m05-saving-and-loading-the-model/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m05-web-services-introduction-to-flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)
- [mlz-m09-preparing-a-docker-image](/course-wiki/mlz-m09-preparing-a-docker-image/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
- [mlz-m09-tensorflow-lite](/course-wiki/mlz-m09-tensorflow-lite/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)
- [mlz-m10-introduction-to-kubernetes](/course-wiki/mlz-m10-introduction-to-kubernetes/)
- [mlz-m10-overview](/course-wiki/mlz-m10-overview/)
- [mlz-m10-running-everything-locally-with-docker-compose](/course-wiki/mlz-m10-running-everything-locally-with-docker-compose/)

## Sources

- [Video](https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/05-deployment/06-docker.md)
