#Linked List all in one .
#  Structure of a Linked list look like:-
                 # NodeA->NodeB->NodeC->NodeD->NodeE
# Linked List is like chain.

# Atfirst we creating a basic node structure.
class List:
    def __init__(self,num):
        self.data=num
        self.address=None
# We linked all nodes by using its address part , to link another nodes.....
class linkedList:
    def __init__(self):
# Its our head part. 
        self.head=None
    def create(self,num):
# Then we creating a new node.
        newNode=List(num)
# If Head is Empty so we add the newnode in head value, so now newnode is our lastnode...  
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode

# Insert at front position.....
# Logic : 1)At first we secure our linkedList, [temp=self.head]
#         2)Then we creating a new node to insert. [newNode=List(num)]
#         3)Now we add the new Node in head .[self.head=neWNode]
#         4)Altimetly now new node is a head and we link the linkedList inside 
#           newNode address part ...
#            [newNode.address=temp] 
    def insert_at_front(self,num):
        temp=self.head
        newNode=List(num)
        self.head=newNode
        newNode.address=temp

#Insert at random position.....
#Logic: 1)At first we count the position..[position=position-2
#                                          while (position>0):
#                                                position=position-1]
#       2)Then we create a new node to insert....[newNode=List(num)]
#       3)Next jump the node [temp=temp.address]
#       4)Now we linked the list(temp) inside the new node's address part
#         ...[newNode.address=temp.address]
#       5)At last we linked new node node to the previous node(temp)...[temp.address=newNode] 
    def insert_at_random_position(self,num,position):
        position=position-2
        newNode=List(num)
        while(position>0):
            position=position-1
            temp=temp.address
        newNode.addrses=temp.address
        temp.address=newNode

#Insert at last position....
#Logic: 1)At first we create a new node to insert .[newNode=List(num)]
#       2)Then we linked the new node to the last node's address part...[self.last.address=newNode]
#       3)So our last node is newNode..[self.last=newNode] 
    def insert_at_last(self,num):
        newNode=List(num)
        self.last.address=newNode
        self.last=newNode

#Delete at last position.....
#Logic: 1)At first we secure the head part .. [delete_node=self.head]
#       2)Now we check the head data part , that if head is empty , so we cant delete at front position...
#         [if self.head is None:
#               print("Linked List is Empty...")
#               return print("Error")]
#       3)Else , we delete the node data & disconnect it to the head part 
#         [self.head=delete_node.address
#          delete.address=None]
#       4)Print the blank data....[return delete_node.data] 
    def delete_in_front(self):
        delete_node=self.head
        if self.head is None:
            print("Linked List is Empty.")
            return print("ERROR.")
        else:
            self.head=delete_node.address
            delete_node.address=None
            return delete_node.data
    
#Delete at random position.......
#Logic: 
    def delete_at_random_position(self,position):
        delete_node=self.head
        position = position-1
        while (position>0):
            position=position-1
            previous=delete_node
            delete_node=delete_node.address
        previous.address=delete_node.address
    def delete_lastNode(self):
        delete_node=self.head
        while delete_node is not self.last:
            previous=delete_node
            delete_node=delete_node.address
        previous.address=None
        print("Deleted item",delete_node.data)
        self.last=previous
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address


xo=linkedList()
a=int(input("Number of inputs (That you want) :- "))
for v in range(0,a):
    xo.create(int(input("Node.data: ")))
num=int(input("insert node: "))
xo.insert_at_last(num)
xo.printList()

