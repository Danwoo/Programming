N = int(input())
points = []
for _ in range(N):
  x, y = map(int,input().split())
  points.append((x,y))

for i in sorted(points):
  print(i[0], i[1])