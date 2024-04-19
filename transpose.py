# 1. Write a function to transpose a given matrix.
# using numpy
import numpy as np
def transpose_mat(matrix):
    return np.transpose(matrix)

matrix=np.array([[1,2,3],[7,4,6],[5,8,9]])
print("Transpose of matrix \n",matrix,"\nis =")
transpose_matrix=transpose_mat(matrix)
print("\n",transpose_matrix)
    