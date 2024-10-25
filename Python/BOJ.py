S = [int(input()) for _ in range(8)]
S += S[:3]
print(max([sum(S[i : i + 4]) for i in range(8)]))
