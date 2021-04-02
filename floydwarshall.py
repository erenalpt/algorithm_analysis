import sys

INF = sys.maxsize


def floydWarshall(graph):
    # number of vertices in the graph
    n = len(graph)

    # dist will be the output matrix that will have the shortest distances between every pair of vertex.
    dist = [[] for i in range(n)]

    # Initialize the dist matrix as same as the input graph matrix.
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])

        for i in range(n):
            for j in range(n):
                if dist[i][j] == INF:
                    print("%7s" % ("INF"), end=' ')
                else:
                    print("%7s" % (dist[i][j]), end=' ')
            print()
    # Taking all vertices one by one and setting them as intermediate vertices
    for k in range(n):
        # Pick all vertices as source one by one.
        for i in range(n):
            # Pick all vertices as the destination for the above choosen source vertex.
            for j in range(n):
                # Update the value of dist[i][j] if k provides a shortest path from i to j
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Shortest distance for every pair of vertex.
    print('Shortest Distance between every pair of vertex:-')
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=' ')
            else:
                print("%7s" % (dist[i][j]), end=' ')
        print()


graph = [[0, 3, 8, INF, -4],
         [INF, 0, INF, 1, 7],
         [INF, 4, 0, INF, INF],
         [2, INF, -5, 0, INF],
         [INF, INF, INF, 6, 0]]

floydWarshall(graph)
