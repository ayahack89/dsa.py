# Linked List delete of a given Node.
# Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE

# At first we create a simple Linked List.
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
    def delete_position(self,position):
        position = position-1
        delete_node=self.head
        while (position>0):
            position=position-1
            delete_node=delete_node.address

        if self.head is None:
            print("The list is empty.")
            return print("Error")
        else:
            self.head=self.head.address
            delete_node.address=None
            return delete_node.data
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address

o=linkedList()
a=int(input("Number of inputs:- "))
for j in range(0,a):
    o.create(int(input("Node.data: ")))
position=int(input("Input a random position: "))
o.delete_position(position)
o.printList()
        
