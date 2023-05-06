# In this implementation, the sum_numbers function takes an argument n, which is the number we want to find the summation up to. If n is 1, the function returns 1, which is the base case of the recursion. If n is not 1, the function returns n plus the recursive call to sum_numbers(n-1).
def summation(num):
    if (num==1):
        return 1
    else:
        return num + summation(num-1)
num = int(input("Enter a number: "))
print(summation(num))