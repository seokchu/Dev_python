T = int(input())
num = []
for i in range(T):
    n = int(input())
    num.append(n)

for _ in range(len(num)):
    for k in range(0,len(num)-1):
        if num[k] > num[k+1]:
            num[k],num[k+1] = num[k+1],num[k]
for a in num:
    print(a)