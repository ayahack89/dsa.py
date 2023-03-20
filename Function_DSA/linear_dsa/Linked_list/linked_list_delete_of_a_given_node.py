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
