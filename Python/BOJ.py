n, a, b = map(int, input().split())
res = [0, 0, 0]
for i in range(1, n + 1):
    if i % a == i % b == 0:
        res[2] += 1
    elif i % a == 0:
        res[0] += 1
    elif i % b == 0:
        res[1] += 1
print(*res)