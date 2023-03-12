# Here, the print_numbers function takes an argument n, which is initially set to 1. The function first checks if n is less than or equal to 10. If it is, it prints the value of n and then calls itself with n+1 as the argument.

# This process continues until n reaches 11, at which point the function returns without doing anything, since the if condition is no longer true.

# When you call print_numbers(1), the function will start printing the numbers from 1 to 10 recursively.

def print_tion(num):
    if (num<=10):
        print (num)
        print_tion(num+1)
num = int(1)
print_tion(num)