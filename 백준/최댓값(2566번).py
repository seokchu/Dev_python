matrix = [list(map(int,input().split())) for _ in range(9)]

max  = max(max(row) for row in matrix)
print(max)

for i, row in enumerate(matrix):
    if max in row:
        j = row.index(max)
        break
print(i+1,j+1)