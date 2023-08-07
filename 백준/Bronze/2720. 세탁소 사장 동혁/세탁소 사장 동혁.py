import sys
T = int(sys.stdin.readline())

for _ in range(T):
  C = int(sys.stdin.readline())
  print(f'{C//25} {(C%25)//10} {((C%25)%10)//5} {(((C%25)%10)%5)}')