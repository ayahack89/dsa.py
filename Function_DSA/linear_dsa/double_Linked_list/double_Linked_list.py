#Double linked list........
#Structure:-
#         previous|data|next-><-previous|data|next-><-previous|data|next-><-previous|data|next
#                  A                   B                    C                      D
# Here is the basic structure of double Linked List.

#At first we create a node which is 3 part > previous,data,next.
class List:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doubleLinkedList:
    def __init__(self):
        self.head=None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            newNode.previous=self.last
            self.last.next=newNode
            self.last=newNode
    def printList(self):
        temp1=self.head
        temp2=self.last
        print("USING NEXT:-")
        while temp1 is not None:
            print(temp1.data)
            temp1=temp1.next
        print("USING PREVIOUS:-")
        while temp2 is not None:
            print(temp2.data)
            temp2=temp2.previous

#Call..........
q=doubleLinkedList()
a=int(input("Number of Inputs:- "))
for n in range(0,a):
    q.create(int(input("Node.Data >")))
print("All Data.......")
q.printList()
print("END")
    
