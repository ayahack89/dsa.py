# Binary search using numpy.
#Binary search.
import numpy as np
x=[2,5,8,10,15,18,22,26,30,41]
x=np.array(x)
search=int(input("Enter a number: "))
low=0
high=len(x)-1
for i in range(0,len(x)):
        # mid formula.
        mid=((low+high)//2)
        
        if(search==x[mid]):
                print("Element found.")
                break
        elif(search>x[mid]):
                # low sequence foemula.
                low=mid+1
        elif(search<x[mid]):
                # high sequence formula.
                high=mid-1
            
if(search==x[mid]):
        print(f"Element found at {mid} position.")
else:
    print(f"Element not found,{search}")
    pass