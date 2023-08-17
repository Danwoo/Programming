import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
  x, y = map(int,sys.stdin.readline().split())
  points.append((y,x))

for i in sorted(points):
  print(i[1], i[0])