N = int(input())

num, deno,count,max_number,sum,index = 1, 1, 1, 1, 1, 1
while N > max_number:
    count += 1
    max_number += count

sum = count + 1
index = N - (max_number - count)

if sum % 2 != 0:
    num = index
    deno = sum - num
    print("{}/{}".format(num,deno))
else:
    num = sum - index
    deno = sum - num
    print("{}/{}".format(num,deno))