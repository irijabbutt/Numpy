# 5. Check if a given matrix is symmetric or not.
# using numpy
import numpy as np
def is_symmetric(matrix):
    return np.allclose(matrix, matrix.T)

matrix=np.array([[1,2,3],[2,1,4],[3,4,5]])
print("Matrix=\n",matrix)
print("\nGiven matrix is=")
if is_symmetric(matrix):
    print("Symmetric")
else:
    print("Not Symmetric")
