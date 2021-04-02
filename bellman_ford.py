#   BellmanFord(0)
#  EX: A,B,C,D,E 5

n = 8

graph = [
        [0, 1, 5],
        [0, 4, 9],
        [0, 7, 8],
        [1, 2, 12],
        [1, 3, 15],
        [1, 7, 4],
        [2, 3, 3],
        [2, 6, 11],
        [3, 6, 9],
        [4, 5, 4],
        [4, 6, 20],
        [4, 7, 5],
        [5, 2, 1],
        [5, 6, 13],
        [7, 2, 7],
        [7, 5, 6],
        ]


def BellmanFord(src):
    dist = [float("inf") for i in range(n)]
    dist[src] = 0

    for i in range(n-1):
        for u, v, w in graph:
            if dist[u] != float("inf") and dist[u]+w < dist[v]:
                for i in range(len(dist)):
                    print(i, '\t', dist[i],)
                print("\n")
                dist[v] = dist[u]+w
               
    
    cycle = 0
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            cycle = 1
            break

    if cycle == 0:
        print('Distance from source vertex',src)
        print('Vertex \t Distance from source')
        for i in range(len(dist)):
            print(i,'\t',dist[i])

BellmanFord(0)
