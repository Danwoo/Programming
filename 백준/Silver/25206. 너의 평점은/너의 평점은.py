# rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

# total = 0	# 학점 총합을 담을 변수
# result = 0	# (학점 * 과목평점) 총합을 담을 변수
# for _ in range(20) :
#     s, p, g = input().split()
#     p = float(p)
#     if g != 'P' :	# 등급이 P인 과목은 계산 안함
#         total += p
#         result += p * grade[rating.index(g)]

# print('%.6f' % (result / total))

S = input('').split()   # 전체 입력 받음

name = S[0::3]      # 과목명만 추출
for n in name:  
  S.remove(n)       # 과목명 삭제 -> 학점, 점수만 남음

score_dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}  # 학점 딕셔너리

total = 0     # (학점*과목평점)의 합
score_total = 0   # 학점의 총합

for i in range(0, len(S), 2):
    score = float(S[i])
    grade = S[i + 1]        # 2개씩 세트로 과목학점, 평점 으로 나뉘어 연산 진행
    
    if grade in score_dict:
        value = score_dict[grade]     # 딕셔너리의 key값에 해당하는 값들을 value값으로 대체
        score_total += score
    else: 
      continue                  # 딕셔너리에 없는 값(P)일때는 계산에서 제외된다.
    total += score * value
print(total/score_total)
