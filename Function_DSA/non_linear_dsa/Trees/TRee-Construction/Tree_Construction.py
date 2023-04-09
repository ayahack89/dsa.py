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
            
            if data<previous.data:
                previous.left_son=newNode
            else:
                previous.right_son=newNode
# INOREDR = LEFT>ROOT>RIGHT;
    def inOrder(self,root):
        if root.left_son is not None:
            e.inOrder(root.left_son)
        print(root.data)
        
        if root.right_son is not None:
            e.inOrder(root.right_son)

# PREORDER = ROOT>LEFT>RIGHT;
    def preOrder(self,root):
        print(root.data)

        if root.left_son is not None:
            e.preOrder(root.left_son)
        
        if root.right_son is not None:
            e.preOrder(root.right_son)

# POSTORDER = LEFT>RIGHT>ROOT;
    def postOrder(self,root):
        if root.left_son is not None:
            e.postOrder(root.left_son)
        
        if root.right_son is not None:
            e.postOrder(root.right_son)

        print(root.data)

       

#Call-::::-
e=Tree()
a = int(input("Number of inputs:- "))
for j in range(0,a):
    e.insert(int(input("Node.Data:: ")))
print("INORDER-")
e.inOrder(e.root)
print("PREORDER-")
e.preOrder(e.root)
print("POSTOREDR-")
e.postOrder(e.root)
print("Tree constracted....")
