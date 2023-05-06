#Two Daimentional array accesing process.
import numpy as np
twoDarray = [[1,2,3,4],[5,6,7,8]]
arr = np.array(twoDarray)
print("Our 2D array is.. \n" ,arr )
print(type(arr))

'''Accesing 1D array'''
print("First row:-")
print(" -",arr[0][0])
print(" -",arr[0][1])
print(" -",arr[0][2])
print(" -",arr[0][3])
print("second row:-")
print(" -",arr[1][0])
print(" -",arr[1][1])
print(" -",arr[1][2])
print(" -",arr[1][3])



 