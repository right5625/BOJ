S, D, I, L, N = map(int, input().split())
print(max(N * 4 - (S + D + I + L), 0))