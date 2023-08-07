A = []
max_num = -1
index_max = (0,0)
for i in range(9):
  input_list = [int(x) for x in input().split()]
  if max_num < max(input_list):
    max_num = max(input_list)
    index_max = (i+1,input_list.index(max_num)+1)

print(max_num)
print(index_max[0], index_max[1])