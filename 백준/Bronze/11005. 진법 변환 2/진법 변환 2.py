# input() 대신 sys.stdin.readline()을 사용한다. -> 버퍼를 저장하기 때문에 더 빠르다.
import sys
N, B = map(int,sys.stdin.readline().split())
# N, B = map(int, input().split())

result = []

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N:
  i = N % B
  N = N // B
  result.append(i)
for r in reversed(result):
  print(number[r], end='')