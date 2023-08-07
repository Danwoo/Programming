import sys
A, B, V = map(int,sys.stdin.readline().split())

# 반복문을 돌리면 연산의 양이 너무 많다!!!
# day = 0
# while True:
#   day += 1
#   V -= A
#   if V <= 0:
#     print(day)
#     break
#   V += B

import math
per_day = A-B
last_remains = math.ceil((V-A)/(per_day))
print(last_remains + 1)