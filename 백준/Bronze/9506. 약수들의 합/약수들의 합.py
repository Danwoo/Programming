# 완전수 : 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같은 수
# Ex) 6 = 1 + 2 + 3

import sys

def perfect_num(n):
  num_list = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      num_list.append(i)
      num_list.append(n // i)
  num_list.remove(n)
  num_list.sort()
  if sum(num_list) == n:
    print(f"{n} = {' + '.join(map(str, num_list))}")
  else: print(f'{n} is NOT perfect.')
  
while True:
  N = int(sys.stdin.readline())
  if N == -1:
      break
  perfect_num(N)    