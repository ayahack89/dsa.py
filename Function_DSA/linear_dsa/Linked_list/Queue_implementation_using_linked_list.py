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
        self.front=None
        self.rear=None
    def Insert(self,data):
        newNode=node(data)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.address=newNode
            self.rear=newNode
# Now we implement the Linked List with queue concept..... 
    def delete(self):
        if self.front is None:
            print("Empty...")
            return print("UNDERFLOW!")
        else:
            print(self.front.data)
            self.front=self.front.address
    def printnode(self):
        temp=self.front
        while temp is not None:
            print(temp.data)
            temp=temp.address

#Call.....
oc=Queue()
while True:
    choice=str(input("Insert->1 \n Delete->2 \n Enter your choice: "))
    if (choice=='1'):
        b=int(input("Number of Inputs:-"))
        for k in range(0,b):
            data=int(input("Node.Data: "))
            oc.Insert(data)
            oc.printnode()
            print("Data Inserted.....")
    elif (choice=='2'):
        oc.delete()
        oc.printnode()
        print("Data Deleted.....")

    else:
        print("ERROR")

