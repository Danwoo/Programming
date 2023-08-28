from collections import deque

N = int(input())
# enumerate를 사용해서 인덱스(풍선순서)를 같이 처리함. 
q = deque(enumerate(map(int, input().split())))
result = []

while q:
  idx, balloon = q.popleft()
  result.append(idx + 1)
  # 풍선 안의 종이 숫자가 양수인 경우와 음수인 경우 방향이 다름
  if balloon > 0:
    q.rotate(-(balloon - 1))
  else:
    q.rotate(-balloon)

print(' '.join(map(str, result)))