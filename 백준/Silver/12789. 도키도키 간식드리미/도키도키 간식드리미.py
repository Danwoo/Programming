N = int(input())
waiting = list(map(int, input().split()))

stack = []
current_number = 1  # 현재 간식 받는 학생의 번호

for student in waiting:
    # 스택이 비어있지 않고, 스택의 맨 위 학생 번호가 현재 간식 받는 학생의 번호와 같으면
    # 스택의 맨 위 학생은 올바른 위치에 대기열에 들어갈 수 있으므로 스택에서 제거
    while stack and stack[-1] == current_number:
        stack.pop()
        current_number += 1
    
    # 대기열의 학생이 현재 간식 받는 학생 번호와 같으면 올바른 위치에 대기열에 들어갈 수 있으므로 스택에 추가하지 않음
    if student == current_number:
        current_number += 1
    else:
        stack.append(student)

# 대기열에 남아있는 학생들을 처리
while stack:
    if stack.pop() != current_number:
        print("Sad")
        break
    current_number += 1
else:
    print("Nice")
