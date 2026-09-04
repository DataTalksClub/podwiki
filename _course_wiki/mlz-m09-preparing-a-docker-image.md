---
title: "Preparing a Docker image — Machine Learning Zoomcamp Module 9"
summary: "Refer to updates.md for info on running TF lite in 2024."
related_course:
  - mlz-module-09
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 9: Serverless Deep Learning](/course-wiki/mlz-module-09/) › Preparing a Docker image

## Notes

Refer to updates.md for info on running TF lite
in 2024. 

### Using `pip install` for TF-Lite binaries

When using `pip` to install the compiled binary, make sure you use the raw file, not a link to the github page.

Correct:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

(Note `/raw/` in the path)

Also correct:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl?raw=true
```

The wheel file above is for Python 3.10. Check other available compiled TF lite versions [here](https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite).

Not correct - won't work:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

If the file is incorrect, you'll get an error message like that: 

```
zipfile.BadZipFile: File is not a zip file
```

### `ENTRYPOINT` vs `CMD`

This link explains the difference between them: https://stackoverflow.com/a/34245657

> `ENTRYPOINT` specifies a command that will always be executed when the container starts.
> `CMD` specifies arguments that will be fed to the `ENTRYPOINT`.

In case of the lambda base pacakge, the authors already specified the entrypoint and
we only need to overwrite the arguments passed to the entrypoint,

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/04/ml-zoomcamp-2023-serverless-part-5/)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m09-api-gateway-exposing-the-lambda-function](/course-wiki/mlz-m09-api-gateway-exposing-the-lambda-function/)
- [mlz-m09-aws-lambda](/course-wiki/mlz-m09-aws-lambda/)
- [mlz-m09-creating-the-lambda-function](/course-wiki/mlz-m09-creating-the-lambda-function/)
- [mlz-m09-explore-more](/course-wiki/mlz-m09-explore-more/)
- [mlz-m09-introduction-to-serverless](/course-wiki/mlz-m09-introduction-to-serverless/)
- [mlz-m09-preparing-the-code-for-lambda](/course-wiki/mlz-m09-preparing-the-code-for-lambda/)
- [mlz-m09-python-3-12-vs-tf-lite-2-17](/course-wiki/mlz-m09-python-3-12-vs-tf-lite-2-17/)
- [mlz-m09-summary](/course-wiki/mlz-m09-summary/)
- [mlz-m09-tensorflow-lite](/course-wiki/mlz-m09-tensorflow-lite/)

## Sources

- [Video](https://www.youtube.com/watch?v=y4_YQjfOsDo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/09-serverless/05-docker-image.md)
