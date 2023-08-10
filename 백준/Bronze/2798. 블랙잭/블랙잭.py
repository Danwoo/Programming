from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

# combinations 함수를 사용하여 숫자들의 조합을 생성하고 합을 계산합니다.
for combination in combinations(nums, 3):
    current_sum = sum(combination)
    if current_sum <= M:
        result = max(result, current_sum)

print(result)
