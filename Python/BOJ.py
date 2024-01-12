N, M = map(int, input().split())
a = list(map(int, input().split())) + [0] * max(M - N, 0)
b = list(map(int, input().split()))
res = 0
for i in range(M):
    res = max(res, b[i] - a[i])
print(res)