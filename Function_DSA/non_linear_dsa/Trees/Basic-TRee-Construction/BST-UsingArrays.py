# -Binary- search tree using -Arraya-.
import numpy as np
tree=np.zeros(100,dtype='int16')
def insert(element):
    o=0
    while tree[o]!=0:
        if tree[o]>element:
            o=(2*o)+1
        else:
            o=(2*o)+2
    tree[o]=element

def preorder(root):
    if tree[root]==0:
        return 0
    else:
        print(tree[root])
        preorder((2*root)+1)
        preorder((2*root)+2)

def inorder(root):
    if tree[root]==0:
        return 0
    else:
        inorder((2*root)+1)
        print(tree[root])
        inorder((2*root)+2)

def postorder(root):
    if tree[root]==0:
        return 0
    else:
        postorder((2*root)+1)
        postorder((2*root)+2)
        print(tree[root])


'''Better Call Functions!'''
while True:
  a = int(input("Number of inputs: "))
  for k in range(0,a):
    insert(int(input("Node..Data_"))) 
  print(tree)
  print("preorder Traversal:-")
  preorder(0)
  print("inorder traversal:-")
  inorder(root=0)
  print("post order Traversal:-")
  postorder(root=0)


        
