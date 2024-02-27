R, C, ZR, ZC = map(int, input().split())
res = []
for i in [input() for _ in range(R)]:
    t = ''
    for j in range(C):
        t += i[j] * ZC
    for _ in range(ZR):
        res.append(t)
print(*res, sep = '\n')