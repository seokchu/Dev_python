N,M = map(int,input().split())
matrix_A = [list(map(int,input().split())) for _ in range(N)]
matrix_B = [list(map(int,input().split())) for _ in range(N)]

sum = [[matrix_A[i][j] + matrix_B[i][j] for j in range(M)] for i in range(N)]
for row in sum:
    print(' '.join(map(str, row)))