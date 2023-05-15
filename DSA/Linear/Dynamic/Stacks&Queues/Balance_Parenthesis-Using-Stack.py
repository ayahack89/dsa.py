import numpy
def push(n):
    global top
    if top>=9:
        return "overflow"
    else:
        top+=1
        stack.append(n)
def pop():
    global top
    if top<0:
        return "underflow"
    else:
        top-=1
        stack.pop()
x=input("enter an expression: ")
stack=[]
top=-1
found=0
for i in x:
    if i=="(":
        push("(")
    elif i==")":
        if top==-1:
            print("unbalanced!")
            found+=1
            break
        else:
            pop()
if found!=1:
    if (top!=-1):
        print("unbalanced")
    else:
        print("balanced")