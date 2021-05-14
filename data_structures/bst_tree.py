class BSTNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
"""
	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right
"""
def printInorder(root):
	if root:
		print(root.data)
		printInorder(root.left)
		printInorder(root.right)
def printPreorder(root):
	if root:
		printPreorder(root.left)
		print(root.data)
		printPreorder(root.right)

def find(root, data):
	current_node = root
	while current_node:
		if data==current_node.data:
			return current_node
		if data > current_node.data:
			current_node = current_node.right
		else:
			current_node = current_node.left
	return current_node

def find_minimum(root):
	current_node = root
	while current_node:
		if current_node.left is None:
			return current_node
		else:
			current_node = current_node.left

def find_maximum(root):
	current_node = root
	while current_node:
		if current_node.right is None:
			return current_node
		else:
			current_node = current_node.right

def insertNode(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.left == None:
				root.left = node
			else:
				insertNode(root.left,node)
		else:
			if root.right == None:
				root.right = node
			else:
				insertNode(root.right, node)

def deleteNode(root, data):
	current_node = root
	while current_node is not Node:
		if current_node.data == data:
			root.left = current_node.left.left
			root.right = current_node.left.right
		
		
root = BSTNode(10)
root.left = BSTNode(6)
root.right = BSTNode(16)
root.left.left = BSTNode(4)
root.left.right = BSTNode(9)
root.left.right.left = BSTNode(7)
root.right.left = BSTNode(13)
root.right.right = BSTNode(20)

printInorder(root)
a = find(root, 13)
if a:
	print(a.data," is found in the tree")
else:
	print("Element is not found")

print("Minimum element in tree is ", find_minimum(root).data)
print("Maximum element in tree is ", find_maximum(root).data)
insertNode(root,BSTNode(34))
printPreorder(root)
print("Maximum element in tree is ", find_maximum(root).data)