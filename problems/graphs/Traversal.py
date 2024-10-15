graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'I', 'J'],
    'E': ['B', 'K', 'L'],
    'F': ['B', 'M', 'N'],
    'G': ['C', 'O', 'P'],
    'H': ['C', 'Q', 'R'],
    'I': ['D', 'S', 'T'],
    'J': ['D'],
    'K': ['E'],
    'L': ['E'],
    'M': ['F'],
    'N': ['F'],
    'O': ['G'],
    'P': ['G'],
    'Q': ['H'],
    'R': ['H'],
    'S': ['I'],
    'T': ['I'],
}


def dfs(graph):
    visited = set()
    st = ['A']
    while len(st) != 0:
        pop = st.pop()
        if pop not in visited:
            visited.add(pop)
            print(pop,end=",")
            for i in graph[pop]:
                st.append(i)


def bfs(graph):
    visited = set()
    queue = ['A']
    while len(queue) != 0:
        pop = queue.pop(0)
        if pop not in visited:
            visited.add(pop)
            print(pop, end=", ")
            for i in graph[pop]:
                queue.append(i)

bfs(graph)


