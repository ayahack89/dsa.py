#Fibonnaci series 
# f0=0 ,f1=1
# fn=f(n-1)+f(n-2)
# 0	1	1	2	3	5	8	13	21	34	55	89	
def fibonnaci(num):
    if (num==0):
        return 0
    elif (num==1):
        return 1
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)
num = int(input("Enter a number: "))
print(fibonnaci(num))



