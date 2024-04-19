# 4. Given two arrays, find the common elements between them.
# using numpy
import numpy as np
a = np.array([1, 2, 3, 6, 5])
b = np.array([5, 6, 7, 2, 9])
print("A=\n",a)
print("B=\n",b)
print("\nCommon elements in A & B=")
print(np.intersect1d(a, b))