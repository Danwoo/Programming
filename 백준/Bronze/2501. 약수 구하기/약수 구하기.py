import sys

N, K = map(int,sys.stdin.readline().split())

count = 0       # 약수의 개수를 카운트할 변수
for i in range(1,N+1):      # 1부터 반복문을 통해 약수를 카운트하여 K와 비교한다.
  if N % i == 0:
    count+=1
  if count == K:
    print(i)
    break
if count < K:           # 만약 K번째 약수가 없으면 0을 출력
  print('0')