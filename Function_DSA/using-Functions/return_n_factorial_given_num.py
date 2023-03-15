#Write a python function to return n the factorial of a given value.
# def fact(n):
#     return 1
#     if n<0:
#         print("Please enter a positive number.")
#     elif n==0:
#         print("The factorial of 0 is 1 ")
#     else:
#         for i in range(1,n+1):
#             fact = fact*1
# n = int(input("Enter a number: "))
# g = fact(n)
# print(f"The factorial of {n} is {fact}")
def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",fact(num))  
  
  
  #----------Doubt code----------#