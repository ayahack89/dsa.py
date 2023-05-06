#Basic class programm,
#In Python, a class is a blueprint for creating objects. It defines a set of attributes and methods that the objects of that class will have.
class agnik:
    def __init__(self,sleep,walk):
        self.sleep=sleep
        self.walk=walk
    def print(self):
        print(self.sleep,self.walk)
    def sleep(self):
        print("agnik can sleep.")
    def walk(self):
        print("Agnik can walk.")
x=agnik("lazy","guint")
x.print()
