# Write a python program to check wether left parenthesis and right parenthesis are given properly....
# We implement this code using Stack.
import numpy
def push(num):
    global top
    if top==9:
        print("OVERFLOW")
    else:
        top=top+1
        stack.append(num)
def pop():
    if top==-1:
        print("UNDERFLOW")
    else:
        top=top-1
        stack.pop()
xx=str(input("Enter an element: "))
stack=[]
top=-1
found=0
for k in xx:
    if k=='(':
        push('(')
        print("BALENCED")
    elif k==')':
        if top==-1:
            found=found+1
            break
        else:
            pop()
if found!=1:
    if top!=-1:
        print("BALENCED")
    else:
        print("BALENCED")

            
        