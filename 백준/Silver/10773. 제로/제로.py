K = int(input())
stack = []
money = 0

for _ in range(K):
    a = int(input())
    if a != 0:
        stack.append(a)
        money += a
    elif stack:
        money -= stack.pop()
print(money)