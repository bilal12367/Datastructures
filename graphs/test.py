from GraphAdjList import WGraph


if __name__ == '__main__':
    g = WGraph()
    
    g.addVertice(0)
    g.addVertice(1)
    g.addVertice(2)
    g.addVertice(3)
    # g.addVertice(4)
    # g.addVertice(5)

    # g.addEdge(0,1,3)
    # g.addEdge(0,3,7)
    # g.addEdge(0,4,8)
    # g.addEdge(4,3,3)
    # g.addEdge(1,2,1)
    # g.addEdge(1,3,4)
    # g.addEdge(3,2,2)
    # g.addEdge(2,5,2)

    # g.addEdge(0,1,4)
    # g.addEdge(0,2,2)
    # g.addEdge(2,1,1)
    # g.addEdge(1,0,3)
    # g.addEdge(1,2,5)
    # g.addEdge(1,3,2)
    # g.addEdge(3,4,2)
    # g.addEdge(4,5,6)
    # g.addEdge(1,4,1)
    # g.addEdge(0,3,1)
    
    g.addEdge(0,1,10)
    g.addEdge(0,3,1)
    g.addEdge(3,2,0)
    g.addEdge(1,2,10)
    g.addEdge(3,4,1)
    g.addEdge(4,2,1)



    # g.dfsTraverse(0)
    print(g.dijkstra(0, 2))


