#Basic Queue implementation using numpy.

#At first we check the 'Over flow' condition, to create an Insert(num) function.
def insert(num):
    global rear
    if (rear==9):
        print("Over flow.")
    else:
        rear=rear+1
        queue[rear]=num
        print("Element inserted.")
    
#Then we check the 'Under flow' condition, to create a delete() function. 
def delete():
    global rear,front
    if(front>rear):
        print("Under flow.")
    else:
        print(f"{queue[front]} removed")
        front+=1

#Now we take a num.py module to create a Queue space.
import numpy as np

#This line work process I already declared in stack.
rear=-1
front=0
queue=np.zeros(10,dtype='int16')
while True:
    ch=int(input('''<Insert-1> <Delete-2> <Exit-3> : '''))
    if(ch==1):
        x=int(input("Enter a element: "))
        insert(x)
    elif(ch==2):
        delete()
    elif(ch==3):
        break
    else:
        print("Error,please Input a valid element.")
        pass
    




