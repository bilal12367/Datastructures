# Adjacency list representation of the graph
graph = {
    0: [(3, 6), (4, 9)],      # Node 0: edges to nodes 3 and 4 with weights
    1: [(3, 7), (4, 9)],      # Node 1: edges to nodes 3 and 4 with weights
    2: [(0, 6), (3, 6)],      # Node 2: edges to nodes 0 and 3 with weights
    3: [(0, 3), (2, 8), (4, 10)],  # Node 3: edges to nodes 0, 2, and 4 with weights
    4: [(0, 9)],              # Node 4: edge to node 0 with weight
    5: [(0, 8), (1, 8)]       # Node 5: edges to nodes 0 and 1 with weights
}

def dijkstra(graph):
    visited = dict()
    st = [0]
    while len(st) != 0:
        pop = st.pop()
        for i in graph[pop]:
            if i[0] not in visited:
                print(i)
                st.append(i[0])
                visited[i[0]] = i[1]
        
    print(visited)
    
            


    
    print(visited)
            

dijkstra(graph)