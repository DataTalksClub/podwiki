---
title: "Linear Algebra Refresher — Machine Learning Zoomcamp Module 1"
summary: "### Linear Algebra Refresher
* Vector operations
* Multiplication
  * Vector-vector multiplication
  * Matrix-vector multiplication
  * Matrix-matrix multiplication
* Identity matrix
* Inverse"
related_course:
  - mlz-module-01
---

[Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/) › [Module 1: Introduction to Machine Learning](/course-wiki/mlz-module-01/) › Linear Algebra Refresher

## Notes

### Linear Algebra Refresher
* Vector operations
* Multiplication
  * Vector-vector multiplication
  * Matrix-vector multiplication
  * Matrix-matrix multiplication
* Identity matrix
* Inverse

### Vector operations
~~~~python
u = np.array([2, 7, 5, 6])
v = np.array([3, 4, 8, 6])

# addition 
u + v

# subtraction 
u - v

# scalar multiplication 
2 * v
~~~~
### Multiplication

#####  Vector-vector multiplication

~~~~python
def vector_vector_multiplication(u, v):
    assert u.shape[0] == v.shape[0]
    
    n = u.shape[0]
    
    result = 0.0

    for i in range(n):
        result = result + u[i] * v[i]
    
    return result
~~~~

#####  Matrix-vector multiplication

~~~~python
def matrix_vector_multiplication(U, v):
    assert U.shape[1] == v.shape[0]
    
    num_rows = U.shape[0]
    
    result = np.zeros(num_rows)
    
    for i in range(num_rows):
        result[i] = vector_vector_multiplication(U[i], v)
    
    return result
~~~~

#####  Matrix-matrix multiplication

~~~~python
def matrix_matrix_multiplication(U, V):
    assert U.shape[1] == V.shape[0]
    
    num_rows = U.shape[0]
    num_cols = V.shape[1]
    
    result = np.zeros((num_rows, num_cols))
    
    for i in range(num_cols):
        vi = V[:, i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:, i] = Uvi
    
    return result
~~~~
### Identity matrix

~~~~python
I = np.eye(3)
~~~~
### Inverse
~~~~python
V = np.array([
    [1, 1, 2],
    [0, 0.5, 1], 
    [0, 2, 1],
])
inv = np.linalg.inv(V)
~~~~

Add notes here (PRs are welcome).

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke - Part 1/3](https://knowmledge.com/2023/09/15/ml-zoomcamp-2023-introduction-to-machine-learning-part-9/)
* [Notes from Peter Ernicke - Part 2/3](https://knowmledge.com/2023/09/15/ml-zoomcamp-2023-introduction-to-machine-learning-part-10/)
* [Notes from Peter Ernicke - Part 3/3](https://knowmledge.com/2023/09/15/ml-zoomcamp-2023-introduction-to-machine-learning-part-11/)

## Links

* [Notebook from the video](notebooks/08-linear-algebra.ipynb)
* [Get a visual understanding of matrix multiplication](http://matrixmultiplication.xyz/)
* [Overview of matrix multiplication functions in python/numpy](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_1-intro_to_ML_linear_algebra/Notes_for_Chapter_1-Linear_Algebra.ipynb)

## Key concepts

_No glossary concepts detected in this lesson._

## Related notes

- [mlz-m01-crisp-dm](/course-wiki/mlz-m01-crisp-dm/)
- [mlz-m01-introduction-to-machine-learning](/course-wiki/mlz-m01-introduction-to-machine-learning/)
- [mlz-m01-introduction-to-numpy](/course-wiki/mlz-m01-introduction-to-numpy/)
- [mlz-m01-introduction-to-pandas](/course-wiki/mlz-m01-introduction-to-pandas/)
- [mlz-m01-ml-vs-rule-based-systems](/course-wiki/mlz-m01-ml-vs-rule-based-systems/)
- [mlz-m01-model-selection-process](/course-wiki/mlz-m01-model-selection-process/)
- [mlz-m01-setting-up-the-environment](/course-wiki/mlz-m01-setting-up-the-environment/)
- [mlz-m01-summary](/course-wiki/mlz-m01-summary/)
- [mlz-m01-supervised-machine-learning](/course-wiki/mlz-m01-supervised-machine-learning/)

## Sources

- [Video](https://www.youtube.com/watch?v=zZyKUeOR4Gg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=8)
- [Lesson file](https://github.com/machine-learning-zoomcamp/blob/main/machine-learning-zoomcamp/cohorts/2026/01-intro/08-linear-algebra.md)
