N, M = map(int, input().split())
a = list(map(int, input().split()))
res = []
group = cur = 0
for i in a:
    if cur + i <= M:
        cur += i
    else:
        group += 1
        cur = i
    res.append(group)
print(*res, sep = '\n')