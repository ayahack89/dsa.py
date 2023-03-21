#Linked List all in one .
#  Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
# Linked List is like chain.

# Atfirst we creating a basic node structure.
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
    def insert_at_front(self,num):
        temp=self.head
        newNode=List(num)
        self.head=newNode
        newNode.address=temp
    def insert_at_random_position(self,num,position):
        position=position-2
        newNode=List(num)
        while(position>0):
            position=position-1
            temp=temp.address
        newNode.addrses=temp.address
        temp.address=newNode
    def insert_at_last(self,num):
        temp=self.head
        newNode=List(num)
        self.last.address=newNode
        self.last=newNode
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address


xo=linkedList()
a=int(input("Number of inputs (That you want) :- "))
for v in range(0,a):
    xo.create(int(input("Node.data: ")))
xo.

