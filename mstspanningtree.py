
class Edge:

    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class DisjointSet:

    def __init__(self, n):
        self.parent = [None] * n
        self.size = [1] * n
        for i in range(n):
            self.parent[i] = i

    def merge_set(self, a, b):

        a = self.find_set(a)
        b = self.find_set(b)

        if self.size[a] < self.size[b]:
            self.parent[a] = b
            self.size[b] += self.size[a]
        else:
            self.parent[b] = a
            self.size[a] += self.size[b]

    def find_set(self, a):

        if self.parent[a] != a:
            self.parent[a] = self.find_set(self.parent[a])

        return self.parent[a]


def kruskal(n, edges, ds):

    edges.sort(key=lambda edge: edge.weight)
    mst = []

    for edge in edges:
        set_u = ds.find_set(edge.u)
        set_v = ds.find_set(edge.v)
        if set_u != set_v:
            ds.merge_set(set_u, set_v)
            mst.append(edge)
            if len(mst) == n-1:
                break

    return sum([edge.weight for edge in mst])


if __name__ == "__main__":

    import sys
    for n_m in sys.stdin:
        n, m = map(int, n_m.split())
        ds = DisjointSet(m)
        edges = [None] * m # Create list of size <m>

        # Read <m> edges from input
        for i in range(m):
            u, v, weight = map(int, input().split())
            u -= 1
            v -= 1
            edges[i] = Edge(u, v, weight)

        print("MST weights sum:", kruskal(n, edges, ds))