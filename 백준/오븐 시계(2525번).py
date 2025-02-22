h, m = map(int,input().split())
t = int(input())
m += t
if h + (m//60) >= 24:
    print(h + (m//60) - 24, m%60)
else:
    print(h + (m//60),m%60)
