origin = [1,1,2,2,2,8]    # 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
found = list(map(int, input().split()))
for i,j in zip(found,origin):
  print(j-i, end=' ')