T = int(input(''))
list = []
for _ in range(T):
  str = input('')
  list.append(str)

for s in list:
  print(f'{s[0]}{s[-1]}')