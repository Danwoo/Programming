T = int(input())

for _ in range(T):
    brackets = input()
    stack = []
    # 괄호 문자열에서 여는 괄호를 스택에 추가하고 닫는 괄호가 나오면 스택에서 여는 괄호를 빼서 짝이 맞는지 확인함.
    # 만약 스택에 여는 괄호가 없으면 바로 False, 모든 문자열을 순회하고 스택 리스트에 괄호가 남으면 False!
    is_valid = True
    
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0:
                is_valid = False
                break
            stack.pop()
    
    if len(stack) == 0 and is_valid:
        print("YES")
    else:
        print("NO")
