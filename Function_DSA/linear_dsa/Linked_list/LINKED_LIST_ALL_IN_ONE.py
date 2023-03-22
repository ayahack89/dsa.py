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
#Logic: 1)At first we count the position...[position=position-2
#                                           while(position>0):
#                                                 position=positon-1]
#       2)Next we secure the head value...[delete_node=self.head]             
#       3)Then we secure the previous node in a previous variable & linked the temp node...
#         [previous=delete_node]
#       4)Now we jump the node..[delete_node=delete_node.address]
#       5)At last we applied the main logic , we linked the delete node address part inside 
#         the previous node........[previous.address=delete_node.address]   
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
    def max_element_found(self):
        maximum=self.head.data
        temp=self.head
        while temp is not None:
            if temp.data>maximum:
                maximum=temp.data
            temp=temp.address
        print(f"The maximum element found at {maximum}")
    def min_element_found(self):
        minimum=self.head.data
        temp=self.head
        while temp is not None:
            if (temp.data<minimum):
                minimum=temp.data
            temp=temp.address
        print(f"The minimum element found at {minimum}")
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address
xo=linkedList()
choice=str(input(" Choice->1 \n Choice->2 \n Choice->3 \n Choice->4 \n Choice->5 \n Choice->6 \n Choice->7 \n Choice->8 \n Choice->9 \n Enter your choice: "))
if (choice=='1'):
    print("All cvalue of Linked list....")
    p=int(input("Number of Inputs:-"))
    for s in range(0,p):
        xo.create(int(input("Node.Data > ")))
    xo.printList()
    print("All Values of linked list...")
elif (choice=='2'):
    print("Insert a node at first position...")
    a=int(input("Number of Inputs:-"))
    for j in range(0,a):
        xo.create(int(input("Node.Data > ")))
    num=int(input("Insert a node: "))
    xo.insert_at_front()
elif (choice=='3'):
    print("Insert at random position...")
    b=int(input("Number of Inputs: "))
    for h in range(0,b):
        xo.create(int(input("Node.Data > ")))
    num=int(input("Insert a node: "))
    position=int(input("Enter your position_: "))
    xo.insert_at_random_position(num,position)
elif (choice=='4'):
    print("Insert at last position... ")
    c=int(input("Number of Inputs: "))
    for i in range(0,c):
        xo.create(int(input("Node.Data > ")))
    num=int(input("Insert a node: "))
    xo.insert_at_last()
elif (choice=='5'):
    print("Delete at first position.....")
    d=int(input("Number of Inputs: "))
    for l in range(0,d):
        xo.create(int(input("Node.Data > ")))
    xo.delete_in_front()
elif (choice=='6'):
    print("Delete at random position....")
    e=int(input("Number of Inputs: "))
    for m in range(0,e):
        xo.create(int(input("Node.Data > ")))
    position=int(input("Enter your position_: "))
    xo.delete_at_random_position(position)
elif (choice=='7'):
    print("Delete at last position....")
    f=int(input("Number of Inputs: "))
    for n in range(0,f):
        xo.create(int(input("Node.Data > ")))
    xo.delete_lastNode()
elif (choice=='8'):
    print("Find the maximum value......")
    g=int(input("Number of Inputs: "))
    for u in range(0,g):
        xo.create(int(input("Node.Data > ")))
    xo.max_element_found()
elif (choice=='9'):
    print("Find the minimum value......")
    k=int(input("Number of Inputs: "))
    for w in range(0,k):
        xo.create(int(input("Node.Data > ")))
    xo.min_element_found()
else:
    print("ERROR.")

    
    






#CODE UNDERCONSTRACTION >>>>>>>.