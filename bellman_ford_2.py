import math
from collections import defaultdict

graph = {
    'A': ['B', 'E', 'H'],
    'B': ['C', 'D', 'H'],
    'C': ['D', 'G'],
    'D': ['G'],
    'E': ['F', 'G', 'H'],
    'F': ['C', 'G'],
    'G': [],
    'H': ['C', 'F'],
}

vertex_to_idx = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

weights = {
    'A': {'B':5, 'E':9, 'H':8},
    'B': {'C':12, 'D':15, 'H':4},
    'C': {'D':3, 'G':11},
    'D': {'G': 9},
    'E': {'F':4, 'G':20, 'H':5},
    'F': {'C':1, 'G':13},
    'G': {},
    'H': {'C':7, 'F':6}
}

num_edges = 0
num_vertices = 0
reversed_graph = defaultdict(list)
for vertex, edges in graph.items():
    num_edges += len(edges)
    num_vertices += 1
    for edge in edges:
        # Reversing the graph so we can later find which
        # the vertices directly lead to a particular vertex
        reversed_graph[edge].append(vertex)

d = [[math.inf for x in range(num_vertices)] for y in range(num_edges + 1)]

d[0][vertex_to_idx['A']] = 0

for i in range(1, num_edges):
    for z in graph.keys():
        z_idx = vertex_to_idx[z]
        d[i][z_idx] = d[i-1][z_idx]

        for y in reversed_graph[z]:
            y_idx = vertex_to_idx[y]
            if d[i][z_idx] > (d[i-1][y_idx] + weights[y][z]):
                d[i][z_idx] = d[i-1][y_idx] + weights[y][z]

print()
print("The memoization table (with headers):")
header_row = ['TBD'] * num_vertices
for vertex, idx in vertex_to_idx.items():
    header_row[idx] = vertex

print(header_row)
for i in range(0, num_edges):
    print(d[i])

print()
print("Final shortest paths to each vertex:")
print(d[num_edges - 1])
