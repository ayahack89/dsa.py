#Interpolation searching in python.
import numpy as np
arr=[1,2,4,6,8,10,12,15,18,20]
array=np.array(arr)
low=0
high=len(array)-1
search=int(input("Enter an Element to search-> "))
count=0
while low<=high and search>=arr[low] and search<=arr[high]:
    mid=int(low+(search-arr[low])*(high-low)/(arr[high]-arr[low]))
    if arr[mid]==search:
        print(f"Element found at {mid} position.")
        break
    elif arr[mid]>search:
        high=mid-1
    elif arr[mid]<search:
       low=mid+1
    else:
        print("Element not found!")
