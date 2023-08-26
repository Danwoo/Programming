import sys

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

# 입력 처리
N = int(sys.stdin.readline())
stack = Stack()

# 명령 처리 및 출력
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == '1':
        stack.push(int(command[1]))
    elif command[0] == '2':
        print(stack.pop())
    elif command[0] == '3':
        print(stack.size())
    elif command[0] == '4':
        print(int(stack.is_empty()))
    elif command[0] == '5':
        print(stack.top())
