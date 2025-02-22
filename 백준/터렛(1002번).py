import math

T = int(input())
inputs = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    inputs.append((x1, y1, r1, x2, y2, r2))
results = []
for x1, y1, r1, x2, y2, r2 in inputs:
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d == 0 and r1 == r2:
        results.append(-1)
    elif d == r1 + r2 or d == abs(r1 - r2):
        results.append(1)
    elif abs(r1 - r2) < d < r1 + r2:
        results.append(2)
    else:
        results.append(0)
for result in results:
    print(result)