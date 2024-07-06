M, N = map(int, input().split())
res = []
for _ in range(N):
    res.append(M % N + M // N)
    M -= res[-1]
print(f"{' '.join(map(str, sorted(res, reverse = True)))}\n{M}")