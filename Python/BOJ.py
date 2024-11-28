n, k = map(int, input().split())
floor = [0] * (k + 1)
for _ in range(n):
    f, t = input().split()
    if t == 'SAFE':
        for i in range(1, int(f) + 1):
            floor[i] = 1
    else:
        for i in range(int(f), k + 1):
            floor[i] = 2
for i in range(2, k + 1):
    if floor[i] % 2 == 0:
        res1 = i
        break
for i in range(k - 1, 0, -1):
    if floor[i] <= 1:
        res2 = i
        break
print(res1, res2)