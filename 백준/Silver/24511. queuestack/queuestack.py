from collections import deque

N = int(input())
structures = list(map(int, input().split()))  # 큐(0)인지 스택(1)인지 나타내는 리스트
values = list(map(int, input().split()))      # 자료구조에 들어 있는 원소 리스트

M = int(input())
C = list(map(int, input().split()))           # 삽입할 원소들의 리스트

q = deque()  # deque 객체 생성
# 스택의 경우 - 결과값에 영향을 주지 못한다.

# 큐스택 구성 
for qs in range(N):
    if structures[qs] == 0:
        q.appendleft(values[qs])  # 큐라면 왼쪽 끝에 원소 추가

# 원소 삽입 및 출력
for i in range(M):
    q.append(C[i])              # 원소를 큐스택에 삽입
    print(q.popleft(), end=' ')  # 왼쪽에서 원소를 pop하고 출력 (리턴값)