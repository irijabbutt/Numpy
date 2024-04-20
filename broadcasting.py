# Broadcasting task 4*7 = 28
# when 1. they are equal, or 2. one of them is 1. If these conditions are not met, a ValueError: operands could not be broadcast together exception is thrown,
import numpy as np

a = np.array([4])
b = np.array([7])
c = a * b

print(c)

a=np.random.random(4)
b=np.random.random(7)
c=a*b
print(c)