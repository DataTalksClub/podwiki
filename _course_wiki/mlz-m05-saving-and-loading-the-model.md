---
title: "Saving and loading the model — Machine Learning Zoomcamp Module 5"
summary: "**In this session we'll cover the idea "How to use the model in future without training and evaluating the code"**
- To save the model we made before there is an option using the pickle library:
  - First install the library with the command ```pip i"
related_course:
  - mlz-module-05
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 5: Deploying Machine Learning Models](/course-wiki/mlz-module-05/) › Saving and loading the model

## Notes

**In this session we'll cover the idea "How to use the model in future without training and evaluating the code"**
- To save the model we made before there is an option using the pickle library:
  - First install the library with the command ```pip install pickle-mixin``` if you don't have it.
  - After training the model and making it ready for the prediction process, use this code to save the model for later.
  - ```python
    import pickle
    
    with open('model.bin', 'wb') as f_out: # 'wb' means write-binary
        pickle.dump((dict_vectorizer, model), f_out)
    ```
  - In the code above we'll make a binary file named model.bin, and write the dict_vectorizer for one hot encoding and the model as array in it. (We will save it as binary in case it wouldn't be readable by humans)
  - To be able to use the model in future without running the code, We need to open the binary file we saved before.
  - ```python
    import pickle
    
    with open('mode.bin', 'rb') as f_in: # very important to use 'rb' here, it means read-binary 
        dict_vectorizer, model = pickle.load(f_in)
    ## Note: never open a binary file you do not trust the source!
    ```
   - With unpacking the model and the dict_vectorizer, We're able to predict again for new input values without training a new model by re-running the code.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/10/ml-zoomcamp-2023-deploying-machine-learning-models-part-2/)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op](/course-wiki/mlz-m05-deployment-to-the-cloud-aws-elastic-beanstalk-op/)
- [mlz-m05-environment-management-docker](/course-wiki/mlz-m05-environment-management-docker/)
- [mlz-m05-explore-more](/course-wiki/mlz-m05-explore-more/)
- [mlz-m05-intro-session-overview](/course-wiki/mlz-m05-intro-session-overview/)
- [mlz-m05-python-virtual-environment-pipenv](/course-wiki/mlz-m05-python-virtual-environment-pipenv/)
- [mlz-m05-serving-the-churn-model-with-flask](/course-wiki/mlz-m05-serving-the-churn-model-with-flask/)
- [mlz-m05-summary](/course-wiki/mlz-m05-summary/)
- [mlz-m05-web-services-introduction-to-flask](/course-wiki/mlz-m05-web-services-introduction-to-flask/)

## Sources

- [Video](https://www.youtube.com/watch?v=EJpqZ7OlwFU&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/05-deployment/02-pickle.md)
