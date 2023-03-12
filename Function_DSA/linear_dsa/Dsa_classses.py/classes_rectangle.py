#Define class rectangle:
#     data member - length,berdth
#     methords - 1)def area()
#                2)def peremeter()
class rectangular:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        area=(self.length)*(self.bredth)
        print(f"The required area is {area}")
    def peremeter(self):
        peremeter=(2*(self.length+self.bredth))
        print(f"The peremeter is {peremeter}")
oop=rectangular(10,11)
a=oop.area()
b=oop.peremeter()