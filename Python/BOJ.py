N, X = map(int, input().split())
res = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        res = max(res, S)
print(res)