#Define a squre formula using the class.oop
class squre:
    def __init__(self,length):
        self.length=length
    def area(self):
        ar=((self.length)**2)
        return ar
obj=squre(int(input("Enter the length of a squre: ")))
x=obj.area()
print(x)
