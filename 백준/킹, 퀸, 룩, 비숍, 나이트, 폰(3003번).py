chess = list(map(int,input().split()))
num = [1,1,2,2,2,8]
result = []
for i in range(len(chess)):
    err = num[i]-chess[i]
    result.append(err)
print("{}".format(" ".join(map(str, result))))