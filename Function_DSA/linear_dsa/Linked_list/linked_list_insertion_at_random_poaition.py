# Linked list using numpy in python.
# Intsertion at random position. 
# Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
#So atfirst we create a Linked list .

class List:
    def __init__(self,num):
        self.data=num
        self.address=None
class linkedList:
    def __init__(self):
        self.head=None
    def create(self,num):
        newNode=List(num)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode
        # So that we properly create our Linked list.
        # Now its time to create a position function(def) there I can easily add a Node.
    def insert_position(self,num,position):
        position=position-2
        newNode=List(num)
        temp=self.head
        while (position>0):
            position=position-1
            temp=temp.address
        newNode.address=temp.address
        temp.address=newNode
        # Then we print the Linked List overall.
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address
# Atlast we call the functions.
o=linkedList()
a=int(input("Number of inputs:- "))
for j in range(0,a):
    o.create(int(input("Node.Data: ")))
num=int(input("Enter a number: "))
position=int(input("Enter a random position->"))
o.insert_position(num,position)
o.printList()
    