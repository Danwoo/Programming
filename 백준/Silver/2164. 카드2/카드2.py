from collections import deque

N = int(input())

q = deque(range(1,N+1))

while True:
  if len(q)==1:
    print(q[0])
    break
  q.popleft()
  if len(q)==1:
    print(q[0])
    break
  q.append(q.popleft())