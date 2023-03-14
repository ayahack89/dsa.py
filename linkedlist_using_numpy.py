# Linked list using numpy.
# Linked list its structure like a chain. Its different betweeen array.
# There are some benifits about linked list, like easy to bolock implement, easy to intiertion, easy to deletation.

#At first we create a node block memory. 
class node:
    def __init__(self,num):
        self.data=num
        self.address=None

#Then we linked a node with other nodes.
class linkedNodes:
    def __init__(self):
        self.head=None

#Now we create the nodes.
    def create(self,num):
        newNode=node(num) # This line is important, its returned to the previous block memory (listNode) & triger to input a data.
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode
    def printnode(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address

#Call the classes.
oop=linkedNodes()
oop.create(int(input("Enter a number: ")))
oop.create(int(input("Enter another number: ")))
print("Output:-")
oop.printnode()

