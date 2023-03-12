#Classes are like template.
#Class Human.
class human:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def print(self):
        print(self.name,self.height)
    def sleep(self):
        print("Human can sleep.")
    def walk(self):
        print("Human can walk.")
s=human("Ayanabha","5.8")
p=human("Agnik","6.1")

p.print()
s.print()
p.walk()
s.sleep()
#Or we change the oop.
p.sleep() 



    
        