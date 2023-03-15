#Basic stack implementation using numpy.
#At first we check the 'Overflow' condition , to create a push(num) function.

def push(num):
#Here I use the global top to define a stack container.
     global top
     if (top==9):
          print("Over flow.")
     else:
          top=top+1
          stack[top]=num

#Then we check the 'Underflow' condition, to create a pop() function.
def pop():
     global top
     if (top==-1):
          print("Under flow.")
          return
     else:
          print(stack[top])
          top-=1

#Then we take a module 'num.py' to create a proper stack container.
import numpy as np

# The line stack=np.zeros(10, dtype='int16') creates a NumPy array called stack with 10 elements initialized to 0 and of data type int16.
# The function numpy.zeros() returns a new array of specified size and data type, filled with zeros. In this case, the size is set to 10 and the data type is set to int16. int16 is a data type that represents integers using 16 bits of memory, which means that it can store integer values from -32,768 to 32,767.
# The resulting stack array can be used to implement a stack data structure with a maximum capacity of 10 elements, where each element is a 16-bit integer.
stack=np.zeros(10,dtype='int16')
top=-1
while True:
     ch=int(input('''<Push-1> <Pop-2> <Exit-3> : '''))
     if(ch==1):
          x=int(input("Enter an element: "))
          push(x)
     elif(ch==2):
          pop()
     elif(ch==3):
          break
     else:
          print("Error,Its an invalid input. ")
          pass
              
     


