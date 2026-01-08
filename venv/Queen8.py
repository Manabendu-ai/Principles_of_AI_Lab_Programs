N = 8
pos = [-1] * N 

def safe(row, col):
    for i in range(row):
        if pos[i] == col or abs(pos[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            pos[row] = col
            if solve(row + 1):
                return True

    return False

solve(0)

for i in range(N):
    print("." * pos[i] + "Q" + "." * (N - pos[i] - 1))
