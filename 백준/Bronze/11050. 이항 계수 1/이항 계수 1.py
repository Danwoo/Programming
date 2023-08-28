N, K = map(int, input().split())
binary = 1

for n in range(N - K + 1, N+1):
  binary *= n
for k in range(1,K+1):
  binary /= k

print(int(binary))