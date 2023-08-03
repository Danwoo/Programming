T = int(input())
list_str = []
for _ in range(T):
  S = input().split()
  S[0] = int(S[0])
  list_str.append(S)
for str_set in list_str:
  for s in str_set[1]:
    print(str_set[0]*s, end='')
  print('')