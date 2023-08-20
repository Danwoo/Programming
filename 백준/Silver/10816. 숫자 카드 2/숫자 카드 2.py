# 1. count 함수를 사용하니 시간 초과
# 이유 : count 함수는 시간복잡도가 O(n)이다. 즉 for문과 같은 역할을 하기 때문에 이중 for문으로 시간복잡도가 O(N^2)이 된다.
# 2. Counter 클래스 사용 : Counter를 n번 하면 시간 복잡도가 O(n)이다.
# 이유 : 딕셔너리에서 원소를 접근하기 때문에 시간복잡도가 O(1)이기 때문
# 그러나 Counter를 사용하면 M_list에 대해 없는 원소에 대한 카운트가 안되므로 추가적인 연산이 필요하다.
# 3. 딕셔너리 사용하여 개수를 반환
# 이유 : python은 정렬함수가 내장되어 빠르게 결과를 도출가능하다.
N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))

count = {}
for n in N_list:
  if n in count:
    count[n] += 1
  else:
    count[n] = 1

for m in M_list:
  if m in count:
    print(count[m], end=' ')
  else:
    print(0, end=' ')