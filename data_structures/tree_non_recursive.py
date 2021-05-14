class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
		
def print_tree(root):
	if not root:
		return
	stack = []
	node = root
	result = []
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			result.append(node.val)
			node = node.right
	return result
import queue
def leave_in_tree(root):
	if root is None:
		return 0
	a = queue.Queue()
	a.put(root)
	node = root
	count = 0 
	import pdb;pdb.set_trace()
	while a.empty():
		node = a.get()
		if node.left is None and node.right is None:
			count = count + 1
		else:
			if node.left is not None:
				a.put(node.left)
			if node.right is not None:
				a.put(node.right)
	return count
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(print_tree(root))
print(leave_in_tree(root))