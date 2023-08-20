# 1. 이름은 고유명사이므로 set함수를 통해 중복성 제거, 리스트(O(n))보다 시간복잡도(O(len))를 줄인다.
# 결과 : 틀렸습니다. -> 사전순으로 출력한다. -> 정렬함수 추가
N, M = map(int, input().split())
unheared = set()     # 듣도 못한 사람
unreported = set()   # 보도 못한 사람
for _ in range(N):
  unheared.add(input())
for _ in range(M):
  unreported.add(input())

ans = unheared & unreported
print(len(ans))
for a in sorted(ans):
  print(a)