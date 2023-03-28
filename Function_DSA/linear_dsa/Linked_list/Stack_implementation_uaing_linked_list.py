# Stack implementation using Linked List,.
#Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
#The Stack is a concept of LIFO > Last In First Out. 
#So this is a basic concept of Linked List...
class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newNode=node(data)
        if self.top is None:
            self.top=newNode
            self.last=newNode
        else:
            newNode.address=self.top
            self.top=newNode
    def pop(self):
        if self.top is None:
            print("Linked List is empty, can't delete it.")
            return print("ERROR")
        if self.head is None:
            print("Linked List is empty , can't delete its.")
            return print("ERROR.")
        else:
            self.top=self.top.address

#Call....
co=Stack()
choice=str(input(" Push->1 \n Pop->2 \n Enter your choice:"))
if (choice=='1'):
    a=int(input("Number of Inputs:- "))
    for j in range(0,a):
        data=int(input("Node.Data: "))
        co.push(data)
        print("Data Inserted.....")
elif (choice=='2'):
    co.pop()
    print("Data deleted.....")
else:
    print("ERROR")
