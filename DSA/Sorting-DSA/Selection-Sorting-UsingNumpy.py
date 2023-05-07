# Selection Sorting using Numpy Array.
"""Here 'a' is an Array[list] . Which I import into 'ndArray'/numpy(array)."""
import numpy as np

a = [23, 67, 38, 19, 56, 78, 44, 88, 90, 100, 1200, 346, 789, 845, 4, 6, 1, 3908, 2, 10]
mai = np.array(a)
print(mai)
print(type(mai))
for index in range(0, len(mai)):
    for secindex in range(index + 1, len(mai)):
        if mai[index] > mai[secindex]:
            temp = mai[index]
            mai[index] = mai[secindex]
            mai[secindex] = temp
print("----------------")
print("AFTER SORTING:-", mai)
