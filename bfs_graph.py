graph = {
    'A': ['B', 'E'],
    'B': ['A', 'F'],
    'C': ['F', 'G', 'D'],
    'D': ['C', 'G', 'H'],
    'E': ['A'],
    'F': ['B', 'C', 'G'],
    'G': ['F', 'C', 'D', 'H'],
    'H': ['G', 'D']
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        
        for neighbour in graph[s]:
            
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    

# Driver Code
bfs(visited, graph, 'B')
print('\n')
