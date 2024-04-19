# 2. Implement matrix multiplication for two given matrices.
# using numpy
import numpy as np
def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

matrix_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_2=np.array([[19,12,13],[14,15,16],[11,18,20]])
print("Matrix 1:\n",matrix_1)
print("Matrix 2:\n",matrix_2)

print("\nMultiplication of Matrix 1 & 2:\n")
print(matrix_multiplication(matrix1=matrix_1,matrix2=matrix_2))