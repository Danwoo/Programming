N = int(input())

first_num = 666   
while True: 
    if '666' in str(first_num):   # 정수형 first_num을 문자형 바꿔 666이 들어 있는 조건
        N = N - 1 
        if N == 0:  
            break
    first_num = first_num + 1 
print(first_num)