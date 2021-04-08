class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
	 
	
class LinkedList(object):
		
	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next
	def push_at_begining(self, node):
		node.next = self.head
		self.head = node
	def push_at_ending(self, node):
		temp = self.head
		while(temp.next):
			temp = temp.next
		temp.next = node
	def append_after(self, previous_node,node):
		if previous_node is None: 
			print ("The given previous node must inLinkedList.")
			return
		node.next = previous_node.next
		previous_node.next = node
	
	def delete_key(self, position):
		temp = self.head
		if position==0:
			self.head=self.head.next
			return
		for i in range(position-1):
			temp = temp.next
			if temp is None:
				break
		if temp is None or temp.next is None:
			print("Position is greater than the length of the linked list")
			return
		temp.next = temp.next.next	
		
	def delete_linked_list(self):
		self.head = None
	
	def length_of_linked_list(self):
		length = 0
		temp = self.head
		while (temp):
			length+=1
			temp = temp.next
		return length
	
	def search(self, data):
		temp = self.head
		is_present = False
		while(temp):
			if temp.data == data:
				is_present = True
				break
			else:
				temp = temp.next
		return is_present

	def nth_node(self,n):
		temp = self.head
		if n == 0:
			return self.head
		start = 0
		while (temp):
			if start == n:
				return temp.data
			else:
				temp = temp.next
				start+=1
		if start < n:
			print('n th position is greater than length of the list')

new_linked_list = LinkedList()
a = Node(00)
b = Node(20)
c = Node(30)
new_linked_list.head = a
new_linked_list.head.next = b
#a.next = b
b.next = c

new_linked_list.push_at_begining(Node(40))
new_linked_list.push_at_ending(Node(50))
new_linked_list.append_after(a,Node(10))
#new_linked_list.printlist()
head = new_linked_list.head
new_linked_list.delete_key(5)
#new_linked_list.delete_linked_list()
head = new_linked_list.head
while (head):
	print (head.data)
	head = head.next
len = new_linked_list.length_of_linked_list()
print('Length of linked list is ', len)
is_present = new_linked_list.search(100)
print('Element present is ', is_present)
n_th_node = new_linked_list.nth_node(10)
print('Data in the N th node is ',n_th_node)