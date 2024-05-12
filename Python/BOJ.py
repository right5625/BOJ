N, M = map(int, input().split())
res = {}
for _ in range(N):
    A = input().split()
    t = cur = 0
    for i in A[:-1]:
        if i == '.':
            cur += 1
        else:
            t = max(t, cur)
            cur = 0
    res[A[-1]] = max(t, cur)
print(len(set(res.values())))
for k, v in res.items():
    print(v, k)