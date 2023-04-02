#BST in python DSA
#BST -> Binary Search Tree....
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bstree:
    def __init__(self):
        self.root=None
    def insertroot(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.pvt_insert(data,self.root)
    def pvt_insert(self,data,node):
        if data<node.data:
            if node.left is None:
                self.left=Node(data)
            else:
                self.pvt_insert(data,node.left)
        else:
            if node.right is None:
                self.left=Node(data)
            else:
                self.pvt_insert(data,node.right)
    def search(self,node):
        if node is None:
            return False
        else:
            node.


            # Code under construction , 
        
                