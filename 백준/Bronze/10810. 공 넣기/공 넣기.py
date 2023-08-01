N, M = map(int,input().split())
basket = [0 for i in range(N)]
for _ in range(M):
  i,j,k = map(int,input().split())
  for m in range(i-1,j):
    basket[m] = k
print(*basket)