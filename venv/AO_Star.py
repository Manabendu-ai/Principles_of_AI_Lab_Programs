
graph = {
    'A': [('B', 'OR'), ('C', 'OR')],
    'B': [('D', 'AND'), ('E', 'AND')],
    'C': [('F', 'AND')],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 1
}

def ao_star(node):
    if graph[node] == []:
        return heuristic[node]

    min_cost = float('inf')

    for child, node_type in graph[node]:
        cost = heuristic[node]

        if node_type == 'OR':
            cost += ao_star(child)

        elif node_type == 'AND':
            cost = heuristic[node]
            for c, _ in graph[node]:
                cost += ao_star(c)
            break

        min_cost = min(min_cost, cost)

    return min_cost


print("Minimum cost from start node A:", ao_star('A'))
