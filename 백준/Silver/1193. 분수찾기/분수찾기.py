import sys
X = int(sys.stdin.readline())

L,k = 0,0   # L : X가 어디 줄인지 찾는 변수(Line), k : 몇번째 줄인지 찾는 변수
while X > L:
  L += k
  k += 1
if (k-1)%2==0:    # k가 짝수, 홀수 인지에 따라 분보와 분자의 위치가 바뀐다.
  print(f'{(k-(L-X)-1)}/{((L-X)+1)}')
else:
  print(f'{((L-X)+1)}/{(k-(L-X)-1)}')