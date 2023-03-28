#Interpolation searching in python.
import numpy as np
x=[1,2,4,6,8,10,12,15,18,20]
array=np.array(x)
low=0
high=len(array)-1
search=int(input("Enter an Element to search-> "))
found=0
while(low<=high):
    formula=round(low+((search-x[low])/(x[high]-x[low]))*(high-low))
    if (array[formula]==search):
        found=1
        print(f"Element found at {formula}")
        break
    elif (array[formula]>search):
        high=formula-1
    elif (array[formula]<search):
       low=formula+1
else:
    print("Element not found!") 