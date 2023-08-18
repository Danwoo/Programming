import sys

N, M = map(int,sys.stdin.readline().split())
S = set()
comp = []

for _ in range(N):
  S.add(sys.stdin.readline())
for _ in range(M):
  comp.append(sys.stdin.readline())
  
count = 0
for c in comp:
    if c in S:
        count+=1
    else:
        continue

print(count)