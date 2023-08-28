T = int(input())

def factorial(N):
  result = 1
  for n in range(1, N+1):
    result *= n
  return result

# combination
for _ in range(T):
  N, M = map(int,input().split())
  print(int(factorial(M)/(factorial(N)*factorial(M-N))))