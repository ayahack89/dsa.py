#Write a python function to return the heigher value between two given values.
def higgest(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("ERROR!,please enter a positive number.")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = higgest(a,b)
print(c)