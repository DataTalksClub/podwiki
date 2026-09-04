---
title: "Web services: introduction to Flask — Machine Learning Zoomcamp Module 5"
summary: "In this session we talked about what is a web service and how to create a simple web service. - What is actually a web service - A web service is a method used to communicate between electronic devices. - There are some methods in web..."
related_course:
  - mlz-module-05
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/) › Web services: introduction to Flask

## Notes

In this session we talked about what is a web service and how to create a simple web service.
- What is actually a web service
  - A web service is a method used to communicate between electronic devices.
  - There are some methods in web services that we can use to satisfy our problems. Here below we would list some.
    - **GET:**  GET is a method used to retrieve files, For example when we are searching for a cat image in google we are actually requesting cat images with GET method.
    - **POST:** POST is the second common method used in web services. It enables sending data to a server to create or update a resource. For example in a sign up process, when we are submiting our name, username, passwords, etc we are posting our data to a server that is using the web service. (Note that there is no specification where the data goes)
    -  **PUT:** PUT is same as POST but we are specifying where the data is going to.
    -  **DELETE:** DELETE is a method that is used to request to delete some data from the server.
    -  For more information just google the HTTP methods, You'll find useful information about this.
- To create a simple web service, there are plenty libraries available in every language. Here we would like to introduce Flask library in python.
  - If you haven't installed the library just try installing it with the code ```pip install Flask```
  - To create a simple web service just run the code below:
  - ```python
    from flask import Flask
    
    app = Flask('ping') # give an identity to your web service
    
    @app.route('/ping', methods=['GET']) # use decorator to add Flask's functionality to our function
    def ping():
        return 'PONG'
    
    if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0', port=9696) # run the code in local machine with the debugging mode true and port 9696
    ```
   - With the code above we made a simple web server and created a route named ping that would send pong string.
   - To test it, just use the `cURL` command in a new terminal by typing ```curl http://localhost:9696/ping```, or simply open your browser and search ```localhost:9696/ping```, You'll see that the 'PONG' string is received. Congrats You've made a simple web server 🥳.
- To use our web server to predict new values we must modify it. See how in the next session.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/11/ml-zoomcamp-2023-deploying-machine-learning-models-part-3/)

## Key concepts

- [Flask](/course-wiki/flask/)
- [Spec-Driven Development](/course-wiki/spec-driven-development/)

## Related notes

- [aidt-m01-ai-native-developer-workflow](/course-wiki/aidt-m01-ai-native-developer-workflow/)
- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-saving-and-loading-the-model](/course-wiki/mlz-m05-saving-and-loading-the-model/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m10-creating-a-pre-processing-service](/course-wiki/mlz-m10-creating-a-pre-processing-service/)
- [mlz-m10-deploying-tensorflow-models-to-kubernetes](/course-wiki/mlz-m10-deploying-tensorflow-models-to-kubernetes/)

## Sources

- [Video](https://www.youtube.com/watch?v=W7ubna1Rfv8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/05-deployment/03-flask-intro.md)
