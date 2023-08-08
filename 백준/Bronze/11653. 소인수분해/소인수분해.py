import sys
N = int(sys.stdin.readline())
divisor = 2 # 최소인 소수(divisor)
while N > 1:
    while N % divisor == 0:
        print(divisor)
        N //= divisor
    divisor += 1