def BinarySearch(x):
 
    low = 0
    high = len(v2) - 1
 
    while low <= high:
        mid = (low + high) // 2
 
        if v2[mid] == x:
            return mid
        elif v2[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
     
    return -1
 
# Function to make ancestors of first node
def MakeAncestorNode1(x):
 
    v1.clear()
    while x:
        v1.append(x)
        x //= 2
     
    v1.reverse()
 
# Function to make ancestors of second node
def MakeAncestorNode2(x):
 
    v2.clear()
    while x:
        v2.append(x)
        x //= 2
     
    v2.reverse()
 
# Function to find distance bewteen two nodes
def Distance():
 
    for i in range(len(v1) - 1, -1, -1):
        x = BinarySearch(v1[i])
         
        if x != -1:
            return (len(v1) - 1 - i +
                    len(v2) - 1 - x)
     
# Driver code
if __name__ == "__main__":
 
    node1, node2 = 5, 7
    v1, v2 = [], []
     
    # Find ancestors
    MakeAncestorNode1(node1)
    MakeAncestorNode2(node2)
    import pdb;pdb.set_trace()
    print("Distance between", node1,
          "and", node2, "is :", Distance())
