S = input().upper()
dict_str = {}
for s in S:
  if s in dict_str:
    dict_str[s] += 1
  else:
    dict_str[s] = 1

common = [key for key, value in dict_str.items() if value == max(dict_str.values())]

if len(common) == 1:
  print(common[0])
else: print('?')