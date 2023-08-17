import sys

N = int(sys.stdin.readline())
num_list = [0]*10001        # N = 0~10000

for i in range(N):
  num = int(sys.stdin.readline())
  num_list[num] += 1        # num_list[num]에 num이 들어온 개수를 count한다.

for i in range(len(num_list)):
  if num_list[i] != 0:        # num_list[i]에 숫자가 있으면
    for j in range(num_list[i]):        # num_list[i]에 num이 들어온 개수 출력
        print(i)