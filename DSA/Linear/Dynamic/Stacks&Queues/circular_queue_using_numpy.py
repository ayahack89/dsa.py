# The key difference between a queue and a circular queue is that a circular queue is a more optimized implementation of a queue, where the last element is linked to the first element, creating a circular structure.
#The code as same as the queue structure.

#At first we check the 'Over flow' condition using insert(num).
def insert(num):
    global rear
    if((rear-front)==9):
        print("Over flow")
    else:
        rear=rear+1
        queue[rear%10]=num
        print("Element inserted.")

#then we check the 'Under flow' condition using delete().
def delete():
    global rear,front
    if(front>rear):
        print("Under flow.")
    else:
        print(f"{queue[front%10]} removed")
        front+=1

#Now we create a queue container using numpy.
import numpy as np
rear=-1
front=0
queue=np.zeros(10,dtype='int16')
while True:
    ch=int(input('''<Insert-1> <Delete-2> <Exit-3> : '''))
    if(ch==1):
        x=int(input("Enter a number: "))
        insert(x)
    elif(ch==2):
        delete()
    elif(ch==3):
        break
    else:
        print("Error, please Enter a valid element. ")
        pass
