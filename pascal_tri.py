# 7. Generate Pascal's triangle up to a given number of rows as a NumPy array.
import numpy as np
def pascal_triangle(n):
    pascal = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):

            if j == 0 or j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal

print(pascal_triangle(5))