class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]
    def addEdge(self, u, v):
        self.adj[u].append(v)

    def countPaths(self, s ,d):
        visited = [False] * self.v 
        pathCount = [0]
        self.countpathUtils(s,d,visited,pathCount)
        return pathCount[0]
    def countpathUtils(self, u ,d, visited, pathCount):
        visited[u] =  True
        if (u == d):
            pathCount[0]+=1
        else:
            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countpathUtils(self.adj[u][i] , d, visited, pathCount)
                i+=1
        visited[u] = False
        
g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(1,3)

s = 2
d = 3
print("No of paths are ",g.countPaths(s, d))