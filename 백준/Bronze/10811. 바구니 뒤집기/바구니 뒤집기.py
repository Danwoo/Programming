N, M = map(int,input().split())
basket = [i+1 for i in range(N)]
for _ in range(M):
  i,j = map(int,input().split())
  reversed_list = basket[i-1:j]
  reversed_list.reverse()   # i-1, j-1번쨰 바구니 사이를 역순으로
  basket[i-1:j] = reversed_list
print(*basket)