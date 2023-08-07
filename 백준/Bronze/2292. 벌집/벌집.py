import sys
N = int(sys.stdin.readline())

a, k, temp = 0, 0, 0     # a는 범위의 끝, k는 이동 카운트 수
while N > a:
  temp += k
  a = 6*temp + 1      # 점화식(a = 6*(0+1+2+...+k) + 1)
  k += 1

print(k)