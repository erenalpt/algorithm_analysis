from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


example_graph = {
    'A': {'B': 22, 'C': 9,  'D': 12},
    'B': {'A': 22, 'C': 35, 'F': 36, 'H': 34},
    'C': {'A': 9,  'B': 35, 'D': 4,  'E':65 , 'F':42},
    'D': {'A': 12, 'C': 4,  'E': 33, 'I': 30},
    'E': {'C': 65, 'D': 33, 'F': 18, 'G': 23},
    'F': {'B': 36, 'C': 42, 'E': 18, 'G': 39, 'H': 24},
    'G': {'E': 23, 'F': 39, 'H': 25, 'I': 21},
    'H': {'B': 34, 'F': 24, 'G': 25, 'I': 19},
    'I': {'D': 30, 'G': 21, 'H': 19},
}

print(dict(create_spanning_tree(example_graph, 'F')))
