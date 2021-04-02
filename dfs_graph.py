graph = {   
    'S': ['Z', 'W'],
    'Y': ['X'],
    'Z': ['Y', 'W'],
    'T': ['V', 'U'],
    'X': ['Z'],
    'W': ['X'],
    'V': ['W', 'S'],
    'U': ['V', 'T'],}

color = {}
pi = {}

count = {} # container for CLRS 22.4-2

d = {}
f = {}
glob_time = 0
edges = []

def DFSVisit(u):
    global glob_time
    color[u] = "gray"

    glob_time += 1
    d[u] = glob_time

    for v in graph[u]:
        print ("Exploring vertices adjacent to " + str(v))
        if color[v] == "white":
            pi[v] = u
            if v == "T":
                count[v] = 1
                color[v] = "black"
            else:
                DFSVisit(v)

        # Each time u finishes with a vertex v, add the count to vertex u
        count[u] += count[v]
    color[u] = "black"
    glob_time += 1
    f[u] = glob_time

def DFS(graph):
    global glob_time
    for u in graph:
        color[u] = "white"
        pi[u] = "nil"
        count[u] = 0
    
    for u in graph:
        print ("Starting DFS from " + str(u))
        if color[u] == "white":
            DFSVisit(u)

def create_edges(graph):
    for u in graph:
        for v in graph[u]:
            dict_m = {u:v}
            edges.append(dict_m)
    
    print (edges)

def print_edges(graph):
    for vert in edges:
        u = vert.keys()[0]
        v = vert.values()[0]

        if pi[v] == u:
            print ("Tree Edge: (" + pi[v] + ", " + v + ")")
        else:
            # v is adj to u 
            # (u, v)
            if d[u] < d[v] and d[v] < f[v] and f[v] < f[u]:
                # v is a desc of u 
                print ("Forward Edge: (" + u + ", " + v + ")")
            elif d[v] < d[u] and d[u] < f[u] and f[u] < f[v]:
                # u is a desc of v 
                print ("Back Edge: (" + u + ", " + v + ")")
            else:
                print ("Cross Edge: (" + u + ", " + v + ")")


def calc_count():
    print (count['S'])


DFS(graph)
create_edges(graph)
print("=========== Done ============")
#print_edges(graph)

print("=========== 22.4-2 ============")
calc_count()