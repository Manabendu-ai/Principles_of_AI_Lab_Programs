from queue import PriorityQueue

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def safe(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def heuristic(state):
    return state[0] + state[1]

def best_first_search():
    pq = PriorityQueue()
    pq.put((heuristic(start), start))
    visited = set()

    while not pq.empty():
        _, state = pq.get()

        if state == goal:
            print("Goal reached:", state)
            return

        visited.add(state)
        m, c, b = state

        for move in moves:
            if b == 1: 
                new_m = m - move[0]
                new_c = c - move[1]
                new_b = 0
            else:   
                new_m = m + move[0]
                new_c = c + move[1]
                new_b = 1

            new_state = (new_m, new_c, new_b)

            if 0 <= new_m <= 3 and 0 <= new_c <= 3:
                if safe(new_m, new_c) and new_state not in visited:
                    pq.put((heuristic(new_state), new_state))
                    print("Visiting:", new_state)

best_first_search()
