
class Vertex:
    def __init__(self, node):
        self.id = node
        self.neighbors = {}
        self.visited = False
    
    def addNeighbor(self, node, weight = 0):
        self.neighbors[node] = weight

    def getAllNeighbors(self):
        return self.neighbors
    
    def setVisited(self):
        self.visited = True
    
    def getId(self):
        return self.id


class Graph:
    def __init__(self) -> None:
        self.vertices = {}
        self.verticeCount = 0
    
    def addVertice(self, node):
        self.verticeCount += 1
        self.vertices[node] = Vertex(node)
    
    def addEdge(self, fromV, toV, weight = 0):
        if fromV not in self.vertices:
            self.addVertice(fromV)
        if toV not in self.vertices:
            self.addVertice(toV)
        self.vertices[fromV].addNeighbor(self.vertices[toV], weight)
        self.vertices[toV].addNeighbor(self.vertices[fromV], weight)
    
    def traverse(self):
        for node in self.vertices:
            vertice = self.vertices[node]
            print("Current: " +vertice.id)
            for nbr in vertice.getAllNeighbors():
                print(nbr.id, end = ",")
            print("\n")
    
    def dfsTraversal(self, node):
        vertex = self.vertices[node]
        if vertex.visited == False:
            vertex.setVisited()
            print(vertex.id)
            for nbr in vertex.getAllNeighbors():
                self.dfsTraversal(nbr.id)
        else:
            return