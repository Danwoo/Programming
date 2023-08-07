# 5개의 문자열을 입력받아 리스트로 저장
str_list = [list(input()) for _ in range(5)]

# 리스트의 가장 긴 문자열의 길이
max_len = max(len(s) for s in str_list)

# 패딩 설정
padding_value = '*'

# 패딩 추가하여 새로운 리스트를 생성
new_list = [s + [padding_value] * (max_len - len(s)) for s in str_list]

for s in zip(*new_list):    # 패딩이 추가된 리스트들을 세로로 묶어 순서대로 문자를 출력
    print(''.join(k for k in s if k != '*'), end='')    # 각 열의 패딩 값을 제외한 문자 출력
