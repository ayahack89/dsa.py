# In this implementation, the sum_range function takes two arguments lower and upper, which represent the lower and upper bounds of the range, respectively. The function first checks if lower is greater than upper. If it is, the function returns 0, which is the base case of the recursion. If lower is not greater than upper, the function returns lower plus the recursive call to sum_range(lower+1, upper).
def sum_range(lower , upper):
    if (lower==upper):
        return upper
    else:
        return (lower + sum_range(lower+1 , upper))
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
print(f"Sum of range is {sum_range(lower , upper)}")   
