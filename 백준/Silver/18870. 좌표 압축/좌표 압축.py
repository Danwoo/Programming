import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
unique_X = sorted(set(X))

num_dict = {unique_X[i] : i for i in range(len(unique_X))}

for i in X:
  print(num_dict[i], end=' ')