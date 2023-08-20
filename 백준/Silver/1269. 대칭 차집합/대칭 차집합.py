a,b = map(int,input().split())
A = set(map(int,input().split()))

B = set(map(int,input().split()))

# 대칭차집합 : (A-B) ∪ (B-A) = (A∪B) - (A∩B)
sym_diff = len(A|B) - len(A&B)
print(sym_diff)