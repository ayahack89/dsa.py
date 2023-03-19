# Linked Liist deletetion from front position.
# # Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
# To delete a node from the front of a linked list in Python, you can follow these steps:

# 1) Check if the linked list is empty. If it is empty, return an error or do nothing.
# 2)If the linked list is not empty, set the head of the linked list to the next node of the current head.
# 3)Return the value of the deleted node.
# 4)Here's a sample implementation:

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
    def delete_in_front(self):
        delete_node=self.head
        if self.head is None:
            print("Linked List is Empty.")
            return print("ERROR.")
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
i=int(input("Number of inputs:- "))
for  a in range(0,i):
    o.create(int(input("Node: ")))
o.delete_in_front()
o.printList()

