class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def sortMerge(a,b):
    if(a == None and b== None):
        return None
    res = None
    while(a != None and b != None):
        if (a.key < b.key):
            temp = a.next
            a.next =  res
            res = a
            a= temp
        else:
            temp = b.next
            b.next = res
            res = b
        b = temp
    while (a != None):
        temp = a.next
        a.next = res
        res = a
        a = temp
    while (b != None):
        temp = b.next   
        b.next = res
        res = b
        b = temp
    return res

def printList(node):
    while(node != None):
        print(node.data, end=" ")
        node = node.next

def newNode(key):

    temp = Node(key)
    temp.key = key
    temp.next = None
    return temp
    
    
a = newNode(5)
a.next = newNode(10)
a.next.next = newNode(15)
  
b = newNode(2)
b.next = newNode(3)
b.next.next = newNode(20)
  
print( "List A before merge: ")
printList(a)
  
print( "\nList B before merge: ")
printList(b)
  
# merge 2 increasing order LLs in descresing order 
res = sortMerge(a, b)
  
print("\nMerged Linked List is: ")
printList(res)