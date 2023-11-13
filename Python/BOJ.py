N, L = map(int, input().split())
res = [0, 0]
for i in [len(list(filter(None, list(input().split('0'))))) for _ in range(N)]:
    if res[0] < i:
        res[0] = i
        res[1] = 1
    elif res[0] == i:
        res[1] += 1
print(*res)