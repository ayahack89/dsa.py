#Sequentional Search for puthon DSA.
#At first we used a basic way to search the element.

x=[6,8,9,12,15,17,20,23,30,47]
search=int(input("1)Code-> \nEnter a element to search:"))
count=0
var=0
for i in x:
    count=count+1
    if(search==i):
        var=1
        print(f"Element found at {count} position")
if(search==0):
    print("Element not found")

print("--------")

# Now we implement the code using function.

#Then we defind a function. the function is work as loop.
#Here we write the global veriable. To define the position.
pos=-1
def searchh(arr,ser):
    i = 0

    while i<len(arr):
        if (arr[i]==ser):
            globals()['pos']=i
            return True
        i=i+1
        
    else:
        return False
 

#At first we create the main. 
arr=[4,55,23,76,89,2,11,10]
ser=int(input("2)Code-> \nEnter a element to search: "))

if searchh(arr,ser):
    print(f"Found at {pos} position")
else:
    print("Not found.")