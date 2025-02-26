N,M = map(int,input().split())
ar = []
for a in range(1,N+1):
    ar.append(a)
for b in range(M):
    i,j = map(int,input().split())
    ar[i-1:j] = reversed(ar[i-1:j])
output = ' '.join(map(str, ar))
print(output)