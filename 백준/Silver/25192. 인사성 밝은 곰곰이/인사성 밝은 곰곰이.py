N = int(input())
input_list = []
for _ in range(N):
    nick = input()
    if nick != 'ENTER':
        input_list.append(nick)
    else:
        input_list.append('|')

# 리스트를 "|"를 기준으로 나누어 세트로 만들기
sets = []
current_set = set()

for item in input_list:  # data -> input_list 수정
    if item == '|':
        if current_set:
            sets.append(current_set)
            current_set = set()
    else:
        current_set.add(item)

if current_set:
    sets.append(current_set)

# 각 세트의 길이를 계산하고 합 구하기
total_length = sum(len(s) for s in sets)

print(total_length)  # 결과 출력
