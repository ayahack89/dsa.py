# Queue implementation using Linked List.....
#The Queue is a concept of FIFO > First In First Out.
#Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
#We create a bsic Linked List....
class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class Queue:
    def __init__(self):
        self.head=None
    def create(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode
# Now we implement the Linked List with queue concept..... 
    def rear(self,data):
        newNode=node(data)
        if self.head is not None:
            return print("FULL")
        else:
            self.head=newNode.address
    def front(self):
        delete_node=self.head
        if self.head is None:
            print("Linked list is empty , we can't delete it.")
            return print("ERROR")
        else:
            self.head=delete_node.address

#Call....
oc=Queue()
b=int(input("Number of inputs:- "))
for k in range(0,b):
    oc.create(int(input("Node.data: ")))
choice=str(input(" Insert->1 \n Delete->2 \n Enter you choice:"))
if (choice=='1'):
    data=int(input("Insert an element: "))
    oc.rear(data)
    print("Data Inserted...")
elif (choice=='2'):
    oc.front()
    print("Data deleted...")
else:
    print("ERROR")

