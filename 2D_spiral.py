#6. Write a function to traverse a given 2D matrix in a spiral order, starting from the top-left corner and moving clockwise. 
# using numpy
import numpy as np
def spiral_matrix(matrix):
    a = np.array(matrix)
    print(a)
    print(a.shape)

    ab = np.transpose(a)
    print(ab)
    print(ab.shape)

    abc = np.flip(ab, axis=1)
    print(abc)
    print(abc.shape)

    abcd = np.flip(abc, axis=0)
    print(abcd)
    print(abcd.shape)

    abcde = np.transpose(abcd)
    print(abcde)
    
print("Spiral Matrix")
spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])