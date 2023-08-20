S = input()

str_set = set()
for s in range(len(S)):
  for k in range(s+1):
    str_set.add(S[k:s+1])

print(len(str_set))