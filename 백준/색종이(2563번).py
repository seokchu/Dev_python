grid = [[0] * 100 for _ in range(100)]

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1

S = sum(sum(row) for row in grid)

print(S)