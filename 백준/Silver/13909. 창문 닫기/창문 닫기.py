# 창문이 열려있으려면 약수의 개수가 홀수개 -> 제곱수의 경우에만 홀수 개이다.

N = int(input())
cnt = 1
for _ in range(2,int(N**(1/2))+1):
  cnt += 1
print(cnt)