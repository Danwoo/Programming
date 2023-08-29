real_div_cnt = int(input())
real_div_list = [int(x) for x in input().split()]

real_div_list.sort()

print(real_div_list[0] * real_div_list[-1])