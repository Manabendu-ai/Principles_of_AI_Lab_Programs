import itertools

cities = [0, 1, 2, 3]

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
min_cost = float('inf')

for path in itertools.permutations(cities):
    if path[0] == start:
        total = 0
        for i in range(len(path) - 1):
            total += cost[path[i]][path[i+1]]
        total += cost[path[-1]][start] 

        min_cost = min(min_cost, total)

print("Minimum travelling cost:", min_cost)
