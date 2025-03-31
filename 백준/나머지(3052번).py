ar = []
values = 0
for i in range(10):
    n = int(input())
    values = n%42
    ar.append(values)
output = set(ar)
print(len(output))