N, K = map(int, input().split())
P = [input().split() for _ in range(N)]
res = []
for i in P:
    t = ''
    for j in i:
        t += j * K
    for _ in range(K):
        res.append(t)
for i in res:
    print(*i)