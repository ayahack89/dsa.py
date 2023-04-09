# Tree Construction , using Inorder , Preorder , Post order;
# We build a Tree , using basic Double Linked List.
# Atfirst we create a basic Double LinkedList .
class node:
    def __init__(self,data):
        self.data=data
        self.left_son=None
        self.right_son=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newNode=node(data)
        if self.root is None:
            self.root=newNode
        else:
            temp=self.root
            while(temp!=None):
                previous=temp
                if data<temp.data:
                    temp=temp.left_son
                else:
                    temp=temp.right_son

# INOREDR = LEFT>ROOT>RIGHT;
    def inorder(self,root):
        if root.left_son is not None:
            e.inorder(root.left_son)
            print(root.data)
        
        if root.right_son is not None:
            e.inorder(root.right_son)
            print(root.data)

                
e=Tree()
a = int(input("Number of inputs:- "))
for j in range(0,a):
    e.insert(int(input("Node.Data:: ")))
e.inorder(e.root)
print("Tree constracted....")
