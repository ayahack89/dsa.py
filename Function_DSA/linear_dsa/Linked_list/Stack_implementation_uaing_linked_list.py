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
        self.head=None
    def create(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.adddress=newNode
            self.last=newNode
# Now we implement the Linked List with stack concept....
    def push(self,data):
        newNode=node(data)
        self.last.address=newNode
        self.last=newNode
    def pop(self):
        delete_node=self.head
        if self.head is None:
            print("Linked List is empty , can't delete its.")
            return print("ERROR.")
        else:
            self.head=delete_node.address


# Call...
co=Stack()
a=int(input("Number of inputs:- "))
for j in range(0,a):
    co.create(int(input("Node.data: ")))
choice=str(input(" Push->1 \n Pop->2 \n Enter your choice: "))
if (choice=='1'):
    data=int(input("Insert a element-> "))
    co.push(data)
    print("Data inserted...")
elif (choice=='2'):
    co.pop()
    print("Data deleted...")
else:
    print("ERROR")
    