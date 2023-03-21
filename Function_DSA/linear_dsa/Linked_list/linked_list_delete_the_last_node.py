#Linked List delete the last node.
# Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
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
    def delete_lastNode(self):
        delete_node=self.head
        while delete_node is not self.last:
            previous=delete_node
            delete_node=delete_node.address
        previous.address=None
        print("Deleted item",delete_node.data)
        self.last=previous
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address

#Call the functions.
o=linkedList()
a=int(input("Number of inputs:-  "))
for j in range(0,a):
    o.create(int(input("Node.data: ")))
o.delete_lastNode()
o.printList()
