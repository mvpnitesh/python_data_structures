class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data
def printList(node):
    while(node!= None):
        print(node.data, end=' ')
        node= node.next
def printReverse(node):
    while(node.next != None):
        node = node.next
    while (node!=None):
        print(node.data , end = ' ')
        node = node.prev

def push(head_ref, data):
    temp = Node(data)
    temp.data = data
    temp.prev = None
    temp.next = head_ref
    if (head_ref != None):
       head_ref.prev = temp
    head_ref = temp
    return head_ref

head = None
head = push(head, 7)

head = push(head, 1)

head = push(head, 4)


print("Created DLL is: ")
printList(head)
print("Reverse ordered DLL is: ")
printReverse(head)