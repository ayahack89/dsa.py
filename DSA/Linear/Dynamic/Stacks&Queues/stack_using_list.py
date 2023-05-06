#DSA Stack implemantation.
#stack implementation using list.
empty= []
#Element Insert.
empty.append(1)
empty.append(2)
empty.append(3)
empty.append(4)
empty.append(5)
#Element pop.(delete)
print(empty.pop())
print(empty.pop())
print(empty.pop())
print(empty)


print()

#Stack POP - push Using recursion function.
def push(num,no):
    num.append(no)
    return num
def pop(num):
    if isEmpty(num):
        return False
    else:
        num.pop()
        return num
def isEmpty(num):
    if not num:
        return True
    else:
        return False
#Now we make our list (List implementation.)
num=[]
push(num,5)
push(num,6)
push(num,7)
pop(num)
pop(num)
print(num)


