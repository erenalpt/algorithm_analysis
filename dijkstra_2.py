from heapq import heappop, heappush

class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
 
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with min heap
    def __lt__(self, other):
        return self.weight < other.weight
 

class Graph:
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for edge in edges:
            self.adj[edge.source].append(edge)
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


def shortest_path(graph, source, N):

    pq = []
    heappush(pq, Node(source, 0))
    dist = [float('inf')] * N
    dist[source] = 0
    done = [False] * N
    done[source] = True
    prev = [-1] * N
    route = []

    while pq:
        node = heappop(pq)
        u = node.vertex
        for edge in graph.adj[u]:
            v = edge.dest
            weight = edge.weight
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        done[u] = True
 
    for i in range(1, N):
        if i != source and dist[i] != float('inf'):
            get_route(prev, i, route)
            print(f"Path ({source} -> {i}): Minimum Cost = {dist[i]}, Route = {route}")
            route.clear()
 
 
if __name__ == '__main__':

    edges = [
		Edge(0, 1, 10), 
		Edge(0, 2, 3), 
		Edge(1, 2, 1),
        Edge(1, 3, 2), 
		Edge(2, 1, 4), 
		Edge(2, 3, 8),
        Edge(2, 4, 2), 
		Edge(3, 4, 7),
        Edge(4, 3, 9),]
 
    N = 5

    graph = Graph(edges, N)
 
    source = 0
    shortest_path(graph, source, N)