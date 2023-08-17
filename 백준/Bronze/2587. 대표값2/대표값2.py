num_list = []
for _ in range(5):
  N = int(input())
  num_list.append(N)

# 평균값
print(int(sum(num_list)/len(num_list)))
# 중앙값
num_list.sort()
print(num_list[5//2])