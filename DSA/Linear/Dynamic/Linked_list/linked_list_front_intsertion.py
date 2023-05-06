#Intsertion at the front of a linked list.
# Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
# Conditions :-
#       1) Secure your previous head value.
#       2) Create a newNode.
#       3) Include newNode at Head position.
#       4) Now link the newNode's address part to the last head node (temp).
 
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

#Insert the front value.
    def insert_front(self,num):
        temp=self.head
        newNode=List(num)
        self.head=newNode
        newNode.address=temp

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address

oop=linkedList()
oop.create(int(input("Enter a number: ")))
oop.insert_front(int(input("Enter the number that you insert at the front position: ")))
print("Output:-")
oop.printList()
