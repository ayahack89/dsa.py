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

# Then we count the position & delete the perticular node.
    def delete_position(self,position):
        delete_node=self.head
        position = position-1
        while (position>0):
            position=position-1
            previous=delete_node
            delete_node=delete_node.address
        previous.address=delete_node.address
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address

# Call The Functions.
o=linkedList()
a=int(input("Number of inputs:- "))
for j in range(0,a):
    o.create(int(input("Node.data: ")))
position=int(input("Input a random position: "))
o.delete_position(position)
o.printList()
        
