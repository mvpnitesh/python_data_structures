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

def tree_max(root):
	global maxData
	if root:
		if root.val > maxData:
			maxData = root.val
		tree_max(root.left)
		tree_max(root.right)
	return maxData

def tree_min(root):
	#import pdb;pdb.set_trace()
	global minData
	if root:
		if root.val < minData:
			minData = root.val
		tree_min(root.left)
		tree_min(root.right)
	return minData
	
def find_in_tree(root, number):
	global found
	if root:
		if root.val == number:
			found = True
			return found
		return found
		find_in_tree(root.left)
		find_in_tree(root.right)
		
def find_size_tree(root):
	global size
	if root:
		size=size+1
		find_size_tree(root.left)
		find_size_tree(root.right)
	return size
	
def maxDepth(root):
	if root == None:
		return 0
	return max(maxDepth(root.left),maxDepth(root.right))+1

root = Node(10)
root.left = Node(2)
a = Node(3)
root.right = a
root.left.left = Node(4)
root.left.right = Node(5)
a.left = Node(6)
a.right = Node(7)
maxData = 0
print(tree_max(root))
minData = root.val
print(tree_min(root))
number = 10
found = False
if find_in_tree(root, number):
	print(number , " is found in the tree")
else:
	print(number , " is not found in the tree")
size = 0
print("No of elements in the tree ",find_size_tree(root))
print("The depth is ",maxDepth(root))