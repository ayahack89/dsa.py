# BST - (Binary Search Tree)
# Construct Binary Search Tree in basic way.
# At first we create a basic Tree.
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
            while temp is not None:
                previous=temp
                if data<temp.data:
                    temp=temp.left_son
                else:
                    temp=temp.right_son
            if data<previous.data:
                previous.left_son=newNode
            else:
                previous.right_son=newNode
    def _search(self,data,node):
        if node == None:
            return False
        elif data == node.data:
            return True
        elif data<node.data:
            return o._search(data,node.left_son)
        else:
            return o._search(data,node.right_son)

# INORDER = LEFT>ROOT>RIGHT;
    def _inorder(self,root):
        if root.left_son is not None:
            return o._inorder(root.left_son)
        
        print(root.data)

        if root.right_son is not None:
            return o._inorder(root.right_son)
        
# PREORDER = ROOT>LEFT>RIGHT;
    def _preorder(self,root):
        print(root.data)

        if root.left_son is not None:
            return o._preorder(root.left_son)

        if root.right_son is not None:
            return o._preorder(root.right_son)
         
# POSTORDER = LEFT>RIGHT>ROOT;
    def _postorder(self,root):
        if root.left_son is not None:
            return o._postorder(root.left_son)
        
        if root.right_son is not None:
            return o.postorder(root.right_son)
        
        print(root.data)



#CALL:::::::::!
o=Tree()
while True:
    a = int(input("Number of Inputs:- "))
    for k in range(0,a):
        o.insert(int(input("Node.Data:: ")))
    choice=str(input(" INORDER:[1] , \n PREORDER:[2] , \n POSTORDER:[3] \n Enter your choice: "))
    if choice == '1':
        print("INORDER-")
        o._inorder(o.root)
    elif choice == '2':
        print("PREORDER-")
        o._preorder(o.root)
    elif choice == '3':
        print("POSTORDER-")
        o._postorder(o.root)
    else:
        break
    

# CODE UNDERCONSTRACTION .....
        
        