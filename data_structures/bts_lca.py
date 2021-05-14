class BSTNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def lca(root, a, b):
	if a <= root.data<=b or b<=root.data<= a:
		return root
	if a<root.data and b<=root.data:
		return lca(root.left,a,b)
	if a>root.data and b> root.data:
		return lca(root.right,a,b)

def printInorder(root):
	if root:
		print(root.data)
		printInorder(root.left)
		printInorder(root.right)
		
root = BSTNode(10)
root.left = BSTNode(6)
root.right = BSTNode(16)
root.left.left = BSTNode(4)
root.left.right = BSTNode(9)
root.left.right.left = BSTNode(7)
root.right.left = BSTNode(13)
root.right.right = BSTNode(20)

printInorder(root)
print('--------------')
a = lca(root,4,20)
print(a.data)