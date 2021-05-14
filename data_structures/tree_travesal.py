class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreorder(root):
	if root:
		print(root.val),
		printPreorder(root.left)
		printPreorder(root.right)
		
def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.val),
		printInorder(root.right)
		
def printPostorder(root):
	if root:
		printPostorder(root.left)
		printPostorder(root.right)
		print(root.val),

def printReverse(root):
	global stack
	if root:
		stack.append(root.val)
		printReverse(root.left)
		printReverse(root.right)
	return stack

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is")
printPreorder(root)
print ("Inorder traversal of binary tree is")
printInorder(root)
print ("Postorder traversal of binary tree is")
printPostorder(root)
stack = []
printReverse(root)
print("Reverse order of tree is ", stack[::-1])
"""
		1
	2		3
4		5
"""