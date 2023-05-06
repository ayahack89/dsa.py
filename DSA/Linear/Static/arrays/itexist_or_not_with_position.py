#Check wether a given element is exist or not & defined the position.
x = [4,-2,8,9,-12,14,11,16]
a = int(input("Enter a number: "))
var = 0
count = 0
for i in x:
    count = count + 1
    if a==i:
        var = 1
        print(f"{a} exist at {count} position.")
if var==0: 
        print(f"ERROR! the number {a} is not exist in the list.")
