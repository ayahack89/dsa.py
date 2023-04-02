#DLL 
#Double linked list all in one.....
class List:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class D_linked_L:
    def __init__(self):
        self.head = None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.Last=newNode
        else:
            newNode.previous=self.last
            self.last.next=newNode
            self.last=newNode
    def insert_at_front_position(self,data):
        temp=self.head
        
          
    def printList(self):
        temp1=self.head
        temp2=self.last
        print("USING NEXT > ")
        while temp1 is not None:
            print(temp1.data)
            temp1=temp1.next
        print("USING PREVIOUS > ")
        while temp2 is not None:
            print(temp2.data)
            temp2=temp2.previous



#Call.........

     