#Sequentional search using num py. (IMP)
import numpy as np
arr = [2,3,5,8,9,10,14,15,20,40,51]
arr=np.array(arr)
search=int(input("Enter a number to search: "))
for i in range(0,len(arr)):
    if (arr[i]==search):
        print(f"Element found at {i} position")
        break
if(search==0):
    print(f"Element not found {search}")

