
from collections import deque

T = int(input())
idx_results = []

for _ in range(T):
  N, idx_point = map(int,input().split())
  priorities_order = list(map(int,input().split()))
  order = 1

  deq = deque(priorities_order) #rotate쓰기위해 자료형 덱으로 변환
  idx_deq = deque([num for num in range(N)]) #1 1 9 1 1 1 오류를 위해 인덱스까지 돌림
  value_point = deq[idx_point]
  while deq:
    if any(deq[0] < x for x in list(deq)[1:]):
      deq.rotate(-1)
      idx_deq.rotate(-1)
      
    else:
      if idx_deq[0] == idx_point:
        idx_results.append(order)
        break
      else:
        order += 1
        deq.popleft()
        idx_deq.popleft()
      

for idx in idx_results:
  print(idx)

