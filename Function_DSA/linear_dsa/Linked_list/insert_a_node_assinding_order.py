# Insert a node in asccinding order......
class node:
    def __init__(self,data):
       self.data=data
       self.address=None
class linkedList:
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
    def insert_in_order(self,data):
        temp=self.head
        previous=None
        while data>temp.data:
            previous=temp
        temp=temp.address
        if previous==None:
            newNode=node(data)
            newNode.address=self.head
            self.head=newNode
        else:
            previous.address=newNode.address
            newNode.address=temp
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp = temp.address
        

#Call.........
o=linkedList()
a=int(input("Number of Inputs:-"))
for r in range(0,a):
    o.create(int(input("Node.Data- ")))
data=int(input("Enter a node to insert: "))
o.insert_in_order(data)
print("ALL DATA INSERTED IN ASCCENDING ORDER.")
o.printList()
print("END")