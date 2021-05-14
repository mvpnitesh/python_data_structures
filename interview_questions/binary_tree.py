class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
 
# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''
 
root.left      = Node(2)
root.right     = Node(3)

root.left.left  = Node(4)

root.left.right = Node(5)

