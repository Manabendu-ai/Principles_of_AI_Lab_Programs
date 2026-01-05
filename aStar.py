def aStar(graph, start, goal, h):
    open_list = {start}
    closed_list = set()

    g= {}
    g[start] = 0

    parent = {}
    parent[start] = start

    while open_list:
        n = None

        for v in open_list:
            if n is None or g[v]+h[v] < g[n]+h[n]:
                n = v

        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start)
            path.reverse()
            print("Path Found: ",path)
            return
        
        for m, cost in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parent[m] = n
                g[m] = g[n] + cost

        open_list.remove(n)
        closed_list.add(n)

    print("path does not exists!")


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

aStar(graph, 'A', 'D', heuristic)

