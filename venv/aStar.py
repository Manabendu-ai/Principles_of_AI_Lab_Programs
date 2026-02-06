def aStar(graph, start, goal, h):
    open_list = [start]
    g = {start : 0}
    parent = {start : None}

    while open_list:
        n = open_list[0]

        for v in open_list:
            if g[v] + h[v] < g[n] + h[n]:
                n = v

        if n==goal:
            path = []
            while n:
                path.append(n)
                n = parent[n]
            print("Path: ", path[::-1])
            return

        open_list.remove(n)
        
        for m, cost in graph[n]:
            if m not in g:
                open_list.append(m)
                parent[m]=n
                g[m] = g[n]+cost

graph = {
    'A' : [('B',1), ('C', 3)],
    'B' : [('D',1)],
    'C' : [('D',1)],
    'D' : []
}

h = {'A' : 3, 'B' : 2, 'C' : 1, 'D' : 0}

aStar(graph, 'A', 'D', h)
