A, B = map(str,input().split())
A = int(A[::-1])   # 문자열 뒤집기
B = int(B[::-1])   # 문자열 뒤집기
print(A if A > B else B)    # 삼항 연산자