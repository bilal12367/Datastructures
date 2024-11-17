

class WGraph:
    def __init__(self):
        self.graph = {}
        self.visited = {}
    
    def addVertice(self, node):
        self.graph[node] = {}
        self.visited[node] = False
    
    def addEdge(self, src, dest, weight = 0):
        if src not in self.graph:
            self.graph[src] = {}
        if dest not in self.graph:
            self.graph[dest] = {}
        self.graph[src][dest] = weight
        # temp = self.graph[dest]
        # temp[src] = weight
        # self.graph[dest] = temp
    
    def dfsTraverse(self,node):
        st = [node]
        visited = []
        while len(st) != 0:
            print(st)
            temp = st.pop()
            if temp not in visited:
                visited.append(temp)
                print(temp)
                for i in self.graph[temp]:
                    st.insert(0,i)
    
    def dijkstra(self, src, dest):
        minSet = {}
        for i in self.graph.keys():
            if i not in minSet:
                minSet[i] = 1e7
        minSet[src] = 0
        st = [(src, 0)]
        while len(st) != 0:
            t = st.pop()
            for i in self.graph[t[0]].keys():
                if self.graph[t[0]][i] + t[1] < minSet[i]:
                    minSet[i] = self.graph[t[0]][i] + t[1]
                    st.insert(0, (i, minSet[i]))
        print(minSet)
        return minSet[dest]

class Graph:
    def __init__(self):
        self.graph = {}
        self.graphVisited = {}
        self.count = 0
    
    def addVertice(self, node):
        self.graph[node] = []
        self.graphVisited[node] = False
        self.count += 1

    def addEdge(self, f, t):
        if f not in self.graph:
            self.addVertice(f)
        if t not in self.graph:
            self.addVertice(t)
        adjL = self.graph[f]
        adjL.append(t)
        self.graph[f] = adjL
    
    def dfsTraversal(self, node):
        if self.graphVisited[node] == False:
            self.graphVisited[node] = True
            for i in self.graph[node]:
                self.dfsTraversal(i)