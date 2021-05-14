from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
	
    def print_graph(self):
        print (self.graph)        
        for i in self.graph.keys():
            print("{}".format(i), end="")
            for j in self.graph[i]:
                print(" -> {}".format(j), end="")
            print(" \n")
 
    def bfs(self,s):
        import pdb;pdb.set_trace()
        print(self.graph)
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        
    
    
    
g = Graph()

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,4)

"""
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
"""
g.print_graph()

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)
