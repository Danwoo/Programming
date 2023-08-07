N, M = map(int,input().split())
A = []
B = []

for n in range(N):
  input_list = [int(x) for x in input().split()]
  A.append(input_list)

for n in range(N):
  input_list = [int(x) for x in input().split()]
  B.append(input_list)

for a,b in zip(A,B):
  for c,d in zip(a,b):
    print(c+d, end=' ')
  print()