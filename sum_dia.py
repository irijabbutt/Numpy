#3. Write a function to calculate the sum of diagonal elements in a square matrix.
# using numpy
import numpy as np
def sum_diagonal(matrix):
    return np.trace(matrix)

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix=\n",matrix)
print("\nSum of Diagonal elements in matrix=",sum_diagonal(matrix))
