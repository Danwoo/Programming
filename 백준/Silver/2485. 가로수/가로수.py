# N개의 가로수 위치(pos)와 가로수 사이의 거리(dist)에 대한 리스트(dist_list) 생성
# 첫번째 가로수의 위치를 먼저 받고 두번째 가로수부터 거리를 연산한다.
# 가로수 사이의 거리의 최대 공약수(gcd_dist)를 통해 모든 가로수가 gcd_dist 간격이 되도록 새로 나무를 심는다.
from math import gcd

N = int(input())
pos = []
dist_list = []
mark_tree = int(input())
pos.append(mark_tree)
for _ in range(N-1):
  tree = int(input())
  pos.append(tree)
  dist_list.append(tree - mark_tree)
  mark_tree = tree

gcd_dist = dist_list[0]
for i in range(1, len(dist_list)):
  gcd_dist = gcd(gcd_dist, dist_list[i])

result = 0
for j in range(1,N):
   dist = pos[j] - pos[j-1] - 1
   result += dist // gcd_dist
  
print(result)