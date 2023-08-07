N, B = map(str, input().split())

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
for idx,n in enumerate(reversed(N)):
  result += number.index(n) * int(B)**idx
print(result)