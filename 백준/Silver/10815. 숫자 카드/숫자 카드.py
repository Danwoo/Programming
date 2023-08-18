import sys
N = int(sys.stdin.readline())
N_set = set(map(int,sys.stdin.readline().split()))      # N은 둘 이상의 원소가 포함되어도 하나만 인식하면 된다.
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

output = []
for m in M_list:
    if m in N_set:
        output.append('1')
    else:
        output.append('0')

print(' '.join(output))