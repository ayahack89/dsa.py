# Write a python function to return the higgest value of array 3 given values.
def maximum(a,b,c):
    ar = [a,b,c]
    if(a>b)and(a>c):
        return a
    elif(b>a)and(b>c):
        return b
    else:
        return c
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = maximum(a,b,c)
print(f"The maximum number is {d}")

