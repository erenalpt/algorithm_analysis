from collections import defaultdict

def build_graph(edge_list):
    graph = defaultdict(list)
    seen_edges = defaultdict(int)
    for src, dst, weight in edge_list:
        seen_edges[(src, dst, weight)] += 1
        if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
            continue
        graph[src].append((dst, weight))
        graph[dst].append((src, weight))  # remove this line of edge list is directed
    return graph


def dijkstra(graph, src, dst=None):
    nodes = []
    for n in graph:
        nodes.append(n)
        nodes += [x[0] for x in graph[n]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        u = min(q, key=dist.get)
        q.remove(u)

        if dst is not None and u == dst:
            return dist[dst], prev

        for v, w in graph.get(u, ()):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def find_path(pr, node):
    p = []
    while node is not None:
        p.append(node)
        node = pr[node]
    return p[::-1]


if __name__ == "__main__":
    edges = [
        ("A", "B", 10),
        ("A", "C", 3),
        ("B", "C", 1),
        ("B", "D", 2),
        ("C", "B", 4),
        ("C", "D", 8),
        ("C", "E", 2),
        ("D", "E", 7),
        ("E", "D", 9),
    ]

    g = build_graph(edges)

    print("=== Dijkstra ===")

    print("--- Single source, single destination ---")
    d, prev = dijkstra(g, "A", "E")
    path = find_path(prev, "E")
    print("A -> E: distance = {}, path = {}".format(d, path))

    d, prev = dijkstra(g, "A", "C")
    path = find_path(prev, "A")
    print("F -> G: distance = {}, path = {}".format(d, path))

    print("--- Single source, all destinations ---")
    ds, prev = dijkstra(g, "A")
    for k in ds:
        path = find_path(prev, k)
        print("A -> {}: distance = {}, path = {}".format(k, ds[k], path))