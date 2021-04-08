class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
	 
	
class LinkedList(object):
		
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev
		
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
		
	def swap_numbers(self):
		temp = self.head
		while(temp is not None and temp.next is not None):
			if temp.data == temp.next.data:
				temp = temp.next.next
			else:
				temp.data,temp.next.data = temp.next.data,temp.data
				temp = temp.next.next
	
	def print_list(self):
		head = new_linked_list.head
		while (head):
			print (head.data)
			head = head.next
	
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
new_linked_list.print_list()
print("after reverse")
new_linked_list.reverse()
new_linked_list.print_list()
new_linked_list.swap_numbers()
print("After Swapping")
new_linked_list.print_list()