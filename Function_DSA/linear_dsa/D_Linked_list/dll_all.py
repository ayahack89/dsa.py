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
            self.last=newNode
        else:
            newNode.previous=self.last
            self.last.next=newNode
            self.last=newNode
    def insert_at_front_position(self,data):
        temp=self.head
        newNOde=List(data)
        self.head=newNOde.next
        temp.previous=newNOde
        newNOde.next=temp
    def insert_at_random_position(self,data,position):
        temp=self.head
        newNode=List(data)
        position=position-1
        while(position>0):
            position=position-1
            temp=temp.next
        newNode.previous=temp.previous
        newNode.next=temp
        temp.previous.next=newNode
        temp.previous=newNode
    def insert_at_last_position(self,data):
        newNode=List(data)
        newNode.previous=self.last
        self.last.next=newNode
        self.last=newNode
    def delete_at_front(self):
        temp=self.head
        if self.head is None:
            print("Linked List is full , can't delete it's.")
            return("ERROR")

          
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
p=D_linked_L()
a=int(input("Number of inputs: "))
for j in range(0,a):
    p.create(int(input("NOde.Data > ")))
data=int(input("Enter a data to insert: "))
position=int(input("Enter a position to insert a given node: "))
p.insert_at_front_position(data)
p.printList()
print("Data Inserted.....")
p.insert_at_random_position(data,position)
p.printList()
print("Data Inserted......")
p.insert_at_last_position(data)
p.printList()
print("Data Inserted......")
print("END")
     