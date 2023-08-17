N, k = map(int, input().split())

score_list = list(map(int, input().split()))

score_list.sort()     # 성적 오름차순 정렬
print(score_list[-k])      # k번째 높은 점수를 추출