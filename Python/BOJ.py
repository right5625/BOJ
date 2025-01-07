A, B, C = input().split()
print(A + B + C) if A == B == C or (A == C and A != B) else print(A + B + C + A if B == C else A + B + C + B + A)